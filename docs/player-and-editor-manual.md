# SURPS Player and Editor Manual

## Part I — The tabletop roleplaying system

### 1. What a roleplaying game is
Explain players, game master, characters, entities, setting, intent, interaction, uncertainty, consequences, and shared authorship. Establish that SURPS must be playable with paper, pencil, dice or agreed randomization, character sheets, rulebooks, and a clock where needed.

### 2. Creating a character or agent
Describe identity, attributes, capabilities, training, anatomy, condition, equipment, goals, and history. Separate what a character is from what it can currently do.

### 3. Declaring intent and resolving interactions
Teach the player-facing procedure: describe intent, identify target/context, consult the relevant rulebook/provider, establish applicable capabilities and constraints, resolve uncertainty, record consequences, and update state.

### 4. Time, turns, initiative, and reaction
Explain turn boundaries, decision windows, delta time, action phases, initiative, reaction opportunities, interruption, deadlines, recovery, and what happens when a player does not decide in time. Include both paused turn-based play and continuously advancing encounters.

### 5. Conflict and capability
Explain opposed capabilities, trained/untrained behavior, equipment providers, risk, injury, recovery, and consequences without assuming digital animation or automation.

### 6. Rulebook selection and LOD
Explain CORE as the baseline and optional rulebooks as higher-detail models. Provide examples of choosing coarse resolution for a fast encounter or detailed gesture/pose/timing resolution for a pivotal duel.

### 7. Running an offline session
Provide the complete paper procedure, character and entity records, rule lookup, timing aids, dice/tables where defined, examples, and a glossary. A reader must be able to play without an application, internet connection, or digital registry.

## Part II — How SURPS was digitized

### 8. From tabletop procedure to explicit model
Map players, game master, characters, attributes, capabilities, actions, timing, randomization, state, and consequences to digital concepts. Explain that digital execution must preserve the tabletop rules rather than inventing hidden rules.

### 9. Opt-in composition
Show SURPS as an experience setting: disabled means no SURPS rulebook system is required; enabled composes the master registry and selected rulebooks. Explain how an experience can use FSM_API/FSM_COS/FSM_Foundry without SURPS.

### 10. Rulebook registration and provider discovery
Explain stable identity/version, registration, applicability, dependencies, provenance, conflict handling, editor visibility, and deterministic resolution.

### 11. Gesture providers and embodied behavior
Explain how objects and environments offer interaction providers, while agents contribute anatomy, skill, condition, intent, and time. Include ladder climbing, sword use, trained/untrained behavior, injury transitions, and failure alternatives.

### 12. Physics and mathematical binding
Explain typed quantities, units, dimensions, assumptions, physical constraints, domain-owned evaluators, and evidence. Clearly distinguish implemented provider capability from conceptual rules.

### 13. LOD, determinism, and execution
Explain selected rule source, precedence, fallback, delta-time stepping, state transitions, reproducibility, and editor diagnostics.

### 14. Editor handbook
Document how to enable SURPS, choose rulebooks/LOD by scope, inspect descriptors and provenance, diagnose missing providers/inputs, and verify behavior without silently changing source rules.

## Editorial contract

Every chapter should contain: (1) theory and vocabulary, (2) tabletop/offline procedure, (3) worked example, (4) digital mapping, (5) editor/player reference, and (6) links to the authoritative domain implementation and evidence. Keep explanatory text and machine-readable descriptors traceable to the same rule identity/version.

This is the chapter plan, not a claim that all chapters or digital providers are already implemented.
