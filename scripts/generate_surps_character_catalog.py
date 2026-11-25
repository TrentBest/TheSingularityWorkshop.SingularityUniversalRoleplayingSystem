from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".surps" / "microbundles" / "registry.json"
OUTPUT = ROOT / "docs" / "assets" / "character-catalog.json"
COLLECTIONS = ("characterOptions", "traits", "capabilities", "equipment", "resources", "creations")


def read_repository_json(root: Path, relative_path: str, context: str) -> dict[str, Any]:
    """Read a repository-owned JSON document without allowing path traversal."""
    if not isinstance(relative_path, str) or not relative_path.strip():
        raise ValueError(f"{context}: expected a non-empty repository-relative path")
    candidate = (root / relative_path).resolve()
    if root.resolve() not in candidate.parents:
        raise ValueError(f"{context}: path escapes the repository: {relative_path}")
    try:
        value = json.loads(candidate.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{context} ({relative_path}): {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{context} ({relative_path}): expected a JSON object")
    return value


def build_catalog(root: Path = ROOT) -> dict[str, Any]:
    """Build the Character Studio catalog from registered canonical MicroBundles."""
    registry = read_repository_json(
        root, ".surps/microbundles/registry.json", "MicroBundle registry"
    )
    repository = registry.get("repository")
    if not isinstance(repository, str) or not repository.strip():
        raise ValueError("MicroBundle registry: repository identity is required")
    entries = registry.get("microbundles")
    if not isinstance(entries, list):
        raise ValueError("MicroBundle registry: microbundles must be an array")

    records: dict[str, list[dict[str, Any]]] = {name: [] for name in COLLECTIONS}
    seen_bundle_ids: set[str] = set()
    seen_record_ids: dict[str, str] = {}

    for index, entry in enumerate(entries):
        context = f"MicroBundle registry entry {index}"
        if not isinstance(entry, dict):
            raise ValueError(f"{context}: expected an object")
        bundle_id = entry.get("id")
        if not isinstance(bundle_id, str) or not bundle_id.strip():
            raise ValueError(f"{context}: stable bundle ID is required")
        if bundle_id in seen_bundle_ids:
            raise ValueError(f"{context}: duplicate MicroBundle ID {bundle_id!r}")
        seen_bundle_ids.add(bundle_id)

        descriptor = read_repository_json(root, entry.get("path"), context)
        if descriptor.get("id") != bundle_id:
            raise ValueError(f"{context}: registry/descriptor identity mismatch")
        if descriptor.get("ownerRepository") != repository:
            raise ValueError(f"{context}: ownerRepository does not match registry repository")
        version = descriptor.get("version")
        if not isinstance(version, str) or not version.strip():
            raise ValueError(f"{context}: MicroBundle version is required")

        content_path = descriptor.get("contentPath")
        content = read_repository_json(root, content_path, f"{bundle_id} content")
        declared_collections = descriptor.get("recordCollections")
        if not isinstance(declared_collections, list) or not declared_collections:
            raise ValueError(f"{bundle_id}: recordCollections must be a non-empty array")
        if any(not isinstance(name, str) or not name.strip() for name in declared_collections):
            raise ValueError(f"{bundle_id}: recordCollections entries must be non-empty strings")
        if len(set(declared_collections)) != len(declared_collections):
            raise ValueError(f"{bundle_id}: recordCollections must not contain duplicates")
        unknown_collections = set(declared_collections) - set(COLLECTIONS) - {"extensions", "rules"}
        if unknown_collections:
            raise ValueError(
                f"{bundle_id}: unsupported record collection(s): {sorted(unknown_collections)}"
            )

        # Validate every declared canonical record collection, including rules and
        # extensions. Only the Character Studio collections are projected to the
        # picker; the others still participate in global identity integrity.
        for collection in declared_collections:
            values = content.get(collection, [])
            if not isinstance(values, list):
                raise ValueError(f"{bundle_id}: content collection {collection!r} must be an array")
            for record_index, record in enumerate(values):
                location = f"{bundle_id}:{collection}[{record_index}]"
                if not isinstance(record, dict):
                    raise ValueError(f"{location}: expected a record object")
                record_id = record.get("id")
                if not isinstance(record_id, str) or not record_id.strip():
                    raise ValueError(f"{location}: stable record ID is required")
                previous = seen_record_ids.get(record_id)
                if previous is not None:
                    raise ValueError(
                        f"duplicate canonical record ID {record_id!r}: {previous} and {location}"
                    )
                seen_record_ids[record_id] = location
                if collection in records:
                    records[collection].append({
                        **record,
                        "source": {
                            "microbundleId": bundle_id,
                            "microbundleVersion": version,
                            "ownerRepository": repository,
                            "contentPath": content_path,
                        },
                    })

    return {
        "schemaVersion": 1,
        "authority": "SURPS registered MicroBundle catalog",
        "collections": records,
    }


def main() -> None:
    payload = build_catalog()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    count = sum(map(len, payload["collections"].values()))
    print(
        f"Generated {OUTPUT.relative_to(ROOT)} with {count} selectable records "
        f"across {len(COLLECTIONS)} collections."
    )


if __name__ == "__main__":
    main()
