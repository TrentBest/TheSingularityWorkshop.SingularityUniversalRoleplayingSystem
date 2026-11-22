# SURPS Rulebooks and Domain Microbundles

## Purpose

A SURPS rulebook is a discoverable, composable description of a domain's rules, concepts, constraints, and supported interactions. It is not required to own the domain implementation. The domain repository remains authoritative for its simulation, experiments, data, or services.

The intended contract name is `ISurpsRulebook`. This is a design target, not yet a committed public API or NuGet contract. We should validate the shape against at least Physics and SingularityLaboratories before fixing signatures.

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

## Example: Physics

The Physics repository supplies its authoritative physics microbundle. A SURPS-enabled container presents that bundle as `SurpsRulebookPhysics`.

The rulebook should make physical concepts, laws, units, constraints, and available simulations discoverable to a SURPS world. When an entity falls, collides, heats, or otherwise interacts physically, the rulebook identifies the applicable domain capability; Physics remains responsible for calculating the physical result.

## Example: Laboratories

SingularityLaboratories supplies its laboratory and experiment microbundles. A SURPS-enabled container presents the relevant content as `SurpsRulebookLaboratories`.

This lets a world contain laboratories as places and experiences, while laboratory apparatus, experiment procedures, safety constraints, observations, and educational material remain grounded in the Laboratories domain.

## Design constraints

1. Do not freeze an interface signature before reviewing real domain microbundles.
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
