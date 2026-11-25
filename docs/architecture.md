# SURPS Architecture

## Responsibility boundary

SURPS defines the roleplaying domain model: the concepts used to describe worlds, entities, capabilities, attributes, behavior, interactions, and narrative state. It should compose ecosystem capabilities rather than reimplement them.

### Domain concepts

- **World** — a coherent collection of environments, entities, rules, and histories.
- **Entity** — anything that can be described as participating in a world: a character, creature, object, organization, location, or abstract actor.
- **Capability** — something an entity can do or make possible.
- **Attribute** — a typed, meaningful property of an entity or environment.
- **Behavior** — a model of how an entity responds to state, perception, goals, rules, and context.
- **Interaction** — a relationship or event involving two or more entities or an entity and its environment.
- **Environment** — the circumstances and constraints in which entities exist and interact.
- **Narrative** — the interpretation and organization of events, intentions, consequences, and change.

These are initial working definitions, not a frozen schema. We will refine them against concrete use cases before committing to implementation contracts.

## Ecosystem boundaries

| Concern | Owning ecosystem |
|---|---|
| State and transitions | FSM_API |
| Physical laws and simulation | Physics |
| Grammar and structured terminology | GrammarAi |
| Communication protocols | ProtocolAi |
| Visual presentation and SVG | GUI / GUI.SVG |
| Narrative construction | StoryBuilder |
| Underground environment | FSM_Dungeon |
| Experience composition | FSM_COS |
| Runtime execution | FSM_Execution |
| Structured world data | DataWarehouse |
| CI workflow contracts and exact-commit evidence | CiAi |

SURPS consumes and composes these capabilities. It must not become a second physics engine, runtime, GUI framework, or dungeon implementation. CiAi is an engineering-governance capability around the repository's build and evidence lifecycle; it is not an in-world ontology provider and must not define inhabitant behavior.

### Cross-repository content and Experience flow

SURPS is not the sole producer of its content. **raWWar both produces SURPS content and consumes SURPS content**, while owning and delivering its own Experience. The relationship is therefore bidirectional for content and downstream for Experience consumption:

- raWWar-authored SURPS material is admitted and validated against SURPS-owned identity, schema, provenance, and composition contracts before it can become canonical.
- raWWar consumes versioned SURPS content to build and validate its Experience.
- SURPS content changes can trigger raWWar compatibility, integration, and Experience-level CI.
- raWWar content contributions can trigger SURPS admission and validation, followed by consumer revalidation against the accepted revision.

CiAi's Autonomous Development Pipeline must coordinate this as a cross-repository dependency graph with exact revision provenance—not a simplistic one-way build order. SURPS owns canonical roleplaying content semantics; raWWar owns its Experience and its runtime/presentation. The ADP orchestrates the hand-offs and CI evidence without collapsing those ownership boundaries.

## SURPS as a System Experience

SURPS is itself a first-class Experience: a versioned composition request that selects the SURPS MicroBundles and external capabilities required by the roleplaying system. FSM_COS assembles that request through portable MicroBundle identities and exact revisions; it is not a recursive bootstrap because FSM_COS and the host are the composition machinery. See [SURPS and Lightweight Experience Composition](experience-composition.md).

A quest, mission, adventure, or campaign is a lightweight scenario Experience. It consumes SURPS and selects only the books/views and additional MicroBundles it needs. It does not duplicate the SURPS system or own canonical shared roleplaying records. A book-selection document remains separate from the portable FSM_COS composition manifest.

A host may make SURPS optional for a scenario. When disabled, that scenario need not discover SURPS books or rule dependencies; FSM_API, FSM_COS, and FSM_Execution remain independently usable. When enabled, the scenario declares its SURPS dependency and selected book views. This host choice does not replace the SURPS System Experience or its own manifest.

## Ontology, microbundles, and books

Ontology is the organizing authority: concepts, entities, attributes, capabilities, relationships, constraints, behaviors, events, and consequences are identified and related as structured knowledge. A rulebook is not the authority that creates those facts. It is a curated view over them.

A **microbundle** is a composable, independently identified unit of knowledge and/or capability. It may contribute ontology terms, typed records, relationships, behavior definitions, procedures, media, provider contracts, executable capabilities, or dependencies. Ownership stays with the domain that knows the truth. A microbundle may be reused by many books and experiences.

A **rulebook** is a collection and presentation of selected microbundles. Its descriptor declares identity, scope, selection criteria, ordering/grouping, applicability, composition relationships, LOD, and publication metadata. The book view can render the same underlying data as player guidance, GM/Workshop inspection, tabletop procedures, digital reference, diagrams, and navigable prose. Those are projections/adapters, not duplicate truths.

Consequently, one ontology item may appear in several books, and one book may draw from many repositories. A book does not own, copy, or redefine a domain merely because it presents that domain. SURPS owns shared ontology semantics and composition conventions; each domain repository remains authoritative for its domain data and implementation. FSM_COS composes selected microbundles into an experience; FSM_Execution executes that experience. See [SURPS Rulebooks and Domain Microbundles](rulebooks.html).

## First integration case: dungeon inhabitants

A dungeon owns its underground environment: spatial structure, environmental conditions, and domain-specific phenomena. It should not own a bespoke intelligence system for every inhabitant.

SURPS supplies the shared ontology through which inhabitants can be described. Their behavior can be authored from reusable roles, capabilities, motivations, states, and interactions. Physics governs physical consequences; the runtime executes the composed experience.

## Design principles

1. Keep ontology separate from implementation.
2. Prefer reusable descriptions over setting-specific hardcoding.
3. Make rules explicit, inspectable, and testable.
4. Preserve provenance: books, diagrams, examples, and implementations should agree.
5. Treat living illustrations as executable explanations, not decoration.
6. Establish contracts from real use cases before proliferating abstractions.

## Initial development sequence

1. Define the domain vocabulary and boundaries.
2. Model a small set of representative entities and interactions.
3. Validate the model against the dungeon inhabitant use case.
4. Create the first source-book chapters from the validated vocabulary.
5. Add living SVG explanations tied to those chapters.
6. Introduce code and package boundaries only when the domain model warrants them.

## Development evidence and CiAi

GitHub Actions remains the authoritative build and documentation execution environment. SURPS is developed through one grouped [Autonomous Development Pipeline](surps-adp.md), with CiAi coordinating related content tasks, shared context, dependency ordering, and validation across the SURPS content graph. SURPS remains the domain authority; CiAi supplies orchestration and exact-commit evidence. The read-only [exact-commit evidence workflow](../.github/workflows/ciai-evidence.yml) is only the CI evidence lane, not the whole ADP. Bounded ADP write operations require task-scoped host authorization; successful onboarding or green CI is not permission to mutate, merge, publish, release, or deploy.


## Gauntlet integration

[Gauntlet](https://github.com/TrentBest/TheSingularityWorkshop.Gauntlet) is the evidence-producing proving ground for integrated SURPS experiences. Gauntlet owns campaigns, probes, invariant checks, findings, deterministic evaluation, and provenance-bound reports. SURPS supplies explicit rulebook/profile/LOD composition; participating domains supply their own rules and providers; FSM_COS composes the runtime; CiAi remains authoritative for exact-CI evidence correlation and gate policy. The first SURPS integration is tracked in [Gauntlet issue #6](https://github.com/TrentBest/TheSingularityWorkshop.Gauntlet/issues/6).

<!-- THE SINGULARITY WORKSHOP FOOTER -->
<p align="center"><img src="https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png" alt="The Singularity Workshop avatar" width="200" /></p>
