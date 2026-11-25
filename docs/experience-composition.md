# SURPS and Lightweight Experience Composition

## The two meanings of Experience

SURPS needs two related but distinct kinds of Experience:

1. **The SURPS System Experience** is the full composition of the roleplaying system itself. It is an authored, versioned composition request that declares the SURPS MicroBundles and external capabilities SURPS consumes. FSM_COS assembles it from those MicroBundles.
2. **A lightweight scenario Experience** is a playable quest, mission, adventure, or campaign that consumes SURPS. It selects only the rules, content, providers, and presentation assets needed for that scenario. It does not copy or reimplement SURPS.

The word *Experience* names the composed thing presented to a participant. The manifest is only its portable composition request; it is not the running Experience, its host, or its renderer.

## 1. SURPS is itself an Experience

SURPS must be usable as a composed system, not merely as a library of books or a checkbox in somebody else's campaign.

The SURPS System Experience is the canonical composition of the roleplaying system. Its manifest selects the SURPS-owned MicroBundles and the external MicroBundles/providers required to make the system work. As SURPS admits more bundles, the composition grows by declaration and dependency resolution rather than by hard-coded assumptions about today's registry.

This is self-assembly in the FSM_COS sense:

```text
SURPS System Experience manifest
    ├── SURPS-owned MicroBundle roots
    ├── selected external capability roots
    └── exact portable identities / versions / digests
                    |
                    v
             FSM_COS resolver
                    |
          dependency closure + validation
                    |
                    v
             Runtime Assembly
                    |
                    v
          SURPS System Experience
```

There is no recursive bootstrap: FSM_COS and the host/platform are the composition machinery that assemble the SURPS System Experience. SURPS does not need to contain a second copy of FSM_COS in order to request its own domain MicroBundles.

The manifest must use portable MicroBundle identity (canonical ontology string) and exact artifact version, with SHA-256 where the artifact contract requires it. Repository storage handles and platform-local numeric slots never belong in the portable manifest. The current numeric FSM_COS RuntimeManifest remains an internal compatibility/runtime surface behind the portable resolution boundary.

The SURPS System Experience is not the same thing as a rulebook, a book registry, or the current CORE Spying pilot. Books are curated views; MicroBundles own reusable records and capabilities; the system Experience composes the required roots and their dependency closure.

## 2. Lightweight scenario Experiences

A scenario Experience is deliberately smaller. Examples include:

- a single quest or short adventure;
- a mission or linked set of operations;
- a campaign composed of multiple sessions, missions, and quests;
- a demonstrator designed to show one SURPS subsystem in operation.

A Dia Blackthorne-style adventure is the right scale of example: a compact, self-contained story with characters, locations, situations, objectives, and consequences. It can demonstrate SURPS without pretending to be the entire system.

A lightweight Experience declares its SURPS compatibility/dependency and selects the books or views relevant to its premise. The selected book views resolve to canonical MicroBundle records; they do not fork those records. The scenario may also contribute its own setting, characters, maps, encounters, and narrative material under its own repository/domain ownership.

A quest, mission, or campaign is content structure within an Experience, not automatically a new runtime or a new copy of SURPS. A campaign can contain missions; missions can contain quests or scenes. The composition manifest stays focused on the capabilities and content roots required to assemble the Experience.

## 3. Keep the layers separate

| Layer | Responsibility |
|---|---|
| SURPS System Experience | Composes the roleplaying system's required MicroBundles and external capabilities |
| Scenario Experience | Declares a playable quest, mission, adventure, or campaign and its dependencies |
| Rulebook / book view | Selects canonical records for an audience, scope, and LOD |
| MicroBundle | Owns independently versioned records, capabilities, procedures, or assets |
| Portable Experience manifest | Requests portable MicroBundle identities and exact revisions |
| FSM_COS | Resolves dependencies and assembles the requested MicroBundles |
| Host / renderer / executor | Presents and runs the assembled Experience |

The existing experience book-selection contract (represented by `schemas/experience-books.schema.json` and `docs/examples/experience-books.example.json`) is a **book-selection document**, not the portable FSM_COS composition manifest. It answers which books and contribution documents an Experience selects. It must remain separate from the portable manifest that requests MicroBundle artifacts.

Likewise, LOD is editorial detail, not a dependency resolver or an automatic precedence rule. A scenario selects applicable books and records explicit scope/overrides; the composition layer resolves declared MicroBundle dependencies.

## 4. Demonstrations are small Experiences, not the system

The quests, missions, and campaigns already identified as demonstrations should remain lightweight fixtures. They prove that the system can be used in context and provide concrete pressure against which the ontology, rules, character model, and presentation can be tested.

