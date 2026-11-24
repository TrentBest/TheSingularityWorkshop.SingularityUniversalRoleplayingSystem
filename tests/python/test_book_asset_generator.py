"""Focused tests for the descriptor-driven SURPS publication generator."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import generate_surps_book_assets as generator


class BookAssetGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.original_root = generator.ROOT
        generator.ROOT = self.root
        (self.root / "docs" / "books").mkdir(parents=True)
        (self.root / "docs" / "assets").mkdir(parents=True)
        self.source = self.root / "docs" / "books" / "sample.md"
        self.source.write_text(
            "# Singularity Universal Roleplaying System - Core - LOD 0 - Sample\n",
            encoding="utf-8",
        )
        (self.root / "docs" / "books" / "art.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg"><title>Sample art</title></svg>',
            encoding="utf-8",
        )
        (self.root / "docs" / "assets" / "lod.svg").write_text(
            '<svg xmlns="http://www.w3.org/2000/svg"><title>LOD 0</title></svg>',
            encoding="utf-8",
        )
        self.descriptor_path = self.root / "docs" / "books" / "sample.book.json"
        self.book = {
            "schemaVersion": 1,
            "id": "surps.core.sample",
            "category": "Core",
            "lod": 0,
            "title": "Sample",
            "version": "0.1.0",
            "publisher": "The Singularity Workshop",
            "publisherMoniker": "https://example.com/moniker.svg",
            "coverArtwork": "docs/books/art.svg",
            "cover": "docs/books/cover.svg",
            "lodBadge": "docs/assets/lod.svg",
            "acknowledgementsPath": "docs/books/ack.md",
            "provenance": {
                "sourceRepository": "example/repository",
                "sourcePath": "docs/books/sample.md",
                "artworkLicense": "Test-only fixture",
            },
        }
        self.descriptor_path.write_text(json.dumps(self.book), encoding="utf-8")

    def tearDown(self):
        generator.ROOT = self.original_root
        self.temp.cleanup()

    def test_repository_paths_cannot_escape_root(self):
        with self.assertRaises(ValueError):
            generator.resolve_repo_path("../outside.txt", "test path")

    def test_absolute_paths_are_rejected(self):
        with self.assertRaises(ValueError):
            generator.resolve_repo_path(str(self.root / "outside.txt"), "test path")

    def test_descriptor_requires_canonical_source_heading(self):
        self.book["title"] = "Different"
        self.descriptor_path.write_text(json.dumps(self.book), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "first H1 must equal"):
            generator.read_descriptor(self.descriptor_path)

    def test_cover_uses_descriptor_identity_and_provenance(self):
        cover = generator.render_cover(self.book, self.descriptor_path)
        self.assertIn(self.book["publisherMoniker"], cover)
        self.assertIn("Asset role: book-cover", cover)
        self.assertIn("sourceRepository: example/repository", cover)
        self.assertIn("TheSingularityWorkshop.png", cover)
        self.assertIn("Sample", cover)


if __name__ == "__main__":
    unittest.main()
