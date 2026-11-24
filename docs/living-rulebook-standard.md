# SURPS Living Rulebook and Experience Standard

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

## Purpose

A SURPS book is a living instruction manual for understanding, authoring, and experiencing a domain. It should teach the big picture first, then reveal the smaller parts and relationships. It should be useful to players, game masters, world builders, authors, developers, and agents.

The book is not a linear wall of prose. It is a navigable experience with concise paths, deep reference material, real examples, interactive demonstrations, and abundant living illustrations.

This standard applies to SURPS itself and every repository registered as a SURPS participant or sourcebook provider.

## A book is a view into ontology

The ontology is the structured source of truth. A book is a curated view over selected ontology records and microbundles—not a separate database, an ownership boundary, or the place where domain truth originates.

- A microbundle is an independently identified, composable contribution of ontology, records, relationships, behavior, procedures, provider capabilities, dependencies, and/or explanatory assets.
- A book selects and organizes microbundles for an audience, scope, LOD, and purpose. One book can aggregate many bundles; one bundle can appear in many books.
- The same source data should support multiple projections: player, Game Master/Workshop, tabletop, digital, reference, diagrammatic, and print.
- Generated prose, diagrams, tables, and navigation should retain links to the ontology items and microbundle provenance from which they were derived.
- Editing a book's presentation must not silently mutate authoritative domain data. Changing domain truth belongs in its owning microbundle/repository and should flow into every relevant view.
- A publication descriptor describes the book view and its presentation contract. It must not grow into a parallel ontology store.

The book is therefore a navigable lens over the living data. Its chapter structure is an editorial arrangement of ontology concepts and relationships, not a competing taxonomy.


## Originality and design distance

SURPS must be independently designed. Do not copy GURPS text, tables, distinctive terminology, procedures, character construction formulas, resolution mechanics, damage structures, or book organization. Familiar broad ideas such as characters, skills, conflict, travel, and consequences are not proprietary; the implementation and expression must be authored from SURPS's own behavior model and play goals.

Do not assume a universal attribute/skill/point-buy formula. A character's properties and capabilities should arise from the shared ontology and the selected domain books. The current CORE Spying 2d6 approach procedure is a scoped playtest adapter, not the universal SURPS resolution mechanic. It must not become the default merely by repetition.

Harm and consequences should communicate what happens in the world—negligible, limited, substantial, severe, or otherwise domain-authored effects—rather than forcing every domain into one generic damage number. Numeric quantities remain available when the owning domain needs them, with units, assumptions, and provenance.

Track the [SURPS originality audit](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/issues/11). The purpose is not to avoid every familiar game concept; it is to ensure SURPS mechanics are independently derived, testable, and expressive of its own model.

## One behavior model, multiple adapters

Every domain must preserve one underlying semantic/behavior model and expose the views it supports:

1. **Tabletop adapter** — a human-manageable procedure derived during authoring/workshop calibration from the underlying behavior. Dice values, target numbers, tables, and qualitative outcome bands are outputs of the model, not its source of truth.
2. **Digital adapter** — detailed evaluation against live state, using domain-owned providers and compiled/cached behavior artifacts.
3. **Player view** — concise, actionable, fiction-facing explanation.
4. **Game Master / Workshop view** — deep data, causal detail, scenario manipulation, hidden state, diagnostics, and authoring controls.

Not every repository must implement every adapter immediately. It must state what exists, what is illustrative, and what is planned. Never label a paper projection as a digital simulation or a conceptual digital model as implemented execution.

See [Behavior Model and Adapters](behavior-and-adapters.md) for the authoritative system contract. Cross-repository adoption is tracked in the [SURPS Living Standard Adoption Tracker](participating-repository-adoption.md).

## Required book reading order

Every substantial book or domain guide should follow this progression. A book may use chapters, tabs, accordions, diagrams, and deep links rather than one long page.

1. **Big picture:** What is this domain? Why does it exist? What does it affect? Show the whole system.
2. **How to use this book:** Who should read which path; prerequisites; what is playable now; what is reference only.
3. **Player overview:** Short, plain-language explanation of what a character can perceive, choose, and do.
4. **Game Master / Workshop overview:** What can be authored, revealed, hidden, changed, inspected, or simulated.
5. **Living domain map:** The main entities, processes, environments, and causal relationships.
6. **Parts and pieces:** Break down the major concepts and explain how each contributes to the whole.
7. **Rules in action:** Every important mechanic gets at least one worked scenario showing inputs, process, outcome, and consequence.
8. **Adapter views:** Explain tabletop and digital presentations, including what is simplified and what remains detailed.
9. **Authoring and reference:** Full data, edge cases, tables, compatibility, provenance, glossary, and implementation evidence.

