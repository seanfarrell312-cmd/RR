# Design log

Everything decided so far, grouped by topic. Each entry is the current rule; superseded rules are listed at the end so nobody reintroduces them by accident. "Owner" means the game's designer; proposals marked *(owner approved)* came from the developer and were accepted.

## Story and concept

- You are the primary control program for a crew of robots on a big ship in space. A disaster deactivates the crew; the ship crashes on a planet and is buried.
- Drones wake up and start clearing the crash site. One drone finds the Captain's power core, installs it, and *becomes* the Captain, gaining his memories and experience. The crew were all upgraded drones: named crew members can be revived by finding their cores and installing them in drones.
- Goal across the game: wake every named crew member, repair and power the ship, and escape the caves. Each level ends when enough power is reached to warp the current section of the ship to the rest of it, slowly reassembling the ship.
- Major job types (building, computing, fighting, defending, and so on) each have at least one upgradable hero.
- The Captain's special ability: he needs no power. The player plays as him early on.
- Drones and heroes persist between levels so the player grows attached to the crew. Named crew are far stronger than drones and have much higher stat limits.
- Between levels: view progress and pick the next level. First version is linear (view progress, start next level). Later: multiple objectives and returning to earlier outposts.
- Story arc: the Captain wakes first and saves everyone. An old, wise bot is the true leader of the crew; he is found last, in the final level. Theme: meeting the moment, and the old generation entrusting the next. Everyone leaves together, until the ship crashes again in the sequel.
- The game ends when enough resources and ship components are recovered and the whole crew is found.

## Platform and process

- Original game, built from scratch. Rock Raiders is a *loose* design reference only (owner). Manic Miners (the folder originally shared) is a compiled Unreal Engine game with no source; it is not used.
- Top-down 2D, browser, single HTML file (owner).
- First playable focused on drone control feel; it grew into the full level 1.
- Working agreement: decisions listed first and approved; small playable steps; this design log; bug fixes and features deployed separately (owner).
- Working title "Crash Site" was picked by the developer as a placeholder.

## Controls (owner: "smooth and pleasant", keep)

- Left-click selects a drone or building; left-drag box-selects; Shift-click adds or removes; Q selects the whole crew; Esc clears selection.
- Right-click is contextual: floor = move; rock, rubble or wreckage = queue a job; item = pick it up; building = deliver, repair, or go there.
- Camera: WASD, arrows, screen-edge pan, middle-drag; wheel zooms. P pauses, H opens controls.
- Drones glide smoothly along tile paths and find their own way. 8-way movement without cutting corners.

## Manual vs auto control (owner, latest)

- A move order (or "go to building" order) switches the selected drones to **manual**: they stay put after arriving.
- Right-clicking a job with drones selected queues it **and** sends those drones to it immediately, switching them back to **auto-work**. Drones that can't do it (ability or pack) are returned to auto-work.
- Each drone has an Auto-work on/off button. The panel shows "Control: Manual" or "Auto-work".
- If a job is queued with nothing selected while every drone is on manual, a notice explains how to get them working.
- Replaces the old 5-second "hold position" after a move order (that hold swallowed orders and caused a bug).

## Job queue (owner)

- Right-click any wall type (soft rock, hard rock, veins, anomaly), rubble, or wreckage to queue it. Mining jobs show an amber pick with corner brackets; clearing jobs show a brown shovel. Jobs nobody can currently do (hard rock before a Captain exists) are drawn dimmed grey.
- Jobs are done **oldest first** (queue order). A drone joins a job while it still has a free side to work from (one drone per open adjacent tile).
- Queuing a job **never** pulls an unselected drone off the job it is doing.
- Right-click a queued job with nothing selected to remove it.
- When a queued wall is mined, its job becomes clearing the rubble, keeping the wall's place in the queue, so sites get finished.
- Idle auto drones check the queue immediately when a job is added.

## Work modes (owner)

- **All-round** (default): hauls loose items, then clears queued rubble, then mines queued walls. Finishes each site.
- **Mine**: only mines queued walls, walking over rubble.
- **Clear**: only clears queued rubble and wreckage.
- **Collect**: only picks up and hauls loose items.
- Drones never take jobs outside their mode. Changing a drone's mode immediately stops any job outside the new mode (owner, latest).
- Set per drone, or for a whole selection at once, in the info panel. With a pack fitted, the selected mode button takes the pack's colour.

## Blocked and idle (owner)

- A drone with nothing it can do, while jobs or items it *can't* handle (ability, pack, or unreachable) are waiting, is **blocked**: a yellow warning triangle with "!" over its head until it gets an order or finds a job it can do.
- Under the power cells: "N idle" and "N blocked" buttons; clicking selects those drones. "All crew working" otherwise.

## Power and units

- Power capacity = 1 (command center) + 1 per crystal stored in the power plant. Each active drone uses 1 power cell.
- The Captain uses 0 power, mines and moves 25% faster than a drone, and works like any drone (owner).
- Only the Captain can mine hard rock (owner). Drones mine soft rock and veins.
- The Captain is just named "Captain" on promotion; renaming him later shows "Newname (Captain)" (owner).
- New drones get a random name from a list; the player can rename at printing and later (owner liked random names; next update changes the generator, see spec).

## Mining, rubble and drops

