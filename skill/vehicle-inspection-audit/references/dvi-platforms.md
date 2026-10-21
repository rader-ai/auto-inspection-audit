# DVI Platforms: Identification and Known Pitfalls

As of 2026-10-20. Built from public help centers, vendor pages, release notes, app-store listings and trade press. No logins, demos or vendor contact.

**Provenance tags:** **[DOC]** = vendor help article, release note or official source. **[3P]** = third-party listing, trade press, review or forum. **[INF]** = inference, not stated anywhere. **[UNVERIFIED]** = plausible but not confirmed publicly. Vendor performance claims (ARO lift, close rates, approval times) are vendor-reported and unverified. Changes dated 2023–2026 are marked **(Mon YYYY)**. Numbers in `[n]` point to Sources (section 6).

**Shop-Ware caveat:** Shop-Ware help-center details (support.shop-ware.com) were fetched with a search-engine user agent. Claims from there are tagged **(re-verify via normal access)**.

## Contents

1. How to identify the platform (fingerprint table)
2. Cross-platform failure modes (read first)
3. Per-platform cards
   - 3A Independent: Tekmetric, Shopmonkey, Shop-Ware, AutoVitals, Bolt On, (integrations)
   - 3B Legacy independent: Mitchell 1 Manager SE, ALLDATA Manage, Protractor, RO Writer, NAPA TRACS, Shop Boss, ARI
   - 3C Dealer: CDK, Reynolds (Service Flex), Xtime, myKaarma, Dealer-FX, Tekion, generic dealer MPI pattern
   - 3D Quick-lube and tire chains: Valvoline, Jiffy Lube, Discount Tire, Les Schwab
   - 3E Fleet: Fleetio, Whip Around, Samsara
4. OEM MPI color conventions
5. Audit playbooks (consumer, shop owner, fleet)
6. Sources

---

## 1. How to identify the platform

Look at grade labels, section names, approval-page style, branding/footer, and link domain. **Link domains are mostly unconfirmed** — none of the customer share-link domains below was confirmed in a public source; treat a domain as a hint, not proof. Confidence reflects how distinctive the tells are.

| Platform | Terminology / grade labels | Layout cues | Link domain | Confidence |
|---|---|---|---|---|
| Tekmetric | "Check & Okay" / "May Require Attention Soon" / "Requires Immediate Attention" / "Not Applicable"; "Technician Concerns"; "Customer Concern" / "Customer States" | "Vehicle Health Report" / "Inspection Report" sent as second tab beside estimate; "Visit Details" tab; Vehicle Health chart (since Sept 2025); text opens "Hello, your vehicle has been inspected at <Shop>…" | **`shop.tekmetric.com/inspection/<token>`** — confirmed from a real customer report (Oct 2026); printed PDFs show it in the page footer | High |
| Shopmonkey | "Passed / Needs Attention / Failed / N/A" with check, !, X, grey icons; "Estimate Requested" / "Deferred by Customer"; "Recommended" services block | SMS/email carries a **PDF attachment plus a link**; inspection footer/terms block when e-signed | [UNVERIFIED] | High |
| Shop-Ware | "DVX" branding; "Approve" / "Decline for Now"; urgency-colored circles; "out the door" totals | Full RO + inspection + recommendations ranked by urgency; optional pay button | App at app.shop-ware.com; customer link [UNVERIFIED] | High |
| AutoVitals | Shop-defined status sections, often "Needs Immediate Attention" / "Needs Future Attention" / "Good" | "Why is this important" educational videos; "Offerings" promo carousel; "Services Being Performed" block; arrowed photo captions; date stamps on images; car-with-stethoscope placeholder | Shop settings at shop.autovitals.com; customer link [UNVERIFIED] | High |
| Bolt On | Green / yellow / red bars per system | "BOLT ON" branding | [UNVERIFIED] | Medium |
| Mitchell 1 Manager SE | Green / yellow / red; "Truck Edition" for heavy duty | Manager SE RO/invoice layout; ProDemand-style labor op names [INF] | [UNVERIFIED] | Low–medium |
| ALLDATA Manage / Inspections | **"Red / Amber / Green"** ("Amber" not "Yellow" is the tell) plus **N/C** (Not Checked); reason codes | Tread in **mm** (Outer/Middle/Inner); ALLDATA footer text block; "Estimate" / "Repair Order" documents | [UNVERIFIED] | High |
| Protractor | Color-coded; "Work Order"; "Deferred Services" list on later visits [INF] | Protractor branding | [UNVERIFIED] | Low–medium |
| RO Writer | — | "R.O. Writer" branding on RO; DVI pages may come from a third-party vendor [INF] | [UNVERIFIED] | Low |
| NAPA TRACS (AutoServe1) | — | NAPA AutoCare branding, often AutoServe1 styling | [UNVERIFIED] | Medium |
| Shop Boss | — | "BOSS Inspect", "BOSS Pay" naming on approval/payment pages [INF] | [UNVERIFIED] | Low |
| ARI | — | Simple invoice/estimate PDFs, often owner-operator [INF] | [UNVERIFIED] | Low |
| CDK | Dealer G/Y/R [INF] | CDK-style RO with dealer branding; "Mobile Approvals" messages | [UNVERIFIED] | Low |
| Reynolds | **"Report Card"**; opcodes on lines | ERA-IGNITE-format RO; eApproval phone page [INF/partly DOC] | [UNVERIFIED] | Low–medium |
| Xtime | Dealer G/Y/R [INF] | Xtime-branded consumer pages under dealer name | Likely xtime.com-based [UNVERIFIED] | Medium |
| myKaarma | — | **"Cart"**-style approval page with per-line video thumbnails and prices | [UNVERIFIED] | Medium |
| Dealer-FX | "Digital MPI"; "All Green" landing page | "Service Summary" page; "Inspection Report PDF"; OEM-branded styling (Nissan etc.) | [UNVERIFIED] | Medium |
| Tekion | Severity tiers for deferred follow-up | Tekion consumer portal; UVeye or Hunter sheets attached to RO [INF] | [UNVERIFIED] | Low–medium |
| Les Schwab | "Checked and OK" / "May Require Follow-Up Attention" / "Requires Immediate Attention" | "Safety Status Check" title; printed report | — | High |
| Valvoline / Jiffy Lube | "18-Point Maintenance Check" (Valvoline); "Signature Service" / 17-point (Jiffy Lube) [3P] | In-lane checklist on invoice | — | Medium |
| Discount Tire | Tread, wear pattern, DOT age, pressure, damage | Store tire report | — | Medium |
| Fleetio | Pass/Fail, drop-downs; "Issue", "Service Entry" | Internal fleet forms | — | High |
| Whip Around | OK / Defect; driver / mechanic / next-driver signatures | DVIR form | — | Medium |
| Samsara | Safe / Unsafe / Resolved | DVIR with per-defect resolution | — | Medium |

**Generic dealer MPI tells** (any dealer DMS): Green OK; yellow/red lines carrying **Op-Code, Concern, Correction**; identical default concern text; "Multi-Point" PDF attached to RO.

**If unidentifiable:** say so in the report, then apply every failure-mode check in section 2 generically: trace each estimate line to red / yellow / menu / nothing; look for missing measurements, uniform wording, all-green pages, reused photos, and online vs PDF differences. Ask the shop which software produced it.

---

## 2. Cross-platform failure modes

Format per mode: **What** happens · **Where** (platforms) · **Shows as** · **Detect** · **Label** (usual status from SKILL.md).

### 2.1 Red *or yellow* automatically adds a priced job
- **What:** a canned job or service package mapped to an inspection item lands on the estimate when the item is rated red **or yellow**. A "monitor / future" item then looks like do-now work.
- **Where:**
  - Tekmetric: red/yellow + mapped canned job + inspection marked complete → auto-added to Estimate (since May 2021, Scale tier) [DOC]. Red/yellow also auto-fill a "Technician Concerns" table.
  - AutoVitals: a Condition's **Default Action** recommends the job every time the condition is tapped; "UPDATE WO" pushes it to the POS as an unapproved labor line [DOC].
  - Protractor via Autoflow: Red or Yellow adds the mapped service package to the work order (or Deferred Services if enabled), matched by exact "SMS Code" [DOC].
  - Mitchell 1 Manager SE: flagged items automatically become **job containers** in Job View [DOC].
  - ALLDATA: Red/Amber displays pre-linked **suggested jobs** (shop configured) [DOC].
  - Reynolds / Tekion: Hunter drive-over recommendations auto-added to the RO / MPI [DOC].
  - Dealer DMS (Dominion pattern): yellow/red open an Op-Code pop-up [DOC].
- **Shows as:** a priced line for every yellow item; labor from guide/Smart Job templates rather than from what the tech saw; job scope broader than the finding (full brake job for a yellow pad).
- **Detect:** for every estimate line, record its source: red finding, yellow finding, menu/interval item, or nothing. Check the Recommended vs Deferred split. Check that the job fits the finding (wrong package code → wrong service).
- **Label:** yellow-sourced lines → **Supported – optional** (if evidence is adequate); scope wider than the finding → **Inconsistent**; no traceable finding → **Evidence missing**.

### 2.2 Mileage / menu items pre-rated or shown as condition findings
- **What:** interval maintenance is presented with the same colors and layout as observed defects.
- **Where:**
  - Tekmetric **Recommended Maintenance on DVI** (Scale tier, Aug–Sept 2026): odometer entry checks OEM / Shop / "Shortest" intervals (OEM data + Tekmetric and Carfax history) and **pre-rates tasks: Overdue → Red, Due Soon → Yellow** (shop can change: Overdue Red/Yellow; Due Soon Red/Yellow/Green). Note pattern: "[Task] is overdue by X miles. Recommended every Y." Tech can override [DOC]. Recommended Jobs tab can use **BG** (fluid brand) presets [DOC].
  - Mitchell 1 + **ProDemand**: ProDemand's estimate guide presents OEM maintenance by time/mileage and indicator lights and transfers into the open RO in one click. ProDemand does not itself color items; the risk is **mixing** schedule jobs with inspection jobs on one estimate without labels [INF].
  - Shopmonkey: MOTOR Maintenance Schedules + mileage/time "Suggestions" [DOC].
  - Dealers: OEM maintenance menus; GM PASE counts menu presentations [DOC]. Brake fluid condition and throttle-body carbon cannot be visually confirmed in a standard MPI and are usually time/mileage items [3P].
  - Quick lube: "manufacturer recommended maintenance" from a visual checklist (Jiffy Lube) [DOC].
