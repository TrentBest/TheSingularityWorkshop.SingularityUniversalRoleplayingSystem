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


def validate_backlog(errors: list[str]) -> tuple[int, int]:
    path = ROOT / ".surps" / "rulebook-backlog.json"
    backlog = load_json(path, errors)
    if backlog is None:
        return 0, 0
    if backlog.get("schemaVersion") != 1:
        fail(errors, "rulebook-backlog.json: unsupported schemaVersion (expected 1)")
    if backlog.get("registryId") != "surps.rulebook.master-backlog":
        fail(errors, "rulebook-backlog.json: unexpected registryId")
    authority = backlog.get("authority")
    if not isinstance(authority, dict) or authority.get("repository") != "TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem" or authority.get("branch") != "development":
        fail(errors, "rulebook-backlog.json: authority must point to this repository's development branch")

    repositories = backlog.get("repositories")
    if not isinstance(repositories, list) or not repositories:
        fail(errors, "rulebook-backlog.json: repositories must be a non-empty array")
        repositories = []
    repo_ids: set[str] = set()
    repo_names: set[str] = set()
    repositories_by_id: dict[str, dict] = {}
    for index, entry in enumerate(repositories):
        label = f"rulebook-backlog.json: repositories[{index}]"
        if not isinstance(entry, dict):
            fail(errors, f"{label} must be an object")
            continue
        repo_id, full_name = entry.get("id"), entry.get("repository")
        if not isinstance(repo_id, str) or not repo_id.strip() or repo_id in repo_ids:
            fail(errors, f"{label}.id must be a unique non-empty string")
        else:
            repo_ids.add(repo_id)
            repositories_by_id[repo_id] = entry
        if full_name is not None and (not isinstance(full_name, str) or "/" not in full_name or full_name in repo_names):
            fail(errors, f"{label}.repository must be a unique owner/repository name or null")
        elif isinstance(full_name, str):
            repo_names.add(full_name)
        if entry.get("status") == "active" and (not entry.get("participationManifest") or not entry.get("catalogue")):
            fail(errors, f"{label}: active repositories must declare participationManifest and catalogue")
        if entry.get("status") == "active" and repo_id != "surps":
            evidence = entry.get("admissionEvidence")
            if not isinstance(evidence, dict):
                fail(errors, f"{label}: external active repositories require admissionEvidence")
            else:
                expected_manifest = f"https://github.com/{full_name}/blob/development/{entry.get('participationManifest')}"
                expected_catalogue = f"https://github.com/{full_name}/blob/development/{entry.get('catalogue')}"
                if evidence.get("branch") != "development":
                    fail(errors, f"{label}.admissionEvidence.branch must be development")
                if evidence.get("manifestUrl") != expected_manifest:
                    fail(errors, f"{label}.admissionEvidence.manifestUrl must point to the declared development manifest")
                if evidence.get("catalogueUrl") != expected_catalogue:
                    fail(errors, f"{label}.admissionEvidence.catalogueUrl must point to the declared development catalogue")
                for field in ("manifestBlobSha", "catalogueBlobSha"):
                    value = evidence.get(field)
                    if not isinstance(value, str) or len(value) != 40 or any(char not in "0123456789abcdef" for char in value):
                        fail(errors, f"{label}.admissionEvidence.{field} must be a 40-character lowercase Git blob SHA")
                verified_at = evidence.get("verifiedAt")
                if not isinstance(verified_at, str) or len(verified_at) != 10 or verified_at[4:5] != "-" or verified_at[7:8] != "-":
                    fail(errors, f"{label}.admissionEvidence.verifiedAt must use YYYY-MM-DD")
                if not isinstance(evidence.get("verifiedBy"), str) or not evidence.get("verifiedBy", "").strip():
                    fail(errors, f"{label}.admissionEvidence.verifiedBy must identify the admission reviewer")
        coordination_issue = entry.get("coordinationIssue")
        if coordination_issue is not None and (not isinstance(coordination_issue, str) or not coordination_issue.startswith("https://github.com/")):
            fail(errors, f"{label}.coordinationIssue must be an absolute GitHub HTTPS URL or null")

    books = backlog.get("books")
    if not isinstance(books, list) or not books:
        fail(errors, "rulebook-backlog.json: books must be a non-empty array")
        books = []
    book_ids: set[str] = set()
    for index, entry in enumerate(books):
        label = f"rulebook-backlog.json: books[{index}]"
        if not isinstance(entry, dict):
            fail(errors, f"{label} must be an object")
            continue
        book_id, family_id, title = entry.get("id"), entry.get("familyId"), entry.get("title")
        if not isinstance(book_id, str) or not book_id.strip() or book_id in book_ids:
            fail(errors, f"{label}.id must be a unique non-empty string")
        else:
            book_ids.add(book_id)
        if not isinstance(family_id, str) or not family_id.strip():
            fail(errors, f"{label}.familyId must be a non-empty string")
        if not isinstance(title, str) or not title.strip():
            fail(errors, f"{label}.title must be a non-empty string")
        lod = entry.get("lod")
        if not isinstance(lod, int) or isinstance(lod, bool) or lod < 0:
            fail(errors, f"{label}.lod must be a non-negative integer")
        owner = entry.get("ownerRepository")
        if owner is not None and owner not in repo_ids:
            fail(errors, f"{label}.ownerRepository references unknown repository id: {owner}")
        candidate_owner = entry.get("candidateOwnerRepository")
        if candidate_owner is not None and candidate_owner not in repo_ids:
            fail(errors, f"{label}.candidateOwnerRepository references unknown repository id: {candidate_owner}")
        contributors = entry.get("contributors", [])
        if not isinstance(contributors, list) or any(item not in repo_ids for item in contributors):
            fail(errors, f"{label}.contributors must reference registered repository ids")
        url = entry.get("bookUrl")
        if url is not None and (not isinstance(url, str) or not url.startswith("https://")):
            fail(errors, f"{label}.bookUrl must be an absolute HTTPS URL or null")
        ownership = entry.get("ownership")
        if not isinstance(ownership, dict) or ownership.get("claimStatus") not in {"unclaimed", "pending", "accepted"}:
            fail(errors, f"{label}.ownership.claimStatus must be unclaimed, pending, or accepted")
        elif ownership.get("claimStatus") == "accepted" and (owner is None or not ownership.get("agent") or not ownership.get("agentRepository")):
            fail(errors, f"{label}: accepted ownership requires ownerRepository, agentRepository, and agent identity")
        elif ownership.get("claimStatus") == "accepted" and owner in repositories_by_id and ownership.get("agentRepository") != repositories_by_id[owner].get("repository"):
            fail(errors, f"{label}: agentRepository must match the accepted owner repository")
        elif ownership.get("claimStatus") == "pending" and (owner is None or not ownership.get("agent") or not ownership.get("agentRepository") or not ownership.get("claimedAt")):
            fail(errors, f"{label}: pending ownership requires ownerRepository, agentRepository, agent, and claimedAt")
        elif ownership.get("claimStatus") == "pending" and owner in repositories_by_id and ownership.get("agentRepository") != repositories_by_id[owner].get("repository"):
            fail(errors, f"{label}: agentRepository must match the claimed owner repository")
    book_owner_by_id = {
        entry.get("id"): entry.get("ownerRepository")
        for entry in books
        if isinstance(entry, dict) and isinstance(entry.get("id"), str)
    }
    for index, entry in enumerate(repositories):
        if not isinstance(entry, dict) or entry.get("status") != "active" or entry.get("id") == "surps":
            continue
        evidence = entry.get("admissionEvidence")
        if not isinstance(evidence, dict):
            continue
        registered_ids = evidence.get("registeredBookIds")
        label = f"rulebook-backlog.json: repositories[{index}].admissionEvidence"
        if not isinstance(registered_ids, list) or not registered_ids:
            fail(errors, f"{label}.registeredBookIds must be a non-empty array")
            continue
        if any(not isinstance(book_id, str) or not book_id.strip() for book_id in registered_ids):
            fail(errors, f"{label}.registeredBookIds entries must be non-empty strings")
            continue
        if len(registered_ids) != len(set(registered_ids)):
            fail(errors, f"{label}.registeredBookIds must not contain duplicates")
        for book_id in registered_ids:
            if book_owner_by_id.get(book_id) != entry.get("id"):
                fail(errors, f"{label}: book {book_id!r} must exist in the registry and be owned by {entry.get('id')!r}")
    return len(repositories), len(books)


def main() -> int:
    errors: list[str] = []
    repository_count, backlog_count = validate_backlog(errors)
    manifest = load_json(MANIFEST_PATH, errors)
    if manifest is None:
        return 1

    if manifest.get("schemaVersion") != 1:
        fail(errors, "participation.json: unsupported schemaVersion (expected 1)")
    if manifest.get("repository") != "TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem":
        fail(errors, "participation.json: repository identity does not match this repository")

    backlog = load_json(ROOT / ".surps" / "rulebook-backlog.json", errors)
    registry_books = (backlog or {}).get("books", [])
    if not isinstance(registry_books, list):
        registry_books = []
    registry_owned_ids = {
        entry.get("id")
        for entry in registry_books
        if isinstance(entry, dict) and entry.get("ownerRepository") == "surps"
    }
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
        if isinstance(book_id, str) and book_id not in registry_owned_ids:
            fail(errors, f"{label}.id is not registered as SURPS-owned in the master backlog: {book_id}")
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
    print(f"SURPS master backlog validation passed: {backlog_count} books and {repository_count} repositories.")
    print("Identity, version, LOD, sourcebook, cover, and LOD badge references are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
