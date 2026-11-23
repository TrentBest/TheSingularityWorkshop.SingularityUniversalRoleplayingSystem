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

## Repository onboarding and coordination

See the [SURPS Repository Onboarding Tracker](../repository-onboarding.md) for each repository's current admission status, domain boundary, and coordination thread. Invitations and comments do not count as enrollment; only verified manifests/catalogues and an accepted registry update do.

## SURPS participating repositories

Only repositories with a verified active SURPS participation declaration are marked **Active** here. A repository referenced by a book or integrated as a dependency is not automatically a participating repository.

| Repository | Domain responsibility | Participation | Catalogue |
|---|---|---|---|
| [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Shared ontology, CORE rules, book identity, composition, cross-domain map | **Active — registry authority** | [SURPS books](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/index.md) |
| [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Physical laws, models, simulations, evidence, Physics sourcebooks | **Active — domain provider** | [Physics books](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/index.md) |

### Integrated or referenced repositories — not yet signed in

| Repository | Role in the ecosystem | Registry status |
|---|---|---|
| [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Underground topology, environmental state, and original fantasy sourcebooks | Integrated / not enrolled; six canonical books declared, all ownership claims pending independent review |
| [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | City systems, infrastructure, services, civic rules, residents, and civic institutions | Integrated / not enrolled; ten structured draft books declared, all ownership claims pending independent review |
| [SingularityLaboratories](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories) | Scientific inquiry, laboratories, experiments, apparatus, facilities, staffing, and research workflows | Integrated / not enrolled; three structured draft books declared, all ownership claims pending independent review |
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
| [Underground Environments: Formation, Space, and Consequence](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/books/underground-environments.md) | Underground Environments | 2 | [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Fantasy Foundations](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/books/fantasy-foundations.md) | Fantasy Foundations | 1 | [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Elves: Peoples of the Long Memory](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/books/elves.md) | Elves | 1 | [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [The Living Bestiary](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/books/bestiary.md) | Living Bestiary | 1 | [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Dragons and Wyrms: Ecology of the Elder Sky](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/books/dragons-and-wyrms.md) | Dragons and Wyrms | 1 | [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Ruins and Lost Places: Reading the Layers of a World](https://github.com/TrentBest/FSM_Dungeon/blob/development/docs/books/ruins-and-lost-places.md) | Ruins and Lost Places | 1 | [FSM_Dungeon](https://github.com/TrentBest/FSM_Dungeon) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Nonplayer Characters](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/nonplayer-characters.md) | Nonplayer Characters | 1 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Thieves & Shadow Work](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/thieves-and-shadow-work.md) | Thieves & Shadow Work | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [The Urban Underworld](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/urban-underworld.md) | The Urban Underworld | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Law Enforcement & Public Safety](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/law-enforcement-and-public-safety.md) | Law Enforcement & Public Safety | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Justice, Courts & Restitution](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/justice-courts-and-restitution.md) | Justice, Courts & Restitution | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Governance & Civic Administration](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/governance-and-civic-administration.md) | Governance & Civic Administration | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Politics, Power & Public Will](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/politics-power-and-public-will.md) | Politics, Power & Public Will | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Elections & Player Participation](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/elections-and-player-participation.md) | Elections & Player Participation | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Vigilantes & Civic Justice](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/vigilantes-and-civic-justice.md) | Vigilantes & Civic Justice | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Villains & Antagonists](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity/blob/development/docs/books/villains-and-antagonists.md) | Villains & Antagonists | 2 | [SingularityCity](https://github.com/TrentBest/TheSingularityWorkshop.SingularityCity) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Scientific Inquiry](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories/blob/development/docs/books/scientific-inquiry.md) | Scientific Inquiry | 1 | [SingularityLaboratories](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Laboratory NPCs](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories/blob/development/docs/books/laboratory-npcs.md) | Laboratory NPCs | 2 | [SingularityLaboratories](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Flagship Laboratory Facilities](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories/blob/development/docs/books/flagship-laboratory-facilities.md) | Flagship Laboratory Facilities | 3 | [SingularityLaboratories](https://github.com/TrentBest/TheSingularityWorkshop.SingularityLaboratories) | Draft — ownership pending SURPS review | ChatGPT GitHub agent (pending SURPS review) |
| [Dwarves](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/dwarves.md) | Dwarves | 1 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft | SURPS editorial ownership |
| [Dwarven Strongholds](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/dwarven-mountain-fortress.md) | Dwarven Strongholds | 2 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft | SURPS editorial ownership |
| [NPCs in Play — SURPS ownership note](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/blob/development/docs/books/nonplayer-characters.md) | Nonplayer Characters | 1 | [SURPS](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem) | Draft | SURPS editorial ownership |
| [Power and Industrial Systems](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/power-and-industrial-systems.md) | Power and Industry | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft | Physics domain ownership |
| [Ocean, Atmosphere, and Maritime Phenomena](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/ocean-atmosphere-maritime-phenomena.md) | Maritime and Atmosphere | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft | Physics domain ownership |
| [Batteries and Energy Storage](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/batteries-and-energy-storage.md) | Energy Storage | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft | Physics domain ownership |
| [Nuclear Fission Facilities](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/nuclear-fission-facilities.md) | Nuclear Energy | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft | Physics domain ownership |
| [Geology and Planetary Evolution](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/geology-and-planetary-evolution.md) | Geology | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft — ownership pending | ChatGPT GitHub agent (pending SURPS review) |
| [Weather and Climate](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/weather-and-climate.md) | Weather and Atmosphere | 1 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft — ownership pending | ChatGPT GitHub agent (pending SURPS review) |
| [Geomorphology and Surface Processes](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/geomorphology-and-surface-processes.md) | Geology | 2 | [Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics) | Draft — ownership pending | ChatGPT GitHub agent (pending SURPS review) |

## Planned and unclaimed books

The master backlog currently contains 65 proposed books. Each title below jumps to its individual registry entry on this page. The registry records the stable ID, family, scope, candidate owner, agent sign-in slot, priority, and acceptance criteria. A planned entry becomes a direct book link when its authoritative sourcebook is published.

### Core

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [The World Model](#book-surps-core-world-model) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | normal | 0 |
| [The Entity Compendium](#book-surps-core-entity-compendium) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | normal | 0 |
| [Behavior and Agency](#book-surps-core-behavior-agency) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | normal | 0 |
| [Interaction and Consequence](#book-surps-core-interaction-consequence) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | normal | 0 |

### Physical

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [Classical Mechanics](#book-physics-domain-classical-mechanics) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Forces, Energy, and Momentum](#book-physics-domain-forces-energy-momentum) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Materials and Material Properties](#book-physics-domain-materials) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Oceans, Rivers, and Hydrology](#book-physics-domain-hydrology) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Ecology and Natural Environments](#book-physics-domain-ecology) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Electricity and Electrical Grids](#book-physics-domain-electricity-grids) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Thermodynamics and Heat Transfer](#book-physics-domain-thermodynamics) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Power Generation and Distribution](#book-physics-domain-power-generation) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Industrial Manufacturing](#book-physics-domain-industrial-manufacturing) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Tools, Machines, and Mechanisms](#book-physics-domain-machines-mechanisms) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Vehicles and Transportation](#book-physics-domain-vehicles) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Aircraft and Flight](#book-physics-domain-aircraft) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Maritime Vessels](#book-physics-domain-maritime-vessels) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Spacecraft and Orbital Systems](#book-physics-domain-spacecraft) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |

### Built World

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [Architecture and Building Systems](#book-city-domain-architecture) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | normal | 1 |
| [Construction Materials and Methods](#book-city-domain-construction) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | normal | 1 |
| [Roads, Bridges, and Transportation Networks](#book-city-domain-transport-networks) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | normal | 1 |
| [Water, Waste, and Public Utilities](#book-city-domain-public-utilities) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | normal | 1 |
| [Residential Buildings](#book-city-domain-residential-buildings) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | normal | 1 |
| [Commercial Buildings](#book-city-domain-commercial-buildings) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | normal | 1 |
| [Industrial Facilities](#book-city-domain-industrial-facilities) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | normal | 1 |
| [Cities and Urban Planning](#book-city-domain-urban-planning) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | normal | 1 |

### Economy

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [Trade, Markets, and Currency](#book-economy-domain-markets-trade) | TrentBest/TheSingularityWorkshop.Economy (candidate; not enrolled) | high | 2 |
| [Labor, Professions, and Occupations](#book-economy-domain-labor-professions) | TrentBest/TheSingularityWorkshop.Economy (candidate; not enrolled) | high | 2 |
| [Supply Chains and Logistics](#book-economy-domain-supply-chains) | TrentBest/TheSingularityWorkshop.Economy (candidate; not enrolled) | high | 2 |
| [Property, Ownership, and Land Use](#book-economy-domain-property-land-use) | TrentBest/TheSingularityWorkshop.Economy (candidate; not enrolled) | high | 2 |

### Life

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [Biology and Living Organisms](#book-surps-domain-biology) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Anatomy and Physiology](#book-surps-domain-anatomy-physiology) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Animal Behavior and Ecology](#book-surps-domain-animal-behavior) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Bestiary Compendium](#book-surps-reference-bestiary) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Plants, Fungi, and Natural Resources](#book-surps-reference-plants-fungi) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |

### Society

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [Government and Civic Institutions](#book-city-domain-government) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | high | 2 |
| [Law, Justice, and Social Order](#book-surps-domain-law-justice) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Population and Demographics](#book-city-domain-population) | TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled) | high | 2 |
| [Species and Peoples](#book-surps-domain-species-peoples) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Factions, Guilds, and Organizations](#book-surps-domain-factions-guilds) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Religion, Belief, and Philosophy](#book-surps-domain-belief-philosophy) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |

### Knowledge

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [Languages, Scripts, and Communication](#book-surps-domain-languages-scripts) | TrentBest/TheSingularityWorkshop.Ontology (candidate; not enrolled) | high | 2 |

### Warfare

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [The Art of War](#book-surps-domain-art-of-war) | raWWar | normal | 1 |
| [The Art of War II — Chinese Warfare](#book-surps-domain-art-of-war-chinese-warfare-ii) | Chinese Warfare domain | normal | 2 |
| [Military Organization](#book-rawwar-domain-military-organization) | raWWar | high | 2 |
| [Tactical Doctrine](#book-rawwar-domain-tactical-doctrine) | raWWar | high | 2 |
| [Strategy and Campaign Logistics](#book-rawwar-domain-campaign-logistics) | raWWar | high | 2 |

### Play

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [The Game Master's Workshop](#book-surps-core-game-masters-workshop) | StoryBuilder | normal | 1 |
| [Combat and Conflict](#book-surps-play-combat-conflict) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Weapons and Equipment](#book-surps-reference-weapons-equipment) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | high | 2 |
| [Armor and Protection](#book-surps-reference-armor-protection) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | high | 2 |
| [Stealth, Espionage, and Intelligence](#book-surps-play-stealth-espionage) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Diplomacy and Negotiation](#book-surps-play-diplomacy) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Exploration and Discovery](#book-surps-play-exploration) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Wilderness Survival](#book-surps-play-wilderness-survival) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Character Progression](#book-surps-play-character-progression) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Reputation and Relationships](#book-surps-play-reputation-relationships) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |
| [Social and Political Consequences](#book-surps-play-social-political-consequences) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | high | 2 |

### Narrative

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [Quests and Adventures](#book-storybuilder-play-quests-adventures) | StoryBuilder | high | 2 |
| [Campaign Construction](#book-storybuilder-play-campaign-construction) | StoryBuilder | high | 2 |
| [Encounter Construction](#book-storybuilder-play-encounter-construction) | StoryBuilder | high | 2 |

### Reference

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [The Living Atlas](#book-surps-core-living-atlas) | TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem | normal | 1 |

### Technology

| Book | Candidate owner | Priority | LOD |
|---|---|---|---:|
| [Technology and Historical Eras](#book-physics-domain-technology-eras) | TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled) | high | 2 |

## Individual backlog entries

<a id="book-surps-domain-art-of-war"></a>
### The Art of War

- **Stable ID:** surps.domain.art-of-war
- **Family:** art-of-war
- **Category / LOD:** Warfare / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** raWWar
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** General strategic warfare sourcebook; exact cultural, historical, and operational scope to be established.
- **Acceptance:** Define scope, playable procedures, worked examples, implementation evidence, and publication assets.

<a id="book-surps-domain-art-of-war-chinese-warfare-ii"></a>
### The Art of War II — Chinese Warfare

- **Stable ID:** surps.domain.art-of-war.chinese-warfare-ii
- **Family:** art-of-war
- **Category / LOD:** Warfare / 2
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** Chinese Warfare domain
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Distinct Chinese-warfare-focused companion or specialization, not a replacement for The Art of War.
- **Related books:** surps.domain.art-of-war
- **Acceptance:** Define scope, playable procedures, worked examples, implementation evidence, and publication assets.

<a id="book-surps-core-world-model"></a>
### The World Model

- **Stable ID:** surps.core.world-model
- **Family:** world-model
- **Category / LOD:** Core / 0
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Worlds, environments, time, space, history, and shared model of a playable reality.
- **Acceptance:** Define scope, playable procedures, worked examples, implementation evidence, and publication assets.

<a id="book-surps-core-entity-compendium"></a>
### The Entity Compendium

- **Stable ID:** surps.core.entity-compendium
- **Family:** entity-compendium
- **Category / LOD:** Core / 0
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Identity, attributes, capabilities, composition, and relationships.
- **Acceptance:** Define scope, playable procedures, worked examples, implementation evidence, and publication assets.

<a id="book-surps-core-behavior-agency"></a>
### Behavior and Agency

- **Stable ID:** surps.core.behavior-agency
- **Family:** behavior-agency
- **Category / LOD:** Core / 0
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Perception, motivation, state, decision-making, and action.
- **Acceptance:** Define scope, playable procedures, worked examples, implementation evidence, and publication assets.

<a id="book-surps-core-interaction-consequence"></a>
### Interaction and Consequence

- **Stable ID:** surps.core.interaction-consequence
- **Family:** interaction-consequence
- **Category / LOD:** Core / 0
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Events, conflict, cooperation, damage, change, and causality.
- **Acceptance:** Define scope, playable procedures, worked examples, implementation evidence, and publication assets.

<a id="book-surps-core-game-masters-workshop"></a>
### The Game Master's Workshop

- **Stable ID:** surps.core.game-masters-workshop
- **Family:** game-masters-workshop
- **Category / LOD:** Play / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** StoryBuilder
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Composing encounters, scenarios, campaigns, and experiences.
- **Acceptance:** Define scope, playable procedures, worked examples, implementation evidence, and publication assets.

<a id="book-surps-core-living-atlas"></a>
### The Living Atlas

- **Stable ID:** surps.core.living-atlas
- **Family:** living-atlas
- **Category / LOD:** Reference / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Linked examples of locations, inhabitants, factions, environments, and world-building patterns.
- **Acceptance:** Define scope, playable procedures, worked examples, implementation evidence, and publication assets.

<a id="book-physics-domain-classical-mechanics"></a>
### Classical Mechanics

- **Stable ID:** physics.domain.classical-mechanics
- **Family:** classical-mechanics
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Motion, forces, work, energy, contact, mechanisms, and worked physical examples.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-forces-energy-momentum"></a>
### Forces, Energy, and Momentum

- **Stable ID:** physics.domain.forces-energy-momentum
- **Family:** forces-energy-momentum
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Force models, impulse, momentum transfer, energy accounting, and conservation.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-materials"></a>
### Materials and Material Properties

- **Stable ID:** physics.domain.materials
- **Family:** materials
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Material identity, mechanical and thermal properties, failure modes, processing, and selection.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-geology"></a>
### Geology and Planetary Evolution

- **Stable ID:** physics.domain.geology
- **Family:** geology
- **Category / LOD:** Physical / 1
- **Status:** draft; authoritative sourcebook created
- **Owner repository:** [TrentBest/TheSingularityWorkshop.Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics)
- **Agent sign-in:** pending SURPS review
- **Sourcebook:** [Geology and Planetary Evolution](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/geology-and-planetary-evolution.md)
- **Descriptor:** [geology-and-planetary-evolution.book.json](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/geology-and-planetary-evolution.book.json)
- **Scope:** Planetary interiors, thermal history, mantle and lithosphere behavior, tectonic plates, crustal deformation, fault systems, earthquakes, magmatism, rock cycles, stratigraphy, and geological time.
- **Acceptance:** Clear scope, evidence-backed status, descriptor, cover, implementation links, and validation limits.

<a id="book-physics-domain-weather-atmosphere"></a>
### Weather and Climate

- **Stable ID:** physics.domain.weather-atmosphere
- **Family:** weather-atmosphere
- **Category / LOD:** Physical / 1
- **Status:** draft; authoritative sourcebook created
- **Owner repository:** [TrentBest/TheSingularityWorkshop.Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics)
- **Agent sign-in:** pending SURPS review
- **Sourcebook:** [Weather and Climate](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/weather-and-climate.md)
- **Descriptor:** [weather-and-climate.book.json](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/weather-and-climate.book.json)
- **Scope:** Atmospheric state, pressure, temperature, moisture, circulation, clouds, precipitation, storms, seasons, climate statistics, extremes, and weather/climate forcing for coupled surface systems.
- **Acceptance:** Clear scope, evidence-backed status, descriptor, cover, implementation links, and validation limits.

<a id="book-physics-domain-hydrology"></a>
### Oceans, Rivers, and Hydrology

- **Stable ID:** physics.domain.hydrology
- **Family:** hydrology
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Water cycles, watersheds, rivers, lakes, ocean systems, currents, tides, and freshwater availability.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-ecology"></a>
### Ecology and Natural Environments

- **Stable ID:** physics.domain.ecology
- **Family:** ecology
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Habitats, food webs, population dynamics, environmental pressures, and ecosystem change.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-electricity-grids"></a>
### Electricity and Electrical Grids

- **Stable ID:** physics.domain.electricity-grids
- **Family:** electricity-grids
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Circuits, loads, networks, generation interfaces, protection concepts, and grid dispatch.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-thermodynamics"></a>
### Thermodynamics and Heat Transfer

- **Stable ID:** physics.domain.thermodynamics
- **Family:** thermodynamics
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Thermal state, heat transfer, phase change, engines, cycles, and energy efficiency.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-power-generation"></a>
### Power Generation and Distribution

- **Stable ID:** physics.domain.power-generation
- **Family:** power-generation
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Generation technologies, conversion, transmission, distribution, dispatch, and resilience.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-industrial-manufacturing"></a>
### Industrial Manufacturing

- **Stable ID:** physics.domain.industrial-manufacturing
- **Family:** industrial-manufacturing
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Process energy, machines, material transformation, throughput, automation, and production constraints.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-machines-mechanisms"></a>
### Tools, Machines, and Mechanisms

- **Stable ID:** physics.domain.machines-mechanisms
- **Family:** machines-mechanisms
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Levers, gears, linkages, fasteners, simple machines, tools, and mechanical advantage.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-vehicles"></a>
### Vehicles and Transportation

- **Stable ID:** physics.domain.vehicles
- **Family:** vehicles
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Shared vehicle concepts, mobility, propulsion, handling, capacity, maintenance, and infrastructure interfaces.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-aircraft"></a>
### Aircraft and Flight

- **Stable ID:** physics.domain.aircraft
- **Family:** aircraft
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Aerodynamics, flight envelopes, propulsion, navigation, aircraft systems, and operating context.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-maritime-vessels"></a>
### Maritime Vessels

- **Stable ID:** physics.domain.maritime-vessels
- **Family:** maritime-vessels
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Hull forms, buoyancy, propulsion, stability, cargo, vessel classes, and maritime operations.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-spacecraft"></a>
### Spacecraft and Orbital Systems

- **Stable ID:** physics.domain.spacecraft
- **Family:** spacecraft
- **Category / LOD:** Physical / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Orbital motion, spacecraft subsystems, propulsion, communications, thermal control, and mission constraints.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-architecture"></a>
### Architecture and Building Systems

- **Stable ID:** city.domain.architecture
- **Family:** architecture
- **Category / LOD:** Built World / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Building types, spatial organization, occupancy, circulation, accessibility, and services.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-construction"></a>
### Construction Materials and Methods

- **Stable ID:** city.domain.construction
- **Family:** construction
- **Category / LOD:** Built World / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Construction processes, structural materials, assemblies, tools, labor, and inspection concepts.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-transport-networks"></a>
### Roads, Bridges, and Transportation Networks

- **Stable ID:** city.domain.transport-networks
- **Family:** transport-networks
- **Category / LOD:** Built World / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Street hierarchies, crossings, bridges, traffic, freight, transit, and network capacity.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-public-utilities"></a>
### Water, Waste, and Public Utilities

- **Stable ID:** city.domain.public-utilities
- **Family:** public-utilities
- **Category / LOD:** Built World / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Water supply, wastewater, drainage, solid waste, energy services, maintenance, and resilience.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-residential-buildings"></a>
### Residential Buildings

- **Stable ID:** city.domain.residential-buildings
- **Family:** residential-buildings
- **Category / LOD:** Built World / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Housing forms, household spaces, construction, utilities, tenancy, and neighborhood context.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-commercial-buildings"></a>
### Commercial Buildings

- **Stable ID:** city.domain.commercial-buildings
- **Family:** commercial-buildings
- **Category / LOD:** Built World / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Retail, offices, hospitality, public access, services, staffing, and commercial operations.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-industrial-facilities"></a>
### Industrial Facilities

- **Stable ID:** city.domain.industrial-facilities
- **Family:** industrial-facilities
- **Category / LOD:** Built World / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Factories, workshops, warehouses, process layouts, utilities, safety zones, and logistics.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-urban-planning"></a>
### Cities and Urban Planning

- **Stable ID:** city.domain.urban-planning
- **Family:** urban-planning
- **Category / LOD:** Built World / 1
- **Status:** proposed
- **Priority:** normal
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Land use, zoning concepts, density, neighborhoods, public spaces, growth, and urban services.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-government"></a>
### Government and Civic Institutions

- **Stable ID:** city.domain.government
- **Family:** government
- **Category / LOD:** Society / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Civic roles, public institutions, services, decision processes, budgets, and accountability.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-domain-law-justice"></a>
### Law, Justice, and Social Order

- **Stable ID:** surps.domain.law-justice
- **Family:** law-justice
- **Category / LOD:** Society / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Norms, legal systems, jurisdiction, adjudication, enforcement, rights, obligations, and consequences.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-city-domain-population"></a>
### Population and Demographics

- **Stable ID:** city.domain.population
- **Family:** population
- **Category / LOD:** Society / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityCity (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Population structure, migration, households, demographics, public needs, and uncertainty.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-economy-domain-markets-trade"></a>
### Trade, Markets, and Currency

- **Stable ID:** economy.domain.markets-trade
- **Family:** markets-trade
- **Category / LOD:** Economy / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.Economy (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Exchange, prices, currency, market structure, trade, contracts, and economic consequences.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-economy-domain-labor-professions"></a>
### Labor, Professions, and Occupations

- **Stable ID:** economy.domain.labor-professions
- **Family:** labor-professions
- **Category / LOD:** Economy / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.Economy (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Skills, occupations, employment, compensation, labor markets, professions, and career progression.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-economy-domain-supply-chains"></a>
### Supply Chains and Logistics

- **Stable ID:** economy.domain.supply-chains
- **Family:** supply-chains
- **Category / LOD:** Economy / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.Economy (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Sourcing, inventory, transport, warehousing, distribution, bottlenecks, and resilience.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-economy-domain-property-land-use"></a>
### Property, Ownership, and Land Use

- **Stable ID:** economy.domain.property-land-use
- **Family:** property-land-use
- **Category / LOD:** Economy / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.Economy (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Property rights, possession, tenancy, land valuation, transfer, inheritance, and use constraints.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-domain-biology"></a>
### Biology and Living Organisms

- **Stable ID:** surps.domain.biology
- **Family:** biology
- **Category / LOD:** Life / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Organism structure, life processes, classification, variation, adaptation, and environmental relationships.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-domain-anatomy-physiology"></a>
### Anatomy and Physiology

- **Stable ID:** surps.domain.anatomy-physiology
- **Family:** anatomy-physiology
- **Category / LOD:** Life / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Body systems, structure, function, health states, injury concepts, and species variation.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-domain-animal-behavior"></a>
### Animal Behavior and Ecology

- **Stable ID:** surps.domain.animal-behavior
- **Family:** animal-behavior
- **Category / LOD:** Life / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Sensing, communication, social behavior, territory, feeding, reproduction, and ecological niches.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-reference-bestiary"></a>
### Bestiary Compendium

- **Stable ID:** surps.reference.bestiary
- **Family:** bestiary
- **Category / LOD:** Life / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** A cross-setting reference for creatures, habitats, behavior, capabilities, evidence, and encounter use.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-reference-plants-fungi"></a>
### Plants, Fungi, and Natural Resources

- **Stable ID:** surps.reference.plants-fungi
- **Family:** plants-fungi
- **Category / LOD:** Life / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Plant and fungal forms, growth, habitats, resources, toxicity concepts, and ecological roles.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-domain-species-peoples"></a>
### Species and Peoples

- **Stable ID:** surps.domain.species-peoples
- **Family:** species-peoples
- **Category / LOD:** Society / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Species identity, variation, culture, communities, adaptation, and cross-society interaction.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-domain-factions-guilds"></a>
### Factions, Guilds, and Organizations

- **Stable ID:** surps.domain.factions-guilds
- **Family:** factions-guilds
- **Category / LOD:** Society / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Membership, roles, authority, resources, incentives, rivalries, alliances, and organizational change.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-domain-belief-philosophy"></a>
### Religion, Belief, and Philosophy

- **Stable ID:** surps.domain.belief-philosophy
- **Family:** belief-philosophy
- **Category / LOD:** Society / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Belief systems, practices, institutions, ethics, worldviews, and cultural variation.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-domain-languages-scripts"></a>
### Languages, Scripts, and Communication

- **Stable ID:** surps.domain.languages-scripts
- **Family:** languages-scripts
- **Category / LOD:** Knowledge / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.Ontology (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Language structures, writing systems, translation, literacy, signals, and communication constraints.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-play-combat-conflict"></a>
### Combat and Conflict

- **Stable ID:** surps.play.combat-conflict
- **Family:** combat-conflict
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Declarations, initiative alternatives, positioning, uncertainty, consequences, retreat, and recovery.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-reference-weapons-equipment"></a>
### Weapons and Equipment

- **Stable ID:** surps.reference.weapons-equipment
- **Family:** weapons-equipment
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Equipment categories, physical properties, handling, maintenance, historical context, and tabletop procedures.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-reference-armor-protection"></a>
### Armor and Protection

- **Stable ID:** surps.reference.armor-protection
- **Family:** armor-protection
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Protective materials, coverage, mobility trade-offs, damage interaction, and repair.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-rawwar-domain-military-organization"></a>
### Military Organization

- **Stable ID:** rawwar.domain.military-organization
- **Family:** military-organization
- **Category / LOD:** Warfare / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** raWWar
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Units, command roles, organization, readiness, recruitment, training, and institutional structures.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-rawwar-domain-tactical-doctrine"></a>
### Tactical Doctrine

- **Stable ID:** rawwar.domain.tactical-doctrine
- **Family:** tactical-doctrine
- **Category / LOD:** Warfare / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** raWWar
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Maneuver, terrain, formations, reconnaissance, coordination, objectives, and tactical trade-offs.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-rawwar-domain-campaign-logistics"></a>
### Strategy and Campaign Logistics

- **Stable ID:** rawwar.domain.campaign-logistics
- **Family:** campaign-logistics
- **Category / LOD:** Warfare / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** raWWar
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Supply, movement, sustainment, intelligence, command, operational tempo, and campaign constraints.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-play-stealth-espionage"></a>
### Stealth, Espionage, and Intelligence

- **Stable ID:** surps.play.stealth-espionage
- **Family:** stealth-espionage
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Concealment, observation, information gathering, counterintelligence, exposure, and consequences.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-play-diplomacy"></a>
### Diplomacy and Negotiation

- **Stable ID:** surps.play.diplomacy
- **Family:** diplomacy
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Interests, leverage, bargaining, agreements, trust, protocol, and relationship consequences.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-play-exploration"></a>
### Exploration and Discovery

- **Stable ID:** surps.play.exploration
- **Family:** exploration
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Navigation, observation, uncertainty, discovery, mapping, expedition planning, and return.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-play-wilderness-survival"></a>
### Wilderness Survival

- **Stable ID:** surps.play.wilderness-survival
- **Family:** wilderness-survival
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Shelter, exposure, water, food, navigation, hazards, resource depletion, and rescue.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-storybuilder-play-quests-adventures"></a>
### Quests and Adventures

- **Stable ID:** storybuilder.play.quests-adventures
- **Family:** quests-adventures
- **Category / LOD:** Narrative / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** StoryBuilder
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Objectives, hooks, scenes, challenges, branching outcomes, rewards, and persistent consequences.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-storybuilder-play-campaign-construction"></a>
### Campaign Construction

- **Stable ID:** storybuilder.play.campaign-construction
- **Family:** campaign-construction
- **Category / LOD:** Narrative / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** StoryBuilder
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Campaign premises, arcs, factions, pacing, continuity, player agency, and long-running state.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-storybuilder-play-encounter-construction"></a>
### Encounter Construction

- **Stable ID:** storybuilder.play.encounter-construction
- **Family:** encounter-construction
- **Category / LOD:** Narrative / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** StoryBuilder
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Encounter goals, environments, participants, tension, challenge composition, and resolution paths.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-play-character-progression"></a>
### Character Progression

- **Stable ID:** surps.play.character-progression
- **Family:** character-progression
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Advancement, learning, capability change, reputation, milestones, and campaign continuity.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-play-reputation-relationships"></a>
### Reputation and Relationships

- **Stable ID:** surps.play.reputation-relationships
- **Family:** reputation-relationships
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Trust, status, social memory, networks, obligations, rivalry, and relationship change.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-surps-play-social-political-consequences"></a>
### Social and Political Consequences

- **Stable ID:** surps.play.social-political-consequences
- **Family:** social-political-consequences
- **Category / LOD:** Play / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Public response, institutional change, faction reactions, legitimacy, and long-term consequences.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-technology-eras"></a>
### Technology and Historical Eras

- **Stable ID:** physics.domain.technology-eras
- **Family:** technology-eras
- **Category / LOD:** Technology / 2
- **Status:** proposed
- **Priority:** high
- **Owner slot:** TrentBest/TheSingularityWorkshop.Physics (candidate; not enrolled)
- **Agent sign-in:** unclaimed; repository and agent identity are not yet signed in
- **Scope:** Materials, energy, manufacturing, communications, transport, and capability constraints by era.
- **Acceptance:** Clear scope, exclusions, and cross-references; Usable tabletop procedures with worked examples; Evidence-backed implementation status and limitations; Descriptor, cover, and validation tests when promoted to a published book

<a id="book-physics-domain-geomorphology-surface-processes"></a>
### Geomorphology and Surface Processes

- **Stable ID:** physics.domain.geomorphology-surface-processes
- **Family:** geology
- **Category / LOD:** Physical / 2
- **Status:** draft; authoritative sourcebook created
- **Owner repository:** [TrentBest/TheSingularityWorkshop.Physics](https://github.com/TrentBest/TheSingularityWorkshop.Physics)
- **Agent sign-in:** pending SURPS review
- **Sourcebook:** [Geomorphology and Surface Processes](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/geomorphology-and-surface-processes.md)
- **Descriptor:** [geomorphology-and-surface-processes.book.json](https://github.com/TrentBest/TheSingularityWorkshop.Physics/blob/development/docs/books/geomorphology-and-surface-processes.book.json)
- **Scope:** Weathering, hillslope transport, rivers, groundwater, karst, glaciers, wind, coasts, sediment budgets, soils, and landscape evolution.
- **Acceptance:** Clear scope, evidence-backed status, descriptor, cover, implementation links, and validation limits.

## Agent sign-in and ownership claims

A domain agent can claim a book without asking SURPS to move it into the SURPS repository. The agent signs in **as the owning repository**, with an identifiable agent identity. The ownership record stores both the registry's repository ID and the exact GitHub repository identity that signed the claim.

Start with the [Rulebook owner sign-in issue template](../../.github/ISSUE_TEMPLATE/rulebook-owner-sign-in.yml). To register a domain repository first, use the [SURPS repository participation template](../../.github/ISSUE_TEMPLATE/surps-repository-participation.yml). A claim PR must update the matching book record in .surps/rulebook-backlog.json. Include:

| Claim field | Required value |
|---|---|
| ownerRepository | Exact owner/repository name |
| ownership.claimStatus | pending for a new claim; SURPS changes it to accepted after review |
| ownership.agent | Stable CiAi agent name/ID or human maintainer identity |
| ownership.agentRepository | Exact GitHub owner/repository identity signing the claim |
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
5. The ownership claim is submitted as a PR to SURPS development. Set ownerRepository, ownership.agentRepository, ownership.agent, ownership.claimedAt, and ownership.claimStatus=pending together. SURPS accepts the claim only after verifying the repository, book link, descriptor, and ownership boundaries.
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
