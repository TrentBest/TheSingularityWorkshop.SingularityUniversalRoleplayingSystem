# Immersive Scene Experiences

## Purpose

A scenario Experience should be able to present a world as a sequence of living, spatially meaningful moments—not merely as paragraphs followed by generic choice buttons.

When a participant presses **Play**, the host may place the Experience into an immersive presentation mode in which the GUI owns the active presentation surface. The player sees a composed scene, hears its soundscape, reads or hears authored narration, and interacts with things that exist in that scene.

The scene is still a projection of authoritative world state. Images, animation, audio, hit regions, dialogue, and menus are presentation. They are not the source of truth.

This document defines the content and responsibility boundaries for that direction. It does not claim that the complete runtime, image pipeline, spatial renderer, audio system, or digital adjudicator already exists.

## 1. A moment is a world projection

A **moment** is a versioned presentation of a particular scene state and point of view. It may contain:

- one composed image, multiple coordinated layers, or a sequence of authored visual frames;
- narration, captions, subtitles, or character-internal text;
- environmental sound, dialogue, music, and timed audio cues;
- visible entities and their spatial relationships;
- interactable regions associated with stable world/entity identities;
- the current participant's permitted observations and available actions;
- a reference to the authoritative scene/session revision from which the projection was produced.

A moment is not necessarily a new story node. The same scene may be presented again after an item moves, a person changes position, a door opens, a character becomes suspicious, or the participant learns something. The host requests a new projection from the updated state; the Renderer manifests it.

A scene may contain several moments. A moment may change without changing the underlying location or story node.

## 2. The scene model is more than its image

The authored scene model describes entities and their relationships independently of the image used to depict them.

At minimum, a spatially interactive scene needs stable identities for:

- locations and sub-locations;
- characters and other actors;
- physical objects and containers;
- interactable surfaces or regions;
- connections such as contains, supports, held-by, carried-by, attached-to, blocks, visible-from, and adjacent-to;
- the current spatial and interaction state of each relevant entity.

An image hotspot must resolve to a stable entity or interaction region. It must not be the identity of the item itself. If a knife moves from a counter into a character's hand, the same knife identity changes its relationship and location. The system must not create a second knife merely because the image is recomposed.

The Renderer uses scene geometry and spatial relationships to produce a visually meaningful projection and to associate visible regions with scene identities. It may help determine what is visible or spatially connected from a particular viewpoint. It does not decide what is true, what an actor knows, whether an action is authorized, or whether an uncertain action succeeds.

## 3. Interaction is contextual

The player does not receive one global list of actions. They inspect or select something in the scene, and the host derives the available interactions from the current context.

An interaction request is evaluated against:

1. the selected entity or region;
2. the actor performing the interaction;
3. the actor's current capabilities, condition, posture, equipment, and knowledge;
4. the selected object's properties and current relationships;
5. the current scene/session revision;
6. scenario-specific prerequisites, risks, and policies.

The same object can expose different actions as context changes.

### Example: a knife

1. A knife rests on a counter. The player selects it and can inspect it or attempt to take it.
2. If taking it is accepted, the knife's existing identity changes from being located on the counter to being held or carried by the character.
3. The next scene projection depicts the character holding that same knife.
4. Selecting the held knife offers actions appropriate to its current state: inspect, stow, conceal, throw, or another authored possibility.
5. Concealment options depend on the character's actual capabilities and circumstances—such as clothing, equipment, posture, and relevant ability—not on a generic always-available menu.
6. Selecting the counter while holding the knife offers contextually valid actions such as putting the knife back or using it on the counter.

These are proposed intents. Selecting an option does not itself prove success or commit a state change.

## 4. FSM_UserIO carries semantic interaction

FSM_UserIO is the semantic boundary between an interacting form's capabilities and application-owned meaning. It is not the GUI, renderer, hit-testing engine, authorization layer, or executor.

A pointer click, gaze fixation, spoken phrase, controller action, or accessibility switch is a source-level observation. The host/surface adapter interprets it in context and carries a semantic interaction through FSM_UserIO.