- **Shows as:** red/yellow filter, fluid, flush or induction-cleaning items with no photo or measurement; "overdue by…" wording.
- **Detect:** ask "what did you observe?"; compare with the owner's manual (normal vs severe) and service history. Every line should be labeled either *observed condition* (measurement/photo/test) or *schedule interval* (with schedule cited); lines with neither are unsupported.
- **Label:** due per OEM → **Supported – optional**; earlier/more often than OEM → **Beyond OEM schedule**; can't check schedule → **Needs OEM spec**.

### 2.3 Bulk-rate, default-green, unmarked-as-green
- **What:** items are rated without a per-item judgment, so a page of green looks like a full inspection.
- **Where:**
  - Tekmetric **"Rate All Tasks"** fills every blank line with one rating (since Apr 2019) [DOC].
  - Mitchell 1 Manager SE: **everything not marked can default to green**; techs mark only problem items [DOC].
  - Shop-Ware TechApp **swipe-to-green** clears a line without opening it [DOC].
  - Dealer MPIs generally: consultant reports of all-green MPIs on 275k-mile trucks [3P]; OEM programs reward MPI completion counts [DOC/INF].
- **Shows as:** many green/N/A items with no photos or findings; green brakes with no mm; green on items that can't be seen without a lift.
- **Detect:** Tekmetric Inspection Report average inspection time; Shopmonkey Items Rated % = 100 with zero media; all-green share by tech vs vehicle mileage; compare to later invoices.
- **Label:** a green item never supports a claim by itself. For missed problems use **Evidence missing**; for safety systems shown green without evidence where other signs suggest a problem → **Verify in person – safety**.

### 2.4 Carry-forward / copied ratings
- **What:** last visit's result is re-issued.
- **Where:** Tekmetric Inspection History can copy a prior inspection **including ratings and findings** to the current RO [DOC]. AutoVitals **Carry Forward → Confirm** (tablet) re-confirms last visit's topic result [DOC]. Fleet: Samsara unresolved defects carry over to the next DVIR [DOC]; Fleetio passing an item later does not close an open Issue [DOC].
- **Shows as:** findings identical to the prior visit; photo dated an earlier visit (AutoVitals date stamp); cluster-photo mileage ≠ RO odometer.
- **Detect:** compare with the prior report; check dates and mileage in photos.
- **Label:** **Inconsistent** when dates/mileage don't match; otherwise **Evidence missing**.

### 2.5 Photos moved or copied between ROs; off-vehicle uploads
- **What:** media may not come from this vehicle on this visit.
- **Where:** AutoVitals photos can be **moved or copied to another topic, the work order, or a different open RO**, and whole inspections moved to another RO [DOC]; AutoVitals tablet inspections match ROs **by VIN** (wrong VIN → wrong match) [DOC]. Tekmetric desktop upload opens a file browser (drag-and-drop since Mar 2026), so media need not be captured live [DOC]. AutoVitals images can be uploaded from the advisor web screen [DOC].
- **Shows as:** plate, VIN, paint, wheel, tire or interior that differ between photos; image date outside the visit; same image across items or customers.
- **Detect:** see `image-evidence.md` identity checks. Never call a photo fake; state the observable mismatch.
- **Label:** **Inconsistent** (photo contradicts vehicle) → evidence **Contradicts**.

### 2.6 Hidden / internal items and evidence
- **Where:**
  - Tekmetric **internal inspections** (e.g., check-in damage, QA) are hidden from all customer documents and links and excluded from the Inspection Report [DOC]. Since Sept 2025 the customer Vehicle Health chart drops N/A and incomplete tasks and hides "Not found" findings [DOC]. Customer Concern block can be hidden via Transparency Settings [DOC].
  - AutoVitals **Hidden** status suppresses an item from the customer report; image suppressor/eye icon hides photos; tech notes stay shop-only until moved to customer notes [DOC].
  - Shop-Ware: recommendations must be **published**; drafts are invisible to the customer [DOC (re-verify via normal access)].
  - ALLDATA: N/C items may be omitted or overlooked [DOC/INF].
- **Shows as:** customer report with fewer items than the template; sparse report that hides skipped items.
- **Detect:** ask for the full shop-view inspection, including N/A/hidden items and internal check-in photos.
- **Label:** **Evidence missing** for anything you can't see.

### 2.7 AI-rewritten or advisor-edited customer text
- **Where:**
  - AutoVitals **Otto Notes** rewrites customer notes for clarity/grammar (not shop notes or measurements); auto-enabled for eligible packages from **Feb 12, 2026**, opt-out [DOC]. Note-conflict icon flags tech-vs-advisor discrepancies [DOC].
  - Shop-Ware **AutoWrite** summarizes, improves, changes tone or translates Notes/Findings and messages (announced v12.7.0, **Oct 2025**, early adoption) [DOC (re-verify via normal access)]. Techs enter details; advisors write customer text; some users can be limited to "save as draft" (**Jan 2024**) [DOC].
  - Tekmetric **"Smart DVI"** (announced **Apr 2026**, "coming soon"): tech narrates a video; AI transcribes, organizes images and drafts estimate items [3P].
  - Shopmonkey: "Completed By" can differ from the rater [DOC]. Dealer DMS: "updates made by Advisors/Managers" counted in upsell report [DOC].
  - Whether AI tools leave any marker in customer output or logs: [UNVERIFIED].
- **Shows as:** polished, uniform prose; text that doesn't match the photo or the tech's terse note.
- **Detect:** ask for the technician's original notes / shop view; compare.
- **Label:** prose alone never supports a finding; mismatch with photo → **Inconsistent**.

### 2.8 Canned condition text / boilerplate
- **Where:** AutoVitals Default Customer Note and Default Image Caption per Condition (one tap sets color, action and text) [DOC]; Shopmonkey Quick Notes [DOC]; Tekmetric preset findings [DOC]; Dealer DMS: saving yellow/red with no text adds a **default concern automatically** [DOC]; Bolt On canned notes [DOC].
- **Shows as:** identical sentences across items or vehicles; caption names a part not visible; wrong side/axle.
- **Label:** **Inconsistent** if text contradicts photo/position; otherwise **Evidence missing**.

### 2.9 No structured measurement fields (normal on some platforms)
- **Where:** **Tekmetric, Shopmonkey and Shop-Ware document no structured tread/pad/rotor/battery fields** in the DVI; readings exist only if typed into free-text findings or attached (photo, PDF, scan screenshot). Bolt On, RO Writer, Shop Boss, ARI: none documented. Measurement-capable: AutoVitals (measurement fields needing advisor approval; Groove Glove; Hunter), ALLDATA (tread mm by position; Value/Unit sub-items), Mitchell 1 (measurement-triggered stored notes), dealer Hunter integrations (Xtime, Reynolds, Tekion).
- **Implication:** on Tekmetric/Shopmonkey/Shop-Ware, a missing number is **normal, not suspicious**. Request the readings ("LF pad mm? tread per position in 32nds?"); don't treat absence as a red flag about the shop.
- **Label:** **Evidence missing** (request measurements), not Inconsistent.

### 2.10 Online vs PDF / print content differences
- **Where:** Dealer-FX inspection-level media (e.g., "All Green" video) **not in the Inspection Report PDF** [DOC]. ALLDATA PDF "View" omits sub-items (e.g., which position failed); "Print inc sub items" shows them [DOC]. Tekmetric videos never print; PDFs can print without photos [DOC]. Shop-Ware PDFs can print without pictures (Jan 2024); Authorization Summary excluded from PDFs unless ticked [DOC (re-verify via normal access)]. AutoFlow → Tekmetric drops image markups (2023) [DOC]. AutoVitals template change **restyles all historical links**; links embedded in the POS stop working after a shop leaves AutoVitals [DOC]. Tekmetric links can be unshared [DOC]. Shopmonkey images follow upload order (spring 2026) [DOC].
- **Detect:** get both the online link and the PDF; compare item counts and positions. Save copies with retrieval date; the current link is not proof of what was originally sent.
- **Label:** content present in one format but not the other → note it; contradictions → **Inconsistent**.

### 2.11 Machine- or AI-generated findings without tech verification
- **Where:** CDK **Predictive Service** adds likely-failure items to the MPI using history/AI (2026) [DOC]; Hunter drive-over tread/alignment into Xtime (since Feb 2021), Reynolds, Tekion [DOC]; UVeye scans into Reynolds, Tekion, myKaarma [DOC]. Whether predicted items are labeled on the customer MPI: [UNVERIFIED].
- **Shows as:** lines citing a scan or prediction; tread/alignment values identical to a drive-over printout.
- **Detect:** ask whether a tech physically confirmed it. Hunter customer view (AutoVitals) shows only after-alignment values [DOC].
- **Label:** predicted, unconfirmed → **Evidence missing**; scan printout present → evidence Partial/Strong.

### 2.12 OEM incentive rubber-stamping (dealers)
- **What:** OEM programs reward MPI completion and menu-presentation counts (GM PASE counts MPVIs and menu presentations monthly from closed ROs [DOC]; Ford Commitment Program requires video MPI from approved vendors [DOC]). This raises the risk of all-green MPIs and menu items next to condition findings [INF].
- **Also:** video quality ≠ diagnostic accuracy — myKaarma's AI "Tech Video Grader" scores clarity/completeness, not correctness [DOC/INF].
- **Detect:** all-green MPI on a high-mileage vehicle; polished video that never shows a gauge or the failed part.
- **Label:** green without evidence → no support; video without the claimed condition → **Evidence missing**.

### 2.13 Quick-lube visual-only checks
- **What:** Valvoline's check reportedly **does not measure tread depth** [partly UNVERIFIED]; Jiffy Lube uses a **visual** checklist [DOC]. Historical: NBC LA 2006 hidden camera found services billed but not performed, and a fuel-injection cleaning attributed to Honda that Honda did not recommend [3P].
- **Detect:** tire or brake verdicts with no measured value; fluid services with no before/after evidence; filters billed with old part not shown.
- **Label:** tire/brake verdicts → **Evidence missing**; fluid/filter by mileage → check schedule (**Beyond OEM schedule** if early).

