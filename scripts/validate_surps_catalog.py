#!/usr/bin/env python3
"""Validate SURPS-owned book descriptors against the participation manifest.

This validates catalogue identity and local publication assets only. It does not
infer release status, rule precedence, or domain implementation capability.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".surps" / "participation.json"
REQUIRED_DESCRIPTOR_FIELDS = (
    "schemaVersion",
    "id",
    "category",
    "lod",
    "title",
    "version",
    "cover",
    "lodBadge",
    "publisher",
    "publisherMoniker",
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> dict | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(errors, f"Missing file: {path.relative_to(ROOT)}")
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(errors, f"Cannot read JSON {path.relative_to(ROOT)}: {exc}")
        return None
    if not isinstance(value, dict):
        fail(errors, f"Expected a JSON object: {path.relative_to(ROOT)}")
        return None
    return value


def local_file(value: object, owner: Path, field: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{owner.relative_to(ROOT)}: {field} must be a non-empty path")
        return
    candidate = (ROOT / value).resolve()
    if ROOT.resolve() not in candidate.parents:
        fail(errors, f"{owner.relative_to(ROOT)}: {field} escapes the repository")
    elif not candidate.is_file():
        fail(errors, f"{owner.relative_to(ROOT)}: {field} does not exist: {value}")


def main() -> int:
    errors: list[str] = []
    manifest = load_json(MANIFEST_PATH, errors)
    if manifest is None:
        return 1

    if manifest.get("schemaVersion") != 1:
        fail(errors, "participation.json: unsupported schemaVersion (expected 1)")
    if manifest.get("repository") != "TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem":
        fail(errors, "participation.json: repository identity does not match this repository")

    books = manifest.get("books")
    if not isinstance(books, list) or not books:
        fail(errors, "participation.json: books must be a non-empty array")
        books = []

    seen_ids: set[str] = set()
    checked = 0
    for index, entry in enumerate(books):
        label = f"participation.json: books[{index}]"
        if not isinstance(entry, dict):
            fail(errors, f"{label} must be an object")
            continue

        book_id = entry.get("id")
        if not isinstance(book_id, str) or not book_id.strip():
            fail(errors, f"{label}.id must be a non-empty string")
        elif book_id in seen_ids:
            fail(errors, f"{label}.id is duplicated: {book_id}")
        else:
            seen_ids.add(book_id)

        descriptor_value = entry.get("descriptorPath")
        book_value = entry.get("bookPath")
        cover_value = entry.get("coverPath")
        local_file(book_value, MANIFEST_PATH, f"books[{index}].bookPath", errors)
        local_file(descriptor_value, MANIFEST_PATH, f"books[{index}].descriptorPath", errors)
        local_file(cover_value, MANIFEST_PATH, f"books[{index}].coverPath", errors)

        if not isinstance(descriptor_value, str) or not descriptor_value.strip():
            continue
        descriptor_path = ROOT / descriptor_value
        descriptor = load_json(descriptor_path, errors)
        if descriptor is None:
            continue

        checked += 1
        for field in REQUIRED_DESCRIPTOR_FIELDS:
            if field not in descriptor:
                fail(errors, f"{descriptor_value}: missing required field '{field}'")

        for field in ("id", "category", "lod", "title", "version"):
            if field in entry and descriptor.get(field) != entry.get(field):
                fail(errors, f"{descriptor_value}: {field} differs from participation manifest")

        if descriptor.get("schemaVersion") != 1:
            fail(errors, f"{descriptor_value}: unsupported schemaVersion (expected 1)")
        lod = descriptor.get("lod")
        if not isinstance(lod, int) or isinstance(lod, bool) or lod < 0:
            fail(errors, f"{descriptor_value}: lod must be a non-negative integer")

        if descriptor.get("cover") != cover_value:
            fail(errors, f"{descriptor_value}: cover does not match participation manifest")
        local_file(descriptor.get("cover"), descriptor_path, "cover", errors)
        local_file(descriptor.get("lodBadge"), descriptor_path, "lodBadge", errors)

        moniker = descriptor.get("publisherMoniker")
        if not isinstance(moniker, str) or not moniker.startswith(("https://", "http://")):
            fail(errors, f"{descriptor_value}: publisherMoniker must be an absolute HTTP(S) URL")

    if errors:
        print("SURPS catalogue validation FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"SURPS catalogue validation passed: {len(books)} manifest entries, {checked} descriptors.")
    print("Identity, version, LOD, sourcebook, cover, and LOD badge references are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
