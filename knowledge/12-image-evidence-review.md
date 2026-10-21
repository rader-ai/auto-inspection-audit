# 12 — Image & Video Evidence Review (Audit Engine Reference)

> Research division: EVIDENCE REVIEW of inspection photos and video in digital vehicle inspections (DVIs) and estimates. This is general technical information, not a diagnosis. Items marked **[UNVERIFIED]** could not be confirmed against a primary or reliable source in this pass. Items marked **[METHOD]** are recommended procedure reasoned from the sourced facts, not a published standard. Many sources are vendor- or forum-authored; this is flagged inline.

---

## 1) Scope & as-of date

- **As of:** 2026-10-20. Sources gathered by web search and fetch on that date.
- **Covers:** what an inspection photo or video can and cannot prove, component by component; what a good substantiating photo looks like; how to check that photos belong to this vehicle and have not been reused or altered; cross-checks between photo, grade, measurement, and recommendation; how to review video; limits of an AI reviewer (Claude) and how it should phrase findings; published accuracy claims for computer-vision tread and vehicle scanners; a per-photo checklist and scoring rubric.
- **Does not cover:** numeric replace thresholds in depth (see `07-technical-inspection-criteria.md`), or legal and dispute guidance (see `09-consumer-protection-dvi-law.md`).
- **Core principle:** A photo is evidence of what was visible to the camera at one moment. It is rarely a measurement. The strongest DVI photos show a **test instrument and its reading**. Photos without one can show *presence* of a condition (a torn boot, a bulge, a cord showing). They usually cannot show *degree* (how many 32nds, how many mm, how much moisture, how much rib loss).

---

## 2) Per-component: what photos can and can't show

Legend for each component: **CAN** = a good photo can reasonably establish this. **CANNOT** = a photo alone cannot establish this; you need a measurement, test, or hands-on check. **Best evidence** = what a strong submission includes.

### 2.1 Tires

