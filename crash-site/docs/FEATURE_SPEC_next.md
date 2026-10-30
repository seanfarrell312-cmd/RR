# Next update: the base-building level flow

Status: **specified by the owner; open questions answered (owner approved all proposals, 2026-10-23), playtest changes decided (2026-10-30). Being built in the steps listed below.** The bug-fix deployment that preceded this spec is done and live.

## Why

The owner wants the first level to feel like the start of a base-building and automation game: a barren site you populate and grow. Mining is now slow enough that the player needs something to do while drones grind, and the fleet should grow large. Resource philosophy, in the owner's words: **crystals let you create new drones and buildings; ore lets you use them better.**

## 1. Fleet size and names

- Maximum fleet in level 1: **20 including the Captain**.
- The map needs many more crystal and ore veins to support that many drones.
- Name generator: names follow a **consonant, vowel, consonant** pattern. They don't need to make sense. The owner described them as "3 syllable" names; see open question 1.
- A created and named drone is part of the team permanently (persists across levels later).

## 2. New level 1 flow

1. **Start**: unchanged. One drone the player steers down the start tunnel.
2. **The clearing**: the player discovers **only two buildings, the command center and the power plant**, plus **two more drones already deployed and named**. (The printer is no longer there at the start.)
3. **Build the printer**: the new little fleet must find enough ore to construct the printer. The **debris on the floor** (rubble and wreckage) is the first target for ore. Then the player is guided to mine walls. This is the first "slow" part of the game: queue jobs and watch the fleet work.
4. **Deploy**: once the printer exists, the player starts printing more drones.
5. **Build the deployer**: after the printer is up and a few more drones exist, the player is told to build the **deployer** using ore gathered from the walls (details in section 3). The player must clear debris in the initial site to make room for it.
6. **Then** the tutorial continues with the search for the Captain's core. **The rest of the tutorial stays as it is.**

## 3. Build menu, placement and construction

- A **Build** button sits at the top of the window, just to the right of the Power window.
- Clicking it opens a simple **drop-down list** of available buildings (the deployer for now).
- After choosing a building, the cursor shows its footprint highlighted **green** where it can be placed and **red** where it can't, like other RTS games.
- **Deployer footprint: 4 x 4 tiles.** It can't overlap walls, rubble, wreckage, or other buildings, so the player has to clear space in the starting site.
- Placing it creates a **square frame** (construction site). Drones carry **ore from the command center's storage** to the frame until the building's requirements are met. Then the building appears in that spot.
- The system should be general enough for future buildings.

## 4. The deployer

- Purpose in later levels: **recall drones you've already created and upgraded** to a new map without reprinting them, so the team carries over.
- In level 1 it establishes how the player will maintain their team in future levels (see open question 4 for what it does here).

## 5. The feel the owner is after

Set mining tasks, deploy more workers, gradually specialise some with packs to speed up mining and gathering, find the Captain's core, and unlock an already-specialised unit who breaks through hard rock. The player should feel satisfaction watching the drone army grow and tackle what they mark, and the base slowly grow. When the Captain arrives, work gets done visibly more efficiently.

## Decisions (owner approved, 2026-10-23)

1. **Names**: one syllable, consonant-vowel-consonant (e.g. “Tav”, “Bok”, “Rix”), random, never repeating a current crew name. They fit map labels and the roster with 20 on screen. Named story crew can get longer hand-written names later.
2. **Building costs**: ore only, hauled from the command center. Crystals stay in the power plant, so “crystals create” works through power (how many drones you can run). Starting costs: printer 8 ore, deployer 12 ore, tuned so the debris-clearing opening lasts about 3 to 5 minutes.
3. **The printer** is rebuilt at a fixed wreck site the player supplies with ore, using the same frame-and-haul code as placed buildings. The deployer is the first building placed freely with the Build menu.
4. **The deployer in level 1**: once built, newly printed drones appear at it, and its panel lists the whole crew.
5. **Map** grows moderately, from 48 x 34 to about 64 x 44, with more crystal and ore veins, so 20 drones aren’t crowding the same faces and the slow middle has enough walls.
6. **Power**: each stored crystal adds **2** power cells (command center still 1). About 9 crystals power 19 drones; the map needs roughly 6 to 8 crystal veins.
7. **Pre-deployed drones** count toward power. The power plant starts with 1 crystal stored: 1 + 2 = 3 cells for the 3 starting drones, and the first mined crystal opens room to print.
8. **Pacing**: target 25 to 35 minutes of real play; a perfect scripted run about 15 to 17 minutes.

