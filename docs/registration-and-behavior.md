# Rulebook Registration and Behavioral Resolution

## Purpose

A world should not need bespoke wiring for every domain behavior. SURPS provides a master registration and resolution layer: domain rulebooks register what they contribute, and the world can discover applicable rules and capabilities from entity, interaction, environment, and context.

Registration is not execution. A registered rule describes applicability, inputs, outputs, assumptions, constraints, units, dependencies, and evidence. The owning domain supplies the evaluator or executable capability.

## Registration model

The conceptual lifecycle is:

1. **Discover** rulebook providers from the composed experience/microbundle set.
2. **Validate** identity, version, compatibility, dependencies, and provenance.
3. **Register** the rulebook and its inspectable descriptors with the SURPS master registry.
4. **Index** concepts, rule identities, capability references, typed quantities, and applicability conditions.
5. **Resolve** candidate rules for a concrete entity, interaction, event, or environment state.
6. **Bind** known values to declared inputs using explicit type and unit semantics.
7. **Delegate** evaluation to the domain-owned capability.
8. **Record** result, evidence, rule/provider versions, and any state transition.

A rulebook registration should be idempotent by stable identity and version. Conflicting registrations must be reported, not silently overwritten. Multiple rulebooks may contribute compatible rules to one world; resolution must preserve provenance and expose ambiguity or conflict.

## Rule descriptors and editor visibility

Rule definitions are fundamental world knowledge. They should be hidden from ordinary experience presentation when appropriate, but always discoverable and inspectable by editors, authors, and diagnostic tools.

An inspectable rule descriptor should eventually carry:

- stable rule identity and semantic version;
- human-readable name, explanation, and source-book reference;
- domain and ontology concepts;
- applicability predicate and scope;
- typed inputs and outputs;
- physical or logical dimensions and units where applicable;
- constraints, assumptions, exclusions, and preconditions;
- required/provided capability identities and versions;
- evaluator/provider reference (not arbitrary executable text);
- evidence status, tests, provenance, and compatibility.

Editor inspection should answer: *why did this rule apply, what values were bound, which units were used, which provider evaluated it, what assumptions were active, and what evidence supports it?*

## Mathematical binding

SURPS should make mathematical relationships discoverable and bindable rather than manually reimplementing them in every world.

The registry can index declared quantities, dimensions, units, symbols, constraints, and rule inputs. When an interaction occurs, a resolver can match available entity/environment values to rule inputs, perform only valid unit conversions, and construct a typed evaluation request for the owning domain provider.

This must be explicit dimensional mathematics, not guesswork:
- quantities carry dimensions and units, not just untyped numbers;
- conversions must be dimensionally valid and traceable;
- missing inputs remain missing; they are not invented;
- assumptions and approximations are visible;
- domain evaluators remain authoritative for calculations;
- results retain the rule, provider, version, and input provenance.

The first useful implementation is metadata registration and deterministic rule/capability resolution. A general-purpose symbolic algebra engine, automatic theorem prover, or universal equation executor is **not** implied by registration and should not be smuggled into the initial contract.

## SURPS, Gestures, and Physics are entangled

Gestures is a first-class participant in SURPS. A gesture is not merely a rendered animation. It can express intent, posture, timing, coordination, perception, and a physical action through an embodied entity.

A representative reach-and-grasp interaction crosses the domains:

1. **SURPS** identifies the actor, intention, capability, target, context, and applicable role/behavior rules.
2. **Gestures** owns gesture vocabulary, posture/pose representation, temporal progression, recognition, and the authored motion/coordination model.
3. **Physics** evaluates physical quantities and consequences: kinematics, contact, impulse, forces, and constraints, using only capabilities it actually provides.
4. **FSM_API / FSM_Foundry** represent and advance state transitions and execute the composed experience.
5. **GUI / GUI.SVG** may visualize the intent, pose, constraints, and resulting interaction.

The domains should exchange stable, typed contracts and capability references. SURPS must not absorb gesture execution or physical simulation; Gestures must not become a duplicate physics engine; Physics must not become the owner of intent, role, or narrative meaning.

The relationship is bidirectional in the model: SURPS behavior can request a gesture capability, while recognized gesture evidence can become an event or observation that SURPS uses to update entity state, intent, or interaction context. Physical feasibility and consequences are resolved through Physics.

## First vertical slice

Build one editor-visible, end-to-end scenario before expanding the registry:

