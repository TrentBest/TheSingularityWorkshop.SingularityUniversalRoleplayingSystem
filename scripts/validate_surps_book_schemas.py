#!/usr/bin/env python3
"""Validate SURPS book schemas, examples, and every registered contribution."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = "schemas/book-contribution.schema.json"
CASES = (
    (SCHEMA_PATH, "docs/examples/book-contribution.example.json"),
    ("schemas/experience-books.schema.json", "docs/examples/experience-books.example.json"),
    ("schemas/behavior-profile.schema.json", "docs/examples/fireball-behavior.json"),
)


def load(path: str):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: {exc}") from exc


def safe_repo_path(value: object, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{context}: expected a non-empty repository-relative path")
    candidate = (ROOT / value).resolve()
    if ROOT.resolve() not in candidate.parents:
        raise ValueError(f"{context}: path escapes the repository: {value}")
    return value


def validate_contribution_integrity(
    contribution: dict,
    descriptor: dict,
    manifest_book: dict,
    contribution_path: str,
    errors: list[str],
) -> None:
    """Check identity alignment and uniqueness before a contribution becomes selectable."""
    book = contribution.get("book")
    if not isinstance(book, dict):
        return

    for field in ("id", "version"):
        expected = manifest_book.get(field)
        descriptor_value = descriptor.get(field)
        contribution_value = book.get(field)
        if expected is not None and descriptor_value != expected:
            errors.append(
                f"{contribution_path}: descriptor {field} {descriptor_value!r} "
                f"does not match participation manifest {expected!r}"
            )
        if descriptor_value is not None and contribution_value != descriptor_value:
            errors.append(
                f"{contribution_path}: contribution book.{field} {contribution_value!r} "
                f"does not match descriptor {descriptor_value!r}"
            )

    seen: dict[str, str] = {}
    collections = contribution.get("contributions", {})
    if not isinstance(collections, dict):
        return
    for collection_name, records in collections.items():
        if not isinstance(records, list):
            continue
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                continue
            identifier = record.get("id")
            if not isinstance(identifier, str) or not identifier.strip():
                continue  # JSON Schema reports the missing/invalid identifier.
            location = f"contributions.{collection_name}[{index}]"
            previous = seen.get(identifier)
            if previous is not None:
                errors.append(
                    f"{contribution_path}: duplicate contribution id {identifier!r} "
                    f"at {location}; first declared at {previous}"
                )
            else:
                seen[identifier] = location


def validate_document(validator: Draft202012Validator, document_path: str, errors: list[str]) -> None:
    try:
        document = load(document_path)
    except ValueError as exc:
        errors.append(str(exc))
        return
    for error in sorted(validator.iter_errors(document), key=lambda item: list(map(str, item.absolute_path))):
        location = "$" + "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
        errors.append(f"{document_path}{location}: {error.message}")


def main() -> int:
    errors: list[str] = []
    validators: dict[str, Draft202012Validator] = {}
    try:
        for schema_path, _ in CASES:
            if schema_path not in validators:
                schema = load(schema_path)
                Draft202012Validator.check_schema(schema)
                validators[schema_path] = Draft202012Validator(
                    schema, format_checker=FormatChecker()
                )
    except (ValueError, TypeError) as exc:
        print(f"SURPS JSON Schema validation FAILED: {exc}")
        return 1

    for schema_path, example_path in CASES:
        validate_document(validators[schema_path], example_path, errors)

    try:
        manifest = load(".surps/participation.json")
        books = manifest.get("books", [])
        if not isinstance(books, list):
            raise ValueError(".surps/participation.json: books must be an array")
        contribution_validator = validators[SCHEMA_PATH]
        registered = 0
        for index, book in enumerate(books):
            if not isinstance(book, dict):
                errors.append(f".surps/participation.json: books[{index}] must be an object")
                continue
            contribution_path = book.get("contributionPath")
            if contribution_path is None:
                continue
            try:
                contribution_path = safe_repo_path(
                    contribution_path, f"participation.json books[{index}].contributionPath"
                )
            except ValueError as exc:
                errors.append(str(exc))
                continue
            descriptor_path = book.get("descriptorPath")
            descriptor = {}
            if isinstance(descriptor_path, str):
                try:
                    descriptor_path = safe_repo_path(descriptor_path, "descriptorPath")
                    descriptor = load(descriptor_path)
                    if descriptor.get("contributionPath") != contribution_path:
                        errors.append(
                            f"{descriptor_path}: contributionPath does not match participation manifest"
                        )
                    if descriptor.get("contributionSchema") != SCHEMA_PATH:
                        errors.append(
                            f"{descriptor_path}: contributionSchema must be {SCHEMA_PATH}"
                        )
                    if descriptor.get("id") != book.get("id"):
                        errors.append(
                            f"{descriptor_path}: descriptor id does not match participation manifest"
                        )
                    if descriptor.get("version") != book.get("version"):
                        errors.append(
                            f"{descriptor_path}: descriptor version does not match participation manifest"
                        )
                except (ValueError, AttributeError) as exc:
                    errors.append(str(exc))
            validate_document(contribution_validator, contribution_path, errors)
            try:
                contribution = load(contribution_path)
                validate_contribution_integrity(
                    contribution, descriptor, book, contribution_path, errors
                )
            except ValueError as exc:
                errors.append(str(exc))
            registered += 1
    except ValueError as exc:
        errors.append(str(exc))
        registered = 0

    if errors:
        print("SURPS book schema validation FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(
        f"SURPS JSON Schema validation passed: {len(CASES)} schemas, "
        f"{len(CASES)} examples, and {registered} registered contribution(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
