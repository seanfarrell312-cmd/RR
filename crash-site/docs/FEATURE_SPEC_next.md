# Next update: the base-building level flow

Status: **specified by the owner; open questions answered (owner approved all proposals, 2026-10-23). Being built in the steps listed below.** The bug-fix deployment that preceded this spec is done and live.

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
- Hauling ore to a construction frame is auto-work, with the same priority as hauling loose items, in All-round and Collect modes.

## Build steps (one playable change each; owner playtests between)

1. Name generator and the 20-crew fleet cap.
2. New start: command center and power plant (1 crystal stored, 2 cells per crystal), 3 drones, printer rebuilt at a wreck frame from floor-debris ore; tutorial steps for the new opening.
3. Build menu, placement ghost, construction frame and hauling; the deployer.
4. Deployer behaviour (drones appear there, crew list) and its tutorial step.
5. Bigger map with more veins, then pacing and balance pass.

## Acceptance checks to add to tests/playthrough.py

- Level starts with the command center and power plant only, and 3 drones.
- Ore from floor debris reaches the command center; the printer gets built from it.
- Build menu opens, the deployer ghost is red over walls, rubble, wreckage and buildings, and green on clear 4 x 4 floor.
- Placing the deployer creates a frame; drones haul ore to it; it completes.
- Fleet never exceeds 20 including the Captain.
- The rest of the level (core, promotion, terminal) still completes.
