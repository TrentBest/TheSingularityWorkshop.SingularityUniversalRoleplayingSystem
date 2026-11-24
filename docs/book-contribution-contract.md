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

The book remains the authored source of truth. SURPS owns the common contribution vocabulary, validation, registration, composition, compatibility, and presentation tooling.

## The four distinct steps

1. **Author** — the book owner writes its human-readable source and a machine-readable contribution document.
2. **Register** — SURPS validates the book identity, version, contribution document, references, provenance, and compatibility, then indexes its declarations.
3. **Select** — an experience declares which registered books and versions it uses. Registration makes content discoverable; it does not automatically activate every rule in every world.
4. **Compose** — SURPS combines selected contributions into the experience's character options, creation catalogue, rule set, and capability index. The shared Character Studio renders the resulting options.

A book's existing `.book.json` descriptor remains its bibliographic identity (ID, title, LOD, version, cover, and related metadata). It is not itself the full game-content payload. A descriptor or repository participation record should point to a versioned contribution document. This separation keeps book registration lightweight while allowing the content contract to evolve independently.

## Canonical contribution document

The initial JSON Schema is [book-contribution.schema.json](../schemas/book-contribution.schema.json). It is a development contract and will be validated against real sourcebooks before being treated as a frozen public API.

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

Stable IDs are globally namespaced by book or owning domain, for example `surps.core.character.identity` or `physics.domain.weather.wind-exposure`. Display names are not identities.

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

The schema and examples in this branch are an initial contract, not a claim that all registration, dynamic UI composition, or runtime rule execution already exists. The next gates are:

1. Validate the schema with JSON Schema tooling and representative book payloads.
2. Add contribution documents to a small pilot set of real books.
3. Define the experience profile schema and resolver precedence/compatibility behavior.
4. Upgrade the Character Studio to render options from the selected book set.
5. Add automated tests for registration, duplicate IDs, dependency conflicts, missing providers, compatibility, and provenance.
6. Integrate one satellite repository only after the central contract is proven.

No NuGet/API release is implied by this documentation work.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