- Mining time at 100% speed: soft rock 12 s, ore vein 15 s, crystal vein 15 s, anomaly 18 s, hard rock 24 s (about 19 s for the Captain). Owner wanted mining slow so queueing and watching matters; numbers set by the developer to reach the 20–30 minute tutorial goal.
- Every mined wall leaves **rubble** (owner, Rock Raiders style). Drops stay buried until the rubble is cleared. Rubble clears at 2x the drone's mining speed (owner) and can be walked over at half speed (path cost doubled).
- Crash **wreckage** is solid (blocks movement), clears like soft-rock rubble, and sometimes hides ore.
- The level starts with 13 rubble piles; about a third hide ore. Half of the wreckage piles hide ore (owner: rubble on the ground at the start so players clear it).
- Drops: soft rock 1 ore about 1 time in 5; ore vein 2 ore; crystal vein 1 crystal; hard rock 1 ore always (owner liked); anomaly = Captain's core + 2 crystals.
- Ore veins are visible as blue flecks in soft rock; crystal veins glow amber (owner).
- Only two kinds of resource item: ore and crystals (owner; scrap as a third resource was rejected).

## Hauling and delivery

- Crystals go to the power plant; ore and packs to the command center; the core to the command center.
- Once the main terminal is discovered, ore and crystals go to it until its needs are met.
- A drone left holding an item delivers it on its own.
- Drones with a mining pack can't haul.

## Buildings (current level 1)

- **Command center**: supplies 1 power, stores ore and packs, fits packs to drones, accepts the power core.
- **Drone printer**: prints drones and upgrade packs from one queue of up to 5 orders, worked in order. A drone order waits for a free power cell; a pack order waits until the command center has 3 ore (cost is taken when printing starts). Click a queued order to remove it. Info panel is in three sections: top (power in use, ore, now printing, queue), middle (drones: cost, how many can deploy now), bottom (packs: cost, ore available, what each does) (owner).
- **Power plant**: stores crystals; each adds a power cell.
- **Main terminal**: needs 12 ore and 2 crystals delivered, then a repair (crew right-clicks it). Progress shows as two centred bars on the building and exact counts in its panel (owner).

## Upgrade packs (owner)

- Three packs, printed at the drone printer for 3 ore each: **red Mining** (mining speed x2, can't haul), **blue Clearing** (clearing speed x2, can't mine), **green Gathering** (move speed +50%, can't clear). Trade-offs proposed by the developer.
- Packs are items the same size as ore and crystals, coloured squares; they can be carried like other items.
- Fitting: select a drone, press Upgrade, pick a pack stored in the command center; the drone walks there and fits it (1.5 s). Click a fitted slot to send the drone back to remove it. Fitting a pack switches the drone to that pack's mode.
- Drones have 1 slot; the Captain has 3. Each extra pack of the same colour adds another +100% (or +50% move for green).
- A drone's packs show as coloured squares after its name everywhere (map label, panel, roster tooltip) and as small marks on its body.
- Promoting a drone that holds packs drops them on the ground; drones haul them back (owner confirmed this works well).
- Later: extra slots bought at the printer.

## Promotion

- After the core is installed, select a drone and press "Promote to Captain". The drone flashes and grows into the Captain's navy-and-gold design; a card shows power use 1 to 0, mining and move speed 100% to 125%, and a power cell visibly frees up. This is one of the game's hooks and must feel rewarding (owner).
- Later: rework the card into a story-heavy moment (a more sentient character revived; the story begins) (owner).

## HUD

- Top left: power meter. Each lit cell is a drone; click to select, Shift-click to add, double-click to centre the camera, hover for a small window with name, packs and current task. The Captain has a navy-and-gold badge in matching colours (owner). Idle/blocked counts below.
- Top right: ore, crystals stored, time, Pause, Controls.
- Bottom left: tutorial objective panel ("Core OS") with step number, message, and a progress line (e.g. "Crystals stored: 1 of 2") (owner asked for clearer crystal progress).
- Bottom right: info panel for the selected drone, group or building. It must show the selected object's own content and change as the player selects different things (owner).
- Level complete card: title, short text, time, Play again. No crew list (owner, latest).

## Level 1 (current version, to be reworked by the next spec)

- Map 48 x 34 tiles. Start tunnel (visible from the start), wreck cavern with command center, printer and power plant, first crystal vein behind soft rock to the east, second crystal vein deep north behind 6 soft rock blocks, south route through wreckage and a long soft-rock tunnel to the anomaly, then 2 hard rock blocks to the hidden terminal cavern (5 ore veins, 3 crystal veins).
- 12 tutorial steps: walk in, mine the first crystal, print a drone, mine the second crystal, print a third, dig to the anomaly, deliver the core, promote, print to 5 drones plus Captain, break through to the terminal, deliver 12 ore and 2 crystals, repair.
- Start with 1 drone; end with 5 drones plus the Captain (owner's original requirement; next spec raises the cap).
- A perfect scripted run takes about 11 minutes of game time; real play is expected around 18 to 25.

## Backlog (agreed, not built)

- Next update: see `docs/FEATURE_SPEC_next.md` (new level flow, Build menu, deployer, bigger fleet, name generator).
- Drones resizing so several can work one wall face without overlapping (owner).
- Tutorial message rewrite (owner: current wording is weak).
- Story-heavy promotion moment.
- Between-level progress screen showing the ship being reassembled.
- Balance: pack cost, ore in early piles, ore routing once the terminal is found.
- Extra pack slots at the printer.

## Superseded (do not reintroduce)

- Nearest-job-first auto-work (replaced by oldest-first; caused drones to ignore marked wreckage).
- Mining with no rubble, and the earlier version where mining auto-cleared its own debris.
- Default mode named "Clear" meaning all-rounder (now "All-round"; "Clear" means clearing only).
- 5-second hold after move orders.
- Shift + right-click as "mark only" (all marking queues now).
- Pip-style ore and crystal counters on the terminal building (replaced by two centred bars).
- Crew list on the level complete card.
