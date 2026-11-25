# SURPS Autonomous Development Pipeline (ADP)

## Purpose

SURPS is developed through a **grouped ADP**, not a queue of unrelated file-level jobs.

The SURPS ADP is the coordinated development context for defining, connecting, validating, and presenting the SURPS content system. Its unit of meaning is a coherent body of related domain content: books, canonical records, MicroBundles, rules, entities, character sheets, maps, semantic tiles, visual themes, and their cross-references.

CiAi supplies the ADP orchestration machinery. SURPS supplies the domain contracts and content authority. The ADP group brings the related work together so that an LLM can reason about dependencies and consistency across the whole content system.

## Group, not file queue

An ADP group retains shared context and a connected work graph. Individual tasks are bounded work packets within that group; they are not independent projects with isolated definitions.

A task may create or revise a book chapter, SVG, tile family, descriptor, or canonical record, but its work packet should carry the relevant group context:

- the SURPS domain contract and applicable schemas;
- canonical IDs and records that the work reuses or extends;
- owning book, MicroBundle, setting, campaign, and LOD context where applicable;
- incoming and outgoing references;
- relevant assets and presentation conventions;
- provenance and exact source revision;
- validation obligations and dependent tasks.

The group should be able to discover that a change to a canonical rule affects several books, a character capability affects sheet presentation, or a tile family affects map composition. It then schedules the affected work and validation as related tasks rather than asking separate agents to reinvent the same context.

## Content workstreams within the group

These are related workstreams, not separate ADPs:

1. **Source intake and provenance** — inventory existing books, Markdown, structured records, SVGs, images, and other authored material; preserve ownership, attribution, licensing, source path, and commit provenance.
2. **Ontology and canonical records** — define entities, attributes, capabilities, behaviors, relationships, rules, and stable identities.
3. **Books and composition** — build human-readable views over canonical records; maintain book descriptors, scope, LOD, cross-book references, and explicit scoped overrides.
4. **Characters and sheets** — define character models and data-bound sheet surfaces, themes, fields, and state-aware presentation.
5. **Worlds, maps, and tiles** — define empty map surfaces, semantic tile families, placement/composition rules, topology constraints, and future simulation bindings.
6. **Rules, procedures, and experiences** — connect shared behavior to tabletop and digital adapters without creating competing rule systems.
7. **Validation and living presentation** — validate schemas, identities, references, overrides, accessibility, SVG integrity, generated book identity, and rendered explanations.

The ADP may run independent tasks in parallel, but shared-record changes and dependent outputs must respect declared dependencies and versioned inputs.

## Cross-repository production and consumption

SURPS content does not originate in only one repository. **raWWar is both a producer of SURPS content and a consumer of SURPS content**, while also being the purveyor of a playable/presented Experience. This is a first-class pipeline relationship, not an exception to the ownership model.

That creates a deliberately more complicated CI graph:

- SURPS authors and validates canonical roleplaying content and its reusable contracts.
- raWWar can contribute authored content back into the SURPS content ecosystem, subject to SURPS identity, schema, provenance, and validation rules.
- raWWar also consumes versioned SURPS content to construct and deliver its Experience.
- A SURPS change can therefore trigger raWWar compatibility and experience validation.
- A raWWar content contribution can trigger SURPS admission, canonicalization, cross-reference checks, and validation, then flow back to raWWar as an updated consumable content revision.
- The graph must distinguish a repository's **content-production edge**, **content-consumption edge**, and **experience-delivery edge**. These are separate relationships even when they connect the same two repositories.

The ADP must model this as a dependency graph across repositories and revisions, not as a one-way build chain and not as an assumption that every producer owns the consumer's runtime. Each task records the exact upstream content revisions it consumed and the exact downstream artifacts it produced. CI should test both directions where applicable: contribution admission into SURPS and consumer compatibility in raWWar.

**Ownership remains explicit:** SURPS decides whether contributed material becomes canonical SURPS content; raWWar owns its Experience, its presentation, and its runtime behavior. Neither repository silently assumes ownership of the other's domain. Shared content contracts and versioned artifacts are the boundary between them.

## Authority and execution boundaries

- **SURPS** owns the roleplaying ontology, canonical IDs, schemas, sourcebook identity, content catalogs, and composition semantics.
- **CiAi** owns ADP orchestration, task grouping, dependency scheduling, bounded LLM work packets, CI evidence correlation, and policy evaluation.
- **Participating repositories and domain packages** retain authority over their own source material and domain records.
- **The host / FSM_Foundry** independently authenticates and authorizes proposed repository operations within explicit task scope.

CiAi can help define and implement SURPS content because the SURPS ADP is explicitly operating inside SURPS's domain contracts. This does not make CiAi the authority on what SURPS means.

Keep these capabilities distinct:

- The GitHub Actions evidence observer is read-only and reports exact-commit CI facts.
- ADP tasks may propose and perform bounded content-development operations only when the host grants the task the required write capability.
- Merge, publication, release, deployment, permission changes, and branch deletion remain separately gated. No green CI result or ADP membership implies those permissions.

## Composition invariants

1. Books are views over canonical records and owned MicroBundles, not competing sources of truth.
2. Reuse canonical records by reference instead of duplicating definitions.
3. A real variation requires an explicit override with target, stable identity, scope, rationale, precedence policy, version, and provenance.
4. LOD describes detail; it is not precedence. File order and load order are never precedence.
5. Ambiguous or conflicting composition fails closed and produces a resolvable finding.
6. Generated Markdown identity, covers, badges, and relative links derive from authoritative descriptors.
7. SVG surfaces remain accessible and semantically meaningful when static; animation is an enhancement driven by explicit data/state.
8. Every task records its inputs, exact source revision, outputs, validation results, and unresolved decisions.

## Group completion

The group is not complete merely because its individual tasks are green. The ADP must also validate the integrated content graph: canonical identity, ownership, references, override resolution, asset integrity, book composition, and generated presentation must agree at the same recorded source revision.

An ADP group can remain active as SURPS evolves. New content joins the existing group with explicit relationships and dependencies; it does not require a new pipeline for every book, asset, or feature.

## CiAi integration note

This document defines the SURPS-side domain contract for its ADP group. CiAi should map it into CiAi's native ADP/group/task model rather than inventing a parallel SURPS-only orchestration schema. If CiAi's current model cannot express shared group context, dependency relationships, and the distinct evidence/write/approval lanes, that is a capability gap to address in CiAi itself.
