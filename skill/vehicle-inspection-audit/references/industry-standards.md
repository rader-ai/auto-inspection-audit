# Industry Standards, Certifications & Shop-Side Inspection QA

As of 2026-10-20. Voluntary (non-statutory) standards only — state law is in `consumer-protection.md` / `state-repair-laws.md`; technical thresholds in `technical-criteria.md`; platform-specific behavior in `dvi-platforms.md`. [UNVERIFIED] = research budget ran out before confirmation. UICS text is copyrighted and largely member-only; only public summaries are paraphrased here.

Source-type tags: **Assoc** = standard/program owner; **Vendor** = DVI/software marketing or help; **Trade** = industry press (some sponsored); **Indep** = survey, academic, government.

## Contents
1. MAP UICS: Required / Suggested codes and how to apply them
2. Partial-service / unsafe rule and other UICS communication rules
3. Certifications and programs: what they do and don't guarantee
4. Trade-association codes of ethics; ISO 17020/9001
5. Generic DVI pitfalls (cross-platform)
6. DVI KPI landscape: selling vs accuracy
7. Conflicts of interest: pay, credence goods, Sears
8. Shop-owner QA program design
9. Audit checks
10. Open questions
11. Sources

---

## 1. MAP UICS: Required / Suggested codes

**What:** Motorist Assurance Program (MAP), run by the Automotive Maintenance and Repair Association (AMRA), publishes the *Uniform Inspection & Communication Standards* (UICS) — industry-written guidance on how to inspect systems and explain findings consistently. Self-reported: started "about 25 years ago," "thousands" of standards, >22,000 participating shops [Assoc: motorist.org]. Sections cover exhaust, brakes, steering/suspension, engine, electrical, HVAC, drivetrain, others.

- Widely associated with the industry response to the 1992 Sears scandal. [UNVERIFIED: founding year (commonly 1994) and causal link to Sears.]
- Oldest public copy: *Exhaust System* guideline, Jan 1999 (shows codes 1–2 only, suggesting 3–4 added later).
- Technical Committee reviews standards before the governing board; intended biannual republication with interim fixes (e.g., brake fluid "corrosion inhibitors depleted" condition added) [Trade].
- Full system tables are member-only; since April 2024 accessible via Today's Class app for AMRA/MAP members [Trade]. [UNVERIFIED: whether a 2025/2026 edition exists.] Public motorist.org pages give no rotor guidance (checked 2026-10-21) [UNVERIFIED: current UICS rotor text]. Brake-fluid 200 ppm copper condition adopted May 2005 [Trade: https://www.fenderbender.com/33022065].

### The codes

| Code | Category | Meaning | Customer choice |
|---|---|---|---|
| **A** | Required | Part no longer performs its intended purpose | Shop needs to repair/replace |
| **B** | Required | Part doesn't meet a design specification (even if it still works) | Shop needs to repair/replace |
| **C** | Required | Part is missing | Shop needs to repair/replace |
| **1** | Suggested | Part close to end of useful life | Always optional |
| **2** | Suggested | Customer need, convenience, or request | Always optional |
| **3** | Suggested | Complies with OEM recommended maintenance | Always optional |
| **4** | Suggested | Technician recommendation based on substantial, informed experience | Always optional |

### How to apply in an audit
- Assign **one code per recommendation**, plus the evidence that code implies:
  - A → evidence of failure (leak, no function, test failure).
  - B → a measurement compared against a named spec.
  - C → photo/note showing absence.
  - 1 → measurement trending toward limit, or age/wear evidence.
  - 3 → the OEM schedule entry for this mileage/severity.
  - 4 → documented basis for the tech's judgment.
