from __future__ import annotations

import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SVG_NS = "{http://www.w3.org/2000/svg}"


class LivingSurfaceAssetTests(unittest.TestCase):
    def _validate_catalog(self, relative_path: str, collection: str) -> dict:
        path = ROOT / relative_path
        catalog = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(1, catalog["schemaVersion"])
        ids = set()
        for item in catalog[collection]:
            with self.subTest(asset=item["id"]):
                self.assertNotIn(item["id"], ids)
                ids.add(item["id"])
                asset = ROOT / item["asset"]
                self.assertTrue(asset.is_file(), f"Missing asset: {asset}")
                root = ET.parse(asset).getroot()
                self.assertEqual("svg", root.tag.removeprefix(SVG_NS))
                self.assertTrue(root.find(f"{SVG_NS}title") is not None)
                self.assertTrue(root.find(f"{SVG_NS}desc") is not None)
                self.assertTrue(root.attrib.get("viewBox"))
        return catalog

    def test_map_templates_are_empty_accessible_svg_surfaces(self) -> None:
        catalog = self._validate_catalog("docs/assets/maps/catalog.json", "templates")
        self.assertEqual(
            {"surps.map.world.blank", "surps.map.region.blank", "surps.map.encounter.blank"},
            {item["id"] for item in catalog["templates"]},
        )
        for item in catalog["templates"]:
            root = ET.parse(ROOT / item["asset"]).getroot()
            labels = " ".join(node.text or "" for node in root.findall(f".//{SVG_NS}text"))
            self.assertIn("EMPTY TEMPLATE", labels)

    def test_core_tiles_declare_valid_connection_edges(self) -> None:
        catalog = self._validate_catalog("docs/assets/tiles/catalog.json", "tiles")
        self.assertGreaterEqual(len(catalog["tiles"]), 8)
        valid_edges = {"north", "east", "south", "west"}
        for tile in catalog["tiles"]:
            edges = set(tile["connections"]["edges"])
            self.assertTrue(edges <= valid_edges)
            self.assertTrue(tile["connections"].get("continuity"))

    def test_surface_contract_is_discoverable_from_site_and_readme(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        studio = (ROOT / "docs/map-studio.html").read_text(encoding="utf-8")
        contract = ROOT / "docs/surface-assets-and-tiles.md"
        self.assertTrue(contract.is_file())
        self.assertIn("surface-assets-and-tiles.md", readme)
        self.assertIn("surface-assets-and-tiles.md", index)
        self.assertIn("map-studio.html", index)
        self.assertIn("assets/maps/catalog.json", studio)
        self.assertIn("assets/tiles/catalog.json", studio)
        self.assertIn("surps.map-draft", studio)


if __name__ == "__main__":
    unittest.main()
