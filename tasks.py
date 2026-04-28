"""Deterministic local task capture CLI for milestone M2.1 Option 2."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


DEFAULT_DATA_FILE = Path(__file__).resolve().parent / "data" / "tasks.json"


def data_file_path() -> Path:
    """Return the configured data file path."""
    override = os.environ.get("TASKS_DATA_FILE")
    if override:
        return Path(override)
    return DEFAULT_DATA_FILE


def _empty_store() -> dict[str, list[dict[str, str]]]:
    return {"tasks": []}


def _validate_store(store: object) -> dict[str, list[dict[str, str]]]:
    if not isinstance(store, dict) or set(store.keys()) != {"tasks"}:
        raise ValueError("invalid tasks store schema")

    tasks = store.get("tasks")
    if not isinstance(tasks, list):
        raise ValueError("invalid tasks store schema")

    for item in tasks:
        if not isinstance(item, dict):
            raise ValueError("invalid tasks store schema")
        if set(item.keys()) != {"id", "title"}:
            raise ValueError("invalid tasks store schema")
        if not isinstance(item["id"], str) or not isinstance(item["title"], str):
            raise ValueError("invalid tasks store schema")

    return {"tasks": tasks}


def _write_store(path: Path, store: dict[str, list[dict[str, str]]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(store, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_store(path: Path | None = None) -> dict[str, list[dict[str, str]]]:
    """Load the task store and initialize it if missing."""
    file_path = path or data_file_path()
    if not file_path.exists():
        store = _empty_store()
        _write_store(file_path, store)
        return store

    raw = file_path.read_text(encoding="utf-8")
    store = json.loads(raw)
    return _validate_store(store)


def add_task(title: str, path: Path | None = None) -> dict[str, str]:
    """Add a task with the next deterministic sequential ID."""
    cleaned_title = title.strip()
    if not cleaned_title:
        raise ValueError("title must be a non-empty string")

    file_path = path or data_file_path()
    store = load_store(file_path)
    next_id = f"T{len(store['tasks']) + 1:04d}"
    task = {"id": next_id, "title": cleaned_title}
    store["tasks"].append(task)
    _write_store(file_path, store)
    return task


def list_tasks(path: Path | None = None) -> list[dict[str, str]]:
    """Return tasks in deterministic insertion order."""
    store = load_store(path or data_file_path())
    return list(store["tasks"])


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments for tasks CLI."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--title", required=True)

    subparsers.add_parser("list")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run tasks CLI command and return exit code."""
    args = parse_args(argv)

    try:
        if args.command == "add":
            task = add_task(args.title)
            print(f"added:{task['id']}:{task['title']}")
            return 0

        if args.command == "list":
            tasks = list_tasks()
            if tasks:
                print("\n".join(f"{task['id']} {task['title']}" for task in tasks))
            return 0

        print("error: unknown command", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
