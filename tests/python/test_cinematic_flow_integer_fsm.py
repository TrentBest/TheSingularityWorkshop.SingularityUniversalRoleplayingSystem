from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SAMPLE = ROOT / "samples" / "SurpsCinematicFlow"
PROJECT = SAMPLE / "SurpsCinematicFlow.csproj"
PROGRAM = SAMPLE / "Program.cs"


class CinematicFlowIntegerFsmTests(unittest.TestCase):
    def test_sample_references_fsm_api_development_source(self) -> None:
        project = PROJECT.read_text(encoding="utf-8")
        self.assertIn("dependencies/Visualize/FSM_API/FSM_API/FSM_API.csproj", project)

    def test_runtime_uses_native_integer_backed_api_and_integer_state_ids(self) -> None:
        source = PROGRAM.read_text(encoding="utf-8")
        self.assertIn("using TheSingularityWorkshop.FSM_API.IntegerBacked;", source)
        self.assertIn("FsmApi.Create.CreateFiniteStateMachine(", source)
        self.assertIn("CurrentStateID", source)
        self.assertNotIn("GetHashCode()", source)

    def test_scene_flow_models_success_and_recoverable_identity_challenge(self) -> None:
        source = PROGRAM.read_text(encoding="utf-8")
        for marker in ("CorrectIdentitySelected", "WrongIdentitySelected", "RetryRequested",
                       "RunSuccess", "RunChallengeThenRecover"):
            with self.subTest(marker=marker):
                self.assertIn(marker, source)


if __name__ == "__main__":
    unittest.main()
