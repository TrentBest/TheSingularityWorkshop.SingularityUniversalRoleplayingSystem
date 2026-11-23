# SURPS Rulebooks and Domain Microbundles

## Purpose

A SURPS rulebook is a discoverable, composable description of a domain's rules, concepts, constraints, supported interactions, and setting assumptions. It is not required to own the domain implementation. The domain repository remains authoritative for its simulation, experiments, data, or services.

**A SURPS rulebook must be a real, usable tabletop sourcebook first.** Players and referees must be able to use it with paper, pencil, character sheets, dice or another agreed resolution method, and conversation. Digital registration, lookup, visualization, and execution are optional ways to organize or automate the same rules; they are not prerequisites for playing.

The initial `ISurpsRulebook` contract is deliberately minimal over `IMicroBundle`. It identifies a composable capability as a SURPS rulebook without prematurely fixing the full ontology, rule serialization, or source-book metadata schema. It must be validated against multiple domain rulebooks before the contract grows.

## Composition pattern

```text
Experience / campaign
    ├── SURPS enabled? (per-experience opt-in)
    ├── CORE rulebook (LOD 0)
    └── explicitly selected rulebooks for declared scopes
            ├── subject/domain
            ├── setting / era
            ├── optional detail / fidelity
            └── tabletop procedures + digital mappings
                    └── domain-owned capabilities where needed
```

A domain microbundle may be wrapped by a SURPS-enabled container and presented as a rulebook such as `SurpsRulebookPhysics`. The container adapts and presents domain knowledge; it must not fork or duplicate the domain implementation.

## LOD, scope, and selection

Every SURPS rulebook declares a non-negative integer **level of detail (LOD)**. LOD is a declared level of rules detail/fidelity and is visible wherever the rulebook is presented. It is not a universal automatic priority number, a graphics-quality setting, or permission for one book to overwrite every lower-numbered book.

- **LOD 0 — CORE** defines the shared baseline ontology and foundational rules. It is the common fallback for any scope without a selected specialization.
- **LOD 1 and above** provide additional detail, specialization, historical or fictional context, domain depth, or a more demanding model for a declared scope.
- **Selection is explicit.** A campaign, experience, or tabletop group chooses which rulebooks apply to which scopes. A higher LOD does not silently activate, replace, or override another rulebook merely because its number is higher.
- **Scope matters.** Two rulebooks at different LODs may describe different eras, genres, domains, or alternative models. They are not necessarily successive revisions of the same rules.
- **Composition is declared.** A selected rulebook may extend CORE, specialize a named rule, replace a named procedure, or provide an independent alternative. Its relationship to other books must be stated.
- **CORE remains the baseline.** Where a selected rulebook does not define a relevant rule, the table falls back to CORE unless the book explicitly declares a different fallback.
- **Conflicts are visible.** If selected rulebooks define incompatible procedures for the same scope, the group/editor must choose a resolution policy. SURPS must not invent a winner based on load order or numeric LOD alone.

### Example: the subject of spying

This is an example of a family of books, not a requirement that every campaign use every level.

| Book | LOD | Scope and contribution | Tabletop use |
|---|---:|---|---|
| SURPS CORE — Spying | 0 | Baseline concepts: secrecy, observation, concealment, information, detection, exposure, risk, and consequences | A complete generic spying procedure usable in any setting |
| Spying Through History | 1 | Broad tradecraft, intelligence organizations, historical methods, and changing technology across eras | Add historical context and more detailed methods when useful |
| Cold War Espionage | 2 | US–Soviet rivalry, period agencies, counterintelligence, proxy operations, equipment, and historical constraints | Select for a campaign set in the Cold War; it specializes only its declared scope |
| Cyberpunk Espionage | 3 | Corporate intelligence, digital intrusion, pervasive surveillance, identity manipulation, autonomous systems, and speculative countermeasures | Select for a cyberpunk campaign; it is a different setting specialization, not an automatic upgrade to Cold War rules |

