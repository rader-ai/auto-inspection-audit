# 08 — Voluntary Industry Standards, Certifications, and Shop-Side Inspection QA

## 1) Scope & as-of date

- **As of:** 2026-10-20. Research done by web search and fetch in a single session. The session's web-search budget ran out before every thread was finished; gaps are marked **[UNVERIFIED]** and listed in Section 7.
- **Scope:** voluntary (non-statutory) standards that shape how inspections are supposed to be done and communicated. Covers:
  - the AMRA/MAP Uniform Inspection & Communication Standards (UICS)
  - certifications and programs: ASE, I-CAR, AAA, NAPA AutoCare, OEM position statements
  - digital vehicle inspection (DVI) platform practices and pitfalls
  - shop KPIs and incentive conflicts
  - designing an inspection QA/audit program
  - trade-association codes of ethics
  - ISO 17020 / ISO 9001 (brief)
- **Not covered here:** state statutes and regulation, covered in `09-consumer-protection-dvi-law.md`, and technical pass/fail thresholds, covered in `07-technical-inspection-criteria.md`.
- **How sources are labeled:** each claim is tagged as one of the following.
  - **Vendor:** marketing or help content from a DVI or software vendor.
  - **Trade press:** sponsored or editorial articles from industry publications.
  - **Association/standards body:** published by the organization that owns the standard or program.
  - **Independent:** surveys, academic research, government.
- **Copyright:** the UICS text is copyrighted and largely member-only. This file paraphrases only publicly visible summaries and does not reproduce the standards.

---

## 2) Standards & certifications

### 2.1 AMRA / Motorist Assurance Program (MAP) — UICS

