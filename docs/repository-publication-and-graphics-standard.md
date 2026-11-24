# Participating Repository Publication and Graphics Standard

> **Canonical policy:** The shared Workshop policy now lives in [FSM_COS `DOCUMENTATION_STANDARD.md`](https://github.com/TrentBest/TheSingularityWorkshop.FSM_COS/blob/development/DOCUMENTATION_STANDARD.md). This SURPS document is a domain-specific adoption companion, not a competing cross-repository standard. SURPS book identity remains governed by the [Rulebook Identity, Titles, and Covers standard](rulebook-identity-and-covers.md).

**Status:** proposed ecosystem standard, effective for new work after domain-owner review. Existing repositories are migrated incrementally; this document does not authorize bulk moves or delete established content.

## 1. Goals and boundaries

For SURPS-facing books and Pages experiences, this companion is supplemented by the normative [SURPS Living Rulebook and Experience Standard](living-rulebook-standard.md) and [Behavior Model and Adapters](behavior-and-adapters.md). Those documents define the one-behavior/two-adapter model, player and Game Master reading paths, workshop-time tabletop derivation, runtime cache boundary, and evidence-labelled living demonstrations. Participating repositories must adopt them rather than inventing competing book formats.

Every SURPS-participating repository should be recognizable, navigable, accessible, and visually coherent while retaining its domain ownership and implementation needs.

This standard governs:
- publication entry points and documentation locations;
- sourcebook/book placement and metadata;
- theory, architecture, implementation, and evidence separation;
- shared visual identity, badges, diagrams, covers, and image accessibility;
- links between a domain's knowledge, its implementation, and its proof;\n- living, interactive demonstrations that make each important domain mechanic observable.

It does **not** require every repository to become a SURPS repository, move source code into a common layout, or duplicate domain documentation. A participating repository may expose a domain book, but the domain owner remains authoritative for its subject.

## 2. Repository entry points

Every participating repository should provide:

1. A root `README.md` as the human landing page.
2. A short domain statement and explicit ownership / non-ownership boundaries.
3. A five-part reader path, adapted to the domain:
   - **What** — purpose, scope, and vocabulary.
   - **Why** — theory, rationale, and domain problem.
   - **How** — architecture, contracts, and implementation.
   - **See it** — a runnable or inspectable proof, clearly labelled by maturity.
   - **Develop** — contribution, testing, branch, and release expectations.
4. A clear link to the repository's published documentation site, when one exists.
5. A clear distinction between implemented, tested, proposed, planned, and externally owned capabilities.

The root README is an index, not a second copy of the entire documentation set.

## 3. Canonical documentation locations

Use these locations for new material. Keep existing paths working during migration; do not mass-rename folders without checking links, Pages workflows, scripts, and external references.

| Location | Responsibility |
|---|---|
| `README.md` | Repository landing page and navigation |
| `docs/index.html` | Published documentation home, where GitHub Pages is used |
| `docs/books/` | Human-readable domain books, sourcebooks, and chapter collections |
| `docs/books/assets/` | Book-specific covers and artwork that should travel with the book collection |
| `docs/theory/` | Explanatory theory, history, principles, and teaching material |
| `docs/architecture/` | System boundaries, component relationships, and architectural decisions |
| `docs/standards/` | Normative contracts, conventions, schemas, and authoring standards |
| `docs/guides/` | Task-oriented user, contributor, and operator procedures |
| `docs/reference/` | API, vocabulary, catalogues, and generated/reference material |
| `docs/implementation/` | Implementation notes that do not belong beside code |
| `docs/evidence/` | Test reports, experiment records, validation evidence, and maturity claims |
| `docs/assets/diagrams/` | Shared conceptual and architecture diagrams |
| `docs/assets/images/` | General documentation imagery |
| `docs/assets/badges/` | Repository/domain/status badges, excluding centrally governed SURPS LOD badges |
| `docs/assets/dividers/` | Decorative section dividers |
| `docs/samples/` | Small documentation samples and browser demonstrations, if not better owned by a code-level samples folder |

### Naming and migration

- New folder names are lowercase and descriptive; use hyphens for multiword names.
- Preserve established public paths during incremental migration. For example, SURPS currently has `docs/Theory/`; it remains valid until a deliberate migration can update every inbound link and workflow together.
- Avoid parallel synonyms such as `images/`, `img/`, `graphics/`, and `assets/` at the same level.
- Keep source code, tests, and executable samples in their existing code-oriented locations. Documentation folders are not a substitute for project structure.
- Do not create empty folders solely to satisfy a template.
- Domain-specific books remain owned by the domain repository; SURPS's catalogue links to them rather than copying them.

## 4. Book and sourcebook placement

A domain book belongs in `docs/books/{slug}.md`. Where a machine-readable descriptor is used, place it beside the book as `{slug}.book.json`. Book-specific covers belong in `docs/books/covers/{slug}.svg` (or a supported raster format). Shared LOD badges remain in SURPS at `docs/assets/rulebook-lod-{N}.svg`.

A descriptor should be the single source of truth for stable ID, title, category, LOD, version, publisher, cover, and badge references. Do not independently retype these values into a catalogue, cover, and title page. See [Rulebook Identity, Titles, and Covers](rulebook-identity-and-covers.md).

A repository without authored books does not need an empty `docs/books/` folder.

## 5. Shared Workshop visual identity

### Publisher identity

- Use the canonical animated Workshop moniker at the top of repository landing pages and authored book title pages:
  `https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg`
- Use the canonical footer mark where a footer mark is appropriate:
  `https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png`
- Do not substitute personal avatars, unrelated logos, or ad-hoc redraws for the canonical publisher identity.
- The moniker identifies the publisher; it is not a repository title or a domain badge.

### Domain and status identity

- A domain may have its own visual mark, but it must not impersonate the Workshop publisher mark.
- Reuse canonical status badges and generated badge assets where available. Do not hand-author a badge that reports a status already owned by a workflow.
- Branch-policy badges must reflect actual branch state; do not hardcode a branch count or maturity claim.
- SURPS LOD badges are a controlled family. Do not recolor, relabel, or locally fork their meaning.

## 6. Graphics system

Every graphic must have a declared communication role:

| Role | Purpose | Typical location |
|---|---|---|
| Publisher mark | Identify The Singularity Workshop | Shared canonical URL |
| Domain mark | Identify a domain or repository | `docs/assets/` |
| Status badge | Communicate a machine-verifiable status | Generated or centrally governed asset |
| LOD badge | Communicate SURPS rulebook LOD | SURPS shared badge family |
| Cover | Establish the identity and subject of a book | `docs/books/covers/` |
| Concept diagram | Explain relationships, boundaries, or causal structure | `docs/assets/diagrams/` |
| Living illustration | Teach a process or changing state through motion | Beside its owning documentation or in `docs/assets/` |
| Evidence image | Show an actual output, measurement, or test artifact | `docs/evidence/` or generated artifact |

### SVG requirements

- Prefer SVG for diagrams, badges, covers, and scalable line art.
- Include an accessible `<title>` and `<desc>`; give the root an appropriate accessible role and reference IDs.
- Use meaningful contrast, legible type, and a viewBox that scales cleanly.
- Keep SVG self-contained; avoid remote fonts, scripts, and unnecessary external dependencies. The canonical animated Workshop moniker and canonical footer PNG are explicit publisher-identity exceptions and must use the exact shared URLs defined above.
- Animation must respect `prefers-reduced-motion` or provide an equally understandable static state.
- Do not encode essential meaning only in color, motion, or tiny text.
- Keep text labels concise; explain complex diagrams in adjacent prose.
- Use raster images for photographic or texture-heavy material where SVG is not appropriate. Prefer lossless formats for diagrams and transparent marks.
- Never use a screenshot as a substitute for an inspectable diagram when the underlying system can be represented directly.

### File naming

Use lowercase kebab-case and describe the subject or role, e.g. `npc-agency-lifecycle.svg`, `laboratory-staffing-model.svg`, `core-spying-cover.svg`. Avoid opaque names, dates in canonical filenames, and ambiguous `final2.svg` variants. Version meaningful revisions in source history or metadata, not by proliferating filenames.

### Image provenance and truthfulness

- Label conceptual artwork, synthetic fixtures, generated illustrations, and measured evidence distinctly.
- Do not present a conceptual image as a screenshot or a simulation result.
- Record source, generator, prompt, license, and review provenance when required by the domain or asset workflow.
- Never claim that an illustration proves a runtime capability.
- A visual should clarify a domain concept, state transition, scale, relationship, or observed result; decoration is secondary.

## 7. Living documentation and proof

A living illustration may be static, animated, or interactive. Its motion must explain a meaningful relationship, not merely attract attention. Provide adjacent prose and a stable static interpretation.

For interactive demonstrations:
- identify the actual implementation path and dependencies;
- state what the demonstration proves and what it does not prove;
- provide keyboard-accessible controls and reduced-motion behavior where applicable;
- distinguish presentation-only behavior from domain simulation;
- link to source and tests for implementation claims.

GUI owns semantic GUI-tree presentation and GUI.SVG. Visualize owns general visual-scene and SVG artifact output. Domain repositories own their domain data and meaning. Do not route graphics through the wrong owner merely for visual consistency.

## 8. Cross-linking and ownership

A domain README should link to:
- its canonical books and theory;
- its architecture and implementation references;
- its best current living demonstration;
- the authoritative owner of any externally owned capability.

Cross-repository links should target the active `development` documentation when describing current work and must not imply that the target has released or accepted the contract. Avoid copied documents that can drift; link to the owner.

## 9. Adoption checklist

For each participating repository, review and record:

- [ ] Root README has a clear domain statement and ownership boundaries.
- [ ] README follows the five-part reader path or documents why a section is not applicable.
- [ ] New documentation uses the canonical folder locations.
- [ ] Existing public paths and inbound links are preserved during migration.
- [ ] Books have stable descriptors and consistent title/LOD/cover treatment where applicable.
- [ ] Publisher moniker and footer mark use canonical assets.
- [ ] Domain marks and status badges have clear ownership.
- [ ] SVGs are accessible, responsive, self-contained, and reduced-motion aware when animated.
- [ ] Conceptual visuals, fixtures, and actual evidence are clearly distinguished.
- [ ] Pages workflows and relative asset paths are verified.
- [ ] No domain contract is duplicated or silently reassigned.
- [ ] Adoption is recorded on the repository's tracking issue/PR.

## 10. Rollout

1. SURPS maintains this cross-repository standard and its LOD/book identity rules.
2. GUI and Visualize maintain the rendering and visual-artifact boundaries; they do not own domain semantics.
3. Each domain owner reviews the standard and identifies exceptions.
4. Apply the standard to new work first; migrate existing docs incrementally with link and workflow verification.
5. Do not merge to `master`, publish packages, or change release settings as part of documentation standardization without explicit approval.
