# SURPS Rulebooks and Domain Microbundles

## Purpose

A SURPS rulebook is a discoverable, composable description of a domain's rules, concepts, constraints, and supported interactions. It is not required to own the domain implementation. The domain repository remains authoritative for its simulation, experiments, data, or services.

The initial `ISurpsRulebook` contract now exists as a deliberately minimal marker over `IMicroBundle`. It identifies a composable capability as a SURPS rulebook without prematurely fixing the full ontology, rule serialization, or source-book metadata schema. This first shape is validated against the Dungeons and Underground composition; it must be exercised by Physics and SingularityLaboratories before the contract grows.

## Composition pattern

```text
Domain microbundle
    ├── domain implementation (owned by its repository)
    ├── domain knowledge and assets
    └── SURPS-enabled container
            └── ISurpsRulebook
                    └── SurpsRulebookPhysics
```

The same pattern can produce `SurpsRulebookLaboratories`, `SurpsRulebookCities`, and other domain rulebooks. A container adapts and presents a domain microbundle through SURPS; it must not fork or duplicate the domain's implementation.

## Contract responsibilities

An `ISurpsRulebook` should eventually provide a stable way to:

- identify the rulebook (stable identity, name, version, and domain);
- describe its scope, assumptions, and boundaries;
- expose the concepts and terminology it contributes to the shared ontology;
- publish rules and constraints in a structured, inspectable form;
- declare capabilities, dependencies, and supported interactions;
- expose examples, source-book material, and living visual explanations;
- state compatibility and provenance for the underlying domain implementation.

The contract should distinguish descriptive knowledge from executable behavior. A rulebook may reference domain capabilities, but it should not silently become the engine that executes them.

## Ownership boundaries

| Concern | Owner |
|---|---|
| Common rulebook contract, composition conventions, cross-domain ontology | SURPS |
| Physical laws, physical quantities, simulation and consequences | Physics |
| Laboratory domains, experiments, apparatus and educational experiences | SingularityLaboratories |
| City-specific entities, infrastructure, services and civic rules | A future Cities domain |
| Microbundle composition | FSM_COS |
| State and transition primitives | FSM_API |
| Execution and stepping | FSM_Foundry |
| Visual rendering and SVG presentation | GUI / GUI.SVG |

SURPS defines how domain knowledge is packaged and understood. It does not take ownership of domain truth.

## First implementation: Dungeons and Underground

The first SURPS rulebook container is `SurpsRulebookDungeonsAndUnderground` in the SURPS repository. It declares the FSM_Dungeon environment MicroBundle as its required dependency and exposes the provider `surps.rulebook.dungeons-and-underground`.

The underlying bundle is authored in FSM_Dungeon as `TheSingularityWorkshop.FSM_Dungeon.MicroBundle`, exposing `fsm-dungeon.underground-environment`. The SURPS wrapper refers to that bundle by its stable MicroBundle identity; it does not copy the Dungeon implementation or add a project dependency on Dungeon source. The composition host resolves the dependency from the MicroBundle repository.

The first implementation is intentionally a composition shell. It establishes the ownership and dependency direction; it does not yet claim that Dungeon provides inhabitant ontology, behavior, communication, or a finalized machine-readable rule catalogue. Those remain separate capabilities and future contract work.

## Example: Physics

The Physics repository supplies its authoritative physics microbundle. A SURPS-enabled container presents that bundle as `SurpsRulebookPhysics`.

The rulebook should make physical concepts, laws, units, constraints, and available simulations discoverable to a SURPS world. When an entity falls, collides, heats, or otherwise interacts physically, the rulebook identifies the applicable domain capability; Physics remains responsible for calculating the physical result.

## Example: Laboratories

SingularityLaboratories supplies its laboratory and experiment microbundles. A SURPS-enabled container presents the relevant content as `SurpsRulebookLaboratories`.

This lets a world contain laboratories as places and experiences, while laboratory apparatus, experiment procedures, safety constraints, observations, and educational material remain grounded in the Laboratories domain.

## Design constraints

1. Keep the initial marker contract minimal until multiple domain microbundles validate its next responsibilities.
2. Keep rulebook metadata and ontology distinct from domain execution.
3. Prefer references/adapters over copied domain implementations.
4. Make dependencies and compatibility explicit.
5. Support multiple rulebooks in one world without assuming one global setting.
6. Keep authored source-book content and machine-readable rule definitions traceable to each other.
7. Treat a SURPS-enabled container as a composition boundary, not a new domain owner.

## First collaboration requests

- **Physics:** identify the smallest useful physics microbundle surface, the concepts/units/rules that should be discoverable, and the correct boundary for requesting physical calculations.
- **SingularityLaboratories:** identify a representative laboratory/experiment microbundle, its apparatus and safety constraints, and how it should be presented as a rulebook without duplicating lab execution.
- **SURPS:** compare both responses, draft the minimal `ISurpsRulebook` contract, and validate it against a shared world containing physical entities and a laboratory experience.


## Registration and behavior resolution

Rulebooks are registered with the SURPS master system so their rules and domain capabilities can be discovered, inspected, and resolved in context. See [Rulebook Registration and Behavioral Resolution](registration-and-behavior.md) for the registration lifecycle, editor-visible rule descriptors, typed mathematical binding, provenance, and the SURPS–Gestures–Physics interaction model.
