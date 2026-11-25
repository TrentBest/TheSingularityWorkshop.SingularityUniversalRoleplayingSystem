# Character capabilities, adversities, and action previews

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Renderer/development/docs/assets/moniker.svg)

## Living character sheets and world surfaces

The first five empty, data-bindable SVG sheet themes and an ambient settlement illustration are now available as visual scaffolds. The [Character Studio](character-studio.html) can select and preview the three starter themes; premium themes are catalogued as preview-only until a real entitlement provider exists. See [Living Character Sheets and World Surfaces](living-world-and-character-studio.md) for the architecture and fidelity progression. The SVG actors and motion are illustrative, not authoritative simulation.

## Character construction

SURPS character construction should be expressed in terms of **Capabilities** and **Adversities**.

- A **Capability** is something the character can bring to an action. Players allocate character points to acquire or improve capabilities. Ratings are bounded values with defined semantics; a rating is not itself the final chance of success.
- An **Adversity** is a meaningful limitation, vulnerability, compulsion, condition, or disadvantage that can affect play. An adversity is not a free-floating penalty: its trigger conditions and effects must be explicit.
- Both kinds have an **awareness** dimension: `conscious` or `subconscious`. This is independent of whether the trait helps or hinders the character.

Conscious/subconscious describes how the trait is represented in the character and how it can be engaged or triggered. It must not be used as a simplistic multiplier on probability. For example, Lock Picking may be a conscious capability; a trained automatic response may be a subconscious capability; a deliberate fear may be a conscious adversity; and an involuntary phobia response may be a subconscious adversity.

Character-point costs, adversity point values, caps, improvement curves, and advancement pacing remain calibration decisions. The first contract records these separately so the economy can be tuned without redefining what a capability or adversity means.

## Capability is not probability

The character's capability rating is one input to a resolution. The action's difficulty and relevant circumstances are separate inputs. Adversities participate only when their declared triggers apply.

`finalChance = resolve(capability, difficulty, circumstances, triggeredAdversities)`

The output is a probability from 0 to 100. A percentile roll is one possible physical interface; a preview may also show the deterministic probability before any random result is generated. Do not conflate:
- capability rating;
- difficulty or adversity effects;
- final success probability;
- the sampled outcome;
- the quality and consequences of that outcome.

The formula and point economy are not yet adopted. Keep them versioned and testable while comparing candidate curves against existing 2d6 playtest procedures.

## Action previews are MicroBundle offerings

A MicroBundle may offer one or more **action previews** alongside its records and book assets. A preview is a declarative composition of providers, not a new owner of their domain behavior. It describes the experience to assemble and the order in which providers contribute.

The lock-picking preview is the first proposed vertical slice:

1. **Character visualization** presents the selected character in a stable, character-local frame.
2. **Environment preview provider** creates the immediate scene around that character: the lock, its mounting, nearby surfaces, light, and other relevant conditions. The environment fades into the character's frame rather than replacing the character sheet or teleporting the character into an unrelated scene.
3. **Gestures provider** filters offered procedures against actor requirements and available environment anchors, then supplies the character's lock-picking movement, adapted to the character's available body/rig and the action context. The existing Gestures contracts already separate `GestureOfferSelector` (eligibility and rejection reasons), `GesturePlayback` (caller-driven lifecycle), and `GestureEvaluator` (deterministic evaluated pose). These are useful existing building blocks. Gestures now includes a test-backed SURPS lock-picking offer fixture (`surps.core.spying.lock-picking.insert-and-turn.v1`) that requires `manual-dexterity`, `lock-tool-use`, and the live `lock-cylinder` anchor; it proves offer eligibility and playback composition, not a completed lock-picking animation or successful physical interaction.
4. **SURPS resolution** first calculates and displays the chance from a frozen character/action/environment snapshot. After the gesture is presented, the authoritative action/domain integration supplies the evidence used to resolve the outcome. An evaluated pose is not evidence that the lock opened.
5. **Presentation** shows the attempt and its consequences in the same frame, then returns control to the character sheet.

The environment provider owns environmental composition, semantic anchors, and environment facts. Gestures owns movement/gesture definitions, offer eligibility, deterministic pose evaluation, and playback primitives. Character visualization owns the character representation. SURPS owns the action meaning, capability/adversity semantics, probability contract, and outcome interpretation. The host/domain integration owns authoritative interaction evidence and persistent effects. A preview descriptor composes them without copying their records.

## Provider contract boundaries

Gesture eligibility is not the same thing as rated competence. The Gestures selector uses actor capability *requirements* and environment anchor availability to decide whether a procedure is compatible. SURPS then uses the character's rated capability, difficulty, circumstances, and triggered adversities to calculate success probability. A character can be eligible to attempt a gesture without being highly competent at the action; a highly rated capability does not make an incompatible rig or missing anchor valid.

A provider should declare:
- stable provider ID, owner repository, and version;
- the role it fulfills and supported action/context identifiers;
- required inputs and produced outputs;
- readiness/failure behavior and capability negotiation;
- provenance for any domain facts it contributes.

The preview host owns orchestration, cancellation, lifetime, and presentation framing. Providers must not silently mutate the character sheet or authoritative character state. The resolver receives an immutable action snapshot; the preview can show a projected attempt, but committing character changes or persistent world effects requires the owning system's explicit action.

Provider discovery is not runtime availability. A descriptor marked `proposed` is a composition target, not proof that every provider can currently be loaded or that this preview can execute.

## Contracts and status

- [Character capability/adversity schema](../schemas/character-capability.schema.json) defines the common character-facing shape.
- [Action preview manifest schema](../schemas/action-preview-manifest.schema.json) lets each MicroBundle offer multiple previews.
- [Action preview schema](../schemas/action-preview.schema.json) defines provider composition and staged preview semantics.
- [CORE Spying preview manifest](../.surps/previews/core-spying.previews.json) registers the bundle's available previews.
- [Lock-picking preview descriptor](../.surps/previews/lock-picking.preview.json) is a proposed composition example.
- [Probability-first resolution proposal](probability-resolution.html) remains provisional.

Current status:
- Capability/adversity vocabulary and awareness axis: specified here, not yet integrated into a complete character-sheet schema.
- Character-point economy: not calibrated or implemented.
- Preview descriptor contract: specified.
- Character visualization, environment, Gestures, and resolution provider runtime: not wired together by this descriptor.
- Gestures repository: deterministic evaluator, offer selector, and playback contracts are available; a lock-picking-specific offer fixture is now implemented and test-backed in [Gestures](https://github.com/TrentBest/TheSingularityWorkshop.Gestures/blob/development/docs/SURPS_LOCK_PICKING_GESTURE_OFFER.md). It is not yet a runtime provider loaded by the SURPS preview host.
- Lock-picking preview: still proposed as an end-to-end experience; the Gestures offer-selection/playback substep now has an executable test fixture.
