#!/usr/bin/env python3
"""Validate SURPS contribution and experience examples against their JSON Schemas."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CASES = (
    ("schemas/book-contribution.schema.json", "docs/examples/book-contribution.example.json"),
    ("schemas/experience-books.schema.json", "docs/examples/experience-books.example.json"),
)


def load(path: str):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: {exc}") from exc


def main() -> int:
    errors: list[str] = []
    for schema_path, example_path in CASES:
        try:
            schema = load(schema_path)
            example = load(example_path)
            Draft202012Validator.check_schema(schema)
            validator = Draft202012Validator(schema, format_checker=FormatChecker())
            for error in sorted(validator.iter_errors(example), key=lambda item: list(map(str, item.absolute_path))):
                location = "$" + "".join(
                    f"[{part}]" if isinstance(part, int) else f".{part}"
                    for part in error.absolute_path
                )
                errors.append(f"{example_path}{location}: {error.message}")
        except (ValueError, TypeError) as exc:
            errors.append(str(exc))

    if errors:
        print("SURPS book schema validation FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"SURPS JSON Schema validation passed: {len(CASES)} schemas and {len(CASES)} examples.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
