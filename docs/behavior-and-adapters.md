# SURPS Behavior Model and Adapters

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

## The central decision

SURPS describes one underlying world and one underlying behavior model. Tabletop play and digital play are not separate rulesets and must not drift into separate truths. They are adapters that expose the same authored semantics at different levels of detail.

- **Behavior model** — the authored description of what exists, what can act, what constrains it, how interactions change state, and what consequences follow.
- **Digital adapter** — evaluates the detailed model against live state with machine assistance.
- **Tabletop adapter** — a deliberately compressed, human-manageable procedure derived from workshop evaluation of the same model.
- **Workshop calibration** — authoring/build-time simulation and analysis that derives dice targets, probability bands, qualitative effects, quick references, and paper procedures.
- **Compiled behavior package** — versioned, reusable digital artifacts generated from the behavior source and its providers.

The source of truth is not a particular die, hit-point scale, or damage formula. Those are possible representations. The source of truth is the behavior and the consequences it produces.

## Why this is not two game systems

A tabletop rule is a useful abstraction, not a second reality. A digital simulation can represent more interacting variables than people can comfortably track. The tabletop adapter selects the smallest set of observable decisions and outcomes that preserves the behavior's identity.

The tabletop adapter must not invent different causal semantics. The digital adapter must not quietly invalidate the tabletop experience. When the adapters differ in precision, the book explains what was compressed and why.

## The authoring and compilation lifecycle

```text
Authored domain behavior + ontology + provider contracts
                    |
                    v
        Validate types, units, scope, provenance
                    |
                    v
       Workshop simulation / scenario sampling
                    |
          +---------+---------+
          |                   |
          v                   v
   Tabletop adapter     Digital compilation
   - dice procedure     - compiled behavior
   - target bands       - response curves / tables
   - qualitative harm   - provider bindings
   - player aids        - diagnostics / provenance
          |                   |
          v                   v
   Human-run session     Cached runtime execution
```

### Workshop time is where expensive derivation belongs

A creator or game master can author a behavior profile, choose its valid operating envelope, and run representative scenarios. The workshop can compare thousands of cases, expose edge conditions, and derive a paper procedure. This is where dice values should be calculated: from observed behavior distributions and declared calibration goals, not chosen first and rationalized afterward.

A derived tabletop artifact records at least:

- source behavior identity and content hash;
- source book and version;
- evaluator/provider identity and version;
- units/schema/compiler version;
- calibration envelope and assumptions;
- scenario set, sample method, and reproducibility seed;
- mapping from measured outcomes to human-readable bands and dice procedure;
- generation timestamp/build identity and validation evidence.

A derived artifact is reproducible and reviewable. A source change invalidates it.

## The cache boundary

**Cache immutable compiled behavior, not stale world outcomes.**

Cacheable artifacts include parsed/validated behavior graphs, provider binding plans, compiled expressions, static lookup tables, response curves, calibrated tabletop profiles, and immutable reference data. Key the cache by every input that can change its meaning: behavior content hash, book version, schema/units version, compiler version, provider version, and declared compilation settings.

Live evaluation still binds current actor condition, target identity and state, equipment, environment, position, time, and other mutable context. Those inputs can change between actions. A result that depends on them must not be reused as if it were still true.

At runtime:

1. Load and warm the experience's compiled behavior package.
2. Resolve the selected book/provider versions.
3. Bind current state to the compiled model.
4. Evaluate only the affected interaction or state transition.
5. Record the result, inputs, provenance, and changed state.
6. Reuse compiled artifacts until their content/version key changes.

This is the gap to close before claiming a high-performance digital RPG: a stable compiled artifact format, dependency/version keys, cache invalidation, cold/warm benchmarks, and proof that live state changes are never hidden by stale result caching.

## Two audiences, one source

A book must offer at least two editorial paths:

- **Player path:** concise concept, what the character can perceive or attempt, meaningful choices, and the procedure needed to participate. Do not burden players with every internal variable.
- **Game Master / Workshop path:** full causal model, hidden facts, domain data, edge cases, authoring controls, scenario tools, and diagnostics. The GM should be able to manipulate the story without holding the whole simulation in working memory.

The same content can also be presented as a tabletop quick-start and a digital implementation guide. These are views, not duplicate books.

## Worked teaching example: a fireball

The [living system guide](system-guide.html) loads an authored [behavior profile](examples/fireball-behavior.json), validated against the [behavior profile schema](schemas/behavior-profile.schema.json), from this repository. It lets a reader compare a miss, hit, and critical casting, inspect energy continuing beyond the target, run deterministic workshop samples, and see an illustrative 2d6 target derived from the sample probability.

**Honesty boundary:** the fireball profile is an executable teaching prototype, not a canonical SURPS spell, not a validated Physics provider, and not the production workshop compiler. It proves the presentation pattern and exposes the data/calibration boundary; it does not claim that the production behavior engine already exists.

## Terminology

Use **Tabletop adapter** in architecture and implementation documentation. “Paper game” is fine in informal prose. Avoid describing tabletop rules as the underlying source of truth.

Use **Digital adapter** for the machine-assisted presentation/execution path. “Digital RPG” is the player-facing phrase.

Use **Workshop calibration** for the expensive authoring-time process that derives human-scale procedures from behavior.

Use **compiled behavior package** for immutable, versioned runtime-ready artifacts.

---

This is the system-level contract. Individual rulebooks and participating repositories should link to it and implement their domain-specific portions without copying the shared model.
