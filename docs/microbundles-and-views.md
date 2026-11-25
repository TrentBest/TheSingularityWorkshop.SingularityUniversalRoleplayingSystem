# SURPS MicroBundles and Rulebook Views

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

## The ownership model

A MicroBundle is the independently identified and versioned unit of selectable content. It has one accountable owner repository, a stable ID, a version, maturity, domain, dependencies, and provenance. Its records keep globally namespaced IDs. A MicroBundle can be selected by many books and experiences without copying or redefining those records.

A rulebook is a view, not an owner of the records it presents. Its view descriptor declares:
- book identity and version;
- audience (player, game master, Workshop, editor, reference, print, or all);
- scope and LOD;
- ordered selections of MicroBundles and record IDs;
- presentation metadata that may change without changing authoritative record identity.

The same MicroBundle can appear in a player handbook, a referee's expanded guide, a Workshop inspector, a digital reference, and a print edition. Each projection is a view over the same record identities. Reordering, hiding, grouping, or explaining content in a view must never mutate its source records.

## MicroBundle-owned book assets

A MicroBundle also owns the reusable assets that explain its records: authored prose, captions, SVGs, diagrams, and image references. It may additionally declare action previews: provider compositions that let a player explore an action through character visualization, a contextual environment, gestures, and resolution without moving ownership of those behaviors into the rulebook. Its asset manifest assigns each resource a stable ID, relative path, accessible description, usage, and optional audience/locale metadata. Views may arrange or select those assets for different books, but they do not copy the canonical source or redefine its meaning. The CORE Spying pilot now includes an SVG approach-spectrum diagram and shared introductory copy in its MicroBundle asset directory. The [asset manifest schema](../schemas/microbundle-assets.schema.json) defines this contract.

## Contracts

- [MicroBundle descriptor schema](../schemas/microbundle.schema.json) defines ownership, content, and optional asset/preview metadata.
- [Character capabilities and adversities](character-capabilities-and-previews.html) defines the conscious/subconscious axis, character-point direction, and action-preview ownership boundaries.
- [Action preview manifest schema](../schemas/action-preview-manifest.schema.json) lets a MicroBundle offer multiple previews; [action preview schema](../schemas/action-preview.schema.json) defines each staged provider composition.
- [CORE Spying preview manifest](../.surps/previews/core-spying.previews.json) registers its [lock-picking preview](../.surps/previews/lock-picking.preview.json), which remains proposed rather than executable.
- [CORE Spying asset manifest](../.surps/microbundles/assets/core-spying.assets.json) registers its SVG and reusable book copy.
- [Repository-local MicroBundle registry schema](../schemas/microbundle-registry.schema.json) and [registry](../.surps/microbundles/registry.json) enumerate independently selectable bundles.
- [Rulebook view schema](../schemas/rulebook-view.schema.json) defines a curated selection.
- [Rulebook view registry schema](../schemas/rulebook-view-registry.schema.json) and [view registry](../.surps/views/registry.json) enumerate independently generated projections.
- [CORE Spying player view](../.surps/views/core-spying-player.view.json) and [game-master view](../.surps/views/core-spying-game-master.view.json) select the same canonical records for different audiences.
- [CORE Spying MicroBundle](../.surps/microbundles/core-spying.microbundle.json) is the first SURPS-owned bundle descriptor; its canonical records live in [book-independent MicroBundle content](../.surps/microbundles/content/core-spying.content.json) validated by the [MicroBundle content schema](../schemas/microbundle-content.schema.json).
- [CORE Spying player view](../.surps/views/core-spying-player.view.json) selects six approaches and six procedures.
- [Resolver and projection validator](../scripts/validate_surps_ontology_views.py) validates schema, identity alignment, and selected-record resolution, then generates a deterministic projection.
- The CI workflow uploads that generated projection as `surps-core-spying-player-view`; it is a build artifact, not a claim that a dynamic Character Studio, action-preview host, or runtime rule engine exists.

## Probability-first resolution direction

The proposed common resolution language is probability from 0 to 100, with percentile dice as one physical interface. Capability remains distinct from final success chance: task difficulty and circumstances transform capability into an outcome probability. This is still a design proposal, not the adopted core mechanic; CORE Spying's current 2d6 playtest procedure remains unchanged pending an exact probability-distribution comparison. See [Probability-first resolution](probability-resolution.html) for the calibration plan.

