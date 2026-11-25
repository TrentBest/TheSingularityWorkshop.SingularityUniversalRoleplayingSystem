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

The studio is intended to become a renderer for the selected experience's SURPS book set, not a hard-coded character form. The initial contracts now define [book contributions](book-contribution-contract.md), [book contribution schema](schemas/book-contribution.schema.json), and [experience book selection schema](schemas/experience-books.schema.json). Books can declare character options, traits, capabilities, adversities, rules, creations, equipment, and resources. The emerging character vocabulary separates **Capabilities** (improvable with character points) from **Adversities** (triggered limitations or liabilities); both are classified as conscious or subconscious. See [Character capabilities, adversities, and action previews](character-capabilities-and-previews.html) for the proposed contract. Experiences select the books and versions they use; SURPS composes the resulting options and provenance for the shared editor.

The editor now has a first data-driven selection slice: `+ Add from SURPS` opens a selector populated by a generated catalog of registered MicroBundle records. The catalog is generated from `.surps/microbundles/registry.json` and each bundle's canonical content document; selected records retain their MicroBundle ID, version, owner repository, and target collection in the draft. This is not yet an experience-filtered resolver: until an experience book-selection manifest is supplied, the picker exposes the registered SURPS catalog rather than claiming to know a campaign's selected book set. Collections with no published records remain empty; the editor does not invent placeholder choices. The new capability/adversity schema and lock-picking preview descriptor are contracts and examples only; they are not yet wired into the local character roster or a running provider host. See the [book contribution example](examples/book-contribution.example.json) and [experience selection example](examples/experience-books.example.json).

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

## Living SVG projection

The five character-sheet themes share the versioned SVG contract `surps.character-sheet@1.0.0`. Each asset declares stable `data-surps-bind` targets for the current Character Studio fields. The Studio embeds the same-origin SVG with an `object` so it can update the SVG document without rewriting the source asset or placing character data into the SVG file. Text is inserted as text nodes (never markup), wrapped to each target's declared line budget, and truncated visually when a field exceeds the available space. The canonical character record remains in the browser roster/export; the SVG is only a live presentation projection. This is a prototype binding contract, not yet the canonical portable character schema.

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
4. Integrate the capability/adversity contract, character-point accounting, and typed editing after their semantics and rating scales are calibrated.
5. Add repository discovery from declared SURPS participation manifests and show only verified, real offerings.
6. Add host handoff only when a host contract exists; keep local-only operation honest and useful in the meantime.
7. Add the preview host as a separate, cancellable experience that consumes an immutable character snapshot and never mutates the saved sheet implicitly.
8. Add automated browser tests for create/edit/save/reload/export/import/delete and malformed input.

## Design standard

The interface follows the GUI repository's successful presentation principles—clear hierarchy, responsive composition, semantic controls, restrained motion, accessible status feedback, and a focused visual identity—without making SURPS depend on the GUI package or a particular rendering adapter. A later GUI-backed implementation can replace the page while preserving the SURPS-owned data and behavior contracts.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
