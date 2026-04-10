import subprocess
import sys
import unittest
from pathlib import Path

from baseline import render_status


BASELINE_SCRIPT = Path(__file__).resolve().parent.parent / "baseline.py"


class TestBaseline(unittest.TestCase):
    def test_happy_path_returns_expected_status(self) -> None:
        self.assertEqual(render_status("Alice"), "baseline-ready:Alice")

    def test_negative_path_rejects_blank_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "^user_name must be a non-empty string$"):
            render_status("   ")

    def test_cli_happy_path_prints_exact_output(self) -> None:
        result = subprocess.run(
            [sys.executable, str(BASELINE_SCRIPT), "--name", "  Alice  "],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "baseline-ready:Alice\n")
        self.assertEqual(result.stderr, "")

    def test_cli_negative_path_prints_exact_error_and_non_zero_exit(self) -> None:
        result = subprocess.run(
            [sys.executable, str(BASELINE_SCRIPT), "--name", "   "],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "error: user_name must be a non-empty string\n")


if __name__ == "__main__":
    unittest.main()
