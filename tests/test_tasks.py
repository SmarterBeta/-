import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tasks import add_task


REPO_ROOT = Path(__file__).resolve().parent.parent
TASKS_PY = REPO_ROOT / "tasks.py"


class TestTasksCli(unittest.TestCase):
    def run_cli(self, data_file: Path, *args: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["TASKS_DATA_FILE"] = str(data_file)
        return subprocess.run(
            [sys.executable, str(TASKS_PY), *args],
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )

    def test_cli_happy_path_exact_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            data_file = Path(tmp_dir) / "tasks.json"

            add_alpha = self.run_cli(data_file, "add", "--title", "alpha")
            self.assertEqual(add_alpha.returncode, 0)
            self.assertEqual(add_alpha.stdout, "added:T0001:alpha\n")
            self.assertEqual(add_alpha.stderr, "")

            add_beta = self.run_cli(data_file, "add", "--title", "beta")
            self.assertEqual(add_beta.returncode, 0)
            self.assertEqual(add_beta.stdout, "added:T0002:beta\n")
            self.assertEqual(add_beta.stderr, "")

            listing = self.run_cli(data_file, "list")
            self.assertEqual(listing.returncode, 0)
            self.assertEqual(listing.stdout, "T0001 alpha\nT0002 beta\n")
            self.assertEqual(listing.stderr, "")

    def test_cli_negative_blank_title_exact_error(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            data_file = Path(tmp_dir) / "tasks.json"
            result = self.run_cli(data_file, "add", "--title", "   ")
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, "")
            self.assertEqual(result.stderr, "error: title must be a non-empty string\n")


class TestTasksPersistence(unittest.TestCase):
    def test_persisted_schema_and_deterministic_id_sequence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            data_file = Path(tmp_dir) / "tasks.json"

            first = add_task("alpha", data_file)
            second = add_task("beta", data_file)

            self.assertEqual(first, {"id": "T0001", "title": "alpha"})
            self.assertEqual(second, {"id": "T0002", "title": "beta"})

            persisted = json.loads(data_file.read_text(encoding="utf-8"))
            self.assertEqual(set(persisted.keys()), {"tasks"})
            self.assertIsInstance(persisted["tasks"], list)
            self.assertEqual(
                persisted,
                {
                    "tasks": [
                        {"id": "T0001", "title": "alpha"},
                        {"id": "T0002", "title": "beta"},
                    ]
                },
            )


if __name__ == "__main__":
    unittest.main()