A table can play CORE alone. It can add the historical book for richer tradecraft, select Cold War rules for one campaign, and select cyberpunk rules for another. The campaign sheet records those choices. A referee can also select only particular chapters or procedures where the book allows it.

The example deliberately demonstrates that **LOD and campaign selection are related but distinct**: LOD communicates depth; scope and explicit selection determine applicability.

## Contract responsibilities

A future rulebook descriptor should provide a stable way to:

- identify the rulebook (stable identity, title, version, LOD, and publisher/domain);
- describe scope, genre, era, assumptions, exclusions, and intended audience;
- declare whether it extends, specializes, replaces, or offers an alternative to a named CORE rule or another source;
- expose concepts and terminology contributed to the shared ontology;
- publish human-readable procedures and, where appropriate, structured rule definitions;
- declare capabilities, dependencies, and supported interactions;
- provide examples, tables, worksheets, player aids, referee guidance, and living visual explanations;
- state compatibility and provenance for underlying domain implementations.

These are documentation and design requirements, not a claim that the current C# marker already exposes all these fields. Do not freeze public CLR signatures until multiple domain providers have been reviewed.

## Tabletop and digital parity

Every foundational rule must be independently understandable and playable without a device. Each rule should explain:

1. What the player declares.
2. What the referee establishes or checks.
3. What character, equipment, environment, and situation records matter.
4. How uncertainty is resolved (including any dice, tables, or agreed procedure).
5. How time passes and what consequences are recorded.
6. What happens on success, partial success, failure, interruption, or an invalid attempt.

The digital mapping may automate calculations, track state, offer prompts, coordinate participants, or visualize outcomes. It must not hide essential rules in code or make a network service necessary for ordinary tabletop play.

See [Tabletop Campaign Composition and Rulebook Selection](Theory/tabletop-campaign-composition.md) for the full player/referee/editor procedure and the spying example.

## Ownership boundaries

| Concern | Owner |
|---|---|
| Common rulebook contract, composition conventions, cross-domain ontology | SURPS |
| Shared NPC/person identity, capabilities, knowledge, motivation, relationships, and agency concepts | SURPS — Nonplayer Characters |
| Institutional positions, staffing requirements, and local operating policies | Owning domain (Laboratories, City, military installation, school, etc.) |
| Physical laws, physical quantities, simulation and consequences | Physics |
| Laboratory domains, experiments, apparatus and educational experiences | SingularityLaboratories |
| City-specific entities, infrastructure, services and civic rules | SingularityCity |
| Posture, gesture, motion and embodied interaction | Gestures |
| Microbundle composition | FSM_COS |
| State and transition primitives | FSM_API |
| Execution and stepping | FSM_Execution |
| Visual rendering and SVG presentation | GUI / GUI.SVG |

SURPS defines how domain knowledge is packaged and understood. It does not take ownership of domain truth.

## People, positions, and institutional staffing

The [Nonplayer Characters sourcebook](books/nonplayer-characters.md) defines the shared person-and-agency concepts. An institution defines the positions it needs and the responsibilities attached to them; an NPC may be assigned to one or more positions. The institution still owns its qualification requirements, policies, and operating procedures. The trusted host/security domain owns authentication, authorization, and enforcement.

For example, Singularity Laboratories can define a Safety Officer position and record a staff assignment. The NPC sourcebook describes the person, their capabilities, knowledge, motivations, and relationships. Laboratory policy determines what qualifications and evidence the position requires. A trusted host decides whether the authenticated principal may access a restricted instrument or dataset. Assignment, qualification, authority, and digital authorization remain distinct.

## First playable CORE tabletop module: Spying

[CORE Spying — LOD 0](books/core-spying.md) is the first setting-neutral, runnable tabletop module. It defines a small playtest character record, 2d6 uncertainty procedure, evidence distinctions, action intervals, pressure clocks, opposition, consequences, and a worked village-ledger mission. [Printable character, referee, and campaign sheets](books/core-spying-play-sheets.md) accompany it. This is an explicitly labeled first playtest slice, not a finalized universal CORE engine or a claim of digital implementation.

## First implementation: Dungeons and Underground

