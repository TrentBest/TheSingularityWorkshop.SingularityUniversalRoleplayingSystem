# SURPS Master Rulebook Map

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

**This is the map of the SURPS rulebook universe.** It points to the authoritative book wherever that book lives, records which repository owns it, and gives domain agents a formal place to sign in as owners. The structured source is the machine-readable [master registry](../../.surps/rulebook-backlog.json); this page is the human-facing, clickable map.

A book may live in SURPS, Physics, FSM_Dungeon, Economy, raWWar, StoryBuilder, or another participating repository. Its location does not change its identity. Similar books remain separate entries when they describe different cultures, eras, settings, or rule variants.

## How to use this map

- **Click a book title** to open its authoritative sourcebook. Planned books link to their registry entry until an owner publishes the book.
- **Owner repository** identifies the one repository accountable for the book. Contributors may supply domain knowledge without taking ownership.
- **Agent sign-in** records the agent identity and repository that claim responsibility. A claim is pending until accepted through a SURPS development-branch pull request.
- **Family** groups related but distinct books. It does not merge them or imply that one replaces the other.
- **Status** describes publication/work readiness. **LOD** describes declared detail, not priority or completion.

## SURPS participating repositories

Only repositories with a verified active SURPS participation declaration are marked **Active** here. A repository referenced by a book or integrated as a dependency is not automatically a participating repository.

