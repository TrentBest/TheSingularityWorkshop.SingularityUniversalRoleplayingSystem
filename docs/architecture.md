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
| Runtime execution | FSM_Foundry |
| Structured world data | DataWarehouse |
| CI workflow contracts and exact-commit evidence | CiAi |

SURPS consumes and composes these capabilities. It must not become a second physics engine, runtime, GUI framework, or dungeon implementation. CiAi is an engineering-governance capability around the repository's build and evidence lifecycle; it is not an in-world ontology provider and must not define inhabitant behavior.

## SURPS activation\n\nSURPS is an opt-in experience setting. When disabled, the experience runs without SURPS rulebook discovery or dependency; FSM_API, FSM_COS, and FSM_Foundry remain usable independently. When enabled, the experience composes the SURPS master system and selected rulebooks/providers. The checkbox is a simple host-facing choice; editors may configure rulebook selection, precedence, and LOD separately.\n\n## Rulebook composition

SURPS exposes domain knowledge through a common `ISurpsRulebook` contract. Domain microbundles are wrapped by SURPS-enabled containers and presented as rulebooks such as `SurpsRulebookPhysics` and `SurpsRulebookLaboratories`. The domain repository remains authoritative for its implementation and execution; SURPS owns the shared contract and composition conventions. See [SURPS Rulebooks and Domain Microbundles](rulebooks.html).

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

GitHub Actions remains the authoritative build and documentation execution environment. CiAi observes exact-commit workflow runs and normalizes their evidence; it does not execute the build, authorize repository writes, or replace human approval. SURPS onboarding must be evaluated from the exact target commit using the root `AgentOnboarding.md`. A successful admission result is only one prerequisite for bounded agent work, not a grant of authority. The first CiAi integration is the read-only [exact-commit evidence workflow](../.github/workflows/ciai-evidence.yml). It observes the Pages workflow and reports completeness, terminality, and success separately.
\n\n## Gauntlet integration\n\n[Gauntlet](https://github.com/TrentBest/TheSingularityWorkshop.Gauntlet) is the evidence-producing proving ground for integrated SURPS experiences. Gauntlet owns campaigns, probes, invariant checks, findings, deterministic evaluation, and provenance-bound reports. SURPS supplies explicit rulebook/profile/LOD composition; participating domains supply their own rules and providers; FSM_COS composes the runtime; CiAi remains authoritative for exact-CI evidence correlation and gate policy. The first SURPS integration is tracked in [Gauntlet issue #6](https://github.com/TrentBest/TheSingularityWorkshop.Gauntlet/issues/6).\n