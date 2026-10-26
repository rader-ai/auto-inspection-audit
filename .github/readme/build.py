"""Build the README visuals for vehicle-inspection-audit.

Run from the repo root:  python3 .github/readme/build.py
Writes light/dark x wide/narrow SVGs to .github/assets/.

Look: a service-bay instrument panel, matching the skill's visual report
(graphite band, signal lamps, segmented decision meter). Every item and number
comes from one real audit: a 2001 Ram 2500 Tekmetric inspection (Oct 2026),
anonymized. Elements are written in their finished state; animations only
describe how they get there.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import svgkit as sk  # noqa: E402
from svgkit import esc, SANS, MONO  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parents[1] / "assets"

THEMES = {
    "light": dict(
        bg="#EEF1F4", panel="#FFFFFF", ink="#101A23", muted="#566573", faint="#C3CCD4", row="#E6EBEF",
        band="#0F1C27", band2="#172937", bandink="#F1F5F8", bandmuted="#94A7B7", bandrule="#2A3C4B",
        brand="#E39A2B", now="#C8263A", go="#11815A", ask="#B97700", skip="#6F7E8B", off="#D3DAE0",
        nowS="#FBE8EA", goS="#E3F3EC", askS="#FCF1DC", skipS="#E9EDF1",
    ),
    "dark": dict(
        bg="#0B1218", panel="#121C25", ink="#E9EEF2", muted="#94A6B5", faint="#2D3B47", row="#172330",
        band="#0A141C", band2="#14232F", bandink="#F1F5F8", bandmuted="#8A9DAD", bandrule="#243644",
        brand="#F0A33A", now="#FF6B78", go="#4FD29A", ask="#F2B544", skip="#9EACB8", off="#2A3743",
        nowS="#34171C", goS="#10291F", askS="#33270E", skipS="#1C2630",
    ),
}
# Signal colours on the dark band, the same in both themes.
BAND_SIG = dict(now="#FF5A69", go="#3FCF8E", ask="#F5B53D", skip="#8FA1B0", red="#FF5A69", yellow="#F5B53D")
LABEL = dict(now="Fix now", go="Approve", ask="Ask first", skip="Skip / defer")


def doc(w, h, title, desc, style, body, bg):
    return sk.svg_doc(w, h, title, desc, f".s {{ font-family: {SANS}; }} .m {{ font-family: {MONO}; }}" + style, body, bg=bg)


# ---------------------------------------------------------------- hero
ROWS = [  # shop item (as the shop named it), shop grade, our call
    ("Front brake system: line leaking", "red", "now"),
    ("Replace calipers + master cylinder", "red", "ask"),
    ("Brake fluid reservoir empty", "red", "now"),
    ("Trac bar + tie rod end play", "yellow", "go"),
    ("Diff & transfer case service", "yellow", "ask"),
    ("Engine air filter", "red", "ask"),
    ("Coolant: “3 years or 30k”", "yellow", "skip"),
    ("Right taillight lens", "yellow", "go"),
]


def hero(c, size="wide"):
    wide = size == "wide"
    if wide:
        W, H = 1280, 540
        px, py, pw = 640, 56, 576           # panel
        tx, ty = 64, 96                     # text block
        title_size, body_y, chips_y = 44, 318, 382
    else:
        W, H = 640, 920
        px, py, pw = 28, 440, 584
        tx, ty = 36, 64
        title_size, body_y, chips_y = 40, 262, 318
    CYCLE, SCAN_END = 13, 58
    head_h, rh, step = 44, 34, 40
    r0 = py + head_h + 12
    n = len(ROWS)
    rows_end = r0 + n * step
    meter_y = rows_end + 18
    ph = meter_y + 52 - py
    sig = BAND_SIG

    style = [f"""
.scan {{ animation: scan {CYCLE}s linear infinite both; }}
@keyframes scan {{ 0% {{ transform: translateY(0); opacity: 0; }} 3% {{ opacity: 1; }}
  {SCAN_END}% {{ transform: translateY({n * step}px); opacity: 1; }} {SCAN_END + 4}%,100% {{ transform: translateY({n * step}px); opacity: 0; }} }}