- **Red / "needs now" requires A, B, or C.** A red item described only as "worn" or "getting low," with no spec value, should be Suggested (yellow) at most → status **Inconsistent** or **Supported – optional**.
- Suggested items presented as urgent or required = finding.
- Worked examples (1999 exhaust guideline, paraphrased): pipe rusted through and leaking → **A**; corroded but not leaking → **1**; customer wants quieter exhaust on a working system → **2**.
- Software defaults: ALLDATA Manage Online ships MAP reason codes mapped to Red/Amber/Green/**Not-Checked** (example "S1" = near end of life) [Vendor].

## 2. Partial-service / unsafe rule and other UICS communication rules

Paraphrased from public summaries [Assoc: motorist.org; 1999 guideline]:
- **No partial service that leaves an unsafe condition.** If a Required repair exists and doing only part of it would create or continue an unsafe condition, the shop should refuse the partial service. → A shop declining half a Required safety repair is **legitimate, not upselling**. But Optional items must never be made a condition of service.
- **Inspect first:** inspect the system before servicing it, explain results, document on an inspection form.
- **Suggestions need a documented basis** (informed experience or OEM interval); customer may decline any Suggestion.
- **Present the options:** facts and generally accepted repair options, even if the shop won't do the work.
- **MAP Pledge:** written recommendations and estimates; no work without prior authorization; written limited warranty (one summary cites minimum 90 days / 4,000 miles [aa1car]).

## 3. Certifications and programs: what they do and don't guarantee

**Bottom line for audits:** credentials signal training and process commitments. **None re-checks individual inspection findings.** A credential is never evidence that a specific recommendation is correct.

| Program | What it requires | What it does NOT guarantee |
|---|---|---|
| **ASE (individual)** | Pass test per area; ~2 years qualifying experience (some roles count non-hands-on); retest every 5 years. Service consultant = **C1**; collision estimator = **B6** [Assoc] | Knowledge at test time only. Doesn't audit any inspection, repair, recommendation, pricing, or ethics; doesn't certify who worked on your car; no inspection-grading standard (inference from program design [UNVERIFIED explicit disclaimer]) |
| **ASE Blue Seal (shop)** | ≥75% of diagnosis/repair techs ASE-certified; each service area covered by ≥1 certified tech; ≥1 C1 consultant if full-time consultants; annual eligibility review; $235 initial, $65/yr [Assoc] | Staffing-credential threshold, not a workmanship audit |
| **I-CAR Gold Class (collision)** | Role coverage (estimator, refinish, structural, non-structural) at ProLevel 2+; 6 training credits/yr; structural welding recert every 3 yrs; from 2026 renewals, in-house ADAS calibrators need an ADAS tech at ProLevel 1–2 and must progress toward Platinum by 2027 [Assoc] | Training standard, not a per-repair audit |
| **AAA Approved Auto Repair** | ASE (or factory-trained) techs, some clubs every service area; ≥90% customer satisfaction; AAA dispute resolution (shop bound, member not); annual re-inspection + periodic visits (one club: quarterly); written estimates (one club: ≤10% over without authorization); minimum BBB rating, insurance; free member MPI with written recommendations (AAA values at $75); **24 mo/24k mi** warranty (one older page: 12/12) [Assoc, varies by club] | Checks facility and process, not individual findings. "<5% of garages qualify" is from a vendor blog [UNVERIFIED] |
| **NAPA AutoCare** | Peace of Mind warranty 24 mo/24k mi (36/36 with NAPA card), nationwide; says ASE-certified techs [Assoc] | Full center criteria not published [UNVERIFIED] |
| Other banners (TECHNET, Bosch Car Service, Federated) | Not researched [UNVERIFIED] | — |
| **OEM position statements** | I-CAR RTS compiles OEM pre/post-repair scan statements (Audi, BMW, Stellantis, Ford, GM, Honda, Hyundai/Kia, Mazda, Mercedes, Nissan, Subaru, Tesla, Toyota, VW, Volvo, others + ASA/ETI). Triggers: part removal/replacement, damage at sensor mounts | Can legitimately support a scan/calibration line (e.g., after alignment, windshield, suspension on ADAS vehicle). A scan/calibration charge with **no OEM trigger or no report** is a flag. [UNVERIFIED: current statement for any specific make — check live] |

**Consumer levers:** AAA-Approved shops agree to AAA dispute resolution; AAR, NAPA AutoCare and MAP shops carry warranties. Ask whether the shop is a MAP participant and uses MAP codes.

## 4. Trade-association codes; ISO

**ASA 17-point code** [Assoc] — audit-relevant points:
- Itemized invoices identifying used/remanufactured parts
- Replaced parts available for inspection on request
- When recommending, explain which items correct existing problems vs preventive maintenance (mirrors Required/Suggested)
- Estimate before work; prior authorization for all work
- Keep service records ≥1 year
- Fair complaint system; cooperate with mediation
- Does **not** literally say "recommend only necessary work"

**ATRA (transmission):** honest diagnosis; suggest removal only when clearly required; "rebuilt" only if meeting ATRA's rebuilding standard.

**Enforcement:** membership loss is the only sanction found. [UNVERIFIED how often enforced.]

**ISO/IEC 17020** (inspection bodies): competence, impartiality, consistency; Type A (independent third party), B, C (inspection body that also repairs, with safeguards). A shop that inspects and sells the repair is structurally **Type C** — the textbook conflict-of-interest case. Common for government emissions/safety programs and fleet/pre-purchase inspectors; rare for retail shops. [UNVERIFIED: ISO page 403; general knowledge.]
**ISO 9001:** usable QA model (documented procedures, internal audit, corrective action, management review); few independent shops registered [UNVERIFIED].

## 5. Generic DVI pitfalls (cross-platform)

Common flow: tech grades R/Y/G → attaches photos/notes (often canned) → **red and yellow auto-populate as recommended (often pre-priced) jobs** → advisor prices → customer approves/declines per line via link → declines go to follow-up marketing. See `dvi-platforms.md` for per-platform details.

Mechanisms documented by vendor feature descriptions; **prevalence not independently measured:**
1. **Canned jobs/notes** — generic note ("fluid dark, recommend flush") without vehicle-specific evidence; priced job appears just because an item was marked yellow (e.g., Tekmetric canned-job mapping, AutoVitals auto-attached notes) [Vendor].
2. **Templated yellow items** — wipers, cabin filter, fluid services, "monitor" tires, seeping gaskets: low evidentiary burden, feed declined-work marketing. Under UICS they should carry 1–4 and be clearly optional. [UNVERIFIED: no independent data on yellow overuse; analytical inference.]
3. **Default-green / unchecked** — if unmarked points default green, green may mean "not inspected" (Mitchell 1 report [UNVERIFIED]). An explicit "Not Checked" state (ALLDATA) is better practice.
4. **Missing measurements** — photos without gauge/reading; "pad at 3 mm" with no gauge photo; many platforms don't require numeric fields.
5. **Photo–finding mismatch** — photo doesn't show the condition; recycled/stock image; another vehicle (wrong VIN/plate/mileage).
6. **Mis-coded urgency** — wear items labeled red/"safety" without A/B/C evidence.
7. **OEM-schedule inflation** — "manufacturer recommended" not in the OEM schedule for that mileage/severity, or duplicating recent service.
8. **Inspection skipped but claimed** — inspection rate <100%, implausibly short durations.

**Published "good DVI" practices** (vendor-authored, usable as QA criteria):
- Photos sharp, lit, with a reference (hand, tool, gauge) showing the actual concern; capture dash (key on, engine off) and VIN; document green items too [Autoflow].
- Specific measured values, not impressions [Autoflow].
- Plain-language notes: why it matters, consequence if ignored; separate safety / maintenance / monitor [Autoflow].
- Short, narrated video (silent or long = weakness) [Autoflow].
- AutoVitals: ≥10 photos per inspection (anecdotal shops: 21–47) [Vendor].
- Compare recommended jobs per inspection against mileage — older cars should generate more; useful over-recommendation detector [Vendor].
- "Inspect what you expect": track inspections per tech vs turn times; skipped/rushed inspections on busy days are a major problem (Bolt On CEO) [Trade].

## 6. DVI KPI landscape: selling vs accuracy

| KPI | Definition | Measures |
|---|---|---|
| Inspection rate | % of ROs with completed inspection | Coverage |
| Inspection sent rate | % of completed inspections sent to customer | Selling |
| Pictures per inspection/RO | — | Evidence volume (not quality) |
| Recommended jobs per inspection | Tech recommendations ÷ inspections; judge vs mileage | Selling |
| Declined jobs per RO; billed hours per advisor | — | Selling |
| Customer research time | Time customer views DVI (vendor correlates with ARO) | Selling |
| Closing ratio | Approved ÷ presented recommendations | Selling |
| ARO | Average repair order $ | Selling |
| Comeback rate | Common target <3% (some 2% or 1%); 30-day vs 6-month windows vary; NASA 2005 fleet handbook ≤2% | Quality (rework) |

**Closing-ratio "benchmarks" conflict (none from a national survey):** 30–40% nationwide, 65–75% target (consultant 2013); 50–59% average, 60%+ optimal (AutoZone-sponsored); 50% good / 60%+ great (Barrett); higher-ARO shops tend to have lower closing ratios. Vendor ARO-lift claims (e.g., AutoServe1 25%) unverified.

**Key point:** nearly every published DVI KPI measures **selling**. None found measures **accuracy** — false positives, verification failures, customer-reported unnecessary work. That gap is what the QA program (§8) and this skill address.

## 7. Conflicts of interest

- **Pay:** flat-rate tech pay (labor-guide hours per job) is standard; advisor pay often base + commission on parts/labor. Trade sources warn heavy commission pushes unnecessary recommendations; one coaching firm pays incentives only when sales, gross profit **and** CSI targets are all met [Trade].
- **Credence good:** customer can't verify what was needed → incentive to over-treat/over-charge (Dulleck & Kerschbamer 2006) [Indep].
- Beck, Kerschbamer, Qiu & Sutter (2014): professional mechanics reportedly more prone to unnecessary services than controls, partly attributed to professional heuristics, not pay alone [Indep; partially UNVERIFIED — PDF unreadable].
- **No study isolates flat-rate or commission pay as the cause** of unnecessary repairs — plausible but inferential.
- **AAA 2016 survey** (>1,000 drivers, ±3%): 63% distrust repair shops generally; top reasons unnecessary recommendations (76%) and overcharging (73%); 64% have found a shop they trust. No newer AAA survey found [Indep].

**Sears (1992)**
- CA BAR/DCA sought to revoke Sears licenses after undercover runs: unnecessary work sold in 34 of 37 or 38 visits (sources differ). Officials alleged per-shift quotas and commissions drove it. NJ parallel tests: 23 of 38 shops misdiagnosed a disconnected alternator wire or recommended superfluous work.
- Sears dropped auto-service commissions June 1992; settled without admitting wrongdoing (reported up to $46.6M in coupons and 3-year probation for 72 CA centers; another account ~$20M).

**Commission regulation**
- **No US statute banning repair commissions found.** Proposals: Maryland HB 1425 (1997, disclosure; died in committee); Alaska HB 330 (2014, written notice before commissioned dealer service sales; outcome [UNVERIFIED]).
- California B&P §9884.7 (misleading statements etc.) is used against upselling conduct, not pay design.
- **Ontario** requires a posted sign disclosing whether staff are paid commission and on what (CPA 2002 s.60; O. Reg. 17/05 s.50, per government guide) — disclosure, not ban.
- [UNVERIFIED: any US state commission-disclosure rule.]

## 8. Shop-owner QA program design

No authoritative published inspection-audit standard exists for retail shops. This framework synthesizes UICS codes, vendor good-DVI criteria, generic QC (checklists with manager/QC sign-off, documented audits; I-CAR), and ISO 9001-style internal audit. **Recommended framework, not an industry mandate.**

### 8.1 Goals (score both directions)
Measure **accuracy** (no false positives *or* false negatives), **evidence quality**, **communication accuracy** (correct Required/Suggested coding and urgency), and **revenue capture** (true needs not missed). Under-recommending is also a failure (missed safety item, lost legitimate revenue).

### 8.2 Sampling

| Layer | Design |
|---|---|
| Random baseline | ~5–10% of DVIs per tech per week, minimum ~3 per tech; stratify by advisor and vehicle-age band [UNVERIFIED as benchmark — no industry source sets these %] |
| Risk-targeted (on top) | Recommendation $ far above shop median for that mileage band; >X red items on a vehicle <50k mi; red items with no measurement/photo; flushes/services before OEM interval; identical canned notes across many vehicles in a day; very short inspection duration; complaints, declines with pushback, comebacks; estimates over a $ threshold |
| **Blind re-inspection** (gold standard) | Second tech re-inspects *before* seeing the first DVI; compare item by item. ~1–2 vehicles per tech per month, plus every disputed high-ticket item. Planted-condition tests (known-good or known-defect vehicle) mirror BAR undercover method — use ethically, **shop-owned vehicles only** |
| **Calibration sessions** | Monthly: all techs independently grade the same photo/measurement set or car; compute % agreement or Cohen's kappa per item category; discuss disagreements; update shop grading thresholds |

### 8.3 Per-item rubric (9 criteria, 0/1/2)

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | Evidence present | No photo, measurement, or test | Photo or note only, ambiguous | Photo clearly showing condition **plus** measurement/test (gauge in frame, value recorded) |
| 2 | Evidence matches vehicle | Wrong VIN/plate/mileage or stock image | Can't tell | VIN/plate/odometer or other identifier consistent |
| 3 | Spec referenced | None | Generic rule of thumb | OEM/service-information value cited |
| 4 | Classification correct | Red without A/B/C basis, or failed item left green | Right direction, wrong code | Correct A/B/C or 1–4 consistent with evidence |
| 5 | Urgency/safety language | Fear language / overstated | Vague | Accurate consequence and timeframe |
| 6 | Recommendation fits finding | Job doesn't address finding (e.g., flush for non-fluid issue) or bundles unneeded parts | Partly | Minimum correct repair, options disclosed |
| 7 | OEM schedule fidelity | Falsely claims OEM schedule | Uncertain | Matches OEM schedule for mileage/severity, or labeled tech-experience (code 4) |
| 8 | Canned text customized | Generic canned note only | Partially edited | Vehicle-specific observation |
| 9 | Missed items (reverse check) | Re-inspection found unreported Required item | Minor miss | None missed |

**Weighting:** safety-critical categories (brakes, tires, steering/suspension, lighting) **2×**.
**Auto-fail rules:** a **0 on "Classification correct" (#4) or "Evidence matches vehicle" (#2)** = automatic fail for that item **and triggers review of the whole RO**.

### 8.4 Scores and dashboards
- **Inspection QA score** = weighted mean of item scores + completeness (every template point has an explicit status; "not checked" only with a reason) + photo count vs standard + in/out odometer and VIN photo present.
- **Technician dashboard (monthly):** verified-accuracy rate (items upheld ÷ audited); false-positive rate; false-negative/miss rate (blind re-inspections); evidence completeness %; calibration agreement; recommendations per inspection **normalized by mileage band** vs peers; comeback rate.
- **Advisor dashboard:** estimate-to-DVI fidelity (yellow upgraded to "needs now"? items added? urgency changed?); Required vs Suggested labeling on customer estimate; closing ratio **by code** (Required closing low → communication problem; Suggested closing very high in some segments → pressure review); complaints.
- **Outlier logic:** flag tech/advisor whose mileage-normalized recommendation rate or avg recommended $/RO is ~**1.5–2 SD** above peers. A flag is a reason to look, not proof. **High recommendations + high verified accuracy is fine.**

### 8.5 Accuracy-gated incentives
- Tie tech/advisor bonuses to **verified accuracy and comebacks**, not just hours or sales. Pay only when sales, GP and CSI are all met, **plus an audit-accuracy gate**.
- **Never** set per-shift unit quotas for specific services (alleged Sears mechanism).
- Disclose pay structure on request (Ontario requires a sign).

### 8.6 Coaching and corrective action
- Weekly one-on-one review of failed items with photos.
- Monthly calibration session; update shop grading guide.
- Track corrective actions (retraining, template edits, removing auto-added canned jobs from yellow items); re-audit affected tech at a higher sample rate for 30 days.
- Lock/require edits on canned notes for Required items. **Require numeric fields** for measurable items: pad/shoe thickness, rotor thickness vs minimum, tread depth (multiple points), battery test result, fluid test strip/meter readings.

### 8.7 Defense file (retain per RO)
Original DVI as sent (timestamped photos/video, VIN, odometer); tech ID and inspection duration; reason codes, measurements, spec source; customer authorization trail (timestamped approvals/declines, channel); audit results and corrections; replaced parts or photos of them. ASA code: records ≥1 year; state rules may be longer (`state-repair-laws.md`). Keep the audit log itself as evidence of good-faith QA.

---

## 9. Audit checks

### Consumer
1. **Needed now vs optional, and why?** Map each item: needed now = A/B/C (failed, out of spec, missing); optional = 1–4. "Worn"/"getting low" red item with no spec value = classification flag.
2. **Evidence:** photo clearly shows *that* condition on *your* car (VIN, plate, odometer, color consistent)? Measurement + spec on measurable items (brakes, tires, battery)?
3. **Canned language:** identical boilerplate across items, or "recommend flush" with no test result → template-driven.
4. **"Manufacturer recommended":** verify in owner's manual for your mileage/conditions; check history for duplicates → **Beyond OEM schedule** if not.
5. **Partial service:** a shop refusing half of a Required safety repair is legitimate. Optional items must never be a condition of service.
6. **Credentials ≠ correct inspection.** Use them as levers (AAA dispute resolution, AAR/NAPA 24/24 warranties); ask about MAP participation.
7. **Ask for what standards entitle you to:** written estimate first; authorization before added work; old parts back or shown; itemized invoice identifying used/reman parts.
8. **Second opinion** on high-ticket or "urgent" items, without the first shop's DVI framing where practical.
9. **ADAS/scan charges** should cite an OEM procedure trigger and include a report.

### Shop owner
1. **Re-classify every item** with A/B/C and 1–4; report mis-coded urgency both ways (red without A/B/C evidence; failed items left green/yellow).
2. **Score evidence** with the 9-criterion rubric (§8.3); apply auto-fail rules.
3. **Template forensics:** auto-added canned jobs on yellow items; verbatim canned notes; same note across many vehicles; default-green or blank points; implausibly fast inspections.
4. **Estimate–DVI–invoice reconciliation:** every estimate line traces to a finding or customer concern; no urgency escalation between DVI and estimate; invoiced = approved; declined items not billed.
5. **False-negative check:** measurable items not measured; safety categories not inspected — surface legitimately needed work.
6. **Peer normalization** by mileage band; outliers for human review; suggest calibration sets.
7. **Incentive/process risk:** if pay data provided, flag quota-like structures and sales-only bonuses; recommend accuracy-gated incentives.
8. **Defense file:** output per-RO QA record (score, findings, corrective action).

## 10. Open questions
- Current UICS edition/year, system thresholds, exact wording of codes 3–4 (member-only).
- MAP founding year and Sears link unverified.
- No US commission ban found; US disclosure laws not established; Ontario from guide pages, not statute text.
- No independent data on DVI over-recommendation, yellow overuse, or recycled photos; vendor ARO/approval claims unverified.
- Benchmarks (closing ratio, photos, comebacks) have inconsistent definitions — rough ranges only.
- RO Writer not researched; Mitchell 1 default-green unconfirmed; numeric-field enforcement in Shopmonkey/Shop-Ware unknown.
- AAA AAR warranty (12/12 vs 24/24) and visit frequency vary by club; "<5% qualify" from vendor blog.
- NAPA and other network criteria unpublished.
- ISO 17020/9001 from general knowledge; prevalence unknown.
- Beck et al. (2014) from search excerpt only.

## 11. Sources
**Association / standards**
- MAP: https://motorist.org/who-we-are/ ; https://motorist.org/top-quality-assurance-standards-for-auto-repair-shops/ ; https://motorist.org/vehicle-systems/
- MAP Exhaust UICS 1999 (third-party copy): https://pdf4pro.com/view/exhaust-system-uniform-inspection-5bb86.html
- [aa1car] AA1Car on MAP: https://www.aa1car.com/library/trtu196.htm
- ASE: https://ase.com/?p=2860 ; https://ase.com/about/certification-pathway/ ; https://ase.com/tests/c1/ ; https://ase.com/tests/b6/
- I-CAR: https://info.i-car.com/gold-class/achieving ; https://rts.i-car.com/crn-581.html ; https://rts.i-car.com/crn-720.html ; https://rts.i-car.com/crn-13.html
- AAA: https://www.acg.aaa.com/knowledge-center/approved-auto-repair-faqs ; https://www.hoosier.aaa.com/automotive/auto-repair-shop-standards ; https://northdakota.aaa.com/automotive/approved_auto_repair.aspx ; survey: https://newsroom.aaa.com/2016/12/u-s-drivers-leery-auto-repair-shops/
- NAPA AutoCare: https://www.napaonline.com/en/auto-care
- ASA Code: https://www.asashop.org/?p=55405 ; ATRA Code: https://members.atra.com/code-of-ethics
- ISO/IEC 17020: https://www.iso.org/standard/52994.html

**Government / legal**
- Ontario: https://www.ontario.ca/page/guide-auto-repair-businesses ; https://forms.mgcs.gov.on.ca/dataset/on00012
- Maryland HB 1425: https://mgaleg.maryland.gov/1997rs/billfile/hb1425.htm ; Alaska HB 330: https://www.akleg.gov/pdf/28/Bills/HB0330A.pdf
- CA BAR accusation (§9884.7): https://www.bar.ca.gov/pdf/accusations/ard243784_2013_05_24_acc.PDF
- NASA fleet handbook: https://nodis3.gsfc.nasa.gov/npg_img/textview/243qualityofrepairs.htm

**Sears**
- https://www.upi.com/Archives/1992/06/16/Sears-hits-back-at-California-probe/4031708667200/ ; https://www.tampabay.com/archive/1992/06/12/sears-accused-of-auto-repair-fraud/ ; https://www.moderntiredealer.com/articles/33372-what-happened-to-sears-auto-centers ; https://legalclarity.org/sears-auto-center-fraud-charges-investigation-and-settlement/

**Academic**
- Dulleck & Kerschbamer: https://www.uibk.ac.at/economics/bbl/cv_papiere/12-dulleck-and-kerschbamer-jel-2006-on-doctors-mechanics-and-computer-specialists.pdf
- Beck et al.: https://www2.uibk.ac.at/downloads/c4041030/wpaper/2014-02.pdf

**Trade press**
- https://www.autoserviceworld.com/?p=267977 ; https://www.brakeandfrontend.com/map-standards-updated-for-brake-systems/ ; https://www.vehicleservicepros.com/industry-news/news/55021554/automotive-maintenance-and-repair-association-amra-amra-map-program-integrates-with-todays-class-app
- https://www.ratchetandwrench.com/articles/9249-ensure-digital-inspections-happen
- Closing ratios: https://www.ratchetandwrench.com/running-a-shop/article/11490381/improving-shop-closing-ratios-october-01-2013 ; https://ratchetandwrench.com/sponsored-content/autozone/article/33010675/the-kpi-closing-ratio ; https://www.ratchetandwrench.com/running-a-shop/article/11483528/six-steps-for-a-better-closing-ratio-2017-03-01 ; https://www.ratchetandwrench.com/articles/10495-bottleneck-disproportionate-closing-ratio
- Pay: https://www.vehicleservicepros.com/shop-operations/service-repair/article/21195702/service-advisor-pay-program-tips-that-work ; https://www.autoshopowner.com/blogs/entry/257-service-advisor-pay-programs-that-work/ ; https://www.repairerdrivennews.com/?p=33815
- Podcast: https://autofixadvisorcast.transistor.fm/7/transcript

**Vendor (non-independent)**
- AutoVitals: https://blog.autovitals.com/auto-repair-shop-metrics ; https://blog.autovitals.com/key-performance-indicators-to-transform-your-shop-operations ; https://blog.autovitals.com/why-shops-choose-digital-vehicle-inspections ; https://help.autovitals.com/low-aro
- Tekmetric: https://www.tekmetric.com/feature/digital-vehicle-inspection
- ALLDATA: https://www.alldata.com/manage-online-article/code-settings-inspection-reason-codes
- [Autoflow]: https://autoflow.com/training/best-practices/how-to-perform-a-good-digital-vehicle-inspection-dvi/
- AutoServe1: https://autoserve1.com/why-youre-losing-service-sales/
- AutoSmarts QC: https://autosmarts.co/en/understanding-auto-body-repair-quality-control/
- Oxmaint comebacks: https://oxmaint.com/industries/fleet-management/technician-comeback-tracking-kpi
- iDriveCertified: https://idrivecertified.com/blog/certified-automotive-repair-shop-how-to-choose-the-best
- Mitchell 1: https://www.ratchetandwrench.com/site-placement/latest-news/news/55315119/mitchell-1-releases-multi-point-inspection-tool-for-manager-se-shop-management-system ; https://www.aftermarketnews.com/mitchell-1-inspection-tool-launch/
