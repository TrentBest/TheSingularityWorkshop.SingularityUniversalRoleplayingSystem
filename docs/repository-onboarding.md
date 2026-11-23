# SURPS Repository Onboarding and Coordination

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

This is the operational intake board for repositories that provide or consume SURPS rulebooks. The [master registry](../.surps/rulebook-backlog.json) remains authoritative for repository status, stable book IDs, ownership, and book paths. This page records the coordination entry point and the next verifiable admission action.

## Admission gate

A repository is **Active** only after SURPS verifies all of the following on its `development` branch:

1. `.surps/participation.json` declares the exact repository, domain responsibility, status, catalogue path, and owned/contributed book IDs.
2. `docs/books/index.md` exists and links to the repository's authoritative books.
3. Each declared book has a unique global ID, one accountable owner, a descriptor, and canonical source/cover paths.
4. The local structure and ownership agree with the SURPS registry.
5. A SURPS registry change is reviewed and accepted.

A comment or invitation is **not** enrollment. A proposed owner is not an accepted owner. Repositories below remain in their current registry status until the admission evidence is verified.

## Canonical shared references

- [Repository Participation Standard](repository-participation.md)
- [Master Rulebook Map](rulebook-backlog/index.md)
- [Machine-readable registry](../.surps/rulebook-backlog.json)
- [Repository enrollment template](../.github/ISSUE_TEMPLATE/surps-repository-participation.yml)
- [Rulebook owner sign-in template](../.github/ISSUE_TEMPLATE/rulebook-owner-sign-in.yml)

## Active participants

| Repository | Domain authority | Coordination |
|---|---|---|
| [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Shared roleplaying ontology, CORE rules, identity, LOD and composition | Registry authority |
| [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Physical laws, materials, models, solvers, simulation and Physics sourcebooks | [Existing sourcebook coordination thread](https://github.com/TrentBest/TheSingularityWorkshop.Physics/issues/61) |

## Invited or referenced repositories

| Repository | Current registry status | Domain boundary | Next admission action | Coordination |
|---|---|---|---|---|
| [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Integrated / not enrolled | Dungeon topology, underground environments, and original fantasy sourcebooks | Six structured draft books are registered with pending claims; complete independent ownership/domain review and verify manifest/catalogue evidence | [SURPS integration thread](https://github.com/TrentBest/FSM_Dungeon/issues/4) |
| [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Integrated / not enrolled | City systems, civic institutions, infrastructure, residents, and urban planning | Ten structured draft books are registered with pending claims; complete independent ownership/domain review and verify manifest/catalogue evidence | [SURPS sourcebook thread](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/issues/1) |
| [SingularityLaboratories](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories) | Integrated / not enrolled | Scientific inquiry, laboratory facilities, experiments, apparatus, staffing, and research workflows | Three structured draft books are registered with pending claims; review descriptive knowledge versus executable capabilities and verify manifest/catalogue evidence | [SURPS sourcebook thread](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories/issues/3) |
| [Gauntlet](https://github.com/TrentBest/TheSingularityWorkshop.Gauntlet) | Planned | Enrollment, selected-book composition, conformance and evidence | Declare its integration contract and manifest consumption; do not claim domain book ownership | [SURPS integration thread](https://github.com/TrentBest/TheSingularityWorkshop.Gauntlet/issues/6) |
| [Economy](https://github.com/TrentBest/TheSingularityWorkshop.Economy) | Integrated / not enrolled | Economic ontology, currency, exchange, production, project finance, logistics, and organized play | Six structured books are registered (four draft, two proposed); complete independent ownership/domain review and verify manifest/catalogue evidence | [SURPS sourcebook thread](https://github.com/TrentBest/TheSingularityWorkshop.Economy/issues/32) |
| [Gestures](https://github.com/TrentBest/TheSingularityWorkshop.Gestures) | Candidate, not enrolled | Posture, movement, locomotion and embodied interaction | Declare movement/procedure sourcebooks and distinguish implementation from SURPS behavior semantics | [SURPS integration thread](https://github.com/TrentBest/TheSingularityWorkshop.Gestures/issues/36) |
| [Ontology](https://github.com/TrentBest/TheSingularityWorkshop.Ontology) | Candidate, not enrolled | Reusable ontological structures, identifiers, relationships and schemas | Declare reusable semantic capabilities and clarify boundaries with SURPS roleplaying ontology | [Enrollment invitation](https://github.com/TrentBest/TheSingularityWorkshop.Ontology/issues/10) |

## Not yet admitted to this intake

StoryBuilder and raWWar appear as candidate domains in proposed book records, but their exact repository identities and participation declarations have not been verified in this intake. They are intentionally not presented as enrolled or assigned. Add them only after confirming their canonical repository identities and inviting them through this same contract.

## Coordination rules

- Keep exactly `master` and `development` as active branches.
- All normal work and cross-repository intake evidence land on `development`.
- Each repository remains the source of truth for its own domain.
- SURPS is the only cross-repository master book registry.
- A book may have contributors, but exactly one accountable owning repository.
- No release or package publication follows from enrollment or documentation changes; those require explicit release authorization.

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
