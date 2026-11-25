"""Tests for multi-MicroBundle selection, identity, and view resolution."""
from __future__ import annotations
import copy, sys, unittest
from unittest.mock import patch
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import validate_surps_ontology_views as ontology

def bundle(identifier, collection, records):
    return ({"id": identifier, "version": "0.1.0", "status": "draft",
             "ownerRepository": "owner/repo", "contentPath": ".surps/sample.json",
             "recordCollections": [collection]},
            {"contributions": {collection: records}})

class OntologyViewTests(unittest.TestCase):
    def setUp(self):
        self.bundles = {
            "surps.microbundle.sample": bundle("surps.microbundle.sample", "capabilities",
                [{"id": "sample.capability.observe", "name": "Observe"}]),
            "physics.microbundle.sample": bundle("physics.microbundle.sample", "rules",
                [{"id": "physics.rule.gravity", "name": "Gravity"}])}
        self.view = {"id": "surps.view.sample", "version": "0.1.0",
                     "bookId": "surps.book.sample", "audience": "player",
                     "scope": "test", "lod": 0, "selections": [
                         {"microbundle": "surps.microbundle.sample", "records": ["sample.capability.observe"]},
                         {"microbundle": "physics.microbundle.sample", "records": ["physics.rule.gravity"]}]}

    def test_composes_records_from_multiple_bundles(self):
        errors = []
        result = ontology.resolve_view(self.bundles, self.view, errors)
        self.assertEqual([], errors)
        self.assertEqual(2, len(result["records"]))
        self.assertEqual(2, len(result["sources"]))
        self.assertEqual("physics.microbundle.sample", result["records"][1]["sourceMicrobundle"])

    def test_resolves_book_independent_microbundle_content(self):
        self.bundles["surps.microbundle.sample"] = (
            self.bundles["surps.microbundle.sample"][0],
            {"schemaVersion": 1, "capabilities": [{"id": "sample.capability.observe", "name": "Observe"}]})
        errors = []
        result = ontology.resolve_view(self.bundles, self.view, errors)
        self.assertEqual([], errors)
        self.assertEqual(2, len(result["records"]))

    def test_same_canonical_records_can_back_distinct_audience_views(self):
        player = copy.deepcopy(self.view)
        player["audience"] = "player"
        referee = copy.deepcopy(self.view)
        referee["id"] = "surps.view.sample.game-master"
        referee["audience"] = "game-master"
        errors = []
        player_projection = ontology.resolve_view(self.bundles, player, errors)
        referee_projection = ontology.resolve_view(self.bundles, referee, errors)
        self.assertEqual([], errors)
        self.assertEqual(
            [item["record"]["id"] for item in player_projection["records"]],
            [item["record"]["id"] for item in referee_projection["records"]])
        self.assertEqual("player", player_projection["view"]["audience"])
        self.assertEqual("game-master", referee_projection["view"]["audience"])

    def test_unresolved_record_fails_closed(self):
        self.view["selections"][0]["records"].append("missing.record")
        errors = []
        ontology.resolve_view(self.bundles, self.view, errors)
        self.assertTrue(any("unresolved record" in error for error in errors))

    def test_duplicate_selection_is_rejected(self):
        self.view["selections"][0]["records"].append("sample.capability.observe")
        errors = []
        ontology.resolve_view(self.bundles, self.view, errors)
        self.assertTrue(any("selected more than once" in error for error in errors))

    def test_unresolved_bundle_is_rejected(self):
        self.view["selections"][0]["microbundle"] = "missing.bundle"
        errors = []
        ontology.resolve_view(self.bundles, self.view, errors)
        self.assertTrue(any("unresolved MicroBundle" in error for error in errors))

    def test_global_record_identity_collision_is_rejected(self):
        self.bundles["physics.microbundle.sample"][1]["contributions"]["rules"][0]["id"] = "sample.capability.observe"
        errors = []
        ontology.validate_bundle_graph(self.bundles, errors)
        self.assertTrue(any("global local-registry ID collision" in error for error in errors))

    def test_preview_manifest_resolves_multiple_owned_previews(self):
        descriptor = {"id": "surps.microbundle.sample",
                      "previewsPath": ".surps/previews/sample-manifest.json",
                      "previewsSchema": "schemas/action-preview-manifest.schema.json"}
        manifest = {"microbundleId": "surps.microbundle.sample",
                    "previews": [{"id": "surps.preview.sample",
                                  "path": ".surps/previews/sample.json"},
                                 {"id": "surps.preview.second",
                                  "path": ".surps/previews/second.json"}]}
        preview = {"id": "surps.preview.sample", "microbundleId": "surps.microbundle.sample"}
        second = {"id": "surps.preview.second", "microbundleId": "surps.microbundle.sample"}
        errors = []
        with patch.object(ontology, "validate_schema", side_effect=[manifest, preview, second]):
            ontology.validate_preview_manifest(descriptor, errors)
        self.assertEqual([], errors)

    def test_preview_descriptor_rejects_foreign_microbundle_identity(self):
        descriptor = {"id": "surps.microbundle.sample",
                      "previewsPath": ".surps/previews/sample-manifest.json",
                      "previewsSchema": "schemas/action-preview-manifest.schema.json"}
        manifest = {"microbundleId": "surps.microbundle.sample",
                    "previews": [{"id": "surps.preview.sample",
                                  "path": ".surps/previews/sample.json"}]}
        preview = {"id": "surps.preview.sample", "microbundleId": "other.microbundle"}
        errors = []
        with patch.object(ontology, "validate_schema", side_effect=[manifest, preview]):
            ontology.validate_preview_manifest(descriptor, errors)
        self.assertTrue(any("microbundleId does not match descriptor" in error for error in errors))

    def test_preview_path_requires_schema(self):
        errors = []
        ontology.validate_preview_manifest(
            {"id": "surps.microbundle.sample", "previewsPath": ".surps/previews/sample.json"},
            errors)
        self.assertTrue(any("previewsPath requires previewsSchema" in error for error in errors))

    def test_missing_required_dependency_is_rejected(self):
        self.bundles["surps.microbundle.sample"][0]["dependencies"] = [{"id": "missing.dependency"}]
        errors = []
        ontology.validate_bundle_graph(self.bundles, errors)
        self.assertTrue(any("unresolved required MicroBundle dependency" in error for error in errors))

if __name__ == "__main__":
    unittest.main()
