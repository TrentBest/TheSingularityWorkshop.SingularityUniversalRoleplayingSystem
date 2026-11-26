from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "docs" / "experiences" / "soviet-facility-opening" / "index.html"
README = ROOT / "experiences" / "soviet-facility-opening" / "README.md"


class SovietFacilityOpeningTests(unittest.TestCase):
    def test_cinematic_opening_contains_all_three_scene_stages(self) -> None:
        html = PAGE.read_text(encoding="utf-8")
        for marker in ("mapStage", "groundsStage", "gateStage", "approachBtn", "gateBtn"):
            with self.subTest(marker=marker):
                self.assertIn(marker, html)

    def test_location_is_explicitly_fictional_and_map_is_not_navigation(self) -> None:
        html = PAGE.read_text(encoding="utf-8").lower()
        readme = README.read_text(encoding="utf-8").lower()
        for phrase in ("fictional", "alleged location", "not for navigation"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, html)
        self.assertIn("not a claim about a real clandestine installation", readme)

    def test_name_challenge_has_twenty_choices_and_handler_reveal(self) -> None:
        html = PAGE.read_text(encoding="utf-8")
        match = re.search(r"const names=\[(.*?)\];\s*const correct=", html, re.S)
        self.assertIsNotNone(match, "The authored identity list must be present.")
        names = re.findall(r'"([^"]+)"', match.group(1))
        self.assertEqual(20, len(names))
        self.assertEqual(20, len(set(names)))
        self.assertIn('const correct="Alexei Morozov"', html)
        self.assertIn("deliverWhisper", html)
        self.assertIn('classList.add("highlight")', html)

    def test_page_does_not_claim_runtime_or_audio_features_that_are_not_present(self) -> None:
        readme = README.read_text(encoding="utf-8").lower()
        self.assertIn("does not claim a live 3d renderer", readme)
        self.assertIn("does not pretend that browser javascript is fsm_api", readme)
        self.assertIn("integer-backed state identity", readme)


if __name__ == "__main__":
    unittest.main()