## First vertical slice: CORE Spying

The first bundle exposes six approach capabilities (Observe, Deceive, Infiltrate, Analyze, Influence, Operate) and six structured procedures (approach allocation, uncertain action resolution, outcome bands, preparation/assets, scene clocks, and information/evidence states).

The player and game-master views select records by stable ID. They intentionally reuse the same canonical record identities; audience-specific ordering and descriptions belong to the view, not duplicate rules. The resolver:
1. loads and validates the MicroBundle descriptor and the view definition;
2. loads the referenced structured payload and checks its schema;
3. verifies bundle ownership/version against the current transitional payload;
4. verifies that the book descriptor and participation manifest identify the same view and MicroBundle;
5. resolves every selected record ID from the declared record collections;
6. rejects missing bundles, missing records, duplicate selections, and duplicate IDs inside the bundle;
7. emits a deterministic JSON projection with source bundle/version/owner provenance attached.

This is real local selection and projection, not just a diagram or a design document.

## Transitional boundary

The CORE Spying records have now been physically moved into `.surps/microbundles/content/core-spying.content.json`. The canonical content envelope contains only the MicroBundle's record collections; it has no book identity, audience, or publication metadata. The old `.surps/contributions/core-spying.json` remains as a compatibility source during migration, but the resolver no longer reads it for the canonical bundle. Views own book/audience selection, while the MicroBundle owns the records.

The next migration is to move the remaining legacy contribution consumers to the canonical MicroBundle content contract and then retire the compatibility payload after all references are confirmed safe. The resolver now discovers every entry in a view registry and emits one deterministic projection per entry. The checked-in pilot currently demonstrates two audience views over one real bundle. It supports multiple bundles from one repository-local registry, but the checked-in MicroBundle registry has only one real bundle. Cross-repository content-record federation, federated global record-ID collision detection, semantic dependency/version-range resolution, typed reference resolution across bundles, conflict policy, and runtime execution remain separate gates. A separate pinned external-provider discovery path now reads actual Physics-owned provider manifests without copying their domain records into SURPS.

## First cross-repository provider discovery

SURPS now pins the Physics repository at commit `0e707e1add24a4009ec5380372f2c8f670e1a7a2` and validates two owner-maintained manifests:

- Physics bundle 5202 — Normal Impulse Response, provider `physics.contact.normal-impulse.v1`.
- Physics bundle 5203 — Prescribed Kinematic Motion, provider `physics.kinematics.prescribed-motion.v1`.

The [external provider registry](../.surps/external-providers/registry.json) records the exact source commit, manifest paths, bundle identities, and provider IDs. The validator checks the owner-repository manifests against those pinned identities and emits a provenance-preserving discovery catalog. CI uploads it as `surps-external-provider-catalog`.

This is a real cross-repository discovery integration: the source manifests remain owned by Physics, and SURPS consumes them at a pinned commit. It is deliberately **not** yet cross-repository rulebook record composition, a runtime provider loader, or a claim that the provider implementation is automatically available to an experience. Provider metadata and authored ontology records remain distinct contracts.

## Ownership and maturity rules

- SURPS owns shared roleplaying ontology vocabulary, identity conventions, view semantics, selection rules, and cross-domain composition.
- Domain repositories own their domain-specific ontology records and executable behavior.
- A MicroBundle descriptor identifies its owner; a book descriptor identifies a publication/view.
- A view selects records; it does not copy them into a second authority.
- LOD describes declared detail, not automatic precedence.
- A record marked `specified` is not automatically `implemented`; a declared capability is not proof of an evaluator.
- The first CORE Spying records remain playtest material. The projection preserves that status and source provenance.
- The current resolver can compose multiple entries from one local registry into each view. The checked-in registries currently contain one real bundle and two audience views; federated cross-repository discovery is not implemented.

## Build and test

Run locally:

```bash
python -m pip install "jsonschema>=4.23,<5"
python3 scripts/validate_surps_ontology_views.py
# With the pinned Physics checkout at _dependencies/Physics:
python3 scripts/validate_surps_external_providers.py --source-root _dependencies/Physics
python3 -m unittest discover -s tests/python -v
```

The build workflow runs the resolver, Python unit tests, the .NET build/tests, and uploads the generated view JSON as a downloadable Actions artifact.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
