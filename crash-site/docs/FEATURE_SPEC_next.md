# Next update: the base-building level flow

Status: **specified by the owner, not built.** The open questions at the bottom must be answered by the owner before implementation (see the working agreement in CLAUDE.md). The bug-fix deployment that preceded this spec is done and live.

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

## Open questions for the owner (answer before building)

1. **Names.** Three-letter names like "Tav" or "Bok" (one consonant-vowel-consonant syllable), or longer names built from three such syllables, like "Baktunim"?
2. **Building costs.** Given "crystals create, ore improves": should the printer and deployer cost crystals, ore, or both? The flow above has drones hauling ore from the command center to the frame. If crystals are involved, do they come out of the power plant (lowering power capacity) or from a separate stock?
3. **The printer.** Is it placed with the same Build menu as the deployer, or rebuilt at a fixed wreck site the player supplies with ore, leaving the deployer as the first building placed freely?
4. **The deployer in level 1.** Does it need to do anything here beyond being built (for example, become where new drones appear, or list the crew)?
5. **Map.** With up to 19 power cells needed, should the map grow, or keep its size with richer veins?
6. **Power for 20.** Should crystals keep adding 1 power cell each, or should each crystal add more so 20 drones doesn't need 19 crystal veins?
7. **Pre-deployed drones.** Do the two drones in the clearing count toward power (so the player starts needing 3 power cells), and does the command center supply enough for them?
8. **Tutorial pacing targets.** Is 20–30 minutes still the target with the longer flow?

## Acceptance checks to add to tests/playthrough.py

- Level starts with the command center and power plant only, and 3 drones.
- Ore from floor debris reaches the command center; the printer gets built from it.
- Build menu opens, the deployer ghost is red over walls, rubble, wreckage and buildings, and green on clear 4 x 4 floor.
- Placing the deployer creates a frame; drones haul ore to it; it completes.
- Fleet never exceeds 20 including the Captain.
- The rest of the level (core, promotion, terminal) still completes.
