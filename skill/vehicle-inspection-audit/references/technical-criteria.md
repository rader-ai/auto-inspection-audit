# Technical Inspection Criteria

As of 2026-10-20. Light-duty cars, SUVs, and light trucks (gas, diesel where noted, hybrid, EV). Not heavy-duty/FMCSA (see `commercial-fleet.md`).

**Core caveat:** Most numbers here (pad minimum, rotor discard, ball-joint play, runout, fluid and plug intervals) are vehicle-specific. Figures labeled "typical" are plausibility checks, not substitutes for the OEM spec. When the outcome turns on one, use **Needs OEM spec**.

## Contents

1. General principles
2. Mapping findings to status labels
3. Per-system criteria
   - 3.1 Tires · 3.2 Brakes · 3.3 Alignment · 3.4 Fluids and flushes · 3.5 Filters · 3.6 Battery and charging · 3.7 Belts and hoses · 3.8 Wipers and lights · 3.9 Suspension and steering · 3.10 Exhaust, mounts, CV axles, wheel bearings · 3.11 Engine diagnostics, plugs, coils, "tune-up" · 3.12 A/C · 3.13 Hybrid and EV · 3.14 ADAS calibration
4. State inspection reject benchmarks (brief)
5. Impossible / not-applicable items checklist
6. Commonly upsold services
7. Per-line-item audit checklist
8. Open uncertainties
9. Sources

---

## 1. General principles

1. **The OEM schedule is the baseline.** The owner's manual / maintenance guide, or the car's maintenance reminder (Honda Maintenance Minder, GM Oil Life Monitor), defines required maintenance. AAA tells drivers to follow the manufacturer's schedule over generic intervals (AAA). Dealer software and "menu" maintenance often add items not in the manual (forum, anecdotal).
2. **Normal vs. severe service.** Severe conditions (towing, short trips, extreme heat/cold, dust, stop-and-go, mountains) vary by OEM. A shop using the severe schedule should name which condition applies to this driver. Defaulting every customer to severe is a red flag.
3. **Condition-based beats calendar-based when a valid test exists.** Brake fluid (copper strip, boiling point), coolant (pH, reserve alkalinity, freeze point), battery (conductance printout), belts (rib-wear gauge), tires (tread gauge, date code). A recommendation without the available test result is weaker.
4. **Measurement beats adjective.** "Pads low," "fluid dirty," "belt cracked," "strut leaking" are opinions. A legitimate finding gives value + unit + spec + location (e.g., LF inner pad), ideally with a photo or printout.
5. **A code is not a diagnosis.** A DTC names a failed monitored circuit or condition, not a failed part. Parts recommended from a code alone, without pinpoint tests, are unsupported.
6. **Mileage, age, and history context.** E.g., 120k-mile plugs recommended at 45k = early; coolant flush on a 2-year-old car with 10-year coolant = early.
7. **Required vs. Suggested (MAP, brief; detail in `industry-standards.md`).** Required: A = no longer performs its function, B = fails a design spec, C = missing. Suggested (always optional): 1 = near end of life, 2 = customer request/convenience, 3 = OEM maintenance, 4 = technician experience. Example: rotor above discard and not needing machining → replacement is Suggested only; below discard, or would be after machining → Required (MOTOR/MAP 1999). Current MAP manual text not verified.
8. **DVI colors are not standardized.** Red should map to Required (safety or failed spec), yellow to Suggested/monitor. Flag red items with no measurement or photo, and yellow items priced or presented as urgent.

## 2. Mapping findings to status labels

| Finding pattern | SKILL.md status |
|---|---|
| Measurement/test fails OEM or recognized threshold; evidence present | Supported |
| Legit maintenance at OEM interval, near-end-of-life wear, or comfort item | Supported – optional |
| Plausible, but no measurement, test, or probative photo | Evidence missing |
| Grade, measurement, photo, or note disagree; measurement passes but item marked red | Inconsistent |
| Maintenance earlier or more often than OEM (incl. unjustified severe schedule) | Beyond OEM schedule |
| Fails vehicle-fit check (section 5) | Not applicable to this vehicle |
| Judgment depends on a vehicle-specific number not in the documents | Needs OEM spec |
| Credible brake, tire, steering, suspension, or fuel-leak hazard | Verify in person – safety (overrides weak documentation) |

A measurement that passes the threshold makes a "replace now" recommendation premature: label it Supported – optional if presented as Suggested, Inconsistent if presented as red/Required.

---

## 3. Per-system criteria

Each system uses the same blocks: **How tested · Thresholds · Evidence a legit recommendation includes · Legitimate reasons · Red flags · Needs OEM spec · Questions to ask.**

### 3.1 Tires

**How tested**
- Tread gauge in 32nds (or mm), in the **lowest major groove**, at inner/center/outer on each tire; not on wear bars.
- DOT date code: last 4 digits of the TIN = week + year (2321 = week 23 of 2021). Pre-2000 used 3 digits (SlashGear).
- Visual: bulges, cuts exposing cords, cracking depth, impact breaks, bead damage.
- Puncture: tire must be dismounted and inspected from inside (USTMA).
- Pressure vs. door-placard spec (not sidewall max). TPMS: scan-tool reading per sensor (pressure, ID, battery status).

**Thresholds**

| Item | Threshold | Source |
|---|---|---|
| Legal minimum / wear bars | 2/32" (federal wear-bar height; legal minimum in most states; traction drops rapidly here). Some states differ or have front-axle rules [verify by state] | (NHTSA interp.), (Ford) |
| Recommended replace/shop point | 4/32" (wet braking); keep ≥ 4/32" through winter | (AAA), (CR via Tire Review) |
| Snow use | ~5–6/32" often advised [UNVERIFIED as a standard] | — |
| Age | No federal limit (NHTSA). Michelin: annual pro inspection after 5 yrs in service; replace at 10 yrs from manufacture regardless of tread, incl. spare. Several automakers (e.g., Ford, Nissan, Mercedes) cite 6 yrs from production — verify in the owner's manual | (NHTSA–NTSB), (Michelin), (ToolSource, secondary) |
| Puncture repairable | Injury ≤ 1/4" (6 mm); tread area only — not shoulder/belt edge/sidewall, not angled into shoulder; no overlapping repairs; never over a prior improper repair; dismount and inspect; plug/stem **plus** inner-liner patch (plug alone unacceptable); no outside-in or on-wheel repairs; run-flats per tire maker | (USTMA) |
| AWD matching | Many AWD OEMs set a max tread (or circumference) difference, commonly 2/32"–4/32" — vehicle-specific | — |

