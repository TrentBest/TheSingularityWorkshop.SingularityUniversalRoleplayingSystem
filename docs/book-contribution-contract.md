# SURPS Book Contribution and Composition Contract

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

## Purpose

A registered book must be more than a title, cover, and link. It must be able to contribute structured, inspectable game content to the SURPS system. The Character Studio and every compatible satellite experience consume the same SURPS-owned tooling and contracts.

A book may contribute:

- Character creation choices: ancestry, heritage, culture, background, occupation, archetype, lineage, form, and origin.
- Character traits: advantages, disadvantages, abilities, disabilities, features, conditions, and mutations.
- Capabilities and training options.
- Rules, procedures, constraints, and rule-resolution metadata.
- Creations: species, creatures, person/NPC templates, items, weapons, armor, vehicles, structures, locations, factions, organizations, hazards, and environments.
- Equipment and resources.
- References to domain-owned evaluators/providers that supply actual execution.

Ontology records are authoritative; their owning domain or shared ontology layer defines their meaning. A contribution document is a machine-readable declaration of records exposed by a provider, while a rulebook/book is a curated view that selects and presents those records. SURPS owns shared ontology semantics, contribution vocabulary, validation conventions, cross-domain composition, compatibility, and view tooling. The current book-scoped contribution file is an initial pilot format, not a claim that books own all underlying ontology data.

## The four distinct steps

1. **Contribute** — an owning domain publishes authoritative ontology records and, where useful, a machine-readable contribution document. Human-readable source material explains those records without becoming a competing authority.
2. **Register** — the contribution validator checks the legacy payload schema, aligns its book ID/version with the descriptor and participation entry, and rejects document-local duplicate record IDs. The new MicroBundle validator checks a bundle descriptor, its owner/version, the payload link, and local record identity.
3. **Select** — a rulebook view selects MicroBundles and stable record IDs for an audience, scope, and LOD. The first CORE Spying player view is now resolved by executable tooling; missing bundles, missing records, duplicate selections, and duplicate local record IDs fail closed.
4. **Project** — the resolver emits a deterministic JSON projection containing the selected records and source MicroBundle/version/owner provenance. CI uploads the generated CORE Spying player projection as a build artifact. This is a local one-bundle vertical slice, not yet a federated multi-repository registry, dynamic Character Studio, or runtime rule engine.

A book's `.book.json` descriptor identifies its curated view and publication identity (ID, title, LOD, version, cover, and related metadata); it is not an ontology database. The first implementation adds a `viewPath` to the CORE Spying descriptor and participation entry. The separate MicroBundle descriptor declares the selectable bundle identity, owner repository, version, domain, source payload, and record collections. CORE Spying still carries legacy `contributionPath` metadata during migration; that payload remains explicitly book-scoped and is not yet the final domain-owned ontology storage shape. Other books may omit both contribution and view paths until they have structured data and a view. See the [book descriptor example](examples/book-descriptor.example.json) and [MicroBundles and Rulebook Views](microbundles-and-views.md).

## Canonical contribution document

The legacy payload schema is [book-contribution.schema.json](schemas/book-contribution.schema.json). The independently selectable bundle and publication view contracts are [microbundle.schema.json](schemas/microbundle.schema.json) and [rulebook-view.schema.json](schemas/rulebook-view.schema.json). These remain development contracts and are not frozen public APIs.

A contribution document contains:

- `book`: stable book ID, semantic version, maturity/status, source, and owner repository.
- `contributions.characterOptions`: selectable character-building choices.
- `contributions.traits`: selectable or granted traits, including advantages, disadvantages, abilities, disabilities, features, and conditions.
- `contributions.capabilities`: capabilities a character or entity may possess or invoke.
- `contributions.rules`: inspectable rules, applicability, inputs/outputs, dependencies, status, and evaluator references.
- `contributions.creations`: authored entity/item/world templates that the book makes available.
- `contributions.equipment/resources`: selectable or granted loadout content.
- `compatibility`: required/conflicting books and supported character-contract version.
- `provenance`: repository and source commit information.

Stable IDs are globally namespaced by the owning ontology/domain, for example `surps.core.character.identity` or `physics.domain.weather.wind-exposure`. A view may select the same ID into multiple books without creating another identity. Display names are not identities.

## Character options are not all the same thing

