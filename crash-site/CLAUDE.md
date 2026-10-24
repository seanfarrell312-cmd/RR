# Crash Site (working title)

A top-down 2D real-time strategy / automation game that runs in the browser. You are the control program of a crashed starship's robot crew: wake drones, mine and clear the buried wreck, store power crystals, and rebuild the ship section by section. Loosely inspired by LEGO Rock Raiders. Everything here is original: no Rock Raiders or Manic Miners files, art, names or code are used, and none should be.

Current state: level 1 (tutorial) is fully playable start to finish, plus a free play mode.

## Files

- `crash-site.html`: the entire game. One self-contained file (HTML, CSS, JavaScript, Canvas 2D). No build step, no dependencies besides an optional Google Font with a system fallback.
- `tests/playthrough.py`: automated regression test. Plays all of level 1 at 18x speed and checks 20 rules.
- `docs/DESIGN_LOG.md`: every design decision made so far, with the reasoning. Read it before changing gameplay.
- `docs/FEATURE_SPEC_next.md`: the next planned update, including open questions that must be answered before building.
- `README.md`: setup notes for humans.

## Running and testing

- Play: open `crash-site.html` in a browser. Needs a mouse and keyboard.
- Test: `python tests/playthrough.py` (first time: `pip install playwright` then `python -m playwright install chromium`). Must print `ALL CHECKS PASSED`. Run it after every change that touches gameplay, and extend it when adding mechanics.
- The test injects a `window.__g` hook by replacing the final `})();` line of the script and speeds up the line `const dt = Math.min(.05, (t - last) / 1000);`. If you rename or move either, update the test.

## How we work (the owner's working agreement)

1. **Decisions come to the owner first.** Before building a feature, list the choices it involves, with a proposed answer for each, numbered so the owner can reply "go" or "3: change X". Don't silently decide gameplay, balance, naming, UI layout, or story. Small technical choices are fine; mention any that affect how the game plays.
2. **Bug fixes and new features ship separately.** Fix bugs in their own commit or PR, keep everything else unchanged, then do features.
3. **Small steps.** One playable change at a time. The owner playtests between steps.
4. **Keep the design log current.** When a decision is made, add it to `docs/DESIGN_LOG.md` in the same commit.
5. **Verify before reporting.** Run the playthrough test, and look at screenshots for visual changes. Report what was tested.
6. Commit with clear messages, one logical change per commit.

## Code map (inside crash-site.html)

The script is one IIFE. Main sections, in order:

- `MAP_SRC`: the level as text rows. Legend: `#` bedrock, `R` hard rock, `d` soft rock, `v` ore vein (soft), `c` crystal vein (soft), `W` anomaly (Captain's core), `.` floor, `r` rubble, `o` rubble hiding ore, `x` wreckage, `X` wreckage hiding ore, `S` start.
- Constants: `HARD` (mining seconds per wall type), `CAPT_BONUS`, `CLEAR_MULT`, `PACK_*`, `NEED_ORE`, `NEED_CRY`, `QUEUE_MAX`.
- State and helpers: `walkable`, `canMine`, `canClear`, `canHaul`, `has` (pack count), `baseOf`/`speedOf`/`workOf`/`clearOf` (stats).
- `init(free)`: builds the level, buildings (`mkBuilding`), first drone.
- Pathfinding: `dijkstra` (8-way, no corner cutting, rubble costs double). **Distances must stay Float64**: Float32 caused a rounding bug that made tunnels unreachable.
- Reveal: `revealFrom` / `revealAll` (sight spreads 11 tiles through open floor).
- Items and delivery: `spawnItem`, `accepts`, `canTake`, `defaultTarget`, `deposit`.
- Orders: `command` (right-click), `markJob` (job queue), `setTask`.
- Unit behaviour: `updateUnit` (task state machine: move, goto, mine, clear, fetch, deliver, install, uninstall, repair), `think` (auto-work: oldest-queued job the drone's mode and abilities allow), `unstack`, `separate`.
- World changes: `breakWall` (wall becomes rubble, drops buried), `clearPile` (rubble or wreckage cleared, buried items appear).
- Printer: `queuePrint`, `updatePrinter`, `finishPrint`. Promotion: `promote`.
- Tutorial: `STEPS` (message, marker target, optional progress text, done condition), `updateObjective`.
- HUD: `renderPower` (power cells, crew roster, idle/blocked counts), `renderSel` (bottom-right info panel; each building's text is built lazily so only the selected building is evaluated), `statusOf`, `focusHTML`/`wireFocus`.
- Rendering: `drawTile`, `drawPile`, `drawJob`, `drawBuilding`, `drawItem`, `drawUnit`, `drawMarker`, `draw`.
- Input, buttons, and the `frame` loop.

## Conventions

- Visible text uses typographic punctuation (’ “ ”); code uses straight quotes.
- Colours are CSS variables with light and dark values; the cave canvas stays dark in both.
- Keep it one file unless the owner agrees to split it.
- Pack colours: red `#e0483e` (mining), blue `#3d7be0` (clearing), green `#3fae5a` (gathering). Amber `#ffb547` = power and crystals. Teal `#5fe0d0` = selection and UI accents. Captain = navy `#2c3e66` with gold `#f2c14e`.