"""]
    body = [f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="12" fill="{c["band2"]}"/>',
            f'<text class="s" x="{px + 20}" y="{py + 28}" font-size="14" font-weight="600" fill="{c["bandmuted"]}">Shop’s inspection</text>',
            f'<text class="s" x="{px + pw - 20}" y="{py + 28}" font-size="14" font-weight="600" text-anchor="end" fill="{c["bandmuted"]}">Our call</text>',
            f'<line x1="{px}" y1="{py + head_h}" x2="{px + pw}" y2="{py + head_h}" stroke="{c["bandrule"]}"/>']
    chip_w = 104
    label_max = pw - 20 - 30 - chip_w - 24
    meter_x, meter_w = px + 20, pw - 40
    seg_w = (meter_w - (n - 1) * 4) / n
    for i, (label, grade, call) in enumerate(ROWS):
        y = r0 + i * step
        hit = 3 + (SCAN_END - 3) * (i + 0.5) / n
        a, b = hit, hit + 2.5
        style.append(sk.reveal(f"v{i}", CYCLE, a, 95, fade=2.5))
        lab = sk.fit(label, 15, label_max, "sans")
        cx = px + pw - 20 - chip_w
        body.append(
            f'<circle cx="{px + 28}" cy="{y + rh / 2}" r="5.5" fill="{sig[grade]}"/>'
            f'<circle cx="{px + 28}" cy="{y + rh / 2}" r="9" fill="none" stroke="{sig[grade]}" stroke-opacity=".3" stroke-width="3"/>'
            f'<text class="s" x="{px + 48}" y="{y + rh / 2 + 5}" font-size="15" fill="{c["bandink"]}">{esc(lab)}</text>'
            f'<g class="v{i}"><rect x="{cx}" y="{y + 5}" width="{chip_w}" height="{rh - 10}" rx="{(rh - 10) / 2}" fill="{sig[call]}" fill-opacity=".16"/>'
            f'<text class="s" x="{cx + chip_w / 2}" y="{y + rh / 2 + 5}" font-size="13.5" font-weight="700" text-anchor="middle" fill="{sig[call]}">{LABEL[call]}</text></g>')
        # the meter segment for this row lights at the same moment
        sx = meter_x + i * (seg_w + 4)
        style.append(sk.reveal(f"g{i}", CYCLE, a, 95, fade=2.5))
        body.append(f'<rect x="{sx:.1f}" y="{meter_y}" width="{seg_w:.1f}" height="12" rx="2" fill="{c["bandrule"]}"/>'
                    f'<rect class="g{i}" x="{sx:.1f}" y="{meter_y}" width="{seg_w:.1f}" height="12" rx="2" fill="{sig[call]}"/>')
    body.append(f'<text class="s" x="{meter_x}" y="{meter_y + 36}" font-size="13" fill="{c["bandmuted"]}">Decision meter: one segment per item</text>')
    body.append(f'<g class="scan"><rect x="{px + 8}" y="{r0 - 6}" width="{pw - 16}" height="2" fill="{c["brand"]}"/>'
                f'<rect x="{px + 8}" y="{r0 - 14}" width="{pw - 16}" height="10" fill="{c["brand"]}" fill-opacity=".14"/></g>')

    # text block
    body.append(f'<rect x="0" y="0" width="{W}" height="5" fill="{c["brand"]}"/>')
    body.append(f'<text class="s" x="{tx}" y="{ty}" font-size="15" font-weight="600" fill="{c["bandmuted"]}">vehicle-inspection-audit · an Agent Skill for Claude</text>')
    for k, (ln, col) in enumerate([("Every red and yellow,", c["bandink"]), ("checked against", c["brand"]), ("the evidence.", c["brand"])]):
        body.append(f'<text class="s" x="{tx - 2}" y="{ty + 56 + k * (title_size + 10)}" font-size="{title_size}" font-weight="800" fill="{col}">{ln}</text>')
    lines = (["For drivers checking what a shop recommends, and",
              "shop owners checking what their technicians wrote."] if wide else
             ["For drivers checking what a shop recommends,",
              "and shop owners checking their technicians."])
    for k, ln in enumerate(lines):
        body.append(f'<text class="s" x="{tx}" y="{body_y + 26 * k}" font-size="17" fill="{c["bandmuted"]}">{esc(ln)}</text>')
    x = tx
    for chip in ["Claude.ai", "Claude Code", "50 states + DC", "Tekmetric · Mitchell 1 · more"]:
        w = sk.text_width(chip, 14, "sans") + 30
        if x + w > (px - 24 if wide else W - tx):
            x, chips_y = tx, chips_y + 42
        body.append(f'<rect x="{x}" y="{chips_y}" width="{w:.0f}" height="32" rx="16" fill="none" stroke="{c["bandrule"]}" stroke-width="1.5"/>'
                    f'<text class="s" x="{x + w / 2:.0f}" y="{chips_y + 21}" font-size="14" text-anchor="middle" fill="{c["bandink"]}">{esc(chip)}</text>')
        x += w + 10
    return doc(W, H, "vehicle-inspection-audit",
               "A shop's inspection list with red and yellow grades. A scan line moves down it and each item gets "
               "an evidence-based call: Fix now, Approve, Ask first, or Skip, while a decision meter fills.",
               "".join(style), "\n".join(body), c["band"])


# ---------------------------------------------------------------- proof
BUCKETS = [("now", 2), ("go", 4), ("ask", 5), ("skip", 5)]


def proof(c, size="wide"):
    wide = size == "wide"
    W, H = (1280, 380) if wide else (640, 900)
    CYCLE = 12
    style, body = [sk.loop_fade("all", CYCLE, 2, 90, 97)], []
    body.append(f'<g class="all">')
    body.append(f'<text class="s" x="48" y="62" font-size="28" font-weight="800" fill="{c["ink"]}">One real inspection, audited</text>')
    sub = "2001 Ram 2500 · Tekmetric report · Oct 2026" if not wide else \
        "2001 Ram 2500 · Tekmetric report · Oct 2026 · one case, not a benchmark"
    body.append(f'<text class="s" x="48" y="92" font-size="16" fill="{c["muted"]}">{esc(sub)}</text>')
    if not wide:
        body.append(f'<text class="s" x="48" y="116" font-size="16" fill="{c["muted"]}">One case, not a benchmark</text>')

    # panel positions
    if wide:
        panels = [(48, 128, 560, 212), (632, 128, 290, 212), (946, 128, 286, 212)]
    else:
        panels = [(32, 148, 576, 250), (32, 418, 576, 220), (32, 658, 576, 220)]
    for (x, y, w, h) in panels:
        body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c["panel"]}" stroke="{c["faint"]}"/>')

    # 1. decision meter, 16 segments
    x, y, w, h = panels[0]
    body.append(f'<text class="s" x="{x + 24}" y="{y + 36}" font-size="16" font-weight="700" fill="{c["ink"]}">16 shop items, sorted by what to do</text>')
    total = sum(n for _, n in BUCKETS)
    sw = (w - 48 - (total - 1) * 4) / total
    k = 0
    for key, n in BUCKETS:
        for _ in range(n):
            on = 6 + 22 * k / total
            style.append(sk.reveal(f"m{k}", CYCLE, on, 100, fade=1.5))
            sx = x + 24 + k * (sw + 4)
            body.append(f'<rect x="{sx:.1f}" y="{y + 60}" width="{sw:.1f}" height="22" rx="3" fill="{c["off"]}"/>'
                        f'<rect class="m{k}" x="{sx:.1f}" y="{y + 60}" width="{sw:.1f}" height="22" rx="3" fill="{c[key]}"/>')
            k += 1
    lx, ly = x + 24, y + 128
    for j, (key, n) in enumerate(BUCKETS):
        col = j if wide else j % 2
        row = 0 if wide else j // 2
        cx = lx + col * (130 if wide else 270)
        cy = ly + row * 52
        body.append(f'<text class="s" x="{cx}" y="{cy}" font-size="34" font-weight="800" fill="{c[key]}">{n}</text>'
                    f'<text class="s" x="{cx + 30}" y="{cy - 2}" font-size="15" font-weight="600" fill="{c["ink"]}">{LABEL[key]}</text>')
    if wide:
        body.append(f'<text class="s" x="{lx}" y="{y + h - 24}" font-size="14" fill="{c["muted"]}">Every item keeps the shop’s own name and wording.</text>')

    # 2. contradictions
    x, y, w, h = panels[1]
    css, txt = sk.count_up("c", CYCLE, [1, 3, 5, 7], 10, 30, x + 24, y + 104,
                           f'font-size="64" font-weight="800" fill="{c["now"]}"')
    style.append(css)
    body.append(f'<g class="s">{txt}</g>')
    body.append(f'<text class="s" x="{x + 24}" y="{y + 36}" font-size="16" font-weight="700" fill="{c["ink"]}">Contradictions</text>')
    for k2, ln in enumerate(sk.wrap("statements in the report that conflict with each other", 15, w - 48, "sans")):
        body.append(f'<text class="s" x="{x + 24}" y="{y + 140 + 21 * k2}" font-size="15" fill="{c["muted"]}">{esc(ln)}</text>')

    # 3. measurements
    x, y, w, h = panels[2]
    body.append(f'<text class="s" x="{x + 24}" y="{y + 36}" font-size="16" font-weight="700" fill="{c["ink"]}">Measurements</text>')
    body.append(f'<text class="s" x="{x + 24}" y="{y + 104}" font-size="64" font-weight="800" fill="{c["ask"]}">1</text>'
                f'<text class="s" x="{x + 66}" y="{y + 104}" font-size="22" font-weight="700" fill="{c["muted"]}">of 16</text>')
    sw2 = (w - 48 - 15 * 3) / 16
    for i in range(16):
        style.append(sk.reveal(f"q{i}", CYCLE, 8 + i * 1.2, 100, fade=1)) if i == 0 else None
        fill = c["ask"] if i == 0 else c["off"]
        cls = ' class="q0"' if i == 0 else ""
        body.append(f'<rect{cls} x="{x + 24 + i * (sw2 + 3):.1f}" y="{y + 124}" width="{sw2:.1f}" height="10" rx="2" fill="{fill}"/>')
    for k2, ln in enumerate(sk.wrap("findings with a number behind them (pads, 7+ mm)", 15, w - 48, "sans")):
        body.append(f'<text class="s" x="{x + 24}" y="{y + 162 + 21 * k2}" font-size="15" fill="{c["muted"]}">{esc(ln)}</text>')
    body.append("</g>")
    return doc(W, H, "One real inspection, audited",
               "From one real Tekmetric inspection of a 2001 Ram 2500: 16 shop items sorted into 2 Fix now, 4 Approve, "
               "5 Ask first and 5 Skip or defer; 7 statements that contradict each other; 1 of 16 findings with a measurement.",
               "".join(style), "\n".join(body), c["bg"])


# ---------------------------------------------------------------- flow
STEPS = [
    ("Read, then ask", "confirms vehicle, timeline, why it came in"),
    ("List every claim", "keeps the shop’s items and words"),
    ("Know the software", "Tekmetric, Mitchell 1, Xtime quirks"),
    ("Check the evidence", "measurements, photos, OEM schedule"),
    ("Find contradictions", "statement against statement"),
    ("Decide and draft", "buckets plus messages to send"),
]


def flow(c, size="wide"):
    wide = size == "wide"
    CYCLE = 11
    n = len(STEPS)
    style, body = [], []
    if wide:
        W, H = 1280, 250
        x0, x1, ly = 96, 1184, 92
        style.append(f"""
