"""Tests for SURPS contribution identity and selectable-record integrity."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import validate_surps_book_schemas as validator


class ContributionIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.contribution = {
            "book": {"id": "surps.core.sample", "version": "0.1.0"},
            "contributions": {
                "capabilities": [{"id": "surps.core.sample.capability.observe"}],
                "rules": [{"id": "surps.core.sample.rule.resolve"}],
            },
        }
        self.descriptor = {"id": "surps.core.sample", "version": "0.1.0"}
        self.manifest_book = {"id": "surps.core.sample", "version": "0.1.0"}
        self.errors = []

    def validate(self):
        validator.validate_contribution_integrity(
            self.contribution,
            self.descriptor,
            self.manifest_book,
            ".surps/contributions/sample.json",
            self.errors,
        )

    def test_matching_book_identity_is_accepted(self):
        self.validate()
        self.assertEqual([], self.errors)

    def test_contribution_identity_must_match_descriptor(self):
        self.contribution["book"]["id"] = "surps.other.book"
        self.validate()
        self.assertTrue(any("contribution book.id" in error for error in self.errors))

    def test_descriptor_identity_must_match_participation_manifest(self):
        self.descriptor["version"] = "0.2.0"
        self.validate()
        self.assertTrue(any("descriptor version" in error for error in self.errors))

    def test_record_ids_must_be_unique_across_collections(self):
        self.contribution["contributions"]["rules"][0]["id"] = (
            "surps.core.sample.capability.observe"
        )
        self.validate()
        self.assertTrue(any("duplicate contribution id" in error for error in self.errors))


if __name__ == "__main__":
    unittest.main()
