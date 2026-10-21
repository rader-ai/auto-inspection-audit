# 07 — Technical Inspection Criteria (Audit Engine Reference)

## 1. Scope & as-of date

- **As of:** 2026-10-20. Researcher division: technical criteria for judging whether each common multi-point / digital vehicle inspection (MPI/DVI) finding and recommendation is justified.
- **Covers:** light-duty passenger cars, SUVs, and light trucks (gas, diesel noted where relevant, hybrid, EV). Not heavy-duty/commercial (FMCSA) criteria.
- **Intended use:** the audit engine compares each line item on an inspection, estimate, or invoice against (a) the vehicle's OEM schedule and specs, (b) the objective thresholds below, and (c) the evidence the shop supplied. Output: Supported / Plausible-but-undocumented / Premature (Suggested at best) / Unsupported / Contradicted.
- **Critical caveat:** Most numeric limits (pad minimum, rotor discard, ball-joint play, runout, fluid intervals, plug intervals) are **vehicle-specific** and must come from OEM service information or the owner's manual/maintenance guide. The figures here are typical/industry values for plausibility checks, not substitutes for OEM data. Where a value is generic, it is labeled "typical."
- **Related files:** MAP "Required vs Suggested" is covered in depth by another researcher; only a brief summary appears here.

## 2. General principles