**Wear-pattern interpretation:** inner edge → negative camber and/or toe-out, worn bushings/springs; outer edge → positive camber/toe or hard cornering; center → over-inflation; both edges → under-inflation; feathering → toe; cupping/scalloping → worn dampers, imbalance, or no rotation (Brake & Front End), (Tire Review).

**Evidence a legit recommendation includes:** per-tire readings (ideally inner/center/outer) with position; DOT code read off the tire; damage photo; for "non-repairable" puncture, photo showing size and location relative to the shoulder; TPMS scan output naming the failed sensor (ID/battery/no signal).

**Legitimate reasons:** ≤ 2/32", cords, bulges, sidewall cuts → Required. 3–4/32" → Suggested (replace soon; stronger in wet/snow climates). > 10 yrs (or beyond OEM age guidance) → Suggested/Required per OEM. Puncture outside USTMA zone → replace. Wear pattern indicating alignment/suspension issue → alignment check plus related-component inspection.

**Red flags**
- "Replace all four" on a non-AWD vehicle when only one or two are worn and the rest are > 4/32".
- Tires at 5–7/32" graded red/urgent. Readings all identical round numbers, or not matching photos.
- "Can't be repaired" for a small tread-center nail without explanation. Conversely, plug-only or shoulder repairs are substandard (shop liability).
- Age-based replacement under ~6 yrs with no visible degradation.
- Four TPMS sensors when one failed (unless shared age/battery readings justify it — still Suggested).
- Nitrogen fills sold as safety (air is already ~78% nitrogen) (CR via Quartz).

**Needs OEM spec:** AWD max tread/circumference difference; automaker tire-age limit; placard pressure.

**Questions:** What did each tire measure, where, and what is the date code? Where is the puncture relative to the shoulder? Which TPMS sensor failed and what did the scan show? Is the uneven wear from alignment or a worn part — which one?

### 3.2 Brakes