## Living pictures are required

Visuals are not decoration. They are a primary teaching surface.

- Every major concept/section should have at least one meaningful living picture, diagram, animation, or interactive model.
- Every mechanic should be shown in action, not merely described. Use a worked example, interactive state transition, simulation, or generated artifact.
- Prefer source-driven SVG/HTML examples and repeatable outputs over manually maintained screenshots.
- Show the whole concept first, then zoom into components, states, forces, relationships, timelines, and edge cases.
- Use the GUI repository's proven principles: strong hierarchy, semantic models, responsive layouts, clear interaction, restrained motion, and explicit adapter boundaries. Do not create a hard dependency on the GUI package just to publish a static Pages guide.
- Label each illustration as implemented, generated, authored concept art, or illustrative prototype. Never imply a picture proves an engine capability it does not exercise.
- Include accessible text alternatives, readable contrast, keyboard-operable controls, and reduced-motion behavior. Motion must clarify a relationship, not distract.

**Quality bar:** a reader should be able to look at a concept and see what it means before reading a long explanation. A mechanic without an example is unfinished teaching.

## Two levels of detail, not two disconnected books

The player path is brief and useful during play. The Game Master path is deep and operational: it should expose enough information to change a scene, adjust an encounter, reveal a consequence, or investigate a surprising result without requiring the GM to memorize every rule.

Use progressive disclosure. Keep the primary reading surface calm; make deeper data available through linked details, diagrams, inspectors, and workshop panels. Do not hide essential player-facing rules behind editor-only controls.

## What a worked mechanic must show

For each important mechanic, include:

- the situation before the action;
- actor, intent, target, context, and relevant constraints;
- which book/rule/provider applies and why;
- what the player declares;
- what the GM decides or controls;
- the tabletop procedure and its derived status;
- the digital evaluation path and implementation status;
- at least two meaningful outcomes where possible (e.g. miss and hit; ideally exceptional/critical too);
- what changes in the world, including effects beyond the immediate target;
- how time, state, and persistent consequences are recorded.

## Workshop-time derivation and runtime caching

If tabletop dice values or procedures are intended to represent a complex behavior, derive them during authoring/workshop preparation:

1. Define the behavior and its valid operating envelope.
2. Select representative and boundary scenarios.
3. Run domain-owned simulations or evaluators.
4. Analyze the outcome distributions and desired human play cadence.
5. Generate the tabletop procedure and qualitative bands.
6. Validate the paper adapter against held-out scenarios and edge cases.
7. Version the derived artifact with full provenance.

The digital adapter compiles reusable behavior at build/authoring time. Runtime loads cached compiled artifacts and binds current mutable state. Cache immutable models and reusable response data; do not cache a final outcome across changes to actor, target, environment, equipment, or time.

## Repository adoption requirements

A participating repository must:

- link this standard from its SURPS participation documentation or book catalogue;
- identify the domain's authoritative behavior owner;
- identify its tabletop and digital adapter status separately;
- provide a player overview and a GM/workshop path;
- include living visual explanations for major concepts and mechanics;
- include at least one interactive or playable Pages experience where the repository has a published Pages site;
- use actual domain data and providers where implemented; mark prototypes and authored concept illustrations honestly;
- preserve rule and data provenance;
- expose its content through a SURPS experience/book selection manifest where appropriate;
- keep the central SURPS character identity/editor contract instead of forking character creation;
- record gaps and conformance work in a repository issue.

SURPS owns the shared standard and composition contracts. Each domain repository owns its domain facts, models, providers, worked examples, and playable demonstration.

## Suggested visual rhythm

A useful chapter often follows:

**Big picture illustration → short explanation → interactive or worked example → zoomed component illustrations → player procedure → GM deep dive → tabletop/digital comparison → reference.**

Avoid making every picture a full-width hero. Use diagrams, small animated figures, timelines, maps, state panels, cutaways, comparison views, and interactive controls where each best communicates the idea.

## Conformance is evidence-based

Use these labels consistently:

- **Implemented:** present in source and exercised by tests or a playable page.
- **Generated:** produced by a repeatable build/workflow from identified source data.
- **Illustrative:** an authored teaching model that is not a validated domain evaluator.
- **Specified:** a documented contract without a complete implementation.
- **Planned:** not yet implemented.

A repository is not conformant because it has a pretty landing page. It is conformant when a visitor can understand the domain, inspect real evidence, and try a meaningful working slice.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
