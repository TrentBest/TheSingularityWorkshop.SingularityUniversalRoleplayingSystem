# SURPS authoritative scene interaction proof

This proof establishes a deliberately small host-side contract. It is not a persistence engine, renderer, network protocol, rules engine, or replacement for FSM_UserIO.

## Authority boundary

- SceneSession owns authoritative entity relationships and a monotonically increasing scene revision for this in-memory proof.
- SceneProjection is observer-scoped. Entities marked non-player-visible are omitted; available actions are filtered by the observer's capabilities.
- A client submits a proposal against the revision it observed. A proposal never mutates the scene.
- The host rejects unknown actors, hidden/unavailable entities, undeclared actions, missing capabilities, invalid destinations, and stale revisions.
- An uncertain proposal remains pending until a referee adjudicates it.
- Adjudication compares the proposal's expected revision with the current revision. A stale decision cannot commit over newer state.
- An accepted take changes the existing entity's parent relationship. It does not manufacture a replacement object. The scene revision advances exactly once.

## Walkthrough

The fixture contains one room, a counter, a knife, and a private inventory container. The player sees the knife and receives inspect and take because their actor has the required manipulate capability. The inventory container and world root are not included in the player projection.

Selecting take creates a pending intent. The knife remains on the counter until a referee accepts the proposal. Acceptance moves the same knife identity to the player's inventory and increments the revision. An intent based on the previous revision is stale and cannot overwrite the new state.

## Deliberate limitations

This is an in-memory aggregate, not durable storage. A live host must persist the session, adjudication identity, event provenance, and revision transactionally. The current capability check is intentionally narrow and does not replace scenario prerequisites, reachability, inventory capacity, line of sight, actor condition, or rule resolution. adjudicatorId is an audit field, not authentication; the host must authenticate it. No private referee facts are included in SceneProjection.

The contract is aligned with the existing FSM_UserIO semantic interaction envelope, Renderer stable entity/observation concepts, and Hermit's read-only observation boundary. Those integrations remain adapters to be implemented and tested; this proof does not claim they are already wired.
