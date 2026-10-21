# Image and Video Evidence Review

As of 2026-10-20. How to judge DVI/estimate photos and video. Numeric thresholds live in `technical-criteria.md`; disputes in `consumer-protection.md`. **[METHOD]** = recommended procedure reasoned from sourced facts, not a published standard.

**Core principle:** A photo shows what the camera saw at one moment. It is rarely a measurement. Strongest photos show a **test instrument and its reading**. Without one, a photo can show the *presence* of a condition (torn boot, bulge, cords), rarely its *degree* (32nds, mm, moisture, rib loss).

## Contents

1. Hard limits for Claude as reviewer
2. Per-component: what photos can and can't establish
3. Evidence standards (strong vs. weak photos)
4. Vehicle-identity and integrity checks
5. Consistency cross-checks (C1–C14)
6. Video review and frame sampling
7. Required phrasing and anti-accusation rules
8. Computer-vision accuracy benchmarks
9. Per-photo checklist
10. Evidence rubric and mapping to status labels
11. Mode-specific notes
12. Open uncertainties
13. Sources

---

## 1. Hard limits for Claude as reviewer

- **Never estimate wear by eye.** Read a gauge, micrometer, strip, or printout only when its scale/readout is legible. Never estimate tread depth, pad thickness, or rotor thickness from appearance. At most: "appears near/at the wear bars" or "friction material appears very thin or absent," labeled as visual impression.
- **Why:** even purpose-built scanners claim only ~±0.5 mm (±1/32") under guided capture; generic CNNs ~±1.5 mm. Decision points (2/32", 4/32", ~2–3 mm pads) are that close together (section 8).
- **No metadata.** Claude does not receive image metadata/EXIF (Claude vision docs). EXIF checks need a separate tool (`exiftool` in Claude Code, or the user's OS file-info panel).
- **Cannot detect AI-generated or edited images** (Claude vision docs). **Never state or imply a photo is fake, fabricated, doctored, or AI-generated.** Observable facts are fine: different vehicle (tire size, wheel, paint), same image used twice, claimed component not shown.
- Other documented vision limits: errors on low-quality, rotated, or very small (< ~200 px) images; approximate spatial localization — never compute measurements from pixel geometry; approximate counting; downscaling of large images can make gauge scales illegible; heavy JPEG compression degrades text and fine detail. Anthropic advises human review for high-stakes use (Claude vision docs). Third-party evaluations report weaker performance on dense non-text layouts and counting (arXiv preprint; Roboflow) — indicative only.
- **Audio:** Claude cannot hear audio in frames. Sound claims (CV click, bearing growl) must be transcribed or taken at face value and marked unverified.

**Image-condition limits for any reviewer:** no scale reference → no depth/thickness; flash glare hides texture, raking light exaggerates it, shop LEDs shift fluid/rust color; compression erases fine cracks, gauge hash marks, DOT digits; single instant → no growth or rate; occlusion (inner pad, rotor back, inboard sidewall, upper strut).

---

## 2. Per-component: what photos can and can't establish

### Summary table

| Component | Photo alone CAN show | Photo alone CANNOT show | Strong evidence |
|---|---|---|---|
| Tire tread | flush with wear bars; cords | depth in 32nds | gauge in main groove, legible, per tire/position |
| Tire wear pattern | presence of pattern | current alignment state | raking light + inner/outer gauge; alignment printout |
| Sidewall | bulge; cut to cords | crack depth; cosmetic vs. structural | close-up + context; cords visible |
| Tire age | DOT week/year (if legible) | that age = unsafe | full TIN photo per tire |
| Brake pads | metal-to-metal; near-zero outer pad | mm thickness; inner pad | pad gauge on friction material, position labeled |
| Rotors | lip, deep grooves, cracks | thickness vs. discard; runout | micrometer + discard spec |
| Brake fluid | level vs. marks | moisture / boiling point | strip vs. chart; meter reading |
| ATF | level; debris on stick | condition from color | OEM-procedure check; fluid analysis |
| Coolant | oil contamination; level | freeze point; inhibitor level | refractometer / strip |
| Air/cabin filter | debris, damage | remaining life | restriction reading / OEM interval |
| Belt | chunks, splits, cords | EPDM material loss | wear gauge (video of rocking) |
| Leak | wet fluid, drips | fresh vs. old; source | clean + dye/UV; before/after |
| Shock/strut | wet below spring seat; drips | marginal misting vs. leak; growth | wide + close-up; wiped recheck |
| CV boot | torn boot, slung grease | joint damage | boot photo + noise/play note |
| Battery | corrosion, swelling | health | tester printout matching battery label |
| Lights | out (if lit comparison) | aim | photo with lamp on |
| Frame rust | holes; section loss | surface vs. structural (often) | pick/hammer test photo + location |

### 2.1 Tires

**Tread depth**
- CAN: gauge seated in a groove with readable scale; tread flush with wear bars (molded at 2/32") (NHTSA interp.), (Ford).
- CANNOT: depth from a gauge-less photo (angle, lens distortion, lighting). One gauge photo can't represent four tires or inner/center/outer of one tire. Read several major grooves; avoid sipes, shoulder decoration grooves, and wear bars (NAPA).
- Check: probe in a **main circumferential groove** (not sipe/wear bar)? Gauge **perpendicular**, base flat on ribs? Scale **legible**, units (32nds/mm)? Photo reading **matches report text**?
- Best: gauge photo per tire (ideally inner/center/outer), position labeled, plus wide shot showing which wheel.

**Uneven wear**
- CAN: center (over-inflation), both shoulders (under-inflation), one edge (camber), feathering (toe), cupping/scalloping (dampers, imbalance, suspension) (Michelin), (Jalopnik/Bridgestone).
- CANNOT: confirm cause or that the car is out of alignment *today* (tires may have been rotated; cause may be fixed). Alignment claims need a before/after printout. Feathering is often felt by touch; flat lighting hides it.
- Best: raking-light photo across tread + inner/outer gauge readings.

**Sidewall**
- CAN: bulge/bubble (Michelin: internal cord damage, don't drive on it); cut exposing cords; deep cracking.
- CANNOT: tell cosmetic weather-checking from structural cracking; crack depth is rarely visible. Cracks are structural when deep, reaching cords, or near the bead [UNVERIFIED: exact Michelin wording]. USTMA knows of no scientific data setting a passenger-tire service life (Barry's Tire Tech, reproducing USTMA) — "cracked = replace" is not automatic.
- Watch for a normal **sidewall indentation** (ply-splice dip) presented as damage; Michelin treats it separately from bulges.

**DOT date code**
- CAN: legible TIN gives week/year (2321 = week 23 of 2021) (SlashGear), (Firestone). Also an identity check — four "aged out" tires need four date-code photos; matching codes are normal for a set bought together.
- CANNOT: prove age alone makes a tire unsafe (no federal limit; guidance varies by maker).
- Pitfall: full date code is often on one sidewall only (may face inboard). A partial TIN with no date is not a date code.

### 2.2 Brakes

**Pads**
- CAN (strong): pad gauge or caliper reading on **friction material only**, legible, position labeled (Phoenix Systems, vendor).
- CAN (moderate): through-spoke/caliper-window view of the outer pad showing near-zero material or metal-to-metal.
- CANNOT: mm from a through-the-wheel photo. **Inner pad usually not visible** and often wears faster (piston pushes on it). > ~2 mm side-to-side difference can point to a sticking caliper (CarFromJapan, secondary). Thick-looking pads can still be cracked, glazed, or separated.
- Removed pads: stronger (both gaugeable) but must be tied to vehicle and position — a bench pad could be from any car. Ask for pad beside the wheel/caliper or with a position label.

**Rotors**
- CAN: pronounced lip, deep grooves, cracks, heavy friction-surface rust, blue heat tint.
- CANNOT: **thickness vs. discard** (needs micrometer + stamped "MIN TH" or OEM value); **runout/DTV** (dial indicator/micrometer).
- Scoring limits are OEM-specific (one Saab procedure allows grooves to 1.5 mm; a heavy-duty manual uses a much smaller figure) (Saab WIS). Blue tint alone does not require replacement if within tolerance (Fras-le). Hard spots extend below the surface and generally call for replacement (Brake & Front End). Light surface rust on a parked car's rotors is common and wipes off with braking [UNVERIFIED; widely observed].
- Best: micrometer with readable display + discard spec.

### 2.3 Fluids

**Color is not a valid condition test for brake fluid, ATF, or coolant.** A color photo is at best a screening observation; a photo of a strip/refractometer/meter result is valid evidence.

- **Brake fluid:** looks don't give water content or boiling reserve; dark fluid can test fine, clear fluid can test high (Phoenix Systems, vendor), (Rick's). Valid: moisture or copper strip against its chart, or boiling-point/moisture meter display. 200 ppm Cu cited as a change point (Rick's) [UNVERIFIED against OEM]. Caveats: reservoir fluid may test better than caliper fluid; strips are for glycol DOT 3/4/5.1, not silicone DOT 5.
- **ATF:** clean red fluid can come from a worn transmission and dark fluid from a healthy one (forums, anecdotal). Burnt smell, debris, shift behavior matter more and can't be photographed. Color "swatch" cards are used as sales aids (BITOG). [UNVERIFIED: no OEM bulletin found; practitioner consensus.]
- **Coolant:** color doesn't reliably indicate type or condition (chemistries share colors; dyes inconsistent) (Prestone UK). Valid: **refractometer** (most accurate for freeze point) or **test strips** (less precise; freeze point + additive level) (Cummins bulletin via BITOG), (SAE 960645). A military field study found strips sometimes off from refractometer by > 10°F (DTIC; approximate). Photos CAN show oil contamination (sludge, milky layer), heavy rust/scale, low level vs. marks.
- **Engine oil:** color says little about remaining life on modern oils [UNVERIFIED]. Dipstick level only if legible and in focus.
- **Level photos:** valid if MIN/MAX marks and fluid line are both visible. Brake fluid drops as pads wear, so low brake fluid alone is not proof of a leak [UNVERIFIED; standard practice].

### 2.4 Filters (engine air, cabin)

- CAN: debris (leaves, nests, bugs), damage, oil soaking, missing filter.
- CANNOT: remaining life. Donaldson: visual inspection is not adequate; very dirty-looking filters may have substantial life left; use restriction measurement (Donaldson, vendor; heavy-duty guidance), (CCJ).
- Staging: inlet side is always darker than outlet; backlighting or a new white filter beside it makes it look worse. Cabin intervals are usually time/mileage per manual, shorter for dust.
- **Audit stance:** "dirty filter" photo = **Weak** unless at/past OEM interval or showing debris/damage.

### 2.5 Belts (serpentine)

- CAN: chunks missing, rib separation, cords, fraying, glazing, oil contamination, misalignment wear.
- CANNOT: **EPDM material loss**, the main modern wear mode. "3 cracks in 3 inches" suits neoprene, not EPDM; EPDM can pass 100,000 mi without visible cracks; ~5% rib material loss can cause problems (Gates TT002-15).
- A "cracked belt" photo on EPDM is not proof of wear; a no-crack photo is not proof it's fine.
- Best: Gates wear gauge (or equivalent) seated in grooves — worn belt lets it rock, best shown in **video**. Gates app green/yellow/red screenshot = moderate evidence (CCJ).

### 2.6 Hoses

- CAN: splits, bulges/ballooning, chafe-through, wet residue at clamp, crusted coolant at a joint.
- CANNOT: softness, internal deterioration, sponginess (tactile). Surface cracking may be cosmetic [UNVERIFIED: no Gates/Dayco hose page retrieved].

### 2.7 Leaks

- CAN: wet shiny fluid, drips, puddles, trails — more of these in frame = stronger.
- CANNOT (generally): (1) fresh vs. old — residue makes old stains hard to tell from current leaks (EngineerFix); (2) source — fluid runs downhill and spreads in airflow, wettest spot is often not the origin (YourMechanic); (3) rate — seepage (dry, dirt-caked film) vs. active (wet, dripping), but one instant; (4) which fluid — color ambiguous under shop light.
- Best: clean → run → **UV-dye photo** traced to origin, or a timed before/after pair (MotoIQ), (YourMechanic). The named source (e.g., valve cover gasket) should sit at the **top** of the wet trail.
- Red flags: repair for a gasket far from the wetness shown; dry, dusty residue called "active."

### 2.8 Suspension

**Shock/strut misting vs. leaking**
- CAN: heavy wet coating along the body, drips, fluid below the spring seat — consistent with leakage.
- Manufacturer criteria:
  - Monroe: minimal film = "weepage," no replacement; leakage = most of the unit wet/oily or dripping (Monroe; via search summary, fetch returned 403).
  - KYB: "sweating" = slight even film from the top, no excess on fingers, may reach spring seat, doesn't grow. Leak = beyond the spring seat, oil on fingers, thick wet streaks or drips worsening over time (KYB 2025).
  - An NHTSA-hosted OEM TSB says misting is normal evaporation; do not replace (NHTSA TSB) [UNVERIFIED: issuing OEM].
- CANNOT: KYB finger test; change over time from one photo. Flash close-ups make light film look dramatic. Fluid may come from above (engine oil, power steering) [UNVERIFIED that Monroe says this].
- Best: wide shot of whole unit and spring seat + close-up + ideally a wiped-and-driven recheck.
- Rule: "leaking" is supported when wetness extends below the spring seat or drips. A "light film at top" photo labeled "leaking — replace" = **Contradicts** under KYB/Monroe criteria.

**Boots and bushings**
- CAN: torn/split/missing boot; cracked or extruded bushing rubber.
- CANNOT: **play** in ball joints, tie rods, bushings — needs pry bar/dial indicator; **video** of movement is the right evidence.

### 2.9 CV boots / axles

- CAN: torn boot, slung grease, missing clamp — strong for boot failure.
- CANNOT: joint damage. Practitioner consensus: silent joint with clean grease may need only boot + regrease; clicking (esp. in turns) or gritty grease points to axle (forum, anecdotal).
- State rules: Virginia does not reject defective CV boots (19VAC30-70-110). (Utah R714-160-10 treated torn boots as advisory, but Utah no longer runs passenger safety inspections — historical example only [UNVERIFIED].)
- **Implication:** torn-boot photo supports a **boot** recommendation; an **axle** needs a documented noise or joint-play finding.

### 2.10 Battery

- CAN: terminal corrosion, swollen/cracked/leaking case, loose hold-down, date sticker.
- CANNOT: capacity or health. Corrosion alone doesn't mean a bad battery — often cleanable, but test anyway (Rick's), (ToolSource).
- Best: tester printout/screen showing state of health, measured vs. rated CCA, internal resistance/conductance, voltage and state of charge. Midtronics material: ≥ 90% of rated CCA healthy, < 80% warning; surface charge after charging/jump can distort readings (Midtronics, vendor claim).
- Printout checks: **rated CCA entered matches the battery label** in another photo? Date/time matches the visit? Printed VIN matches? Does "Replace" follow from the numbers?

### 2.11 Wipers

- CAN: torn, split, detached rubber; bent/corroded frame.
- CANNOT: streaking or hardening reliably — a dirty windshield streaks too; clean and retest (forum). A short video of a wipe on wet glass beats a still.

### 2.12 Lights

- CAN: lamp **switched on** beside its working mate shows an out bulb; cracked or moisture-filled housing; yellowed lens.
- CANNOT: an unlit lamp proves nothing about function; aim can't be judged from a casual photo; haze severity is lighting-dependent [METHOD].

### 2.13 Exhaust

- CAN: holes, broken hangers, separated joints, rust-through, soot trails at a joint (consistent with a leak).
- CANNOT: prove an active leak (sound, smoke test, feel) or that surface rust is structural [METHOD].

### 2.14 Undercarriage / frame rust

- CAN: perforation, flaking scale with section loss, broken/separated brackets, rust at suspension mounts.
- CANNOT: surface vs. structural loss — metal can be thinned under superficial-looking rust. Inspectors use scrape/pick and hammer-tap tests (solid rings, weak sounds dull or perforates) (EngineerFix), (ToolSource).
- UK MOT practice judges corrosion by location and function (small corrosion at a load-bearing mount can be serious) (NI DVA); "pass and advise" when in doubt (MOT blog).
- Best: pick/screwdriver penetrating metal, or a hole, plus a context shot locating it on the frame.
- Surface rust on bare-steel underbody parts of a salt-region car is normal, not by itself a repair finding [UNVERIFIED].

---

## 3. Evidence standards

### 3.1 What a strong substantiating photo includes

Vendor best practice: a photo per checklist item, close-up plus wider shot, good lighting, fewer distractions (AutoVitals), (AutoServe1).

1. **Identifiable item** — in frame, in focus, recognizable as the claimed part.
2. **Position** — LF/RF/LR/RR, inner/outer, bank 1/2; ideally visible (wheel, fender, chalk mark, label).
3. **Context shot + close-up.**
4. **Instrument with readable scale** for any quantitative finding (tread gauge, pad gauge, micrometer, belt gauge, strip vs. chart, refractometer, printout).
5. **Lighting and focus** — no flash glare on the area of interest, no motion blur, no extreme digital zoom.
6. **Unedited framing** — no crop removing needed context (strut spring seat, tire wear bars).
7. **Vehicle linkage** — at least one photo ties the set to this vehicle (VIN, odometer, plate, distinctive feature).
8. **Timestamp** — DVI platform timestamp, or metadata if the user extracted it.

### 3.2 Weak or non-probative photos

- Generic "it's dirty" filter/fluid/engine-bay shot with no instrument and no interval context.
- Through-the-wheel pad photo with no gauge used to claim a mm value.
- Fluid color (or fluid on a towel/swab) as the sole basis for a flush.
- "Cracks" on an EPDM belt.
- Close-up of light film on a strut cropped so the spring seat is hidden.
- Dry, dust-caked residue labeled active leak, no dye or cleaned recheck.
- One tire photo for all four.
- Unlit headlamp for "bulb out."
- Unidentifiable component, or one that could be on any vehicle.
- Bench photos of removed parts with no vehicle/position link.
- Stock/illustrative images (manufacturer diagrams, template "example" pictures). Some DVI platforms offer canned reference images [UNVERIFIED which; look for "example" labels].

---

## 4. Vehicle-identity and integrity checks

**Framing rule:** these checks find inconsistencies to ask about, not proof of wrongdoing. Template images, mislabeled corners, and wrong-vehicle photos are usually workflow errors (tech photographing the next car, mis-tap in the app). Report as "does not appear to match; please clarify."

### 4.1 Does the photo belong to this vehicle? [METHOD]

| Check | Compare | Notes |
|---|---|---|
| VIN | VIN plate / door label photo vs. VIN on RO/estimate | Strongest single link; last 6–8 digits suffice |
| Odometer | Odometer photo vs. RO mileage-in | Mismatch may be a typo; note it |
| Plate | Plate in any context shot | Consumer can confirm |
| Tire size | Sidewall size vs. door placard and estimate | One odd "LF" size = flag; staggered fitments can be legit |
| Tire brand/model | Brand and tread pattern across all tire photos and vs. owner's set | Four patterns on a matched set = flag |
| DOT codes | Week/year across the set | Sets bought together share close codes |
| Wheels | Design, finish, center cap, lug style across corners | Different alloy designs = flag |
| Paint/body | Paint at fender/door edges, body style, trim | Easy consumer check |
| Brake hardware | Caliper color/style, rotor type (slotted/drilled) vs. vehicle and across corners | Performance calipers on a base model = flag |
| Left vs. right | Steering parts, engine-bay side, wheel direction, caliper leading/trailing position | Mirroring can reveal mislabeled sides [METHOD] |
| Engine bay | Engine cover, under-hood labels, battery location vs. engine | |
| Mileage plausibility | Wear vs. mileage (cords on 6-month-old tires) | Possible with damage/alignment issues; ask |

### 4.2 Duplicate or reused photos

- **Within a report:** same image (or same frame slightly cropped/brightened) for two corners or items (e.g., "LF pad" = "RF pad"); matching background details (floor stain, glove, reflection) [METHOD].
- **Across reports:** compare with prior reports from the same shop; an identical image on two visits or vehicles is a strong flag. Shop owners can spot-check this across their DVI system.
- **Stock/web images:** reverse image search (Google Lens, TinEye "oldest first") can show whether a photo appears online (Bellingcat), (Georgetown), (Data Detox Kit). It won't find images on private DVI platforms, so "no match" proves nothing. Uploading customer images to third parties has privacy implications — the user decides.

### 4.3 Metadata (EXIF) and provenance

- Claude cannot read it (section 1). Use `exiftool` or OS file info.
- **Absence of EXIF is normal, not a red flag.** Many platforms re-encode and strip it (Fast.io, vendor); DVI links/texts likely re-encode [UNVERIFIED: no DVI vendor documentation].
- When present (user-extracted): compare capture date/time with visit date and RO time-in/out; camera model consistent across the set. EXIF is easily edited — a match is weak support, a mismatch is a question.
- **C2PA Content Credentials:** e.g., Pixel 10 signs JPEG captures and Google Photos records edits (Google Security Blog, Sept 2025). Intact credentials = strong provenance, but DVI apps and re-encoding usually drop them [UNVERIFIED for any DVI platform].

### 4.4 Framing and editing

- **Misleading framing is far more common than pixel editing** [UNVERIFIED as a measured rate]: tight crop hiding the spring seat; flash close-up making light film look wet; dirty filter beside a pristine new one; gauge angled so scale reads high/low; probe sitting on a wear bar.
- Possible-edit signs (low reliability): inconsistent shadows/lighting direction, repeated texture patches, mismatched blur/noise, text overlays covering parts, odd edges around a part. Report only as "[oddity] is visible; image analysis can't confirm editing."
- Forensic tools are unreliable here: Error Level Analysis maps compression differences, not edits; false positives on smooth areas, misses same-software edits, degrades with re-saves (FotoForensics), (GIMP forensics wiki). Re-compressed DVI images make it even less meaningful.

### 4.5 Fraud context (calibration, not accusation)

- Deliberate damage happens: Pennsylvania police charged two dealership techs with damaging a customer's brake pads, found via second opinion (The Drive). This is the strongest reason to recommend **in-person verification or a second opinion** over remote "photo proof."
- No published case of a shop sending another vehicle's DVI photo was found [UNVERIFIED]. Mismatch scenarios are plausible but unquantified.
- DVI marketing says photos raise approval rates (Tire Review), (AutoServe1) — an incentive for *many* photos, not necessarily *probative* ones.

---

## 5. Consistency cross-checks [METHOD]

Run for every line item. Any mismatch becomes a question for the shop.

| # | Cross-check | Example mismatch | Output phrasing |
|---|---|---|---|
| C1 | Photo vs. grade | Gauge shows 7 mm, graded red | "Photo shows ~7 mm on the gauge, inconsistent with a red/urgent grade. Ask for the OEM minimum and measured value." |
| C2 | Photo vs. measurement text | Text 3/32, gauge 6/32 | "The written value does not match the gauge visible in the photo." |
| C3 | Photo vs. recommendation | Torn CV boot → full axle, no noise noted | "Photo supports a boot repair; the axle needs a documented joint finding." |
| C4 | Coverage (N items vs. N photos) | "Replace all 4 tires," one photographed | "Only one tire is documented; the other three are unsupported by photos." |
| C5 | Position | Labeled LF, photo shows right side | "Position in photo may not match the label." |
| C6 | Pair logic | Both front pads "2 mm," photos look very different | Ask for both gauge readings |
| C7 | Measurement vs. threshold | 5/32 graded red; shop legend says red < 3/32 | Flag the internal inconsistency |
| C8 | Photo vs. notes | "Active leak, dripping," photo shows dry caked residue | "Photo does not show active wetness." |
| C9 | Cross-item | Brake fluid "low – leak suspected" + pads near minimum | Low fluid may reflect pad wear, not a leak [UNVERIFIED; standard practice] |
| C10 | Photo vs. vehicle data | Tire size ≠ placard/estimate; VIN digits ≠ RO | Identity question (4.1) |
| C11 | Photo vs. price/part | "Strut assembly" quoted on a shock-absorber vehicle; estimate tire size differs | Ask for clarification |
| C12 | Photo vs. history | Same belt yellow last visit, now red with no new evidence | Ask what changed |
| C13 | Duplicate image | Same image for two items/corners | "Two items appear to use the same photo." |
| C14 | Required vs. Suggested | Functioning but aged part priced as safety item | Map to MAP Suggested (see `technical-criteria.md`) |

---

## 6. Video review and frame sampling [METHOD]

No published DVI-video standard was found.

### 6.1 What video adds
- **Motion/play:** ball-joint, tie-rod, wheel-bearing play; belt gauge rocking (Gates test is lateral movement); tensioner flutter; engine-mount movement.
- **Active leaks:** drips forming in real time.
- **Function:** lights on/off, wipers on wet glass, warning lamps, scan-tool screens.
- **Continuity:** one continuous take from VIN/plate to the component links the defect to the vehicle better than separate stills.
- **Sound:** cannot be verified by Claude (section 1).

### 6.2 Narration vs. what is shown
- Summarize each narration claim; mark whether frames **show** it, are **consistent with** it, or **do not show** it.
- Common gaps: "see how much play" with no movement against a fixed reference; "pads almost gone" with no gauge; "this is leaking" over a dry part; a number spoken but not shown.
- Measurement demos: tool visibly seated correctly and readout legible in at least one frame. Reading spoken only → **Partial**.
- Play demos: need a fixed reference in frame (e.g., knuckle vs. control arm) and visible hand force. Whole-assembly movement with the hand is not joint play [UNVERIFIED as sourced rule; widely taught].

### 6.3 Frame sampling (Claude takes stills, not video)
Claude accepts JPEG/PNG/GIF/WebP; animated GIFs use only the first frame (Claude vision docs). Convert video to frames via user screenshots or `ffmpeg` in Claude Code.

1. Baseline grid: ~1 frame/s for clips < 60 s; ~1 per 2–3 s for longer.
2. Add frames at every narration claim, every gauge readout, and the start and end of every motion demo (rest vs. max displacement).
3. Add frames showing identity (VIN, plate, odometer).
4. Keep full resolution; don't downscale below scale legibility (high-res tier handles up to 2576 px long edge; larger is downscaled). Crop to the region of interest **in addition to** the full frame.
5. Label frames with timestamps ("Frame 00:14") for citation.

Limit: single frames lose motion. For play, compare rest vs. max-displacement frames against a fixed reference. If no difference is visible, report "cannot determine from sampled frames," not "no play."

---

## 7. Required phrasing and anti-accusation rules

### 7.1 Phrasing table [METHOD]

| Situation | Use | Avoid |
|---|---|---|
| Condition clearly shown with legible instrument | "The photo shows a gauge reading of about X, which **supports** the finding." | "Proven," "definitely" |
| Condition shown, not degree | "The photo is **consistent with** [condition], but it does not show how severe it is." | "Needs replacing" |
| Claim not shown | "The photo **does not show** [claim]." | "The shop is wrong," "false" |
| Can't tell | "This **cannot be determined from the photo**; [test] would confirm it." | Guessing a value |
| Photo contradicts claim | "The photo **appears inconsistent with** [claim] because [specific visible fact]. Worth asking the shop to clarify." | "Fraud," "lie," "fake," "scam" |
| Identity mismatch | "This photo **may not be from your vehicle**: [specific difference]. It could be a labeling mix-up; ask the shop." | "Doctored," "stolen photo" |
| Possible edit | "[Specific visual oddity] is visible. Image analysis can't confirm editing; ask for the original or an in-person look." | "Photoshopped," "AI-generated" |

### 7.2 Rules
1. Never assert fraud, intent, or fabrication. Describe observations and the gap between evidence and claim.
2. Absence of evidence ≠ evidence of absence. Missing gauge photo = *unsupported by the photo*, not *the part is fine*.
3. Prefer benign explanations first: mislabeling, template image, wrong car photographed, rotation history, typo.
4. Separate technical conclusion from evidence grade — a recommendation can be reasonable (e.g., OEM interval reached) with weak photos.
5. Always offer a verification path: ask for the measurement/test result; see the part in person or get old parts back; second opinion; for tires/pads, check with a gauge or coin.
6. Quote what is visible ("gauge needle at the '7' mark," not "plenty of pad").
7. State image-quality uncertainty (resolution, blur, glare, compression).
8. Never overrule an instrument reading with visual impression, unless the instrument is visibly misused (probe on a wear bar, gauge on the backing plate).

---

## 8. Computer-vision accuracy benchmarks

Purpose-built systems with controlled capture still state limits; a general model on an arbitrary DVI photo should be assumed less accurate and must not output numeric depth without a gauge in frame.

| System | Method | Claimed accuracy | Caveats |
|---|---|---|---|
| Anyline Tire Tread Scanner | Phone camera + CV, guided capture | Avg 0.5 mm (~1/32") for 1–10 mm depth; grooves ≥ 5 mm wide (vendor claim) | Datasheet calls it an estimate, no guarantee; not a roadworthiness verdict; limited by lighting, distance, shine, blur, resolution; needs ≥ 1080p (Anyline), (MOTOR) |
| UVeye Artemis/Atlas/Helios | Drive-through multi-camera AI | No tread tolerance published; CEO claim: detects 96% of problems vs. < 25% manual (vendor claim) | Not broken down by system; no independent test (RDN), (The Batch) [UNVERIFIED: exact article] |
| ProovStation + Michelin QuickScan | Drive-over magnetic sensors + cameras | "Millimeter precision" < 5 s (vendor claim) | No tolerance or independent data |
| Hunter Quick Tread | Drive-over 3D laser | "Most accurate," no tolerance; says handheld plunger gauges vary ~±2.4 mm by operator (vendor claim) | No published spec |
| Zebra Tread Intel | Handheld swipe scanner | Within 1/32" (0.79 mm) (vendor claim) | Fact sheet only |
| QBurst | Mobile image, multi-stage CNN | ±1.5 mm on 90% of test images (vendor case study) | ±1.5 mm ≈ ±2/32" — enough to flip pass/fail at 2/32 or 4/32 |
| Open demo (Hugging Face) | Single close-up, EfficientNet ensemble | Not validated | Demo only |

- Drive-over systems are affected by rain, snow, ice (US11421982 patent).
- No independent peer-reviewed accuracy study found [UNVERIFIED gap].
- Claude's accuracy on gauge-reading tasks is not benchmarked.

---

## 9. Per-photo checklist [METHOD]

For each photo or sampled frame:

1. **ID and claim** — photo #/frame time; which line item; what the report claims (condition, value, grade, recommendation).
2. **Quality** — focus, lighting, glare, resolution for scales/text, compression, rotation → Usable / Limited / Unusable.
3. **Identification** — component identifiable as claimed? Y / Partial / N.
4. **Position** — stated and visually consistent (side, axle, inner/outer)? Y / Unclear / Conflicts.
5. **Vehicle linkage** — VIN, odometer, plate, consistent wheels/tires/paint/size? Conflicts with other photos?
6. **Instrument** — present? Correctly applied (main groove, friction material only, strip vs. chart, printout rating matches label)? Readable value?
7. **What it shows** — plain observable terms, no interpretation.
8. **Can/cannot** — per section 2, what this component's photo inherently can't establish.
9. **Cross-checks** — C1–C14.
10. **Integrity** — possible duplicate? Crop hides context? Visual oddities? User-extracted EXIF consistent?
11. **Score** — rubric below.
12. **Finding + verification step** in plain language.

---

## 10. Evidence rubric and mapping to status labels

| Rating | Definition | Typical examples | What to say |
|---|---|---|---|
| **Strong** | Component identifiable, position clear, correctly applied instrument with legible reading (or unambiguous visible failure) supports the claim and grade; linked to the vehicle | Tread gauge at 2/32 in LF main groove + context shot; pad gauge at 2 mm on friction material; torn CV boot with slung grease; sidewall bulge; battery printout "Replace" at ~60% of label CCA; belt gauge rocking on video | "The photo supports this finding." |
| **Partial** | Consistent with the condition but doesn't establish degree, position, or all items; or instrument present but illegible/technique uncertain | Through-wheel outer pad, no gauge; one tire for four; wet strut with spring seat cropped; reading spoken not shown; refractometer with illegible scale | "Consistent with the finding, but it doesn't show [X]. Ask for [Y]." |
| **Weak** | Component shown, but condition is subjective or color/appearance-based where a valid test exists | Dirty-looking filter; dark brake fluid/ATF; "cracks" on EPDM belt; light strut film called leaking; dry residue called active leak; corrosion used to condemn a battery | "This photo alone isn't a reliable basis for the recommendation; [test] would be." |
| **None** | No photo; photo doesn't show the claimed component/condition; or unusable | No image; blurred/dark/unidentifiable; unlit headlamp for "bulb out" | "No photo evidence supports this item." |
| **Contradicts** | Visible content conflicts with claim, grade, value, or vehicle identity | Gauge 7/32 but text 2/32; green-looking item graded red; different tire size/wheel/paint; same image for LF and RF; film above spring seat called a leak requiring replacement | "The photo appears inconsistent with the claim because [specific visible fact]. This may be a mix-up; ask the shop." |

**Modifiers:** [ID?] vehicle linkage missing/questionable · [POS?] position unclear/conflicting · [DUP?] possible duplicate · [Q] image quality limits the conclusion.

**Roll-up per line item:** use the best supporting photo's rating — but if any photo is **Contradicts**, the item is Contradicts pending clarification.

**Mapping to SKILL.md status labels** (photo rating is one input; combine with `technical-criteria.md` thresholds and schedule):

| Photo rating | Default status | Adjustments |
|---|---|---|
| Strong | **Supported** (if threshold fails / Required) or **Supported – optional** (Suggested) | Strong photo of a passing measurement with a red grade → Inconsistent |
| Partial | **Evidence missing** | Upgrade to Supported / Supported – optional if non-photo evidence carries it (printout, OEM interval reached); → Needs OEM spec if the missing piece is the spec |
| Weak | **Evidence missing** | Same upgrades as Partial (e.g., OEM interval reached justifies a fluid service despite a color-only photo) |
| None | **Evidence missing** | Same upgrades |
| Contradicts | **Inconsistent** | Identity mismatch ([ID?]) also → Inconsistent, phrased as a possible mix-up |

**Safety override:** if any rating (including None or Contradicts) leaves a credible brake, tire, steering, suspension, or fuel-leak hazard, the status is **Verify in person – safety**. Weak photos never mean "ignore it."

---

## 11. Mode-specific notes

**Consumer**
- Output: per-item table of what the photo shows, rating, and what to ask for. Prioritize Strong safety items (approve or verify fast) and Weak/None/Contradicts items (ask before approving).
- Self-checks: coin test or a cheap gauge (penny ≈ 2/32") (Firestone); read DOT codes; compare tire size/brand with their car; check plate/wheels in context shots; look at their own wipers and lights.
- Ask the shop for: measurements with gauge photos, printouts (battery, strips), a look at the part on the lift, old parts back.
- Tone: mismatches are questions to clarify. Encourage a second opinion for expensive or Contradicts items. Never advise accusing the shop of fraud.
- Privacy: reverse image search uploads the photo to a third party.

**Shop owner / service manager**
- Measure per tech: share of red/yellow items with Strong evidence; items with no photo; color-only fluid calls; EPDM-crack belt calls; gauge-less pad/tread calls. Integrity flags: duplicate images across ROs, wrong-vehicle photos, position mislabels. Grade-vs-photo inconsistencies.
- Standards: gauge in frame for every quantitative finding; context + close-up; position labels; strips/refractometer for fluids; belt gauge for belts; dye/UV or cleaned recheck for leaks; battery printouts; VIN or odometer photo on every DVI.
- Spot audit: sample N ROs per tech per week, run the checklist, look for repeated images across ROs. Track Contradicts rate as a coaching metric, not a disciplinary verdict.
- Vendors push high photo counts (AutoVitals); evidence quality matters more than count.

---

## 12. Open uncertainties

Unknown: whether DVI platforms strip EXIF, re-compress, watermark, or insert canned images; C2PA adoption in DVI apps; prevalence of reused/mismatched DVI photos. Not retrieved: Monroe ServiceGram full text, Gates/Dayco hose guidance, current MAP UICS text, OEM statements on ATF/coolant color. No independent tread-scanner accuracy studies. Claude's gauge-reading accuracy is unbenchmarked (an internal labeled test set is recommended). Video sampling is reasoned, not validated.

---

## 13. Sources

1. Claude vision docs (Anthropic): https://platform.claude.com/docs/en/build-with-claude/vision
2. NHTSA interp. — 2/32" wear indicators: https://www.nhtsa.gov/interpretations/11497awkm
3. Ford — Tread wear: https://ford.com/support/how-tos/tires-and-wheels/tire-replacement-and-maintenance/why-does-tread-wear-matter
4. NAPA Know How — Reading tread depth: https://knowhow.napaonline.com/know-how-to-read-tire-tread-depth/
5. Michelin — Tire inspector (wear patterns): https://www.michelinman.com/auto/auto-tips-and-advice/tire-damage/tire-inspector-tool-tire
6. Jalopnik (Bridgestone on cupping): https://jalopnik.com/2074863/tire-wear-patterns-could-reveal-what-wrong-with-car/
7. Michelin — Sidewall symptoms: https://www.michelin.ca/en/auto/learn/tire-damage/sidewall-problems/symptom-indentation
8. Barry's Tire Tech (USTMA service-life statement): https://barrystiretech.com/tire-aging-and-weather-cracking/
9. SlashGear — DOT date codes: https://www.slashgear.com/1419676/numbers-tires-date-code/
10. Firestone — Date codes: https://www.firestonecompleteautocare.com/tires/tire-info/basics/tire-date-codes/
11. Firestone — When to replace / penny test: https://www.firestonecompleteautocare.com/tires/tire-info/buying-considerations/when-do-you-need-new-tires/
12. Phoenix Systems — Pad gauge (vendor): https://phoenixsystems.co/blogs/company-news-tips/how-do-i-measure-brake-pad-thickness-with-a-gauge
13. CarFromJapan — Pad thickness: https://carfromjapan.com/article/brake-pad-thickness
14. Saab WIS — Rotor inspection: https://saabwisonline.com/9-4x/2011/5-brakes/brake-discs-and-pads/fault-diagnosis-fault-symptoms/brake-rotor-surface-and-wear-inspection
15. Fras-le via Transport Operator: https://transportoperator.co.uk/?p=30722
16. Brake & Front End — Rotors/hard spots: https://www.brakeandfrontend.com/?p=39135
17. Phoenix Systems — Clean-looking brake fluid (vendor): https://phoenixsystems.co/blogs/company-news-tips/why-that-clean-brake-fluid-might-be-a-silent-problem
18. Phoenix Systems — Strip limits (vendor): https://phoenixsystems.co/blogs/company-news-tips/brake-fluid-test-strips-the-quick-check-that-tells-a-bigger-story-about-your-brakes
19. Rick's — Brake fluid color: https://ricksfreeautorepairadvice.com/the-truth-about-brake-fluid-color-and-brake-fluid-condition/
20. Ram Forum — ATF color: https://www.ramforum.com/threads/transmission-fluid-dark-before-30k-miles.137306/
21. BITOG — ATF color: https://bobistheoilguy.com/forums/threads/why-so-much-attention-toward-atf-color.40838/post-527180 ; https://bobistheoilguy.com/forums/threads/why-so-much-attention-toward-atf-color.40838/post-527175
22. Prestone UK (Holts) — Coolant colors: https://www.holtsauto.com/prestone/why-is-coolant-different-colours/
23. BITOG — Green vs. orange coolant: https://bobistheoilguy.com/forums/threads/green-vs-orange.229893/
24. BITOG — Coolant hydrometers (Cummins bulletin): https://bobistheoilguy.com/forums/threads/coolant-hydrometers.90700/
25. SAE 960645 — Coolant test strips: https://saemobilus.sae.org/content/960645
26. DTIC AD0750569 — Coolant field measurement: https://apps.dtic.mil/sti/tr/pdf/AD0750569.pdf
27. Donaldson — Air filter catalogue (vendor): https://ecatalog.donaldson.com/view/477292580/136/
28. CCJ — Donaldson service indicators: https://www.ccjdigital.com/business/article/14906155/think-that-air-filters-too-dirty-try-donaldsons-filter-service-indicators
29. BITOG — Cabin filter interval: https://bobistheoilguy.com/forums/threads/cabin-filter-change-interval.324421/
30. Gates TT002-15 — Belt inspection: https://www.gates.com/content/dam/documents-library/tech-tips-bulletins/tt002-15.pdf
31. CCJ — Gates belt-wear app: https://ccjdigital.com/business/article/14925015/gates-app-measures-serpentine-belt-wear
32. EngineerFix — Oil leak diagnosis: https://engineerfix.com/how-to-diagnose-an-engine-oil-leak/
33. YourMechanic — Oil leak source: https://yourmechanic.com/article/how-to-find-the-source-of-an-oil-leak-by-ed-ruelas
34. MotoIQ — UV dye: https://motoiq.com/wrench-tips-30-finding-oil-leaks-using-fluorescent-goo/
35. Monroe — Weepage vs. leakage: https://images.oreillyauto.com/parts/img/documents/mon/monroe_servicegram_weepageleakage_v01no05_eng_final.pdf
36. KYB — Leaking vs. sweating (2025): https://kyb-europe.com/wp-content/uploads/2025/08/Technical-Bulletin-Leaking-vs-Sweating.pdf
37. NHTSA-hosted TSB — Shock misting: https://static.nhtsa.gov/odi/tsbs/2020/MC-10170656-0001.pdf
38. Acurazine forum — CV joint: https://acurazine.com/forums/3g-tl-problems-fixes-114/cv-joint-%5B-913147
39. Utah Admin. Code R714-160-10: https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R714-160-10
40. Virginia 19VAC30-70-110: https://law.lis.virginia.gov/admincode/title19/agency30/chapter70/section110/
41. Midtronics — Printout clues (vendor): https://www.midtronics.com/blog/the-hidden-clues-in-battery-test-printouts-that-techs-might-miss
42. Midtronics — Healthy battery test (vendor): https://www.midtronics.com/blog/key-indicators-of-a-healthy-battery-test/
43. Rick's — Battery corrosion: https://ricksfreeautorepairadvice.com/does-corrosion-on-car-battery-terminals-mean-the-battery-is-bad/
44. ToolSource — Battery corrosion: https://www.toolsource.com/blog/battery-terminal-corrosion-safe-cleanup-testing-and-when-to-replace/
45. BITOG — Wiper blades: https://bobistheoilguy.com/forums/threads/replacement-wiper-blades.208727/latest
46. EngineerFix — Frame surface rust: https://engineerfix.com/is-surface-rust-on-a-frame-bad/
47. ToolSource — Tacoma frame rust: https://www.toolsource.com/blog/how-to-assess-and-repair-severe-frame-rust-on-tacomas-a-technicians-reality-check/
48. NI DVA — Structural integrity and corrosion: https://www.infrastructure-ni.gov.uk/articles/appendix-structural-integrity-and-corrosion
49. DVSA MOT blog — Corrosion: https://mattersoftesting.blog.gov.uk/why-its-important-to-check-for-corrosion/
50. AutoVitals — DVI best practices: https://blog.autovitals.com/digital-vehicle-inspection-best-practices
51. AutoServe1 — Photos in DVI: https://autoserve1.com/founder-protip-photos-improve-digital-vehicle-inspection/
52. Tire Review — DVI and trust: https://www.tirereview.com/digital-vehicle-inspection-shop-trust/
53. The Drive — Brake tampering case: https://www.thedrive.com/news/dealership-techs-caught-tampering-with-customers-brakes-police-say
54. Fast.io — Metadata stripping (vendor): https://fast.io/resources/social-media-photo-metadata-platforms-strip/
55. Google Security Blog — Pixel C2PA (Sept 2025): https://security.googleblog.com/2025/09/pixel-android-trusted-images-c2pa-content-credentials.html
56. FotoForensics — ELA tutorial / common mistakes: https://fotoforensics.com/tutorial.php?tt=ela ; https://fotoforensics.com/tutorial-mistakes.php
57. GIMP forensics wiki — ELA: https://sourceforge.net/p/gimp-forensics/wiki/Error%20Level%20Analysis/
58. Bellingcat — Reverse image search: https://www.bellingcat.com/resources/2015/05/08/manual-reverse-image-search-with-google-and-tineye/
59. Georgetown library — Verify images: https://guides.library.georgetown.edu/writ015day/verify
60. Data Detox Kit — Reverse search: https://datadetoxkit.org/en/misinformation/reversesearch/
61. arXiv 2602.15950 (preprint): https://www.arxiv.org/pdf/2602.15950
62. Roboflow — Claude vision evaluation: https://blog.roboflow.com/claude-fable-5-for-vision/
63. Anyline — Tread SDK datasheet: https://anyline.com/?p=25309
64. MOTOR — Anyline launch: https://www.motor.com/2022/11/anyline-launches-industry-first-tire-tread-scanner-for-smartphones-at-sema-show/
65. RDN — UVeye: https://www.repairerdrivennews.com/?p=152963
66. The Batch — UVeye: https://www.deeplearning.ai/the-batch/auto-diagnosis
67. Tire Technology International — ProovStation/Michelin: https://tiretechnologyinternational.com/news/testing-analysis/proovstation-partners-with-michelin-to-provide-automated-tire-and-vehicle-inspection.html
68. VehicleServicePros — ProovStation/Michelin: https://vehicleservicepros.com/service-repair/undercar/news/21292135/michelin-and-proovstation-partner-on-magnetic-tire-scanner
69. Fleet Maintenance — Hunter Quick Tread: https://www.fleetmaintenance.com/in-the-bay/tools/press-release/12022741/hunter-engineering-company-hunter-announces-quick-tread-drive-over-tread-depth-system
70. Zebra — Tread Intel fact sheet: https://prod-www.zebra.com/content/dam/zebra_dam/en/fact-sheet/zebra-tread-intel-fact-sheet-en-us.pdf
71. QBurst — Tire inspection case study: https://www.qburst.com/downloads/tire-inspection-system.pdf
72. Hugging Face — Tread demo: https://uncodespecial-tire-tread-depth.hf.space/
73. US11421982 — Drive-over tread patent: https://patents.google.com/patent/US11421982
