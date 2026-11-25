import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "validate_surps_external_providers.py"

class ExternalProviderValidationTests(unittest.TestCase):
    def run_validator(self, source):
        return subprocess.run([sys.executable, str(SCRIPT), "--source-root", str(source)],
                              cwd=ROOT, capture_output=True, text=True)

    def test_pinned_physics_provider_manifests_validate(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            fixtures = {
                "microbundles/NormalImpulseResponse/microbundle.json": (5202, "physics.contact.normal-impulse.v1"),
                "microbundles/PrescribedKinematicMotion/microbundle.json": (5203, "physics.kinematics.prescribed-motion.v1")
            }
            for path, (bundle_id, provider_id) in fixtures.items():
                target = source / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(json.dumps({
                    "bundle":{"id":bundle_id,"version":"1.0.0","name":"Fixture","providerIds":[provider_id]},
                    "ontology":{"domain":"physics","branch":"mechanics"},
                    "capability":{"id":provider_id,"summary":"fixture","kind":"model"},
                    "evidence":{"status":"implemented"}
                }), encoding="utf-8")
            result = self.run_validator(source)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_provider_identity_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            target = source / "microbundles/NormalImpulseResponse/microbundle.json"
            target.parent.mkdir(parents=True)
            target.write_text(json.dumps({
                "bundle":{"id":999,"providerIds":["wrong"]},
                "ontology":{"domain":"physics"},
                "capability":{"id":"wrong"},
                "evidence":{"status":"implemented"}
            }), encoding="utf-8")
            result = self.run_validator(source)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("bundle ID mismatch", result.stdout)

if __name__ == "__main__":
    unittest.main()
