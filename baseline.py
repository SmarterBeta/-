"""Deterministic baseline scaffold for M1.2 Option 1 CLI validation."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence


ERROR_MESSAGE = "user_name must be a non-empty string"


def render_status(user_name: str) -> str:
    """Return a deterministic readiness string for a non-empty user name."""
    if not isinstance(user_name, str):
        raise ValueError(ERROR_MESSAGE)

    cleaned_name = user_name.strip()
    if not cleaned_name:
        raise ValueError(ERROR_MESSAGE)
    return f"baseline-ready:{cleaned_name}"


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entrypoint for status rendering."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", dest="user_name")
    args = parser.parse_args(argv)

    try:
        print(render_status(args.user_name))
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