- register the Dungeon, Physics, and Gestures rulebooks/providers;
- describe an embodied actor, a reachable object, and an interaction intent;
- resolve the gesture capability for reaching and grasping;
- bind only available, dimensionally valid physical inputs;
- delegate physical evaluation to the existing Physics provider surface;
- show the selected rules, bound values, provider identity, and outcome in an editor/diagnostic view;
- preserve the full provenance chain.

This slice should expose what is genuinely implemented. In particular, do not label gravity integration, friction, angular impulse, or general rigid-body solving as available unless a domain provider actually supplies them.

## Ownership

| Responsibility | Owner |
|---|---|
| Master rulebook registry, ontology, rule resolution, provenance | SURPS |
| Gesture vocabulary, posture, temporal motion, recognition and coordination | Gestures |
| Physical laws, dimensional quantities, simulation and physical consequences | Physics |
| Underground environment and dungeon-specific phenomena | FSM_Dungeon |
| Laboratory apparatus, experiments, procedures and safety | SingularityLaboratories |
| City infrastructure, civic systems and city-domain rules | SingularityCity |
| Composition | FSM_COS |
| State primitives and execution/stepping | FSM_API / FSM_Foundry |
| Presentation | GUI / GUI.SVG |

## Contract maturity

This document extends the current minimal ISurpsRulebook marker/composition seam. The registry, descriptors, typed mathematical binding, and resolver described here are design targets to be validated against real provider implementations. Do not freeze public CLR signatures or publish a package until the Physics, Gestures, Dungeon, Laboratories, and City seams have been reviewed together.


## SURPS as an opt-in experience setting

SURPS is not a mandatory runtime layer. An experience declares whether SURPS is enabled in its settings/composition manifest. When disabled, the experience continues to use FSM_API, FSM_COS, and FSM_Foundry without acquiring a SURPS dependency or SURPS behavior. When enabled, the SURPS master system discovers the rulebooks and behavior providers included by that experience.

The setting is a composition choice, not a global switch that changes every experience on the machine. A host may expose it as a simple enabled/disabled checkbox while retaining detailed editor controls for rulebook selection, precedence, LOD, and diagnostics.

## Behavior comes from the interaction provider

An agent should not need a built-in catalogue of every possible behavior. The interacting object, environment, tool, or other participant can offer a gesture/interaction provider describing ways an interaction may be attempted. The agent contributes its own anatomy, capabilities, training, condition, intent, and available time. The provider evaluates the compatibility of those contributions and offers the applicable behavior paths.

### Example: approaching and climbing a ladder

1. The world identifies a ladder and a desired interaction.
2. The ladder's provider declares approach requirements, a target position, orientation, initial pose, and the subsequent climbing interaction.
3. The agent moves to the approach position and adopts the required initial pose, subject to its movement capabilities and physical constraints.
4. At the interaction boundary, the agent is assigned to the ladder's climbing provider for the attempt.
5. The provider evaluates the agent's anatomy and condition: available limbs, reach, grip, balance, mobility, and any other declared requirements.
6. A compatible agent receives the climbing behavior sequence. An incompatible agent receives a meaningful failure or alternative attempt path.

A dog is not simply told "you cannot climb." The ladder may offer exploratory attempts that expose why climbing fails: inability to establish the required grip, insufficient reach, loss of balance, or another grounded constraint. Those attempts are still subject to the provider's actual declared capabilities and Physics evaluation; they are not fabricated outcomes.

The provider belongs to the interaction being attempted, not to a hard-coded species behavior table. Other objects can offer other ways to interact with the same agent.

## Example: trained and untrained sword use

The sword offers a sword-use interaction provider. The agent with sword training registers its relevant capability/training evidence and receives the trained behavior set: controlled guards, parries, cuts, thrusts, feints, recoveries, and disarms where supported by the model.

An untrained agent can still ask the sword provider how it might attempt to use the object. It receives an untrained behavior set: poorly controlled swings, exposed openings, clumsy thrusts, weak or mistimed parries, and recovery/balance problems. The agent is not granted expertise merely because the provider can describe expert technique.

During a duel, both agents' attempts are evaluated against timing, pose, reach, weapon geometry, intent, training, current condition, and physical constraints. A trained fighter may exploit an untrained attack with a controlled parry, bind, displacement, or disarm. The outcome must emerge from declared capabilities and evaluated state, not from a scripted narrative guarantee.

If an agent is injured, the injury is a state/context change. The next behavior resolution can select an injured movement/gesture provider or a constrained variant of the existing provider. The injury changes what the agent can attempt, how quickly it can do so, and what consequences it risks.