**What it is**
- MAP is run by the Automotive Maintenance and Repair Association (AMRA). It publishes the *Uniform Inspection & Communication Standards* (UICS): industry-written guidance on how to inspect vehicle systems and how to explain findings to motorists consistently. (Association: https://motorist.org/who-we-are/)
- MAP's site says the program was started "about 25 years ago" by a cross-section of the industry. It claims "thousands" of standards and more than 22,000 participating shops. These are self-reported figures. (https://motorist.org/who-we-are/)

**History**
- MAP is widely associated with the industry's response to the 1992 Sears Auto Center scandal (see 4.3).
- **[UNVERIFIED]:** the exact founding year (commonly given as 1994) and a documented causal link to Sears. No primary source confirming either was retrieved.
- The oldest public UICS copy found is the *Exhaust System* guideline dated January 1999. (Third-party copy: https://pdf4pro.com/view/exhaust-system-uniform-inspection-5bb86.html)
- UICS sections cover exhaust, brakes, steering/suspension, engine, electrical, HVAC, drivetrain and other systems. (Trade press: https://www.autoserviceworld.com/?p=267977)

**Classification scheme (publicly summarized on motorist.org)**
- **Required** (letter codes): the shop needs to replace or repair the part.
  - **A:** the part no longer performs its intended purpose.
  - **B:** the part does not meet a design specification, regardless of whether it still performs.
  - **C:** the part is missing.
- **Suggested** (number codes): always optional for the customer.
  - **1:** the part is close to the end of its useful life.
  - **2:** addresses a customer need, convenience, or request.
  - **3:** complies with the OEM's recommended maintenance.
  - **4:** the technician's recommendation, based on substantial, informed experience.
- Source: https://motorist.org/who-we-are/. The 1999 exhaust guideline shows codes 1–2 only, which suggests codes 3–4 were added later. (https://pdf4pro.com/view/exhaust-system-uniform-inspection-5bb86.html)
- Shop software uses these codes as defaults. ALLDATA Manage Online ships with MAP reason codes, and each code maps to a Red / Amber / Green / Not-Checked status. Its example is "S1", meaning a part near the end of its useful life. (Vendor: https://www.alldata.com/manage-online-article/code-settings-inspection-reason-codes)

**Communication rules (paraphrased from public summaries)**
- *No partial service that leaves an unsafe condition.* If a Required repair exists and doing only part of the job would create or continue an unsafe condition, the shop should refuse the partial service. (https://motorist.org/who-we-are/; https://pdf4pro.com/view/exhaust-system-uniform-inspection-5bb86.html)
- *Inspect first.* Inspect the relevant system before servicing it, explain the results, and document them on an inspection form. (1999 guideline, as above)
- *Suggestions need a documented basis.* A Suggestion must rest on substantial, informed experience or on the manufacturer's interval, and the basis should be documented. The customer may decline any Suggestion. (1999 guideline)
- *Present the options.* Give the customer the facts and the generally accepted repair options, even when the shop won't do the work itself. (1999 guideline)
- *MAP Pledge to customers.* Written recommendations and estimates; no work without prior authorization; a written limited warranty. One summary cites a minimum warranty of 90 days / 4,000 miles. (https://motorist.org/who-we-are/; https://www.aa1car.com/library/trtu196.htm)

**Worked examples from the 1999 exhaust guideline (paraphrased)**
- A pipe that is rusted through and leaking exhaust is Required, code A.
- A pipe that is corroded but not leaking is Suggested, code 1.
- A customer who wants a quieter exhaust while the system still works is Suggested, code 2.
- These map cleanly onto audit logic: a "red" finding with no failure or spec evidence should probably be "yellow" at most.

**Maintenance and access**
- Standards are reviewed by the AMRA/MAP Technical Committee before going to the governing board. (https://www.autoserviceworld.com/?p=267977)
- One MAP notice said the standards are meant to be republished biannually, with interim fixes in between. One example fix added a "corrosion inhibitors depleted" condition to brake fluid. (Trade press, via search excerpt: https://www.brakeandfrontend.com/map-standards-updated-for-brake-systems/)
- **Member-only:** the full system-by-system standard tables (conditions, codes, procedures).
  - In April 2024 AMRA/MAP integrated UICS access into the Today's Class training app for users who are also AMRA/MAP members. (Trade press: https://www.vehicleservicepros.com/industry-news/news/55021554/automotive-maintenance-and-repair-association-amra-amra-map-program-integrates-with-todays-class-app)
  - Public material is limited to the reason codes, the Pledge, consumer videos, and older third-party copies.
  - Checked 2026-10-21: the public motorist.org home and Vehicle Systems pages give no brake-rotor guidance (video topics cover oil, tires, A/C, steering, suspension). Current UICS rotor text remains **[UNVERIFIED]**. (https://motorist.org/vehicle-systems/)
  - The 200 ppm copper brake-fluid condition was adopted by MAP in May 2005, per trade press. (Trade press: https://www.fenderbender.com/33022065)
- **[UNVERIFIED]:** whether a 2025/2026 UICS edition exists. None was found.

**Why it matters for the skill:** UICS is the only widely adopted, industry-authored taxonomy that separates "needs it" (failure, out of spec, missing) from "might want it" (wear, convenience, OEM schedule, technician experience). An audit can require every recommendation to carry one reason code plus the evidence that code implies.

### 2.2 ASE (National Institute for Automotive Service Excellence)

**What individual certification requires**
- Passing a test in each area.
- About 2 years of qualifying work experience. Some roles, such as parts and service consultant, count non-hands-on experience.
- Recertification by retest every 5 years.
- Sources: https://ase.com/about/certification-pathway/; https://ase.com/tests/c1/
- Service consultants have their own credential, **C1**. Collision estimators have **B6**. (https://ase.com/tests/c1/; https://ase.com/tests/b6/)

**What ASE does not guarantee**
- ASE certifies individuals' knowledge at test time. It does not audit any particular inspection, repair, recommendation, pricing, or shop ethics.
- It does not certify that a given technician did your car, and it has no inspection-grading standard.
- This is our inference from ASE's program design (tests plus experience). **[UNVERIFIED]:** whether ASE publishes an explicit disclaimer to this effect.

**Blue Seal of Excellence (business-level recognition)**
- At least 75% of technicians doing diagnosis and repair must be ASE-certified.
- Each service area offered must be covered by at least one certified technician.
- Shops with full-time service consultants need at least one C1-certified consultant.
- ASE reviews eligibility annually. Fees: $235 initial, $65 annual renewal.
- Source: https://ase.com/?p=2860
- Blue Seal is a staffing-credential threshold, not a workmanship audit.

### 2.3 I-CAR (collision)

- **Gold Class** requires role coverage for estimator, refinish, structural, and non-structural technicians, at ProLevel 2 or higher.
- Annual renewal requires 6 training credits.
- Structural welding certification is renewed every 3 years.
- From 2026 renewals, shops that calibrate ADAS in-house must have an ADAS technician who has completed ProLevel 1–2, and must progress toward Platinum by 2027.
- Source: https://info.i-car.com/gold-class/achieving
- Gold Class is a training standard, not a per-repair audit.

### 2.4 OEM position statements (brief)

- I-CAR's Repairability Technical Support (RTS) portal keeps a compiled list of OEM pre- and post-repair scanning position statements. The list includes Audi, BMW, FCA/Stellantis, Ford, GM, Honda/Acura, Hyundai/Genesis/Kia, Mazda, Mercedes, Nissan, Subaru, Tesla, Toyota/Lexus, VW, Volvo, and others, plus the ASA and ETI positions. (https://rts.i-car.com/crn-581.html; https://rts.i-car.com/crn-720.html)
- I-CAR's role descriptions tie pre-repair scans, post-repair scans, and calibrations to OEM procedures. Triggers include part removal or replacement and damage to sensor mounting locations. (https://info.i-car.com/gold-class/achieving)
- **Audit relevance:**
  - On mechanical jobs, an OEM statement can legitimately support a scan or calibration line item, for example a calibration after an alignment, windshield replacement, or suspension work on an ADAS-equipped vehicle.
  - Conversely, a scan or calibration charge with no OEM-procedure trigger, or with no report attached, is a flag.
  - **[UNVERIFIED]:** the current OEM statement for any specific make. Statements are revised over time, so check the live statement.

### 2.5 AAA Approved Auto Repair (AAR)

**Commonly published requirements** (sources vary by club and date):
- ASE-certified technicians. Some clubs require ASE or factory-trained technicians in every service area, plus ongoing training.
- A customer-satisfaction rating of at least 90% from surveys of recent customers.
- AAA dispute resolution. The shop agrees to accept AAA's decision; the member is not bound by it.
- Annual re-inspection plus periodic staff visits. One club says quarterly visits.
- Written estimates. One club caps work at 10% over the estimate without prior authorization.
- A minimum BBB rating, and insurance.
- A free multi-point inspection for members with written recommendations, valued by AAA at $75.
- A **24-month / 24,000-mile** warranty on parts and labor. One older club page says 12/12.
- Sources: AAA club pages https://www.acg.aaa.com/knowledge-center/approved-auto-repair-faqs (flagged stale by the site); https://www.hoosier.aaa.com/automotive/auto-repair-shop-standards; https://northdakota.aaa.com/automotive/approved_auto_repair.aspx

**Caveats**
- A claim that fewer than 5% of garages qualify comes from a vendor blog and is **[UNVERIFIED]**. (https://idrivecertified.com/blog/certified-automotive-repair-shop-how-to-choose-the-best)
- AAR is the closest thing to an external audit of a shop, but it checks facility and process. It does not re-check individual inspection findings.

### 2.6 NAPA AutoCare and similar networks

- NAPA AutoCare: the Peace of Mind warranty is 24 months / 24,000 miles on qualifying repairs (36/36 with the NAPA credit card), honored nationwide. NAPA says centers employ ASE-certified technicians. (https://www.napaonline.com/en/auto-care)
- **[UNVERIFIED]:** NAPA's full center-certification criteria. No published checklist was found.
- Other networks have similar banner programs: Carquest/Worldpac TECHNET, Bosch Car Service, Federated Car Care, and others. Their inspection-quality standards were not researched. **[UNVERIFIED]**

### 2.7 Trade-association codes of ethics

**ASA (Automotive Service Association)** — a 17-point code. Points relevant to auditing:
- Itemized invoices that identify used or remanufactured parts.
- Replaced parts available for inspection on request.
- When recommending work, explain which items correct existing problems and which are preventive maintenance. This mirrors the Required/Suggested split.
- A price estimate before work, and prior authorization for all work.
- Keep service records for at least one year.
- Maintain a fair complaint system and cooperate with mediation.
- Source: https://www.asashop.org/?p=55405
- The code does not literally say "recommend only necessary work."

**ATRA (transmission)**
- Honest diagnosis. Transmission removal should be suggested only when clearly required.
- A shop may call a unit "rebuilt" only if it meets ATRA's rebuilding standard.
- Source: https://members.atra.com/code-of-ethics

**Enforcement:** these codes are membership conditions. Membership loss is the only sanction found. **[UNVERIFIED]:** how often any association enforces its code.

### 2.8 ISO/IEC 17020 and ISO 9001 (brief)

- **ISO/IEC 17020** specifies competence, impartiality, and consistency requirements for *inspection bodies*. It distinguishes Type A (independent third party), Type B, and Type C (an inspection body that may also do design, repair, or other work, with safeguards required).
  - A repair shop that inspects and also sells the repairs is structurally a "Type C" situation. That is the textbook conflict-of-interest case the standard asks organizations to mitigate.
  - Accreditation to 17020 is common for government emissions/safety inspection programs and fleet or pre-purchase inspectors, and rare for retail repair shops.
  - **[UNVERIFIED in session]:** the ISO page (https://www.iso.org/standard/52994.html) returned HTTP 403. This description is from general knowledge.
- **ISO 9001** (quality management) offers a usable model for a shop QA program: documented procedures, internal audits, corrective action, and management review. Very few independent shops are registered. **[UNVERIFIED]:** prevalence.

---

## 3) DVI practices & pitfalls

### 3.1 Platforms and typical features

| Platform | Publicly documented features (source type) |
|---|---|
| **AutoVitals** | Guided tech workflow. Canned notes auto-attach to each condition along with photos and educational content. KPI dashboards (inspection rate, sent rate, pictures per RO, recommended jobs per inspection, customer "research time"). Declined-job follow-up. (Vendor: https://blog.autovitals.com/why-shops-choose-digital-vehicle-inspections; https://blog.autovitals.com/auto-repair-shop-metrics; https://help.autovitals.com/?p=21586) |
| **Bolt On Technology (NextGear)** | Red/yellow/green health reports with photos and video. Two-way texting for approvals. Integrates with Tekmetric, Protractor, and others. (Trade press/vendor PR: https://www.vehicleservicepros.com/industry-news/service-repair/press-release/21231788/...; https://www.aftermarketnews.com/bolt-on-technology-now-integrates-with-protractor-shop-management-platform/) |
| **Tekmetric** | Color-coded severity. Photo and video markup. Red/yellow items flow into "Technician Concerns." **Canned jobs can be mapped to inspection tasks and auto-added to the RO.** Declined items saved for follow-up. Shared by email or text. (Vendor: https://www.tekmetric.com/feature/digital-vehicle-inspection; https://tours.tekmetric.com/answers/performing-an-inspection-tekmetric) |
| **Shopmonkey** | Multiple templates (check-in, multipoint, pre-purchase). Status, notes, and photos/video per item. Inspection lives inside the RO and flows to the estimate. (Vendor: https://www.shopmonkey.io/product/inspections; https://help.shopmonkey.io/en/articles/8887793-inspections-in-shopmonkey-for-techs-mobile-app) |
| **Mitchell 1 Manager SE Inspections** (launched Sept 2025) | Phone/tablet capture of photos, video, and notes. Advisor alert when an inspection is marked "inspected." Items convert to job containers. Reusable templates. Branded customer report with approve/decline portal. Deferred work saved. (Trade press: https://www.ratchetandwrench.com/site-placement/latest-news/news/55315119/...) One summary says unmarked points default to green; the R+W article does not confirm this. **[UNVERIFIED]** (https://www.aftermarketnews.com/mitchell-1-inspection-tool-launch/) |
| **Shop-Ware** | Native DVI with photos, video, and notes shared in real time. Inspections built in its "Cannery." Canned jobs by vehicle type. (Vendor: https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/; https://shop-ware.com/questions/) |
| **RO Writer** | Not researched. **[UNVERIFIED]** |
| **ALLDATA Manage Online** | Ships MAP reason codes as defaults, mapped to RAG status. (Vendor: https://www.alldata.com/manage-online-article/code-settings-inspection-reason-codes) |
| **ServiceProfessional** (example) | Items that pass or fail automatically from entered measurements, and canned services linked to inspection items. (Vendor: https://serviceprofessional.support.site/article/whats-new) |

**Common pattern across platforms:**
1. The tech grades items red, yellow, or green.
2. The tech attaches photos or video and notes, optionally from canned text.
3. Red and yellow items auto-populate as recommended jobs, often with pre-priced canned jobs.
4. The advisor reviews and prices.
5. The customer gets a link and approves or declines line by line.
6. Declined items go into follow-up marketing.

### 3.2 Published "good DVI" practices

These are vendor-authored, but they make reasonable QA criteria.
- **Photos:** sharp and well lit, with a reference (hand, tool, gauge) that shows the actual concern. Capture the dashboard (key on, engine off) and the VIN. Document green items too, not just problems. (https://autoflow.com/training/best-practices/how-to-perform-a-good-digital-vehicle-inspection-dvi/)
- **Measurements:** give specific values rather than impressions. (Same source; it gives no thresholds.)
- **Notes and priority:** plain language. Explain why each item matters and what happens if it is ignored. Keep safety, maintenance, and monitor items separate. (Same source)
- **Video:** short and narrated. Silent or long videos are listed as weaknesses. (Same source)
- **Photo volume:** AutoVitals recommends at least **10 pictures per inspection**. (Vendor: https://blog.autovitals.com/auto-repair-shop-metrics) Anecdotal shops report 21 to 47 photos per visit. (Vendor radio/testimonial, via search excerpts)
- **Recommendations vs. mileage:** AutoVitals advises comparing recommended jobs per inspection against vehicle mileage, since older, higher-mileage cars should generate more. This is useful as an over-recommendation detector. (https://blog.autovitals.com/auto-repair-shop-metrics)
- **Inspect every car:** Bolt On's CEO calls skipped or rushed inspections on busy days a major "human behavior" problem. He recommends "inspect what you expect": track inspections per technician against turn times. (Trade press: https://www.ratchetandwrench.com/articles/9249-ensure-digital-inspections-happen)

### 3.3 Known or likely pitfalls (what an audit should look for)

The mechanisms below are documented through vendor feature descriptions. Their prevalence is **not** independently measured.
1. **Canned jobs and canned notes.**
   - Tekmetric maps canned jobs to inspection tasks so they are auto-added. AutoVitals auto-attaches canned explanatory notes.
   - Risk: a generic note ("fluid dark, recommend flush") gets selected without vehicle-specific evidence, and a pre-priced job appears just because an item was marked yellow. (Vendor: https://www.tekmetric.com/feature/digital-vehicle-inspection; https://blog.autovitals.com/why-shops-choose-digital-vehicle-inspections)
2. **Templated "yellow" items.**
   - Yellow (future attention) items such as wipers, cabin filter, fluid services, "monitor" tires, and seeping gaskets carry low evidentiary burden and feed declined-work marketing.
   - Under UICS they should carry code 1–4 and be clearly optional.
   - **[UNVERIFIED]:** no independent data on how often yellow is overused. Searches found no trade-press critique naming "everything yellow." This is an analytical inference.
3. **Default-green or unchecked items.** If a platform defaults unmarked points to green, a "green" may mean "not inspected." (Mitchell 1 report, **[UNVERIFIED]**.) ALLDATA's RAG scheme has an explicit "Not Checked" state, which is the better practice.
4. **Missing measurements.** Photos without a gauge or reading, and a pad "at 3 mm" with no photo of the gauge. Vendor guidance asks for specific measurements, but many platforms do not require numeric fields.
5. **Photo–finding mismatch.** A photo that does not show the cited condition, a recycled or stock image, or a photo from another vehicle (wrong VIN, plate, or mileage visible). A trade podcast stresses verifying in/out mileage and photos. (https://autofixadvisorcast.transistor.fm/7/transcript)
6. **Mis-coded urgency.** Wear items labeled red or "safety" with no failure or out-of-spec evidence. Under UICS, Required needs A, B, or C.
7. **OEM-schedule inflation.** Services labeled "manufacturer recommended" that are not in the OEM schedule for that mileage or severity, or that duplicate recent service. Cross-check against `07-technical-inspection-criteria.md`.
8. **Inspection skipped but billed or claimed.** Inspection rate below 100%, or inspections completed in implausibly short times.

---

## 4) KPIs & conflicts of interest

### 4.1 Inspection-related KPIs (definitions)

From AutoVitals (vendor) and trade press:
- **Inspection rate:** % of ROs with a completed inspection.
- **Inspection sent rate:** % of completed inspections sent to the customer. A shop coach warned about shops that inspect but rarely send. (Vendor: https://blog.autovitals.com/key-performance-indicators-to-transform-your-shop-operations; https://help.autovitals.com/low-aro)
- **Pictures per inspection / per RO.** (Vendor: https://blog.autovitals.com/auto-repair-shop-metrics)
- **Recommended jobs per inspection:** tech-selected recommendations ÷ inspections. Judge it relative to mileage. (Same source)
- **Declined jobs per RO**, and **billed hours sold per advisor**. (Same source)
- **Customer research time:** how long the customer views the DVI. The vendor links it to higher ARO; that is a correlation the vendor itself reports.
- **Closing ratio:** approved recommendations ÷ presented. Published "benchmarks" conflict:
  - Nationwide 30–40%, with 65–75% as a target for good salespeople. (Consultant, 2013: https://www.ratchetandwrench.com/running-a-shop/article/11490381/improving-shop-closing-ratios-october-01-2013)
  - Industry average 50–59%, optimal 60%+. (AutoZone-sponsored: https://ratchetandwrench.com/sponsored-content/autozone/article/33010675/the-kpi-closing-ratio)
  - Good advisors 50%, great advisors 60%+. (Barry Barrett: https://www.ratchetandwrench.com/running-a-shop/article/11483528/six-steps-for-a-better-closing-ratio-2017-03-01)
  - Shops with higher ARO tend to have lower closing ratios. (https://www.ratchetandwrench.com/articles/10495-bottleneck-disproportionate-closing-ratio)
  - **None of these come from a national survey.**
- **ARO (average repair order):** the topline revenue metric. Vendor claims of DVI-driven ARO lifts are unverified. One example is AutoServe1's 25% claim. (Vendor: https://autoserve1.com/why-youre-losing-service-sales/)
- **Comeback rate:** a common target is under 3%, with some setting 2% or 1%. Definitions vary (30-day vs. 6-month window). Sources are fleet and trade blogs, plus a 2005 NASA fleet handbook citing 2% or less. (https://oxmaint.com/industries/fleet-management/technician-comeback-tracking-kpi; https://nodis3.gsfc.nasa.gov/npg_img/textview/243qualityofrepairs.htm)

**Key point:** almost every published DVI KPI measures *selling* (volume, photos, approvals, ARO). None of the public KPI sets found measures *accuracy*: false-positive recommendations, verification failures, or customer-reported unnecessary work. That is the gap this skill fills.

### 4.2 Pay structures and incentives

**How pay is structured**
- Flat-rate technician pay is standard: techs are paid labor-guide hours per job, not clock hours. (Credence-goods literature summary and trade discussion: https://www.repairerdrivennews.com/?p=33815)
- Advisor pay commonly mixes a base with commission on parts and/or labor. Trade sources warn that heavy commission can push unnecessary recommendations. One coaching firm recommends paying incentives only when sales, gross profit, **and** customer-satisfaction targets are all met. (Trade press: https://www.vehicleservicepros.com/shop-operations/service-repair/article/21195702/service-advisor-pay-program-tips-that-work; https://www.autoshopowner.com/blogs/entry/257-service-advisor-pay-programs-that-work/)

**Independent evidence**
- Auto repair is a classic **credence good**: the customer cannot verify what was needed, which creates incentives to over-treat and over-charge. (Academic: https://www.uibk.ac.at/economics/bbl/cv_papiere/12-dulleck-and-kerschbamer-jel-2006-on-doctors-mechanics-and-computer-specialists.pdf)
- A field/lab experiment with professional mechanics (Beck, Kerschbamer, Qiu & Sutter, 2014) reportedly found mechanics significantly more prone to supply unnecessary services than control subjects. The authors attribute this partly to professional heuristics rather than pay alone. (Academic, via search excerpt: https://www2.uibk.ac.at/downloads/c4041030/wpaper/2014-02.pdf — PDF text not machine-readable in session, **partially [UNVERIFIED]**)
- **No study was found that isolates flat-rate or commission pay as the cause** of unnecessary auto repairs. The link is plausible but inferential.
- A 2016 AAA telephone survey (more than 1,000 drivers, ±3%) found:
  - about two-thirds (63%) distrust repair shops in general;
  - the top reasons were recommendations for unnecessary services (76%) and overcharging (73%);
  - 64% have found a shop they trust.
  - Source: https://newsroom.aaa.com/2016/12/u-s-drivers-leery-auto-repair-shops/
  - No newer AAA survey was found.

### 4.3 The Sears case (1992) and regulation of commissions

**The case**
- California's Bureau of Automotive Repair / Department of Consumer Affairs sought to revoke Sears' auto repair licenses after undercover runs. Investigators were reportedly sold unnecessary work in 34 of 37 or 38 visits; sources differ on the denominator. (https://www.upi.com/Archives/1992/06/16/Sears-hits-back-at-California-probe/4031708667200/)
- Officials alleged that per-shift sales quotas and commission structures drove the conduct. (Tampa Bay Times archive, via search excerpt: https://www.tampabay.com/archive/1992/06/12/sears-accused-of-auto-repair-fraud/)
- New Jersey ran parallel tests: 23 of 38 shops misdiagnosed a disconnected alternator wire or recommended superfluous work. (UPI, above)
- Sears' chairman announced it was discontinuing commissions for auto service employees in June 1992. (https://www.moderntiredealer.com/articles/33372-what-happened-to-sears-auto-centers)
- Sears settled without admitting wrongdoing. Reported figures include up to $46.6M in coupons and 3-year probation for its 72 California centers; another account says about $20M was paid. (https://legalclarity.org/sears-auto-center-fraud-charges-investigation-and-settlement/)

**Do states ban commissions?**
- **No US statute banning repair commissions was found.** Proposals surfaced instead:
  - Maryland HB 1425 (1997) would have required disclosure of commissions; it died in committee. (https://mgaleg.maryland.gov/1997rs/billfile/hb1425.htm)
  - Alaska HB 330 (2014) would have required a written notice before commissioned dealer service sales; its outcome is **[UNVERIFIED]**. (https://www.akleg.gov/pdf/28/Bills/HB0330A.pdf)
- California's general disciplinary statute (B&P §9884.7: misleading statements and similar grounds) is used against upselling conduct, not against pay design as such. (https://www.bar.ca.gov/pdf/accusations/ard243784_2013_05_24_acc.PDF)
- **Ontario (Canada)** requires repair shops to post a sign disclosing whether staff are paid commission, and on what (Consumer Protection Act, 2002, s.60; O. Reg. 17/05 s.50, per the government guide). This is disclosure, not a ban. (https://www.ontario.ca/page/guide-auto-repair-businesses; https://forms.mgcs.gov.on.ca/dataset/on00012)
- **[UNVERIFIED]:** whether any US state has a commission-disclosure rule. See file 09.

---

## 5) Shop-owner audit program design (sampling, rubric, scoring)

No single published, authoritative "inspection audit standard" exists for retail shops. The design below synthesizes:
- UICS reason-code logic (2.1);
- vendor "good DVI" criteria (3.2);
- generic QC practices: checklists with a manager or QC-tech sign-off, documented audits, digital records (I-CAR: https://rts.i-car.com/crn-13.html; https://autosmarts.co/en/understanding-auto-body-repair-quality-control/);
- standard quality-management practice (ISO 9001-style internal audit and corrective action).

Treat it as a recommended framework, not an industry mandate.

### 5.1 Program goals (balanced)

Measure **accuracy** (no false positives or false negatives), **evidence quality**, **communication accuracy** (correct Required/Suggested coding and urgency), and **revenue capture** (true needs not missed). Shop owners want both quality and revenue, and under-recommending is also a failure (a missed safety item, lost legitimate revenue). Score both directions.

### 5.2 Sampling

- **Random baseline:** about 5–10% of DVIs per technician per week, with a minimum of about 3 per tech so low-volume techs are still covered. Stratify by advisor and by vehicle-age band. *(Recommended practice; no industry source sets these percentages. [UNVERIFIED as benchmark])*
- **Risk-targeted (add on top of random):**
  - ROs with recommendation value far above the shop median for that mileage band;
  - more than X red items on a vehicle under 50k miles;
  - Required (red) items with no measurement or photo;
  - recommendations of fluid flushes or services before the OEM interval;
  - identical canned notes across many vehicles in one day;
  - very short inspection duration;
  - customer complaints, declines with pushback, or comebacks;
  - high-ticket estimates over a set dollar threshold.
- **Blind re-inspection (gold standard):**
  - Periodically, a second technician re-inspects the vehicle *before* seeing the first DVI, and the results are compared item by item.
  - Use for a small subset (for example 1–2 vehicles per tech per month) and for every disputed high-ticket item.
  - Planted-condition tests (a known-good vehicle, or a known defect) mirror the BAR undercover method (4.3). Use them ethically and only on shop-owned vehicles.
- **Calibration sessions:** monthly, all techs grade the same photo/measurement set (or the same car) independently. Compute agreement (% agreement or Cohen's kappa per item category), discuss disagreements, and update the shop's grading thresholds.

### 5.3 Per-item rubric (score each recommended or graded item)

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| **Evidence present** | No photo, measurement, or test result | Photo or note only, ambiguous | Photo clearly showing the condition *plus* measurement or test reading (gauge in frame, value recorded) |
| **Evidence matches vehicle** | Wrong VIN/plate/mileage, or stock image | Can't tell | VIN/plate/odometer or other identifier is consistent |
| **Spec referenced** | None | Generic rule of thumb | OEM spec or service-information value cited (min thickness, tread depth, interval) |
| **Classification correct** | Red without A/B/C basis, or a failed item left green | Right direction, wrong code | Correct UICS-style code (A/B/C, or 1–4) consistent with evidence |
| **Urgency/safety language** | Fear language or overstated | Vague | Accurate consequence and timeframe |
| **Recommendation fits finding** | Job doesn't address finding (e.g., flush for a non-fluid issue) or bundles unneeded parts | Partly | Minimum correct repair, with options disclosed |
| **OEM schedule fidelity** | Claims OEM schedule falsely | Uncertain | Matches the OEM schedule for mileage and severity, or is labeled as tech-experience (code 4) |
| **Canned text customized** | Generic canned note only | Edited partially | Vehicle-specific observation |
| **Missed items (reverse check)** | Re-inspection found an unreported Required item | Minor miss | None missed |

**Weighting and outcomes**
- Weight safety-critical categories (brakes, tires, steering/suspension, lighting) at 2×.
- Any item scoring 0 on "Classification correct" or "Evidence matches vehicle" is an **automatic fail** for that item and triggers review of the whole RO.

### 5.4 Inspection-level and technician-level scores

- **Inspection QA score** = weighted mean of item scores, plus completeness (all template points marked with an explicit status, "not checked" allowed only with a reason), photo count against standard, and the in/out odometer and VIN photo present.
- **Technician dashboard (monthly):**
  - verified-accuracy rate (items upheld on audit ÷ items audited);
  - false-positive rate;
  - false-negative/miss rate from blind re-inspections;
  - evidence completeness %;
  - calibration agreement;
  - recommendations per inspection *normalized by mileage band* against shop peers;
  - comeback rate.
- **Advisor dashboard:**
  - estimate-to-DVI fidelity (did the advisor upgrade a yellow to "needs now," add items, or change urgency?);
  - Required vs. Suggested labeling on the customer-facing estimate;
  - closing ratio *by code* (Required items closing low suggests a communication problem; Suggested items closing very high in some customer segments may warrant a pressure review);
  - customer complaints.
- **Outlier logic:** flag any tech or advisor whose mileage-normalized recommendation rate or average recommended dollars per RO is more than about 1.5–2 standard deviations above peers. A flag is a reason to look, not proof. Cross-check against verified-accuracy rate: high recommendations combined with high accuracy is fine.

### 5.5 Incentive design (to defuse conflicts)

- Tie any tech or advisor bonus to **verified accuracy and comebacks**, not just hours or sales. Pay only when sales, gross profit, and CSI are all met (a trade recommendation: https://www.autoshopowner.com/blogs/entry/257-service-advisor-pay-programs-that-work/), and add an audit-accuracy gate.
- Never set per-shift unit quotas for specific services. That was the alleged Sears mechanism (4.3).
- Disclose the pay structure to customers on request. Ontario requires a sign (4.3).

### 5.6 Coaching and corrective action

- Weekly: review failed items one-on-one with photos.
- Monthly: calibration session and update of the shop grading guide.
- Track corrective actions (retraining, template edits, removing auto-added canned jobs from yellow items) and re-audit the affected tech at a higher sample rate for 30 days.
- Lock or require edits on canned notes for Required items. Require numeric fields for measurable items: pad/shoe thickness, rotor thickness against minimum, tread depth (multiple points), battery test result, fluid test strip or meter readings, and the like.

### 5.7 Documentation for regulatory and dispute defense

Retain for each RO:
- the original DVI as sent (photos and video with timestamps, VIN, odometer);
- the tech ID and inspection duration;
- reason codes, measurements and the spec source;
- the customer authorization trail (time-stamped approvals and declines, the consent channel);
- audit results and any corrections;
- replaced parts or photos of them (ASA code: parts available for inspection, https://www.asashop.org/?p=55405).

ASA's code says keep records at least 1 year. State record-retention rules may be longer (see file 09). Keep the audit log itself as evidence of good-faith QA.

---

## 6) Audit implications

### 6.1 Consumer-facing checks (what the skill should ask or flag)

1. **Is each recommendation labeled "needed now" or "optional," and why?** Map each item to the UICS logic.
   - Needed now = failed, out of spec, or missing (A/B/C).
   - Optional = wear, convenience, OEM schedule, or tech experience (1–4).
   - A "red" item described only as "worn" or "getting low," with no spec value, is a classification flag.
2. **Evidence check:**
   - Does each red or yellow item have a photo that clearly shows *that* condition on *your* car (VIN, plate, odometer, color consistent)?
   - Is there a measurement and a spec? Missing measurements on measurable items (brakes, tires, battery) are a flag.
3. **Canned-language check:** identical boilerplate across items, or generic "recommend flush" notes with no test result, suggest template-driven recommendations.
4. **OEM schedule claim:** if an item says "manufacturer recommended," verify it against the owner's manual for your mileage and driving conditions. Also check service history for duplicates.
5. **Partial service and safety:** under UICS a shop may refuse to do half of a Required safety repair. That is legitimate, not upselling. Optional items should never be presented as conditions of service.
6. **Credentials are not proof of a correct inspection.** ASE, Blue Seal, I-CAR Gold, AAA, NAPA, or MAP membership signals training and process commitments, not that this inspection is right.
   - Useful levers: AAA-Approved shops agree to AAA dispute resolution. AAR, NAPA AutoCare, and MAP shops carry warranties (often 24/24 for AAR and NAPA).
   - Ask whether the shop is a MAP participant and uses MAP codes.
7. **Ask the questions the standards entitle you to:** written estimate before work; authorization before added work; your old parts back or shown (ASA code); itemized invoice that identifies used or reman parts.
8. **Get a second opinion on high-ticket or "urgent" items** without the first shop's DVI framing, where practical.
9. **ADAS and scan items:** a calibration or scan charge should cite an OEM procedure trigger and come with a report.

### 6.2 Shop-owner checks (what the skill should do for an owner)

1. **Re-classify every item** using A/B/C and 1–4, and report mis-coded urgency (red without A/B/C evidence; failed items left green or yellow).
2. **Evidence scoring** with the rubric in 5.3: photo shows condition, identifier consistency, measurement against spec, video narration.
3. **Template forensics:** detect auto-added canned jobs on yellow items, verbatim canned notes, the same note across many vehicles, default-green or blank points, and inspections completed implausibly fast.
4. **Estimate–DVI–invoice reconciliation:**
   - every estimate line traces to a DVI finding or customer concern;
   - nothing was escalated in urgency between DVI and estimate;
   - invoiced items match what was approved;
   - declined items are not billed.
5. **Missed-revenue (false-negative) check:** flag measurable items not measured, and safety categories not inspected. A quality audit should surface legitimately needed work, not only over-selling.
6. **Peer normalization:** compare tech and advisor recommendation rates by mileage band, and highlight outliers for human review. Provide calibration-set suggestions.
7. **Incentive and process risk notes:** if pay data is provided, flag quota-like structures and sales-only bonuses. Recommend accuracy-gated incentives.
8. **Defense file:** output a per-RO QA record (score, findings, corrective action) suitable for the shop's records.

---

## 7) Open questions / uncertainties

- **UICS current content:** the full, current UICS tables are member-only. Publicly confirmed are the reason codes (A/B/C, 1–4), the Pledge, the partial-service rule, and old 1999-era structure. Unknown: current edition and year, system-specific thresholds, and whether codes 3–4 have exact current wording beyond motorist.org's summary.
- **MAP history:** founding year and formal link to the Sears scandal not verified from a primary source.
- **Commission regulation:** no US state ban found; disclosure laws in US states not established (see file 09). Ontario disclosure confirmed from government guide pages, not statute text.
- **Independent DVI data:** no independent study found on whether DVIs raise unnecessary recommendations, how often yellow is overused, or how often photos are recycled. Vendor ARO/approval claims are unverified.
- **Benchmarks:** closing ratio, photos per inspection, and comeback rates come from consultants, vendors, and fleet sources with inconsistent definitions. Treat them as rough ranges only.
- **Platform specifics:** RO Writer not researched; Mitchell 1 "default green" behavior unconfirmed; measurement-field enforcement across Shopmonkey and Shop-Ware unknown.
- **AAA AAR:** warranty and re-inspection frequency vary by club and over time (12/12 vs. 24/24; annual vs. quarterly). The "under 5% qualify" figure is from a vendor blog.
- **NAPA AutoCare and other networks:** formal admission and audit criteria not published or found.
- **ISO 17020/9001:** described from general knowledge (ISO site blocked), and its prevalence among repair shops is unknown.
- **Academic:** Beck et al. (2014) findings taken from a search excerpt; the PDF was not readable in session.
- **Session limit:** the web-search budget was exhausted before follow-ups on MAP brake-specific rules, RO Writer, Ratchet+Wrench audit articles, and Motor Age / Fixed Ops Journal QA guidance. These are worth a follow-up pass.

---

## 8) Sources

**Association / standards bodies**
- MAP – Who we are (reason codes, Pledge): https://motorist.org/who-we-are/
- MAP – QA standards blog (Sept 2024): https://motorist.org/top-quality-assurance-standards-for-auto-repair-shops/
- MAP – Vehicle systems: https://motorist.org/vehicle-systems/
- MAP Exhaust UICS 1999 (third-party copy): https://pdf4pro.com/view/exhaust-system-uniform-inspection-5bb86.html
- AA1Car on MAP: https://www.aa1car.com/library/trtu196.htm
- ASE Blue Seal: https://ase.com/?p=2860
- ASE certification pathway: https://ase.com/about/certification-pathway/
- ASE C1: https://ase.com/tests/c1/
- ASE B6: https://ase.com/tests/b6/
- I-CAR Gold Class: https://info.i-car.com/gold-class/achieving
- I-CAR RTS OEM position statements: https://rts.i-car.com/crn-581.html
- I-CAR RTS: https://rts.i-car.com/crn-720.html
- I-CAR QC: https://rts.i-car.com/crn-13.html
- AAA AAR FAQ: https://www.acg.aaa.com/knowledge-center/approved-auto-repair-faqs
- AAA Hoosier standards: https://www.hoosier.aaa.com/automotive/auto-repair-shop-standards
- AAA North Dakota: https://northdakota.aaa.com/automotive/approved_auto_repair.aspx
- AAA 2016 trust survey: https://newsroom.aaa.com/2016/12/u-s-drivers-leery-auto-repair-shops/
- NAPA AutoCare: https://www.napaonline.com/en/auto-care
- ASA Code of Ethics: https://www.asashop.org/?p=55405
- ATRA Code of Ethics: https://members.atra.com/code-of-ethics
- ISO/IEC 17020 (not retrievable in session): https://www.iso.org/standard/52994.html

**Government / legal**
- Ontario auto repair guide: https://www.ontario.ca/page/guide-auto-repair-businesses
- Ontario sample sign: https://forms.mgcs.gov.on.ca/dataset/on00012
- Maryland HB 1425 (1997): https://mgaleg.maryland.gov/1997rs/billfile/hb1425.htm
- Alaska HB 330: https://www.akleg.gov/pdf/28/Bills/HB0330A.pdf
- CA BAR accusation citing §9884.7: https://www.bar.ca.gov/pdf/accusations/ard243784_2013_05_24_acc.PDF
- NASA fleet handbook: https://nodis3.gsfc.nasa.gov/npg_img/textview/243qualityofrepairs.htm

**Sears history**
- UPI 1992: https://www.upi.com/Archives/1992/06/16/Sears-hits-back-at-California-probe/4031708667200/
- Tampa Bay Times 1992: https://www.tampabay.com/archive/1992/06/12/sears-accused-of-auto-repair-fraud/
- Modern Tire Dealer: https://www.moderntiredealer.com/articles/33372-what-happened-to-sears-auto-centers
- LegalClarity: https://legalclarity.org/sears-auto-center-fraud-charges-investigation-and-settlement/

**Academic**
- Dulleck & Kerschbamer (2006): https://www.uibk.ac.at/economics/bbl/cv_papiere/12-dulleck-and-kerschbamer-jel-2006-on-doctors-mechanics-and-computer-specialists.pdf
- Beck et al. working paper: https://www2.uibk.ac.at/downloads/c4041030/wpaper/2014-02.pdf

**Trade press**
- Auto Service World on UICS: https://www.autoserviceworld.com/?p=267977
- MAP brake update: https://www.brakeandfrontend.com/map-standards-updated-for-brake-systems/
- Today's Class/AMRA (2024): https://www.vehicleservicepros.com/industry-news/news/55021554/automotive-maintenance-and-repair-association-amra-amra-map-program-integrates-with-todays-class-app
- Ensure DVIs happen: https://www.ratchetandwrench.com/articles/9249-ensure-digital-inspections-happen
- Mitchell 1 Manager SE Inspections: https://www.ratchetandwrench.com/site-placement/latest-news/news/55315119/mitchell-1-releases-multi-point-inspection-tool-for-manager-se-shop-management-system
- Mitchell 1 (AftermarketNews): https://www.aftermarketnews.com/mitchell-1-inspection-tool-launch/
- Bolt On + Tekmetric: https://www.vehicleservicepros.com/industry-news/service-repair/press-release/21231788/bolt-on-technology-bolt-on-technology-teams-with-tekmetric-to-bring-popular-customer-engagement-features-to-even-more-repair-shops
- Bolt On + Protractor: https://www.aftermarketnews.com/bolt-on-technology-now-integrates-with-protractor-shop-management-platform/
- Closing ratios: https://www.ratchetandwrench.com/running-a-shop/article/11490381/improving-shop-closing-ratios-october-01-2013
- KPI: closing ratio (AutoZone-sponsored): https://ratchetandwrench.com/sponsored-content/autozone/article/33010675/the-kpi-closing-ratio
- Six steps for a better closing ratio: https://www.ratchetandwrench.com/running-a-shop/article/11483528/six-steps-for-a-better-closing-ratio-2017-03-01
- Bottleneck: disproportionate closing ratio: https://www.ratchetandwrench.com/articles/10495-bottleneck-disproportionate-closing-ratio
- Advisor pay: https://www.vehicleservicepros.com/shop-operations/service-repair/article/21195702/service-advisor-pay-program-tips-that-work
- Advisor pay programs: https://www.autoshopowner.com/blogs/entry/257-service-advisor-pay-programs-that-work/
- Flat-rate discussion: https://www.repairerdrivennews.com/?p=33815
- Podcast transcript: https://autofixadvisorcast.transistor.fm/7/transcript

**Vendor (marketing / help; treat claims as non-independent)**
- AutoVitals metrics: https://blog.autovitals.com/auto-repair-shop-metrics
- AutoVitals KPIs: https://blog.autovitals.com/key-performance-indicators-to-transform-your-shop-operations
- AutoVitals DVI: https://blog.autovitals.com/why-shops-choose-digital-vehicle-inspections
- AutoVitals help, low ARO: https://help.autovitals.com/low-aro
- AutoVitals help, declined jobs: https://help.autovitals.com/?p=21586
- Tekmetric DVI: https://www.tekmetric.com/feature/digital-vehicle-inspection
- Tekmetric performing an inspection: https://tours.tekmetric.com/answers/performing-an-inspection-tekmetric
- Shopmonkey inspections: https://www.shopmonkey.io/product/inspections
- Shopmonkey tech app help: https://help.shopmonkey.io/en/articles/8887793-inspections-in-shopmonkey-for-techs-mobile-app
- Shop-Ware DVI: https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/
- Shop-Ware questions: https://shop-ware.com/questions/
- ALLDATA reason codes: https://www.alldata.com/manage-online-article/code-settings-inspection-reason-codes
- ServiceProfessional: https://serviceprofessional.support.site/article/whats-new
- Autoflow DVI best practices: https://autoflow.com/training/best-practices/how-to-perform-a-good-digital-vehicle-inspection-dvi/
- AutoServe1: https://autoserve1.com/why-youre-losing-service-sales/
- AutoSmarts QC: https://autosmarts.co/en/understanding-auto-body-repair-quality-control/
- Oxmaint comeback KPI: https://oxmaint.com/industries/fleet-management/technician-comeback-tracking-kpi
- iDriveCertified: https://idrivecertified.com/blog/certified-automotive-repair-shop-how-to-choose-the-best
