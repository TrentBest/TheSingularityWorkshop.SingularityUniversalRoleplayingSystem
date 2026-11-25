# SURPS Living Surfaces, Maps, and Tile Contract

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

## Purpose

SURPS publishes reusable visual surfaces as SVG. A surface may be printed, embedded in a book, displayed in a browser, or used as the presentation layer of an interactive experience. The same asset must remain understandable when animation and scripting are unavailable.

This contract extends the [Living Character Sheets and World Surfaces](living-world-and-character-studio.md) direction with a discoverable map-template and semantic-tile catalog.

## Three layers; never conflate them

1. **Canonical content** — characters, places, topology, rules, inventories, ownership, and events. These are structured SURPS/domain records and are never stored only in SVG.
2. **Surface definition** — SVG geometry, semantic element IDs, theme tokens, labels, accessibility text, and optional animation. SVG is a view/template, not the canonical record.
3. **Runtime projection** — a host binds canonical records to stable SVG targets and may animate presentation. Commands go back through the owning domain; SVG never mutates authoritative state.

An ambient river animation does not imply water simulation. A moving traveler does not imply an NPC, pathfinding, or a completed journey. A shop illustration does not imply stock, sales, or a shopkeeper entity.

## Asset families

### Character sheets

The existing `docs/assets/character-sheets/catalog.json` is the theme registry. The five initial themes (Verdant, Stone, Woodwright, Aegis, and Aether) are intentionally blank presentation templates. Preserve their shared semantic field targets when adding themes so the same character projection can populate every theme.

### Maps

Map templates are intentionally empty surfaces. They define composition, coordinate space, scale hints, and optional grid/region overlays—not pre-authored geography.

Initial template roles:

- **World** — large-scale world canvas; continents, oceans, climate and political overlays are optional layers.
- **Region** — terrain and route canvas with nested settlement/site anchors.
- **Encounter** — tactical/local canvas with a configurable grid and placement anchors.

Nested maps preserve stable place identity. A child map is a detail view of a parent anchor, not a duplicate place. Transform/coordinate metadata must make the relationship explicit.

### Tiles

A tile is a reusable semantic visual component with a stable ID, kind, footprint, connection/edge semantics, accessibility label, and SVG asset. Tiles are not just pictures. A road tile declares which edges connect; a river tile declares flow/continuity connection points; a bridge declares what it crosses and which approaches connect.

Initial tile families should include terrain (water, grass, forest, mountain, desert), routes (road, path, bridge), and built environment (settlement, building, landmark). Additional packs can contribute their own namespaced IDs without replacing core tiles.

Tile rotation and mirroring are presentation transforms. They must preserve the tile's declared connection semantics. A map validator should reject incompatible joins or report them as deliberate authored exceptions.

## SVG authoring requirements

- Use a `viewBox`; avoid fixed pixel assumptions.
- Include `title`, `desc`, and an appropriate `role`/accessible name.
- Give bindable semantic groups stable, namespaced IDs (for example `surps-map-water`, `surps-tile-road`, `surps-character-identity-name`).
- Keep labels and data targets separate from decorative geometry.
- Use SVG/CSS animation only for ambient presentation. Respect `prefers-reduced-motion`; provide a static equivalent.
- Keep print-safe contrast and ensure the asset remains legible without animation.
- Do not embed secrets, remote executable scripts, or authoritative game state in an SVG.
- Keep theme styling separate from semantic identity wherever possible.

## Catalog and extension rules

Each catalog entry has a stable namespaced ID, display name, kind/role, asset path, description, tags, and version. Tile entries additionally declare footprint and edge/connection semantics. Map-template entries declare coordinate space and intended scale. New content is additive; an extension must not redefine an existing ID.

Books and experiences select assets by ID and version, not by copying SVG markup. A book may provide an alternate view or theme, but it must retain source attribution and a resolvable reference to the canonical asset.

## CiAi adoption contract

When CiAi enrolls a repository into SURPS, it should:

1. Inspect existing Markdown, JSON, SVG, and image assets before generating anything.
2. Preserve existing content and provenance; propose repackaging rather than destructively moving source material.
3. Identify candidate book ownership, canonical record IDs, and asset roles.
4. Reuse shared records by reference. When the same rule or concept appears in multiple books, emit a reference to its canonical record and the other book/view.
5. Require an explicit, scoped override to change behavior. An override names the base record, its scope, the replacing record, rationale, and precedence. Example: a Spy-vs-Spy Russia book may explicitly overload the shared Spying procedure for its declared setting, while the US book retains the base behavior.
6. Generate or update book descriptors and required Markdown identity/header fragments from descriptor data. Do not invent titles, LOD, attribution, or publication status.
7. Validate all references, overrides, asset paths, IDs, schema versions, and generated outputs. Fail closed on ambiguity; report the source path and suggested resolution.
8. Produce a reviewable migration plan and deterministic evidence. CiAi may prepare changes and report evidence; it does not silently approve publication or release.

### Cross-book resolution

A repeated concept is not a second definition by default. Its record identity is canonical and reusable. A view may explain the same record differently for its audience, but a mechanical change requires an explicit override. LOD is descriptive detail, not precedence. Load order is never precedence.

An override must declare:

- `targetRecordId`: canonical record being specialized;
- `overrideRecordId`: stable identity of the specialization;
- `scope`: book, campaign, setting, geography, or experience boundary;
- `reason`: why the specialization exists;
- `precedencePolicy`: explicit policy identifier;
- `sourceBook` and version: provenance.

Two applicable overrides that conflict without a declared resolution are a validation error, not a last-write-wins merge.

## Publication identity

A Markdown document that represents a sourcebook must carry the canonical book identity/header derived from its `.book.json` descriptor. The descriptor is authoritative for title, category, LOD, version, cover, publisher, and provenance. Generators must calculate relative paths from the target Markdown file's directory. Ordinary technical notes should not be falsely presented as books; book membership must be explicit in the catalog/descriptor.

## Current maturity

The character-sheet theme catalog and Character Studio preview exist. A settlement ambient SVG is an illustrative prototype. This document defines the map/tile extension contract; a full map editor, topology validator, tile composer, dynamic domain binding, and simulation remain future implementation stages.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
