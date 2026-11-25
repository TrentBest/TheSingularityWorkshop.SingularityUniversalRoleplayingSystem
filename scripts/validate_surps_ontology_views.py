#!/usr/bin/env python3
"""Validate MicroBundle identity, resolve rulebook selections, and build deterministic views."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem"
OUTPUT = "docs/generated/core-spying-player-view.json"


def load(path: str):
    candidate = (ROOT / path).resolve()
    if ROOT.resolve() not in candidate.parents:
        raise ValueError(f"path escapes repository: {path}")
    return json.loads(candidate.read_text(encoding="utf-8"))


def validate_schema(schema_path: str, document_path: str, errors: list[str]) -> dict | None:
    try:
        schema = load(schema_path)
        document = load(document_path)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for error in validator.iter_errors(document):
            location = "$" + "".join(f"[{p}]" if isinstance(p, int) else f".{p}" for p in error.absolute_path)
            errors.append(f"{document_path}{location}: {error.message}")
        return document
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, TypeError) as exc:
        errors.append(f"{document_path}: {exc}")
        return None


def resolve_view(bundle: dict, payload: dict, view: dict, errors: list[str]) -> dict:
    records_by_id: dict[str, tuple[str, dict]] = {}
    contributions = payload.get("contributions", {})
    for collection in bundle.get("recordCollections", []):
        records = contributions.get(collection, [])
        if not isinstance(records, list):
            errors.append(f"{bundle.get('id')}: content collection {collection!r} is not an array")
            continue
        for index, record in enumerate(records):
            if not isinstance(record, dict) or not isinstance(record.get("id"), str):
                continue
            identifier = record["id"]
            if identifier in records_by_id:
                errors.append(f"{bundle.get('id')}: duplicate record id {identifier!r}")
            records_by_id[identifier] = (collection, record)

    resolved = []
    selected_ids: set[str] = set()
    for selection in view.get("selections", []):
        if selection.get("microbundle") != bundle.get("id"):
            errors.append(f"{view.get('id')}: unresolved MicroBundle {selection.get('microbundle')!r}")
            continue
        for identifier in selection.get("records", []):
            if identifier in selected_ids:
                errors.append(f"{view.get('id')}: record selected more than once: {identifier}")
                continue
            selected_ids.add(identifier)
            found = records_by_id.get(identifier)
            if found is None:
                errors.append(f"{view.get('id')}: unresolved record {identifier!r} in {bundle.get('id')}")
                continue
            collection, record = found
            resolved.append({"collection": collection, "record": record})

    return {
        "schemaVersion": 1,
        "view": {
            "id": view.get("id"),
            "version": view.get("version"),
            "bookId": view.get("bookId"),
            "audience": view.get("audience"),
            "scope": view.get("scope"),
            "lod": view.get("lod"),
            "title": view.get("presentation", {}).get("title"),
            "description": view.get("presentation", {}).get("description")
        },
        "sources": [{
            "microbundle": bundle.get("id"),
            "version": bundle.get("version"),
            "status": bundle.get("status"),
            "ownerRepository": bundle.get("ownerRepository"),
            "contentPath": bundle.get("contentPath")
        }],
        "records": resolved
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if the checked-in projection is stale")
    args = parser.parse_args()
    errors: list[str] = []
    bundle = validate_schema("schemas/microbundle.schema.json", ".surps/microbundles/core-spying.microbundle.json", errors)
    view = validate_schema("schemas/rulebook-view.schema.json", ".surps/views/core-spying-player.view.json", errors)
    if bundle is None or view is None:
        return report(errors)

    try:
        payload = load(bundle["contentPath"])
        Draft202012Validator.check_schema(load(bundle["contentSchema"]))
        content_validator = Draft202012Validator(load(bundle["contentSchema"]), format_checker=FormatChecker())
        for error in content_validator.iter_errors(payload):
            errors.append(f"{bundle['contentPath']}: {error.message}")
        source_book = payload.get("book", {})
        if bundle.get("sourceBookId") != source_book.get("id"):
            errors.append("MicroBundle sourceBookId does not match transitional payload identity")
        if bundle.get("version") != source_book.get("version"):
            errors.append("MicroBundle version does not match transitional payload version")
        if bundle.get("ownerRepository") != source_book.get("ownerRepository"):
            errors.append("MicroBundle ownerRepository does not match transitional payload owner")
        if view.get("bookId") != "surps.core.spying" or view.get("lod") != 0:
            errors.append("CORE Spying view identity/LOD must match its book descriptor")
        descriptor = load("docs/books/core-spying.book.json")
        manifest = load(".surps/participation.json")
        entry = next((item for item in manifest.get("books", []) if item.get("id") == view.get("bookId")), None)
        if entry is None:
            errors.append("view bookId is not registered in participation manifest")
        else:
            if descriptor.get("viewPath") != ".surps/views/core-spying-player.view.json":
                errors.append("book descriptor viewPath does not identify the player view")
            if entry.get("viewPath") != descriptor.get("viewPath"):
                errors.append("participation manifest viewPath does not match book descriptor")
            if entry.get("microbundlePath") != ".surps/microbundles/core-spying.microbundle.json":
                errors.append("participation manifest microbundlePath does not identify the registered MicroBundle")
        if descriptor.get("id") != view.get("bookId") or descriptor.get("lod") != view.get("lod"):
            errors.append("view identity/LOD does not match the book descriptor")
        if descriptor.get("viewPath") != ".surps/views/core-spying-player.view.json":
            errors.append("book descriptor viewPath does not identify the player view")
        projection = resolve_view(bundle, payload, view, errors)
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        errors.append(str(exc))
        projection = {}

    if errors:
        return report(errors)
    rendered = json.dumps(projection, indent=2, ensure_ascii=False) + "\n"
    output = ROOT / OUTPUT
    if args.check:
        if not output.is_file() or output.read_text(encoding="utf-8") != rendered:
            errors.append(f"{OUTPUT} is missing or stale; run python3 scripts/validate_surps_ontology_views.py")
            return report(errors)
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(f"SURPS ontology/view validation passed: 1 MicroBundle, 1 view, {len(projection['records'])} resolved records.")
    print(f"Deterministic player projection {'verified' if args.check else 'generated'}: {OUTPUT}")
    return 0


def report(errors: list[str]) -> int:
    print("SURPS ontology/view validation FAILED:")
    for error in errors:
        print(f" - {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