.mk {{ animation: mk {CYCLE}s cubic-bezier(.45,0,.55,1) infinite both; }}
@keyframes mk {{ 0%,4% {{ transform: translateX(0); opacity: 0; }} 6% {{ opacity: 1; }} 84% {{ transform: translateX({x1 - x0}px); opacity: 1; }} 92%,100% {{ transform: translateX({x1 - x0}px); opacity: 0; }} }}""")
        body.append(f'<line x1="{x0}" y1="{ly}" x2="{x1}" y2="{ly}" stroke="{c["faint"]}" stroke-width="3"/>')
        for i, (t, s) in enumerate(STEPS):
            x = x0 + (x1 - x0) * i / (n - 1)
            on = 6 + 78 * i / (n - 1)
            style.append(sk.reveal(f"st{i}", CYCLE, on, 95, fade=2))
            body.append(f'<circle cx="{x}" cy="{ly}" r="17" fill="{c["panel"]}" stroke="{c["faint"]}" stroke-width="2"/>'
                        f'<circle class="st{i}" cx="{x}" cy="{ly}" r="17" fill="{c["band"]}"/>'
                        f'<text class="s" x="{x}" y="{ly + 5}" font-size="14" font-weight="700" text-anchor="middle" fill="{c["brand"]}">{i + 1}</text>'
                        f'<text class="s" x="{x}" y="{ly + 48}" font-size="16" font-weight="700" text-anchor="middle" fill="{c["ink"]}">{esc(t)}</text>')
            for k, ln in enumerate(sk.wrap(s, 13.5, 168, "sans")):
                body.append(f'<text class="s" x="{x}" y="{ly + 72 + 19 * k}" font-size="13.5" text-anchor="middle" fill="{c["muted"]}">{esc(ln)}</text>')
        body.append(f'<g class="mk"><circle cx="{x0}" cy="{ly}" r="6" fill="{c["brand"]}"/></g>')
    else:
        W, H = 640, 700
        lx, y0, y1 = 64, 64, 636
        style.append(f"""