A selectable option may grant one or more traits, capabilities, equipment, or resources. These grants are references to canonical records, not copied definitions. A character records the selected option and resolved grants, with provenance back to the source book and version.

A trait is a descriptive or mechanical character feature. Its kind indicates whether it is an advantage, disadvantage, ability, disability, feature, condition, or another declared category. A disability is not automatically a penalty or a single numeric modifier: the book must describe the actual functional effects, contexts, accommodations, constraints, and any relevant capabilities. SURPS preserves the authored semantics; a domain evaluator determines consequences when one is required.

A capability declaration does not mean SURPS has implemented its evaluator. The contribution may reference a provider owned by Gestures, Physics, Economy, or another domain. If no compatible provider is present, the UI can explain that the capability is described but not executable in this experience.

## Rules are selected, inspectable, and attributable

Rules declare scope, applicability, typed inputs/outputs, assumptions, constraints, required capabilities, status, and an optional evaluator/provider reference. They do not embed arbitrary executable code in JSON.

Resolution must preserve provenance and expose:
- the selected book and version;
- the rule and rule status;
- why it applies;
- required and available inputs, including units where relevant;
- required capabilities and resolved providers;
- conflicts, precedence, and unresolved requirements;
- the provider and evidence behind any evaluated result.

Conflicting contributions are reported, never silently overwritten. A higher LOD may add detail but must not silently erase CORE semantics. Experience authors select the book set and any explicit precedence policy.

## Experience book selection

A satellite repository declares an experience profile that references registered book IDs and version ranges. It may select SURPS CORE plus domain books and setting/experience books. The same experience profile feeds the character editor and runtime rule resolver.

The experience does not fork the Character Studio. It opens the shared SURPS editor with a public experience context. SURPS loads the experience's declared book set and supplies the matching creation options, traits, capabilities, and rules. The satellite may add its own experience-specific content through the same contribution contract and ownership rules.

An experience may offer several profiles (for example, a basic campaign and an advanced campaign) without duplicating character schemas. Switching profiles must show which selections are unavailable or incompatible; it must not silently delete character data.

## Character persistence and provenance

The canonical character record stores stable identity, user choices, and resolved references/grants with book IDs and versions. It must preserve unknown optional extensions and reject unsupported required semantics as defined by the character serialization contract.

Character definition remains separate from:
- campaign/quest progress owned by the satellite experience;
- transient runtime/session state owned by the host;
- rule evaluation results/events owned by the running experience.

When a book version changes, SURPS can report whether the character remains compatible, needs migration, or has unresolved references. It must not rewrite a character silently.

## Satellite integration promise

The intended integration is deliberately small:

1. Add a SURPS tab/link that opens the central Character Studio with a public experience identifier.
2. Publish an experience book-selection manifest.
3. Publish any satellite-owned contribution documents and reference them from its book descriptors.
4. Use the SURPS validator and shared editor/resolver contract; do not implement a local character schema or duplicate character editor.

The portal can then render the same character creation flow anywhere, with the extra content from that experience's selected books. A City experience might offer City backgrounds, residents, and civic rules; a dungeon experience might offer its ancestries, hazards, equipment, and dungeon rules; a laboratory experience might offer its own roles, apparatus, and procedures.

## Maturity and implementation gates

CI now validates the legacy payload schema plus the MicroBundle and view schemas. It resolves the CORE Spying player view against the bundle's declared record collections, rejects unresolved local record references and duplicate selections, and emits a deterministic projection with source provenance. Unit tests exercise successful resolution and fail-closed cases. The six approach capabilities and six written procedures remain playtest declarations; they are not an executable evaluator or universal character attributes.

The remaining gates are:

1. Move the canonical records out of the transitional book-scoped payload into an independently owned MicroBundle content document.
2. Extend dependency checks from local required-bundle presence to semantic version-range resolution, optional dependency policy, and cycle detection.
3. Add a federated registry/admission process and global identity collision detection across participating repositories.
4. Resolve typed references between records and bundles, including missing providers and compatibility constraints.
5. Define explicit conflict and precedence policies without inferring precedence from LOD or load order.
6. Upgrade the Character Studio and Workshop adapters to consume projections dynamically.
7. Integrate a second domain-owned MicroBundle (for example, Physics or FSM_Dungeon) and prove cross-repository composition.
8. Keep tabletop procedures independently playable and calibrate executable digital behavior only where a real evaluator exists.

No NuGet/API release is implied by this documentation work.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