Technical choices that affect play (owner accepted with the above):
- Rubble, wreckage, buildings and walls block a building footprint. Drones and items standing in it don’t; drones step out once the frame is placed.
- Hauling ore to a construction frame is auto-work, with the same priority as hauling loose items, in All-round and Collect modes. (Changed 2026-10-30: only once the player starts the build with a construct job; see playtest decision 6.)

## Build steps (one playable change each; owner playtests between)

1. Name generator and the 20-crew fleet cap. **Done.**
2. **Done.** New start: command center and power plant (1 crystal stored, 2 cells per crystal), 3 drones, printer rebuilt at a wreck frame from floor-debris ore; tutorial steps for the new opening.
2a. **Done.** Playtest decisions A: no naming pop-up, quick-succession printing.
2b. Playtest decisions B: construct job; building only when the player starts it.
2c. Playtest decisions C: fog of war.
2d. Playtest decisions D: several drones per wall.
3. Build menu, placement ghost, construction frame (started with a construct job); the deployer.
4. Deployer behaviour (drones appear there, crew list) and its tutorial step.
5. Bigger map with more veins, then pacing and balance pass.

## Playtest decisions (owner approved all proposals, 2026-10-30)

The owner playtested step 2 and asked for five changes: building only when the player says so, several drones per wall, a stricter fog of war, no naming pop-up, and quick-succession printing. They were turned into these decisions, built in steps 2a to 2d before the Build menu.

**A. Printing**
1. No naming pop-up. A printed drone appears with its generated name and a short message (“Tov printed.”). The game never pauses for it. (The pop-up paused the game, which made printing feel slow.)
2. Renaming stays on the Rename button in the drone’s info panel (bottom right), which opens the same small name box; Enter or Esc closes it.
3. Clicking Print drone several times queues one drone per free power cell, counting drones already queued. A click beyond that gives “No free power cell. Store more crystals in the power plant.” (Before, extra drones joined the queue and waited.)
4. Print time stays 3 seconds per drone; drones and packs still share the 5-order queue.

**B. Building starts when the player says so**
5. Ore always goes to the command center first. No drone takes ore to a frame until the player starts building it.
6. The player starts building by right-clicking the frame, or pressing Start building in its panel. Either adds a **construct** job to the job queue; selected drones go straight to it, as with mining jobs.
7. Construct jobs are worked like any queued job, oldest first, by up to 3 drones at once. Each does round trips carrying 1 ore at a time from the command center until the frame is finished.
8. All-round and Collect modes take construct jobs. Drones with a Mining pack can’t (they can’t carry items).
9. With no ore in the command center the job stays queued, the frame shows “Waiting for ore”, and drones work on other jobs meanwhile. Ore isn’t reserved: construction and pack printing take whatever ore is there, first come first served.
10. Cancelling: right-click the job with nothing selected, like any other job. Ore already delivered stays in the frame.
11. Tutorial: a short new step after the debris step, “Right-click the printer frame to start rebuilding it.” Final wording goes to the owner before it’s built.

**C. Fog of war**
12. Walls show 2 deep from any visible open floor, veins included.
13. Open floor behind walls stays hidden until it’s connected to open space the crew can reach, even inside that 2-deep band.
14. Drone sight stays 11 tiles through connected open floor (revealing whole caverns at once would show the clearing from the first second).
15. A visible second-row wall can be queued; drones start on it once the wall in front is mined.

**D. Several drones per wall**
16. Up to 4 drones per wall or rubble pile. Each open side gets work spots in a small 2 x 2 group on the floor in front of it, so even a wall at the end of a 1-tile tunnel takes 4. Drones still path tile to tile but no longer claim a whole tile.
17. Drones shrink to about 75% of their size so 2 fit side by side without overlapping; the Captain shrinks by the same amount. (Covers the drone-resizing backlog item.)
18. Speeds add up: 4 drones mine a wall 4 times as fast (soft rock 12 s to 3 s). Pacing is tuned in step 5; the map growth to about 64 x 44 stays in step 5.

## Acceptance checks to add to tests/playthrough.py

- Level starts with the command center and power plant only, and 3 drones.
- Ore from floor debris reaches the command center; the printer gets built from it.
- Build menu opens, the deployer ghost is red over walls, rubble, wreckage and buildings, and green on clear 4 x 4 floor.
- Placing the deployer creates a frame; drones haul ore to it; it completes.
- Fleet never exceeds 20 including the Captain.
- The rest of the level (core, promotion, terminal) still completes.
