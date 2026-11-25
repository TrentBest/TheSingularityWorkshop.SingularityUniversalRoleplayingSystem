from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import generate_surps_character_catalog as catalog


class CharacterCatalogTests(unittest.TestCase):
    def write_json(self, root: Path, relative: str, value) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def make_repository(self, root: Path, *, content=None, descriptor_overrides=None, registry_overrides=None):
        content = content or {
            "capabilities": [{"id": "surps.core.observe", "name": "Observe"}],
            "rules": [{"id": "surps.core.resolution", "name": "Resolution"}],
        }
        descriptor = {
            "id": "surps.microbundle.core",
            "version": "0.1.0",
            "ownerRepository": "owner/surps",
            "contentPath": ".surps/microbundles/content/core.json",
            "recordCollections": ["capabilities", "rules"],
        }
        descriptor.update(descriptor_overrides or {})
        registry = {
            "repository": "owner/surps",
            "microbundles": [{"id": "surps.microbundle.core", "path": ".surps/microbundles/core.json"}],
        }
        registry.update(registry_overrides or {})
        self.write_json(root, ".surps/microbundles/registry.json", registry)
        self.write_json(root, ".surps/microbundles/core.json", descriptor)
        self.write_json(root, descriptor["contentPath"], content)

    def test_catalog_projects_only_registered_character_collections_with_provenance(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root)
            result = catalog.build_catalog(root)
            self.assertEqual(["surps.core.observe"], [r["id"] for r in result["collections"]["capabilities"]])
            self.assertEqual([], result["collections"]["traits"])
            self.assertEqual("surps.microbundle.core", result["collections"]["capabilities"][0]["source"]["microbundleId"])
            self.assertEqual("0.1.0", result["collections"]["capabilities"][0]["source"]["microbundleVersion"])
            self.assertEqual("owner/surps", result["collections"]["capabilities"][0]["source"]["ownerRepository"])

    def test_duplicate_ids_across_different_collections_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root, content={
                "capabilities": [{"id": "same.record"}],
                "rules": [{"id": "same.record"}],
            })
            with self.assertRaisesRegex(ValueError, "duplicate canonical record ID"):
                catalog.build_catalog(root)

    def test_registry_and_descriptor_owner_must_match(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root, descriptor_overrides={"ownerRepository": "other/repo"})
            with self.assertRaisesRegex(ValueError, "ownerRepository"):
                catalog.build_catalog(root)

    def test_registry_descriptor_identity_must_match(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root, descriptor_overrides={"id": "other.bundle"})
            with self.assertRaisesRegex(ValueError, "identity mismatch"):
                catalog.build_catalog(root)

    def test_registry_paths_cannot_escape_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root, registry_overrides={
                "microbundles": [{"id": "surps.microbundle.core", "path": "../outside.json"}]
            })
            with self.assertRaisesRegex(ValueError, "escapes the repository"):
                catalog.build_catalog(root)

    def test_invalid_collection_shape_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_repository(root, content={"capabilities": {"not": "an array"}})
            with self.assertRaisesRegex(ValueError, "must be an array"):
                catalog.build_catalog(root)


if __name__ == "__main__":
    unittest.main()