The first SURPS rulebook container is `SurpsRulebookDungeonsAndUnderground` in the SURPS repository. It declares the FSM_Dungeon environment MicroBundle as its required dependency and exposes the provider `surps.rulebook.dungeons-and-underground`.

The underlying bundle is authored in FSM_Dungeon as `TheSingularityWorkshop.FSM_Dungeon.MicroBundle`, exposing `fsm-dungeon.underground-environment`. The SURPS wrapper refers to that bundle by its stable MicroBundle identity; it does not copy the Dungeon implementation or add a project dependency on Dungeon source. The composition host resolves the dependency from the MicroBundle repository.

The sourcebook supplies the human-readable domain knowledge layer:

- [Dungeons and Underground — LOD 1 sourcebook](books/dungeons-and-underground.md)
- [Sourcebook catalogue and living illustrations](books/index.md)
- [Authoritative FSM_Dungeon implementation](https://github.com/TrentBest/FSM_Dungeon/tree/development)
- [Domain architecture](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/ARCHITECTURE.md)
- [World simulation model](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/WORLD_SIMULATION.md)
- [Underground rendering and observation](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/UNDERGROUND_RENDERING.md)

The sourcebook describes formation, construction, topology, geology, materials, environmental conditions, hazards, traversal, observation, and authoring. It distinguishes implemented behavior from design targets and keeps ownership of inhabitants, physical calculations, perception, communication, movement, rendering, and execution with their respective capabilities.

The SURPS MicroBundle project packs the sourcebook and its living SVG diagrams, plus the LOD 1 badge, into the NuGet package under `contentFiles/any/any/`. This makes the human-readable rulebook travel with the composition artifact; it does not make prose executable or transfer domain ownership.

The current C# `ISurpsRulebook` remains a minimal marker. The sourcebook is editorial knowledge, not yet a machine-readable rule catalogue or executable rule resolver.

## Examples: Physics and Laboratories

Physics supplies its authoritative physics microbundles. A SURPS-enabled container presents those capabilities as a rulebook. The book describes physical concepts, units, constraints, assumptions, and supported calculations; Physics remains responsible for calculating physical results. It must not claim a world-step loop, gravity integration, friction, or a general rigid-body solver unless those capabilities are actually implemented.

SingularityLaboratories supplies laboratory and experiment microbundles. A SURPS-enabled container presents apparatus, procedures, safety constraints, observations, and educational material while the Laboratories domain remains responsible for its execution.

## Design constraints

1. Keep the marker contract minimal until multiple domain microbundles validate its next responsibilities.
2. Keep ontology and sourcebook rules distinct from domain execution.
3. Prefer references/adapters over copied domain implementations.
4. Make dependencies, scope, compatibility, provenance, and selection explicit.
5. Support multiple rulebooks in one world without assuming one global setting.
6. Keep authored source-book content and machine-readable descriptors traceable to the same rule identity/version.
7. Keep human-readable sourcebooks useful independently of a particular UI or host.
8. Never describe an aspirational capability as implemented without evidence from its owning repository.
9. Do not infer precedence from numeric LOD alone.

## Registration and behavior resolution

Rulebooks may be registered with the SURPS master system so their rules and domain capabilities can be discovered, inspected, and resolved in context. Registration is a digital convenience; the same selected sourcebooks can be placed on a tabletop and used manually. See [Rulebook Registration and Behavioral Resolution](registration-and-behavior.md) for the current design boundary and provider examples.


## Identity, titles, and cover requirements

Every rulebook uses one descriptor as the source of truth for its stable ID, controlled category, LOD, title, version, cover image, and LOD badge. Its canonical title is derived as **Singularity Universal Roleplaying System - {Category} - LOD {N} - {Rulebook Title}**. The Workshop moniker remains the creator/publisher identity above the book, not part of the book title. Every book requires a real, checked-in cover image distinct from its LOD badge. See [Rulebook Identity, Titles, and Covers](rulebook-identity-and-covers.md) for the descriptor contract, required cover-page composition, controlled categories, and fail-closed validation requirements.