**Tread depth**
- **CAN:** Show a tread-depth gauge seated in a groove with a readable scale. That makes the reading checkable. It can also show tread worn flush with the wear bars. Federal rules require wear bars molded at 2/32 in., and NHTSA picked that level because traction falls off quickly at that depth ([NHTSA interpretation](https://www.nhtsa.gov/interpretations/11497awkm); [Ford](https://ford.com/support/how-tos/tires-and-wheels/tire-replacement-and-maintenance/why-does-tread-wear-matter)).
- **CANNOT:** Give a depth reading from a gauge-less photo. Camera angle, lens distortion, and lighting all change how deep grooves look. Even dedicated tread-scanning software disclaims precision (see §7.4). One gauge photo cannot represent all four tires, or the inner, center, and outer grooves of the same tire. Guides recommend reading several major grooves across the width and avoiding sipes, shoulder decoration grooves, and the wear bars themselves ([NAPA Know How](https://knowhow.napaonline.com/know-how-to-read-tire-tread-depth/)).
- **Photo-review checks:**
  - Is the probe in a **main circumferential groove**, not a sipe or on a wear bar?
  - Is the gauge **perpendicular**, with the base flat on adjacent ribs?
  - Is the scale **legible**, and in which units (32nds or mm)?
  - Does the reading in the photo **match the text** in the report?
- **Best evidence:** a gauge photo per tire (ideally inner, center, outer) with position labeled (LF/RF/LR/RR), plus a wide shot that shows which wheel it is.

**Uneven or irregular wear**
- **CAN:** Show visible patterns:
  - center wear (overinflation)
  - wear on both shoulders (underinflation)
  - wear on one edge (camber)
  - feathering (toe)
  - cupping or scalloping (worn dampers, imbalance, or other suspension issues)

  Sources: [Michelin tire inspector](https://www.michelinman.com/auto/auto-tips-and-advice/tire-damage/tire-inspector-tool-tire); [Jalopnik, quoting Bridgestone on cupping](https://jalopnik.com/2074863/tire-wear-patterns-could-reveal-what-wrong-with-car/).
- **CANNOT:** Confirm the *cause*. A wear pattern is consistent with an alignment or suspension problem, but it does not prove the vehicle is out of alignment *today*. The tires may have been rotated, or the cause may already be fixed. An alignment printout (before/after) is the evidence for alignment claims. Feathering is often detected by touch. Low-angle light helps a photo show it, but flat lighting hides it.
- **Best evidence:** a raking-light photo across the tread, plus gauge readings at inner and outer grooves that show the difference.

**Sidewall cracking, bulges, cuts**
- **CAN:** A clear close-up can establish a **bulge** or bubble. Michelin treats this as internal cord damage and says not to drive on it ([Michelin – sidewall](https://www.michelin.ca/en/auto/learn/tire-damage/sidewall-problems/symptom-indentation)). A photo can also show a cut that exposes cords, or deep cracking.
- **CANNOT:** Reliably tell cosmetic surface weather-checking from structural cracking. Fine surface cracks are common on older tires and may be cosmetic at first. Cracks are structural when they are deep, reach the cords, or sit near the bead ([Michelin guidance as summarized](https://www.michelin.ca/en/auto/learn/tire-damage/sidewall-problems/symptom-indentation) **[UNVERIFIED: exact Michelin page wording for cracking]**). Crack *depth* is rarely visible in a photo. USTMA says it knows of no scientific data that sets a minimum or maximum service life for passenger tires ([Barry's Tire Tech, reproducing USTMA manual](https://barrystiretech.com/tire-aging-and-weather-cracking/)). So "cracked = replace" is not automatic.
- Watch for a **sidewall indentation** (a normal dip at a ply splice) being presented as damage. Michelin's sidewall-symptom page addresses indentations separately from bulges ([Michelin](https://www.michelin.ca/en/auto/learn/tire-damage/sidewall-problems/symptom-indentation)).

**DOT date code (tire age)**
- **CAN:** A legible photo of the TIN can establish manufacture week and year. The last four digits are week then year, so 2321 = week 23 of 2021 ([SlashGear](https://www.slashgear.com/1419676/numbers-tires-date-code/); [Firestone](https://www.firestonecompleteautocare.com/tires/tire-info/basics/tire-date-codes/)). It is also an **identity check**. If four tires are claimed "aged out," four date-code photos should show four codes. Matching codes are fine for a set bought together.
- **CANNOT:** Prove the tire is unsafe from age alone. There is no federal age limit, and guidance varies by manufacturer (see 07 §3.1).
- **Pitfall:** The full date code is often on only one sidewall, which may face inboard. A photo of a partial TIN with no date is not a date code.

### 2.2 Brakes

**Pad thickness**
- **CAN (strong):** A pad-gauge or caliper reading on the **friction material only**, legible, with position (LF outer/inner etc.). Guides stress measuring friction material, not the steel backing plate ([Phoenix Systems pad gauge guide](https://phoenixsystems.co/blogs/company-news-tips/how-do-i-measure-brake-pad-thickness-with-a-gauge), vendor).
- **CAN (moderate):** A photo through the wheel spokes or caliper window may show the outer pad roughly. It can show near-zero friction material or metal-to-metal contact.
- **CANNOT:** Estimating mm from a through-the-wheel photo is unreliable. The **inner pad is usually not visible** and often wears faster, because the piston pushes on it directly. A difference of more than about 2 mm side to side can point to a sticking caliper ([CarFromJapan](https://carfromjapan.com/article/brake-pad-thickness), secondary). Pads can look thick and still be cracked, glazed, or separated from the backing plate. Thresholds vary by OEM, so check the service manual (see 07).
- **Removed-pad photos:** Stronger, because both pads can be gauged. But they must be tied to the vehicle and wheel position. A loose pad on a bench could be from any car. Ask for the pad beside the wheel or caliper, or with a position label.

**Rotors (lip, scoring, heat spots)**
- **CAN:** Show a pronounced lip, deep grooves, cracks, heavy rust on the friction surface, and bluish heat tint.
- **CANNOT:** Show **thickness vs. discard spec**. That needs a micrometer reading compared with the minimum stamped on the rotor or in the OEM spec. A photo also cannot show **runout or thickness variation**, which needs a dial indicator or micrometer. Scoring limits are OEM-specific: one Saab procedure allows grooves to 1.5 mm ([Saab WIS](https://saabwisonline.com/9-4x/2011/5-brakes/brake-discs-and-pads/fault-diagnosis-fault-symptoms/brake-rotor-surface-and-wear-inspection)), while a heavy-duty manual uses a much smaller figure. Sources disagree on blue tint. Fras-le says blueing alone does not require replacement if the disc is within tolerance ([Fras-le via Transport Operator](https://transportoperator.co.uk/?p=30722)). **Hard spots** extend below the surface and generally call for replacement ([Brake & Front End](https://www.brakeandfrontend.com/?p=39135)). Light surface rust on a parked car's rotors is common and wipes off with braking. **[UNVERIFIED as a sourced claim; widely observed]**
- **Best evidence:** a micrometer on the rotor with a readable display, plus the discard spec (photo of the stamped "MIN TH" or a cited OEM value).

### 2.3 Fluids

**General rule: color is not a valid condition test for brake fluid, ATF, or coolant.** A photo of fluid color is at best a *screening observation*. Test strips, refractometers, and meters produce real readings, and a photo of the result is valid evidence.

- **Brake fluid:**
  - Looks are not a moisture test. Color may hint at age or contamination but does not give water content or boiling reserve. Dark fluid can test fine, and clear fluid can test high in moisture ([Phoenix Systems](https://phoenixsystems.co/blogs/company-news-tips/why-that-clean-brake-fluid-might-be-a-silent-problem), vendor; [Rick's Free Auto Repair Advice](https://ricksfreeautorepairadvice.com/the-truth-about-brake-fluid-color-and-brake-fluid-condition/), blog).
  - Valid evidence is a photo of a **moisture strip or copper strip against its color chart**, or a boiling-point or moisture meter display. One source cites 200 ppm copper as a change point ([Rick's](https://ricksfreeautorepairadvice.com/the-truth-about-brake-fluid-color-and-brake-fluid-condition/) **[UNVERIFIED against OEM]**).
  - Caveat: reservoir fluid may test better than fluid at the calipers. Strips are for glycol (DOT 3/4/5.1) fluid, not silicone DOT 5 ([Phoenix Systems](https://phoenixsystems.co/blogs/company-news-tips/brake-fluid-test-strips-the-quick-check-that-tells-a-bigger-story-about-your-brakes)).
- **Automatic transmission fluid (ATF):**
  - Color is a weak indicator. Practitioners note that clean red fluid can come out of a worn transmission, and dark fluid can come out of a healthy one ([Ram Forum](https://www.ramforum.com/threads/transmission-fluid-dark-before-30k-miles.137306/); [BITOG](https://bobistheoilguy.com/forums/threads/why-so-much-attention-toward-atf-color.40838/post-527180), anecdotal).
  - Burnt smell, debris, and shift behavior matter more, and none of these can be photographed. Color-chart "swatch" cards are used as a sales aid in shops ([BITOG](https://bobistheoilguy.com/forums/threads/why-so-much-attention-toward-atf-color.40838/post-527175)).
  - **[UNVERIFIED: no OEM bulletin found stating color is non-diagnostic; flag as practitioner consensus.]**
- **Coolant:**
  - Color does not reliably indicate type or condition. Different chemistries share colors, and makers use dyes inconsistently ([Holts/Prestone UK](https://www.holtsauto.com/prestone/why-is-coolant-different-colours/); [BITOG](https://bobistheoilguy.com/forums/threads/green-vs-orange.229893/)).
  - Valid evidence: a **refractometer reading** (most accurate for freeze point) or **test strips** (less precise; indicate freeze point and additive level). This is per a Cummins bulletin quoted on [BITOG](https://bobistheoilguy.com/forums/threads/coolant-hydrometers.90700/) and an SAE paper on strips ([SAE 960645](https://saemobilus.sae.org/content/960645)).
  - A military field study found strip readings sometimes deviated from the refractometer by more than 10°F ([DTIC AD0750569](https://apps.dtic.mil/sti/tr/pdf/AD0750569.pdf), partly garbled; approximate).
  - Photos *can* show oil contamination (sludge, a milky layer), heavy rust or scale, or a low level against the reservoir marks.
- **Engine oil:** Color says little about remaining life on modern oils **[UNVERIFIED; not researched in this pass]**. A photo can show the level on the dipstick only if the dipstick is legible and the photo is in focus.
- **Fluid level photos:** Valid if the MIN/MAX marks and the fluid line are both visible. Note that brake fluid level drops as pads wear, so low brake fluid alone is not proof of a leak. **[UNVERIFIED; standard practice]**

### 2.4 Filters (engine air, cabin)

- **CAN:** Show debris (leaves, rodent nesting, bugs), physical damage, oil soaking, or a missing filter.
- **CANNOT:** Establish remaining life. Donaldson states that visual inspection of air filters is not adequate to set service life, and that very dirty-looking filters may have substantial life left. It recommends restriction measurement instead ([Donaldson catalogue](https://ecatalog.donaldson.com/view/477292580/136/); [CCJ](https://www.ccjdigital.com/business/article/14906155/think-that-air-filters-too-dirty-try-donaldsons-filter-service-indicators)). Note that this is heavy-duty guidance and Donaldson is a vendor.
- **Lighting and staging:** The inlet side of an air filter is always darker than the outlet side. A filter photographed against a bright light, or next to a brand-new white filter, will look worse. Cabin-filter intervals are usually time/mileage per the owner's manual, shortened for dusty use ([BITOG excerpt of Cadillac manual](https://bobistheoilguy.com/forums/threads/cabin-filter-change-interval.324421/)).
- **Audit stance:** "Dirty filter" photos are **Weak** evidence unless the vehicle is at or past the OEM interval or the photo shows debris or damage.

### 2.5 Belts (serpentine/accessory)

- **CAN:** Show chunks missing, rib separation, cords showing, fraying edges, glazing, contamination (oil), and misalignment wear. All of these are visible failures.
- **CANNOT:** Show **material loss on EPDM belts**, the main wear mode on modern belts. Gates says the old "three cracks in three inches" rule suits neoprene, not EPDM. EPDM belts can pass 100,000 miles with no visible cracks, and material loss is the better indicator ([Gates TT002-15](https://www.gates.com/content/dam/documents-library/tech-tips-bulletins/tt002-15.pdf)). Gates also notes that about 5% rib material loss can cause problems ([same](https://www.gates.com/content/dam/documents-library/tech-tips-bulletins/tt002-15.pdf)).
- **Implication:** A "cracked belt" photo on an EPDM belt is not proof of wear. A *no-crack* photo is not proof the belt is fine either.
- **Best evidence:** a photo or short video of the **Gates belt-wear gauge** (or equivalent) seated in the grooves. A worn belt lets the gauge rock side to side ([Gates TT002-15](https://www.gates.com/content/dam/documents-library/tech-tips-bulletins/tt002-15.pdf)). Rocking is best shown in **video**. Gates also offers a phone-app gauge that returns green/yellow/red ([CCJ](https://ccjdigital.com/business/article/14925015/gates-app-measures-serpentine-belt-wear)); a screenshot of its result is moderate evidence.

### 2.6 Hoses

- **CAN:** Show visible splits, bulges or ballooning, chafe-through, wet residue at a clamp, and crusted coolant residue at a joint.
- **CANNOT:** Show softness, internal deterioration, or "spongy" feel, which are tactile checks. Hose surface cracking may be cosmetic. **[UNVERIFIED: no Gates/Dayco hose-inspection page retrieved in this pass; Gates publishes hose guidance; follow-up needed.]**

### 2.7 Leaks (engine, transmission, differential, power steering, coolant)

- **CAN:** Show wet, shiny fluid, drips, puddles, and fluid trails. The more of these that are in frame, the stronger the photo.
- **CANNOT (generally):**
  1. **Fresh vs. old.** Existing residue makes it very hard to tell an old stain from a current leak ([EngineerFix](https://engineerfix.com/how-to-diagnose-an-engine-oil-leak/)).
  2. **Source.** Oil runs downhill and is spread by airflow, so the wettest spot is often not the origin ([YourMechanic](https://yourmechanic.com/article/how-to-find-the-source-of-an-oil-leak-by-ed-ruelas)).
  3. **Rate.** Seepage (a dry, dirt-caked film) and an active leak (wet, dripping) look different, but a photo shows one instant.
  4. **Which fluid.** Color under shop lighting is ambiguous.
- **Best evidence:** cleaned area → run → **UV-dye photo** showing the glow traced to the origin. Or a before/after pair at known times ([MotoIQ](https://motoiq.com/wrench-tips-30-finding-oil-leaks-using-fluorescent-goo/); [YourMechanic](https://yourmechanic.com/article/how-to-find-the-source-of-an-oil-leak-by-ed-ruelas)). Note that the leak source named in the report (e.g., "valve cover gasket") should be at the **top** of the wet trail in the photo.
- **Red flag:** A recommended repair for a gasket far from where the photo shows wetness, or a "leak" photo with only dry, dusty residue described as "active."

### 2.8 Suspension (shocks/struts, boots, bushings)

**Shock/strut misting vs. leaking**
- **CAN:** Show a heavy, wet coating running the length of the body, drips, or fluid below the spring seat. These are consistent with leakage.
- **Manufacturer criteria:**
  - **Monroe:** a minimal film is "weepage" and does not require replacement. Leakage means most of the unit looks wet and oily, or fluid is dripping ([Monroe ServiceGram](https://images.oreillyauto.com/parts/img/documents/mon/monroe_servicegram_weepageleakage_v01no05_eng_final.pdf), via search summary; direct fetch returned 403).
  - **KYB:** "sweating" is a slight, even film from the top that leaves no excess on fingers, may reach the spring seat, and does not grow. A leak extends beyond the spring seat, leaves oil on fingers, and shows thick wet streaks or drips that worsen over time ([KYB Europe bulletin, 2025](https://kyb-europe.com/wp-content/uploads/2025/08/Technical-Bulletin-Leaking-vs-Sweating.pdf)).
  - A vehicle-maker TSB on NHTSA's site says misting is normal evaporation and should not be replaced ([NHTSA TSB MC-10170656](https://static.nhtsa.gov/odi/tsbs/2020/MC-10170656-0001.pdf) **[UNVERIFIED: issuing OEM not confirmed]**).
- **CANNOT:** Perform KYB's finger test, and cannot show change over time from a single photo. A light film photographed close-up with flash can look dramatic. Fluid on a strut may also come from another source above it (engine oil, power steering). **[UNVERIFIED that Monroe states this explicitly]**
- **Best evidence:** a wide shot showing the whole unit and spring seat, a close-up, and ideally a second photo after wiping and a test drive.
- A **leaking** finding is supported when wetness extends below the spring seat or drips. A "light film at top" photo labeled "leaking — replace" is **Contradicts** under KYB/Monroe criteria.

**Torn boots and bushings**
- **CAN:** Show a torn or split boot, missing boot, cracked or extruded bushing rubber.
- **CANNOT:** Show **play** in ball joints, tie rods, or bushings. That needs a pry bar or dial indicator, and **video** of movement is the right evidence. See 07 for play specs.

### 2.9 CV boots / axles

- **CAN:** Show a torn boot, grease slung onto nearby parts, a missing clamp. These are strong visual evidence of a boot failure.
- **CANNOT:** Show whether the **joint** is damaged. Practitioner consensus is that a silent joint with clean grease may need only a boot and regrease. A clicking joint, especially in turns, or gritty grease points to axle replacement ([Acurazine forum](https://acurazine.com/forums/3g-tl-problems-fixes-114/cv-joint-%5B-913147), anecdotal).
- Some state inspection rules treat torn boots as **advisory, not rejection**. For example, Utah says to advise the customer on torn boots and reject only for a clicking joint on a road test ([Utah R714-160-10](https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R714-160-10)); Virginia does not reject defective CV boots ([19VAC30-70-110](https://law.lis.virginia.gov/admincode/title19/agency30/chapter70/section110/)).
- **Audit implication:** A torn-boot photo supports a **boot** recommendation. It supports an **axle** recommendation only with a documented noise or joint-play finding.

### 2.10 Battery

- **CAN:** Show terminal corrosion, a swollen or cracked case, a leaking case, a loose hold-down, and a date sticker.
- **CANNOT:** Show capacity or health. Corrosion does not by itself mean the battery is bad. It can come from venting or seepage at the post and can often be cleaned, but the battery should still be tested ([Rick's Free Auto Repair Advice](https://ricksfreeautorepairadvice.com/does-corrosion-on-car-battery-terminals-mean-the-battery-is-bad/); [ToolSource](https://www.toolsource.com/blog/battery-terminal-corrosion-safe-cleanup-testing-and-when-to-replace/)).
- **Best evidence:** a **tester printout or screen** (e.g., Midtronics). A full printout shows:
  - state of health
  - measured vs. rated CCA
  - internal resistance or conductance
  - voltage and state of charge

  Midtronics material describes 90% or more of rated CCA as healthy and below 80% as a warning sign, but the same Midtronics page elsewhere calls 80%+ good, 70–79% marginal and < 70% replace, so there is no single cutoff. GM warranty policy relies on the tester's Replace/Bad decision code, not a percentage (https://gm-techlink.com/?p=16086). It also notes that surface charge, right after charging or a jump, can distort readings ([Midtronics – hidden clues](https://www.midtronics.com/blog/the-hidden-clues-in-battery-test-printouts-that-techs-might-miss); [Midtronics – key indicators](https://www.midtronics.com/blog/key-indicators-of-a-healthy-battery-test/); vendor).
- **Printout photo checks:**
  - Does the **rated CCA entered** match the battery label in another photo? Entering the wrong rating skews the result.
  - Does the date/time match the visit?
  - Does the VIN (if printed) match the vehicle?
  - Does "Replace" follow from the numbers?

### 2.11 Wipers

- **CAN:** Show a torn, split, or detached rubber edge, or a frame that is bent or corroded.
- **CANNOT:** Show streaking performance or hardening reliably. Streaking can come from a dirty windshield, so clean the glass and retest ([BITOG](https://bobistheoilguy.com/forums/threads/replacement-wiper-blades.208727/latest), anecdotal). A short video of a wipe on wet glass is better evidence than a still.

### 2.12 Lights

- **CAN:** A photo of the lamp **switched on** next to its working mate can establish an out bulb. A photo can also show cracked or moisture-filled housings and yellowed lenses.
- **CANNOT:** A photo of an unlit lamp proves nothing about whether it works. Headlight aim cannot be judged from a casual photo. Lens haze severity is lighting-dependent. **[METHOD]**

### 2.13 Exhaust

- **CAN:** Show holes, broken hangers, separated joints, heavy rust-through, soot trails at a joint (consistent with a leak).
- **CANNOT:** Prove an active exhaust leak (usually confirmed by sound, smoke test, or feel), or that surface rust on a pipe is structural. **[METHOD; no exhaust-specific source retrieved]**

### 2.14 Undercarriage / frame rust

- **CAN:** Show perforation (holes), flaking scale with visible section loss, broken or separated brackets, and rust at suspension mounting points.
- **CANNOT:** Tell surface rust from structural loss. Rust can look superficial while the metal underneath has thinned a lot. Inspectors use a scrape or pick test and a hammer-tap test: solid metal rings, weak metal sounds dull or perforates ([EngineerFix](https://engineerfix.com/is-surface-rust-on-a-frame-bad/); [ToolSource – Tacoma frames](https://www.toolsource.com/blog/how-to-assess-and-repair-severe-frame-rust-on-tacomas-a-technicians-reality-check/)).
- UK MOT practice judges corrosion by **location and function**. Small corrosion at a load-bearing mount can be serious, while heavy corrosion on an unimportant panel may not matter ([NI DVA appendix](https://www.infrastructure-ni.gov.uk/articles/appendix-structural-integrity-and-corrosion)). The official MOT blog advises "pass and advise" when in doubt ([MOT blog](https://mattersoftesting.blog.gov.uk/why-its-important-to-check-for-corrosion/)).
- **Best evidence:** a photo of a pick or screwdriver penetrating the metal, or of a hole, with a context shot showing where on the frame it is.
- **Normal-condition caution:** Surface rust on bare-steel underbody parts (exhaust, rotors, suspension arms) of a vehicle from a salt region is normal and is not, by itself, a repair finding. **[UNVERIFIED as a sourced statement]**

### 2.15 Summary table

| Component | Photo alone CAN show | Photo alone CANNOT show | Strong evidence |
|---|---|---|---|
| Tire tread | flush with wear bars; cords | depth in 32nds | gauge in groove, legible, per tire/position |
| Tire wear pattern | presence of pattern | current alignment state | raking light + inner/outer gauge; alignment printout |
| Sidewall | bulge, cut to cords | crack depth; cosmetic vs structural | close-up + context; cords visible |
| Tire age | DOT week/year (if legible) | that age = unsafe | full TIN photo per tire |
| Brake pads | metal-to-metal; near-zero outer pad | mm thickness; inner pad | pad gauge on friction material, position labeled |
| Rotors | lip, deep grooves, cracks | thickness vs discard; runout | micrometer + discard spec |
| Brake fluid | level vs marks | moisture/boiling point | strip vs chart; meter reading |
| ATF | level; debris on stick | condition from color | OEM-procedure check; fluid analysis |
| Coolant | oil contamination; level | freeze point; inhibitor level | refractometer / strip |
| Air/cabin filter | debris, damage | remaining life | restriction reading / OEM interval |
| Belt | chunks, splits, cords | EPDM material loss | wear gauge (video of rocking) |
| Leak | wet fluid, drips | fresh vs old; source | clean + dye/UV; before/after |
| Shock/strut | wet below spring seat; drips | misting vs leak (marginal); growth | wide + close-up; wiped recheck |
| CV boot | torn boot, slung grease | joint damage | boot photo + noise/play note |
| Battery | corrosion, swelling | health | tester printout matching battery label |
| Lights | out (if lit comparison) | aim | photo with lamp on |
| Frame rust | holes; section loss | surface vs structural (often) | pick/hammer test photo + location |

---

## 3) Evidence standards

### 3.1 What a strong substantiating photo includes

Drawn from DVI vendor best practices plus the instrument requirements above. Vendors recommend a photo per checklist item ([AutoVitals](https://blog.autovitals.com/digital-vehicle-inspection-best-practices)), a close-up plus a wider shot so the customer can see where the part is ([AutoServe1](https://autoserve1.com/founder-protip-photos-improve-digital-vehicle-inspection/)), and good lighting with fewer distractions ([AutoVitals](https://blog.autovitals.com/digital-vehicle-inspection-best-practices)).

1. **Identifiable item.** The component is in frame, in focus, and recognizable as what the report says it is.
2. **Position.** The corner or side is stated (LF/RF/LR/RR; inner/outer; bank 1/2), ideally visible in the image (wheel, fender, chalk mark, or a label).
3. **Context shot plus close-up.** A wide shot ties the part to the vehicle and location. The close-up shows the defect.
4. **Measurement instrument with readable scale** whenever the finding is quantitative: tread gauge, pad gauge, micrometer, belt gauge, strip vs. chart, refractometer, tester printout.
5. **Adequate lighting and focus.** No blown-out flash glare on the area of interest, no motion blur, no extreme digital zoom.
6. **Unedited framing.** No crop that removes context needed to judge the claim, such as the spring seat on a strut or the wear bars on a tire.
7. **Vehicle linkage.** At least one photo in the report ties the set to this vehicle: VIN plate or door label, odometer, license plate, or a distinctive feature (see §4).
8. **Timestamp.** A DVI platform timestamp, or embedded metadata if available (see §4.3).

### 3.2 Weak or non-probative photos

- A generic "it's dirty" shot of a filter, fluid, or engine bay with no instrument and no interval context.
- A through-the-wheel pad photo with no gauge, used to claim a specific mm value.
- A fluid-color photo, or a fluid on a white towel or swab, used as the sole basis for a flush.
- A belt "cracks" photo on an EPDM belt.
- A close-up of a light oil film on a strut, cropped so the spring seat is not visible.
- A "leak" photo showing dry, dust-caked residue labeled active, with no dye or cleaned recheck.
- One tire photo used to justify all four tires.
- An unlit headlamp used to claim a bulb is out.
- A photo where the component cannot be identified, or could be on any vehicle.
- Bench photos of removed parts with no link to the vehicle or position.
- Stock or illustrative images, such as manufacturer diagrams or "example" pictures inserted by the DVI template. Some DVI platforms offer canned reference images. **[UNVERIFIED which platforms; check report for "example" labels]**

---

## 4) Authenticity & integrity checks

**Framing rule:** These checks find *inconsistencies to ask about*, not proof of wrongdoing. Template images, mislabeled corners, and photos from the wrong vehicle are usually workflow errors (a tech photographing the next car, a mis-tap in the app). Report them as "does not appear to match; please clarify."

### 4.1 Does the photo belong to THIS vehicle?

Compare photos within the report against each other and against facts the user knows. **[METHOD]**

| Check | What to compare | Notes |
|---|---|---|
| VIN | VIN plate (dash or windshield) or door-jamb label photo vs. the VIN on the RO/estimate | Strongest single link. Last 6–8 digits are enough to compare. |
| Odometer | Odometer photo vs. the RO mileage-in | Mismatch may be a typo; note it. |
| Plate | License plate in any context shot | Consumer can confirm directly. |
| Tire size | Size on sidewall in photos (e.g., 235/65R17) vs. the door-placard size and the size quoted on the estimate | A different size on one "LF" tire photo is a flag. Mixed sizes can be legitimate on staggered fitments. |
| Tire brand/model | Brand and tread pattern consistent across all tire photos, and with what the owner has | Four different tread patterns when the owner has a matched set = flag. |
| DOT codes | Week/year consistent across a set | A set bought together usually shares close date codes. |
| Wheels | Wheel design, finish, center cap, lug style consistent across corner photos | Different alloy designs within the report = flag. |
| Paint color & body | Paint visible at fender/door edges; body style; trim | Easy consumer check. |
| Brake hardware | Caliper color, style, rotor type (slotted/drilled) consistent with the vehicle and across corners | Performance calipers on a base model = flag. |
| Left vs. right | Steering parts, the side of the engine bay, the direction the wheel faces, which side the caliper sits on | Calipers are usually trailing or leading by design, so mirroring can reveal mislabeled sides. **[METHOD]** |
| Engine bay | Engine cover shape, under-hood labels, battery location vs. the vehicle's engine | |
| Mileage plausibility | Wear shown vs. mileage (e.g., cords showing on 6-month-old tires) | Plausible with damage or alignment problems; worth asking. |

### 4.2 Duplicate or reused photos

- **Within one report:** Look for the same image (or the same frame, slightly cropped or brightened) used for two corners or two items, e.g., "LF pad" and "RF pad" identical. Look for matching background details: the same shop-floor stain, the same glove, the same lighting reflection. **[METHOD]**
- **Across reports:** If the user has prior inspection reports from the same shop, compare. An identical image appearing on two visits or two vehicles is a strong flag. A shop owner can do this at scale across their DVI system by spot-checking techs.
- **Stock or web images:** A reverse image search (Google Lens "find image source," TinEye "oldest first") can show whether a photo appears elsewhere online ([Bellingcat](https://www.bellingcat.com/resources/2015/05/08/manual-reverse-image-search-with-google-and-tineye/); [Georgetown library guide](https://guides.library.georgetown.edu/writ015day/verify); [Data Detox Kit](https://datadetoxkit.org/en/misinformation/reversesearch/)). Limits: it will not find images on private systems such as DVI platforms, so "no match" proves nothing. Uploading customer images to third-party search services has privacy implications; the consumer should decide.

### 4.3 Timestamps and metadata (EXIF)

- **Claude cannot read metadata.** Anthropic's docs state Claude does not parse or receive image metadata ([Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)). EXIF checks must be done with a separate tool. In Claude Code, `exiftool` can be run locally if installed. Or the user can use their OS file-info panel.
- **Metadata is often stripped.** Many platforms re-encode uploads and strip EXIF (e.g., Instagram, Facebook, Reddit-hosted images), while file lockers and some apps keep it ([Fast.io overview](https://fast.io/resources/social-media-photo-metadata-platforms-strip/), vendor). DVI platforms commonly deliver images through web links or texts, which likely re-encode them. **[UNVERIFIED: no DVI vendor documentation found on EXIF handling.]** **Absence of EXIF is normal and is not a red flag.**
- **When present:** Compare capture date/time with the visit date and the RO time-in/time-out. Check that the camera model is consistent across the set. Note that EXIF is easily edited, so a match is weak support and a mismatch is a question, not proof.
- **Content Credentials (C2PA):** Some newer phones sign captures. Google's Pixel 10 camera adds C2PA Content Credentials to JPEG captures, and Google Photos records edits ([Google Security Blog, Sept 2025](https://security.googleblog.com/2025/09/pixel-android-trusted-images-c2pa-content-credentials.html)). If a DVI image carries intact credentials, that is strong provenance. Most will not, because DVI apps and re-encoding usually drop them. **[UNVERIFIED for any DVI platform]**

### 4.4 Cropping, framing, and editing

- **Misleading framing** is far more common than pixel editing. **[UNVERIFIED as a measured rate]** Examples:
  - a tight crop that hides the spring seat
  - a flash close-up that makes a light film look wet
  - a dirty filter next to a pristine new one
  - a gauge held at an angle so its scale reads high or low
  - a wear-bar shot where the probe sits on the bar
- **Signs of editing to look for (low reliability):** inconsistent shadows or lighting direction, repeated texture patches (cloning), mismatched blur or noise between regions, text overlays covering parts of the image, and odd edges around a part.
- **Forensic tools are unreliable for this use.** Error Level Analysis (ELA) maps JPEG compression differences, not "edits." It gives false positives on smooth areas, can miss edits saved with the same software, and loses signal after repeated re-saves ([FotoForensics ELA tutorial](https://fotoforensics.com/tutorial.php?tt=ela); [FotoForensics common mistakes](https://fotoforensics.com/tutorial-mistakes.php); [GIMP forensics wiki](https://sourceforge.net/p/gimp-forensics/wiki/Error%20Level%20Analysis/)). DVI images are typically re-compressed, which makes ELA even less meaningful.
- **Claude cannot detect AI-generated images.** Anthropic says Claude cannot determine whether an image is AI-generated and should not be relied on to detect fake or synthetic images ([Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)). **The skill must never state or imply that an image is fabricated or AI-generated.**

### 4.5 Known fraud context (for calibration, not accusation)

- Documented cases of deliberate damage exist. Pennsylvania state police charged two dealership technicians with damaging a customer's brake pads, found after a second opinion ([The Drive](https://www.thedrive.com/news/dealership-techs-caught-tampering-with-customers-brakes-police-say)). This is the strongest reason to recommend **in-person verification or a second opinion** over remote "photo proof."
- No published case of a shop sending another vehicle's DVI photo was found in this pass **[UNVERIFIED]**. Treat mismatch scenarios as plausible but unquantified.
- DVI marketing claims photos increase approval rates ([Tire Review](https://www.tirereview.com/digital-vehicle-inspection-shop-trust/); [AutoServe1](https://autoserve1.com/founder-protip-photos-improve-digital-vehicle-inspection/)). That is an incentive to include *many* photos, not necessarily *probative* ones.

---

## 5) Consistency cross-checks

Run these for every line item. Any mismatch becomes a "question for the shop" in the output. **[METHOD]**

| # | Cross-check | Example mismatch | Output phrasing |
|---|---|---|---|
| C1 | **Photo vs. grade** (green/yellow/red) | Pad photo shows a gauge reading of 7 mm, item graded red | "Photo shows ~7 mm on the gauge, which is inconsistent with a red/urgent grade. Ask for the OEM minimum and the measured value." |
| C2 | **Photo vs. measurement text** | Text says 3/32, gauge in photo reads 6/32 | "The written value does not match the gauge visible in the photo." |
| C3 | **Photo vs. recommendation** | Torn CV boot photo → recommendation is a full axle, no noise noted | "Photo supports a boot repair; the axle recommendation needs a documented joint finding." |
| C4 | **Coverage: N items vs. N photos** | "Replace all 4 tires," one tire photographed | "Only one tire is documented; the other three are unsupported by photos." |
| C5 | **Position consistency** | Item says LF, but the photo shows a right-side wheel by steering or caliper orientation | "Position in photo may not match the label." |
| C6 | **Pair logic** | Both front pads "2 mm," but the left and right photos look very different | Ask for both gauge readings. |
| C7 | **Measurement vs. threshold** | Tread 5/32 graded red, while the shop's own legend says red <3/32 | Flag the internal inconsistency. |
| C8 | **Photo vs. narration/notes** | Note says "active leak, dripping," photo shows dry caked residue | "Photo does not show active wetness." |
| C9 | **Cross-item** | Brake fluid "low – leak suspected" + pads near minimum | Low fluid may reflect pad wear (piston extension), not a leak. **[UNVERIFIED; standard practice]** |
| C10 | **Photo vs. vehicle data** | Tire size in photo ≠ placard/estimate size; VIN digits ≠ RO | Identity question (see §4.1). |
| C11 | **Photo vs. price/part** | Quote is for a "strut assembly," photo shows a shock-absorber vehicle, or the estimate lists a different tire size | Ask for clarification. |
| C12 | **Photo vs. history** | Same "worn" belt photographed last visit and graded yellow, now red with no new evidence | Ask what changed. |
| C13 | **Duplicate image** | Same image used for two items or corners | "Two items appear to use the same photo." |
| C14 | **Required vs. Suggested** | Photo shows a functioning but aged part, priced and labeled as a safety item | Map to MAP-style Suggested (see 07 §2). |

---

## 6) Video review

No published standard for reviewing DVI videos was found. The following is **[METHOD]**, built from the component facts above.

### 6.1 What video adds over stills
- **Motion and play:** ball-joint, tie-rod, and wheel-bearing play with a pry bar or hand rocking; a belt gauge rocking (Gates' worn-belt test is about lateral movement, per [Gates TT002-15](https://www.gates.com/content/dam/documents-library/tech-tips-bulletins/tt002-15.pdf)); tensioner flutter; engine-mount movement.
- **Active leaks:** drips forming in real time.
- **Function:** lights turning on and off, wipers on wet glass, warning lamps, a scan-tool screen.
- **Continuity:** a single continuous take from the VIN or plate to the component ties the defect to the vehicle better than separate stills.
- **Sound:** CV click in turns, bearing growl (audio quality permitting). Claude cannot hear audio in frames. Audio claims must be transcribed or taken at face value, and noted as unverified.

### 6.2 Narration vs. what is shown
- Transcribe or summarize each narration claim. For each, note whether the frames **show** it, **are consistent with** it, or **do not show** it.
- Common gaps:
  - "See how much play" with no visible movement relative to a fixed reference
  - "Pads are almost gone" without a gauge
  - "This is leaking" over a dry component
  - a measurement number spoken but not shown
- **Measurement demonstrations:** The tool must be visibly seated correctly and the readout legible in at least one frame. If the reading is spoken only, score as Partial.
- **Play demonstrations:** Look for a fixed reference in frame (e.g., the knuckle vs. control arm) and for the hand-applied force. Movement of the *whole* assembly with the hand is not joint play. **[UNVERIFIED as a sourced rule; widely taught]**

### 6.3 How to sample frames (Claude accepts images, not video)
- Claude's API takes still images (JPEG/PNG/GIF/WebP; animated GIFs use only the first frame) ([Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)). Video must be turned into frames, by the user taking screenshots or by a tool such as `ffmpeg` when running in Claude Code.
- **Recommended sampling [METHOD]:**
  1. Take a baseline grid of ~1 frame per second for short clips (<60 s), or ~1 per 2–3 s for longer ones.
  2. Add frames at every narration claim timestamp, at any gauge readout, and at the start and end of every motion demonstration (rest position vs. max displacement).
  3. Add the frame(s) showing vehicle identity (VIN, plate, odometer).
  4. Keep frames at full resolution. Do not downscale below what keeps scales legible. Claude's high-resolution tier handles up to a 2576 px long edge; larger images are downscaled ([Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)). Crop to the region of interest *in addition to*, not instead of, a full frame, so context is preserved.
  5. Label frames with their timestamps ("Frame 00:14") so findings can be cited.
- **Limits:** Single frames lose motion. For play claims, compare a rest frame with a max-displacement frame against a fixed reference. If the difference cannot be seen, report "cannot determine from sampled frames," not "no play."

---

## 7) AI-reviewer limits & framing

### 7.1 Known limits of Claude's vision (from Anthropic documentation)
Source: [Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision).
- May hallucinate or err on **low-quality, rotated, or very small** images (under ~200 px).
- **Spatial and localization output is approximate.** Do not use pixel geometry to compute a measurement.
- **Counting is approximate**, especially with many small objects.
- **Cannot detect AI-generated images.**
- **Does not receive metadata.**
- Images over the model's resolution limit are **downscaled**, which can make small gauge scales illegible. Heavy JPEG compression degrades reading of text and fine detail.
- Anthropic advises human review for high-stakes use and not relying on Claude where perfect precision is required.

Third-party evaluations report weaker performance on dense non-text visual layouts and counting ([arXiv 2602.15950, preprint](https://www.arxiv.org/pdf/2602.15950); [Roboflow evaluation](https://blog.roboflow.com/claude-fable-5-for-vision/)). Treat these as indicative only.

### 7.2 Image-condition limits that apply to any reviewer
- **No scale:** Without a gauge or known-size reference, depth and thickness cannot be measured. Perspective makes grooves look deeper or shallower.
- **Lighting:** Flash glare hides texture. Raking light exaggerates it. Shop LED color shifts fluid and rust color.
- **Compression and resolution:** DVI texts and portals often deliver compressed images. Fine cracks, gauge hash marks, and DOT digits may not survive.
- **Single instant:** No before/after, so growth and rate (leaks, sweating) cannot be shown.
- **Occlusion:** The inner pad, back of the rotor, inboard sidewall, and upper strut are often hidden.

### 7.3 Confidence language (required phrasing)

Use these phrases; avoid verdict words. **[METHOD]**

| Situation | Use | Avoid |
|---|---|---|
| Photo clearly shows the condition with a legible instrument | "The photo shows a gauge reading of about X, which **supports** the finding." | "Proven," "definitely" |
| Photo shows the condition but not its degree | "The photo is **consistent with** [condition], but it does not show how severe it is." | "Needs replacing" |
| Photo doesn't show what is claimed | "The photo **does not show** [claim]." | "The shop is wrong," "false" |
| Can't tell | "This **cannot be determined from the photo**; [test] would confirm it." | Guessing a value |
| Photo contradicts claim | "The photo **appears inconsistent with** [claim] because [specific visible fact]. Worth asking the shop to clarify." | "Fraud," "lie," "fake," "scam" |
| Identity mismatch | "This photo **may not be from your vehicle**: [specific difference]. It could be a labeling mix-up; ask the shop." | "Doctored," "stolen photo" |
| Possible edit | "[Specific visual oddity] is visible. Image analysis can't confirm editing; ask for the original or an in-person look." | "Photoshopped," "AI-generated" |

### 7.4 Rules to avoid false accusations
1. **Never assert fraud, intent, or fabrication.** Describe observations and the gap between evidence and claim.
2. **Absence of evidence ≠ evidence of absence.** A missing gauge photo means *unsupported by the photo*, not *the part is fine*.
3. **Prefer benign explanations first:** mislabeling, template images, the tech photographing the wrong car, rotation history, a typo.
4. **Separate the technical conclusion from the evidence grade.** A recommendation can be technically reasonable (e.g., OEM interval reached) even with weak photos.
5. **Always offer a verification path:**
   - ask the shop for the measurement or test result
   - ask to see the part in person, or ask for old parts back
   - get a second opinion
   - for tires and pads, check yourself with a gauge or coin
6. **Quote what is visible.** "Gauge needle at the '7' mark" is better than "plenty of pad."
7. **State uncertainty about the image itself:** resolution, blur, glare, compression.
8. **Never overrule an instrument reading with visual impression,** unless the instrument is visibly misused (probe on a wear bar, gauge on the backing plate).

### 7.5 Computer-vision accuracy benchmarks (to calibrate expectations)

Purpose-built systems with controlled cameras, lighting, lasers, or magnetic sensors still state limits. A general vision model looking at an arbitrary DVI photo should be assumed *less* accurate than these, and should not output numeric depth without a gauge in frame.

| System | Method | Claimed accuracy | Caveats | Source |
|---|---|---|---|---|
| **Anyline Tire Tread Scanner** (smartphone SDK) | Phone camera + CV, guided capture | Average accuracy **0.5 mm (~1/32")** for 1–10 mm depth on recommended devices; grooves ≥5 mm wide | Datasheet calls the result an estimate and says Anyline does not guarantee it matches reality. It is not a roadworthiness verdict. Extreme lighting, distance, shiny surfaces, blur, and low resolution limit accuracy. Needs a ≥1080p camera. | [Anyline datasheet](https://anyline.com/?p=25309); [MOTOR launch coverage](https://www.motor.com/2022/11/anyline-launches-industry-first-tire-tread-scanner-for-smartphones-at-sema-show/) |
| **UVeye Artemis** (drive-through tires); Atlas (body), Helios (underbody) | Multi-camera drive-through, AI | No tread-depth tolerance published. Company CEO claim of detecting **96%** of existing vehicle problems vs. <25% for manual checks. | Vendor claim, not broken down by system, no independent test found | [Repairer Driven News](https://www.repairerdrivennews.com/?p=152963); [The Batch](https://www.deeplearning.ai/the-batch/auto-diagnosis) **[UNVERIFIED: exact article carrying the 96% quote]** |
| **ProovStation + Michelin QuickScan / TireStation** | Drive-over **magnetic** tread sensors + cameras | "Millimeter precision" in under 5 s | Vendor wording, no tolerance or independent data | [Tire Technology International](https://tiretechnologyinternational.com/news/testing-analysis/proovstation-partners-with-michelin-to-provide-automated-tire-and-vehicle-inspection.html); [VehicleServicePros](https://vehicleservicepros.com/service-repair/undercar/news/21292135/michelin-and-proovstation-partner-on-magnetic-tire-scanner) |
| **Hunter Quick Tread** | Drive-over 3D laser point cloud | "Most accurate" (no tolerance). Hunter material is reported to cite handheld plunger gauges varying by about ±2.4 mm depending on operator (vendor claim). **[UNVERIFIED: re-checked 2026-10-21; the cited press release and Hunter's Quick Tread Edge release do not contain the figure; Hunter's site only calls plunger gauges time-consuming and error-prone. Possibly in an image-only Hunter brochure.]** | No published spec found | [Fleet Maintenance](https://www.fleetmaintenance.com/in-the-bay/tools/press-release/12022741/hunter-engineering-company-hunter-announces-quick-tread-drive-over-tread-depth-system) |
| **Zebra Tread Intel** | Handheld swipe scanner | Within **1/32" (0.79 mm)** | Vendor fact sheet | [Zebra fact sheet](https://prod-www.zebra.com/content/dam/zebra_dam/en/fact-sheet/zebra-tread-intel-fact-sheet-en-us.pdf) |
| **QBurst** (commercial CNN case study) | Mobile image, multi-stage CNN | **±1.5 mm on 90%** of test images | Vendor case study; ±1.5 mm ≈ ±2/32", enough to flip a pass/fail at 2/32 or 4/32 | [QBurst PDF](https://www.qburst.com/downloads/tire-inspection-system.pdf) |
| **Open demo** (EfficientNet ensemble, 730 tires) | Single close-up photo | Not validated | Demo only; requires straight-on close-ups | [Hugging Face demo](https://uncodespecial-tire-tread-depth.hf.space/) |

**Takeaways:**
- Even the best purpose-built image system claims about **±0.5 mm (±1/32")** under guided capture, and disclaims real-world correlation. Generic CNN approaches report about ±1.5 mm. Decision thresholds (2/32, 4/32) are only 2/32 apart, so **image-only tread estimates can easily land on the wrong side of a threshold.**
- Drive-over patents note that environmental conditions (rain, snow, ice) affect sensors ([US11421982](https://patents.google.com/patent/US11421982)).
- No independent, peer-reviewed accuracy study of these products was found **[UNVERIFIED gap; re-searched 2026-10-21 — only vendor datasheets, patents and a Goodyear/Taazaa proof of concept with no published error figures]**.
- **Rule for the skill:** Claude may *read* a gauge visible in a photo. It must not *estimate* tread depth, pad thickness, or rotor thickness from appearance. At most it may say "appears near/at the wear bars" or "friction material appears very thin or absent," labeled as visual impression.

---

## 8) Checklist & rubric

### 8.1 Per-photo review checklist [METHOD]

For each photo (or sampled video frame), record:

1. **ID & claim:** Photo # / frame timestamp. Which report line item it supports. What the report claims (condition, value, grade, recommendation).
2. **Image quality:** In focus? Adequately lit? Glare? Resolution enough to read text and scales? Heavily compressed? Rotated? → Usable / Limited / Unusable.
3. **Identification:** Is the component identifiable as the claimed part? Y / Partial / N.
4. **Position:** Is position stated, and is it visually consistent (side, axle, inner/outer)? Y / Unclear / Conflicts.
5. **Vehicle linkage:** Does anything tie it to this vehicle (VIN, odometer, plate, consistent wheels, tires, paint, tire size)? Any conflicts with other photos?
6. **Instrument:** Is a measuring tool or test result present? Correctly applied (probe in main groove, gauge on friction material, strip read against chart, printout CCA rating matches label)? Readable value?
7. **What the photo shows:** Describe in plain observable terms, without interpretation.
8. **Can / cannot:** Using §2, what does this component's photo inherently not establish?
9. **Cross-checks:** C1–C14 (§5): grade, text value, recommendation, coverage, position, pair, threshold, notes, vehicle data, price/part, history, duplicate.
10. **Integrity notes:** Possible duplicate? Crop hides context? Visual oddities? EXIF (if the user extracted it) consistent with the visit?
11. **Evidence-strength score** (rubric below).
12. **Plain-language finding + verification step** for the user.

### 8.2 Evidence-strength rubric

| Score | Definition | Typical examples | What the skill says |
|---|---|---|---|
| **Strong** | Component identifiable; position clear; a correctly applied instrument with legible reading (or an unambiguous visible failure) supports the specific claim and grade; linked to the vehicle. | Tread gauge at 2/32 in LF main groove + context shot; pad gauge at 2 mm on friction material; torn CV boot with slung grease; sidewall bulge; battery printout "Replace" with CCA ~60% of the label rating; belt gauge rocking on video. | "The photo supports this finding." |
| **Partial** | The photo is consistent with the condition but does not establish degree, position, or all items claimed; or the instrument is present but its reading is illegible or the technique is uncertain. | Through-wheel outer-pad photo with no gauge; one tire photographed for four; strut wet but spring seat cropped; reading spoken in video but not shown; refractometer photo without legible scale. | "Consistent with the finding, but it doesn't show [X]. Ask for [Y]." |
| **Weak** | The photo shows the component but the claimed condition is subjective, or color/appearance-based where a valid test exists. | Dirty-looking air or cabin filter; dark brake fluid or ATF color; "cracks" on an EPDM belt; light film on a strut called "leaking"; dry residue called "active leak"; corrosion photo used to condemn a battery. | "This photo alone isn't a reliable basis for the recommendation; [test] would be." |
| **None** | No photo for the item; or the photo does not show the claimed component/condition; or unusable quality. | Item recommended with no image; blurred, dark, or unidentifiable photo; unlit headlamp for "bulb out." | "No photo evidence supports this item." |
| **Contradicts** | Visible content conflicts with the claim, grade, value, or vehicle identity. | Gauge shows 7/32 but text says 2/32; green-looking item graded red; photo shows a different tire size, wheel, or paint; same image used for LF and RF; film above spring seat called a leak requiring replacement under KYB/Monroe criteria. | "The photo appears inconsistent with the claim because [specific visible fact]. This may be a mix-up; ask the shop." |

**Modifiers (append to score):**
- **[ID?]** vehicle linkage missing or questionable
- **[POS?]** position unclear or conflicting
- **[DUP?]** possible duplicate
- **[Q]** image quality limits the conclusion

**Roll-up per line item [METHOD]:** Take the *best* supporting photo's score. But if any photo scores **Contradicts**, the item is flagged Contradicts regardless, pending clarification. Map to the audit's overall verdict (see 07 §1: Supported / Plausible-but-undocumented / Premature / Unsupported / Contradicted):
- Strong → Supported
- Partial → Plausible-but-undocumented
- Weak or None → Unsupported (by photo)
- Contradicts → Contradicted

The technical criteria in 07 can upgrade an item, e.g., an OEM interval reached justifies a fluid service even with Weak photos.

---

## 9) Audit implications — consumer vs. shop owner

### 9.1 Consumer
- **Goal:** Decide what to approve, what to question, and what to verify elsewhere.
- **Output focus:** a plain-language per-item table: what the photo shows, evidence score, and what to ask for. Prioritize safety items with Strong evidence (approve or verify fast) and Weak, None, or Contradicts items (ask before approving).
- **Self-checks a consumer can do:**
  - Tread: coin test, or a $5 gauge. The penny test approximates 2/32 ([Firestone](https://www.firestonecompleteautocare.com/tires/tire-info/buying-considerations/when-do-you-need-new-tires/)).
  - Read the DOT date codes.
  - Compare tire size and brand with their own car.
  - Check the plate or wheels in context shots.
  - Look at their own wipers and lights.
- **Ask the shop for:** measurements with photos showing the gauge; test printouts (battery, strips); a look at the part on the lift; old parts back.
- **Tone:** non-accusatory. Mismatches are framed as "questions to clarify." Encourage a second opinion for expensive or Contradicts items. Never advise the consumer to accuse the shop of fraud (see 09 for dispute steps).
- **Privacy:** Remind users that reverse-image searching uploads the photo to a third party.

### 9.2 Shop owner / service manager
- **Goal:** QA of technician documentation, coaching, and risk reduction (comebacks, complaints, regulatory exposure; see 09).
- **Output focus:**
  - Per-tech documentation quality: share of red/yellow items with Strong evidence; items with no photo; color-only fluid calls; EPDM-crack belt calls; gauge-less pad or tread calls.
  - Integrity flags: duplicate images across ROs, wrong-vehicle photos, position mislabels.
  - Grade-vs-photo inconsistencies.
- **Standards to set:** gauge-in-frame for every quantitative finding; context + close-up; position labels; test strips or refractometer for fluids; belt gauge for belts; dye/UV or cleaned recheck for leaks; printouts for batteries; a VIN or odometer photo on every DVI.
- **Spot-audit method:** Sample N ROs per tech per week. Run the checklist. Look for repeated images across ROs. Track the Contradicts rate as a coaching metric, not a disciplinary verdict.
- **Note:** Vendor guidance pushes high photo counts ([AutoVitals](https://blog.autovitals.com/digital-vehicle-inspection-best-practices)). Quality of evidence matters more than count for trust and compliance.

---

## 10) Open questions

1. **DVI platform image handling:** Do major platforms (AutoVitals, Tekmetric, Shopmonkey, Bolt On, AutoServe1, Mitchell1, etc.) strip EXIF, re-compress, or watermark images with time/VIN? Can shops export originals? **[UNVERIFIED; a 2026-10-21 search found no public help-center statement from these vendors]**
2. **Do any DVI platforms insert canned or reference images** that could be mistaken for vehicle photos? **[UNVERIFIED]**
3. **Monroe ServiceGram full text** (403 on fetch). Confirm exact wording and any note about contamination from other fluids.
4. **Gates/Dayco hose inspection guidance** not retrieved; add.
5. **OEM statements on ATF and coolant color** as non-diagnostic. Only practitioner and vendor sources found.
6. **Independent accuracy studies** of smartphone or drive-over tread scanners. None found; only vendor claims.
7. **MAP UICS current text** on strut seepage, CV boots, and filters as Required vs. Suggested. Not retrieved (see 07).
8. **Claude accuracy on gauge-reading tasks** (tread gauge, pad gauge, micrometer, strip-vs-chart) is not benchmarked. Recommend building an internal test set of labeled DVI images before release.
9. **C2PA adoption** in DVI capture apps. Unknown.
10. **Prevalence data** on mismatched or reused photos in DVIs. None found.
11. **Video frame sampling** guidance is reasoned, not sourced. Validate on real DVI videos.

---

## 11) Sources

**Tires**
- NHTSA interpretation on 2/32" wear indicators — https://www.nhtsa.gov/interpretations/11497awkm
- Ford, tread wear — https://ford.com/support/how-tos/tires-and-wheels/tire-replacement-and-maintenance/why-does-tread-wear-matter
- SlashGear, DOT date codes — https://www.slashgear.com/1419676/numbers-tires-date-code/
- Firestone, date codes — https://www.firestonecompleteautocare.com/tires/tire-info/basics/tire-date-codes/
- Firestone, when to replace / penny test — https://www.firestonecompleteautocare.com/tires/tire-info/buying-considerations/when-do-you-need-new-tires/
- Michelin, sidewall symptoms — https://www.michelin.ca/en/auto/learn/tire-damage/sidewall-problems/symptom-indentation
- Michelin, tire inspector (wear patterns) — https://www.michelinman.com/auto/auto-tips-and-advice/tire-damage/tire-inspector-tool-tire
- Barry's Tire Tech (USTMA service-life statement) — https://barrystiretech.com/tire-aging-and-weather-cracking/
- Jalopnik (Bridgestone cupping) — https://jalopnik.com/2074863/tire-wear-patterns-could-reveal-what-wrong-with-car/
- NAPA Know How, reading tread depth — https://knowhow.napaonline.com/know-how-to-read-tire-tread-depth/

**Brakes**
- Phoenix Systems, pad gauge (vendor) — https://phoenixsystems.co/blogs/company-news-tips/how-do-i-measure-brake-pad-thickness-with-a-gauge
- CarFromJapan, pad thickness — https://carfromjapan.com/article/brake-pad-thickness
- Saab WIS, rotor inspection — https://saabwisonline.com/9-4x/2011/5-brakes/brake-discs-and-pads/fault-diagnosis-fault-symptoms/brake-rotor-surface-and-wear-inspection
- Fras-le via Transport Operator — https://transportoperator.co.uk/?p=30722
- Brake & Front End, rotors/hard spots — https://www.brakeandfrontend.com/?p=39135
- The Drive, brake tampering case — https://www.thedrive.com/news/dealership-techs-caught-tampering-with-customers-brakes-police-say

**Fluids**
- Phoenix Systems, clean-looking brake fluid (vendor) — https://phoenixsystems.co/blogs/company-news-tips/why-that-clean-brake-fluid-might-be-a-silent-problem
- Phoenix Systems, strip limits (vendor) — https://phoenixsystems.co/blogs/company-news-tips/brake-fluid-test-strips-the-quick-check-that-tells-a-bigger-story-about-your-brakes
- Rick's Free Auto Repair Advice, brake fluid color — https://ricksfreeautorepairadvice.com/the-truth-about-brake-fluid-color-and-brake-fluid-condition/
- Ram Forum, ATF color — https://www.ramforum.com/threads/transmission-fluid-dark-before-30k-miles.137306/
- BITOG, ATF color — https://bobistheoilguy.com/forums/threads/why-so-much-attention-toward-atf-color.40838/post-527180 ; https://bobistheoilguy.com/forums/threads/why-so-much-attention-toward-atf-color.40838/post-527175
- Holts/Prestone UK, coolant colors — https://www.holtsauto.com/prestone/why-is-coolant-different-colours/
- BITOG, green vs orange coolant — https://bobistheoilguy.com/forums/threads/green-vs-orange.229893/
- BITOG, coolant hydrometers (Cummins bulletin quote) — https://bobistheoilguy.com/forums/threads/coolant-hydrometers.90700/
- SAE 960645, coolant test strips — https://saemobilus.sae.org/content/960645
- DTIC AD0750569, coolant field measurement — https://apps.dtic.mil/sti/tr/pdf/AD0750569.pdf

**Filters, belts, leaks, suspension, CV, battery, wipers, rust**
- Donaldson engine air filter catalogue — https://ecatalog.donaldson.com/view/477292580/136/
- CCJ, Donaldson service indicators — https://www.ccjdigital.com/business/article/14906155/think-that-air-filters-too-dirty-try-donaldsons-filter-service-indicators
- BITOG, cabin filter interval (manual excerpt) — https://bobistheoilguy.com/forums/threads/cabin-filter-change-interval.324421/
- Gates Tech Tip TT002-15, belt inspection changes — https://www.gates.com/content/dam/documents-library/tech-tips-bulletins/tt002-15.pdf
- CCJ, Gates belt-wear app — https://ccjdigital.com/business/article/14925015/gates-app-measures-serpentine-belt-wear
- EngineerFix, diagnosing oil leaks — https://engineerfix.com/how-to-diagnose-an-engine-oil-leak/
- YourMechanic, finding oil leak source — https://yourmechanic.com/article/how-to-find-the-source-of-an-oil-leak-by-ed-ruelas
- MotoIQ, UV dye — https://motoiq.com/wrench-tips-30-finding-oil-leaks-using-fluorescent-goo/
- Monroe ServiceGram, weepage vs leakage — https://images.oreillyauto.com/parts/img/documents/mon/monroe_servicegram_weepageleakage_v01no05_eng_final.pdf
- KYB Europe, leaking vs sweating (2025) — https://kyb-europe.com/wp-content/uploads/2025/08/Technical-Bulletin-Leaking-vs-Sweating.pdf
- NHTSA-hosted TSB on shock misting — https://static.nhtsa.gov/odi/tsbs/2020/MC-10170656-0001.pdf
- Acurazine forum, CV joint — https://acurazine.com/forums/3g-tl-problems-fixes-114/cv-joint-%5B-913147
- Utah Admin. Code R714-160-10 — https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R714-160-10
- Virginia 19VAC30-70-110 — https://law.lis.virginia.gov/admincode/title19/agency30/chapter70/section110/
- Midtronics, printout clues — https://www.midtronics.com/blog/the-hidden-clues-in-battery-test-printouts-that-techs-might-miss
- Midtronics, healthy battery test — https://www.midtronics.com/blog/key-indicators-of-a-healthy-battery-test/
- GM TechLink, battery testing and warranty replacement (OEM) — https://gm-techlink.com/?p=16086
- Rick's, battery corrosion — https://ricksfreeautorepairadvice.com/does-corrosion-on-car-battery-terminals-mean-the-battery-is-bad/
- ToolSource, battery corrosion — https://www.toolsource.com/blog/battery-terminal-corrosion-safe-cleanup-testing-and-when-to-replace/
- BITOG, wiper blades — https://bobistheoilguy.com/forums/threads/replacement-wiper-blades.208727/latest
- EngineerFix, frame surface rust — https://engineerfix.com/is-surface-rust-on-a-frame-bad/
- ToolSource, Tacoma frame rust — https://www.toolsource.com/blog/how-to-assess-and-repair-severe-frame-rust-on-tacomas-a-technicians-reality-check/
- NI DVA, structural integrity & corrosion — https://www.infrastructure-ni.gov.uk/articles/appendix-structural-integrity-and-corrosion
- DVSA MOT blog, corrosion — https://mattersoftesting.blog.gov.uk/why-its-important-to-check-for-corrosion/

**DVI practice**
- AutoVitals, DVI best practices — https://blog.autovitals.com/digital-vehicle-inspection-best-practices
- AutoServe1, more photos — https://autoserve1.com/founder-protip-photos-improve-digital-vehicle-inspection/
- Tire Review, DVI and trust — https://www.tirereview.com/digital-vehicle-inspection-shop-trust/

**Authenticity, metadata, forensics**
- Fast.io, platforms that strip metadata (vendor) — https://fast.io/resources/social-media-photo-metadata-platforms-strip/
- Google Security Blog, Pixel C2PA (Sept 2025) — https://security.googleblog.com/2025/09/pixel-android-trusted-images-c2pa-content-credentials.html
- FotoForensics, ELA tutorial — https://fotoforensics.com/tutorial.php?tt=ela
- FotoForensics, common mistakes — https://fotoforensics.com/tutorial-mistakes.php
- GIMP forensics wiki, ELA — https://sourceforge.net/p/gimp-forensics/wiki/Error%20Level%20Analysis/
- Bellingcat, reverse image search — https://www.bellingcat.com/resources/2015/05/08/manual-reverse-image-search-with-google-and-tineye/
- Georgetown library, verify images — https://guides.library.georgetown.edu/writ015day/verify
- Data Detox Kit, reverse search — https://datadetoxkit.org/en/misinformation/reversesearch/

**AI / computer vision**
- Anthropic, Claude vision docs — https://platform.claude.com/docs/en/build-with-claude/vision
- arXiv 2602.15950 (grid transcription, preprint) — https://www.arxiv.org/pdf/2602.15950
- Roboflow, Claude vision evaluation — https://blog.roboflow.com/claude-fable-5-for-vision/
- Anyline Tire Tread SDK datasheet — https://anyline.com/?p=25309
- MOTOR, Anyline launch — https://www.motor.com/2022/11/anyline-launches-industry-first-tire-tread-scanner-for-smartphones-at-sema-show/
- Repairer Driven News, UVeye — https://www.repairerdrivennews.com/?p=152963
- The Batch, UVeye — https://www.deeplearning.ai/the-batch/auto-diagnosis
- Tire Technology International, ProovStation/Michelin — https://tiretechnologyinternational.com/news/testing-analysis/proovstation-partners-with-michelin-to-provide-automated-tire-and-vehicle-inspection.html
- VehicleServicePros, ProovStation/Michelin — https://vehicleservicepros.com/service-repair/undercar/news/21292135/michelin-and-proovstation-partner-on-magnetic-tire-scanner
- Fleet Maintenance, Hunter Quick Tread — https://www.fleetmaintenance.com/in-the-bay/tools/press-release/12022741/hunter-engineering-company-hunter-announces-quick-tread-drive-over-tread-depth-system
- Zebra Tread Intel fact sheet — https://prod-www.zebra.com/content/dam/zebra_dam/en/fact-sheet/zebra-tread-intel-fact-sheet-en-us.pdf
- QBurst tire inspection case study — https://www.qburst.com/downloads/tire-inspection-system.pdf
- Hugging Face tread demo — https://uncodespecial-tire-tread-depth.hf.space/
- US11421982, drive-over tread depth patent — https://patents.google.com/patent/US11421982
