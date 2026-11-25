# Living World Opportunities and In-World Economy

## Purpose

A SURPS world should not feel like a menu of quests placed in front of the player. It should be a coherent environment whose places, people, institutions, resources, and events can create opportunities. A player may discover an adventure because they deliberately investigate something ordinary: they stop to read a notice board, listen to a conversation, ask a shopkeeper a question, or spend an evening in a tavern.

The world should reward attention without requiring the player to guess a hidden authorial trigger. Opportunities emerge from world state and are revealed through meaningful interaction.

This document defines the domain behavior and integration boundaries. It is not a claim that autonomous NPC schedules, clue generation, job boards, or economic simulation are already implemented.

## 1. The environment is an opportunity surface

Every meaningful place can expose several kinds of interaction:

- **Presence:** what is visibly or audibly happening without deliberate inspection.
- **Attention:** what becomes available when a participant looks, listens, reads, waits, or approaches.
- **Inquiry:** what a participant can learn by asking an entity or using a capability.
- **Action:** what a participant can change by touching, moving, taking, buying, offering, repairing, or otherwise acting.
- **Consequence:** the authoritative world-state changes caused by the interaction.

A notice board illustrates the distinction. Passing it may show that papers are posted. Stopping to read it can reveal available work, a public warning, a missing-person notice, or a suspicious detail. Examining one posting closely may expose a clue: a date that conflicts with another record, a repeated mark, a forged seal, or a location that matters to an ongoing situation.

The clue is not a quest marker that the renderer invents. It is information attached to a world object, with provenance, visibility conditions, and a relationship to the underlying situation. The player may notice it, overlook it, misunderstand it, or investigate it further. Character capability, context, time, and the chosen interaction can affect what is perceived; the renderer must not decide what is true.

A tavern can expose a different opportunity surface: patrons, rumors, a job offered by an employer, a dispute, a merchant seeking an escort, or someone quietly looking for a particular person. Entering the tavern does not guarantee a job. It places the character in a social environment where the opportunity may exist and where attention, reputation, timing, and conversation matter.

## 2. Opportunities are world records, not UI buttons

An opportunity should have a stable identity and explicit state. A job posting, rumor, invitation, lead, contract, or discovery can share a common opportunity vocabulary while retaining type-specific details.

A useful opportunity record includes:

- issuer or originating entity;
- location and discovery surface;
- creation time, availability window, and expiry conditions;
- prerequisites and visibility/discovery conditions;
- description, known facts, uncertain claims, and concealed information;
- requested outcome and acceptable alternatives;
- reward, costs, payment terms, and collateral where applicable;
- risk, opposition, deadlines, and consequences;
- acceptance, assignment, progress, completion, failure, and cancellation state;
- provenance linking the opportunity to the event, need, or actor that produced it.

A posting can be discovered without being accepted. Acceptance creates a relationship or contract; it should not teleport the player into a mission. A mission or quest can be assembled from the accepted opportunity, but remains a scenario structure inside the containing Experience. The SURPS System Experience is not rebuilt for each posting.

Opportunities may be authored, generated from simulation state, or produced by a combination of both. Generated content must preserve its source state and deterministic inputs so that it can be explained, tested, and replayed.

## 3. The economic loop is part of play

Money must have meaning in the world. It is not merely a score counter or a reward number attached to a completed quest.

The game-facing economic loop should connect:

1. **Production and services** — people and organizations create goods, perform work, provide lodging, transport, repair, information, protection, and other services.
2. **Ownership and inventory** — goods have owners, locations, quantities, condition, and availability.
3. **Markets and exchange** — offers, bids, prices, supply, demand, scarcity, negotiation, and accepted trades.
4. **Work and contracts** — wages, commissions, advances, expenses, deposits, penalties, and payment on verified outcomes.
5. **Obligations** — debts, credit, rent, taxes, fees, upkeep, recurring payments, and other commitments.
6. **Accounting and history** — every transfer has parties, amount, currency, reason, time, and a traceable transaction record.

A job should state what is being paid, by whom, in which currency, under what conditions, and when payment becomes due. An advance is not the same as a final reward. Expenses may reduce the net result. A failed contract may still have costs or partial payment. A merchant's ability to pay depends on its actual resources and obligations, not on an unlimited quest-reward generator.

The world should support more than one currency and economic convention where a setting requires them. Exchange rates, denominations, barter, credit, and local acceptance are explicit domain rules, not assumptions embedded in UI code.

SURPS defines the roleplaying meaning of work, ownership, exchange, reward, obligation, and economic consequence. The Economy domain owns monetary and market simulation capabilities. A SURPS Experience composes the required Economy MicroBundles through the Workshop/FSM_COS path rather than implementing a second economy inside SURPS.

