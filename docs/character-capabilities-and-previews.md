# Character capabilities, adversities, and action previews

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

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
3. **Gestures provider** supplies the character's lock-picking movement, adapted to the character's available body/rig and the action context.
4. **SURPS resolution** combines the selected capability, task difficulty, relevant circumstances, and only those adversities whose triggers apply. It presents the final probability and resolves the outcome.
5. **Presentation** shows the attempt and its consequences in the same frame, then returns control to the character sheet.

The environment provider owns environmental composition and environment facts. Gestures owns movement/gesture semantics and execution. Character visualization owns the character representation. SURPS owns the action meaning, capability/adversity semantics, probability contract, and outcome interpretation. A preview descriptor composes them without copying their records.

## Provider contract boundaries

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
- [Action preview schema](../schemas/action-preview.schema.json) defines provider composition and staged preview semantics.
- [Lock-picking preview descriptor](../.surps/previews/lock-picking.preview.json) is a proposed composition example.
- [Probability-first resolution proposal](probability-resolution.html) remains provisional.

Current status:
- Capability/adversity vocabulary and awareness axis: specified here, not yet integrated into a complete character-sheet schema.
- Character-point economy: not calibrated or implemented.
- Preview descriptor contract: specified.
- Character visualization, environment, Gestures, and resolution provider runtime: not wired together by this descriptor.
- Lock-picking preview: proposed, not executable.
