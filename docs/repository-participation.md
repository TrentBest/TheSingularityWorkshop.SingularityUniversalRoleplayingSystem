# SURPS Repository Participation Standard

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

This document is the canonical participation contract for repositories contributing to the Singularity Universal Roleplaying System (SURPS). It exists to prevent duplicated catalogues, conflicting identities, overlapping domain implementations, and repeated reinvention of repository conventions.

**Authority:** [SURPS master rulebook map](rulebook-backlog/index.md) and [machine-readable registry](../.surps/rulebook-backlog.json), maintained on the `development` branch of this repository.

## 1. Authority and ownership

- SURPS owns shared roleplaying ontology, CORE rules, rulebook identity, cross-domain semantics, LOD selection, and composition.
- A domain repository owns its specialized knowledge, models, implementation, evidence, and domain sourcebooks.
- An experience repository owns its experience-specific narrative, interface, objectives, progression, and presentation.
- A repository may contribute to a book without owning it. Every book has one accountable owning repository.
- SURPS composes authoritative domain capabilities; it does not copy or absorb their implementation or silently impose a runtime dependency.

## 2. Required repository structure

An enrolled repository declares its participation in `.surps/participation.json`. That manifest identifies the exact repository, domain, active participation status, contribution types, catalogue path, and books owned or contributed to.

Each participating repository maintains:

- `.surps/participation.json` — machine-readable participation declaration.
- `docs/books/index.md` — local human-readable catalogue.
- One Markdown sourcebook per distinct work.
- One `.book.json` descriptor per sourcebook, with stable identity and canonical paths.
- The descriptor's `lodBadge` may use a repository-local SVG path or the canonical shared SURPS LOD badge URL; the badge level must match the book's declared LOD.
- One distinct cover asset per sourcebook; shared SURPS identity and LOD badges remain separate from cover artwork.
- Links to authoritative implementation, validation, worked examples, assumptions, and limitations.

Reuse existing repository build, validation, and documentation conventions. This contract is a shared structure, not a mandate to create redundant frameworks.

## 3. Stable book identity and ownership

- Check the central registry before creating a book or assigning an owner.
- Every book has a globally unique, immutable ID. Related works may share a `familyId`, but distinct works retain distinct book IDs.
- Record the accountable owner separately from contributors and candidate owners.
- A proposed title is not a completed sourcebook. Do not fabricate canonical source paths or links for work that does not yet exist.
- Ownership claims use the [Rulebook Owner Sign-In issue template](../.github/ISSUE_TEMPLATE/rulebook-owner-sign-in.yml). Claims remain pending until reviewed and accepted by SURPS. An agent may not approve its own claim.
- Repository enrollment uses the [SURPS Repository Participation issue template](../.github/ISSUE_TEMPLATE/surps-repository-participation.yml). A repository is not an active participant until its manifest and catalogue are verified.

## 4. LOD, status, and evidence

- LOD expresses the intended level of detail and composition; it is not a maturity score. Assign it deliberately using the [rulebook identity and cover standard](books/index.md).
- Distinguish proposed, draft, and published book states.
- Within content, distinguish implemented, partial, experimental, specified, and planned capabilities.
- Include theory and assumptions, units where relevant, worked examples, authoritative implementation links, validation evidence, and explicit limitations.
- Do not claim that planned models, simulators, or procedures are implemented.
- Keep paper-and-pencil play possible where applicable; deterministic time and state semantics must remain explicit.

## 5. Admission evidence and revalidation

An external repository may be marked `active` in the central registry only after a SURPS reviewer has inspected its `development` branch and recorded:

- The exact manifest URL and catalogue URL, both targeting `development`.
- The Git blob SHA of each inspected file, so the reviewed snapshot is identifiable.
- The verification date and reviewer identity.
- The declared manifest and catalogue paths in the repository record.

The SURPS validator checks that active external records contain this evidence, that URLs exactly match the declared repository paths and branch, and that both blob identifiers have valid Git SHA-1 syntax. This is an auditable admission record, not a live remote fetch: a changed remote file must be fetched and reviewed again, then its blob SHA and verification date refreshed before the registry can continue to represent that snapshot as verified. Invitations, issue comments, repository existence, and candidate book titles are not admission evidence.

## 6. Cross-repository contribution workflow

1. Find the relevant book and owning repository in the [master map](rulebook-backlog/index.md).
2. Contact the owner before creating overlapping material. Extend the authoritative source where appropriate.
3. Work on the repository's `development` branch. Maintain only `master` and `development` as active branches.
4. Keep local manifest, catalogue, descriptor, cover, and sourcebook paths consistent.
5. Submit cross-repository identity, owner, contributor, participation, or canonical-path changes as a reviewed PR to SURPS `development`.
6. Include stable book ID, exact repository, agent identity, canonical URL, source path, descriptor path, scope, exclusions, dependencies, and evidence in ownership claims.
7. Validate through the owning repository's CI. Cross-repository composition must not imply a dependency the owner has not declared.
8. Do not publish NuGet packages or perform a release without explicit release authorization.

## 7. Avoid reinvention

The central registry is the single cross-repository index. Local catalogues are useful navigation surfaces, not competing authorities. Reuse existing IDs, descriptors, LOD semantics, validation, badges, and documentation patterns. Link to the owner; do not fork its domain truth into a consumer repository.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
