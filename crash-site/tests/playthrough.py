"""
Automated playthrough of level 1 (tutorial mode).

Builds a temporary test copy of crash-site.html with:
  - a window.__g hook exposing game internals
  - the game clock sped up 18x
then plays the whole level the way a player would (marking jobs, printing,
fitting a pack, promoting) and checks key rules along the way.

Usage:
  pip install playwright
  python -m playwright install chromium
  python tests/playthrough.py

Exit code 0 = level won with no page errors and all checks passed.
"""
import pathlib, sys, time
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "crash-site.html"
TEST = ROOT / "tests" / "_test_build.html"

HOOK = ('window.__g={get units(){return units},get items(){return items},B,command,printDrone,queuePrint,promote,addUnit,capacity,'
        'setTask,ringTiles,get jobs(){return jobs},get step(){return step},idx,closeName,get mode(){return mode},'
        'discovered,get revealed(){return revealed},get pile(){return pile}};})();')

def build_test_copy():
    html = SRC.read_text(encoding="utf-8")
    lines = html.split("\n")
    # the game's closing IIFE line is exactly "})();"
    end = max(i for i, l in enumerate(lines) if l.strip() == "})();")
    lines[end] = HOOK
    html = "\n".join(lines)
    old = "const dt = Math.min(.05, (t - last) / 1000);"
    assert old in html, "frame-loop dt line changed; update tests/playthrough.py"
    html = html.replace(old, "const dt = Math.min(.3, (t - last) / 1000 * 18);")
    TEST.write_text(html, encoding="utf-8")

failures = []
def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok: failures.append(name)