## 4. The world can create work without a quest designer

A useful emergent loop is:

```text
World state changes
      |
      v
Needs, events, scarcity, relationships, and schedules
      |
      v
Actors and institutions form intentions or offers
      |
      v
Opportunity becomes available at a place or through a person
      |
      v
Player notices, investigates, negotiates, accepts, or ignores
      |
      v
Action changes world state and economic obligations
      |
      v
New opportunities and consequences become possible
```

Examples:

- A delivery is late because a bridge is damaged. A merchant posts a courier contract; the detour reveals evidence of deliberate sabotage.
- A tavern keeper needs a reliable person to escort a guest. The guest's real purpose is not stated in the posting and emerges through conversation.
- A job-board notice offers a reward for locating a missing worker. The posting's ink, date, and wording connect it to another event in the settlement.
- A shop has no stock because its supplier has not arrived. The player can investigate, find another supplier, pay a premium, or leave the shortage unresolved.
- A character's reputation changes which employers approach them, what terms are offered, and whether an advance is trusted.

These are not necessarily separate authored quests. They can be consequences of the same world entities, relationships, inventories, schedules, and transactions the simulation already tracks.

## 5. Separate truth, knowledge, and presentation

The architecture must preserve three distinct states:

- **World truth:** authoritative facts and current simulation state.
- **Participant knowledge:** what a character has observed, inferred, been told, verified, or merely heard claimed.
- **Presentation:** what the current interface chooses to display, animate, highlight, or make interactive.

Reading a notice may add an observation to participant knowledge. It does not make every statement on the notice true. Hearing a rumor records a report with a source and reliability context. A renderer can animate a crowded tavern, but it cannot create authoritative customers, transactions, or rumors merely by drawing them.

This separation enables mystery, deception, investigation, and meaningful uncertainty without confusing visual detail with simulation.

## 6. Time, scale, and fidelity

The same opportunity model should work at several levels of fidelity:

- **Authored tabletop:** a referee presents a board, tavern, employer, and consequences using the same concepts.
- **Interactive digital:** selecting, reading, asking, or trading routes through domain commands and returns explicit results.
- **Simulated settlement:** schedules, inventories, production, markets, and actor goals update world state over time.
- **Large-scale world:** simulation can aggregate distant or low-relevance activity while preserving the facts needed when a participant approaches or investigates.

Level of detail controls how much is simulated or presented, not which source is authoritative. A settlement may aggregate market updates while no player is nearby, then resolve a specific shop or conversation in greater detail when relevant. Any approximation must have an explicit policy and must not silently contradict committed transactions or observed facts.

## 7. Ownership and composition

- **SURPS** owns shared roleplaying concepts: actors, intentions, observations, knowledge, opportunities, work, contracts, consequences, and the semantics of interaction.
- **Economy** owns currency, balances, markets, pricing, inventory exchange, and accounting capabilities.
- **World/environment domains** own places, topology, environmental state, and spatial relationships.
- **Character/NPC domains** own identity, capabilities, schedules, goals, relationships, and behavior state.
- **Story/scenario Experiences** own authored premises, named characters, setting-specific opportunities, and curated narrative structure.
- **Workshop and FSM_COS** assemble the Experience and its required MicroBundles; the host executes commands and presents projections.
- **GUI/SVG** presents the world and projects interaction affordances without becoming the source of truth.

A scenario may author a particular job board or tavern, but shared opportunity and economic semantics remain reusable. A world-specific posting is content; the system that explains how postings, contracts, payment, and consequences work is a reusable capability.

## 8. Acceptance scenarios

The first useful end-to-end proof should exercise ordinary interaction rather than a preselected quest list:

1. A player enters a settlement and sees a notice board as part of the environment.
2. The player chooses to inspect it; the system records what the character can actually perceive.
3. One posting contains a discoverable clue whose source and truth state are distinct from the player's interpretation.
4. The player visits a tavern and can discover an opportunity through a person, conversation, or social context.
5. The player negotiates or accepts a contract with explicit reward, terms, deadline, and issuer.
6. Completing the work produces a verified outcome and ledgered payment; expenses and obligations are accounted for.
7. The resulting world changes can create new postings, relationships, prices, or consequences.
8. The same authored scenario can run as a tabletop experience without requiring the digital simulation.

The proof is successful when the player can discover and pursue work through the world, economic state is consistent and auditable, and the visual layer never fabricates authoritative facts.

## Implementation status

This is a domain and integration target. The existing living settlement SVG is an ambient illustration, not an NPC or commerce simulation. The current SURPS repository does not yet claim an implemented emergent opportunity engine, job-board service, market simulator, or transaction ledger.