### 2.14 Severity mismatch between layers / thresholds
- **Where:** Shop-Ware inspection-line color and recommendation urgency are **independent**; default urgency white = not set [DOC (re-verify via normal access)]. AutoVitals CRM "Needs Immediate Attention" reminder mode may re-recommend work already done [DOC]. Gauge color bands vary by tool (OTC pencil gauge vs heavy-duty gauge, section 4) and store policy (Discount Tire 4/32") vs legal 2/32" [DOC].
- **Detect:** compare line color vs recommendation urgency; ask which threshold/gauge set the color; check mm vs 32nds (ALLDATA mm: 3 mm ≈ 3.8/32").
- **Label:** **Inconsistent** when layers disagree; store policy shown as legal requirement → **Supported – optional**.

### 2.15 Approval-record gaps
- **Where:** Shop-Ware Authorization Summary opt-in, off PDFs by default (since Jul 2024) [DOC (re-verify via normal access)]; Tekmetric method dropdown allows phone/text with no signature, digital signature optional [DOC]; Shopmonkey "reset authorization when price increases" optional [DOC]; Shopmonkey "Recommended" services sit outside the estimate total until authorized [DOC/INF].
- **Detect:** ask for authorization history / point-in-time copy; compare price at approval vs invoice.

### 2.16 Fleet issue-carryover quirks
- **Fleetio:** a failed item creates an **Issue** by default, but a user can "acknowledge" a failure with no action; Issues close only by Service Entry, Work Order or manual close — **passing later doesn't close it**; next inspector can reject a resolution, creating a new issue [DOC].
- **Samsara:** unresolved defects **carry over** to the next DVIR; DVIR status (Safe/Unsafe/Resolved) tracked separately from per-defect resolution [DOC, via excerpt].
- **Whip Around:** Defect → work order only on Pro tier [DOC].
- **Shows as:** same defect for weeks; repair invoiced while issue stays open; acknowledged-but-unrepaired failures.
- **Detect:** reconcile WO, Issue and invoice; check 49 CFR 396.11 repair certification.
- **Label:** unrepaired safety defect → **Verify in person – safety**; invoiced but issue open → **Inconsistent**.

### 2.17 Completion and KPI artifacts (owner audits)
- Shopmonkey "Completed" counts only if someone taps Complete [DOC]. Tekmetric Inspection Report counts only **posted** ROs and excludes internal inspections [DOC]. AutoVitals BCP counts by RO **close date**, closed ROs only, and the **highest revision** even if a lower one was edited last [DOC]. Use per-inspection detail rows, not dashboards, to reconstruct events.
- CDK June 2024 ransomware outage may have left missing or paper MPIs at CDK dealers in that window [INF].

---

## 3. Per-platform cards

Template: **Structure · Grading · Measurements · Media · Finding → estimate · Customer report & approval · Owner audit data · Pitfalls · Doc quality · Src.** Pitfall numbers (2.x) point to section 2.

### 3A. Independent shop platforms

#### Tekmetric (all-in-one shop management with built-in DVI)

**Observed in a real customer report (Oct 2026, printed from the share link):** sections run "Your Visit" (customer, vehicle, RO#, Time In, Service Advisor) → "Reason for Visit" (customer concerns, sometimes with a tech "Finding" and photos under each) → "Vehicle Health" donut chart → "Technician Findings" (red/yellow items only) → "Inspections Performed" (named template, e.g. "All Star Inspection", grouped Walk Around / Test Drive / Exterior / Interior / Underhood & Fluid Condition / Suspension & Alignment / Tires & Brakes) → "N technician concerns found". Legend reads "Checked & Okay / May Require Attention Soon / Requires Immediate Attention"; a gray minus icon = N/A. Things the audit should expect: **no odometer reading anywhere on the inspection report** (ask for mileage before judging any interval-based item); **no prices** (the estimate is a separate document); **the printed PDF embeds photos only as ~150×200 px thumbnails** and videos as a play icon — too small to verify any photo-based claim, so ask for the live link or full-size images. Maintenance items used canned text with generic intervals ("typically due every 3 years or 30,000 miles", "due based on maintenance intervals") rather than the OEM schedule, consistent with preset findings (2.8).

- **Structure:** Template → Inspection Groups → Tasks, with preset Findings (general dropdown + task-specific; custom text allowed) [DOC]. Templates marked **Default** auto-add to every RO (default ordering Sept 2026). Templates can be **internal by default** (hidden from customers). No item types beyond rating + finding + media; no stock library documented [UNVERIFIED whether onboarding seeds templates].
- **Grading:** Check & Okay / May Require Attention Soon / Requires Immediate Attention / Not Applicable (= green/yellow/red/N/A). Unrated tasks used to show "Incomplete"; Tekmetric advises N/A as positive confirmation. Non-judgment ratings: **Rate All Tasks** (2.3), **copy prior inspection with ratings** (2.4), **Recommended Maintenance pre-rating** (2.2, Aug–Sept 2026). No measurement-driven color.
- **Measurements:** none structured (2.9). Readings only in free text, photos, PDFs; Tekmetric suggests scan-tool/Mode 6 screenshots. Canadian units setting (Sept 2026). Tire DOT capture outside DVI. Midtronics integration [UNVERIFIED].
- **Media:** camera/video/PDF per task row; video since May 2020; markup (circle, arrow, text, rotate; draw/zoom/crop Aug–Oct 2025) — **annotated image replaces what the customer sees**; videos can't be edited. Desktop file upload; drag-and-drop (Mar 2026). Media on Technician Concern (Feb 2026) and Customer Concern (Jan 2026). No capture-timestamp overlay documented.
- **Finding → estimate:** canned job mapped per task; **red/yellow + inspection complete → auto-added** (2.1). Smart Jobs resolve labor/parts by VIN. Labor: Tekmetric guide, ProDemand and ALLDATA (Grow/Scale); Tekmetric calls guide times reference only. Recommended Jobs tab with Tekmetric or **BG** presets. **Draft** jobs (never presented) vs **Declined** (presented; counted in close ratio, Declined Jobs report, Job History).
- **Customer report & approval:** "Inspection Report"/"Vehicle Health Report" auto-sent as second tab with estimate. Layout since Sept 2025: Visit Details tab, Customer Concern first, Vehicle Health chart, "Not found" hidden. Default inspection text reworded Feb 2024 (old wording implied car ready). Per-job approve/decline; method recorded (digital signature, paper, verbal in person, phone, text, email); digital signature optional; **point-in-time authorization copies** on Summary tab; jobs can be un-approved. Transparency Settings can differ estimate vs invoice and per RO. Links can be unshared; "viewed" indicator (Aug 2022).
- **Owner audit data:** **Inspection Report** (all tiers since Feb 2026): ARO and close ratio with vs without inspections, completion rate, average inspection time, average findings, % sent/viewed, by attachment count; group by tech/writer/inspection; PDF/CSV. Posted ROs only; internal inspections excluded. **Inspection History** per vehicle: RO#, PDF, tech, rating counts, created/completed dates, vehicle-transferred flag. Public API Inspection endpoint since Jun 2019 [fields UNVERIFIED].
- **Pitfalls:** bulk-rated lines (2.3); copied ratings (2.4); interval-driven red/yellow — red "Engine Air Filter" with "overdue by X miles" wording and no photo is an interval item, not a defect (2.2); auto-added lines priced from templates (2.1); hidden N/A/incomplete and internal inspections (2.6); videos never print (2.10); free-text only (2.9). Whether pre-ratings are labeled as interval-based on the customer report: [UNVERIFIED].
- **Doc quality:** deep, current help center. **Src:** [1]–[25], [184].

#### Shopmonkey (all-in-one with built-in DVI)
- **Structure:** inspection created from an estimate's Inspections tab, from scratch or template (Lists → Inspection Templates). Item = name + status + photos/videos/PDFs/notes/recommendations. Ad-hoc items allowed; mobile techs can add but not create templates. Positioned partly as check-in/check-out documentation. **Quick Notes** (title hidden, content visible; editing after insert changes only that instance). HQ can share templates across locations. Stock templates [UNVERIFIED].
- **Grading:** Passed (green check) / Needs Attention (yellow !) / Failed (red X) / N/A (grey). Custom statuses appear possible [config UNVERIFIED]. Optional review actions on yellow/red: "Estimate Requested" / "Deferred by Customer". No default or measurement-driven color documented; bulk-rate not documented [UNVERIFIED].
- **Measurements:** none structured (2.9). Tread depth is a tire-inventory spec, not an inspection field. TIN/DOT scanning (Apr 2026). Battery import [UNVERIFIED].
- **Media:** per item jpeg/png/PDF/mp4, **max 50 MB**; voice notes (marketing). Upload system rebuilt Apr 2026 after reliability problems. Markup [UNVERIFIED]. Images follow **upload order** in customer view/prints (spring 2026); upside-down print fix. Info tooltip shows created/performed/completed dates and user.
- **Finding → estimate:** canned services aligned to findings **by hand**; no automatic red-to-estimate rule documented. "Recommended" services excluded from total until authorized, shown in separate section. MOTOR Maintenance Schedules + mileage/time Suggestions. Labor: MOTOR; ALLDATA since Mar 2026. Deferred services created on invoice/archive; Deferred Services by Customer report.
- **Customer report & approval:** "Share Inspection" by SMS/email sends **PDF + live link**; all inspections on order shared together; customers can comment. **Inspection e-signature** (Apr–May 2026) requires Inspection Footer; signed PDF in Activity tab; adding/removing an attachment invalidates the signature (fix Apr 2026). Estimate: per-service authorize, optional e-signature, shop can authorize on behalf and record method; optional **reset authorization on price increase** (history kept). Each status change creates an updated PDF link (Apr 2025).
- **Owner audit data:** **Vehicle Inspections Detail** (per inspection, Excel): inspectors vs **Completed By**, Items Rated / %, Passed/Needs Attention/Failed/N/A counts, **Avg Finding %** = (yellow+red) ÷ (green+yellow+red); "Unassigned" = rated without credited tech. **Summary**: Orders with Inspection %, per-tech volume, ARO. REST API (inspection objects [UNVERIFIED]).
- **Pitfalls:** "Completed" needs the button (2.17); Completed By ≠ rater (2.7); resends go only to primary contact; Recommended lines outside total (2.15); Quick Notes boilerplate (2.8); free-text only (2.9).
- **Doc quality:** deep, current. **Src:** [26]–[45], [186], [187].

#### Shop-Ware (Vehlo since Mar 2024; customer portal "DVX")
- Help-center claims below are **(re-verify via normal access)**; marketing-page claims (shop-ware.com) are not affected.
- **Structure:** templates in the "Cannery"; added on the fly; auto-populated safety inspection on every work order [DOC, marketing]. Inspections live **under a service** on the RO (with labor, parts, fees, sublet), added in Edit Mode (re-verify via normal access). No item types beyond color + notes + images.
- **Grading:** two independent layers (2.14): **inspection line** green/orange(yellow)/red in TechApp; **recommendation urgency** set by advisor: white = not set (default), green low, yellow medium, red high (re-verify via normal access). Orange vs yellow likely the same tier [INF]. **Swipe-to-green** without opening (2.3) [DOC, marketing]; yellow/red open "Create Findings".
- **Measurements:** none documented (2.9). API partners include AutoVitals, AutoFlow, so a measurement-capable add-on may sit on top (re-verify via normal access).
- **Media:** native camera; photo markup (Mar 2024); video limit 50 MB → **500 MB (Jul 2025)**; notes/attachments as icons per item; PDFs printable without pictures (Jan 2024); MMS photos/videos (May 2026, v13.4.0) (re-verify via normal access).
- **Finding → estimate:** clipboard-and-wrench icon on a line, "Create a Finding" in Notes Feed, or convert a service. Recommendation must be **published** to be visible; users can be limited to "save as draft only" (Jan 2024). States: Approve, Add to RO, Reset to Pending, Decline ("Decline for Now"), Mark as Done, Postpone. Pending/declined reappear on new estimates and in unfulfilled-recommendations export; no automatic declined-work reminders; recommendation added to a **closed** RO doesn't carry forward. Labor: canned jobs, past services, "Estimator" guide; good/better/best options. **AutoWrite** AI (Oct 2025) (2.7). (All re-verify via normal access.)
- **Customer report & approval:** **DVX**: full RO + inspection + photos + recommendations ranked by urgency + out-the-door totals + approve/"Decline for Now" + signature + payment [DOC, marketing]. Shop notified when opened; viewer-logging fix for additional contacts (Apr 2026). **Approval capture** (opt-in, off by default, Jul 2024): in person = contact + signature; phone = contact + number; email = address; stored in **Authorization Summary, not in PDFs unless ticked**; CA BAR "Write it Right"-format summary available. Optional block on job start until signed. (Re-verify via normal access.)
- **Owner audit data:** Technician Report (efficiency, productivity, parts); unfulfilled-recommendations export; public API (re-verify via normal access). Inspection KPI report [UNVERIFIED]. Vendor-reported: median share rate 56%, close rate ~56% with DVX.
- **Pitfalls:** two color scales (2.14); white urgency = none stated; advisor-written/AI-rephrased text (2.7); swipe-to-green (2.3); Authorization Summary missing from consumer PDFs (2.15).
- **Doc quality:** public but thin on inspection mechanics. **Src:** [46]–[61], [182], [183].

#### AutoVitals (DVI/workflow add-on on top of a POS)
- **Structure:** Inspection Sheet → Sections → Topics → Conditions → Actions. Library of prebuilt sheets searchable by the shop that built them; customer-facing "Friendly Name" (2025). Topic options: mandatory before submit, **image required**, auto-open caption editor, alert advisor. Condition options: **Default Status, Default Action, Default Customer Note, Default Image Caption**, educational note/video ("Why is this important"), Guided Mode skip settings. Tablet inspections can start before an RO and match **by VIN**.
- **Grading:** shop-defined statuses (name/color/icon) each mapped to Good (only one) / Needs Future Attention / Requires Immediate Action / **Hidden**. CRM treats any status containing "future" as future attention. **Tapping a Condition applies status, action, note and caption at once** — color follows the canned condition, not a measured value (2.8). Carry Forward Confirm (2.4).
- **Measurements:** measurement fields exist; advisors review/edit/approve them ("untouched" filter) [field details UNVERIFIED]. **Groove Glove** tread scanner: tire topics must map to axle and Conditions (edge wear → alignment condition); unconfigured → **no data appears**; notes arrive **unapproved**; matched by VIN. **Hunter Quick Check/WinAlign**: tread, alignment, battery, diagnostic per topic; shows only if mapped topic has a condition selected and VIN entered; **customer view shows only after-alignment values**, shop view also before. Midtronics direct integration [UNVERIFIED].
- **Media:** photos **auto-approved and visible** unless hidden or deleted; editor with arrows, circles, text, crop, rotate, suppressor. **Move/copy photos between topics, work order or another open RO; move whole inspection to another RO** (2.5). PDFs (2025). Upload from advisor web screen. Customer images always show **date**; time-of-day only if shop enables it. Photo best practice: plate/front, 4 corners, VIN tag, cluster with mileage, fluids on drip tray, brake-fluid moisture test, battery test results, 4 treads + size, brake lining if yellow/red.
- **Finding → estimate:** Actions = POS canned jobs (synced ~2 h) or text. **Default Action recommends every time**; Selectable optional. "UPDATE WO" pushes to POS (e.g., Tekmetric) as **unapproved labor lines** with notes, photos and inspection URL; Tekmetric Smart Canned Jobs look identical to standard ones. CRM reminder modes: declined only / unsold recommendations / all "Needs Immediate Attention" (may include work already done). Declined-job data depends on POS fields; post-close changes not detected. **Otto Notes** AI (Feb 2026) (2.7).
- **Customer report & approval:** "Inspection Results" link; 3 templates; up to 4 "Offerings" (promos/financing); results grouped by status; optional "Services Being Performed". **Template changes restyle historical links** (2.10). Tech notes hidden until moved/approved; note-conflict icon. Stock car-with-stethoscope image if no vehicle photo. Approval via host POS [INF].
- **Owner audit data:** **BCP**: Inspection Rate, Sent Rate (repeat visits within 2 weeks excluded), Avg Pictures per RO, **Edited Pictures per Inspection**, Avg Recommended Jobs per Inspection, Recommendation Rate (canned jobs only), Avg Customer Research Time, Canned Jobs Approved, Jobs Completed on Tablet, Groove Glove Inspection Rate. Close-date, closed-RO, highest-revision counting (2.17). **Built-in audit tool**: rate images 0–5 (focus, arrow/circle, caption names part, caption names service, reason to buy today); suggests 2 inspections per staff per pay period; deactivated inspections hidden unless included. Historical URL after leaving; POS-embedded links stop.
- **Pitfalls:** canned conditions (2.8); moved/copied media (2.5); auto-approved photos; Carry Forward (2.4); Hidden status (2.6); unreviewed Groove Glove notes may not match graphics; Hunter before-values omitted; over-inclusive reminders (2.14); retroactive restyling (2.10).
- **Doc quality:** deep, current. **Src:** [62]–[85], [185].

#### Bolt On Technology (DVI/communications add-on; Performant Capital since 2021)
- **Profile:** "Mobile Manager Pro" DVI (2013); "NextGear" standalone web DVI; ~25 POS integrations claimed (incl. Protractor 2021, Mitchell 1, NAPA TRACS); AI phone advisor "MILES" (not DVI); new iOS app (2026).
- **Structure:** customizable inspections from tire report to 50-point; canned notes and recommendations [DOC, marketing]; builder details [UNVERIFIED].
- **Grading:** green good / yellow OK or non-urgent / red urgent [DOC]. Thresholds, bulk-rate [UNVERIFIED].
- **Measurements:** none documented.
- **Media:** photos/video on mobile; vendor says timestamped visual record per inspection; offline then sync; image markup ("graphics"). Per-item linkage [UNVERIFIED].
- **Finding → estimate:** canned jobs speed estimates; POS mapping [UNVERIFIED].
- **Customer report & approval:** text/email; approval from phone; tablet signature capture [DOC]. Layout [UNVERIFIED].
- **Owner audit data:** "Reporting" module; metrics [UNVERIFIED].
- **Pitfalls:** Bolt On's own list (Apr 2026) — unprioritized findings, poor photos, inconsistent tech standards, "problems-only" reports — doubles as an audit checklist.
- **Doc quality:** minimal (customer-portal help desk); many [UNVERIFIED]. **Src:** [86]–[96], [188].

#### Integrations and add-ons (independent)
- **AutoVitals ↔ Tekmetric** (two-way, Aug 2023): pushes VIN, odometer, tech, recommended canned jobs (unapproved), customer notes/photos, inspection URL; nothing sent until advisor clicks UPDATE WO [DOC].
- **AutoFlow → Tekmetric** (2023): only green/yellow/red items appear; **markups don't carry over** — the same inspection can look different in each system [DOC].
- **Shopgenie** (Tekmetric, Oct 2024) and **Steer** (Shop-Ware API partner): CRM/marketing, not DVI; may originate declined-work reminders.

### 3B. Legacy independent platforms

#### Mitchell 1 Manager SE + Manager SE Inspections (Snap-on)
- **Structure:** native MPI **launched Sept 2025**, auto + Truck Edition (Class 4–8). Service-specific reusable templates; **techs mark only problem items** [DOC]. Earlier: ProSpect mobile app (~2018; graded tire health from tread with shop rules) [3P] or third-party DVIs (certified list [UNVERIFIED]).
- **Grading:** G/Y/R; **unmarked items can default to green** (2.3) [DOC]. "Stored notes" can trigger red/yellow from details or measurements [DOC].
- **Measurements:** only as stored-note triggers; tire-by-position / brake-mm fields [UNVERIFIED]. ProSpect had before/after pressure [3P].
- **Media:** photo, video, notes, annotation per item [DOC]; timestamps [UNVERIFIED].
- **Finding → estimate:** flagged items **auto-become job containers** in Job View; Workshop View alerts advisor when "inspected" [DOC]. ProDemand (integrated since 2013) supplies labor, parts, OEM maintenance by time/mileage and indicator lights, one-click into RO (2.2 mixing risk [INF]). Severe vs normal handling [UNVERIFIED].
- **Customer report & approval:** branded report by text/email with annotated photos, video, notes; line-item approve/decline via secure link; deferred work stored [DOC].
- **Owner audit data:** RO, history, reporting; fleet integration (FleetNet America, 2021). Inspection exports [UNVERIFIED].
- **Pitfalls:** default-green; shop-defined thresholds vary or are absent; every flagged item becomes a priced job without triage; new product → template immaturity, many shops still run a third-party DVI [INF].
- **Doc quality:** medium (press materials). **Src:** [98]–[104].

#### ALLDATA Manage Online + ALLDATA Inspections (AutoZone)
- **Structure:** Vehicle Inspection > Inspection Setup: List > Categories > Items > optional Sub-items. Lists can be **linked to symptoms**. Footer text ≤350 chars (ALLDATA advises checking state requirements). App launched Oct 2022 (6 templates); now 10 prebuilt + visual check-in damage template [DOC].
- **Grading:** Manage Online: condition checkbox. App: **Red / Amber / Green / N/C (Not Checked)** + **Inspection Reason Codes** [DOC].
- **Measurements:** items flagged "Tire?" get **Outer / Middle / Inner tread in mm**; sub-items can have Value/Unit (e.g., "3mm") [DOC]. Optional; no auto-grading documented [INF].
- **Media:** photos per line item (app) [DOC].
- **Finding → estimate:** items pre-linked to **custom jobs suggested on failure**; Red/Amber shows them, including a **generic empty job** for tracking (2.1). Suggested job = shop configuration, not tech judgment [INF].
- **Customer report & approval:** email, text, print, PDF. **PDF "View" omits sub-items**; "Print inc sub items" shows them (2.10) [DOC].
- **Owner audit data:** Inspection Search; lists Open (uninvoiced) / Complete (invoiced) [DOC].
- **Pitfalls:** mm vs 32nds confusion (3 mm ≈ 3.8/32"); N/C items overlooked; Manage Online without the Inspections subscription may produce paper/plain checklists.
- **Doc quality:** high (best public docs in legacy/dealer group). **Src:** [113]–[116].

#### Protractor
- **Structure:** native web DVI **Oct 2023**, "color-coded templates"; mileage/VIN editable on inspection screen; VIN scanner (2D/OCR) [DOC]. Third-party DVIs integrate (Bolt On, Autoflow). Ownership [UNVERIFIED].
- **Grading:** color-coded; definitions [UNVERIFIED].
- **Measurements:** not published.
- **Media:** images, video, descriptions per inspection [DOC].
- **Finding → estimate (Autoflow integration):** **Red or Yellow auto-adds the mapped service package** to work order, or to Deferred Services if enabled; mapping by exact "SMS Code" [DOC] (2.1).
- **Customer report & approval:** shared digitally; channel not published.
- **Pitfalls:** every yellow can become a priced line; wrong package code attaches wrong service/labor [INF].
- **Doc quality:** medium. **Src:** [95], [108]–[110].

#### RO Writer
- **Structure:** DVI Suite → RO Writer DVI (Cloud), GA **Feb 2025**; vendor "best-practice" checklists; mobile-responsive [DOC]. Perseus Group / Constellation since 2021 (TBC-owned 2012–2021; Midas history).
- **Grading / measurements:** not published [UNVERIFIED].
- **Media:** photos and video of concerns, texted/emailed [DOC].
- **Finding → estimate:** results sync into RO Writer; mechanics not published.
- **Owner audit data:** [UNVERIFIED].
- **Pitfalls:** franchise/tire-chain shops may run older on-premise builds with third-party DVIs [INF].
- **Doc quality:** low–medium. **Src:** [105]–[107].

#### NAPA TRACS (with AutoServe1)
- **Structure:** **AutoServe1** = NAPA AutoCare's preferred DVI, embedded in TRACS with two-way integration and one-click toggle; packages ~$68–$258/month incl. TRACS Enterprise [DOC; pricing may be stale]. Autoflow also integrates. Legacy "DVVI" tablet app status [UNVERIFIED].
- **Grading / measurements / media:** not detailed on NAPA pages [UNVERIFIED].
- **Finding → estimate:** advisor builds estimate while tech inspects; findings become recommendations [DOC].
- **Customer report:** AutoServe1- or NAPA-branded. AutoServe1's RO-increase claims (22%/23%/25%) inconsistent across its pages — marketing.
- **Doc quality:** low–medium. **Src:** [91], [111], [112].

#### Shop Boss (BOSS Inspect)
- Native DVI; two-way customer communication; images, notes, estimates; MOTOR and ProDemand labor inside the inspection; unlimited canned jobs; custom inspection fields; text/email link to view RO and approve; BOSS Pay [3P]. Grading, measurements [UNVERIFIED].
- **Doc quality:** low. **Src:** [117], [118].

#### ARI (Auto Repair Software)
- Low-cost cloud/mobile app for small and mobile mechanics (~$39.99/mo); basic DVI with claimed "AI damage detection", VIN/plate decode, DTC/TSB, labor times; email delivery [3P]. Grading [UNVERIFIED]. Expect narrative findings, no measurement fields [INF].
- **Doc quality:** low. **Src:** [119], [120].

### 3C. Dealer platforms

Dealer DMS vendors publish little user-level MPI documentation; much below comes from press releases, OEM-partner pages, and the Dominion help center (generic pattern).

#### CDK Global (CDK Inspect / CDK Service / Fixed Operations Suite)
- **Structure:** CDK Inspect standardizes the MPI and feeds the DMS in real time; redesigned UI 2021; suite extended to non-CDK DMS dealers [DOC/3P]. No CDK product named "Service Edge" found [UNVERIFIED].
- **Grading / measurements:** not published; dealer G/Y/R, often from the OEM form [INF].
- **Media:** "interactive service videos", HD inspection video [DOC].
- **Finding → estimate:** CDK ServicePricing; in-bay parts availability; **Predictive Service (2026) adds AI-predicted items to the MPI** (2.11) [DOC].
- **Customer report & approval:** Mobile Approvals by text/email; eSignature; Vehicle Tracker [DOC].
- **Pitfalls:** predicted-not-observed lines; June 2024 ransomware gap (2.17). Brookfield ownership since Jul 2022 [3P]. Dealer-FX is **not** CDK (Snap-on; integrates via Fortellis).
- **Doc quality:** low–medium. **Src:** [121]–[124], [189].

#### Reynolds and Reynolds (ERA-IGNITE, Advanced Service, eApproval, Service Flex)
- **Structure:** **Service Flex – Technician** (renamed 2025) iPad/phone MPI app; works only with ERA-IGNITE and Advanced Service. 2025 release: search **"Report Card Line Items" by opcode** — MPI lines tied to opcodes [DOC]. docuPAD is F&I, not inspection.
- **Measurements:** Hunter drive-through tire/alignment data auto-documented in MPI; **recommended services auto-added to the work order**; UVeye integration [DOC].
- **Media / estimate / approval:** techs send advisors recommended work with photos, video, pricing; **eApproval** sends vehicle health + priced recommendations + media to customer's phone [DOC].
- **Pitfalls:** machine recommendations without tech judgment (2.11); opcode lines may carry OEM menu pricing [INF].
- **Doc quality:** low–medium. **Src:** [125]–[131].

#### Cox Automotive Xtime Inspect
- **Structure:** digital MPI iOS/Android; dashboards/scoreboards for tech performance and inspection quality; integrates with Xtime Schedule, Cox products, third-party DMS (enhanced CDK integration add-on) [DOC].
- **Measurements:** Hunter tread depth auto-populates (since Feb 2021) [DOC].
- **Media:** photos, HD video; Service Multimedia Pro add-on [DOC].
- **Finding → estimate:** **Service Pricing** catalog add-on; **Service Financing** payment plans at approval [DOC].
- **Customer report & approval:** visual report, online approval before returning. Cox claims approvals in ~7 minutes, up to $144 more per RO (vendor).
- **Owner audit data:** approval rate, engagement, RO revenue [DOC].
- **Pitfalls:** financing at approval may push bundling of yellow items [INF]; reviews cite tedious setup [3P].
- **Doc quality:** medium. **Src:** [132]–[134].

#### myKaarma (ServiceCart Video MPI)
- Video-first MPI (HD, pause/resume, VIN scan); advisor sends recommendations as a **"cart"**; customer approves line by line with upfront pricing [DOC]. AI **"Tech Video Grader"** scores video clarity/completeness — **not diagnostic accuracy** [DOC/INF] (2.12). Ford-certified vMPI / Video Check partner (one of eight per vendor); Porsche digital MPI page; UVeye and TraXtion feed underbody/tire/body findings [DOC].
- **Doc quality:** medium. **Src:** [135]–[138].

#### Dealer-FX (Snap-on since Mar 2021)
- OEM-branded help portals (e.g., Nissan Technician Inspection) → OEM-specific configurations. **Visual MPI** (Feb 2021): QR-code video capture, no app, no storage on personal devices; RO details attach automatically; share by text/email [DOC].
- **Inspection-level media (e.g., "All Green" video) is not in the Inspection Report PDF**; recommendation-level media is; **"All Green" landing page** auto-sent if configured; admin toggle "Enable Media Capture" (formerly "Enable Inspection Cam") [DOC] (2.10). Audi Technician Video Walk-Around certified vendor (2022).
- **Doc quality:** medium [DOC]. **Src:** [139]–[143].

#### Tekion (Automotive Retail Cloud, ARC)
- MPI form and video on ARC mobile app; video and report can be **auto-sent**; **deferred-service follow-up dates set by severity** (implementation guide via search excerpt; PDF not parsed — re-read for severity tiers) [DOC, partial]. **Hunter** tire/alignment auto-added to MPI with sheet and media on RO; **UVeye** reports by text/email/portal [DOC]. Consumer portal: status, recommendations, approvals, media, payment [3P].
- **Doc quality:** low–medium. **Src:** [144]–[147].

#### Generic dealer DMS MPI pattern (Dominion help center; illustrative, not CDK/Reynolds/Tekion)
- Green = OK. Yellow/Red open a pop-up for **Op-Code, Concern, Correction, photo**. **Saving without text auto-adds a default concern.** On completion the "Multi-Point" button turns green and a PDF attaches for email/text/print [DOC].
- **MPI Results & Upsell Report:** per advisor, tech recommendations sold / deferred / voided and **"updates made by Advisors/Managers"** [DOC].
- **Implications [INF]:** boilerplate concern on yellow/red with no tech narrative (2.8); advisor edits after the tech (2.7) — ask for the tech's original MPI.
- **Src:** [148]–[150].

### 3D. Quick-lube and tire chains (public info only)

| Chain | What the check covers | Measured? | Thresholds / labels | Audit notes | Src |
|---|---|---|---|---|---|
| Valvoline Instant Oil Change | "18-Point Maintenance Check": fluids, filters, lights, wipers, battery, tire pressure, under-chassis visual (lists vary) [3P] | Reportedly **does not measure tread depth** (FAQ didn't render; relayed via search excerpt) [partly UNVERIFIED] | — | Recommendations typically filters, wipers, fluid services by mileage [INF]. Bought Breeze Autocare; FTC ordered 45-shop divestiture (Nov 2025). Report format (digital vs print) [UNVERIFIED] | [167], [168] |
| Jiffy Lube | Signature Service **visual** checklist used to plan "manufacturer recommended maintenance" [DOC]; 17-point per job posting [3P] | Visual | — | NBC LA 2006: services billed not performed; Honda-attributed fuel-injection cleaning Honda didn't recommend [3P]. CBC Marketplace quick-lube upselling (transmission flushes, air filters) [3P] | [169]–[171] |
| Discount Tire | Free tread, wear pattern, DOT age, pressure, damage checks | Tread yes | Replace at **4/32"**; replace at 6 yrs from manufacture; no service ≥10 yrs; guidance supplements manufacturer's. A blog post says 3/32" (inconsistency) [DOC] | 4/32" is store policy, more conservative than 2/32" legal minimum in many states — not a legal requirement | [172], [173] |
| Les Schwab | "Safety Status Check": Checked and OK / **May Require Follow-Up Attention** (yellow) / **Requires Immediate Attention** (red) | Tires and alignment **visual**; brakes pad/shoe **gauge**; battery **load test** [DOC] | 3-tier OEM-style | Free brake check with **printed** report | [174], [175] |

### 3E. Fleet

| Platform | Structure / grading | Failure → work | Quirks | Src |
|---|---|---|---|---|
| Fleetio | Forms with pass/fail, drop-down, photo-required items; configurable [DOC] | Failed item → **Issue** by default → Service Entry / Work Order / manual close | Failure can be "acknowledged" with no action; **passing later doesn't close the Issue**; next inspector can reject a resolution (new Issue) | [176], [177] |
| Whip Around | DVIR items OK / Defect + notes; signatures: driver, mechanic certification (repaired / no repair needed), next driver; form cites 3-month retention (49 CFR 396.11/396.13) | Defect → work order with labor/parts (**Pro tier**) | Samsara defects can flow in | [178], [179] |
| Samsara DVIR | DVIR status Safe / Unsafe / Resolved; per-defect resolution; mechanic signature when all resolved | — | **Unresolved defects carry over** to next DVIR; DVIR status separate from defect resolution (KB via excerpt) | [180] |

**Regulatory baseline (49 CFR 396.11):** covers service/parking brakes, steering, lights/reflectors, tires, horn, wipers, mirrors, coupling, wheels/rims, emergency equipment. Safety defects must be repaired and certified (or certified unnecessary) before operation; 3-month retention; no-defect reports not required; electronic allowed [181]. See `commercial-fleet.md`.

---

## 4. OEM MPI color conventions

| Source | Green | Yellow | Red |
|---|---|---|---|
| Ford Genuine Service ("Service Excellence") [151] | Checked and OK at this time | May require future attention | Requires immediate attention |
| Honda dealer (Casey Honda) [157] | Safe, meets factory standards | Attention needed in near future | Unsafe, immediate attention |
| Porsche dealer [158] | Checked and OK at this time | Future attention | Immediate attention |
| Kimoby (dealer vendor docs) [159] | Checked OK | May need future attention | Requires immediate attention |
| Les Schwab (tire chain, same pattern) [174] | Checked and OK | May require follow-up; increased wear | Requires immediate attention; significant wear |

- **Norm: three tiers; yellow = future, red = now.** Yellow priced as due today with no measurement or explanation departs from the convention [INF] → usually **Supported – optional**.
- **"OK at this time" is time-bound**; green is not a warranty to the next visit.
- **No public OEM numeric cut-offs** per color (brake mm, tread 32nds) found for Ford, GM, Toyota, Honda [UNVERIFIED]; likely in dealer-only guides. Third-party "Toyota" checklist claims 5/32" tread — unofficial [160].
- **Gauge color bands vary by tool** [162]: OTC pencil gauge green ≥8 mm / yellow 3–8 mm / red 0–3 mm; OTC heavy-duty gauge green ≥12 mm / yellow 6–12 mm / red <6 mm. A dealer's color can reflect the gauge or vendor default used. Owners' forum: same tread graded yellow by one tech, green by another [3P, 161].
- **OEM program pressures:** GM PASE counts MPVIs and menu presentations monthly from nightly closed-RO feeds; red/yellow MPVI items can carry opcodes; GM certifies Service Lane Tool vendors (Dealerlogix, Jun 2024); GM SAVI can capture MPVI data from OBD dongles [150], [155], [156]. Ford Commitment Program requires **video MPI ("Video Check")** from approved vendors (myKaarma, TruVideo, UpdatePromise, Dealerlogix/TCC, others; Vehlo support Apr 2026) [135], [153], [154]; Ford inspection point counts vary (83-point Canada vs 139-point Blue Certified third-party template) [152]. Audi Technician Video Walk-Around (Dealer-FX); Porsche digital MPI (myKaarma). These reward completion/menu counts → rubber-stamp risk (2.12).
- **Menu vs condition at dealers:** advisors largely commission-paid; brake-fluid condition and throttle-body carbon can't be visually confirmed in a standard MPI [3P, 166]. Apply the observed-vs-schedule labeling rule (2.2).

---

## 5. Audit playbooks

### 5.1 Consumer — what to ask for, by platform

**Always:** (1) identify the platform (section 1); (2) trace each estimate line to red / yellow / menu / nothing; (3) ask for the online link **and** the PDF, the full inspection (incl. N/A/hidden items), the technician's original notes, and the authorization record (method, time, price at approval); (4) save copies with date — links can be unshared or restyled; (5) treat yellow as "plan for later"; (6) for schedule items, compare with the owner's manual (normal vs severe).

**Measurements to request** for brake, tire, battery items: pad mm per position; tread per position with unit (32nds or mm); battery test printout (CCA measured vs rated).

| Platform | Specific asks |
|---|---|
| Tekmetric | Readings aren't structured — ask for numbers. "Was this red/yellow from Recommended Maintenance (mileage) or observed?" Ask for the internal check-in inspection and N/A/incomplete items. Videos don't print — ask for the link. Unannotated photo if markup obscures detail. |
| Shopmonkey | Ask for readings (none structured). Look in the "Recommended" block — not in total. Ask for authorization history if prices changed. |
| Shop-Ware | Ask for readings. Compare line color vs urgency color. Ask for the tech's original finding (advisor/AutoWrite may have rewritten). Ask for the Authorization Summary (not in PDF by default). |
| AutoVitals | Ask for measurement values and Groove Glove/Hunter printout (incl. before-alignment values). Check image date stamps and plate/VIN photo (media can be moved between ROs). Ask for tech notes (Otto Notes rewrites customer notes). Ask about Hidden items. |
| Mitchell 1 | Green may mean "not flagged" — ask which items were actually checked. Ask which lines are ProDemand schedule items vs inspection findings. |
| ALLDATA | Ask for "Print inc sub items" (positions). Convert mm (3 mm ≈ 3.8/32"). Ask about N/C items. |
| Protractor / ALLDATA / Mitchell 1 | Yellow may auto-convert to a priced job — ask why it's urgent. |
| CDK / Reynolds / Xtime / Tekion | Ask whether each line came from a physical finding, a Hunter/UVeye scan, or Predictive Service; ask a tech confirmed it. |
| Dealer-FX | Ask for the online Digital MPI — inspection-level video isn't in the PDF. |
| Dealer (any) | Ask for the tech's original MPI (advisors can edit); ask schedule vs observed for fluid/induction services. |
| Quick lube | Don't accept tire/brake verdicts from a visual check; ask for measured value; ask to see old filters. |
| Discount Tire | 4/32" is store policy, not law. |

### 5.2 Shop owner — built-in audit data

| Platform | Reports / audit columns |
|---|---|
| Tekmetric | Inspection Report (avg inspection time, avg findings, attachments, % sent/viewed, ARO/close ratio with vs without inspection; by tech/writer); Inspection History per vehicle; posted ROs only, internal excluded |
| Shopmonkey | Vehicle Inspections Detail (inspectors vs Completed By, Items Rated %, Avg Finding %, "Unassigned"); Summary (Orders with Inspection %, per-tech ARO) |
| AutoVitals | BCP (pictures/RO, edited pictures/inspection, recommendation rate, research time); built-in 0–5 image audit tool (2 per staff per pay period) |
| Shop-Ware | Unfulfilled-recommendations export; Technician Report (re-verify via normal access) |
| ALLDATA | Inspection Search (Open/Complete) |
| Xtime | Tech performance/inspection-quality dashboards; approval rate |
| Dealer DMS (Dominion pattern) | MPI Results & Upsell Report incl. advisor/manager edits |
| Fleetio / Samsara / Whip Around | Issue/defect trail vs WOs and invoices |

**Flag outliers:** very high Avg Finding % or recommendation counts; very short inspection times; few photos per red item; high all-green share on high-mileage vehicles; high advisor-edit counts.

### 5.3 Shop owner — configuration fixes

- **Require measurements:** AutoVitals topic "image required"/mandatory; Mitchell 1 measurement-triggered stored notes with documented thresholds; on Tekmetric/Shopmonkey/Shop-Ware (no fields) require readings in findings text and gauge photos. Document which gauge bands you use.
- **Remove default statuses:** AutoVitals Default Status/Default Action on Conditions; Mitchell 1 default-green (require explicit tap where possible); restrict Tekmetric Rate All Tasks and copy-prior-inspection; discourage Shop-Ware swipe-to-green.
- **Separate menu maintenance from condition findings:** review Tekmetric Recommended Maintenance defaults (Due Soon → not Red); label ProDemand/MOTOR/OEM-menu lines "per schedule"; keep yellows in Deferred, not Recommended — confirm Protractor/Autoflow, Tekmetric and Mitchell 1 integrations don't auto-push yellows; review mapping tables (canned jobs, package codes, ALLDATA suggested jobs) at least quarterly.
- **Review AI-rewritten text:** check Otto Notes (opt-out available), Shop-Ware AutoWrite and "save as draft" permissions; compare against tech notes; use AutoVitals note-conflict icon.
- **Restrict photo moving:** limit AutoVitals move/copy media and move-inspection permissions; enable image timestamps in customer view; require plate/VIN/cluster photos.
- **Machine/AI items** (Hunter, UVeye, CDK Predictive Service): require tech confirmation before pricing.
- **Stronger approval records:** Tekmetric require digital signature; Shop-Ware approval capture + Authorization Summary in PDFs; Shopmonkey reset authorization on price increase.
- **Track advisor edits** to tech recommendations (upsell/sold reports).

### 5.4 Fleet manager

- Reconcile vendor DVI and invoice lines against your DVIR/Issue trail (Fleetio, Samsara, Whip Around).
- Flag vendor work on items drivers/techs reported OK, unless measurements are supplied.
- Check 396.11 repair certification before return to service; watch acknowledged-but-unrepaired (Fleetio) and carried-over (Samsara) defects.
- Put thresholds in the vendor agreement: tread 4/32" steer, 2/32" drive under FMCSA (see `commercial-fleet.md`), brake mm, battery test standard. Require vendor exports, not just PDFs.

---

## 6. Sources

**Tekmetric**
1. https://support.tekmetric.com/hc/en-us/articles/360037472174-Creating-Inspections
2. https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection
3. https://support.tekmetric.com/hc/en-us/articles/16773448793751-Mark-Inspections-as-Default
4. https://support.tekmetric.com/hc/en-us/articles/1500011364982-Link-Canned-Jobs-to-Inspections
5. https://support.tekmetric.com/hc/en-us/articles/35205687782423-DVI-Enhancements-That-Drive-Impact
6. https://support.tekmetric.com/hc/en-us/articles/42955960801943-Recommended-Maintenance-on-DVI
7. https://support.tekmetric.com/hc/en-us/articles/41093244754199-Recommended-Jobs
8. https://support.tekmetric.com/hc/en-us/articles/34327534094871-DVI-Image-Markup
9. https://support.tekmetric.com/hc/en-us/articles/9864603066519-Inspection-Report
10. https://support.tekmetric.com/hc/en-us/articles/18139709709719-Internal-Inspections
11. https://support.tekmetric.com/hc/en-us/articles/5178699794455-Digital-Vehicle-Inspection-History
12. https://support.tekmetric.com/hc/en-us/articles/4421125978391-Digital-Signature-Authorization-Process
13. https://support.tekmetric.com/hc/en-us/articles/360039270153-What-is-the-difference-between-declined-jobs-draft-jobs
14. https://support.tekmetric.com/hc/en-us/articles/360056145094-How-Do-I-Add-Previously-Declined-Work-to-a-Repair-Order
15. https://support.tekmetric.com/hc/en-us/articles/44090257340311-Mobile-App-What-s-New
16. https://support.tekmetric.com/hc/en-us/articles/360063488693-Labor-Guide
17. https://support.tekmetric.com/hc/en-us/articles/25868623867927-ALLDATA-Labor-Guide-Integration
18. https://support.tekmetric.com/hc/en-us/articles/27373807531287-Smart-Jobs-101
19. https://support.tekmetric.com/hc/en-us/articles/360035798334-Estimate-and-Invoice-Transparency-Settings
20. https://support.tekmetric.com/hc/en-us/articles/25416840474135-Adjust-Verbiage-for-Inspection-Estimate-Invoice-Texts
21. https://support.tekmetric.com/hc/en-us/articles/36897066105111-The-Customer-Concern
22. https://support.tekmetric.com/hc/en-us/articles/17119553542167-Tire-DOT-Management-in-Tekmetric
23. https://support.tekmetric.com/hc/en-us/articles/360041785434-Release-Date-Feature-Notes
24. https://www.ratchetandwrench.com/news/article/55370320/tekmetric-unveils-new-platform-innovations-at-tektonic-2026
25. https://www.axios.com/pro/retail-deals/2024/10/16/tekmetric-acquires-shopgenie-auto-repair

**Shopmonkey**
26. https://support.shopmonkey.io/hc/en-us/articles/38743049848852-Perform-Inspections
27. https://support.shopmonkey.io/hc/en-us/articles/38743088738452-Inspection-Templates
28. https://support.shopmonkey.io/hc/en-us/articles/38743122026388-Inspections-in-Shopmonkey-for-Techs-Mobile-App
29. https://support.shopmonkey.io/hc/en-us/articles/38744430526612-Send-Inspections-to-Customers
30. https://support.shopmonkey.io/hc/en-us/articles/47883995635476-Customer-E-Signatures-on-Inspections
31. https://support.shopmonkey.io/hc/en-us/articles/38743424357652-Customer-E-Signatures-to-Authorize-Services
32. https://support.shopmonkey.io/hc/en-us/articles/38743372579988-Request-Customer-Authorization
33. https://support.shopmonkey.io/hc/en-us/articles/38742880884756-Recommend-Services-on-an-Estimate
34. https://support.shopmonkey.io/hc/en-us/articles/38743421091988-Deferred-Services
35. https://support.shopmonkey.io/hc/en-us/articles/38743018176148-Manage-Inspection-Quick-Notes
36. https://support.shopmonkey.io/hc/en-us/articles/44632017228948-Vehicle-Inspections-Detail-Report
37. https://support.shopmonkey.io/hc/en-us/articles/44632022471060-Vehicle-Inspections-Summary-Report
38. DVI Master Series: https://support.shopmonkey.io/hc/en-us/articles/43553316659092 ; https://support.shopmonkey.io/hc/en-us/articles/43553515271572 ; https://support.shopmonkey.io/hc/en-us/articles/43553591811348 ; HQ templates https://support.shopmonkey.io/hc/en-us/articles/43357106322964
39. https://support.shopmonkey.io/hc/en-us/articles/38743045057172-Maintenance-Schedules
40. https://support.shopmonkey.io/hc/en-us/articles/46833875823124-ALLDATA-Integration ; https://support.shopmonkey.io/hc/en-us/articles/38743038698388-Vehicle-Parts-Labor-Lookup
41. https://support.shopmonkey.io/hc/en-us/articles/38743124485780-Shopmonkey-API
42. Improvements Apr 2026: https://support.shopmonkey.io/hc/en-us/articles/51946021436692
43. Improvements May 2026: https://support.shopmonkey.io/hc/en-us/articles/51950286356756
44. https://help.shopmonkey.io/en/articles/5564534-how-do-tires-work-in-shopmonkey
45. https://www.shopmonkey.io/demo-digital-vehicle-inspections

**Shop-Ware** (support.shop-ware.com items: re-verify via normal access)
46. https://support.shop-ware.com/s/article/What-is-TechApp-by-Shop-Ware
47. https://support.shop-ware.com/s/article/How-Do-I-Create-a-Recommendation
48. https://support.shop-ware.com/s/article/Recommendations-Urgency-Sorting-and-Viewing-Totals
49. https://support.shop-ware.com/s/article/Does-Shop-Ware-Capture-Recommendation-Approvals
50. https://support.shop-ware.com/s/article/Getting-Started-Repair-Orders-and-Appointments
51. https://support.shop-ware.com/s/article/API-Partner-Integrations
52. https://support.shop-ware.com/s/article/Are-You-Able-to-Track-Declined-Work-Or-Estimated-Work-per-Invoice-Can-You-Look-at-Daily-and-Weekly-Declined-Sales
53. https://support.shop-ware.com/s/article/If-a-Customer-Declines-Work-Will-Shop-Ware-Still-Send-an-Email-or-Text-Remind-Them-of-Needed-Work
54. Product Updates v10.10–v13.4 (2023–2026): https://support.shop-ware.com/s/product-updates
55. https://shop-ware.com/features/dvx/
56. https://shop-ware.com/features/dvx/digital-vehicle-inspection-vs-dvx/
57. https://shop-ware.com/features/techapp/
58. https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/
59. https://www.vehicleservicepros.com/industry-news/news/53099000/shop-ware-acquired-by-vehlo
60. https://support.shop-ware.com/s/article/What-is-the-Technician-Report-in-Shop-Ware
61. https://support.shop-ware.com/s/article/How-Can-A-Customer-Respond-to-a-Recommendation ; https://support.shop-ware.com/s/article/When-a-Client-Approves-Repairs-Online-Do-They-See-the-Total-Revised-Amount

**AutoVitals**
62. https://support.autovitals.com/hc/en-us/articles/4406522377876-AutoVitals-Inspection-Builder
63. https://support.autovitals.com/hc/en-us/articles/24804398734868-Starting-an-Inspection-from-the-Mobile-App-Tablet
64. https://support.autovitals.com/hc/en-us/articles/4415124929812-Recommendations-From-Inspections-on-TVP-X
65. https://support.autovitals.com/hc/en-us/articles/4416143388308-Recommendations-Declined-Jobs
66. https://support.autovitals.com/hc/en-us/articles/4418702821524-Timestamps-on-Customer-Inspection-Results
67. https://support.autovitals.com/hc/en-us/articles/4406164881556-How-to-Audit-Digital-Inspections-on-TVP-x
68. https://support.autovitals.com/hc/en-us/articles/12869672914708-Inspection-Results-Templates
69. https://support.autovitals.com/hc/en-us/articles/12869700549780-Offerings-on-Inspection-Results
70. https://support.autovitals.com/hc/en-us/articles/11734690213524-Historical-Inspection-Results
71. https://support.autovitals.com/hc/en-us/articles/4401760600340-Carry-Forward-AutoVitals-X-app
72. https://support.autovitals.com/hc/en-us/articles/4408845974420-The-Images-Notes-Editor
73. https://support.autovitals.com/hc/en-us/articles/4454837777172-Business-Control-Panel-Inspection-Data
74. https://support.autovitals.com/hc/en-us/articles/6535417910164-Business-Control-Panel-BCP-List-of-KPIs
75. https://support.autovitals.com/hc/en-us/articles/8754627477012-AutoVitals-DVI-Photo-Best-Practices
76. https://support.autovitals.com/hc/en-us/articles/5909835783956-How-To-Set-Up-Tire-Profiles-Groove-Glove-with-AutoVitals
77. https://support.autovitals.com/hc/en-us/articles/4414874909716-How-to-Set-Up-Hunter-Alignment-With-AutoVitals
78. https://support.autovitals.com/hc/en-us/articles/4410220960788-How-to-Move-an-Inspection-to-a-Different-RO-on-TVP-x
79. https://support.autovitals.com/hc/en-us/articles/27719371914388-AutoVitals-Basic-Training-6-Inspection-Editing
80. https://support.autovitals.com/hc/en-us/articles/27703698371476-AutoVitals-Basic-Training-8-Moving-Inspections-Photos
81. https://support.autovitals.com/hc/en-us/articles/17938877792404-Tekmetric-2-Way-Integration
82. https://support.autovitals.com/hc/en-us/articles/51041681108628-Using-Smart-Canned-Jobs-with-AutoVitals-Tekmetric-Integration
83. https://support.autovitals.com/hc/en-us/articles/37727459578516-Display-Jobs-Performed-on-Inspection-Results
84. https://support.autovitals.com/hc/en-us/articles/33931313088532-2025-Release-Notes
85. https://support.autovitals.com/hc/en-us/articles/46150691759124-Otto-Notes-AI-Powered-Customer-Notes

**Bolt On Technology**
86. https://www.boltontechnology.com/
87. https://blog.boltontechnology.com/what-are-digital-vehicle-inspections
88. https://blog.boltontechnology.com/optimizing-digital-vehicle-inspection-software
89. https://blog.boltontechnology.com/dvi-mistakes-that-kill-trust
90. https://lp.boltontechnology.com/mitchell-1
91. https://napatracs.com/extension/bolt-on-technology/
92. https://apps.apple.com/us/app/bolton-technology/id6755896971
93. https://en.wikipedia.org/wiki/Bolt_On_Technology (COI-flagged)
94. https://www.brakeandfrontend.com/bolt-on-technology-introduces-nextgear/
95. https://www.motor.com/2021/05/bolt-on-technology-now-integrates-with-protractor-shop-management-platform/
96. https://ratchetandwrench.com/sponsored-content/bolt-on-technology/article/11476185/an-inside-look-at-your-vehicle-2018-10-24
97. AutoFlow → Tekmetric (2023): https://autoflow.com/?p=21995446

**Mitchell 1**
98. https://mitchell1.com/?p=16796
99. https://www.aftermarketnews.com/mitchell-1-inspection-tool-launch/
100. https://autosphere.ca/mechanical/2025/09/09/mitchell-1-launches-manager-se-inspections-feature/
101. https://www.aftermarketnews.com/mitchell-1-announces-mobile-vehicle-inspection-solution/
102. https://www.moderntiredealer.com/industry-news/service/article/11509732/mitchell-1-integrates-manager-se-with-prodemand-2013-02-28
103. https://www.fenderbender.com/running-a-shop/finance/article/33034899/mitchell-1-introduces-prodemand-estimate-guide-enhancements
104. https://www.worktruckonline.com/news/mitchell-1-enhances-fleet-integration-in-shop-management

**RO Writer**
105. https://info.rowriter.com/blog/ro-writer-takes-dvi-to-the-cloud/
106. https://info.rowriter.com/software/solutions
107. https://info.rowriter.com/about-us/

**Protractor**
108. https://www.motor.com/2023/10/protractor-adds-digital-vehicle-inspection-and-vin-scanner/
109. https://autoflow.com/help-center/training/sms-training/protractor-integration-training/protractor-dvi-setup-and-administration/
110. https://www.aftermarketnews.com/bolt-on-technology-now-integrates-with-protractor-shop-management-platform/

**NAPA TRACS / AutoServe1**
111. https://partner.autoserve1.com/napa-tracs/
112. https://autoflow.com/napa-tracs/

**ALLDATA**
113. https://www.alldata.com/us/en/manage-online-article/setting-up-inspection
114. https://www.alldata.com/ca/en/support/manage-online/article/using-inspection-lists
115. https://www.alldata.com/ca/en/digital-vehicle-inspections
116. https://www.alldata.com/us/en/new=alldata-inspections-offers-fast-curbside-check-in-with-digital-inspections

**Shop Boss / ARI**
117. https://www.getapp.com/industries-software/a/shop-boss-pro/
118. https://www.capterra.com/p/121909/Shop-Boss-Pro/
119. https://apps.apple.com/app/id1189544427
120. https://www.getapp.ca/software/131559/ari

**CDK**
121. https://cdkglobal.com/cdk-inspect
122. https://www.businesswire.com/news/home/20210209005198/en/CDK-Global-Reimagines-Its-Service-Layered-Applications
123. https://www.autosuccessonline.com/cdk-fixed-operations-software-dealerships/
124. https://www.cdkglobal.com/fixed-ops/service/cdk-service

**Reynolds and Reynolds**
125. https://apps.apple.com/us/app/-/id6475359821
126. https://www.vehicleservicepros.com/industry-news/service-repair/company-association-news/news/21259834/hunter-engineering-announces-inspection-equipment-integration
127. https://www.uveye.com/reynoldsandreynolds
128. https://www.autodealertodaymagazine.com/369796/reynolds-unveils-expanded-service-offering-at-nada
129. https://platform.softwareone.com/product/eapproval/PCP-2371-1078
130. https://www.casestudies.com/company/reynolds-and-reynolds/case-study/bmw-of-tenafly-improves-service-trust-with-reynolds-and-reynolds
131. https://www.autodealertodaymagazine.com/news/penske-to-install-reynolds-docupad-in-all-stores

**Xtime**
132. https://xtime.com/solutions/inspect
133. https://www.fleetmaintenance.com/in-the-bay/shop-equipment/press-release/21211157/hunter-engineering-company-hunter-engineering-xtime-partner-to-integrate-inspection-products
134. https://www.capterra.com/p/187244/Xtime/reviews/

**myKaarma**
135. https://mykaarma.com/oems/ford/
136. https://mykaarma.com/news/mykaarma-selected-as-ford-dealer-technology-preferred-partner-for-video-capability/
137. https://mykaarma.com/blog/from-inspection-to-approval-streamlining-the-service-process-with-uveye-and-mykaarma/
138. https://mykaarma.com/?p=10188

**Dealer-FX**
139. https://www.businesswire.com/news/home/20210308005223/en/Snap-on-Acquires-Dealer-FX-Group-Inc.
140. https://help.dealer-fx.com/nissan/en-US/technician%20inspection/Content/RNotes/New%20Features%20MPImedia.htm
141. https://dealer-fx.com/visual-mpi-empower-technicians-with-integrated-video/
142. https://dealer-fx.com/dealer-fx-strengthens-integration-with-cdk-added-as-publisher-on-fortellis-automotive-exchange-platform/
143. https://dealer-fx.com/category/news

**Tekion**
144. https://go.tekion.com/hubfs/Tekion%20One%20-%20Implementation%20Guides/SVC-04.pdf
145. https://www.hunter.com/media-center/press-releases/hunter-engineering-and-tekion-partner-to-drive-customer-service-experience-plus-dealer-profitability/
146. https://tekion.com/blog/uveye-and-tekion-partner-to-enhance-the-dealership-customer-service-experience
147. https://tekion.com/blog/top-10-customer-experience-trends-in-automotive-industry-fixed-ops

**Generic dealer MPI (Dominion)**
148. https://help.dominiondms.com/en/knowledge/multi-point-inspections-mpi
149. https://help.dominiondms.com/en/knowledge/mpi-results-upsell-report
150. https://help.dominiondms.com/hubfs/2021%20VUE%20GM%20SLT%20and%20PASE%20Integration%20-%20USER.pdf

**OEM programs and conventions**
151. https://www.caribe.ford.com/en/abw/owners/genuine-service/service-excellence/
152. https://goaudits.com/checklist/ford-multi-point-inspection-checklist/913/122/
153. https://truvideo.com/ford-mpi-program/
154. https://secure.businesswire.com/news/home/20260427424905/en/Vehlos-Solutions-Now-Support-the-Requirements-of-the-Ford-Commitment-Program
155. https://www.businesswire.com/news/home/20240627793533/en/Vehlo%E2%80%99s-Dealerlogix-Becomes-Newest-Participating-Certified-Service-Lane-Tool-Partner-for-General-Motors
156. https://gm-techlink.com/?p=16273
157. https://www.caseyhonda.com/multi-point-inspection/
158. https://oklahomacity.porsche.com/en/service/multi-point-inspection
159. https://help.kimoby.com/multi-point-inspections
160. https://goaudits.com/checklist/toyota-multi-point-inspection-checklist/913/124/
161. https://www.toyotaownersclub.com/forums/topic/107157-do-different-mechanics-read-tread-depth-differently/
162. https://otctools.com/node/18673

**Industry failure modes**
163. https://digitaldealer.com/news/a-service-process-that-actually-makes-money-right-now/151974/
164. https://www.ratchetandwrench.com/columns/article/55366971/french-the-400-air-filter-why-your-mpi-process-is-restricting-profit
165. https://autoshopowner.com/forums/topic/19935-do-technicians-give-you-pushback-on-performing-the-multipoint-inspection
166. https://www.motor1.com/news/794085/toyota-dealership-service-scam/

**Quick lube and tire**
167. https://www.vioc.com/faq/what-is-included-in-safety-inspection
168. https://www.ftc.gov/news-events/news/press-releases/2025/11/ftc-requires-divestiture-oil-change-shops-valvoline-greenbriar-deal
169. https://assets1.jiffylube.com/auto-services/oil-change
170. https://www.nbclosangeles.com/local/is_your_mechanic_cheating/1852378/
171. https://www.aol.com/6-auto-repair-chains-accused-130050737.html
172. https://www.discounttire.com/learn/tire-safety
173. https://www.discounttire.com/blog/road-trip-checklist
174. https://www.lesschwab.com/article/safety-status-check-report.html
175. https://counter.lesschwab.com/brakes

**Fleet**
176. https://help.fleetio.com/en_US/inspections-item-failures
177. https://help.fleetio.com/en_US/inspections-overview
178. https://whiparound.com/wp-content/uploads/2026/08/Whip-Around-DVIR-Form-Template.pdf
179. https://www.samsara.com/ca/resources/marketplace/whip-around
180. https://kb.samsara.com/hc/articles/4406022633741
181. https://www.law.cornell.edu/cfr/text/49/396.11

**Other**
182. https://shop-ware.com/best-digital-vehicle-inspection-software/
183. https://support.shop-ware.com/s/article/Using-eCommerce-for-Estimates-and-Recommendations
184. https://support.tekmetric.com/hc/en-us/articles/26781766611351-Tekmetric-Mobile ; DVI guide (2023) https://tours.tekmetric.com/answers/digital-vehicle-inspection-guide
185. https://support.autovitals.com/hc/en-us/articles/45299274011540-2026-Release-Notes
186. https://support.shopmonkey.io/hc/articles/38744406930068
187. Shopmonkey updates Apr 2025 / Aug 2025 / other: https://support.shopmonkey.io/hc/en-us/articles/40018217207316 ; https://support.shopmonkey.io/hc/en-us/articles/42346343428628 ; https://support.shopmonkey.io/hc/en-us/articles/49055039153044
188. https://www.boltontechnology.com/products/digital-vehicle-inspections/
189. https://www.cbinsights.com/compare/cdk-global-vs-dealer-fx ; https://www.businesswire.com/news/home/20210308005223/en/Snap-on-Acquires-Dealer-FX-Group-Inc.
