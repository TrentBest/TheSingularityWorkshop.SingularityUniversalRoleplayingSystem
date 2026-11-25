from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / ".surps" / "microbundles" / "registry.json"
OUTPUT = ROOT / "docs" / "assets" / "character-catalog.json"
COLLECTIONS = ("characterOptions", "traits", "capabilities", "equipment", "resources", "creations")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    records: dict[str, list[dict]] = {name: [] for name in COLLECTIONS}
    seen: set[tuple[str, str]] = set()

    for entry in registry.get("microbundles", []):
        descriptor_path = ROOT / entry["path"]
        descriptor = json.loads(descriptor_path.read_text(encoding="utf-8"))
        if descriptor.get("id") != entry.get("id"):
            raise ValueError(f"Registry/descriptor identity mismatch: {entry['path']}")
        content_path = ROOT / descriptor["contentPath"]
        content = json.loads(content_path.read_text(encoding="utf-8"))
        for collection in COLLECTIONS:
            for record in content.get(collection, []):
                record_id = record.get("id")
                if not isinstance(record_id, str) or not record_id:
                    raise ValueError(f"Missing stable ID in {content_path}:{collection}")
                key = (collection, record_id)
                if key in seen:
                    raise ValueError(f"Duplicate catalog record: {key}")
                seen.add(key)
                records[collection].append({
                    **record,
                    "source": {
                        "microbundleId": descriptor["id"],
                        "microbundleVersion": descriptor["version"],
                        "ownerRepository": descriptor["ownerRepository"],
                        "contentPath": descriptor["contentPath"],
                    },
                })

    payload = {
        "schemaVersion": 1,
        "authority": "SURPS registered MicroBundle catalog",
        "collections": records,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    count = sum(map(len, records.values()))
    print(f"Generated {OUTPUT.relative_to(ROOT)} with {count} selectable records across {len(COLLECTIONS)} collections.")


if __name__ == "__main__":
    main()
