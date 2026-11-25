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




class MissingLedgerStoryGraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = json.loads(
            (ROOT / "experiences" / "missing-ledger" / "story-graph.json").read_text(encoding="utf-8")
        )

    def test_graph_has_unique_nodes_and_resolvable_entry(self) -> None:
        nodes = self.graph["nodes"]
        ids = [node["id"] for node in nodes]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn(self.graph["entryNodeId"], ids)

    def test_every_choice_target_and_state_reference_is_declared(self) -> None:
        nodes = {node["id"]: node for node in self.graph["nodes"]}
        state_keys = set(self.graph["stateKeys"])
        for node in nodes.values():
            choice_ids = [choice["id"] for choice in node["choices"]]
            self.assertEqual(len(choice_ids), len(set(choice_ids)), node["id"])
            for choice in node["choices"]:
                self.assertIn(choice["nextNodeId"], nodes, choice["id"])
                self.assertIn(choice["resolution"], ("direct", "referee"))
                for key in choice.get("requiresAll", []) + choice.get("setsAll", []):
                    self.assertIn(key, state_keys, (node["id"], choice["id"], key))

    def test_all_story_nodes_are_reachable_and_endings_are_terminal(self) -> None:
        nodes = {node["id"]: node for node in self.graph["nodes"]}
        reached = set()
        pending = [self.graph["entryNodeId"]]
        while pending:
            current = pending.pop()
            if current in reached:
                continue
            reached.add(current)
            pending.extend(choice["nextNodeId"] for choice in nodes[current]["choices"])
        self.assertEqual(set(nodes), reached)
        for node in nodes.values():
            if node["kind"] == "ending":
                self.assertEqual([], node["choices"], node["id"])

    def test_story_graph_is_authoring_content_not_a_client_secret_store(self) -> None:
        semantics = self.graph["semantics"]
        self.assertIn("pending player intent only", semantics["transitionAuthority"])
        self.assertIn("human referee records an adjudicated result", semantics["transitionAuthority"])
        self.assertIn("not a complete map of outcome-specific consequences", semantics["transitionAuthority"])
        self.assertIn("not a secure store", semantics["presentationBoundary"])
        schema = json.loads(
            (ROOT / "schemas" / "scenario-story-graph.schema.json").read_text(encoding="utf-8")
        )
        self.assertEqual(1, schema["properties"]["schemaVersion"]["const"])
        choice = schema["properties"]["nodes"]["items"]["properties"]["choices"]["items"]["properties"]
        self.assertIn("pending intent only", choice["resolution"]["description"])
        self.assertIn("only when this choice transition is committed", choice["setsAll"]["description"])
        self.assertIn("does not encode separate destinations", choice["nextNodeId"]["description"])


if __name__ == "__main__":
    unittest.main()
