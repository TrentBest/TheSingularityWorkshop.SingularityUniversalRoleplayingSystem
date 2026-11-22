# TheSingularityWorkshop.SingularityUniversalRoleplayingSystem

> A universal ontology and simulation framework for roleplaying worlds, entities, stories, and experiences.

[![GitHub Pages](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/actions/workflows/pages.yml/badge.svg)](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/actions/workflows/pages.yml)

## 1. Overview

The Singularity Universal Roleplaying System (SURPS) is the shared foundation for describing and experiencing worlds. It is not tied to one genre, game, ruleset, setting, or medium. It aims to make entities, attributes, capabilities, behavior, interactions, environments, and narrative consequences composable and reusable.

The source books are human-readable expressions of that system. They should explain the underlying concepts while demonstrating them through living diagrams, interactive examples, and simulations.

## 2. Architecture

SURPS owns the roleplaying ontology: what entities are, what properties and capabilities they possess, how behavior is represented, and how rules are expressed. It does not absorb the responsibilities of the ecosystem that supports it.

- **FSM_API** — state and transition foundations.
- **Physics** — physical laws and interactions.
- **GrammarAi / ProtocolAi** — structured language and communication concepts.
- **GUI / GUI.SVG** — presentation, interfaces, and living illustrations.
- **StoryBuilder** — narrative construction.
- **FSM_Dungeon** — dungeon environments and their environmental behavior.
- **FSM_COS / FSM_Foundry** — composition and execution of experiences.
- **DataWarehouse** — structured world and entity data.

See [Architecture](docs/architecture.md) for the initial responsibility boundaries.

Repository-specific agent work is governed by the root [AgentOnboarding.md](AgentOnboarding.md). CiAi is used as a read-only CI evidence and admission capability; it does not own SURPS ontology or authorize changes.

## 3. Source Books

Books will be authored as modular, versionable source material rather than isolated documents. The initial publishing structure is intentionally small; book titles, scope, and chapter plans will be established as the ontology matures.

See [Source Books](books/README.md).

## 4. Living Documentation

Illustrations should teach, not merely decorate. SVGs can expose anatomy, state transitions, movement, forces, equipment, environments, and cause-and-effect. Where useful, diagrams will animate or respond to user interaction while remaining accessible and understandable as static illustrations.

The first site is a lightweight static publication surface. The SVG examples are authored assets, not screenshots or video substitutes.

## 5. Development

- `master` represents the last released, published state.
- `development` is the active source branch.
- Work is developed and validated on `development`; release synchronization to `master` is a deliberate step.
- GitHub Pages is deployed from the repository's `docs/` directory by GitHub Actions.
- No package or publication release is implied by documentation deployment.

Start with the [SURPS Workshop site](https://trentbest.github.io/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/).
