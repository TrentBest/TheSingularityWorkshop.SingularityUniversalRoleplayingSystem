from __future__ import annotations

import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "docs" / "assets" / "character-sheets" / "catalog.json"
STUDIO = ROOT / "docs" / "character-studio.html"
SVG_NS = "{http://www.w3.org/2000/svg}"


class CharacterSheetAssetTests(unittest.TestCase):
    def test_catalog_assets_are_valid_accessible_empty_svg_templates(self) -> None:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        themes = {theme["id"]: theme for theme in catalog["themes"]}

        self.assertEqual(
            {"verdant", "stone", "woodwork", "steel", "aether"},
            set(themes),
        )
        self.assertEqual(
            {"verdant", "stone", "woodwork"},
            set(catalog["starterThemes"]),
        )
        self.assertEqual(
            {"steel", "aether"},
            set(catalog["premiumThemes"]),
        )

        for theme_id, theme in themes.items():
            with self.subTest(theme=theme_id):
                asset = ROOT / theme["asset"]
                self.assertTrue(asset.is_file(), f"Missing SVG: {asset}")
                root = ET.parse(asset).getroot()
                self.assertEqual("svg", root.tag.removeprefix(SVG_NS))
                self.assertEqual("img", root.attrib.get("role"))
                self.assertEqual("title desc", root.attrib.get("aria-labelledby"))
                self.assertTrue(root.find(f"{SVG_NS}title").text.strip())
                self.assertTrue(root.find(f"{SVG_NS}desc").text.strip())
                text_content = " ".join(
                    node.text or "" for node in root.findall(f".//{SVG_NS}text")
                )
                self.assertIn("CHARACTER RECORD", text_content)
                self.assertIn("EMPTY TEMPLATE", text_content)
                self.assertTrue(theme["animatedDetails"] is (theme_id == "aether"))
                self.assertEqual("surps.character-sheet", root.attrib.get("data-surps-contract"))
                self.assertEqual("1.0.0", root.attrib.get("data-surps-contract-version"))
                bindings = {
                    node.attrib["data-surps-bind"]
                    for node in root.findall(f".//*[@data-surps-bind]")
                }
                self.assertEqual(
                    {
                        "name", "pronouns", "role", "origin", "attributes",
                        "capabilities", "training", "condition", "goals",
                        "equipment", "concept", "relationships", "history",
                        "appearance",
                    },
                    bindings,
                )

    def test_character_studio_exposes_only_starter_themes_for_selection(self) -> None:
        html = STUDIO.read_text(encoding="utf-8")
        self.assertIn('id="sheetTheme"', html)
        self.assertIn('<object id="sheetPreview"', html)
        self.assertIn('contentDocument', html)
        self.assertIn('updateSheetBindings', html)
        self.assertIn('data-surps-bind', html)
        self.assertIn('value="verdant"', html)
        self.assertIn('value="stone"', html)
        self.assertIn('value="woodwork"', html)
        self.assertIn('value="steel" disabled', html)
        self.assertIn('value="aether" disabled', html)
        self.assertIn('sheetTheme:selectedTheme', html)
        self.assertIn("prefers-reduced-motion", html)


if __name__ == "__main__":
    unittest.main()
