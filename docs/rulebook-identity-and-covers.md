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

The descriptor contains stable identity, publisher identity and moniker reference, category, numeric LOD, human-facing rulebook title, version, cover path, and LOD badge path. The canonical title is derived from category, LOD, and rulebook title using the exact pattern above. Do not store a separately editable canonical-title string.

The Markdown sourcebook's first H1 must match the descriptor's canonical title. The catalogue must use the same descriptor values. The first descriptor-driven publishing generator now exists at `scripts/generate_surps_book_assets.py`. It renders the cover SVG and acknowledgements page from an opted-in descriptor. This is an initial pilot, not yet the complete publication pipeline; generated outputs are checked for staleness in CI.

## Required cover

Every published or CI-admissible rulebook must have a cover image. A title page is incomplete if the image is missing, empty, broken, or points outside the book's checked-in assets.

- Store covers under `docs/books/covers/{slug}.svg` (or a supported raster format when appropriate).
- The descriptor's `cover` value is a repository-relative path and must resolve to a non-empty file.
- SVG covers must be valid, accessible, and self-contained; raster covers must use a supported, documented format.
- A generic placeholder is not a finished cover. The book must have a deliberate image that communicates its subject.
- The cover page presents, in order: the Workshop's canonical animated moniker/creator identity, canonical rulebook title, LOD badge, and cover artwork. The moniker reference is recorded in the descriptor so the presentation does not depend on authors finding or retyping an asset URL. The moniker is the publisher identity, not an extra title segment.
- The cover artwork is distinct from the small LOD badge. The badge communicates classification and level; the cover image communicates the book's subject and visual identity.

## Descriptor-driven publication opt-in\n\nA book opts into the first automated asset pass by setting `publication.generate: true` in its entry in `.surps/participation.json`. The descriptor declares `coverArtwork`, `cover`, `lodBadge`, and `acknowledgementsPath`. The generator reads only opted-in entries by default and supports `--check` for deterministic CI verification.\n\nThe initial pilot is CORE Spying. Its subject artwork is separate from the generated cover frame; the generated cover combines that artwork with canonical publisher text, category, LOD badge, title, and edition. The generated acknowledgements page records only descriptor-supplied contributor, rights, and provenance data. An empty contributor list is reported honestly; no author or permission is inferred.\n\nThe animated Workshop moniker remains the publisher identity at the top of the Markdown book presentation. The SVG cover uses a static publisher wordmark so the artwork remains a portable image; the title-page composition and SVG are separate presentation layers.\n\nTracking and next stages: [SURPS automated book publishing issue #14](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/issues/14).\n\n## LOD badge

Use the shared SVG badge family at `docs/assets/rulebook-lod-{N}.svg`. The numeric LOD in the descriptor must match the badge filename and visible badge text. Extend the family as needed; do not substitute a badge from another level.

## Applying the presentation to Markdown

The presentation is not a README feature. Any authored Markdown file may carry the same document identity, LOD badge, and cover/title presentation when that document represents the rulebook or a deliberate excerpt/entry for it.

- The book descriptor remains the source of truth; do not copy editable title/category/LOD values into each Markdown file.
- Keep the LOD badge and cover artwork as separate image roles with meaningful alt text.
- Place the canonical moniker/creator identity above the canonical book title, then the LOD badge and cover artwork.
- A Markdown generator must receive the target Markdown path as well as the descriptor. It must calculate each relative asset URL from the target file's directory; it must never assume the target is `README.md` or that all Markdown lives at the repository root.
- GitHub-flavored Markdown has no portable native include mechanism. Until the shared GUI badge composition/Markdown adapter is available, author the small Markdown fragment explicitly or generate it in the consuming repository's build. Do not invent a `WithBadge` API or claim a shared renderer exists before GUI implements and tests it.
- The shared GUI presentation contract is tracked in [GUI issue #86](https://github.com/TrentBest/TheSingularityWorkshop.GUI/issues/86); SURPS adoption is tracked in [SURPS issue #3](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/issues/3).

## Validation requirements

The SURPS authoring/build checks should fail closed when any of these conditions is true:

1. A descriptor is missing, malformed, or has an unsupported schema version.
2. Stable ID, publisher identity/moniker reference, category, LOD, title, or version is missing or invalid.
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

Dungeons and Underground remains the first descriptor-backed sourcebook. CORE Spying is the first pilot for descriptor-driven cover and acknowledgements generation. The remaining book family (chapter openers, dividers, diagrams, callouts, credits/colophon, print/PDF layouts) is still being designed and must be reviewed before the system is called publication-ready.