.mk {{ animation: mk {CYCLE}s cubic-bezier(.45,0,.55,1) infinite both; }}
@keyframes mk {{ 0%,4% {{ transform: translateY(0); opacity: 0; }} 6% {{ opacity: 1; }} 84% {{ transform: translateY({y1 - y0}px); opacity: 1; }} 92%,100% {{ transform: translateY({y1 - y0}px); opacity: 0; }} }}""")
        body.append(f'<line x1="{lx}" y1="{y0}" x2="{lx}" y2="{y1}" stroke="{c["faint"]}" stroke-width="3"/>')
        for i, (t, s) in enumerate(STEPS):
            y = y0 + (y1 - y0) * i / (n - 1)
            on = 6 + 78 * i / (n - 1)
            style.append(sk.reveal(f"st{i}", CYCLE, on, 95, fade=2))
            body.append(f'<circle cx="{lx}" cy="{y}" r="18" fill="{c["panel"]}" stroke="{c["faint"]}" stroke-width="2"/>'
                        f'<circle class="st{i}" cx="{lx}" cy="{y}" r="18" fill="{c["band"]}"/>'
                        f'<text class="s" x="{lx}" y="{y + 5}" font-size="15" font-weight="700" text-anchor="middle" fill="{c["brand"]}">{i + 1}</text>'
                        f'<text class="s" x="{lx + 40}" y="{y - 2}" font-size="20" font-weight="700" fill="{c["ink"]}">{esc(t)}</text>'
                        f'<text class="s" x="{lx + 40}" y="{y + 24}" font-size="16" fill="{c["muted"]}">{esc(s)}</text>')
        body.append(f'<g class="mk"><circle cx="{lx}" cy="{y0}" r="7" fill="{c["brand"]}"/></g>')
    return doc(W, H, "How the audit works",
               "Six steps: read the documents then ask what only you know; list every claim keeping the shop's items; "
               "apply the inspection software's known quirks; check evidence and the OEM schedule; find contradictions; "
               "decide each item and draft the messages.", "".join(style), "\n".join(body), c["bg"])


# ---------------------------------------------------------------- walkthrough
def window(c, x, y, w, h, title):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c["panel"]}" stroke="{c["faint"]}"/>'
            f'<line x1="{x}" y1="{y + 40}" x2="{x + w}" y2="{y + 40}" stroke="{c["faint"]}"/>'
            f'<text class="s" x="{x + 18}" y="{y + 26}" font-size="14" font-weight="600" fill="{c["muted"]}">{esc(title)}</text>')


INPUT = [
    ("red", "Front Brake System",
     "Right front brake line banjo bolt is leaking. Brake pads at 7+mm – currently in good condition."),
    (None, "Reason for visit: brakes",
     "Front brake calipers recently have been replaced… Recommend replacing both front calipers, and replacing the master cylinder."),
    ("yellow", "Differential & Transfer Case",
     "Recommend servicing the front differential, rear differential and transfer case… due based on maintenance intervals."),
]


def walk_input(c, size="wide"):
    wide = size == "wide"
    W = 1280 if wide else 640
    CYCLE = 12
    x, y, w = (48, 24, 1184) if wide else (24, 24, 592)
    tsize = 16 if wide else 15
    lines_all, yy = [], y + 74
    for grade, name, text in INPUT:
        wrapped = sk.wrap("“" + text + "”", tsize, w - 90, "sans")
        lines_all.append((grade, name, wrapped, yy))
        yy += 30 + 24 * len(wrapped) + 22
    H = yy + 10
    style, body = [], [window(c, x, y, w, H - y - 16, "The shop’s report, as written (excerpt)")]
    grade_col = {"red": c["now"], "yellow": c["ask"], None: c["off"]}
    for i, (grade, name, wrapped, top) in enumerate(lines_all):
        on = 6 + i * 14
        style.append(sk.reveal(f"in{i}", CYCLE, on, 95, fade=3))
        g = [f'<g class="in{i}"><circle cx="{x + 32}" cy="{top - 6}" r="6" fill="{grade_col[grade]}"/>',
             f'<text class="s" x="{x + 52}" y="{top}" font-size="17" font-weight="700" fill="{c["ink"]}">{esc(name)}</text>']
        for k, ln in enumerate(wrapped):
            g.append(f'<text class="s" x="{x + 52}" y="{top + 28 + 24 * k}" font-size="{tsize}" fill="{c["muted"]}">{esc(ln)}</text>')
        g.append("</g>")
        body.append("".join(g))
    return doc(W, H, "Step 1: the shop's report",
               "Excerpt of the real report: Front Brake System graded red, right front banjo bolt leaking, pads 7+ mm good; "
               "reason for visit says calipers were recently replaced but recommends replacing both calipers and the master "
               "cylinder; a yellow item bundles front diff, rear diff and transfer case service as due by interval.",
               "".join(style), "\n".join(body), c["bg"])


CONFLICTS = [
    ("Front brake calipers recently have been replaced", "Recommend replacing both front calipers",
     "No reason given for why nearly new calipers failed."),
    ("Banjo bolt leaking caused the master cylinder to run dry", "Replace calipers and master cylinder",
     "The plan never repairs the leak the shop named as the cause."),
    ("Towed in due to possible loss of brakes", "Test drive: pedal almost goes to the floor",
     "Driven without working brakes, or template text."),
]


def walk_check(c, size="wide"):
    wide = size == "wide"
    CYCLE = 13
    style, body = [], []
    if wide:
        W, x, w = 1280, 48, 1184
        rowh = 92
        H = 24 + 52 + len(CONFLICTS) * rowh + 34
        body.append(window(c, x, 24, w, H - 40, "Conflicting statements found"))
        for i, (a, b, why) in enumerate(CONFLICTS):
            top = 24 + 66 + i * rowh
            on = 6 + i * 16
            style.append(sk.reveal(f"ca{i}", CYCLE, on, 95, fade=2))
            style.append(sk.reveal(f"cb{i}", CYCLE, on + 4, 95, fade=2))
            style.append(sk.draw(f"cl{i}", CYCLE, 40, on + 6, on + 9))
            style.append(sk.reveal(f"cw{i}", CYCLE, on + 9, 95, fade=2))
            if i:
                body.append(f'<line x1="{x + 20}" y1="{top - 14}" x2="{x + w - 20}" y2="{top - 14}" stroke="{c["faint"]}" stroke-dasharray="4 4"/>')
            qa = sk.fit("“" + a + "”", 15.5, 360, "sans")
            qb = sk.fit("“" + b + "”", 15.5, 330, "sans")
            body.append(f'<text class="s ca{i}" x="{x + 24}" y="{top + 22}" font-size="15.5" fill="{c["ink"]}">{esc(qa)}</text>')
            body.append(f'<line class="cl{i}" x1="{x + 404}" y1="{top + 17}" x2="{x + 444}" y2="{top + 17}" stroke="{c["now"]}" stroke-width="2.5"/>')
            body.append(f'<text class="s cb{i}" x="{x + 460}" y="{top + 22}" font-size="15.5" fill="{c["ink"]}">{esc(qb)}</text>')
            body.append(f'<g class="cw{i}"><rect x="{x + 822}" y="{top + 2}" width="3" height="44" fill="{c["now"]}"/>')
            for k, ln in enumerate(sk.wrap(why, 15, 330, "sans")):
                body.append(f'<text class="s" x="{x + 838}" y="{top + 20 + 21 * k}" font-size="15" font-weight="600" fill="{c["ink"]}">{esc(ln)}</text>')
            body.append("</g>")
    else:
        W, x, w = 640, 24, 592
        rowh = 196
        H = 24 + 52 + len(CONFLICTS) * rowh + 20
        body.append(window(c, x, 24, w, H - 40, "Conflicting statements found"))
        for i, (a, b, why) in enumerate(CONFLICTS):
            top = 24 + 70 + i * rowh
            on = 6 + i * 16
            style.append(sk.reveal(f"ca{i}", CYCLE, on, 95, fade=2))
            style.append(sk.reveal(f"cb{i}", CYCLE, on + 4, 95, fade=2))
            style.append(sk.reveal(f"cw{i}", CYCLE, on + 9, 95, fade=2))
            if i:
                body.append(f'<line x1="{x + 20}" y1="{top - 18}" x2="{x + w - 20}" y2="{top - 18}" stroke="{c["faint"]}" stroke-dasharray="4 4"/>')
            for k, ln in enumerate(sk.wrap("“" + a + "”", 16, w - 48, "sans")):
                body.append(f'<text class="s ca{i}" x="{x + 24}" y="{top + 21 * k}" font-size="16" fill="{c["ink"]}">{esc(ln)}</text>')
            body.append(f'<text class="s cb{i}" x="{x + 24}" y="{top + 50}" font-size="14" font-weight="700" fill="{c["now"]}">but also says</text>')
            for k, ln in enumerate(sk.wrap("“" + b + "”", 16, w - 48, "sans")):
                body.append(f'<text class="s cb{i}" x="{x + 24}" y="{top + 76 + 21 * k}" font-size="16" fill="{c["ink"]}">{esc(ln)}</text>')
            body.append(f'<g class="cw{i}"><rect x="{x + 24}" y="{top + 104}" width="3" height="40" fill="{c["now"]}"/>')
            for k, ln in enumerate(sk.wrap(why, 15, w - 70, "sans")):
                body.append(f'<text class="s" x="{x + 38}" y="{top + 120 + 20 * k}" font-size="15" font-weight="600" fill="{c["ink"]}">{esc(ln)}</text>')
            body.append("</g>")
    return doc(W, H, "Step 2: the contradictions",
               "Three conflicts from the real report: calipers recently replaced vs replace both calipers; the leak named as "
               "the cause vs a plan that never repairs it; towed in for loss of brakes vs a test drive reporting brake feel.",
               "".join(style), "\n".join(body), c["bg"])


MESSAGE = [
    "Please go ahead with:",
    "1. Repair the leak at the right-front brake line",
    "   fitting, refill and bleed, then check the pedal.",
    "2. Replace the right taillight lens.",
    "The calipers were installed at another shop and I’m",
    "checking the warranty. Please document the fitting",
    "with photos and hold off on new calipers.",
    "Which warning-light codes came up on the scan?",
]


def walk_output(c, size="wide"):
    wide = size == "wide"
    CYCLE = 14
    style, body = [], []
    line_h, fs = 23, 15
    if wide:
        W, H = 1280, 360
        bx, by, bw = 640, 40, 592
        lx, ly = 64, 72
    else:
        W, H = 640, 700
        bx, by, bw = 24, 330, 592
        lx, ly = 40, 56
    # left: approve list + your to-do
    body.append(f'<text class="s" x="{lx}" y="{ly}" font-size="22" font-weight="800" fill="{c["ink"]}">Approve today</text>')
    items = [("go", "Leak repair, refill and bleed, pedal check"), ("go", "Right taillight lens")]
    todo = [("Call the shop that installed the calipers"), ("about warranty")]
    for i, (_, t) in enumerate(items):
        y = ly + 40 + i * 34
        style.append(sk.reveal(f"ap{i}", CYCLE, 4 + i * 4, 95, fade=2))
        body.append(f'<g class="ap{i}"><rect x="{lx}" y="{y - 16}" width="20" height="20" rx="5" fill="none" stroke="{c["go"]}" stroke-width="2"/>'
                    f'<path d="M{lx + 5} {y - 6} l4 4 l7 -8" fill="none" stroke="{c["go"]}" stroke-width="2.4" stroke-linecap="round"/>'
                    f'<text class="s" x="{lx + 32}" y="{y}" font-size="16" fill="{c["ink"]}">{esc(t)}</text></g>')
    ty = ly + 40 + len(items) * 34 + 34
    body.append(f'<text class="s" x="{lx}" y="{ty}" font-size="22" font-weight="800" fill="{c["ink"]}">Your own to-do</text>')
    style.append(sk.reveal("td", CYCLE, 12, 95, fade=2))
    body.append(f'<g class="td"><rect x="{lx}" y="{ty + 24}" width="20" height="20" rx="5" fill="none" stroke="{c["muted"]}" stroke-width="2"/>'
                f'<text class="s" x="{lx + 32}" y="{ty + 40}" font-size="16" fill="{c["ink"]}">{esc(todo[0])}</text>'
                f'<text class="s" x="{lx + 32}" y="{ty + 62}" font-size="16" fill="{c["ink"]}">{esc(todo[1])}</text></g>')
    # right: text thread
    bh = 56 + len(MESSAGE) * line_h + 36
    body.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh + 30}" rx="18" fill="{c["panel"]}" stroke="{c["faint"]}"/>'
                f'<text class="s" x="{bx + 20}" y="{by + 28}" font-size="14" font-weight="600" fill="{c["muted"]}">Text to the shop · ready to send</text>'
                f'<line x1="{bx}" y1="{by + 42}" x2="{bx + bw}" y2="{by + 42}" stroke="{c["faint"]}"/>')
    bub_x, bub_y, bub_w = bx + 24, by + 60, bw - 48
    body.append(f'<rect x="{bub_x}" y="{bub_y}" width="{bub_w}" height="{len(MESSAGE) * line_h + 26}" rx="16" fill="{c["band"]}"/>')
    for i, ln in enumerate(MESSAGE):
        on = 18 + i * 5
        style.append(sk.reveal(f"ml{i}", CYCLE, on, 95, fade=1.5))
        body.append(f'<text class="s ml{i}" x="{bub_x + 18}" y="{bub_y + 30 + i * line_h}" font-size="{fs}" fill="{c["bandink"]}" xml:space="preserve">{esc(ln)}</text>')
    return doc(W, H, "Step 3: what you send",
               "The output: an approve-today list (leak repair with bleed and pedal check; taillight lens), a to-do to call "
               "the shop that installed the calipers about warranty, and a ready-to-send text to the shop.",
               "".join(style), "\n".join(body), c["bg"])


if __name__ == "__main__":
    sk.write_all(OUT, {"hero": hero, "proof": proof, "flow": flow,
                       "walk-input": walk_input, "walk-check": walk_check, "walk-output": walk_output}, THEMES)
