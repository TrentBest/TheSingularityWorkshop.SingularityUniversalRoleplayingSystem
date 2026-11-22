# From Tabletop Procedure to Digital Systems

This page complements [A History of Roleplaying Games](history-of-roleplaying-games.md) and [Tabletop Campaign Composition and Rulebook Selection](tabletop-campaign-composition.md). It focuses on the transformation itself: what changes when a group moves from a human-refereed tabletop session to a computer-mediated experience?

## The tabletop loop

A tabletop roleplaying exchange can be described without reference to a particular game:

1. A participant states an intent for a character.
2. The group establishes the relevant situation and target.
3. The referee and selected rules identify applicable capabilities, constraints, and uncertainty.
4. The group resolves uncertainty using the agreed procedure.
5. The referee describes the outcome.
6. The character, world, and shared record are updated.

This loop is human-readable and can be performed with paper, pencil, dice, tokens, and conversation. The referee is not merely a random-number generator: the referee interprets context, applies the social contract, portrays the world, and handles situations that were not anticipated by the written rules.

## What software commonly takes over

| Tabletop activity | Digital responsibility | What must remain explicit |
|---|---|---|
| Character sheet and notes | Entity records and persistence | Meaning, units, ownership, history, and version |
| Dice, tables, arithmetic | Deterministic or stochastic evaluators | Probability, modifiers, assumptions, and reproducibility |
| Referee's initiative tracker | Turn scheduler or simulation clock | Time policy, deadlines, interruptions, and tie-breaking |
| Miniatures and maps | Spatial model and renderer | Coordinate system, scale, semantic identity, and collision rules |
| Rule lookup | Registry and rule/provider discovery | Stable identity, version, scope, applicability, and provenance |
| Referee's description | UI, animation, audio, generated text | Distinguish presentation from authoritative state |
| Campaign journal | Event history and saved world state | Persistence policy, authority, migration, and auditability |

Automating arithmetic is relatively straightforward. Automating judgment is much harder. A digital referee must either encode a decision procedure, ask a human, delegate to a provider/agent, or explicitly report that the situation is outside its model.

## Three broad digital strategies

### 1. Encode a tabletop ruleset

A title can translate a published ruleset into data structures, formulas, menus, and encounter procedures. SSI's *Gold Box* games are a useful example of computer-managed AD&D tactical encounters.

**Strength:** consistency and reduced bookkeeping.

**Trade-off:** the software can only resolve situations its implementation recognizes. The digital version may simplify or reinterpret the tabletop rules.

### 2. Design a game-native roleplaying system

A title can borrow RPG concepts—character progression, equipment, attributes, quests, party roles—while creating rules specifically for its own medium. Console RPGs such as *Dragon Quest* and *Final Fantasy* developed recognizable conventions this way.

**Strength:** mechanics and presentation can be designed together for a clear player experience.

**Trade-off:** the system may not map cleanly back to tabletop procedures or other games.

### 3. Build a systemic or persistent world

A title can expose interacting world systems, continuous time, networked authority, or player-created content. *Ultima Online*, *Deus Ex*, *The Elder Scrolls*, and many simulation sandboxes illustrate different parts of this direction.

**Strength:** player action can create consequences beyond a fixed sequence of authored choices.

**Trade-off:** systemic complexity requires careful ownership of state, synchronization, performance, and rule precedence.

These strategies can coexist in one title. None is a replacement for the tabletop rules; each is a different way of presenting, automating, or extending play.

## The boundary between presentation and simulation

A rendered sword swing is presentation. A sword-use interaction is a model of intent, capability, timing, reach, orientation, contact, resistance, and consequence. One animation may illustrate one outcome, but it is not a reusable rule for every sword, wielder, target, or circumstance.

Similarly:

- A climbing animation does not establish whether the agent can reach the ladder.
- A dialogue option does not prove that the character has the knowledge or authority implied by the line.
- A health bar does not explain what injury means for mobility, grip, balance, or reaction time.
- A physics engine does not automatically provide a roleplaying ontology, skill model, or social rulebook.
- An AI-generated response does not become authoritative world state merely because it sounds plausible.

A robust system keeps the underlying event and its presentation connected but distinct.

## The SURPS mapping

SURPS describes the shared roleplaying model independently of any one client or runtime.

- **Experience settings:** SURPS is opt-in per experience. Disabled means the experience does not require SURPS rulebook discovery. Enabled means it composes the master system and explicitly selected rulebooks/providers.
- **CORE:** the common baseline. Optional sourcebooks are selected explicitly for declared campaign scopes. LOD communicates detail/specialization; it does not silently replace another book.
- **Rulebooks/providers:** discoverable, versioned sources of rules or interaction behavior with inspectable inputs, outputs, assumptions, and provenance.
- **Gestures:** embodied posture, pose, movement, temporal phases, and interaction behavior. The interacted-with object/environment can supply a provider.
- **Physics:** physical quantities, constraints, and consequences. A provider must not claim physical behavior it does not implement.
- **StoryBuilder:** narrative construction and authored story structure, observing state and consequences rather than secretly replacing physical rules.
- **FSM_API / FSM_COS / FSM_Foundry:** state primitives, experience composition, and execution respectively. They remain usable when SURPS is disabled.

### Example: climbing a ladder

The ladder offers a climb interaction provider. It supplies a suitable approach location and orientation, an initial posture, and the interaction phases it supports. The agent contributes its anatomy, reach, grip, balance, mobility, condition, and intent. The provider evaluates a feasible attempt and reports progress, failure, interruption, or completion. Physics contributes the physical consequences.

The system should not hard-code “dogs cannot climb” as a universal species rule. It should evaluate the actual agent and ladder constraints, and report a grounded result or alternative.

### Example: using a sword

The sword offers a weapon-use provider. A trained agent may have access to practiced guards, parries, cuts, thrusts, recovery, and disarming responses. An untrained agent may attempt the same broad intent but produce less controlled, riskier variants. Timing, reach, orientation, balance, training, condition, and physical contact shape the outcome.

An injury changes the agent's condition and therefore changes later attempts. It should not merely switch to a cosmetic animation while leaving the capability model unchanged.

## The offline equivalence test

A digital feature is not fully specified if the only explanation of its behavior is hidden in code.

For every foundational rule, the source material should explain:

1. What participants need to know.
2. What a player declares or records.
3. What the referee/editor checks.
4. How uncertainty is resolved.
5. What state changes and what evidence is recorded.
6. How the same procedure maps to digital inputs, outputs, and execution.

The tabletop procedure is the human-readable specification. Software can automate it, accelerate it, visualize it, or coordinate many participants—but the core rule must remain understandable and playable without an app, internet connection, registry, or digital runtime.
