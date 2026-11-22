# Rulebook Identity, Titles, and Covers

## Purpose

Every SURPS rulebook must have one authoritative identity record. The record supplies the values used to render its title, LOD badge, cover page, catalogue entry, and future package metadata. Authors must not independently retype those values in several places.

The Workshop moniker identifies the creator/publisher presentation and remains above the book. It is not part of the canonical book title.

## Canonical title

Render every book title using this exact pattern:

`Singularity Universal Roleplaying System - {Category} - LOD {N} - {Rulebook Title}`

For example:

`Singularity Universal Roleplaying System - Domain - LOD 1 - Dungeons and Underground`

The category is a controlled classification, not free-form prose. Initial categories:

- `Core` — the shared core rulebook.
- `Domain` — a domain knowledge/sourcebook.
- `Setting` — a setting, era, genre, or world-specific book.
- `Campaign` — a campaign or scenario collection.
- `Supplement` — a focused optional supplement.

New categories should be added deliberately to this list and to the validator's allowed values. Category and LOD are separate dimensions: category describes what kind of book it is; LOD describes its declared detail/fidelity level.

## Single source of truth

Each book has a machine-readable descriptor beside its sourcebook:

`docs/books/{slug}.book.json`

The descriptor contains stable identity, category, numeric LOD, human-facing rulebook title, version, cover path, and LOD badge path. The canonical title is derived from category, LOD, and rulebook title using the exact pattern above. Do not store a separately editable canonical-title string.

The Markdown sourcebook's first H1 must match the descriptor's canonical title. The catalogue must use the same descriptor values. A future build/authoring tool should render the title and cover page directly from the descriptor rather than ask authors to re-enter them.

## Required cover

Every published or CI-admissible rulebook must have a cover image. A title page is incomplete if the image is missing, empty, broken, or points outside the book's checked-in assets.

- Store covers under `docs/books/covers/{slug}.svg` (or a supported raster format when appropriate).
- The descriptor's `cover` value is a repository-relative path and must resolve to a non-empty file.
- SVG covers must be valid, accessible, and self-contained; raster covers must use a supported, documented format.
- A generic placeholder is not a finished cover. The book must have a deliberate image that communicates its subject.
- The cover page presents, in order: Workshop moniker/creator identity, canonical rulebook title, LOD badge, and cover artwork. The moniker is the publisher identity, not an extra title segment.
- The cover artwork is distinct from the small LOD badge. The badge communicates classification and level; the cover image communicates the book's subject and visual identity.

## LOD badge

Use the shared SVG badge family at `docs/assets/rulebook-lod-{N}.svg`. The numeric LOD in the descriptor must match the badge filename and visible badge text. Extend the family as needed; do not substitute a badge from another level.

## Validation requirements

The SURPS authoring/build checks should fail closed when any of these conditions is true:

1. A descriptor is missing, malformed, or has an unsupported schema version.
2. Stable ID, category, LOD, title, or version is missing or invalid.
3. Category is not in the controlled category list.
4. LOD is not a non-negative integer.
5. The canonical title computed from the descriptor does not match the sourcebook H1.
6. The referenced cover is absent, empty, unsupported, or invalid.
7. The referenced LOD badge is absent or its filename/visible LOD does not match the descriptor.
8. A catalogue entry references a missing descriptor or disagrees with it.

The checks should report the book ID, offending field/path, and expected value. A failed check must not silently substitute a generic cover or infer an LOD.

CiAi may observe and normalize the resulting workflow evidence. CiAi does not own the SURPS title/cover schema, alter the rulebook data, or grant publication/deployment approval. SURPS owns the content contract; the SURPS workflow owns its validation; the host/human remains responsible for any separate release or deployment authorization.

## Current book descriptor

Dungeons and Underground is the first descriptor-backed sourcebook:

- ID: `surps.domain.dungeons-and-underground`
- Category: `Domain`
- LOD: `1`
- Rulebook title: `Dungeons and Underground`
- Canonical title: `Singularity Universal Roleplaying System - Domain - LOD 1 - Dungeons and Underground`

Its cover is `docs/books/covers/dungeons-and-underground.svg`, and its badge is `docs/assets/rulebook-lod-1.svg`.

This establishes the editorial and metadata contract. The automated fail-closed checks are a follow-on implementation task and must be proven in CI before the repository claims enforcement.