def main():
    build_test_copy()
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1280, "height": 800})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(TEST.as_uri()); pg.wait_for_timeout(300); pg.click("#startTut")
        ev = pg.evaluate
        val = lambda c: ev("()=>{const g=window.__g; return (" + c + ");}")
        def sel(expr): ev("()=>{const g=window.__g; g.units.forEach((u,k)=>u.sel=(" + expr + "));}")
        def cmd(x, y): ev(f"()=>{{const g=window.__g; g.command(({x}+.5)*32,({y}+.5)*32,false);}}")
        def dismiss(): ev('()=>{ if(document.getElementById("nameOv").classList.contains("show")) window.__g.closeName(); if(document.getElementById("promoOv").classList.contains("show")) document.getElementById("promoOk").click(); }')
        def waitfor(cond, limit=60, label="", marks=None):
            t0 = time.time(); marks = list(marks or [])
            while time.time() - t0 < limit:
                rest = []
                for (x, y) in marks:
                    if val(f"g.revealed[g.idx({x},{y})]"): sel("false"); cmd(x, y)
                    else: rest.append((x, y))
                marks = rest
                if val("!!(" + cond + ")"): return True
                dismiss(); pg.wait_for_timeout(150)
            print("TIMEOUT", label, "tutorial step", val("g.step")); return False

        check("level starts with rubble piles", val("Array.from(g.pile).filter(v=>v===1).length") >= 10)
        check("level starts with 3 drones, 2 of them powered down", val("g.units.length") == 3 and val("g.units.filter(u=>u.dormant).length") == 2)
        check("power plant starts with 1 crystal: 3 power cells", val('g.B("plant").crystals') == 1 and val("g.capacity()") == 3)
        check("printer starts as a frame needing 8 ore", val('g.B("printer").frame && g.B("printer").frame.need') == 8)
        sel("k===0"); cmd(13, 17); check("walk down the start tunnel", waitfor("g.step>=1", 20, "walk"))
        check("powered-down drones wake when the clearing is found", waitfor("g.units.every(u=>!u.dormant)", 10, "wake"))
        cmd(20, 17); waitfor("!g.units[0].path.length", 20, "walk2")
        check("move order switches the drone to manual", val("g.units[0].auto") is False)
        cmd(19, 13)  # drone still selected: direct job order on ore-hiding rubble
        check("selected drone + right-click debris starts clearing", val("g.units[0].task && g.units[0].task.t") == "clear")
        check("a job order switches the drone back to auto-work", val("g.units[0].auto") is True)
        sel("false")
        check("printer frame receives ore hauled from the command center", waitfor('g.B("printer").frame && g.B("printer").frame.ore>=1', 120, "frame ore", marks=[(24, 14), (23, 20), (18, 21), (13, 15), (3, 16)]))
        check("printer rebuilt", waitfor('!g.B("printer").frame', 200, "printer", marks=[(10, 17)]))
        check("first crystal stored", waitfor('g.B("plant").crystals>=2', 120, "crystal1", marks=[(27, 15), (28, 15)]))
        check("one crystal adds two power cells", val("g.capacity()") == 5)
        cmd(20, 11); waitfor('g.units.some(u=>u.task && u.task.t==="mine" && u.task.i===g.idx(20,11))', 30, "start mine")
        busy = val('g.units.findIndex(u=>u.task && u.task.t==="mine" && u.task.i===g.idx(20,11))')
        cmd(16, 14); pg.wait_for_timeout(300)
        check("busy drone keeps its job when a new job is queued", busy >= 0 and val(f"g.units[{busy}].task && g.units[{busy}].task.i") == val("g.idx(20,11)"))
        cmd(20, 11)  # remove the north job again: it's optional now
        ev("()=>{window.__g.printDrone(); window.__g.printDrone();}")
        check("print two drones: five in all", waitfor("g.units.length>=5", 30, "print to 5")); dismiss()
        ev('()=>window.__g.queuePrint("red")')
        check("Captain's core delivered", waitfor('g.B("cc").core===true', 300, "core", marks=[(20, 24), (20, 25), (20, 26), (20, 27), (21, 28), (22, 28), (24, 28), (25, 28), (26, 28), (27, 28), (28, 28), (30, 28), (31, 28), (34, 28)]))
        check("mining pack printed and stored", waitfor('g.B("cc").packs.red>=1', 120, "red pack", marks=[(29, 28), (15, 18), (21, 18)]))
        ev('()=>{const g=window.__g; const u=g.units[2]; g.setTask(u,{t:"install",color:"red"},g.ringTiles(g.B("cc")));}')
        check("pack fitted", waitfor('g.units[2].packs.includes("red")', 40, "install"))
        check("mining pack sets Mine mode", val("g.units[2].focus") == "mine")
        ev("()=>window.__g.promote(window.__g.units[2])"); pg.wait_for_timeout(600); dismiss()
        check("promoted drone is named Captain", val("g.units[2].name") == "Captain")
        check("promotion drops the pack", val('g.items.filter(i=>i.type==="red").length + g.units.filter(u=>u.carry==="red").length + g.B("cc").packs.red') >= 1)
        check("anomaly crystals stored", waitfor('g.B("plant").crystals>=4', 90, "anomaly crystals"))
        for _ in range(4): ev("()=>window.__g.printDrone()")
        check("eight drones plus the Captain", waitfor("g.units.filter(u=>!u.captain).length>=8", 60, "print to 8")); dismiss()
        names = val('g.units.map(u=>u.name).filter(n=>n!=="Bolt"&&n!=="Captain")')
        check("printed drones get unique consonant-vowel-consonant names", len(names) >= 4 and len(set(names)) == len(names) and all(len(n) == 3 and n[0].isupper() and n[1] in "aeiou" and n[2].islower() and n[2] not in "aeiou" for n in names))
        check("terminal discovered", waitfor('g.discovered(g.B("terminal"))', 150, "terminal", marks=[(35, 28), (35, 27)]))
        veins = [(36, 22), (36, 24), (38, 20), (42, 20), (45, 22), (45, 24), (42, 26), (39, 27), (44, 21), (44, 25), (37, 21), (43, 20)]
        check("terminal materials delivered", waitfor('g.B("terminal").ore>=12 && g.B("terminal").crystal>=2', 260, "materials", marks=veins))
        sel("true"); cmd(40, 23)
        check("level won", waitfor('g.mode==="won"', 60, "win"))
        ev('()=>{const g=window.__g; g.B("plant").crystals=40; g.B("printer").queue.length=0; while(g.units.length<19) g.addUnit("Tst",20,17);}')
        for _ in range(3): ev('()=>window.__g.queuePrint("drone")')
        check("printer won't queue past 20 crew including the Captain", val('g.B("printer").queue.filter(k=>k==="drone").length') == 1)
        check("no page errors", not errs)
        if errs: print("\n".join(errs))
        b.close()
    TEST.unlink(missing_ok=True)
    print("\nALL CHECKS PASSED" if not failures else f"\n{len(failures)} CHECK(S) FAILED")
    sys.exit(1 if failures else 0)

if __name__ == "__main__":
    main()
