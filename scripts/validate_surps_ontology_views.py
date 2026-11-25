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

def collection_records(payload: dict, collection: str):
    """Read canonical MicroBundle content, with a read-only legacy adapter."""
    if "contributions" in payload:
        return payload.get("contributions", {}).get(collection, [])
    return payload.get(collection, [])

def validate_asset_manifest(descriptor: dict, errors: list[str]) -> None:
    """Validate MicroBundle-owned book assets and keep paths inside the repository."""
    manifest_path = descriptor.get("assetsPath")
    if not manifest_path:
        return
    schema_path = descriptor.get("assetsSchema")
    if not schema_path:
        errors.append(f"{descriptor.get('id')}: assetsPath requires assetsSchema")
        return
    manifest = validate_schema(schema_path, manifest_path, errors)
    if manifest is None:
        return
    if manifest.get("microbundleId") != descriptor.get("id"):
        errors.append(f"{manifest_path}: microbundleId does not match descriptor")
    seen = set()
    for asset in manifest.get("assets", []):
        if not isinstance(asset, dict):
            errors.append(f"{manifest_path}: asset entries must be objects")
            continue
        asset_id, asset_path = asset.get("id"), asset.get("path")
        if asset_id in seen:
            errors.append(f"{manifest_path}: duplicate asset id {asset_id!r}")
            continue
        seen.add(asset_id)
        try:
            candidate = (ROOT / asset_path).resolve()
            if ROOT.resolve() not in candidate.parents:
                raise ValueError(f"path escapes repository: {asset_path}")
            if not candidate.is_file():
                errors.append(f"{manifest_path}: missing asset file {asset_path!r}")
                continue
            if asset.get("kind") == "svg":
                source = candidate.read_text(encoding="utf-8")
                if "<svg" not in source or "<title" not in source or "<desc" not in source:
                    errors.append(f"{manifest_path}: SVG asset {asset_id!r} requires svg, title, and desc elements")
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            errors.append(f"{manifest_path}: invalid asset {asset_id!r}: {exc}")

def validate_preview_manifest(descriptor: dict, errors: list[str]) -> None:
    """Validate every action preview offered by a MicroBundle manifest."""
    manifest_path = descriptor.get("previewsPath")
    if not manifest_path:
        return
    schema_path = descriptor.get("previewsSchema")
    if not schema_path:
        errors.append(f"{descriptor.get('id')}: previewsPath requires previewsSchema")
        return
    manifest = validate_schema(schema_path, manifest_path, errors)
    if manifest is None:
        return
    if manifest.get("microbundleId") != descriptor.get("id"):
        errors.append(f"{manifest_path}: microbundleId does not match descriptor")
    seen_ids, seen_paths = set(), set()
    for entry in manifest.get("previews", []):
        if not isinstance(entry, dict):
            errors.append(f"{manifest_path}: preview entries must be objects")
            continue
        preview_id, preview_path = entry.get("id"), entry.get("path")
        if preview_id in seen_ids:
            errors.append(f"{manifest_path}: duplicate preview id {preview_id!r}")
            continue
        if preview_path in seen_paths:
            errors.append(f"{manifest_path}: duplicate preview path {preview_path!r}")
            continue
        seen_ids.add(preview_id)
        seen_paths.add(preview_path)
        preview = validate_schema("schemas/action-preview.schema.json", preview_path, errors)
        if preview is None:
            continue
        if preview.get("id") != preview_id:
            errors.append(f"{preview_path}: id does not match preview manifest")
        if preview.get("microbundleId") != descriptor.get("id"):
            errors.append(f"{preview_path}: microbundleId does not match descriptor")


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
            source_book = payload.get("book")
            if source_book is not None and descriptor.get("sourceBookId") != source_book.get("id"):
                errors.append(f"{descriptor_path}: sourceBookId does not match legacy compatibility payload")
            if descriptor.get("ownerRepository") != REPOSITORY:
                errors.append(f"{descriptor_path}: ownerRepository does not match repository identity")
            validate_asset_manifest(descriptor, errors)
            validate_preview_manifest(descriptor, errors)
            bundles[bundle_id] = (descriptor, payload)
        except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            errors.append(f"{descriptor_path}: {exc}")
    validate_bundle_graph(bundles, errors)
    return bundles

