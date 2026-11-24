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
2. **Register** — the current validator checks the contribution schema, aligns the contribution's book ID/version with its descriptor and participation entry, and rejects duplicate record IDs within that contribution. Full cross-repository reference resolution and registry indexing are not implemented yet.
3. **Select** — a book/view definition declares which contributions and ontology records it presents for an audience, scope, LOD, and purpose. The current experience manifest is a selection contract; its complete resolver is not implemented yet.
4. **Project** — future SURPS tooling will compose selected records into player, Workshop, tabletop, digital, and print projections. The current Character Studio does not yet dynamically compose all these views.

A book's `.book.json` descriptor identifies its curated view and publication identity (ID, title, LOD, version, cover, and related metadata); it is not an ontology database. The current pilot allows a descriptor to declare a repository-relative `contributionPath` and `contributionSchema`, mirrored by the participation manifest. This is a transitional convenience for the CORE Spying pilot. As ontology ownership and cross-repository composition mature, descriptors should select domain-owned contributions rather than imply that the book owns their truth. A book without a machine-readable payload may omit `contributionPath`; it is then bibliographically registered but has no structured contribution attached yet. See the [book descriptor example](examples/book-descriptor.example.json).

## Canonical contribution document

The initial JSON Schema is [book-contribution.schema.json](schemas/book-contribution.schema.json). It is a development contract and will be validated against real sourcebooks before being treated as a frozen public API.

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

The schema and examples in this branch are an initial contract, not a claim that all registration, dynamic UI composition, or runtime rule execution already exists. CI checks both schemas and their examples, then validates every registered contribution document against the book-contribution schema. It also verifies that the contribution's book ID/version agree with its descriptor and participation entry, and that record IDs are unique across all record collections within each contribution document. This is document-local integrity, not global ontology identity resolution: cross-repository duplicate detection, reference resolution, and ontology query/projection remain future work. CORE Spying is the first real sourcebook pilot: its six playtest approaches and its written uncertainty, outcome, preparation, clock, and information/evidence procedures are represented as structured declarations. The declarations preserve the sourcebook's playtest status; they do not claim an executable evaluator or universal character attributes.

The remaining gates are:

1. Validate more real books and tighten the schema from actual authoring experience.
2. Define the experience profile resolver, version ranges, dependency/conflict checks, and precedence behavior.
3. Upgrade the Character Studio to render options and rulebook-provided fields from the selected book set.
4. Extend integrity tests to cross-repository identity collisions, unresolved references, dependency conflicts, missing providers, compatibility, and provenance.
5. Integrate one satellite repository only after the central contract is proven.

No NuGet/API release is implied by this documentation work.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
