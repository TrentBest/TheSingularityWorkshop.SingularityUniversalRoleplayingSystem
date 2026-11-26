# Site K-17 — Cinematic Opening

**Scenario slice:** `surps.demo.soviet-facility-opening@0.1.0`  
**Setting continuity:** Autumn 1981, Russian SFSR, Soviet Union  
**Location:** Fictional alleged site in the northern Ural region

[Play the cinematic opening](../../docs/experiences/soviet-facility-opening/index.html).

## What this proves

1. A period-inspired USSR orientation map establishes the alleged location.
2. The map hands off to a first-person-style property reveal.
3. The player approaches an admission checkpoint with armed guards and an attendant.
4. The attendant asks for the character's name and presents twenty plausible choices.
5. The handler's first instruction reveals and highlights the correct identity.
6. The player still commits the answer; an incorrect response raises suspicion rather than silently teleporting the story to a fixed ending.

## Authorship and truth boundary

Site K-17, its designation, its location, and the events are fictional. The map is a schematic, historical-style orientation surface, not a navigational map and not a claim about a real clandestine installation. The scene uses the existing immersive-scene model: images and controls are presentation projections, not authoritative world state.

This is a visual/interaction prototype. It does not claim a live 3D renderer, spatial simulation, audio pipeline, Hermit connection, persistent session, or automated action adjudicator. The handler instruction is currently delivered as authored text on request; voice synthesis/audio is a later presentation integration.

## Runtime and FSM boundary

The page is a static GitHub Pages artifact, so its local scene-navigation code is deliberately a presentation prototype. It does not pretend that browser JavaScript is FSM_API. When the experience is connected to an authoritative runtime, scene and interaction transitions must be represented with FSM_API 2.0's integer-backed state identity and executed through the owning runtime; GUI/Renderer remain projections. The SURPS Pages build already checks out FSM_API development as a source dependency through the Visualize publication pipeline.

## Executable FSM_API 2.0 proof

The Pages build also runs [SurpsCinematicFlow](../../samples/SurpsCinematicFlow/Program.cs), which uses the native `TheSingularityWorkshop.FSM_API.IntegerBacked.FsmApi` API. It exercises integer state IDs for map, grounds, admission, handler, admitted, and identity-challenged states. It verifies both the clean identity path and a wrong-answer/retry path, then generates an SVG state-flow diagram and JSON trace manifest for the site.

This is an executable state-machine proof, not a claim that the browser prototype is already wired to a trusted live session. The HTML still owns only its local presentation interactions; a production host must own authoritative session state and player-authorized projections.

## Next vertical slice

- Replace the schematic orientation graphic with a properly sourced, period-appropriate map asset and explicit projection/geographic provenance.
- Replace the illustrative estate composition with a high-fidelity rendered environment and camera progression.
- Connect the name choice to a session-owned identity/cover record and the handler's scoped knowledge.
- Add authentic period sound, localized dialogue, captions, and accessibility controls.
- Exercise the scene's wrong-answer and delayed-response consequences through the SURPS adjudication model.