| Repository | Domain responsibility | Participation | Catalogue |
|---|---|---|---|
| [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Shared ontology, CORE rules, book identity, composition, cross-domain map | **Active — registry authority** | [SURPS books](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/index.md) |
| [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Physical laws, models, simulations, evidence, Physics sourcebooks | **Active — domain provider** | [Physics books](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/index.md) |

### Integrated or referenced repositories — not yet signed in

| Repository | Role in the ecosystem | Registry status |
|---|---|---|
| [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Underground topology and dungeon environments | Integrated dependency; participation declaration not yet verified |
| [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | City systems, infrastructure, services, civic rules | Referenced domain; participation declaration not yet verified |
| [SingularityLaboratories](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories) | Laboratory staffing, experiments, apparatus, educational experiences | Referenced domain; participation declaration not yet verified |
| [Gauntlet](https://github.com/TrentBest/TheSingularityWorkshop.Gauntlet) | Selected-book enrollment and conformance evidence | Planned integration |


### Domain repositories available for future sign-in

These repositories are known in the Workshop ecosystem, but their active SURPS participation has not yet been verified. They are eligible to submit their own participation declaration and agent sign-in when ready.

| Repository | Domain | Registry status |
|---|---|---|
| [Economy](https://github.com/TrentBest/TheSingularityWorkshop.Economy) | Markets, currency, trade, production, labor, logistics | Candidate — not enrolled |
| [Gestures](https://github.com/TrentBest/TheSingularityWorkshop.Gestures) | Posture, gesture, locomotion, embodied interaction | Candidate — not enrolled |
| [Ontology](https://github.com/TrentBest/TheSingularityWorkshop.Ontology) | Shared ontological structures and concepts | Candidate — not enrolled |
| StoryBuilder | Campaign and narrative construction | Candidate repository identity needs confirmation |
| raWWar | Warfare and military systems | Candidate repository identity needs confirmation |

Repositories become Active by adding a valid .surps/participation.json declaration in their own development branch and submitting a registration PR to this map. SURPS must not claim a repository has signed in before that evidence exists.

## Existing books — authoritative links

| Book | Family | LOD | Owner repository | Status | Agent sign-in |
|---|---|---:|---|---|---|
| [Dwarves — Core Concept](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/dwarves-core-concept.md) | Dwarves | 0 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft | SURPS editorial ownership |
| [CORE Spying](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/core-spying.md) | Spying | 0 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft / tabletop playtest | SURPS editorial ownership |
| [Dungeons and Underground](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/dungeons-and-underground.md) | Dungeons and Underground | 1 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft | SURPS editorial ownership |
| [Dwarves](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/dwarves.md) | Dwarves | 1 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft | SURPS editorial ownership |
| [Dwarven Strongholds](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/dwarven-mountain-fortress.md) | Dwarven Strongholds | 2 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft | SURPS editorial ownership |
| [NPCs in Play — SURPS ownership note](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/nonplayer-characters.md) | Nonplayer Characters | 1 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft | SURPS editorial ownership |
| [Power and Industrial Systems](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/power-and-industrial-systems.md) | Power and Industry | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft | Physics domain ownership |
| [Ocean, Atmosphere, and Maritime Phenomena](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/ocean-atmosphere-maritime-phenomena.md) | Maritime and Atmosphere | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft | Physics domain ownership |
| [Batteries and Energy Storage](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/batteries-and-energy-storage.md) | Energy Storage | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft | Physics domain ownership |
| [Nuclear Fission Facilities](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/nuclear-fission-facilities.md) | Nuclear Energy | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft | Physics domain ownership |

## Planned and unclaimed books

The following are backlog entries, not claims that the books already exist. Each entry's stable ID, scope, owner slot, and dependencies are in the [machine-readable registry](../../.surps/rulebook-backlog.json).

### Universal foundations

- The World Model — worlds, environments, time, space, history. **Proposed owner:** SURPS; Physics contributes physical models.
- The Entity Compendium — identity, attributes, capabilities, composition, relationships. **Proposed owner:** SURPS.
- Behavior and Agency — perception, motivation, state, decision-making, action. **Proposed owner:** SURPS; Gestures and Physics contribute.
- Interaction and Consequence — events, conflict, cooperation, damage, change, causality. **Proposed owner:** SURPS.
- The Game Master's Workshop — encounters, scenarios, campaigns, experiences. **Proposed owner:** StoryBuilder.
- The Living Atlas — worked examples, locations, inhabitants, factions, environments. **Proposed owner:** SURPS with domain contributors.

### Warfare and strategy — same family, distinct books

- The Art of War — general strategic warfare foundation. **Owner:** unclaimed.
- The Art of War II — Chinese Warfare — a distinct Chinese-warfare-focused companion/specialization, not a replacement for the first book. **Owner:** unclaimed; a Chinese Warfare domain agent may sign in when its repository and scope are established.

These books demonstrate the identity model: shared familyId, different stable IDs, separate scope, separate owner slot, and separate clickable destination once published.

## Agent sign-in and ownership claims

A domain agent can claim a book without asking SURPS to move it into the SURPS repository. The agent signs in **as the owning repository**, with an identifiable agent identity.

A claim PR must update the matching book record in .surps/rulebook-backlog.json. Include:

| Claim field | Required value |
|---|---|
| ownerRepository | Exact owner/repository name |
| ownership.claimStatus | pending for a new claim; SURPS changes it to accepted after review |
| ownership.agent | Stable CiAi agent name/ID or human maintainer identity |
| ownership.claimedAt | UTC ISO-8601 timestamp |
| bookUrl | Canonical GitHub URL to the book, or null until it exists |
| sourcePath | Repository-relative Markdown path |
| descriptorPath | Repository-relative descriptor path when created |
| contributors | Other registered repositories supplying authoritative content |

**Claim sequence**

1. Agent checks that the book's scope and family are correct and that no equivalent book already exists.
2. Agent confirms its repository is registered as Active. If not, it first submits a participation registration.
3. Agent opens a SURPS issue or PR naming the stable book ID, repository, agent ID, intended path, scope, and dependencies.
4. Agent creates or develops the sourcebook in its own repository's development branch. No NuGet publication or release is implied.
5. The ownership claim is submitted as a PR to SURPS development. SURPS accepts the claim only after verifying the repository, book link, descriptor, and ownership boundaries.
6. The map's book title becomes a direct link to the authoritative book. The registry records the owner and contributors.

An agent may propose a new book entry, but it must search for an existing family/title/scope before creating a new stable ID. Similar titles are allowed when the scope is genuinely distinct. A repository may contribute to a book without claiming ownership.

## Status vocabulary

| Status | Meaning |
|---|---|
| Proposed | Backlog idea with initial scope; no sourcebook is promised |
| Scoped | Scope, family, owner candidate, and acceptance criteria are defined |
| Routed | Accountable owner repository selected |
| Ready | Dependencies and work package are ready for an agent |
| Assigned | An agent has accepted the work |
| In progress | Sourcebook work is underway |
| Review | Content and evidence await review |
| Validated | Acceptance criteria and repository checks pass |
| Published | Stable public book revision released |
| Superseded | A newer or more specific book replaces it for a declared scope; history remains linked |

Ownership claim status is separate: unclaimed, pending, or accepted.

## Rules for the map

1. Stable book IDs never change when titles, owners, or paths change.
2. One accountable owner repository per book; any number of registered contributors.
3. Similar books in different traditions, locations, eras, or settings receive distinct IDs and links.
4. The family groups related books; it does not merge their content or determine precedence.
5. Every existing book link points to the authoritative repository path, not a copied SURPS mirror.
6. A planned book links to its registry entry until an authoritative sourcebook exists.
7. SURPS records participation only when the repository has signed in with a valid declaration.
8. CiAi may propose and prepare changes; claims become accepted only after review. Agents cannot approve their own ownership claims.
9. master remains the released state; registry work is committed to development only.

## Registry and existing catalogues

- [Machine-readable master registry](../../.surps/rulebook-backlog.json)
- [Current SURPS sourcebook catalogue](../books/index.md)
- [Rulebook contract and composition](../rulebooks.md)
- [Rulebook identity and cover standard](../rulebook-identity-and-covers.md)
- [SURPS participation manifest](../../.surps/participation.json)
- [Physics participation manifest](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/.surps/participation.json)

---

![The Singularity Workshop](https://raw.githubusercontent.com/TrentBest/FSM_API/master/Documentation/Branding/TheSingularityWorkshop.png)