They should not be promoted into the SURPS System Experience, and their scenario-specific material should not become canonical SURPS content merely because it appears in a demonstration. Shared roleplaying semantics belong to SURPS; setting-specific material belongs to its owning Experience or domain MicroBundle.

## 5. Publication and change control

A published Experience manifest is an immutable, versioned request snapshot. A creator's newer MicroBundle revision does not silently change an existing Experience. The Experience author reviews the update, validates the resulting composition, and publishes a new manifest version.

Before activation, resolution must fail closed for unknown or ambiguous ontology identities, missing artifacts, conflicting mappings, version mismatch, or digest mismatch. A repository address is not a runtime ID, and a platform-local slot is not portable identity.

## Current implementation boundary

SURPS currently has a repository-local MicroBundle registry with the CORE Spying pilot and a separate book-selection schema/example. It also has a generated Character Studio catalog and provenance-preserving book/view projections. Those are useful authoring and validation pieces; they are not yet a complete portable Experience-manifest publisher or an end-to-end SURPS System Experience executor.

The portable identity and dependency contract is being defined additively in [MicroBundleDomain issue #28](https://github.com/TrentBest/TheSingularityWorkshop.MicroBundleDomain/issues/28), with the corresponding FSM_COS boundary tracked in [FSM_COS issue #51](https://github.com/TrentBest/TheSingularityWorkshop.FSM_COS/issues/51). Align SURPS to those contracts rather than inventing a competing manifest identity or pretending the current numeric runtime API is already the portable format.

## Related contracts

- [SURPS architecture](architecture.md)
- [MicroBundles and rulebook views](microbundles-and-views.md)
- [Tabletop campaign composition](Theory/tabletop-campaign-composition.md)
- [Experience book-selection schema](../schemas/experience-books.schema.json)
- [FSM_COS Runtime Manifest](https://github.com/TrentBest/TheSingularityWorkshop.FSM_COS/blob/development/docs/RUNTIME_MANIFEST.md)
- [FSM_COS MicroBundle consumption guide](https://github.com/TrentBest/TheSingularityWorkshop.FSM_COS/blob/development/docs/CONSUMING_MICROBUNDLES.md)
- [Portable MicroBundle identity and dependency contract](https://github.com/TrentBest/TheSingularityWorkshop.MicroBundleDomain/blob/development/docs/PORTABLE_DEPENDENCY_CONTRACT.md)


## 6. Workshop authority, repository hosting, and variants

The Singularity Workshop is the sole Experience granted creative authority over the user's canonical MicroBundle repository. This is a deliberate authority boundary, not a restriction that every MicroBundle must be stored in one repository.

The Workshop composes **Experiences and MicroBundles**. It is the privileged creative environment for authoring and changing canonical material in the user's MicroBundle repository. Other repositories may independently host MicroBundles, including MicroBundles that consume or extend canonical Workshop material.

A subscribing repository may:

1. resolve and pull an exact canonical MicroBundle revision from the user's repository;
2. host the pulled content in its own repository under its own storage and development workflow;
3. make local modifications as a creator-owned derivative;
4. validate and publish that derivative as an independently versioned variant;
5. retain provenance to the canonical source revision from which the variant was derived.

This is not a silent edit to the canonical source. A local variant has its own creator, portable identity/revision, repository ownership, and provenance. It must not masquerade as the upstream canonical artifact or overwrite it. The portable identity contract remains ontology + exact version (+ digest where required); repository paths and local storage handles remain implementation details.

The distinction is **creative authority versus repository hosting**:

- The Workshop alone has the granted creative authority over the user's canonical MicroBundle repository.
- A MicroBundle may live in, be maintained by, and be published from another repository.
- A subscribing creator may adapt content locally and publish a variant under that creator's authority.
- The canonical source and the derivative remain distinguishable and independently versioned.

### AiCi and the subscribing repository

Signing in to AiCi is the intended way for a subscribing repository to receive and apply the Workshop's ADP definition. AiCi should map that definition into its native repository-level ADP/group/task model, preserving the subscribing repository's ownership and the distinction between proposed work, authorized writes, evidence, and separately gated publication actions.

This is an evolving integration target. The existing read-only exact-commit evidence lane is not proof that sign-in, ADP application, delegated creative authority, or autonomous variant publication is already end-to-end operational. Authentication identifies the subscriber; it does not by itself grant every write, merge, release, or deployment permission.

The Workshop's canonical authority therefore does not erase repository autonomy. It establishes the trusted source and governance path from which independently hosted, locally modified, provenance-preserving variants can grow.