The intended flow is:

```text
Player / interacting form
        |
        v
GUI surface + Renderer spatial projection
        |
        v
Observation of a scene entity or region
        |
        v
FSM_UserIO semantic intent
        |
        v
Host policy + capability/prerequisite validation
        |
        v
SURPS scenario/rule resolution
        |
        v
Human referee when the outcome is uncertain
        |
        v
FSM_Execution performs an accepted transition
        |
        v
New authoritative scene/session revision
        |
        v
Renderer + GUI present the next moment
```

The GUI may take over the active screen while the Experience is playing, but that is a GUI presentation-mode decision. FSM_UserIO does not take ownership of the screen. The host remains responsible for focus, pause/resume, exit, accessibility, and returning to the previous application surface.

Capability is not authority. A character may be capable of attempting an action without being guaranteed permission, success, or a particular consequence.

## 5. Dialogue and player responses persist

Dialogue choices are not disposable navigation buttons. A selected response can become a durable, provenance-bearing session fact.

For example, an opening handler message may offer several internal responses. The player's selection can influence later dialogue, trust, suspicion, NPC reactions, and which actions are offered. Two participants may arrive at the same scene and see the same people, but receive different contextual interactions because their earlier responses and actions differ.

The authored model should prefer shared scenes with state-dependent projections over duplicating an entire scene graph for every response. A response variable must have:

- a stable identity;
- an explicit value or selected option;
- an actor/session scope;
- source and time/revision provenance;
- a declared set of consumers or conditions that may inspect it.

A response does not become world truth merely because it was selected. The host records what the participant said or chose; the scenario decides which later conditions may use that record.

## 6. Player perception is not world truth

The world model, each participant's knowledge, and the visual presentation are separate.

A visible person may have an unknown identity. The scenario may know their identity while the player does not. The player may infer something incorrectly. An NPC may know a fact that another NPC does not. A generated line of dialogue is not evidence that its content is true.

The host must construct a player-authorized projection from the authoritative scene/session state. Referee-only facts, hidden identities, private NPC knowledge, and adjudication notes must not be included in public client assets, scene hit-region metadata, or prompts supplied to a participant-facing companion.

A static public Pages site cannot securely conceal data delivered to the browser. Any live experience that relies on secrets requires a trusted host to issue authorized projections and validate submitted intents against the current revision.

The accessible observation view remains important: the participant should be able to request a textual description such as **“You enter the room and see…”**, including visible people, objects, exits, sounds, and other perceptible details. This view is another projection of what the character can perceive, not a dump of the referee's scene model.

## 7. Sound, music, and timing

Audio is part of the moment's presentation, not an afterthought. A moment may declare:

- ambient loops associated with a location;
- music cues and transitions;
- authored dialogue and voice performance;
- timed narration or subtitle events;
- silence, distortion, interruption, or loss of a signal as deliberate scene events.

Audio cues must be synchronized to the moment/revision and must not imply facts unavailable to the player's character. The host must support pause/resume and reduced-motion/reduced-audio/accessibility preferences without changing authoritative scenario state.

## 8. Historical and setting accuracy

The scene author owns the period, location, material culture, equipment, communications, and vocabulary. Those choices constrain which objects and actions can appear.

For the proposed first cinematic opening, **1981 in the Soviet Union** is a working setting choice, not a claim that the player is told the date or their role. A concealed, one-way or burst-style message is a better starting point than a modern always-open two-way earpiece. Soviet jamming of foreign broadcasts is historically documented in the period, but that fact must not be used as a blanket explanation for every lost clandestine signal. Signal loss should have an authored cause appropriate to the actual equipment and location.

Historical references for this proposed setting:

- [U.S. Department of State, Radio Jamming Policy in the East Bloc (August 13, 1981)](https://history.state.gov/historicaldocuments/frus1981-88v10/d4)
- [U.S. Department of State, 1977–1980 record describing Soviet broadcast interference](https://history.state.gov/historicaldocuments/frus1977-80v30/d212)
- [Clandestine communications in cyber-denied environments](https://www.tandfonline.com/doi/full/10.1080/18335330.2023.2209578), discussing late-Cold-War encrypted burst transmission.

## 9. Responsibility boundaries

| Concern | Owner |
|---|---|
| Scenario moments, scene entities, authored dialogue, clues, motives, and contextual affordance declarations | Scenario Experience / SURPS content |
| Character capabilities, item semantics, evidence, scenario state, and selected rule procedures | SURPS and selected MicroBundles |
| Spatial connectivity, visibility projection, hit regions, composition, and visual manifestation | Renderer / Visualize |
| Active presentation surface, scene transitions, captions, controls, and accessibility | GUI |
| Semantic observations and intents across forms and input sources | FSM_UserIO |
| Persistent companion identity, scoped NPC portrayal, observations, and bounded proposals | Hermit |
| Trusted session state, authorized projections, persistence, validation, and policy | Host / FSM_COS |
| Execution of accepted state transitions | FSM_Execution |
| Uncertain action adjudication until a separately validated evaluator is authorized | Human referee |

Hermit may describe, ask, suggest, plan, and propose within its assigned role. It may not adjudicate uncertain actions, reveal facts outside its scoped knowledge, or mutate authoritative world state.

## 10. First proving sequence

The first vertical slice should prove one complete loop rather than attempt to build a universal game engine:

1. Press **Play** and enter the Experience's immersive GUI presentation mode.
2. Present an authored cinematic arrival with a visual moment, narration, and sound.
3. Show an explorable room with spatially connected, selectable entities.
4. Select an object and receive contextual actions.
5. Attempt an action; record intent and obtain the required authorization/adjudication.
6. Commit one accepted item/location relationship change and render the same item in its new location.
7. Receive a short, period-appropriate handler message without revealing the player's full mission or identity.
8. Choose an internal response and persist it with provenance.
9. Reach a later shared scene whose dialogue or available interactions differ because of that response.

The existing CORE Spying material remains the selected rules source for its current playtest. The immersive presentation model must consume canonical rules/content rather than fork them. The first implementation must label simulated, human-operated, and implemented behavior honestly; it must not claim a digital evaluator or secure client-side referee mode that does not exist.


## 11. First cinematic opening prototype — Site K-17

The first cinematic presentation proof is [Site K-17](experiences/soviet-facility-opening/), a fictional 1981 Soviet-era opening. Its first three moments are deliberately ordered:

1. A period-inspired, schematic USSR map establishes the northern Ural region and marks the facility as an **alleged fictional location**.
2. The map hands off to an illustrated first-person approach across the grounds, revealing the estate and its security.
3. The player reaches the admission desk, receives a twenty-name identity challenge, and can request the first handler instruction. The instruction reveals and highlights the correct response; the player still commits the answer.

The current page is an authored presentation prototype. It does not yet provide a live 3D camera, production-quality rendered assets, recorded voice, a trusted session, or secure player/referee separation. In particular, a static public page cannot conceal the answer from someone inspecting its delivered source. A production host must keep the expected identity and handler knowledge server-side and send only the authorized player projection.

### FSM_API 2.0 integration rule

The prototype's HTML scene IDs are presentation selectors, not FSM_API state identities. Do not treat JavaScript strings, DOM IDs, or `GetHashCode()` values as persistent runtime identity. When the scene is connected to the authoritative session runtime:

- register the scene flow through the FSM_API 2.0 integer-backed runtime;
- use deterministic, versioned integer identities for executable states and transitions;
- keep readable names as authoring/diagnostic labels, with explicit forward/reverse mapping;
- keep player intent separate from committed transition; and
- let the host validate and commit accepted transitions before GUI/Renderer project the next moment.

The SURPS Pages pipeline checks out the FSM_API `development` source and runs [an executable native integer-backed cinematic-flow proof](../samples/SurpsCinematicFlow/Program.cs). It exercises the success and recoverable challenge paths and generates the state-flow SVG/manifest. That dependency does not make this static HTML prototype itself an FSM_API runtime: the proof and browser presentation are deliberately separate until a trusted session host connects them.