## Time is part of behavior

Behavior is evaluated over delta time, not as a timeless list of animations. Providers should declare timing semantics and the FSM/API execution path should advance them through explicit state transitions.

Relevant time concepts include:
- decision window and response deadline;
- initiative or priority when a decision is late;
- preparation, commitment, execution, and recovery phases;
- interruption windows and reaction opportunities;
- action duration, cooldown, fatigue, and injury-related timing changes;
- time scale and pause/step behavior for the experience.

A turn-based encounter may pause at a decision boundary, collect player choices, then advance the simulation. A real-time or reaction-time encounter may keep advancing while a decision window expires, allowing an opponent to gain initiative. These are different rulebook policies over shared state/time primitives, not separate assumptions embedded in every gesture.

The source-book model must explain these concepts in tabletop terms as well as their digital delta-time expression.

## Core and rulebook LOD

SURPS CORE is the lowest common rules layer: shared terms, entity/capability descriptions, interaction structure, time/state vocabulary, and deterministic resolution principles. Domain and experience rulebooks may add higher-detail behavior.

LOD is explicit and selectable. It is not merely visual polygon detail. It describes the fidelity and cost of a behavior model: for example, a coarse opposed-skill resolution, a detailed sequence of guards and attacks, or a fine-grained pose/contact/timing simulation. Each higher-LOD rulebook must declare its relationship to CORE and the capabilities it requires.

An editor must be able to choose which rulebook/LOD supplies behavior for a given experience, entity class, interaction, or subsystem. Resolution should expose the selected source and precedence. A higher LOD must not silently replace CORE or another rulebook. If no higher-LOD rulebook is selected or available, the experience falls back to CORE behavior.

## Registration and offline equivalence

The master registry should register rulebooks and behavior providers, not require the world to be online. The same rulebook definitions must support:
- digital experiences, where providers are resolved and executed through the composed runtime;
- tabletop/offline play, where players and game masters use the printed or readable sourcebooks, character sheets, dice/tables, clocks, and written procedures.

The manual must define enough information to play without any digital service, application, or runtime. Digital automation is an implementation of the documented rules, not the only place where the rules exist.

## Next vertical slice

The first behavior-provider demonstration should be ladder approach/climb, followed by trained versus untrained sword interaction and injury transition. These cases test provider ownership, capability matching, failure alternatives, time, and LOD more effectively than a generic animation demo.


## Behavior compilation, workshop calibration, and runtime caching

The registry describes which rules and capabilities exist; it does not make them executable. A behavior source belongs to its authoritative domain. SURPS resolves the selected source and provider versions, preserves their provenance, and coordinates the adapters.

The shared lifecycle is:

1. Author the domain behavior and its operating envelope.
2. Validate identities, typed inputs, units, assumptions, constraints, and provider references.
3. Run representative and boundary scenarios in the authoring/workshop environment.
4. Derive the tabletop adapter from those results: dice targets, probability bands, qualitative effect tiers, tables, and printable aids.
5. Compile the digital adapter into reusable behavior artifacts, provider-binding plans, and response data.
6. At experience load, resolve versions and warm the immutable compiled artifacts.
7. During play, bind current actor, target, equipment, environment, and time state; evaluate only what has changed and record provenance.

### Cache policy

Cache immutable compiled behavior, validated rule graphs, provider binding plans, compiled expressions, static reference data, and reusable response curves. The cache key must include the behavior content hash, book/version identity, schema and unit versions, compiler version, provider version, and relevant compile settings.

Do not cache a final interaction outcome across changes to mutable world state. A moving target, changing weather, injury, equipment loss, closed door, or elapsed time may change the answer. The runtime must bind current state even when the compiled behavior is warm.

The [Behavior Model and Adapters contract](behavior-and-adapters.md) defines this boundary. The [Living System Guide](system-guide.html) includes an explicitly illustrative fireball profile that demonstrates workshop sampling and a derived tabletop target. It is a teaching prototype, not a validated Physics evaluator or production compiler.

### Required evidence before calling the pipeline implemented

- reproducible workshop samples with a fixed seed and recorded calibration envelope;
- held-out scenario validation showing the tabletop projection preserves the intended outcome distribution;
- versioned compiled artifacts and cache-key tests;
- invalidation tests when source, provider, compiler, schema, units, or settings change;
- warm-cache and cold-cache benchmarks;
- tests proving live-state changes are not hidden by cached final outcomes;
- provenance traces connecting a result to its source book, rule, provider, versions, and bound inputs.
