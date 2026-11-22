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
