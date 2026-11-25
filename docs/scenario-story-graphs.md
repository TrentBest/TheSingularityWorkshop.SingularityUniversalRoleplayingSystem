# Scenario Story Graphs

A SURPS scenario can be presented as a choice-driven story without requiring spatial movement controls. The player moves through situations by choosing what their character intends to do. The underlying authored adventure is a graph, not a linear page sequence.

## The graph is the adventure

- A **node** is a meaningful situation: a briefing, observation, conversation, investigation, confrontation, or ending. It is not merely a screen.
- A node's **player presentation** describes only what the player-facing experience may currently present.
- A **choice** expresses an intention and points to the next possible situation.
- A choice's **requirements** describe scenario state needed before it is offered.
- A choice's **state effects** name scenario facts that may become true after the transition is accepted.
- **Converging paths** let different approaches reach the same situation while preserving the state accumulated along the way.
- **Endings** are explicit nodes. Distinct achievements should not be collapsed into one pass/fail result.

The author maps the whole adventure. The player sees only the current node and choices that are valid for the character's current state and authorized knowledge.

## Choice is not adjudication

A choice records what the player wants to attempt. It does not automatically mean the attempt succeeds.

- Selecting any choice first records **pending player intent**. Selection alone never advances the current node or changes scenario state.
- `direct` choices are decisions that need no uncertain-action ruling; their transition may be committed immediately.
- `referee` choices remain pending until a human referee uses the selected scenario procedure, records the ruling, and explicitly accepts the transition.
- `setsAll` effects apply only when the transition is committed—not when the player selects the choice.
- `nextNodeId` names the continuation after commitment for direct choices and referee choices without an outcome map.
- A referee choice may instead declare `outcomeRuleId` and `outcomeBranches`. The rule ID points to the selected MicroBundle's outcome vocabulary; each branch key is one of that rule's stable outcome IDs and supplies its own continuation and optional state effects.
- An outcome-mapped choice has no default `nextNodeId`. The human referee must record an outcome from the referenced rule and explicitly accept the matching branch. An unmapped or unknown outcome cannot silently fall back to another path.
- Branch state effects are applied only when that specific branch is committed. The graph does not calculate a roll, choose an outcome, or advance pressure clocks.

The graph does not define a new dice system, evaluate uncertain actions, advance clocks, or mutate authoritative world state. It describes narrative possibilities. CORE Spying remains the selected source for the current provisional tabletop procedure. Its outcome IDs are namespaced to that MicroBundle; another book may define a different vocabulary. The graph maps those source-specific results to authored scenario continuations without promoting them into universal SURPS outcome categories.

## State and knowledge

Scenario state and character knowledge are related but not interchangeable. A flag such as `recipient_identified` records a scenario milestone; it must not silently grant every character knowledge of the underlying facts. The session host must eventually project information according to the observing character's access, evidence, and provenance.

The graph's `playerPresentation` is suitable for the player-facing projection. Authoring metadata, state flags, referee guidance, and any future private fact ledger must not be treated as player-visible content merely because they exist in the authoring model.

**A static Pages site cannot securely conceal data shipped to the browser.** This graph is an authoring and validation artifact, not a secure referee store. A future live experience must deliver authorized projections from a trusted host and keep private facts out of public client assets.

## Current pilot: The Missing Ledger

[The Missing Ledger story graph](../experiences/missing-ledger/story-graph.json) maps the opening investigation through the market, Mara, the river contact, the storehouse, the river landing, evidence review, and four distinct outcomes.

The graph deliberately allows multiple approaches and converging paths. For example, a player may identify the recipient by observation or learn about the river through a contact. Both routes can reach the landing, but they need not produce identical knowledge or evidence.

The `follow-the-contact` choice is the first outcome-mapped example. It references `surps.core.spying.resolution.outcome-bands` and defines separate continuations for that rule's strong success, success, mixed result, and miss. Strong success reaches the landing with an additional `tail_unnoticed` state effect; success reaches the landing without that extra benefit; a mixed result preserves the lead but creates a compromised-tail situation; a miss loses the contact and offers a different investigation route. The referee chooses and commits the branch. None of these results is inferred by the graph.

The [story graph JSON Schema](../schemas/scenario-story-graph.schema.json) defines the portable authoring shape. Repository tests validate node identity, all branch destinations, state-key references, rule/outcome identity, and graph reachability. This is an authoring contract and testable fixture—not yet a general story runtime or a claim that the browser experience is graph-driven. Outcome branches are optional and source-specific; legacy single-continuation choices remain valid.

## Boundaries

| Concern | Owner |
|---|---|
| Scenario scenes, choices, motives, clues, and endings | Scenario Experience |
| Shared spying concepts and current tabletop procedure | CORE Spying |
| Character identity and portable character contract | SURPS character contract |
| Session identity, trusted state, persistence, and authorized projections | Host / FSM_COS / FSM_Execution |
| Companion dialogue and bounded proposals | Hermit |
| Player controls and visual presentation | GUI / Renderer / Visualize |
| Validation evidence | SURPS tests and CiAi |

A story graph does not replace the SURPS System Experience, the book-selection document, or the portable FSM_COS composition manifest. It is scenario content consumed by an Experience.
