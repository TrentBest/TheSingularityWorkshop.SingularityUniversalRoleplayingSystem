# Living Character Sheets and World Surfaces

> Direction and first visual scaffold for SURPS digital presentation.

## Intent

A character sheet is an empty, reusable, data-bindable SVG surface—not a static form or a character record. A map is a nested, composable visual surface—not merely a board of inert squares. SVG is the first presentation layer for a world that will eventually be backed by authoritative entities, rules, and simulation.

The visual layer may animate rivers, show tiny travelers on roads, give a shop a keeper and visiting customers, or suggest wildlife and settlement activity. These are ambient illustrations and previews. They are not evidence that the corresponding world event occurred, nor do they own authoritative state.

## Character sheet themes

The initial catalog contains five empty SVG sheets:

| Theme | Visual language | Catalog tier |
|---|---|---|
| Verdant | Vines, leaves, organic dividers | Starter |
| Stone | Carved mineral borders and facets | Starter |
| Woodwright | Crafted wood grain and joinery | Starter |
| Aegis | Precision steel framing | Premium-ready |
| Aether | Luminous energy field | Premium-ready |

Assets live in `docs/assets/character-sheets/`; `catalog.json` describes presentation metadata and the initial tier grouping. The tier values are catalog intent only. They do not implement payments, entitlements, storefronts, or unlock enforcement. A future commerce/entitlement adapter must authorize a theme without changing the character's underlying data.

Every sheet remains an empty template when opened directly. Each theme implements the shared versioned `surps.character-sheet@1.0.0` presentation contract through stable `data-surps-bind` targets. Character Studio projects the current draft into those targets at runtime; it does not write character data back into the SVG asset. The character model remains the source of truth; SVG fields are projections. This is the first data-bound stage, not a canonical character serialization contract.

## Living maps and nested places

The initial [map and tile catalogues](surface-assets-and-tiles.md) and the interactive [Map Workshop](map-studio.html) provide three blank map surfaces and a semantic tile starter set. The workshop exports a local draft referencing stable tile IDs; it is not yet a canonical map editor or simulation engine.

The map model should compose from broad to fine detail:

1. World
2. Region
3. Settlement
4. District
5. Site or building
6. Interior, room, or encounter space

A parent map owns the placement and identity of child map regions, not their entire detailed contents. Opening a child map changes the level of detail while preserving stable identity and coordinates/transform relationships.

A tile is a semantic visual component with a stable kind and data contract. Examples include river, road, forest, field, bridge, town, shop, home, and landmark. SVG renderers may add ambient motion:
- water highlights drift along a river path;
- tiny travelers move along connected roads;
- shopkeepers remain at their shop while customers approach, enter, and leave;
- smoke, flags, foliage, lights, and wildlife create a sense of place.

The settlement SVG in `docs/assets/living-world/settlement-ambient-demo.svg` is a deliberately illustrative prototype. Its people and traffic are decorative motion, not generated NPCs, pathfinding, or simulated commerce.

## NPC generation pipeline

NPC generation should be composable, reproducible, and provenance-aware. A generated NPC should eventually resolve through distinct stages:

1. **Concept and role:** purpose, occupation, faction, social function, and narrative relevance.
2. **Identity:** stable identifier, name, ancestry/kind, pronouns, language, and origin.
3. **Appearance:** body plan, silhouette, palette, clothing, equipment, and optional portrait.
4. **Capabilities:** attributes, skills, traits, adversities, knowledge, and tools.
5. **Relationships:** household, employer, allies, rivals, community, and affiliations.
6. **Placement:** home, workplace, schedule, map location, and environmental context.
7. **Behavior:** goals, needs, routines, reactions, and permitted action vocabulary.
8. **Presentation:** a visual actor projected into a map, shop, scene, or character sheet.

Generation should accept constraints and seeds, record provenance, and distinguish authored canon from generated suggestions. A visual actor can be shown before behavior is simulated; later, the same stable NPC identity should bind to richer state and behavior.

## Shared contracts and fidelity progression

The architecture must keep three things separate:

- **Domain state:** authoritative characters, places, maps, inventories, relationships, and world events.
- **Presentation state:** SVG layers, animation parameters, visual themes, camera/LOD, and decorative actors.
- **Simulation state:** physical movement, schedules, pathfinding, commerce, needs, and other executable behavior.

The SVG renderer consumes domain/presentation projections. It must not mutate authoritative world state or imply simulation results. Ambient animation may be deterministic from stable seeds and presentation time so previews remain coherent and testable.

Progression is intentional:

- **Stage 1 — Living picture:** authored SVG templates, tile illustrations, ambient animation, and nested visual composition.
- **Stage 2 — Data-bound picture:** stable IDs and schemas bind characters, tiles, buildings, and NPC actors to real domain records.
- **Stage 3 — Interactive world:** selections and user actions route through domain commands; SVG remains a projection.
- **Stage 4 — Simulated world:** movement, schedules, shop activity, ecology, and other systems produce authoritative state that the same visual surfaces display.

## Ownership boundaries

- SURPS owns character/world ontology and roleplaying semantics.
- Map/environment domains own geography, topology, tile meaning, and place state.
- NPC/character domains own identity, capabilities, relationships, and behavior state.
- SVG/GUI presentation owns visual composition, animation, accessibility, and interaction projection.
- Simulation domains own authoritative execution and outcomes.
- Commerce/entitlements own theme purchase and unlock authorization.

This document records the intended architecture and the first SVG artifacts. It does not claim that the NPC pipeline, map engine, commerce, or simulation stages are implemented.


## Attention, discoveries, and economic activity

A living world should expose opportunities through its ordinary places and inhabitants, not only through a quest list. A player who stops to read a settlement notice board may discover a job, warning, missing-person notice, or clue. A visit to a tavern may create an opportunity through a conversation, a patron's need, or a contract offered by the keeper. These discoveries are interactions with authoritative world entities, not UI-generated quest markers.

The distinction between world truth, participant knowledge, and visual presentation is essential: inspecting a posting records what the character can perceive; it does not make every claim on the posting true. A clue may be noticed, missed, misunderstood, or investigated. The presentation layer reveals affordances but does not invent facts.

Economic activity belongs in the same world model. Work, wages, contracts, inventory, markets, debt, expenses, and payment should have explicit parties, terms, and transaction history. SURPS supplies shared roleplaying semantics; the Economy domain supplies monetary and market capabilities. A job accepted in a tavern should be a real obligation with a defined reward and completion condition, not a detached reward counter.

See [Living World Opportunities and In-World Economy](world-opportunities-and-economy.md) for the interaction model, economic loop, ownership boundaries, and first end-to-end acceptance scenarios. The existing ambient settlement SVG remains an illustration, not a simulation of NPC activity or commerce.
