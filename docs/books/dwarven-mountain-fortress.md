# Dwarven Mountain Fortress — a living settlement case study

![SURPS Rulebook LOD 1](../assets/rulebook-lod-1.svg)

**Status:** LOD 1 scenario framework. This is a worked world-building case study, not a finalized universal dwarven biology or culture system and not a claim that the fortress is already generated or playable.

The Dwarven Mountain Fortress is the first large-scale composition of the Dungeons and Underground sourcebook. It demonstrates how a society, a mountain, and an underground environment can share one persistent world without one domain taking ownership of another.

## 1. The mountain comes first

The mountain is not a hollow prop whose interior is invented after the settlement. It has an exterior, a physical volume, geological regions, materials, water-bearing zones, and a history. Its shape constrains where a fortress can be built.

Physics owns terrain generation and physical consequences. Its existing 2D height field can produce and inspect exterior relief, but it cannot represent internal caves, overhangs, vertical faces, or a 3D solid. A real cutaway fortress therefore depends on a future 3D volume capability. Until that exists, any complete mountain cutaway is an authored schematic.

## 2. The fortress is a history written into stone

The settlement should reveal successive eras:
- natural caverns first occupied as shelter;
- early delving and prospecting;
- the first defended entrance and civic hall;
- expansion of workshops, residences and storage;
- waterworks, ventilation, lifts and freight routes;
- abandoned workings, repairs, sealed passages and later discoveries.

A constructed feature should carry provenance: who built it, why, from which material, using what method, when, and what is known about its present condition. The visual surface should distinguish natural rock, rough excavation, dressed stone, masonry, metalwork, timber support and later damage.

## 3. A continuous three-dimensional place

The fortress is not a stack of disconnected floors. Named districts are navigation and authoring partitions over a continuous spatial world.

Initial districts:
- **High Gate and Switchback** — approach, gatehouse, terraces and watch positions.
- **The Great Hall** — civic heart, assembly, public memory and vertical volume.
- **The Deep Foundry** — smelting, forging, heat, fuel and ventilation.
- **The Stonewright Quarter** — carving, masonry, structural components and repair.
- **The Delving Works** — active and abandoned mines, shafts, ore and spoil.
- **The Underways** — stairs, lifts, bridges, gates and freight circulation.
- **The Deep Reservoir** — cisterns, channels, water access and drainage.
- **The Root Halls** — older natural caverns incorporated into the settlement.
- **The Ancestor Vaults** — memorials, burial architecture and protected records.
- **The Lower Dark** — sealed, abandoned, dangerous or unexplored depths.

A shaft can connect regions vertically without making them walkable. A lift can fail. A passage can flood. A collapsed route remains part of the world's history even when it is no longer traversable.

## 4. Dwarven life is broader than the mine

Dwarves are people, not a single occupation or personality. A setting may choose traditions around stone, metal, craft, ancestry or mountain stewardship, but these must remain authored cultural conventions rather than universal assumptions.

The society needs ordinary life as well as adventure:
- food production, kitchens, storage and distribution;
- clean water, sanitation, drainage and waste handling;
- ventilation, heating, lighting and fire safety;
- homes, communal spaces, schools and apprenticeships;
- workshops, guilds, markets, trade and transport;
- medicine, care, disability accommodation and aging;
- governance, law, diplomacy, disputes and defense;
- art, music, ceremony, humor, leisure and remembrance.

Roles are contextual and plural. A dwarf may be a mason, parent, council member, musician and volunteer rescuer. Roles can change. Guild membership does not erase personal identity or disagreement.

SURPS supplies the entity and society models. The fortress environment supplies places, resources, hazards and constraints. Neither should hard-code the other.

## 5. Production and material logistics

A working fortress can be understood through chains of cause:

**Ore seam → extraction → sorting → haulage → smelting → alloy/metal stock → forging → finished tool or structure.**

Each stage consumes inputs, occupies space, requires capabilities, produces outputs and may create by-products. The scenario should track provenance and stock movement rather than conjuring finished equipment into a workshop.

Likewise, construction consumes stone, timber, metal, labor and time. Excavation creates spoil that must be stored, processed, reused or transported out. A mine with no spoil route, a foundry with no fuel or exhaust path, or a population with no food/water system is an unfinished world model.

The first Pages slice may display authored logistics records. Do not label them as simulated production until an owning model advances inventories and validates the transfers.

## 6. Water, heat, air and structural consequence

Water should have a source, elevation/head, connections, storage, capacity, outlet and overflow path. The existing Dungeon hydraulic proof is a bounded network model, not a general 3D fluid solver. Physics owns the underlying physical laws and calculations; Dungeon owns where underground water features exist and how they connect.

A foundry needs heat and exhaust. A residential district needs breathable air. A sealed shaft, blocked vent, fire, or flood can alter habitability and routes. These are coupled systems, not decorative ambience. Implement them only through validated Physics and environmental capabilities.

Stone supports, arches, pillars, bridges and retaining walls are constructed features with geometry and material provenance. A visual support does not establish structural safety. Structural assessment must wait for an appropriate physical model and evidence.

## 7. Exploration and knowledge

The fortress should support several truthful lenses:
- **Atlas:** omniscient authoring view of all known world facts.
- **Explorer:** what a particular visitor can currently perceive.
- **Dwarven resident:** what a selected inhabitant knows through experience and reports.
- **Historian:** records, inscriptions, construction phases and uncertain interpretations.
- **Engineer:** material, clearance, support, water and route evidence available to that role.

These views must not be collapsed. A hidden passage can exist without the explorer knowing it. A survey report can be incomplete or wrong. A historian may infer an older construction phase without having direct proof.

## 8. Cross-domain responsibility

| Question | Owner |
|---|---|
| How is the exterior mountain and physical solid volume generated? | Physics |
| What are the material fields and physical consequences? | Physics |
| What chambers, passages, shafts, gates and environmental regions exist? | FSM_Dungeon |
| What is a dwarf, what can they do, and what do they want? | SURPS |
| How are craft actions, climbing, hauling and mechanism operation performed? | Gestures / movement / interaction providers |
| What does an observer know? | Perception, memory and communication capabilities |
| How is the world presented? | Renderer / Visualization |
| Which capabilities are composed and state changes validated? | Host / FSM_COS / FSM_Foundry |

The SURPS core contract remains outside this case study's scope. This book composes domain knowledge; it does not redefine the core.

## 9. First explorable journey

The initial journey should be understandable without combat:
1. Approach the mountain and inspect its exterior terrain.
2. Enter through the High Gate.
3. Stand in the Great Hall and inspect the vertical scale and surrounding districts.
4. Follow a freight route to the Delving Works.
5. Inspect an ore occurrence and its provenance.
6. Follow material toward the Deep Foundry and Stonewright Quarter.
7. Visit the Deep Reservoir and trace water infrastructure.
8. Compare a maintained route with an abandoned or collapsed passage.
9. Descend toward the Lower Dark, where the map becomes incomplete and observer knowledge matters.

This is the first proof that the world is a living, coherent place—not merely a sequence of encounter rooms.

## References

- [Dungeons and Underground, LOD 1](dungeons-and-underground.md)
- [FSM_Dungeon fortress scenario and integration contract](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/DWARVEN_MOUNTAIN_FORTRESS.md)
- [Physics mountain-volume and fortress design brief](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/GEOLOGY_MOUNTAIN_VOLUME_AND_FORTRESS.md)
