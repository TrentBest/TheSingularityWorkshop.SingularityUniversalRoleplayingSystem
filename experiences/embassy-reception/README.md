# Embassy Reception

**Scenario Experience:** `surps.demo.embassy-reception@0.1.0`  
**Status:** composition declaration added; existing browser scene is the current playable tabletop adapter.

This is the first small SURPS scenario composition. It selects the canonical CORE Spying book by stable book ID and compatible version range. It does not copy the book, MicroBundle, player view, or rules into this Experience.

## Play the current scene

[Open the Embassy Reception playable scene](../../docs/books/core-spying-play.html).

The scene currently supports a player/referee view, declared intent and approach, the provisional CORE Spying 2d6 tabletop procedure, pressure clocks, and information evidence notes.

**Important maturity boundary:** this is a tabletop playtest scene. It is not yet a live Hermit-connected session, a persistent campaign runtime, or a calibrated digital spying evaluator. A human referee remains responsible for uncertain action adjudication.

## Composition declaration

- [Experience book selection](experience-books.json) — validated against the SURPS [Experience Book Selection schema](../../schemas/experience-books.schema.json).
- [Selected book descriptor](../../docs/books/core-spying.book.json).
- [Selected player view](../../.surps/views/core-spying-player.view.json).
- [Selected MicroBundle descriptor](../../.surps/microbundles/core-spying.microbundle.json).

This book-selection document is not the portable FSM_COS composition manifest. Runtime MicroBundle resolution and session execution remain separate integration work.

## Next integration

Track the end-to-end companion/session vertical slice in [SURPS #15](https://github.com/TrentBest/TheSingularityWorkshop.SingularityUniversalRoleplayingSystem/issues/15) and [Hermit #8](https://github.com/TrentBest/TheSingularityWorkshop.Hermit/issues/8).
