# TheSingularityWorkshop.SingularityUniversalRoleplayingSystem

> A universal ontology and simulation framework for roleplaying worlds, entities, stories, and experiences.

[![GitHub Pages](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/actions/workflows/pages.yml/badge.svg)](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/actions/workflows/pages.yml)
<!-- SURPS:PARTICIPATION:START -->
[![SURPS participation and sourcebooks](docs/assets/badges/surps-participation.svg)](docs/books/index.md)
<!-- SURPS:PARTICIPATION:END -->


## 1. Overview

The Singularity Universal Roleplaying System (SURPS) is the shared foundation for describing and experiencing worlds. It is not tied to one genre, game, ruleset, setting, or medium. It aims to make entities, attributes, capabilities, behavior, interactions, environments, and narrative consequences composable and reusable.

**SURPS has one underlying behavior model and multiple adapters.** The tabletop adapter is a complete human-usable game, but its dice values, target numbers, and qualitative outcome bands are derived during authoring/workshop calibration from the underlying behavior. The digital adapter evaluates the same semantics in greater detail against live state. Neither adapter is a separate ruleset or a competing source of truth. No application or internet connection is required to use a published tabletop adapter.

The source books are human-readable views over shared ontology and independently owned MicroBundles. A book selects canonical records for an audience, scope, and LOD; it does not create a competing source of truth. SURPS now validates and resolves the first CORE Spying MicroBundle/player-view slice into a provenance-bearing JSON projection. See the [MicroBundle and Rulebook View contract](docs/microbundles-and-views.md) for the implemented boundary and remaining federation/runtime work.

Start with the **[SURPS: The Living Game — Core Manual](docs/game-manual.md)**. Play the first short spy mission, [The Missing Ledger](docs/experiences/missing-ledger/), built on the canonical CORE Spying book. Explore the [living character sheets and world surfaces](docs/living-world-and-character-studio.md), including the first themed SVG sheets and ambient settlement study. The [living-world opportunity and economy model](docs/world-opportunities-and-economy.md) defines how attention, discoveries, jobs, contracts, and in-world transactions should emerge from simulation state. The [surface, map, and semantic tile contract](docs/surface-assets-and-tiles.md) defines reusable empty map canvases, tile catalogs, SVG semantics, and CiAi adoption rules. It is the primary reader-facing game book. The [Player and Editor Manual](docs/player-and-editor-manual.md) is its technical companion; [Theory: tabletop campaign composition](docs/Theory/tabletop-campaign-composition.md) and [Theory: roleplaying history](docs/Theory/history-of-roleplaying-games.md) provide deeper context.

## 2. Architecture

SURPS owns the roleplaying ontology: what entities are, what properties and capabilities they possess, how behavior is represented, and how rules are expressed. It does not absorb the responsibilities of the ecosystem that supports it.

- **FSM_API** — state and transition foundations.
- **Physics** — physical laws and interactions.
- **GrammarAi / ProtocolAi** — structured language and communication concepts.
- **GUI / GUI.SVG** — presentation, interfaces, and living illustrations.
- **StoryBuilder** — narrative construction.
- **FSM_Dungeon** — dungeon environments and their environmental behavior.
- **FSM_COS / FSM_Execution** — composition and execution of experiences.
- **Gauntlet** — integrated adversarial proving ground and evidence-producing campaign harness for MicroBundles and SURPS-enabled experiences.

See [Architecture](docs/architecture.md) for the initial responsibility boundaries. SURPS itself is also a first-class, self-assembled [System Experience](docs/experience-composition.md); quests, missions, adventures, and campaigns remain lightweight scenario Experiences that consume it.

Repository-specific agent work is governed by the root [AgentOnboarding.md](AgentOnboarding.md). SURPS is organized as one **grouped Autonomous Development Pipeline (ADP)**: CiAi coordinates related content-definition work across books, canonical records, MicroBundles, characters, maps, tiles, SVG surfaces, and validation, with shared context and explicit dependencies. SURPS remains the authority for its domain contracts; CiAi supplies orchestration and evidence. See the [SURPS ADP domain contract](docs/surps-adp.md). The [CiAi evidence workflow](.github/workflows/ciai-evidence.yml) is a separate read-only lane observing exact-commit Pages evidence; ADP write operations require task-scoped host authorization, and merge/publication/release/deployment remain separately gated.

## 3. Source Books

Books are modular, versionable source material rather than isolated documents. Each book declares its scope, LOD, assumptions, and relationship to CORE and other books. **LOD communicates detail; campaign selection and declared scope determine which books apply.** A higher number does not silently override another book.

See the [SURPS Master Rulebook Map](docs/rulebook-backlog/index.md) for the cross-repository book inventory, ownership sign-in, and participating repository registry. Every contributor repository follows the [canonical Repository Participation Standard](docs/repository-participation.md). See the [Repository Onboarding Tracker](docs/repository-onboarding.md) for current invitations and verified admission status. Also see [Source Books](books/README.md), [SURPS Rulebooks](rulebooks.md), and [Tabletop Campaign Composition](docs/Theory/tabletop-campaign-composition.md). The first executable composition is `SurpsRulebookDungeonsAndUnderground`, which wraps the authoritative FSM_Dungeon environment MicroBundle.

## 4. Living Documentation

Illustrations should teach, not merely decorate. SVGs can expose anatomy, state transitions, movement, forces, equipment, environments, and cause-and-effect. Where useful, diagrams will animate or respond to user interaction while remaining accessible and understandable as static illustrations.

The first site is a lightweight static publication surface. The SVG examples are authored assets, not screenshots or video substitutes.

For cross-repository contributors, use the canonical [Workshop Documentation Standard](https://github.com/TrentBest/TheSingularityWorkshop.FSM_COS/blob/development/DOCUMENTATION_STANDARD.md), which now defines SURPS enrollment, sourcebook/cover requirements, generated README badges, and Gauntlet conformance. The [SURPS publication and graphics adoption notes](docs/repository-publication-and-graphics-standard.md) provide domain-specific context and are subordinate to the shared standard.

The book-specific [Rulebook Identity, Titles, and Covers standard](docs/rulebook-identity-and-covers.md) remains authoritative for descriptors, title pages, covers, and LOD badges.

## 5. Development

- `master` represents the last released, published state.
- `development` is the active source branch.
- Work is developed and validated on `development`; release synchronization to `master` is a deliberate step.
- GitHub Pages is deployed from the repository's `docs/` directory by GitHub Actions.
- No package or publication release is implied by documentation deployment.

Start with the [SURPS Workshop site](https://trentbest.github.io/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/).
