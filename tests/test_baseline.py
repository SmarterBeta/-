import unittest

from baseline import render_status


class TestBaseline(unittest.TestCase):
    def test_happy_path_returns_expected_status(self) -> None:
        self.assertEqual(render_status("Alice"), "baseline-ready:Alice")

    def test_negative_path_rejects_blank_name(self) -> None:
        with self.assertRaises(ValueError):
            render_status("   ")


if __name__ == "__main__":
    unittest.main()
