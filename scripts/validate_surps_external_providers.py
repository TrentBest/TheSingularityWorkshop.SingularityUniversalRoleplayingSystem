#!/usr/bin/env python3
"""Validate pinned external MicroBundle provider manifests and emit a provenance catalog."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ".surps/external-providers/registry.json"
SCHEMA = "schemas/external-provider-registry.schema.json"
OUTPUT = "docs/generated/external-provider-catalog.json"

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", required=True, help="Checkout root for pinned external provider repositories")
    parser.add_argument("--check", action="store_true", help="Fail if generated catalog is stale")
    args = parser.parse_args()
    errors: list[str] = []
    try:
        schema = read_json(ROOT / SCHEMA)
        registry = read_json(ROOT / REGISTRY)
        Draft202012Validator.check_schema(schema)
        errors.extend(f"{REGISTRY}: {e.message}" for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(registry))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        return report([str(exc)])
    source_root = Path(args.source_root).resolve()
    sources = []
    for source in registry.get("sources", []):
        repository = source["repository"]
        bundles = []
        for expected in source.get("bundles", []):
            relative = Path(expected["path"])
            path = (source_root / relative).resolve()
            if source_root not in path.parents:
                errors.append(f"{repository}: provider path escapes checkout: {relative}")
                continue
            try:
                manifest = read_json(path)
            except (OSError, UnicodeError, json.JSONDecodeError) as exc:
                errors.append(f"{repository}/{relative}: {exc}")
                continue
            bundle = manifest.get("bundle", {})
            capability = manifest.get("capability", {})
            evidence = manifest.get("evidence", {})
            actual_providers = bundle.get("providerIds", [])
            if bundle.get("id") != expected["bundleId"]:
                errors.append(f"{repository}/{relative}: bundle ID mismatch")
            if sorted(actual_providers) != sorted(expected["providerIds"]):
                errors.append(f"{repository}/{relative}: provider IDs do not match pinned registry")
            if not capability.get("id") or capability.get("id") not in actual_providers:
                errors.append(f"{repository}/{relative}: capability ID is not declared by bundle")
            if evidence.get("status") not in {"specified", "partial", "implemented", "experimental", "deprecated"}:
                errors.append(f"{repository}/{relative}: missing or invalid evidence status")
            if not manifest.get("ontology", {}).get("domain"):
                errors.append(f"{repository}/{relative}: ontology domain is missing")
            if errors:
                continue
            bundles.append({
                "bundleId": bundle["id"], "version": bundle.get("version"),
                "name": bundle.get("name"), "providerIds": actual_providers,
                "domain": manifest["ontology"]["domain"],
                "branch": manifest["ontology"].get("branch"),
                "subdomain": manifest["ontology"].get("subdomain"),
                "capability": capability,
                "evidence": evidence,
                "sourcePath": expected["path"]
            })
        sources.append({"repository": repository, "commit": source["commit"], "bundles": bundles})
    if errors:
        return report(errors)
    catalog = {"schemaVersion": 1, "catalogueKind": "external-provider-discovery",
               "authorityNote": "Provider metadata is discovered from pinned owner-repository manifests. This catalog does not copy domain records or claim runtime resolution.",
               "sources": sources}
    rendered = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"
    output = ROOT / OUTPUT
    if args.check:
        if not output.is_file() or output.read_text(encoding="utf-8") != rendered:
            return report([f"{OUTPUT} is missing or stale; regenerate the external provider catalog"])
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    count = sum(len(item["bundles"]) for item in sources)
    print(f"External provider validation passed: {len(sources)} pinned source(s), {count} bundle(s).")
    print(f"Deterministic provider catalog {'verified' if args.check else 'generated'}: {OUTPUT}")
    return 0

def report(errors: list[str]) -> int:
    print("SURPS external provider validation FAILED:")
    for error in errors:
        print(f" - {error}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