1. **OEM schedule is the baseline.** The owner's manual / warranty & maintenance guide (or the vehicle's maintenance reminder, e.g., Honda Maintenance Minder, GM Oil Life Monitor) defines required maintenance. AAA's consumer guidance repeatedly tells drivers to follow the manufacturer's schedule rather than generic intervals ([AAA myths](https://www.aaa.com/autorepair/articles/debunking-common-myths-about-car-maintenance)). Dealer service software and "menu" maintenance often add items not in the manual ([forum discussion, anecdotal](https://www.garagejournal.com/forum/goto/post?id=5137367)).
2. **Normal vs. severe service.** Most OEMs publish a "special operating conditions"/severe schedule (towing, short trips, extreme heat/cold, dusty roads, stop-and-go, mountain driving). A shop applying the severe schedule should be able to say which condition applies to this driver. Defaulting every customer to severe is a red flag. [Severe-schedule criteria vary by OEM; verify per vehicle.]
3. **Condition-based beats calendar/mileage-based when a valid test exists.** Brake fluid (copper strip / OEM interval), coolant (pH/reserve alkalinity/freeze point), battery (conductance printout), belts (rib-wear gauge), tires (tread gauge, date code) all have objective tests. A recommendation without the test result is weaker than one with it.
4. **Measurement > adjective.** "Pads low," "fluid dirty," "filter dirty," "belt cracked," "strut leaking" are opinions. A legitimate finding states the measured value, the spec/threshold, the location (e.g., LF inner pad), and ideally a photo or printout.
5. **Diagnosis ≠ code.** A trouble code (DTC) identifies a monitored circuit/condition that failed, not a failed part. A parts recommendation from a code alone, without pinpoint testing, is unsupported.
6. **Mileage/age context.** A recommendation should make sense against the vehicle's mileage, age, and service history (e.g., 120k-mile spark plugs recommended at 45k is premature; coolant "flush" on a 2-year-old car with OEM 10-year coolant is premature).
7. **Required vs. Suggested (MAP logic, brief).** The Motorist Assurance Program (MAP) Uniform Inspection & Communication Standards classify findings as **Required** (part no longer performs its intended function, fails a spec/discard limit, or is a safety/legal issue) or **Suggested** (part works but is near end of life, would improve performance/comfort, or is customer-convenience). Shops are expected to document the reason for each R/S recommendation. Example: a rotor above discard thickness that does not need machining → replacement is only Suggested; below discard (or would be after machining) → Required ([MOTOR/MAP brake article, 1999](https://www.motor.com/wp-content/uploads/BRAKE-SYSTEM-INSPECTION-021999_22.pdf); [The Brake Report on MAP](https://thebrakereport.com/map-august-brake-safety-awareness-month/)). Current MAP manual text not verified here.
8. **Color-coding on DVIs (green/yellow/red)** is not standardized. Red should map to Required (safety/failed spec), yellow to Suggested/monitor. A red item with no measurement or photo, or yellow items priced as urgent, are audit flags.

## 3. Per-system criteria

Template for each system: **How properly measured/tested · Objective thresholds · Evidence a legitimate recommendation includes · Legitimate reasons · Overreach patterns / red flags · Questions to ask.**

---

### 3.1 Tires

**How measured/tested**
- Tread depth with a tread-depth gauge in 32nds of an inch (or mm), measured in the **lowest major groove**, at inner/center/outer positions on each tire; avoid measuring on wear bars.
- DOT date code: last four digits of the TIN = week + year of manufacture (e.g., 2321 = week 23 of 2021). Pre-2000 used 3 digits ([SlashGear explainer](https://www.slashgear.com/1419676/numbers-tires-date-code/)).
- Visual: sidewall bulges, cuts exposing cords, weather checking/cracking depth, impact breaks, bead damage.
- Puncture: tire must be dismounted and inspected from inside ([USTMA](https://www.ustires.org/tire-care-safety/tire-repair-basics)).
- Pressure vs. door-placard spec (not the sidewall max). TPMS: scan tool reading of each sensor (pressure, ID, battery status).

**Objective thresholds**
- **2/32"** = federal wear-bar indicator height and the legal minimum in most states; NHTSA chose it because traction drops rapidly at that depth ([NHTSA interpretation](https://www.nhtsa.gov/interpretations/11497awkm); [Ford](https://www.ford.com/support/how-tos/tires-and-wheels/tire-replacement-and-maintenance/why-does-tread-wear-matter/)). Some states set different limits or front-axle rules [verify by state].
- **4/32"** = widely recommended replace/shop point for wet-weather performance. AAA advises replacing at 4/32" based on its wet-braking research ([AAA](https://www.aaa.com/autorepair/articles/debunking-common-myths-about-car-maintenance)); Consumer Reports advises starting to shop at 4/32" and keeping at least 4/32" through winter ([CR, paywalled](https://www.consumerreports.org/tires/what-happens-to-performance-when-tires-are-worn/); [Tire Review summary](https://www.tirereview.com/treading-close-to-limits/)). Snow use: many advise ~5–6/32" [UNVERIFIED as a standard].
- **Age:** No federal age limit; NHTSA defers to vehicle/tire makers ([NHTSA–NTSB response](https://www.nhtsa.gov/document/nhtsa-ntsb-response-may-2016-passenger-vehicle-tire-safety-tire-registration-tire-recalls)). Michelin: annual professional inspection after 5 years in service; replace at 10 years from manufacture regardless of tread, spare included ([Michelin](https://www.michelinman.com/auto/auto-tips-and-advice/tire-buying-guide/when-do-i-need-new-tires)). Several automakers (e.g., Ford, Nissan, Mercedes) cite 6 years from production ([secondary summary](https://www.toolsource.com/blog/tire-age-vs-tread-depth-why-the-dot-date-code-matters-more-than-you-think/) — verify in specific owner's manual).
- **Puncture repairability (USTMA):** injury ≤ 1/4" (6 mm) diameter; tread area only — not in shoulder/belt-edge or sidewall, and not angled into the shoulder; no overlapping repairs; never repair over a prior improper repair; must be dismounted and inspected; repair = plug/stem filling the injury **plus** an inner-liner patch — a plug alone is unacceptable; no outside-in or on-wheel repairs; run-flat limits per tire maker ([USTMA tire repair basics](https://www.ustires.org/tire-care-safety/tire-repair-basics); [USTMA procedures PDF](https://www.ustires.org/system/files/2026-06/Puncture%20Repair%20Procedures%20for%20Passenger%20and%20Light%20Truck%20Tires.pdf)).
- **Uneven wear interpretation:** inner-edge wear → typically negative camber and/or toe-out, also worn bushings/springs; outer-edge → positive camber/toe or hard cornering; center → over-inflation; both edges → under-inflation; feathering → toe; cupping/scalloping → worn dampers, imbalance, or lack of rotation ([Brake & Front End](https://www.brakeandfrontend.com/tire-tread-wear-causes/); [Tire Review](https://www.tirereview.com/?p=156607)).
- **Replacing in pairs/sets on AWD:** many AWD OEMs specify a maximum tread-depth (or circumference) difference between tires (commonly 2/32"–4/32" depending on OEM) [vehicle-specific; verify].

**Evidence a legitimate recommendation includes**
- Per-tire tread readings (ideally inner/center/outer) with position (LF/RF/LR/RR); DOT date code read off the tire; photo of damage; for "non-repairable" puncture, a photo showing location relative to shoulder or size; TPMS scan output identifying which sensor failed (ID/battery/no signal).

**Legitimate reasons to recommend**
- Any tire ≤ 2/32" or showing cords, bulges, sidewall cuts → Required. 3–4/32" → Suggested (replace soon), stronger in wet/snow climates. Tire > 10 years old (or beyond OEM age guidance) → Suggested/Required per OEM. Puncture outside USTMA repair zone → replace. Uneven wear that indicates alignment/suspension problem → recommend alignment check plus inspection of related components.

**Overreach / red flags**
- "Replace all four" when only one/two are worn on a non-AWD vehicle and the others are > 4/32".
- Tires at 5–7/32" labeled red/urgent. Tread readings that are all identical round numbers or don't match photos.
- "Can't be repaired" for a small tread-center nail (USTMA zone) without explanation; conversely, a plug-only repair or a repair in the shoulder is substandard (shop-owner liability flag).
- Age-based replacement on tires under ~6 years with no visible degradation.
- TPMS: selling four sensors when one failed (unless sensors share age and battery-status readings justify it — still Suggested). Selling "nitrogen" fills as a safety item (CR notes air is already ~78% nitrogen; [via Quartz summary of CR](https://qz.com/5-car-dealership-upsells-consumer-reports-says-to-avoid)).

**Questions to ask**
- What did each tire measure, where, and what's the date code? Where exactly is the puncture relative to the shoulder? Which TPMS sensor failed and what did the scan show? Is the uneven wear from alignment or a worn part — which one?

---

### 3.2 Brakes

**How measured/tested**
- Wheels off. Pad friction material measured in mm **excluding backing plate** (a reading that includes the ~5 mm steel backplate is a common error/inflation; [forum example](https://www.audizine.com/threads/time-for-pads-rotors-too.617618/)). Inner and outer pads both measured — inner often wears faster.
- Rotor thickness with an outside micrometer at several points ~1/4" in from the edge; compare to **discard/minimum thickness** cast or stamped on the rotor (hat or edge) and to the separate **machine-to/refinish** minimum in OEM data ([Hella Pagid](https://www.techtips.ie/Hella-Ireland/technical-information---testing-the-minimum-thickness-of-a-brake-disc.pdf); [GM spec example](https://static.nhtsa.gov/odi/tsbs/2018/MC-10138391-9999.pdf)).
- Lateral runout with a dial indicator, lug nuts torqued (or with conical washers), caliper off; thickness variation (DTV/parallelism) with a micrometer at multiple points ([Tomorrow's Technician](https://www.tomorrowstechnician.com/brake-rotor-specs-measurement-and-service-techniques/); [Vehicle Service Pros](https://vehicleservicepros.com/service-repair/article/53082990/brake-rotor-runout)).
- Drum: inside-diameter with drum micrometer vs. max diameter cast in drum; shoe lining thickness.
- Brake fluid: copper strip test (ppm Cu), or moisture/boiling-point tester; or OEM time interval.
- Caliper: slide pin freedom, piston seal/boot condition, leaks, uneven inner/outer pad wear, sticking (heat/drag).

**Objective thresholds**
- **Pad minimum:** vehicle-specific; many OEM specs list ~2.0 mm lining minimum ([GM/Saab examples](https://saabwisonline.com/9-4x/2011/5-brakes/brake-discs-and-pads/technical-data/disc-brake-component-specifications)). Many shops recommend at ~3 mm (a Suggested, not Required point) [typical]. New pads are typically ~10–12 mm [typical].
- **Rotor:** below cast discard = Required replacement; above discard but would be below machine-to after refinishing = replacement Required if refinishing is needed; above both and no pulsation/scoring/DTV issue = **no service required** — replacement is at most Suggested ([MAP/MOTOR](https://www.motor.com/wp-content/uploads/BRAKE-SYSTEM-INSPECTION-021999_22.pdf)).
- **Runout/DTV:** OEM-specific; commonly cited ~0.002" (0.05 mm) total lateral runout as a good-condition limit, >0.005" likely pulsation; DTV often ≤ 0.0005–0.001" ([Phoenix Systems guide](https://phoenixsystems.co/blogs/company-news-tips/how-do-i-check-brake-rotor-runout-with-a-dial-indicator); [Brake & Front End](https://www.brakeandfrontend.com/?p=114514)). Rust between hub and rotor is the leading runout cause — cleaning the hub may fix it without new parts.
- **"Warped rotors"** — pulsation is usually DTV from runout/uneven deposits, not literal warping ([Rick's](https://ricksfreeautorepairadvice.com/disc-thickness-variation-and-the-myth-of-warped-rotors/)).
- **Brake fluid:** MAP uniform standard: copper ≥ 200 ppm indicates depleted corrosion inhibitors → replacement ([Phoenix Systems, vendor](https://phoenixsystems.co/pages/brake-fluid-testing-how-and-why-to-test); vendor-sourced, treat with caution). Time-based: AAA says most OEMs recommend replacement every 2–3 years ([AAA](https://www.aaa.com/autorepair/articles/debunking-common-myths-about-car-maintenance)); Honda: every 3 years independent of Maintenance Minder ([dealer summaries](https://www.buerklehonda.com/a-guide-to-hondas-maintenance-minder-codes/)); Tesla: check every 4 years, replace if needed ([Tesla manual](https://www.tesla.com/ownersmanual/model3/en_sg/GUID-E95DAAD9-646E-4249-9930-B109ED7B1D91.html)). Some OEMs list long or no fixed intervals — check manual. **Fluid color alone is not a valid test.** Moisture "pens" that measure conductivity are considered less reliable than copper strips or boiling-point testers [UNVERIFIED — industry opinion].

**Evidence a legitimate recommendation includes**
- Pad readings in mm per wheel and per pad (inner/outer), OEM minimum cited; rotor thickness readings vs. stamped discard and machine-to spec; runout reading if pulsation claimed; photo of measurement; brake-fluid strip photo next to color chart or boiling-point reading.

**Legitimate reasons**
- Pads at/below OEM minimum, metal-to-metal, wear-indicator squeal, cracked/delaminated lining, contamination with oil/fluid. Rotor below discard, deep scoring, heat cracks, DTV causing pulsation. Caliper seized/leaking/torn boot causing uneven wear. Fluid ≥ 200 ppm Cu, low boiling point, or past OEM interval.

**Overreach / red flags**
- "Pads at 4 mm — replace now" labeled Required (that's Suggested at most).
- Automatic rotor replacement on every pad job with no thickness measurement (common; may be shop policy for comeback avoidance — acceptable only if disclosed as policy/Suggested and priced transparently).
- Calipers sold as routine with every brake job ("loaded calipers") without leak/sticking evidence.
- Brake-fluid flush based on color or "it's dark." Flush at 12 months on a vehicle with a 3-year OEM interval and no test.
- Measurement that includes backing plate. Pad readings that differ wildly from photos.
- Hybrid/EV: pads "worn" at low mileage — implausible given regen (see 3.13) unless rust/seized slides.

**Questions to ask**
- What were the pad and rotor measurements, and what's the minimum spec for my car? Is the rotor below discard, or would it be after machining? Can I see the strip test or boiling-point reading? Is the caliper actually leaking or seized?

---

### 3.3 Alignment

**How measured/tested**
- Four-wheel alignment machine; tires inflated to spec; ride height checked; steering/suspension inspected first (worn parts make alignment meaningless). Printout shows camber, caster, toe (and thrust angle, SAI where relevant) **before** and **after** against OEM min/max spec ([forum discussion of printouts](https://www.bobistheoilguy.com/forums/threads/getting-a-print-out-of-alignment-specs.82512/post-1067218)).

**Objective thresholds**
- OEM spec ranges (vehicle-specific). Out-of-spec "before" values in red on the printout are the justification. Many cars have non-adjustable camber/caster; shops may only set toe unless kits are installed.

**Indicated when**
- Pull/drift, off-center steering wheel, abnormal tire wear patterns (edge wear, feathering), after a significant pothole/curb impact, after replacing steering/suspension parts (tie rods, control arms, struts) or lowering/lifting, and with new tires (optional/Suggested) ([Continental Tire](https://continentaltire.com/learn/tony-stewart-talks-proper-tire-alignment)). Off-center wheel can also be worn components, not alignment.

**Evidence**
- Before/after printout with spec columns; description of symptom or wear pattern; tire photos.

**Overreach / red flags**
- Alignment recommended with no symptom, no wear pattern, no impact, no parts replaced, and no "before" readings showing out-of-spec.
- "Alignment done" with an after-printout identical to before, or no printout provided.
- Alignment recommended while worn tie rods/ball joints are noted but not addressed (alignment won't hold).
- Charging for camber adjustment on a vehicle with non-adjustable camber and no kit installed.
- "Lifetime alignment" upsell — value question, not a technical need.

**Questions**: May I see the before printout? Which angles were out of spec? Did anything change (impact, parts) to cause it?

---

### 3.4 Fluids & "flush" services

**General rule:** compare every fluid service to the OEM schedule for the vehicle's mileage/age and the applicable (normal vs. severe) condition. Ask "Where is this in my maintenance guide?" ([Rick's on fuel services](https://ricksfreeautorepairadvice.com/is-a-recommended-fuel-system-cleaner-really-necessary/)).

**Engine oil**
- *How determined:* OEM oil-life monitor (OLM) or OEM mileage/time interval; correct viscosity/spec (e.g., API SP/ILSAC GF-6, dexos, OEM approvals).
- *Thresholds:* AAA calls the 3,000-mile rule a myth; for vehicles ≤ ~15 years old typical intervals are 5,000–7,500 miles, up to ~15,000 with full synthetic where the OEM allows ([AAA](https://www.aaa.com/autorepair/articles/debunking-common-myths-about-car-maintenance)). GM research behind the OLM found oil could often run 10,000–12,000 miles before significant degradation and that temperature/operating conditions matter more than miles ([STLE](https://www.stle.org/files/TLTArchives/2019/02_February/From_the_Editor.aspx)).
- *Red flags:* 3,000-mile window stickers on vehicles whose OEM interval is 7,500–10,000; resetting OLM early; "engine flush" chemical add-ons (generally not OEM-specified) [UNVERIFIED as universal; some OEMs explicitly advise against flushing additives].
- *Legit:* OLM at ≤ 15%, OEM interval reached, oil level low (also find why), contamination (coolant/fuel) — which is a diagnostic finding, not just an oil change.

**Transmission fluid (automatic/CVT/DCT)**
- *How determined:* OEM schedule (many list "inspect" only under normal use; replacement under severe use); fluid level check method per OEM (many sealed units have no dipstick and require temperature-specific check-plug procedure).
- *"Lifetime/sealed" claims:* OEM "lifetime" often means warranty-period life or normal use; many technicians advise periodic drain-and-fill anyway. Treat replacement as **Suggested** unless OEM schedule calls for it, severe use applies, or fluid is burnt/contaminated/low.
- *Flush vs. drain-and-fill:* A drain-and-fill replaces only part of the fluid (commonly ~25–50% depending on design; [forum reports](https://bobistheoilguy.com/forums/threads/when-to-drain-and-fill-atf-for-toyota.320835/)); machine exchange/flush replaces more. Some transmission specialists prefer repeated drain-and-fills on high-mileage units never serviced, citing risk of dislodging debris [anecdotal — UNVERIFIED as engineering consensus]. Some OEMs specify drain-and-fill only; using a flush machine or a "universal" fluid where OEM requires a specific fluid (Toyota WS, Honda ATF DW-1/HCF-2, CVT fluids) is an error.
- *Red flags:* "Flush" on a low-mileage vehicle outside OEM schedule; fluid judged by color/smell only; universal/multi-vehicle fluid on invoice for a vehicle requiring OEM-specific fluid; flush recommended to "fix" shifting problems without diagnosis.

**Coolant**
- *How determined:* OEM interval (many modern long-life coolants: first change ~100,000–150,000 miles or ~10 years, then shorter intervals [typical; verify]); condition tests: refractometer for freeze point (glycol concentration), test strips for pH and reserve alkalinity; visual for contamination/oil.
- *Thresholds:* Freeze protection per climate (often to ~−34°F at 50/50) [typical]. pH below ~7–8 indicates depleted inhibitors → replace ([CDX Learning](https://www.cdxlearning.com/blog/cdx/2018/12/11/tips-for-testing-and-maintaining-coolant-before-the-winter-weather-hits)). Note that freeze point alone says nothing about corrosion protection.
- *Red flags:* coolant "flush" on a car with OEM 10-year coolant at 30k–60k miles without failed test; universal "all-makes" coolant replacing OEM-specified type; recommendation based on color alone. Autoblog flags routine coolant replacement as a classic upsell unless contaminated or very high mileage ([Autoblog](https://www.autoblog.com/2014/05/19/car-repair-tricks-scams-upsells/)).
- *Legit:* failed pH/RA strip, poor freeze protection, contamination (oil, rust, sludge), OEM interval reached, cooling-system repair requiring drain.

**Power steering fluid**
- Many OEMs list inspect-only; many modern vehicles have electric power steering (EPS) with **no fluid at all** — a power-steering flush on an EPS vehicle is a fabricated service. Legit: OEM interval, contamination, noise/hard steering with diagnosis.

**Differential / transfer case / manual transmission**
- OEM schedules commonly specify gear-oil change at 30k–60k under severe use (towing), and longer or inspect-only under normal use [vehicle-specific]. Legit for AWD/4WD vehicles that tow. Red flag: differential service on a FWD car with no separate differential (it shares the transaxle), or both front and rear diffs billed on a 2WD vehicle.

**Fuel system / induction / throttle body cleaning**
- Generally **not** in OEM maintenance schedules; Top Tier detergent gasoline is designed to keep injectors clean; some OEMs have issued bulletins against unneeded fuel-system services ([Rick's](https://ricksfreeautorepairadvice.com/is-a-recommended-fuel-system-cleaner-really-necessary/); [Haynes](https://us.haynes.com/blogs/tips-tutorials/common-auto-repair-upsells-and-scams)) [OEM bulletin specifics UNVERIFIED]. Exceptions: some OEMs publish TSBs for intake-valve carbon cleaning on specific direct-injection engines, or throttle-body cleaning for an idle/drivability complaint — these are **diagnosis-driven**, not mileage-driven.
- Red flags: mileage-based "fuel induction service" at 15k/30k/45k; injector cleaning without a misfire/lean code, fuel-trim data, or flow test.

**Brake fluid** — see 3.2.

**OEM schedule vs. dealer "menu"**
- Dealer menus often bundle items (fuel induction, throttle body, coolant/trans/PS flushes, "multi-point" fees) at round-number milestones. Audit each menu line against the OEM guide; anything not listed is optional/Suggested and should be labeled as such ([forum examples](https://www.ranger5g.com/forum/threads/fuel-induction-and-throttle-body-cleaning-service.8525/post-211556)).

**Questions**: Is this in my owner's maintenance schedule at this mileage (normal or severe)? What test result shows the fluid is degraded? What fluid spec/brand will you use — does it meet the OEM spec? Flush or drain-and-fill, and why?

---

### 3.5 Filters

**Engine air filter**
- *How judged:* visual inspection against light, debris/blockage; OEM interval (often 15k–30k normal, shorter for dusty conditions) [vehicle-specific]; some vehicles show it on maintenance reminders.
- *Legit:* visibly clogged, damaged, contaminated (oil, water, rodent nest), or OEM interval reached. Autoblog: replace only when clogged with dirt ([Autoblog](https://www.autoblog.com/2014/05/19/car-repair-tricks-scams-upsells/)).
- *Red flags:* "dirty" filter photo of a filter's intake side that is lightly gray (normal); recommending at every oil change; photo that doesn't match the vehicle's filter shape; price far above part + minimal labor (many are tool-free).

**Cabin air filter**
- OEM intervals ~1–2 years or 15k–30k miles commonly; e.g., Tesla Model 3 every 2 years (yearly in China) ([Tesla](https://www.tesla.com/ownersmanual/model3/en_sg/GUID-E95DAAD9-646E-4249-9930-B109ED7B1D91.html)). Legit: debris/leaves, odor, reduced airflow, interval reached. Red flag: same as above; photos of a different vehicle's filter (photo reuse is a known DVI integrity issue).

**Questions**: Can I see the filter (or photo of my actual filter)? When was it last replaced?

---

### 3.6 Battery & charging

**How tested**
- Conductance tester (e.g., Midtronics-type) with correct rating entered (CCA SAE vs. EN vs. JIS); state of charge; resting voltage; charging-system test (alternator output, ripple/diode); starter draw. Results: Good / Good-Recharge / Charge & Retest / Replace / Bad Cell.
- Surface charge and low state of charge can cause false Replace results; tester should charge-and-retest.

**Objective thresholds**
- Measured CCA vs. rated: Midtronics material suggests healthy batteries at ≥ ~80–90% of rated; sources vary, 70–79% marginal, < 70% replace commonly cited ([Midtronics blog](https://midtronics.com/blog/key-indicators-of-a-healthy-battery-test); [summary](https://www.rotronicsbms.com/battery-tips/midtronics-testing-jargon-buster)). Entering the wrong rating type/value can produce a false "Replace" ([GM TechLink](https://gm-techlink.com/?p=20367)).
- Resting voltage ~12.6 V full; < 12.4 V indicates low charge [typical].
- Age: AAA — batteries typically last 3–5 years; test starting around year 3; heat shortens life ([AAA](https://www.aaa.com/autorepair/articles/debunking-common-myths-about-car-maintenance); [regional AAA data via WECT](https://www.wect.com/2024/08/02/how-often-should-you-change-your-car-battery-depends-where-you-live)).

**Evidence**: tester printout showing rated vs. measured CCA, voltage, decision, and test date/time; battery date code; charging-system result.

**Legit**: Replace/Bad Cell on a properly charged battery; slow cranking with failing test; swollen/leaking case; age plus marginal result (Suggested).

**Red flags**: "Battery weak" with no printout; printout with wrong rating entered (e.g., 500 CCA entered for 750 CCA battery); recommending replacement based on age alone on a battery that tests Good; "Charge & Retest" result reported as "Replace"; AGM vehicle receiving flooded battery (and missing battery registration where OEM requires it on BMS-equipped vehicles).

**Questions**: May I have the printout? What rating was entered? Was it charged and retested?

---

### 3.7 Belts & hoses

**How tested**
- Serpentine (EPDM) belts: rib-wear gauge or Gates PIC Gauge app measuring material loss in rib valleys; **crack counting is obsolete for EPDM** — the "3 cracks in 3 inches" rule applied to older neoprene belts; EPDM can run ~100,000 miles with few/no cracks yet be worn by material loss ([Gates tech tip](https://www.techtips.ie/Gates/belt-inspection-changes.pdf); [Gates gauge description](https://www.fleetmaintenance.com/in-the-bay/tools/product/12099611/gates-corporation-belt-wear-gauge)).
- Tensioner: arm movement/bounce, wear-indicator marks, pulley bearing noise/wobble, misalignment.
- Timing belt: OEM replacement interval (time and miles) — not visually judged in most cases.
- Hoses: squeeze test for softness/swelling/hardening, cracks, leaks at clamps, bulging; cooling-system pressure test if leak suspected.

**Thresholds**: Belt gauge seats flush = OK; rocks laterally = replace. Chunks missing, rib separation, cord visible, glazing with noise = replace. Timing belt per OEM interval (often 60k–105k miles or ~7–10 years) [vehicle-specific; many engines use timing chains with no interval].

**Evidence**: photo of gauge on belt; tensioner observation; hose photo showing crack/leak; pressure-test result.

**Red flags**: "Belt has cracks" on EPDM as the sole reason; timing belt recommended on an engine with a timing chain; "water pump while you're in there" when no timing-belt job is being done (it's only a cost-saving Suggested item when the pump is timing-belt-driven and accessed anyway); hose replacement on appearance alone.

**Questions**: Did you use a belt-wear gauge? Does my engine have a timing belt or chain? Is the hose leaking or just old-looking?

---

### 3.8 Wipers, lights, bulbs

- **Wipers**: streaking, chatter, torn/hardened rubber, frame damage. Legit Suggested item; Required only if visibility is impaired. Red flags: high labor charge for tool-free blades; "replace" on blades that wipe cleanly.
- **Lights/bulbs**: functional check of all exterior lamps (headlamps low/high, turn, brake incl. CHMSL, reverse, plate, markers). Burnt-out lamp = Required (legal). Headlamp lens oxidation → restoration is Suggested unless output/inspection fails. Red flags: "upgrade" bulbs, replacing pairs when one is out (pairs for headlamps is reasonable/Suggested for color/output match), LED/HID assemblies quoted when a bulb is the issue.
- **Questions**: Which bulb is out? Is the lens restoration needed for safety or cosmetic?

---

### 3.9 Suspension & steering

**How tested**
- Inspect with vehicle on lift, wheels unloaded or loaded per OEM procedure. Ball joints: dial indicator measuring axial/radial play vs. OEM spec, or built-in wear indicator (raised shoulder or pin must protrude) ([AA1Car](https://www.aa1car.com/library/ball_joints.htm); [Brake & Front End](https://www.brakeandfrontend.com/why-do-ball-joints-tie-rods-and-control-arms-wear-out/)). Load-carrying vs. follower joint procedure matters (spring position determines which joint is loaded).
- Tie rods/inner rack joints: grip-and-shake test, dry-park check (steering wheel rocked with wheels on ground while observing joints).
- Shocks/struts: ride control symptoms (excess bounce, nosedive, body roll, cupping), leak inspection, mount/bushing condition, road test.
- Bushings: visible tearing, separation, movement under pry.

**Objective thresholds**
- Ball-joint play: **OEM-specific** (many have zero allowable play for load-carrying joints; some allow small values) [vehicle-specific — must cite OEM].
- **Misting vs. leaking**: a light film/"weep" near the upper seal is normal and does not require replacement; a leak is fluid wet over most of the body or dripping/streaming ([Monroe ServiceGram](https://images.oreillyauto.com/parts/img/documents/mon/monroe_servicegram_weepageleakage_v01no05_eng_final.pdf); [KYB bulletin](https://kyb-europe.com/wp-content/uploads/2025/08/Technical-Bulletin-Leaking-vs-Sweating.pdf); [NZTA inspection rule](https://vehicleinspection.nzta.govt.nz/downloadPdf/634)).
- **Bounce test**: crude; modern gas-charged dampers may pass while worn, and it does not quantify damping. Not adequate sole evidence [industry consensus; UNVERIFIED single authoritative source]. Mileage-based strut replacement (e.g., "every 50,000 miles") is a marketing guideline, not an OEM requirement in most cases [UNVERIFIED].

**Evidence**: measured play vs. spec or video of the movement; photo showing wet/dripping damper (not just dust-coated mist); cupping photos; road-test notes.

**Legit**: play beyond OEM spec, torn boots with grease loss, clunks with confirmed looseness, leaking (dripping) dampers, broken springs, bent components.

**Red flags**: "struts leaking" photo shows dry dust film/mist; recommending all four struts plus mounts "as a set" at 40k miles with no symptom; "ball joints worn" without measurement on a joint with an intact wear indicator; lifetime-lubricated joints "need grease."

**Questions**: How much play, and what's the spec? Is it leaking (dripping) or just misting? Can I see the video/photo?

---

### 3.10 Exhaust, engine mounts, CV boots/axles, wheel bearings

- **Exhaust**: inspect for leaks (sound, soot trails, smoke test), rusted-through pipes, broken hangers, catalytic converter efficiency (P0420/P0430 require diagnosis: O2 sensor data, exhaust leaks, misfire history before condemning the converter). CarMD lists catalytic converter replacement among the most frequent/costly check-engine repairs ([CarMD via AftermarketNews](https://www.aftermarketnews.com/carmd-releases-2023-check-engine-repair-trends/)) — a high-value line to audit for diagnostic support. Surface rust ≠ failure.
- **Engine/transmission mounts**: torn/collapsed rubber, fluid loss from hydraulic mounts, excessive engine movement during power-brake test (observe while shifting D/R with brake held). Red flag: replacing all mounts when one is failed; "cracked" surface rubber without excess movement.
- **CV boots/axles**: torn boot slinging grease = repair (boot or axle); clicking on turns = worn outer joint; inner-joint vibration on acceleration. A tear caught early may only need a boot; long-torn boots with contamination → axle. Red flag: axle replacement for a "dry" boot with no tear; grease on the boot from another source.
- **Wheel bearings**: noise that changes with speed/load (swerve test), play with wheel rocked at 12/6 o'clock, roughness when spun, ABS wheel-speed codes; OEM endplay specs for hub units (often ~zero) [vehicle-specific]. Red flag: replacing both sides when one is noisy (pairs = Suggested at most); diagnosing bearing noise that's actually tire cupping.
- **Questions**: Where is the leak/tear — photo? What test confirmed the converter has failed? Which bearing, and how was it confirmed?

---

### 3.11 Engine diagnostics, spark plugs, coils, "tune-up"

- **CEL/DTC**: a code is a starting point. Proper diagnosis = code + freeze-frame + live data (fuel trims, O2/AF sensor, misfire counters) + pinpoint tests following OEM or industry diagnostic trees, plus TSB check. Charging a diagnostic fee is legitimate; replacing parts named by the code without testing is not. CarMD's index historically shows O2 sensor, catalytic converter, ignition coil/spark plug, and loose gas cap among the top CEL repairs ([CarMD 2018 data via AftermarketNews](https://www.aftermarketnews.com/carmd-vehicle-health-index-ignition-coils-spark-plugs-o2-sensors-tied-for-most-commonly-diagnosed-check-engine-repair%ef%bb%bf/); [2020 summary](https://www.tomorrowstechnician.com/carmd-vehicle-health-index-marks-10-years-of-reporting/)).
- **Spark plugs**: OEM intervals commonly ~60k–120k miles for platinum/iridium (e.g., Toyota iridium ~120k; Honda via Maintenance Minder code 4) ([Toyota owner reports](https://priuschat.com/goto/post?id=1416052); [Honda codes](https://www.buerklehonda.com/a-guide-to-hondas-maintenance-minder-codes/)) [verify per model]. Legit: OEM interval reached, misfire traced to plug (gap erosion, fouling, cracked insulator). Red flag: plugs at 30k on a 100k+ interval engine; "tune-up" packages.
- **Ignition coils**: replace the coil(s) proven bad (swap test, misfire follows coil, scope/spark test). Red flag: replacing all coils for one misfire without testing (all-coils is Suggested at most on high mileage).
- **"Tune-up"**: obsolete term for modern engines (no points/carburetor/adjustable timing). A "tune-up" line must be decomposed into specific OEM items (plugs, filters) — otherwise it's an unsupported bundle.
- **Questions**: What code(s), and what tests confirmed the part is bad? Did you check TSBs? Is this at the OEM spark-plug interval?

---

### 3.12 A/C & cabin

- **How tested**: vent outlet temperature vs. ambient/humidity chart, high/low side pressures with gauges, leak detection (dye/UV, electronic sniffer, nitrogen pressure/vacuum decay), compressor clutch/operation, refrigerant identification (R-134a vs. R-1234yf). Recovery/recharge by weight per OEM charge spec.
- **Legit**: insufficient cooling with low charge plus leak located; failed compressor (verified); clogged cabin filter reducing airflow.
- **Red flags**: "A/C recharge" without leak test (refrigerant doesn't get "used up" — low charge implies a leak); "A/C performance service" as mileage maintenance; topping off with sealer-containing cans (can damage shop recovery equipment and system); R-1234yf price inflation without disclosure. Evaporator "cleaning/deodorizing" is Suggested/comfort only.
- **Questions**: What was the outlet temperature and pressures? Where's the leak? How much refrigerant was recovered vs. spec?

---

### 3.13 Hybrid & EV specifics

- **12 V battery**: still present in most hybrids/EVs and a common failure; test the same way (conductance printout). Often AGM; replacement must match type.
- **HV battery state of health (SoH)**: obtained via OEM scan tool (e.g., Toyota Techstream hybrid health check) or OEM app/report; a pass/fail result is less informative than per-block voltage deltas, internal resistance, or capacity estimate ([Toyota UK hybrid health check](https://mag.toyota.co.uk/toyota-hybrid-health-check); [owner forum on printouts](https://toyotaownersclub.com/forums/topic/194641-hybrid-battery-pack-health-status)). HV battery replacement recommendations need scan-tool data and OEM DTCs, and check warranty (federal emissions warranty and state rules often cover HV batteries 8 yrs/100k, 10 yrs/150k in CARB states) [UNVERIFIED — another researcher may cover warranty]. HV work requires trained technicians and OEM safety procedures.
- **Brakes**: regenerative braking does much of the slowing, so pad/rotor wear is typically much lower; the more common hybrid/EV brake problems are rotor corrosion and seized slides from under-use [widely reported; UNVERIFIED single authoritative source]. Pad replacement at low mileage on a hybrid/EV deserves measurement scrutiny. Brake fluid still required per OEM (Tesla: check every 4 years).
- **Coolant loops**: many hybrids/EVs have separate coolant circuits (engine, inverter/power electronics, battery thermal management) with distinct OEM fluids and intervals, and specific bleed procedures (sometimes requiring scan-tool pump activation). Red flag: generic "coolant flush" on an EV, or wrong coolant spec; legit if OEM interval/test supports it.
- **No-fluid items**: EVs have no engine oil, spark plugs, air filter (engine), timing belt, or exhaust — any such line item is fabricated. EV reduction gear oil intervals are OEM-specific (some "lifetime").
- **Questions**: Can I see the scan-tool SoH/block data? Is this covered by HV warranty? Which coolant loop and what fluid?

---

### 3.14 ADAS calibration

- **When required**: per OEM position statements/repair procedures — common triggers include windshield replacement (forward camera mounted to glass), camera/radar removal or replacement, bumper/grille work affecting radar, collision damage, ride-height or suspension changes, and on many makes after a wheel alignment (thrust-angle/steering-angle changes). Requirements vary by OEM and model; the authoritative source is the OEM repair procedure, not a generic rule ([BodyShop Business](https://www.bodyshopbusiness.com/closing-the-oem-procedure-gap-in-adas-calibration/); [Brake & Front End on alignment](https://www.brakeandfrontend.com/?p=196547)). IIHS research found improperly calibrated cameras can impair performance ([Repairer Driven News](https://www.repairerdrivennews.com/2018/04/16/iihs-research-shows-risk-of-uncalibrated-front-facing-cameras/)). Steering angle sensor reset after alignment is a separate, commonly required step on many vehicles.
- **Evidence**: citation of the OEM procedure requiring it; pre/post scan report; calibration report (static target setup or dynamic drive) showing completion.
- **Red flags**: calibration billed on a vehicle without the relevant ADAS feature; billed with no calibration report; billed for "radar" on a camera-only system; failure to calibrate when OEM requires it (shop-owner liability flag — the inverse risk).
- **Questions**: Which OEM procedure requires this? May I have the calibration report and post-scan?

## 4. Commonly upsold services (consumer research & trade press)

Ranked roughly by how frequently they appear in consumer guidance as upsells (sourcing quality varies):

1. **Fluid "flushes"** — transmission, coolant, power steering, brake fluid without test/OEM interval ([Autoblog](https://www.autoblog.com/2014/05/19/car-repair-tricks-scams-upsells/); [Haynes](https://us.haynes.com/blogs/tips-tutorials/common-auto-repair-upsells-and-scams)).
2. **Fuel system / fuel injection / induction / throttle-body cleaning** — generally absent from OEM schedules ([Rick's](https://ricksfreeautorepairadvice.com/is-a-recommended-fuel-system-cleaner-really-necessary/); [Haynes](https://us.haynes.com/blogs/tips-tutorials/common-auto-repair-upsells-and-scams)).
3. **Premature brake jobs** — pads/rotors before minimum; Haynes calls brake jobs probably the most common unnecessary repair ([Haynes](https://haynes.com/en-us/tips-tutorials/common-auto-repair-upsells-and-scams)).
4. **Oil changes at 3,000 miles / early resets** ([AAA](https://www.aaa.com/autorepair/articles/debunking-common-myths-about-car-maintenance)).
5. **Engine and cabin air filters** shown "dirty" at every visit ([Autoblog](https://www.autoblog.com/2014/05/19/car-repair-tricks-scams-upsells/)).
6. **New tire instead of USTMA-compliant repair**; full tire sets when only some are worn ([Autoblog](https://www.autoblog.com/2014/05/19/car-repair-tricks-scams-upsells/)).
7. **Nitrogen tire fills** ([CR via Quartz](https://qz.com/5-car-dealership-upsells-consumer-reports-says-to-avoid)).
8. **Alignment** with no symptom or "before" readings.
9. **Struts/shocks** on mileage or misting alone.
10. **Batteries** without printout.
11. **"Tune-ups"** and mileage-milestone dealer menus.
12. **A/C recharge** without leak diagnosis.
- Survey context: a 1,000-consumer survey (AmericanTrucks, via ConsumerAffairs) found upselling unnecessary repairs was the most reported problem ([ConsumerAffairs](https://www.consumeraffairs.com/news/too-many-consumers-are-being-scammed-by-auto-mechanics-claims-a-new-report-080323.html)) — commercial survey, moderate reliability.
- CarMD's Vehicle Health Index (2025 edition exists; ranking not verified here) tracks most common CEL repairs; historically O2 sensors, catalytic converters, ignition coils/plugs ([CarMD 2025 summary](https://aftermarketinsight.spglobal.com/news/4261/carmd-finds-check-engine-repair-costs-down-slightly)).

## 5. Audit implications — line-item checklist

### 5.1 Universal checks (both audiences)
For every line item on inspection/estimate/invoice:
1. **Classify**: maintenance (schedule-driven) vs. repair (condition-driven) vs. diagnostic vs. optional/comfort.
2. **OEM schedule match** (maintenance): Is it listed in the owner's guide at this mileage/age? Normal or severe? If severe, which condition applies? Not listed → Suggested/optional at most.
3. **Measurement present?** (repair): numeric value + unit + location + spec. Missing → "Plausible but undocumented."
4. **Threshold test**: does the measurement fail the OEM spec or recognized threshold (sec. 3)? Pass → recommendation is premature/Suggested; fail → Required.
5. **Evidence quality**: photo of *this* vehicle (VIN/plate/mileage context, consistent with other photos), test printouts (battery, alignment, scan, calibration), strip-vs-chart photos.
6. **Internal consistency**: tread readings vs. tire-replacement claim; pad mm vs. "red" status; brake job on hybrid at low miles; EV with oil/plug items; EPS vehicle with PS flush; FWD with rear diff service; timing belt on a chain engine.
7. **Severity labeling**: Red/Required only for safety, legal, or failed-spec items; yellow priced as urgent = flag.
8. **Bundling**: "while you're in there" items must be justified individually; flag pairs/sets beyond what failed unless OEM requires (e.g., AWD tire matching) or disclosed as Suggested.
9. **Parts/fluid spec**: invoice fluid/part meets OEM spec (e.g., WS ATF, OEM coolant type, dexos oil, AGM battery).
10. **Invoice vs. estimate**: performed items match authorized items; labor hours plausible vs. standard labor guides (another researcher covers pricing).
11. **Diagnostic logic** (CEL): code → tests → conclusion documented; TSB checked.

### 5.2 Consumer-specific
- Ask for: measurements, photos, printouts, and the old parts (most states allow return of replaced parts — confirm via legal researcher).
- Use the "questions to ask" per system (sec. 3).
- Prioritize: Required safety items now; Suggested items can be deferred or second-opinioned.
- Self-checks you can do: read tire DOT date code; penny/quarter test is crude (penny ≈ 2/32", quarter ≈ 4/32") [commonly cited; UNVERIFIED as exact]; check owner's manual schedule; check whether car has EPS/timing chain/no PS fluid.
- Red-flag phrases: "while we had it apart," "it's due" (without schedule reference), "it's dirty/dark," "lifetime fluid is a myth so we flush it," "highly recommended" with no measurement.

### 5.3 Shop-owner-specific
- **Documentation standard**: require techs to record numeric measurements for tires (per tire, per position), pads (inner/outer, friction only), rotors (vs. discard/machine-to), battery printout, alignment before/after, fluid test results — and attach photos for every red/yellow item.
- **Spec sourcing**: require OEM spec lookup (pad minimum, rotor discard, ball-joint play) rather than shop rules of thumb; flag DVIs that show "3 mm = red" if OEM minimum is 2 mm (re-label as yellow/Suggested).
- **Photo integrity**: watch for reused/stock photos, photos from other vehicles, mismatched mileage — a common DVI integrity failure and a liability exposure.
- **Menu discipline**: label non-OEM menu items as optional; do not present them as "manufacturer recommended."
- **Substandard-repair liability**: plug-only/shoulder tire repairs, universal fluids in OEM-specific transmissions, skipped ADAS calibration or SAS reset where OEM requires, wrong battery type/registration — these are the inverse audit risks (under-service).
- **Tech incentive review**: correlate high-upsell techs with low measurement documentation rates (pattern audit; sales-incentive analysis belongs to the business-practices researcher).
- **MAP alignment**: map each DVI status to MAP Required/Suggested reasons for defensible customer communication.

## 6. Open questions / uncertainties

- Current MAP Uniform Inspection & Communication Standards text (brakes, tires, fluids) could not be retrieved; logic summarized from a 1999 MOTOR article and secondary sources. The copper 200 ppm figure is reported mainly via Phoenix Systems (vendor).
- Consumer Reports' 4/32" data and its upsell lists are paywalled; cited via secondary summaries. No CR-authored list of "most upsold services" was verified.
- NHTSA has no tire-age rule; automaker 6-year guidance cited secondarily — verify per owner's manual.
- Midtronics CCA percentage thresholds differ between Midtronics sources (70/80/90%); tester decision logic is proprietary.
- Transmission flush risk on neglected high-mileage units is widely repeated by technicians but lacks a verified engineering study.
- OEM bulletins advising against fuel-system cleaning services are reported by a repair blog; specific bulletin numbers not verified.
- Hybrid/EV pad-wear reduction and HV warranty terms are widely stated but not verified to a primary source here.
- Rotor runout/DTV values are commonly cited trade figures; OEM specs vary.
- Ball-joint, wheel-bearing endplay, AWD tire mismatch limits, coolant/trans/diff intervals are vehicle-specific — engine must request OEM data per VIN or flag as "needs OEM spec."
- Severe-service criteria wording differs by OEM; whether a given driver qualifies is a judgment call.

## 7. Sources

- AAA — Debunking common myths about car maintenance: https://www.aaa.com/autorepair/articles/debunking-common-myths-about-car-maintenance
- USTMA — Tire repair basics: https://www.ustires.org/tire-care-safety/tire-repair-basics
- USTMA — Puncture repair procedures (PDF): https://www.ustires.org/system/files/2026-06/Puncture%20Repair%20Procedures%20for%20Passenger%20and%20Light%20Truck%20Tires.pdf
- NHTSA interpretation on 2/32" wear indicators: https://www.nhtsa.gov/interpretations/11497awkm
- NHTSA–NTSB 2016 tire safety response: https://www.nhtsa.gov/document/nhtsa-ntsb-response-may-2016-passenger-vehicle-tire-safety-tire-registration-tire-recalls
- Ford — Why does tread wear matter: https://www.ford.com/support/how-tos/tires-and-wheels/tire-replacement-and-maintenance/why-does-tread-wear-matter/
- Michelin — When do I need new tires: https://www.michelinman.com/auto/auto-tips-and-advice/tire-buying-guide/when-do-i-need-new-tires
- Consumer Reports — Worn tire performance (paywalled): https://www.consumerreports.org/tires/what-happens-to-performance-when-tires-are-worn/
- Tire Review — Treading close to limits: https://www.tirereview.com/treading-close-to-limits/
- Tire Review — Reading tire wear patterns: https://www.tirereview.com/?p=156607
- Brake & Front End — Tire tread wear causes: https://www.brakeandfrontend.com/tire-tread-wear-causes/
- SlashGear — DOT date code: https://www.slashgear.com/1419676/numbers-tires-date-code/
- ToolSource — Tire age vs tread depth (automaker age guidance summary): https://www.toolsource.com/blog/tire-age-vs-tread-depth-why-the-dot-date-code-matters-more-than-you-think/
- Continental Tire — Alignment: https://continentaltire.com/learn/tony-stewart-talks-proper-tire-alignment
- MOTOR / MAP brake inspection article (1999): https://www.motor.com/wp-content/uploads/BRAKE-SYSTEM-INSPECTION-021999_22.pdf
- The Brake Report — MAP: https://thebrakereport.com/map-august-brake-safety-awareness-month/
- Hella Pagid — Testing minimum brake disc thickness: https://www.techtips.ie/Hella-Ireland/technical-information---testing-the-minimum-thickness-of-a-brake-disc.pdf
- GM spec sheet (NHTSA TSB file): https://static.nhtsa.gov/odi/tsbs/2018/MC-10138391-9999.pdf
- Saab WIS — Disc brake specifications: https://saabwisonline.com/9-4x/2011/5-brakes/brake-discs-and-pads/technical-data/disc-brake-component-specifications
- Tomorrow's Technician — Rotor specs: https://www.tomorrowstechnician.com/brake-rotor-specs-measurement-and-service-techniques/
- Vehicle Service Pros — Rotor runout: https://vehicleservicepros.com/service-repair/article/53082990/brake-rotor-runout
- Brake & Front End — Brake pulsation: https://www.brakeandfrontend.com/?p=114514
- Phoenix Systems — Runout guide: https://phoenixsystems.co/blogs/company-news-tips/how-do-i-check-brake-rotor-runout-with-a-dial-indicator
- Phoenix Systems — Brake fluid testing (vendor): https://phoenixsystems.co/pages/brake-fluid-testing-how-and-why-to-test
- Rick's Free Auto Repair Advice — DTV myth: https://ricksfreeautorepairadvice.com/disc-thickness-variation-and-the-myth-of-warped-rotors/
- Rick's — Fuel system cleaner: https://ricksfreeautorepairadvice.com/is-a-recommended-fuel-system-cleaner-really-necessary/
- STLE — The 3,000-mile myth: https://www.stle.org/files/TLTArchives/2019/02_February/From_the_Editor.aspx
- CDX Learning — Coolant testing: https://www.cdxlearning.com/blog/cdx/2018/12/11/tips-for-testing-and-maintaining-coolant-before-the-winter-weather-hits
- Gates — Belt inspection changes (tech tip): https://www.techtips.ie/Gates/belt-inspection-changes.pdf
- Gates belt wear gauge: https://www.fleetmaintenance.com/in-the-bay/tools/product/12099611/gates-corporation-belt-wear-gauge
- Midtronics — Healthy battery test indicators: https://midtronics.com/blog/key-indicators-of-a-healthy-battery-test
- Rotronics — Midtronics jargon buster: https://www.rotronicsbms.com/battery-tips/midtronics-testing-jargon-buster
- GM TechLink — 12V battery ratings: https://gm-techlink.com/?p=20367
- WECT (AAA regional battery life): https://www.wect.com/2024/08/02/how-often-should-you-change-your-car-battery-depends-where-you-live
- Monroe ServiceGram — Weepage vs leakage: https://images.oreillyauto.com/parts/img/documents/mon/monroe_servicegram_weepageleakage_v01no05_eng_final.pdf
- KYB — Leaking vs sweating: https://kyb-europe.com/wp-content/uploads/2025/08/Technical-Bulletin-Leaking-vs-Sweating.pdf
- NZTA — Vehicle inspection (shock absorbers): https://vehicleinspection.nzta.govt.nz/downloadPdf/634
- AA1Car — Ball joints: https://www.aa1car.com/library/ball_joints.htm
- Brake & Front End — Ball joint/tie rod wear: https://www.brakeandfrontend.com/why-do-ball-joints-tie-rods-and-control-arms-wear-out/
- Honda Maintenance Minder (dealer guide): https://www.buerklehonda.com/a-guide-to-hondas-maintenance-minder-codes/
- Tesla Model 3 owner's manual — Maintenance intervals: https://www.tesla.com/ownersmanual/model3/en_sg/GUID-E95DAAD9-646E-4249-9930-B109ED7B1D91.html
- Toyota UK — Hybrid health check: https://mag.toyota.co.uk/toyota-hybrid-health-check
- Toyota Owners Club — HV pack health thread: https://toyotaownersclub.com/forums/topic/194641-hybrid-battery-pack-health-status
- PriusChat — Spark plug interval thread: https://priuschat.com/goto/post?id=1416052
- BITOG — Toyota ATF drain-and-fill thread: https://bobistheoilguy.com/forums/threads/when-to-drain-and-fill-atf-for-toyota.320835/
- BITOG — Alignment printout thread: https://www.bobistheoilguy.com/forums/threads/getting-a-print-out-of-alignment-specs.82512/post-1067218
- Garage Journal / Ranger5G forum threads (dealer menu items): https://www.garagejournal.com/forum/goto/post?id=5137367 ; https://www.ranger5g.com/forum/threads/fuel-induction-and-throttle-body-cleaning-service.8525/post-211556
- BodyShop Business — OEM ADAS procedure gap: https://www.bodyshopbusiness.com/closing-the-oem-procedure-gap-in-adas-calibration/
- Brake & Front End — Forward cameras after alignment: https://www.brakeandfrontend.com/?p=196547
- Repairer Driven News — IIHS camera calibration research: https://www.repairerdrivennews.com/2018/04/16/iihs-research-shows-risk-of-uncalibrated-front-facing-cameras/
- Autoblog — Car repair tricks/upsells: https://www.autoblog.com/2014/05/19/car-repair-tricks-scams-upsells/
- Haynes — Common upsells and scams: https://us.haynes.com/blogs/tips-tutorials/common-auto-repair-upsells-and-scams
- Quartz — CR dealership upsells: https://qz.com/5-car-dealership-upsells-consumer-reports-says-to-avoid
- ConsumerAffairs — Mechanic scam survey: https://www.consumeraffairs.com/news/too-many-consumers-are-being-scammed-by-auto-mechanics-claims-a-new-report-080323.html
- CarMD / AftermarketNews — CEL repair trends: https://www.aftermarketnews.com/carmd-releases-2023-check-engine-repair-trends/ ; https://www.aftermarketnews.com/carmd-vehicle-health-index-ignition-coils-spark-plugs-o2-sensors-tied-for-most-commonly-diagnosed-check-engine-repair%ef%bb%bf/ ; https://www.tomorrowstechnician.com/carmd-vehicle-health-index-marks-10-years-of-reporting/ ; https://aftermarketinsight.spglobal.com/news/4261/carmd-finds-check-engine-repair-costs-down-slightly
