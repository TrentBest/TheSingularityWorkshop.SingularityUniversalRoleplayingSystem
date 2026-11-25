"""Tests for MicroBundle record selection and deterministic view resolution."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import validate_surps_ontology_views as ontology


class OntologyViewTests(unittest.TestCase):
    def setUp(self):
        self.bundle = {"id": "surps.microbundle.sample", "version": "0.1.0",
                       "status": "draft", "ownerRepository": "owner/repo",
                       "contentPath": ".surps/sample.json",
                       "recordCollections": ["capabilities", "rules"]}
        self.payload = {"contributions": {
            "capabilities": [{"id": "sample.capability.observe", "name": "Observe"}],
            "rules": [{"id": "sample.rule.resolve", "name": "Resolve"}]}}
        self.view = {"id": "surps.view.sample", "version": "0.1.0",
                     "bookId": "surps.book.sample", "audience": "player",
                     "scope": "test", "lod": 0,
                     "selections": [{"microbundle": "surps.microbundle.sample",
                                     "records": ["sample.capability.observe", "sample.rule.resolve"]}]}

    def test_resolves_selected_records_with_collection_and_provenance(self):
        errors = []
        result = ontology.resolve_view(self.bundle, self.payload, self.view, errors)
        self.assertEqual([], errors)
        self.assertEqual(2, len(result["records"]))
        self.assertEqual("capabilities", result["records"][0]["collection"])
        self.assertEqual("surps.microbundle.sample", result["sources"][0]["microbundle"])

    def test_unresolved_record_fails_closed(self):
        self.view["selections"][0]["records"].append("missing.record")
        errors = []
        ontology.resolve_view(self.bundle, self.payload, self.view, errors)
        self.assertTrue(any("unresolved record" in error for error in errors))

    def test_duplicate_selection_is_rejected(self):
        self.view["selections"][0]["records"].append("sample.rule.resolve")
        errors = []
        ontology.resolve_view(self.bundle, self.payload, self.view, errors)
        self.assertTrue(any("selected more than once" in error for error in errors))

    def test_unresolved_bundle_is_rejected(self):
        self.view["selections"][0]["microbundle"] = "missing.bundle"
        errors = []
        ontology.resolve_view(self.bundle, self.payload, self.view, errors)
        self.assertTrue(any("unresolved MicroBundle" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