def validate_bundle_graph(bundles: dict[str, tuple[dict, dict]], errors: list[str]) -> None:
    """Check required local dependencies and ID uniqueness across every registered bundle."""
    known_ids = set(bundles)
    for bundle_id, (descriptor, _) in bundles.items():
        for dependency in descriptor.get("dependencies", []):
            if not dependency.get("optional", False) and dependency.get("id") not in known_ids:
                errors.append(f"{bundle_id}: unresolved required MicroBundle dependency {dependency.get('id')!r}")
    record_owners: dict[str, str] = {}
    for bundle_id, (descriptor, payload) in bundles.items():
        for collection in descriptor.get("recordCollections", []):
            for index, record in enumerate(collection_records(payload, collection)):
                if not isinstance(record, dict) or not isinstance(record.get("id"), str):
                    continue
                identifier = record["id"]
                previous = record_owners.get(identifier)
                if previous is not None:
                    if previous == bundle_id:
                        errors.append(f"{bundle_id}: duplicate record id {identifier!r} across declared collections")
                    else:
                        errors.append(f"global local-registry ID collision {identifier!r}: {previous} and {bundle_id}")
                else:
                    record_owners[identifier] = bundle_id

def resolve_view(bundles: dict[str, tuple[dict, dict]], view: dict, errors: list[str]) -> dict:
    resolved, selected_ids, used_bundles, records_by_bundle = [], set(), {}, {}
    for bundle_id, (descriptor, payload) in bundles.items():
        records = {}
        for collection in descriptor.get("recordCollections", []):
            values = collection_records(payload, collection)
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
    parser.add_argument("--check", action="store_true", help="fail if any checked-in projection is stale")
    args = parser.parse_args()
    errors, bundles = [], {}
    bundles = load_bundle_registry(errors)
    view_registry = validate_schema("schemas/rulebook-view-registry.schema.json",
                                    ".surps/views/registry.json", errors)
    if view_registry is None or not bundles:
        return report(errors)
    generated = []
    seen_ids, seen_paths, seen_outputs = set(), set(), set()
    for entry in view_registry.get("views", []):
        view_id, view_path, output_path = entry.get("id"), entry.get("path"), entry.get("output")
        if view_id in seen_ids or view_path in seen_paths or output_path in seen_outputs:
            errors.append(f".surps/views/registry.json: duplicate view identity/path/output: {view_id!r}")
            continue
        seen_ids.add(view_id); seen_paths.add(view_path); seen_outputs.add(output_path)
        view = validate_schema("schemas/rulebook-view.schema.json", view_path, errors)
        if view is None:
            continue
        if view.get("id") != view_id:
            errors.append(f"{view_path}: id does not match view registry")
        try:
            descriptor_path = entry.get("bookDescriptor")
            if descriptor_path:
                descriptor = load(descriptor_path)
                manifest = load(".surps/participation.json")
                book_id = view.get("bookId")
                participation = next((item for item in manifest.get("books", [])
                                      if item.get("id") == book_id), None)
                if participation is None:
                    errors.append(f"{view_path}: bookId is not registered in participation manifest")
                else:
                    if descriptor.get("id") != book_id or descriptor.get("lod") != view.get("lod"):
                        errors.append(f"{view_path}: view identity/LOD does not match book descriptor")
                    primary_view = descriptor.get("viewPath")
                    if participation.get("viewPath") != primary_view:
                        errors.append(f"{view_path}: book descriptor/participation primary viewPath mismatch")
                    registered_view_paths = {item.get("path") for item in view_registry.get("views", [])}
                    if primary_view not in registered_view_paths:
                        errors.append(f"{view_path}: book descriptor primary view is not registered")
                    registry_paths = {item["path"] for item in load(REGISTRY_PATH)["microbundles"]}
                    if participation.get("microbundlePath") not in registry_paths:
                        errors.append(f"{view_path}: participation MicroBundle path is not in local registry")
            projection = resolve_view(bundles, view, errors)
            resolved_output = (ROOT / output_path).resolve()
            if ROOT.resolve() not in resolved_output.parents:
                errors.append(f"{view_path}: output path escapes repository: {output_path}")
                continue
            rendered = json.dumps(projection, indent=2, ensure_ascii=False) + "\n"
            generated.append((output_path, rendered, len(projection["records"])))
        except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            errors.append(f"{view_path}: {exc}")
    if errors:
        return report(errors)
    for output_path, rendered, _ in generated:
        output = ROOT / output_path
        if args.check:
            if not output.is_file() or output.read_text(encoding="utf-8") != rendered:
                errors.append(f"{output_path} is missing or stale; run python3 scripts/validate_surps_ontology_views.py")
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(rendered, encoding="utf-8")
    if errors:
        return report(errors)
    total_records = sum(count for _, _, count in generated)
    print(f"SURPS ontology/view validation passed: {len(bundles)} registered MicroBundle(s), {len(generated)} view(s), {total_records} projected record selections.")
    print(f"Deterministic projections {'verified' if args.check else 'generated'}: {len(generated)}")
    return 0

def report(errors: list[str]) -> int:
    print("SURPS ontology/view validation FAILED:")
    for error in errors:
        print(f" - {error}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