**How tested**
- Wheels off. Pad friction material in mm **excluding the backing plate** (~5 mm steel; including it is a common inflation error) (forum). Measure inner and outer — inner often wears faster.
- Rotor thickness by outside micrometer at several points ~1/4" in from the edge; compare to **discard/minimum** stamped on the rotor and to the separate **machine-to** minimum in OEM data (Hella Pagid), (GM spec).
- Lateral runout: dial indicator, lugs torqued (or conical washers), caliper off. Thickness variation (DTV): micrometer at multiple points (Tomorrow's Technician), (Vehicle Service Pros).
- Drum: inside diameter vs. max cast in drum; shoe lining thickness.
- Fluid: copper strip (ppm Cu), moisture/boiling-point tester, or OEM time interval.
- Caliper: slide-pin freedom, piston seal/boot, leaks, uneven inner/outer wear, sticking (heat/drag).

**Thresholds**

| Item | Threshold | Source |
|---|---|---|
| Pad minimum | Vehicle-specific; many OEM specs ~2.0 mm lining. Many shops recommend at ~3 mm (a Suggested point, not Required) [typical]. New pads ~10–12 mm [typical] | (Saab/GM WIS) |
| Rotor | Below discard → Required. Above discard but below machine-to after refinishing → Required if refinishing is needed. Above both, no pulsation/scoring/DTV → no service required; replacement at most Suggested | (MOTOR/MAP) |
| Runout | OEM-specific; ~0.002" (0.05 mm) commonly cited good-condition limit; > 0.005" likely pulsation | (Phoenix Systems), (Brake & Front End) |
| DTV | Often ≤ 0.0005–0.001" | same |
| Brake fluid (test) | Copper ≥ 200 ppm = depleted inhibitors → replace (described as MAP standard; reported via a vendor — treat with caution) | (Phoenix Systems, vendor claim) |
| Brake fluid (time) | Most OEMs 2–3 yrs (AAA); Honda every 3 yrs regardless of Minder; Tesla check every 4 yrs, replace if needed. Some OEMs list long or no fixed interval | (AAA), (Honda dealer guide), (Tesla) |

- Hub-to-rotor rust is the leading runout cause — cleaning the hub may fix it without parts.
- "Warped rotors": pulsation is usually DTV from runout/uneven deposits, not literal warping (Rick's).
- **Fluid color alone is not a valid test.** Conductivity moisture "pens" are considered less reliable than strips or boiling-point testers [UNVERIFIED — industry opinion].

**Evidence a legit recommendation includes:** pad mm per wheel and per pad (inner/outer) with OEM minimum cited; rotor readings vs. stamped discard and machine-to; runout reading if pulsation claimed; photo of the measurement; fluid strip photo next to its chart, or a boiling-point reading.

**Legitimate reasons:** pads at/below OEM minimum, metal-to-metal, wear-indicator squeal, cracked/delaminated lining, oil/fluid contamination. Rotor below discard, deep scoring, heat cracks, DTV causing pulsation. Caliper seized/leaking/torn boot causing uneven wear. Fluid ≥ 200 ppm Cu, low boiling point, or past OEM interval.

**Red flags**
- "Pads at 4 mm — replace now" labeled Required (Suggested at most).
- Automatic rotor replacement on every pad job with no thickness reading. Acceptable only if disclosed as shop policy/Suggested and priced transparently.
- Calipers sold routinely ("loaded calipers") without leak/sticking evidence.
- Fluid flush based on color ("it's dark"); flush at 12 months on a 3-year OEM interval with no test.
- Measurement that includes the backing plate; pad readings that differ wildly from photos.
- Hybrid/EV pads "worn" at low mileage — implausible given regen unless rust/seized slides (see 3.13).

**Needs OEM spec:** pad minimum, rotor discard and machine-to, runout/DTV limits, drum max diameter, fluid interval.

**Questions:** What were the pad and rotor measurements, and what is the minimum for my car? Is the rotor below discard, or would it be after machining? Can I see the strip test or boiling-point reading? Is the caliper actually leaking or seized?

### 3.3 Alignment

**How tested:** four-wheel alignment machine; tires at spec pressure; ride height checked; steering/suspension inspected first (worn parts make alignment meaningless). Printout shows camber, caster, toe (and thrust angle, SAI where relevant) **before and after** against OEM min/max.

**Thresholds:** OEM ranges (vehicle-specific). Out-of-spec "before" values are the justification. Many cars have non-adjustable camber/caster; shop may only set toe unless a kit is installed.

**Legitimate reasons (indicated when):** pull/drift, off-center wheel, abnormal tire wear (edge wear, feathering), significant pothole/curb impact, after replacing tie rods/control arms/struts or lowering/lifting; with new tires = optional/Suggested (Continental). Off-center wheel can also be worn components.

**Evidence:** before/after printout with spec columns; symptom or wear-pattern description; tire photos.

**Red flags**
- No symptom, no wear pattern, no impact, no parts replaced, and no out-of-spec "before" readings.
- "Alignment done" with after = before, or no printout.
- Alignment sold while worn tie rods/ball joints are noted but not fixed (it won't hold).
- Camber adjustment billed on non-adjustable camber with no kit.
- "Lifetime alignment" — a value question, not a technical need.
- Note: alignment may trigger ADAS calibration / steering-angle-sensor reset on many vehicles (3.14).

**Needs OEM spec:** angle ranges; which angles are adjustable.

**Questions:** May I see the before printout? Which angles were out of spec? What changed (impact, parts) to cause it?

### 3.4 Fluids and flushes

**General rule:** compare every fluid service to the OEM schedule for this mileage/age and the applicable normal/severe condition. Ask "Where is this in my maintenance guide?" (Rick's). Fluid color is not a valid condition test for brake fluid, ATF, or coolant (see `image-evidence.md`).

**Engine oil**
- How determined: OEM oil-life monitor or OEM mileage/time interval; correct viscosity/spec (API SP/ILSAC GF-6, dexos, OEM approvals).
- Thresholds: AAA calls the 3,000-mile rule a myth; for vehicles ≤ ~15 yrs old, typical intervals 5,000–7,500 mi, up to ~15,000 with full synthetic where OEM allows (AAA). GM's OLM research found oil often ran 10,000–12,000 mi before significant degradation; temperature/operating conditions matter more than miles (STLE).
- Legit: OLM ≤ 15%, OEM interval reached, low level (find why), contamination (coolant/fuel) — a diagnostic finding, not just an oil change.
- Red flags: 3,000-mile stickers on 7,500–10,000-mile OEM intervals; resetting OLM early; "engine flush" additives (generally not OEM-specified; some OEMs advise against) [UNVERIFIED as universal].

**Automatic / CVT / DCT fluid**
- How determined: OEM schedule (many list "inspect" under normal use, replace under severe); OEM level-check method (many sealed units have no dipstick and need a temperature-specific check-plug procedure).
- "Lifetime/sealed" often means warranty-period or normal-use life. Treat replacement as **Suggested** unless the OEM schedule calls for it, severe use applies, or fluid is burnt/contaminated/low.
- Drain-and-fill replaces ~25–50% depending on design (forum reports); machine exchange replaces more. Some specialists prefer repeated drain-and-fills on neglected high-mileage units, citing debris risk [anecdotal — UNVERIFIED as engineering consensus].
- Errors: flush machine where OEM specifies drain-and-fill only; "universal" fluid where OEM requires a specific fluid (Toyota WS, Honda ATF DW-1/HCF-2, CVT fluids).
- Red flags: flush on a low-mileage vehicle outside schedule; judged by color/smell only; universal fluid on invoice; flush sold to "fix" shifting without diagnosis.

**Coolant**
- How determined: OEM interval (many long-life coolants first change ~100,000–150,000 mi or ~10 yrs, then shorter [typical; verify]); refractometer for freeze point; strips for pH and reserve alkalinity; visual for oil/contamination.
- Thresholds: freeze protection per climate (often ~−34°F at 50/50) [typical]; pH below ~7–8 = depleted inhibitors → replace (CDX). Freeze point alone says nothing about corrosion protection.
- Legit: failed pH/RA strip, poor freeze protection, contamination (oil, rust, sludge), OEM interval reached, repair requiring drain.
- Red flags: flush at 30k–60k on 10-year coolant without a failed test; universal "all-makes" coolant replacing OEM type; color-only basis. Autoblog lists routine coolant replacement as a classic upsell unless contaminated or very high mileage (Autoblog).

**Power steering fluid:** many OEMs list inspect-only. Electric power steering (EPS) has **no fluid** — a PS flush on EPS is not applicable. Legit: OEM interval, contamination, noise/hard steering with diagnosis.

**Differential / transfer case / manual transmission:** OEM schedules commonly specify gear-oil change at 30k–60k under severe use (towing); longer or inspect-only under normal use [vehicle-specific]. Legit for AWD/4WD that tow. Red flags: diff service on a FWD car (shares the transaxle); front and rear diffs billed on a 2WD vehicle.

**Fuel system / induction / throttle body cleaning:** generally **not** in OEM schedules; Top Tier gasoline is designed to keep injectors clean; some OEMs reportedly issued bulletins against unneeded fuel services (Rick's), (Haynes) [bulletin specifics UNVERIFIED]. Exceptions are **diagnosis-driven**: OEM TSBs for intake-valve carbon cleaning on specific direct-injection engines; throttle-body cleaning for an idle/drivability complaint. Red flags: mileage-based "fuel induction service" at 15k/30k/45k; injector cleaning without a misfire/lean code, fuel-trim data, or flow test.

**Brake fluid:** see 3.2.

**Dealer menus:** often bundle fuel induction, throttle body, coolant/trans/PS flushes, "multi-point" fees at round-number milestones. Audit each line against the OEM guide; anything not listed is optional and should be labeled so (forum examples).

**Needs OEM spec:** every fluid interval (normal and severe), fluid type/spec, level-check procedure, drain-and-fill vs. exchange.

**Questions:** Is this in my maintenance schedule at this mileage (normal or severe)? What test result shows the fluid is degraded? What fluid will you use, and does it meet the OEM spec? Flush or drain-and-fill, and why?

### 3.5 Filters

**Engine air filter**
- How judged: visual (against light) for debris/blockage; OEM interval (often 15k–30k normal, shorter for dust) [vehicle-specific]; some cars show it on the maintenance reminder.
- Legit: visibly clogged, damaged, contaminated (oil, water, rodent nest), or OEM interval reached. Replace only when clogged (Autoblog).
- Red flags: lightly gray intake side shown as "dirty" (normal); recommended at every oil change; photo doesn't match the vehicle's filter shape; price far above part + minimal labor (many are tool-free).

**Cabin air filter**
- OEM intervals commonly ~1–2 yrs or 15k–30k mi; e.g., Tesla Model 3 every 2 yrs (yearly in China) (Tesla).
- Legit: debris/leaves, odor, reduced airflow, interval reached. Red flags: as above; another vehicle's filter in the photo (photo reuse is a known DVI integrity issue).

**Needs OEM spec:** both intervals.
**Questions:** Can I see my actual filter? When was it last replaced?

### 3.6 Battery and charging

**How tested:** conductance tester (Midtronics-type) with the correct rating **type and value** entered (CCA SAE vs. EN vs. JIS); state of charge; resting voltage; charging-system test (alternator output, ripple/diode); starter draw. Results: Good / Good-Recharge / Charge & Retest / Replace / Bad Cell. Surface charge and low state of charge can produce a false Replace — tester should charge and retest.

**Thresholds**

| Item | Threshold | Source |
|---|---|---|
| Measured vs. rated CCA | Healthy ≥ ~80–90% of rated; 70–79% marginal; < 70% replace (sources vary) | (Midtronics, vendor), (Rotronics) |
| Wrong rating entered | Can produce a false Replace | (GM TechLink) |
| Resting voltage | ~12.6 V full; < 12.4 V low charge [typical] | — |
| Age | Typically 3–5 yrs; test from ~year 3; heat shortens life | (AAA), (WECT/AAA regional) |

**Evidence:** printout with rated vs. measured CCA, voltage, decision, date/time; battery date code; charging-system result.

**Legitimate reasons:** Replace/Bad Cell on a properly charged battery; slow cranking with failing test; swollen/leaking case; age plus marginal result (Suggested).

**Red flags:** "battery weak" with no printout; wrong rating entered (e.g., 500 CCA for a 750 CCA battery); age-only replacement on a battery testing Good; "Charge & Retest" reported as "Replace"; flooded battery in an AGM vehicle; missing battery registration where the OEM requires it (BMS-equipped).

**Needs OEM spec:** battery type (AGM/flooded), rating, registration requirement.
**Questions:** May I have the printout? What rating was entered? Was it charged and retested?

### 3.7 Belts and hoses

**How tested**
- Serpentine (EPDM): rib-wear gauge or Gates app measuring material loss in rib valleys. **Crack counting is obsolete for EPDM** — "3 cracks in 3 inches" applied to older neoprene belts; EPDM can run ~100,000 mi with few/no cracks yet be worn by material loss (Gates).
- Tensioner: arm movement/bounce, wear-indicator marks, pulley bearing noise/wobble, misalignment.
- Timing belt: OEM interval (time and miles); not visually judged in most cases.
- Hoses: squeeze test (soft/swollen/hard), cracks, clamp leaks, bulging; cooling-system pressure test if leak suspected.

**Thresholds:** gauge seats flush = OK; rocks laterally = replace. Chunks missing, rib separation, cord visible, glazing with noise = replace. Timing belt per OEM (often 60k–105k mi or ~7–10 yrs) [vehicle-specific]; many engines have chains with no interval.

**Evidence:** photo of gauge on belt; tensioner observation; hose photo showing crack/leak; pressure-test result.

**Red flags:** "belt has cracks" on EPDM as the sole reason; timing belt on a chain engine; "water pump while you're in there" with no timing-belt job (cost-saving Suggested only when the pump is belt-driven and accessed anyway); hose replacement on appearance alone.

**Needs OEM spec:** timing belt vs. chain; timing-belt interval; whether the water pump is timing-belt-driven.
**Questions:** Did you use a belt-wear gauge? Does my engine have a timing belt or chain? Is the hose leaking or just old-looking?

### 3.8 Wipers and lights

- **Wipers:** streaking, chatter, torn/hardened rubber, frame damage. Legit Suggested item; Required only if visibility is impaired. Red flags: high labor for tool-free blades; "replace" on blades that wipe cleanly.
- **Lights/bulbs:** function check of all exterior lamps (low/high, turn, brake incl. CHMSL, reverse, plate, markers). Burnt-out lamp = Required (legal). Headlamp lens restoration = Suggested unless output/inspection fails. Red flags: "upgrade" bulbs; LED/HID assemblies quoted when a bulb is the issue. Replacing headlamps in pairs for color/output match is reasonable as Suggested.
- **Questions:** Which bulb is out? Is the lens restoration for safety or cosmetics?

### 3.9 Suspension and steering

**How tested**
- On a lift, wheels unloaded or loaded per OEM procedure. Ball joints: dial indicator for axial/radial play vs. OEM spec, or built-in wear indicator (raised shoulder/pin must protrude) (AA1Car), (Brake & Front End). Load-carrying vs. follower procedure depends on spring position.
- Tie rods/inner joints: grip-and-shake; dry-park check (wheel rocked, wheels on ground, watching joints).
- Shocks/struts: symptoms (bounce, nosedive, body roll, cupping), leak inspection, mount/bushing condition, road test.
- Bushings: tearing, separation, movement under pry.

**Thresholds**
- Ball-joint play: **OEM-specific** (many load-carrying joints allow zero; some allow small values).
- **Misting vs. leaking:** a light film/weep near the upper seal is normal and does not need replacement; a leak is fluid wet over most of the body, or dripping/streaming (Monroe), (KYB), (NZTA).
- Bounce test is crude; gas-charged dampers may pass while worn; not adequate sole evidence [UNVERIFIED single source]. Mileage-based strut replacement ("every 50,000 miles") is marketing guidance, not an OEM requirement in most cases [UNVERIFIED].

**Evidence:** measured play vs. spec, or video of the movement; photo of wet/dripping damper (not dust-coated mist); cupping photos; road-test notes.

**Legitimate reasons:** play beyond OEM spec; torn boots with grease loss; clunks with confirmed looseness; dripping dampers; broken springs; bent parts.

**Red flags:** "struts leaking" photo shows dry dust film/mist; all four struts plus mounts "as a set" at 40k with no symptom; "ball joints worn" without measurement on a joint with an intact wear indicator; lifetime-lubricated joints "need grease."

**Needs OEM spec:** ball-joint play and procedure; tie-rod limits.
**Questions:** How much play, and what is the spec? Dripping or just misting? Can I see the video/photo?

### 3.10 Exhaust, mounts, CV axles, wheel bearings

| Component | How tested | Legit | Red flags |
|---|---|---|---|
| Exhaust | Sound, soot trails, smoke test; rust-through, hangers. P0420/P0430 need diagnosis (O2 data, exhaust leaks, misfire history) before condemning the converter | Holes, broken hangers, confirmed leak, diagnosed converter failure | Converter from code alone (high-value line — CarMD lists it among the most frequent/costly CEL repairs); surface rust called failure |
| Engine/trans mounts | Torn/collapsed rubber, hydraulic fluid loss, excess movement in power-brake test (D/R with brake held) | Failed mount with excess movement | All mounts replaced when one failed; "cracked" surface rubber without excess movement |
| CV boots/axles | Torn boot slinging grease; clicking on turns = outer joint; inner-joint vibration on acceleration | Early tear → boot may suffice; long-torn, contaminated → axle | Axle for a "dry" boot with no tear; grease from another source |
| Wheel bearings | Noise changing with speed/load (swerve test), play rocking at 12/6 o'clock, roughness spinning, ABS wheel-speed codes; hub-unit endplay often ~zero [vehicle-specific] | Confirmed noisy/loose bearing | Both sides when one is noisy (pair = Suggested at most); "bearing noise" that is actually tire cupping |

State note: Virginia's inspection rules treat torn CV boots as advisory, not reject (see `image-evidence.md`).
**Needs OEM spec:** bearing endplay.
**Questions:** Where is the leak/tear — photo? What test confirmed the converter failed? Which bearing, and how was it confirmed?

### 3.11 Engine diagnostics, plugs, coils, "tune-up"

- **CEL/DTC:** proper diagnosis = code + freeze-frame + live data (fuel trims, O2/AF, misfire counters) + pinpoint tests per OEM/industry trees + TSB check. A diagnostic fee is legitimate; replacing parts named by the code without testing is not. Top CEL repairs historically: O2 sensor, catalytic converter, ignition coil/plug, loose gas cap (CarMD).
- **Spark plugs:** OEM intervals commonly ~60k–120k for platinum/iridium (e.g., Toyota iridium ~120k; Honda via Minder code 4) [verify per model]. Legit: interval reached, misfire traced to plug (gap erosion, fouling, cracked insulator). Red flags: plugs at 30k on a 100k+ interval; "tune-up" packages.
- **Ignition coils:** replace coils proven bad (swap test, misfire follows coil, scope/spark test). Red flag: all coils for one misfire without testing (all-coils = Suggested at most on high mileage).
- **"Tune-up":** obsolete term for modern engines. Must be decomposed into specific OEM items (plugs, filters); otherwise an unsupported bundle.
- **Needs OEM spec:** plug interval; TSBs.
- **Questions:** What codes, and what tests confirmed the part is bad? Did you check TSBs? Is this at the OEM plug interval?

### 3.12 A/C

- **How tested:** vent temp vs. ambient/humidity chart; high/low pressures; leak detection (UV dye, electronic sniffer, nitrogen pressure/vacuum decay); compressor operation; refrigerant ID (R-134a vs. R-1234yf); recover/recharge by weight per OEM charge.
- **Legit:** poor cooling with low charge **and** located leak; verified compressor failure; clogged cabin filter.
- **Red flags:** "recharge" without leak test (refrigerant isn't used up — low charge means a leak); "A/C performance service" as mileage maintenance; sealer-containing top-off cans (can damage system and shop recovery equipment); undisclosed R-1234yf price inflation. Evaporator cleaning/deodorizing = Suggested/comfort only.
- **Questions:** What were outlet temp and pressures? Where is the leak? How much refrigerant was recovered vs. spec?

### 3.13 Hybrid and EV

- **12 V battery:** present in most hybrids/EVs and a common failure; test the same way; often AGM — replacement must match type.
- **HV battery state of health:** from OEM scan tool (e.g., Toyota hybrid health check) or OEM report. Per-block voltage deltas, internal resistance, or capacity are more informative than pass/fail. Replacement needs scan data and OEM DTCs; check warranty (federal emissions and state rules often cover HV batteries 8 yrs/100k, 10 yrs/150k in CARB states) [UNVERIFIED — see `federal.md`]. HV work requires trained techs and OEM safety procedures.
- **Brakes:** regen does much of the slowing, so pad/rotor wear is typically much lower; common problems are rotor corrosion and seized slides from under-use [UNVERIFIED single source]. Low-mileage pad replacement needs measurement scrutiny. Brake fluid still per OEM (Tesla: check every 4 yrs).
- **Coolant loops:** separate circuits (engine, inverter/power electronics, battery thermal) with distinct OEM fluids, intervals, and bleed procedures (sometimes scan-tool pump activation). Red flag: generic "coolant flush" on an EV or wrong spec.
- **No-fluid items on EVs:** no engine oil, spark plugs, engine air filter, timing belt, or exhaust. EV reduction-gear oil intervals are OEM-specific (some "lifetime").
- **Questions:** Can I see the scan-tool SoH/block data? Is this covered by HV warranty? Which coolant loop and which fluid?

### 3.14 ADAS calibration

- **When required:** per OEM position statements/repair procedures. Common triggers: windshield replacement (camera on glass), camera/radar removal or replacement, bumper/grille work near radar, collision damage, ride-height/suspension changes, and on many makes after alignment (thrust/steering angle changes). The OEM procedure is authoritative, not a generic rule (BodyShop Business), (Brake & Front End). Improperly calibrated cameras can impair performance (IIHS via RDN). Steering-angle-sensor reset after alignment is a separate, commonly required step.
- **Evidence:** citation of the OEM procedure; pre/post scan report; calibration report (static targets or dynamic drive) showing completion.
- **Red flags:** calibration billed on a vehicle without the feature; no calibration report; "radar" billed on a camera-only system. Inverse risk: skipping calibration when OEM requires it (shop liability).
- **Needs OEM spec:** whether this repair triggers calibration for this model.
- **Questions:** Which OEM procedure requires this? May I have the calibration report and post-scan?

---

## 4. State inspection reject benchmarks (brief)

Official reject criteria are legal minimums, not maintenance guidance — but a shop cannot honestly call a part a "state inspection failure" if it meets them. Full detail: `state-inspection-programs.md`.

| State | Pads/linings | Tires | Other notes |
|---|---|---|---|
| PA (67 Pa. Code §175.80) | Bonded < 2/32"; riveted < 1/32" above rivet; rotor below min; scoring > 0.015" | < 2/32" in two adjacent grooves | Ball-joint play beyond mfr spec; shocks rocking past 3 cycles; any exhaust leak. Brake and tire measurements must be written on the receipt/work order |
| VA (19VAC30-70-80, -130) | < 2/32" at any point; pad-wear light alone is not a reject | < 2/32" in two adjacent grooves at 3 spots | Torn CV boots not rejected |
| VT (VN-113) | Below OEM minimum (not fixed 2/32") | Reject < 2/32"; **advise only** 2/32–4/32", > 8 yrs old, weather cracking | Model two-tier Reject/Advise structure |
| TX | No non-commercial safety inspection since 1/1/2025 | — | "Needed to pass state inspection" on a non-commercial TX vehicle is factually wrong |

---

## 5. Impossible / not-applicable items checklist

Any hit → **Not applicable to this vehicle**. High-signal for templated or copied content.

**Wrong for the configuration**
- [ ] Power-steering flush/fluid on electric power steering (EPS)
- [ ] Timing belt (or "water pump with timing belt") on a timing-chain engine
- [ ] Rear differential service on a FWD car (shares the transaxle); front and rear diffs on a 2WD vehicle
- [ ] Transfer-case service on a vehicle with no transfer case
- [ ] EV: engine oil, oil filter, spark plugs, engine air filter, timing belt, exhaust, fuel induction/injector service
- [ ] ADAS calibration for a feature the vehicle doesn't have; "radar" calibration on a camera-only system
- [ ] Camber adjustment on non-adjustable camber with no kit installed
- [ ] "Grease" service on lifetime-lubricated joints
- [ ] Tire sizes or wheel count not matching the vehicle/placard; wrong engine in the report

**Physically implausible (→ Inconsistent unless explained)**
- [ ] Pad thickness above new (~10–12 mm typical) or a reading that includes the backing plate
- [ ] All four tires with identical round-number readings
- [ ] Hybrid/EV pads "worn out" at low mileage with no rust/seized-slide finding
- [ ] Cords showing on months-old tires with no damage/alignment note

**Spec mismatch (parts/fluids on invoice)**
- [ ] Universal ATF or coolant where OEM requires a specific fluid (Toyota WS, Honda DW-1/HCF-2, CVT fluid, OEM coolant type)
- [ ] Flooded battery in an AGM vehicle; no registration where OEM requires it
- [ ] Wrong oil spec (e.g., dexos-required vehicle)
- [ ] Flush machine where OEM specifies drain-and-fill only

---

## 6. Commonly upsold services

Roughly by frequency in consumer guidance (source quality varies):

1. Fluid flushes (transmission, coolant, power steering, brake) without test or OEM interval (Autoblog), (Haynes)
2. Fuel system / injection / induction / throttle-body cleaning (Rick's), (Haynes)
3. Premature brake jobs — Haynes calls brake jobs probably the most common unnecessary repair (Haynes)
4. 3,000-mile oil changes / early OLM resets (AAA)
5. Engine and cabin air filters shown "dirty" every visit (Autoblog)
6. New tire instead of a USTMA-compliant repair; full sets when only some are worn (Autoblog)
7. Nitrogen fills (CR via Quartz)
8. Alignment with no symptom or "before" readings
9. Struts/shocks on mileage or misting alone
10. Batteries without a printout
11. "Tune-ups" and mileage-milestone dealer menus
12. A/C recharge without leak diagnosis

Context: a 1,000-consumer commercial survey found upselling unnecessary repairs was the most reported problem (ConsumerAffairs; moderate reliability). CarMD's index historically ranks O2 sensors, catalytic converters, and coils/plugs as top CEL repairs (CarMD).

Consumer red-flag phrases: "while we had it apart," "it's due" (no schedule reference), "it's dirty/dark," "lifetime fluid is a myth so we flush it," "highly recommended" with no measurement.

---

## 7. Per-line-item audit checklist

For every inspection, estimate, and invoice line:

1. **Classify:** maintenance (schedule) / repair (condition) / diagnostic / optional-comfort.
2. **Vehicle fit:** run section 5. Hit → Not applicable to this vehicle.
3. **OEM schedule match (maintenance):** listed at this mileage/age? Normal or severe — if severe, which condition? Not listed → Supported – optional at most; earlier than OEM → Beyond OEM schedule; done recently per history → Inconsistent.
4. **Measurement present (repair):** value + unit + location + spec? Missing → Evidence missing (or Needs OEM spec if the spec is the gap).
5. **Threshold test:** fails OEM/recognized threshold → Required/Supported. Passes → premature (Supported – optional if labeled Suggested; Inconsistent if red/Required).
6. **Evidence quality:** photo of *this* vehicle, instrument legible, printouts (battery, alignment, scan, calibration), strip-vs-chart. Rate per `image-evidence.md`.
7. **Internal consistency:** tread vs. tire claim; pad mm vs. red; hybrid brakes at low miles; EV with oil/plugs; EPS with PS flush; FWD with rear diff; belt on chain engine.
8. **Severity labeling:** red/Required only for safety, legal, or failed-spec items. Yellow priced as urgent = finding.
9. **Bundling and sets:** "while you're in there" items justified individually; pairs/sets beyond what failed only if OEM requires (e.g., AWD matching) or disclosed as Suggested.
10. **Parts/fluid spec:** invoice part/fluid meets OEM spec.
11. **Invoice vs. estimate:** performed = authorized; labor plausible (pricing covered elsewhere).
12. **Diagnostic logic (CEL):** code → tests → conclusion documented; TSB checked.
13. **Safety override:** credible brake, tire, steering, suspension, or fuel-leak hazard → Verify in person – safety, whatever the documentation.

**Consumer mode:** ask for measurements, photos, printouts, old parts; use the per-system questions; approve Required safety items now, defer or second-opinion Suggested items. Self-checks: read DOT codes; penny ≈ 2/32", quarter ≈ 4/32" (crude) [UNVERIFIED as exact]; check the owner's manual schedule; check whether the car has EPS / a timing chain.

**Shop-owner mode:**
- Require numeric fields: tires per position, pads inner/outer friction only, rotors vs. discard/machine-to, battery printout, alignment before/after, fluid test results; photos for every red/yellow item.
- Require OEM spec lookup over rules of thumb; e.g., a DVI legend "3 mm = red" when OEM minimum is 2 mm should be re-labeled yellow/Suggested.
- Watch for reused/stock photos, wrong-vehicle photos, mismatched mileage.
- Label non-OEM menu items optional; never "manufacturer recommended."
- Under-service liability (inverse risk): plug-only or shoulder tire repairs, universal fluids in OEM-specific transmissions, skipped ADAS calibration/SAS reset, wrong battery type or missing registration.
- Correlate high-upsell techs with low measurement-documentation rates; map each DVI status to a MAP reason code.

---

## 8. Open uncertainties

Not verified to primary sources: current MAP UICS text (logic from 1999 MOTOR article; 200 ppm Cu via vendor); CR 4/32" data (paywalled); automaker 6-year tire-age guidance; Midtronics CCA percentages (sources differ 70/80/90%); transmission-flush risk on neglected units; OEM bulletins against fuel services; hybrid/EV pad wear and HV warranty terms. Runout/DTV are trade figures. Ball-joint play, bearing endplay, AWD mismatch, fluid intervals, and severe-service qualification are vehicle- or OEM-specific → Needs OEM spec.

---

## 9. Sources

1. AAA — Debunking maintenance myths: https://www.aaa.com/autorepair/articles/debunking-common-myths-about-car-maintenance
2. USTMA — Tire repair basics: https://www.ustires.org/tire-care-safety/tire-repair-basics
3. USTMA — Puncture repair procedures (PDF): https://www.ustires.org/system/files/2026-06/Puncture%20Repair%20Procedures%20for%20Passenger%20and%20Light%20Truck%20Tires.pdf
4. NHTSA interp. — 2/32" wear indicators: https://www.nhtsa.gov/interpretations/11497awkm
5. NHTSA–NTSB 2016 tire response: https://www.nhtsa.gov/document/nhtsa-ntsb-response-may-2016-passenger-vehicle-tire-safety-tire-registration-tire-recalls
6. Ford — Tread wear: https://www.ford.com/support/how-tos/tires-and-wheels/tire-replacement-and-maintenance/why-does-tread-wear-matter/
7. Michelin — When do I need new tires: https://www.michelinman.com/auto/auto-tips-and-advice/tire-buying-guide/when-do-i-need-new-tires
8. CR — Worn tire performance (paywalled): https://www.consumerreports.org/tires/what-happens-to-performance-when-tires-are-worn/
9. Tire Review — Treading close to limits: https://www.tirereview.com/treading-close-to-limits/
10. Tire Review — Wear patterns: https://www.tirereview.com/?p=156607
11. Brake & Front End — Tread wear causes: https://www.brakeandfrontend.com/tire-tread-wear-causes/
12. SlashGear — DOT date code: https://www.slashgear.com/1419676/numbers-tires-date-code/
13. ToolSource — Tire age (automaker guidance summary): https://www.toolsource.com/blog/tire-age-vs-tread-depth-why-the-dot-date-code-matters-more-than-you-think/
14. Continental — Alignment: https://continentaltire.com/learn/tony-stewart-talks-proper-tire-alignment
15. MOTOR/MAP — Brake inspection (1999): https://www.motor.com/wp-content/uploads/BRAKE-SYSTEM-INSPECTION-021999_22.pdf
16. The Brake Report — MAP: https://thebrakereport.com/map-august-brake-safety-awareness-month/
17. Hella Pagid — Disc minimum thickness: https://www.techtips.ie/Hella-Ireland/technical-information---testing-the-minimum-thickness-of-a-brake-disc.pdf
18. GM spec (NHTSA TSB file): https://static.nhtsa.gov/odi/tsbs/2018/MC-10138391-9999.pdf
19. Saab/GM WIS — Disc brake specs: https://saabwisonline.com/9-4x/2011/5-brakes/brake-discs-and-pads/technical-data/disc-brake-component-specifications
20. Tomorrow's Technician — Rotor specs: https://www.tomorrowstechnician.com/brake-rotor-specs-measurement-and-service-techniques/
21. Vehicle Service Pros — Rotor runout: https://vehicleservicepros.com/service-repair/article/53082990/brake-rotor-runout
22. Brake & Front End — Pulsation: https://www.brakeandfrontend.com/?p=114514
23. Phoenix Systems — Runout guide: https://phoenixsystems.co/blogs/company-news-tips/how-do-i-check-brake-rotor-runout-with-a-dial-indicator
24. Phoenix Systems — Brake fluid testing (vendor): https://phoenixsystems.co/pages/brake-fluid-testing-how-and-why-to-test
25. Rick's — DTV myth: https://ricksfreeautorepairadvice.com/disc-thickness-variation-and-the-myth-of-warped-rotors/
26. Rick's — Fuel system cleaner: https://ricksfreeautorepairadvice.com/is-a-recommended-fuel-system-cleaner-really-necessary/
27. STLE — 3,000-mile myth: https://www.stle.org/files/TLTArchives/2019/02_February/From_the_Editor.aspx
28. CDX — Coolant testing: https://www.cdxlearning.com/blog/cdx/2018/12/11/tips-for-testing-and-maintaining-coolant-before-the-winter-weather-hits
29. Gates — Belt inspection tech tip: https://www.techtips.ie/Gates/belt-inspection-changes.pdf
30. Gates — Belt wear gauge: https://www.fleetmaintenance.com/in-the-bay/tools/product/12099611/gates-corporation-belt-wear-gauge
31. Midtronics — Healthy battery indicators (vendor): https://midtronics.com/blog/key-indicators-of-a-healthy-battery-test
32. Rotronics — Midtronics jargon buster: https://www.rotronicsbms.com/battery-tips/midtronics-testing-jargon-buster
33. GM TechLink — 12 V ratings: https://gm-techlink.com/?p=20367
34. WECT — AAA regional battery life: https://www.wect.com/2024/08/02/how-often-should-you-change-your-car-battery-depends-where-you-live
35. Monroe — Weepage vs. leakage: https://images.oreillyauto.com/parts/img/documents/mon/monroe_servicegram_weepageleakage_v01no05_eng_final.pdf
36. KYB — Leaking vs. sweating: https://kyb-europe.com/wp-content/uploads/2025/08/Technical-Bulletin-Leaking-vs-Sweating.pdf
37. NZTA — Shock absorber inspection: https://vehicleinspection.nzta.govt.nz/downloadPdf/634
38. AA1Car — Ball joints: https://www.aa1car.com/library/ball_joints.htm
39. Brake & Front End — Ball joint/tie rod wear: https://www.brakeandfrontend.com/why-do-ball-joints-tie-rods-and-control-arms-wear-out/
40. Honda Maintenance Minder (dealer guide): https://www.buerklehonda.com/a-guide-to-hondas-maintenance-minder-codes/
41. Tesla Model 3 manual — Maintenance: https://www.tesla.com/ownersmanual/model3/en_sg/GUID-E95DAAD9-646E-4249-9930-B109ED7B1D91.html
42. Toyota UK — Hybrid health check: https://mag.toyota.co.uk/toyota-hybrid-health-check
43. Toyota Owners Club — HV pack health: https://toyotaownersclub.com/forums/topic/194641-hybrid-battery-pack-health-status
44. PriusChat — Plug interval: https://priuschat.com/goto/post?id=1416052
45. BITOG — ATF drain-and-fill: https://bobistheoilguy.com/forums/threads/when-to-drain-and-fill-atf-for-toyota.320835/
46. BITOG — Alignment printouts: https://www.bobistheoilguy.com/forums/threads/getting-a-print-out-of-alignment-specs.82512/post-1067218
47. Forum — Pad measurement incl. backing plate: https://www.audizine.com/threads/time-for-pads-rotors-too.617618/
48. Forums — Dealer menu items: https://www.garagejournal.com/forum/goto/post?id=5137367 ; https://www.ranger5g.com/forum/threads/fuel-induction-and-throttle-body-cleaning-service.8525/post-211556
49. BodyShop Business — ADAS procedure gap: https://www.bodyshopbusiness.com/closing-the-oem-procedure-gap-in-adas-calibration/
50. Brake & Front End — Cameras after alignment: https://www.brakeandfrontend.com/?p=196547
51. RDN — IIHS camera calibration: https://www.repairerdrivennews.com/2018/04/16/iihs-research-shows-risk-of-uncalibrated-front-facing-cameras/
52. Autoblog — Repair upsells: https://www.autoblog.com/2014/05/19/car-repair-tricks-scams-upsells/
53. Haynes — Upsells and scams: https://us.haynes.com/blogs/tips-tutorials/common-auto-repair-upsells-and-scams
54. Quartz — CR dealership upsells: https://qz.com/5-car-dealership-upsells-consumer-reports-says-to-avoid
55. ConsumerAffairs — Mechanic survey: https://www.consumeraffairs.com/news/too-many-consumers-are-being-scammed-by-auto-mechanics-claims-a-new-report-080323.html
56. CarMD via AftermarketNews/others: https://www.aftermarketnews.com/carmd-releases-2023-check-engine-repair-trends/ ; https://www.tomorrowstechnician.com/carmd-vehicle-health-index-marks-10-years-of-reporting/ ; https://aftermarketinsight.spglobal.com/news/4261/carmd-finds-check-engine-repair-costs-down-slightly
57. PA 67 Pa. Code §175.80: https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/067/chapter175/s175.80.html
58. VA 19VAC30-70-80 / -130: https://law.lis.virginia.gov/admincode/title19/agency30/chapter70/section80/ ; https://law.lis.virginia.gov/admincode/title19/agency30/chapter70/section130/
59. VT DMV VN-113 Periodic Inspection Manual: https://dmv.vermont.gov/sites/dmv/files/documents/VN-113-Periodic_Inspection_Manual.pdf
