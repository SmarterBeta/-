import subprocess
import sys
import unittest
from pathlib import Path

from baseline import render_status


REPO_ROOT = Path(__file__).resolve().parent.parent
BASELINE_PY = REPO_ROOT / "baseline.py"


class TestBaseline(unittest.TestCase):
    def test_happy_path_returns_expected_status(self) -> None:
        self.assertEqual(render_status("Alice"), "baseline-ready:Alice")

    def test_happy_path_trims_name(self) -> None:
        self.assertEqual(render_status("  Alice  "), "baseline-ready:Alice")

    def test_negative_path_rejects_blank_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "^user_name must be a non-empty string$"):
            render_status("   ")


class TestBaselineCli(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(BASELINE_PY), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cli_happy_path_exact_contract(self) -> None:
        result = self.run_cli("--name", "  Alice  ")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "baseline-ready:Alice\n")
        self.assertEqual(result.stderr, "")

    def test_cli_negative_path_exact_contract(self) -> None:
        result = self.run_cli("--name", "   ")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "error: user_name must be a non-empty string\n")


if __name__ == "__main__":
    unittest.main()
