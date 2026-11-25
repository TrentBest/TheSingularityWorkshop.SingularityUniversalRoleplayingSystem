from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLAYER_PAGE = ROOT / "docs" / "books" / "core-spying-play.html"
EXPERIENCE_README = ROOT / "experiences" / "embassy-reception" / "README.md"
BOOK_SELECTION = ROOT / "experiences" / "embassy-reception" / "experience-books.json"


class EmbassyReceptionBoundaryTests(unittest.TestCase):
    def test_public_player_page_contains_no_referee_secret_or_role_toggle(self) -> None:
        html = PLAYER_PAGE.read_text(encoding="utf-8")
        lowered = html.lower()

        # These were the concrete private facts accidentally shipped to every
        # browser before the player/referee boundary hardening commit.
        for secret in (
            "silver cufflink",
            "west service exit",
            "kitchen contact is being watched",
        ):
            with self.subTest(secret=secret):
                self.assertNotIn(secret, lowered)

        # A client-side role toggle is presentation, not authorization.
        for marker in (
            'class="gm"',
            "gm-on",
            "viewtoggle",
            "show game master view",
            "game master view",
        ):
            with self.subTest(marker=marker):
                self.assertNotIn(marker, lowered)

        self.assertIn("the referee maintains the hidden fact ledger separately", lowered)

    def test_scenario_selects_the_canonical_core_spying_book(self) -> None:
        selection = json.loads(BOOK_SELECTION.read_text(encoding="utf-8"))
        self.assertEqual(1, selection["schemaVersion"])
        self.assertEqual("surps.demo.embassy-reception", selection["experience"]["id"])
        self.assertEqual("0.1.0", selection["experience"]["version"])
        self.assertEqual(
            [{"id": "surps.core.spying", "versionRange": "^0.1.0", "required": True,
              "lod": 0,
              "purpose": "The selected CORE Spying playtest rules, evidence model, and scene procedures."}],
            selection["books"],
        )
        self.assertNotIn("contributions", selection)

    def test_experience_documents_the_current_runtime_limitations(self) -> None:
        readme = EXPERIENCE_README.read_text(encoding="utf-8").lower()
        self.assertIn("tabletop playtest scene", readme)
        self.assertIn("not yet a live hermit-connected session", readme)
        self.assertIn("not yet a live hermit-connected session, a persistent campaign runtime", readme)
        self.assertIn("human referee remains responsible", readme)
        self.assertIn("portable fsm_cos composition manifest", readme)



class MissingLedgerExperienceTests(unittest.TestCase):
    def test_manifest_selects_canonical_core_spying_book(self) -> None:
        manifest_path = ROOT / "experiences" / "missing-ledger" / "experience-books.json"
        selection = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual("surps.demo.missing-ledger", selection["experience"]["id"])
        self.assertEqual("0.1.0", selection["experience"]["version"])
        self.assertEqual(
            [{"id": "surps.core.spying", "versionRange": "^0.1.0", "required": True,
              "lod": 0,
              "purpose": "The canonical CORE Spying playtest rules, information states, and scene procedures."}],
            selection["books"],
        )
        self.assertNotIn("contributions", selection)

    def test_public_mission_page_does_not_ship_referee_only_facts(self) -> None:
        page = (ROOT / "docs" / "experiences" / "missing-ledger" / "index.html").read_text(encoding="utf-8").lower()
        for secret in (
            "blue oilcloth folder",
            "millwright",
            "old ferry landing",
            "corrupt clerk",
            "watch sergeant",
        ):
            with self.subTest(secret=secret):
                self.assertNotIn(secret, page)
        self.assertIn("keep private facts and adjudication notes outside this public site", page)
        self.assertNotIn("game master view", page)
        self.assertNotIn("gm-on", page)

    def test_mission_labels_human_adjudication_and_no_digital_evaluator(self) -> None:
        page = (ROOT / "docs" / "experiences" / "missing-ledger" / "index.html").read_text(encoding="utf-8").lower()
        self.assertIn("human referee remains the adjudicator", page)
        self.assertIn("no automated digital spying evaluator is claimed", page)
        self.assertIn("no clock advances automatically", page)


if __name__ == "__main__":
    unittest.main()
