# SURPS probability-first resolution (design proposal)

![The Singularity Workshop animated moniker](https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg)

## The common language

SURPS should express uncertain outcomes as probabilities on a 0–100 scale. A percentile roll is the natural physical interface: roll 1d100 and succeed when the result is at or below the final success chance. The same probability can also be evaluated deterministically by simulations, AI agents, probability tables, or digital interfaces.

This is a proposed direction, not yet the adopted or implemented core mechanic. Existing CORE Spying 2d6 procedures remain playtest records until a deliberate migration is designed and tested.

## Keep capability distinct from chance

A capability rating describes what an entity can do. It should not be mislabeled as the final probability of success.

For example, a character's Marksmanship capability might be 3/100 for a complete novice or 87/100 for an exceptional marksman. The action resolver then combines that capability with task difficulty, range, visibility, target movement, equipment, preparation, assistance, injury, pressure, and other relevant circumstances.

The resolver produces a final chance in the inclusive range 0–100. A simple first experiment could be:

`chance = clamp(baseCapability + situationalModifiers - taskDifficulty, 0, 100)`

That equation is deliberately provisional. We must calibrate what a rating means, how modifiers stack, how difficulty is represented, and whether capability curves should be linear before making it canonical.

## One probability model, many outcome models

A binary percentile check is a useful baseline, but it should not erase richer outcomes. The probability model can support:
- binary success/failure;
- degrees of success or failure;
- quality, speed, cost, or resource-efficiency distributions;
- opposed actions and competing probabilities;
- repeated attempts, cumulative hazards, and clocks;
- confidence intervals and uncertainty when the source data is incomplete.

The selected outcome model belongs to the action's domain MicroBundle. The shared resolution contract supplies probability semantics and reproducible evaluation.

## Design constraints

1. A capability rating is not automatically a probability of success.
2. Every modifier needs an explicit meaning, unit, range, and stacking rule.
3. A probability of 0 and 100 must have clearly defined edge semantics.
4. Random sampling must be reproducible when a seed is supplied.
5. Probability calculations should be inspectable and testable independently of dice presentation.
6. Do not roll for outcomes that are certain, inconsequential, or better resolved by the fiction.
7. Preserve domain-specific outcome consequences; shared probability does not mean identical procedures.

## Migration experiment

Use CORE Spying as the first comparison case. Implement a side-by-side probability calculator against its existing 2d6 + approach procedure. Enumerate all 36 2d6 outcomes to obtain exact success and outcome-band probabilities for each approach rating and target number. Compare those distributions with candidate percentile curves. Only after the calibration is understood should a new canonical resolution MicroBundle replace or coexist with the playtest procedure.

## Status

- Probability-first direction: proposed.
- Percentile roll interface: proposed.
- Capability rating examples: illustrative.
- Calibration and conversion from existing 2d6 rules: not implemented.
- Current CORE Spying 2d6 procedure: still the active playtest specification.
