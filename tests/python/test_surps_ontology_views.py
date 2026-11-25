"""Tests for multi-MicroBundle selection, identity, and view resolution."""
from __future__ import annotations
import sys, unittest
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

    def test_missing_required_dependency_is_rejected(self):
        self.bundles["surps.microbundle.sample"][0]["dependencies"] = [{"id": "missing.dependency"}]
        errors = []
        ontology.validate_bundle_graph(self.bundles, errors)
        self.assertTrue(any("unresolved required MicroBundle dependency" in error for error in errors))

if __name__ == "__main__":
    unittest.main()
