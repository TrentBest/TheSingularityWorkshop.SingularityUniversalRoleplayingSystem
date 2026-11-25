#!/usr/bin/env python3
"""Validate the local MicroBundle registry, resolve rulebook views, and build deterministic projections."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem"
REGISTRY_PATH = ".surps/microbundles/registry.json"
VIEW_PATH = ".surps/views/core-spying-player.view.json"
OUTPUT = "docs/generated/core-spying-player-view.json"

def load(path: str):
    candidate = (ROOT / path).resolve()
    if ROOT.resolve() not in candidate.parents:
        raise ValueError(f"path escapes repository: {path}")
    return json.loads(candidate.read_text(encoding="utf-8"))

def validate_schema(schema_path: str, document_path: str, errors: list[str]) -> dict | None:
    try:
        schema, document = load(schema_path), load(document_path)
        Draft202012Validator.check_schema(schema)
        for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(document):
            location = "$" + "".join(f"[{p}]" if isinstance(p, int) else f".{p}" for p in error.absolute_path)
            errors.append(f"{document_path}{location}: {error.message}")
        return document
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, TypeError) as exc:
        errors.append(f"{document_path}: {exc}")
        return None

def load_bundle_registry(errors: list[str]) -> dict[str, tuple[dict, dict]]:
    registry = validate_schema("schemas/microbundle-registry.schema.json", REGISTRY_PATH, errors)
    if registry is None:
        return {}
    if registry.get("repository") != REPOSITORY:
        errors.append(f"{REGISTRY_PATH}: repository identity does not match this repository")
    bundles, seen_paths = {}, set()
    for item in registry.get("microbundles", []):
        bundle_id, descriptor_path = item.get("id"), item.get("path")
        if bundle_id in bundles:
            errors.append(f"{REGISTRY_PATH}: duplicate MicroBundle id {bundle_id!r}")
            continue
        if descriptor_path in seen_paths:
            errors.append(f"{REGISTRY_PATH}: duplicate descriptor path {descriptor_path!r}")
            continue
        seen_paths.add(descriptor_path)
        descriptor = validate_schema("schemas/microbundle.schema.json", descriptor_path, errors)
        if descriptor is None:
            continue
        if descriptor.get("id") != bundle_id:
            errors.append(f"{descriptor_path}: id does not match MicroBundle registry")
        try:
            content_path, schema_path = descriptor["contentPath"], descriptor["contentSchema"]
            payload, content_schema = load(content_path), load(schema_path)
            Draft202012Validator.check_schema(content_schema)
            for error in Draft202012Validator(content_schema, format_checker=FormatChecker()).iter_errors(payload):
                errors.append(f"{content_path}: {error.message}")
            source_book = payload.get("book", {})
            for field, value in (("sourceBookId", source_book.get("id")),
                                 ("version", source_book.get("version")),
                                 ("ownerRepository", source_book.get("ownerRepository"))):
                if descriptor.get(field) != value:
                    errors.append(f"{descriptor_path}: {field} does not match transitional payload identity")
            bundles[bundle_id] = (descriptor, payload)
        except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            errors.append(f"{descriptor_path}: {exc}")
    known_ids = set(bundles)
    for bundle_id, (descriptor, _) in bundles.items():
        for dependency in descriptor.get("dependencies", []):
            if not dependency.get("optional", False) and dependency.get("id") not in known_ids:
                errors.append(f"{bundle_id}: unresolved required MicroBundle dependency {dependency.get('id')!r}")
    global_ids = {}
    for bundle_id, (descriptor, payload) in bundles.items():
        for collection in descriptor.get("recordCollections", []):
            for record in payload.get("contributions", {}).get(collection, []):
                if isinstance(record, dict) and isinstance(record.get("id"), str):
                    identifier = record["id"]
                    previous = global_ids.get(identifier)
                    if previous is not None and previous != bundle_id:
                        errors.append(f"global local-registry ID collision {identifier!r}: {previous} and {bundle_id}")
                    global_ids[identifier] = bundle_id
    return bundles

def resolve_view(bundles: dict[str, tuple[dict, dict]], view: dict, errors: list[str]) -> dict:
    resolved, selected_ids, used_bundles, records_by_bundle = [], set(), {}, {}
    for bundle_id, (descriptor, payload) in bundles.items():
        records = {}
        for collection in descriptor.get("recordCollections", []):
            values = payload.get("contributions", {}).get(collection, [])
            if not isinstance(values, list):
                errors.append(f"{bundle_id}: content collection {collection!r} is not an array")
                continue
            for index, record in enumerate(values):
                if not isinstance(record, dict) or not isinstance(record.get("id"), str):
                    continue
                identifier = record["id"]
                if identifier in records:
                    errors.append(f"{bundle_id}: duplicate record id {identifier!r} at {collection}[{index}]")
                records[identifier] = (collection, record)
        records_by_bundle[bundle_id] = records
    for selection in view.get("selections", []):
        bundle_id = selection.get("microbundle")
        if bundle_id not in bundles:
            errors.append(f"{view.get('id')}: unresolved MicroBundle {bundle_id!r}")
            continue
        descriptor, _ = bundles[bundle_id]
        used_bundles[bundle_id] = descriptor
        for identifier in selection.get("records", []):
            if identifier in selected_ids:
                errors.append(f"{view.get('id')}: record selected more than once: {identifier}")
                continue
            selected_ids.add(identifier)
            found = records_by_bundle[bundle_id].get(identifier)
            if found is None:
                errors.append(f"{view.get('id')}: unresolved record {identifier!r} in {bundle_id}")
                continue
            collection, record = found
            resolved.append({"collection": collection, "record": record, "sourceMicrobundle": bundle_id})
    return {
        "schemaVersion": 1,
        "view": {"id": view.get("id"), "version": view.get("version"), "bookId": view.get("bookId"),
                 "audience": view.get("audience"), "scope": view.get("scope"), "lod": view.get("lod"),
                 "title": view.get("presentation", {}).get("title"),
                 "description": view.get("presentation", {}).get("description")},
        "sources": [{"microbundle": bid, "version": desc.get("version"), "status": desc.get("status"),
                     "ownerRepository": desc.get("ownerRepository"), "contentPath": desc.get("contentPath")}
                    for bid, desc in used_bundles.items()],
        "records": resolved
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if the checked-in projection is stale")
    args = parser.parse_args()
    errors, bundles = [], {}
    bundles = load_bundle_registry(errors)
    view = validate_schema("schemas/rulebook-view.schema.json", VIEW_PATH, errors)
    if view is None or not bundles:
        return report(errors)
    try:
        descriptor, manifest = load("docs/books/core-spying.book.json"), load(".surps/participation.json")
        entry = next((item for item in manifest.get("books", []) if item.get("id") == view.get("bookId")), None)
        if entry is None:
            errors.append("view bookId is not registered in participation manifest")
        else:
            if descriptor.get("viewPath") != VIEW_PATH:
                errors.append("book descriptor viewPath does not identify the player view")
            if entry.get("viewPath") != descriptor.get("viewPath"):
                errors.append("participation manifest viewPath does not match book descriptor")
            registry_paths = {item["path"] for item in load(REGISTRY_PATH)["microbundles"]}
            if entry.get("microbundlePath") not in registry_paths:
                errors.append("participation manifest MicroBundle path is not present in the local registry")
        if descriptor.get("id") != view.get("bookId") or descriptor.get("lod") != view.get("lod"):
            errors.append("view identity/LOD does not match the book descriptor")
        projection = resolve_view(bundles, view, errors)
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
    print(f"SURPS ontology/view validation passed: {len(bundles)} registered MicroBundle(s), 1 view, {len(projection['records'])} resolved records.")
    print(f"Deterministic projection {'verified' if args.check else 'generated'}: {OUTPUT}")
    return 0

def report(errors: list[str]) -> int:
    print("SURPS ontology/view validation FAILED:")
    for error in errors:
        print(f" - {error}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
