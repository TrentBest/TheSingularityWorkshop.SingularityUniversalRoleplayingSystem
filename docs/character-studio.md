# SURPS Character Studio

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

The [Character Studio](character-studio.html) is the first interactive visitor-facing character creator for SURPS. It is deliberately a small, browser-native application: no framework dependency, account requirement, or remote service is implied.

## What is implemented

- Create a named character with identity, role, pronouns, origin, concept, and appearance/form.
- Record attributes, capabilities, training, current condition, goals, equipment, relationships, and history.
- Keep multiple character records in a local browser roster and switch between them.
- Edit and save a selected character.
- Export the selected character as readable JSON.
- Import a previously exported JSON character as a new local copy.
- Review a live character summary while editing.
- Delete a local record with an explicit confirmation.

## Book-driven character creation

The studio is intended to become a renderer for the selected experience's SURPS book set, not a hard-coded character form. The initial contracts now define [book contributions](book-contribution-contract.md), [book contribution schema](../schemas/book-contribution.schema.json), and [experience book selection schema](../schemas/experience-books.schema.json). Books can declare character options, traits (including advantages, disadvantages, abilities, and disabilities), capabilities, rules, creations, equipment, and resources. Experiences select the books and versions they use; SURPS composes the resulting options and provenance for the shared editor.

This dynamic book-driven composition is **not implemented in the current editor yet**. The current free-form fields remain a prototype workspace until the canonical character contract and contribution resolver are validated. See the [book contribution example](examples/book-contribution.example.json) and [experience selection example](examples/experience-books.example.json).

## Ownership and data boundaries

| Concern | Owner |
|---|---|
| Shared character ontology, stable identity, portable wire format, compatibility | SURPS |
| Character editor presentation and interaction | SURPS Character Studio, using browser-native HTML/CSS/JavaScript |
| Campaign, quest, encounter, and experience progress | The participating experience repository |
| Account identity, authorization, authoritative sessions, cloud persistence | A host service when implemented |
| Specialized attribute evaluators and physical consequences | Their owning domain repositories |

The portable character definition is not a campaign save file. Experience-owned progress and transient host session state must remain separate from the character record.

## Prototype storage and portability

The current page stores its roster in `localStorage` under a SURPS-specific key on the shared `trentbest.github.io` origin used by the GitHub Pages site. Other project Pages sites under that same origin can access the same browser storage, so they must reuse the central portal rather than create competing character stores. This means:

- Data remains in the browser profile and origin where it was created.
- Clearing site data or using another browser/device may make the local roster unavailable.
- Exported JSON is the user's portable backup and import path.
- This implementation does not provide accounts, cloud synchronization, cross-device synchronization, or guaranteed third-party iframe storage.

Visitors should export important characters. Participating repositories should link to the central SURPS page rather than embedding another copy of the editor.

## Draft JSON envelope

The first prototype exports a clearly marked draft envelope:

- `format`: `surps.character-draft`
- `formatVersion`: `0.1.0`
- `status`: `prototype-not-canonical`
- `character`: the character record, including a stable record ID and the current editable fields
- `exportedAt`: export timestamp

This is an implementation fixture, not the canonical SURPS wire contract. The contract is being defined in [issue #7](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/issues/7). The editor must migrate to that contract when its identity, required semantics, extension behavior, and compatibility rules are accepted. It must not silently promote prototype field names into permanent CORE semantics.

## Next implementation gates

1. Finalize the canonical identity and serialization contract in issue #7.
2. Add schema-backed validation, migration, and round-trip fixtures.
3. Replace the draft envelope with the canonical versioned format.
4. Add typed attribute/capability editing only after the relevant semantics and rating scales are defined; do not invent a universal scale.
5. Add repository discovery from declared SURPS participation manifests and show only verified, real offerings.
6. Add host handoff only when a host contract exists; keep local-only operation honest and useful in the meantime.
7. Add automated browser tests for create/edit/save/reload/export/import/delete and malformed input.

## Design standard

The interface follows the GUI repository's successful presentation principles—clear hierarchy, responsive composition, semantic controls, restrained motion, accessible status feedback, and a focused visual identity—without making SURPS depend on the GUI package or a particular rendering adapter. A later GUI-backed implementation can replace the page while preserving the SURPS-owned data and behavior contracts.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
