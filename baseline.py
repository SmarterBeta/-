"""Deterministic baseline scaffold for Option 1 validation."""

from __future__ import annotations

import argparse
import sys


def render_status(user_name: str) -> str:
    """Return a deterministic readiness string for a non-empty user name."""
    cleaned_name = user_name.strip()
    if not cleaned_name:
        raise ValueError("user_name must be a non-empty string")
    return f"baseline-ready:{cleaned_name}"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments for the baseline CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", dest="user_name", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the baseline CLI and return an exit code."""
    args = parse_args(argv)
    try:
        print(render_status(args.user_name))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
