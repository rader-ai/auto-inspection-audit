# 11. DVI / MPI Platforms: Legacy Independent, Dealership, Quick-Lube/Tire, and Fleet (Group B)

## 1. Scope and as-of date

- **As of:** 2026-10-20. Research used public web sources only: vendor product pages, public help centers, press releases, app-store listings, trade press, and review/forum content. No logins, demos, or contact with vendors.
- **In scope (Group B):**
  - Independent and legacy shop management: Mitchell 1 Manager SE (plus Manager SE Inspections and ProDemand links), RO Writer, Protractor, NAPA TRACS (with AutoServe1), ALLDATA Manage Online and ALLDATA Inspections, Shop Boss, ARI.
  - Dealership: CDK Global (CDK Inspect / CDK Service), Reynolds and Reynolds (Advanced Service, eApproval, Service Flex), Cox Automotive Xtime Inspect, myKaarma ServiceCart Video MPI, Dealer-FX (Snap-on), Tekion ARC, and the OEM-driven MPI programs from Ford, GM, Honda, and Toyota.
  - Quick-lube and tire chains: Valvoline, Jiffy Lube, Discount Tire, Les Schwab.
  - Fleet: Fleetio, Whip Around, Samsara DVIR.
- **Out of scope** (covered by the other researcher): Tekmetric, Shopmonkey, Shop-Ware, AutoVitals, Bolt On.
- **Evidence labels used below:**
  - **[DOC]**: stated in a vendor or official source.
  - **[3P]**: comes from a third-party listing, trade article, or review.
  - **[INF]**: my inference from the evidence.
  - **[UNVERIFIED]**: plausible, but I found no public source confirming it.
- **Key caveat:** Dealer DMS vendors (CDK, Reynolds, Tekion) publish very little user-level MPI documentation. Most dealer detail below comes from press releases, OEM-program partner pages, and one competitor DMS help center (Dominion) that shows the generic dealer MPI pattern.

### Product changes, 2021-2026

| Date | Change | Source |
|---|---|---|
| Mar 2021 | Snap-on bought Dealer-FX for about $200M. Snap-on also owns Mitchell 1. | https://www.businesswire.com/news/home/20210308005223/en/Snap-on-Acquires-Dealer-FX-Group-Inc. |
| 2021 | TBC Corporation placed RO Writer with Perseus Group, part of Constellation Software. | https://info.rowriter.com/about-us/ |
| Jul 2022 | Brookfield acquired CDK Global. | https://www.cbinsights.com/compare/cdk-global-vs-dealer-fx [3P] |
| Oct 2022 | ALLDATA Inspections launched as an add-on. | https://www.alldata.com/us/en/new=alldata-inspections-offers-fast-curbside-check-in-with-digital-inspections |
| Oct 2023 | Protractor launched its own native web DVI and VIN scanner. | https://www.motor.com/2023/10/protractor-adds-digital-vehicle-inspection-and-vin-scanner/ |
| Jun 2024 | A CDK ransomware attack disrupted dealerships, a reminder that dealer records may have gaps for that period. | https://www.cdkglobal.com/fixed-ops/service/cdk-service (context) [3P on details] |
| Jun 2024 | Dealerlogix (Vehlo) became a certified GM Service Lane Tool partner, with MPVI video and photos. | https://www.businesswire.com/news/home/20240627793533/en/Vehlo%E2%80%99s-Dealerlogix-Becomes-Newest-Participating-Certified-Service-Lane-Tool-Partner-for-General-Motors |
| Feb 2025 | RO Writer DVI moved to the cloud and became generally available. | https://info.rowriter.com/blog/ro-writer-takes-dvi-to-the-cloud/ |
| Sep 2025 | Mitchell 1 launched **Manager SE Inspections**, a native MPI inside Manager SE for auto and truck. | https://mitchell1.com/?p=16796 |
| 2025 | The Reynolds technician app was renamed **Service Flex - Technician**. | https://apps.apple.com/us/app/-/id6475359821 |
| Nov 2025 | The FTC required Valvoline to divest 45 shops as a condition of buying Breeze Autocare from Greenbriar. | https://www.ftc.gov/news-events/news/press-releases/2025/11/ftc-requires-divestiture-oil-change-shops-valvoline-greenbriar-deal |
| Apr 2026 | Vehlo said it supports Ford Commitment Program video-MPI requirements. Ford maintains an approved video-MPI ("Video Check") vendor list. | https://secure.businesswire.com/news/home/20260427424905/en/Vehlos-Solutions-Now-Support-the-Requirements-of-the-Ford-Commitment-Program |
| 2026 | CDK added AI "Predictive Service," which adds likely-failure items to the MPI. | https://cdkglobal.com/cdk-inspect |

- **Dealer-FX ownership:** Dealer-FX is **not** part of CDK. It integrates with CDK through Fortellis (https://dealer-fx.com/dealer-fx-strengthens-integration-with-cdk-added-as-publisher-on-fortellis-automotive-exchange-platform/), but Snap-on owns it.
- **"Service Edge":** I found no CDK product by that name. **[UNVERIFIED]**

---

## 2. Comparison table

Abbreviations: G/Y/R = green/yellow/red; N/C = not checked; RO = repair order.

| Platform | Segment | Native DVI? | Grading | Measurement-linked grade? | Media per item | Finding becomes estimate line | Customer delivery and approval | Confidence |
|---|---|---|---|---|---|---|---|---|
| Mitchell 1 Manager SE Inspections | Independent and truck | Yes (since Sep 2025) | G/Y/R. Unmarked items **default to green**. | Partly. Stored notes can set R/Y from "details or measurements." | Photo, video, annotations, notes | Items auto-create **job containers** in Job View. ProDemand supplies labor and OEM maintenance. | Branded report by text or email. Line-item approve/decline via secure link. | Medium [DOC] |
| RO Writer DVI (DVI Suite / Cloud) | Independent | Yes (add-on) | Not published [UNVERIFIED] | Not published | Photo, video | Synced to the RO | Text or email of photos and video | Low-medium |
| Protractor DVI | Independent and tire | Yes (since Oct 2023). Third-party DVIs also integrate. | Color-coded templates | Not published | Photo, video, notes | Red/Yellow items auto-add mapped services to the work order or Deferred Services (via the Autoflow integration) | Shared digitally. Channel not published. | Medium |
| NAPA TRACS + AutoServe1 | Independent (NAPA AutoCare) | Via embedded AutoServe1 | Not published on the NAPA pages | Not published | Photo (AutoServe1) | Advisor builds the estimate while the tech inspects. Two-way sync. | AutoServe1 report, NAPA or custom branded | Low-medium |
| ALLDATA Manage Online + ALLDATA Inspections | Independent | Yes (add-on subscription) | Red / Amber / Green / **N/C**, plus reason codes | Tire items capture Outer/Middle/Inner mm. Sub-items can hold numeric values. | Photo per line item | Red/Amber shows **pre-linked suggested jobs**, including a generic empty job | Email, text, or print. PDF. | High [DOC] |
| Shop Boss (BOSS Inspect) | Independent | Yes | Not published | Not published | Images, notes | Canned jobs. ProDemand and MOTOR labor in the inspection. | Text/email link to the RO for approval. BOSS Pay. | Low [3P] |
| ARI | Small independent / mobile | Yes (basic) | Not published | Not published | Photos. "AI damage detection" claimed. | Labor items, DTC/TSB lookup | Email | Low [3P] |
| CDK Inspect / CDK Service | Dealer | Yes | Not published. Dealer convention is G/Y/R. [INF] | Not published | Video ("interactive service videos") | DMS real-time integration, CDK ServicePricing, **AI Predictive Service adds items** | Mobile Approvals by text or email. eSignature. | Low-medium |
| Reynolds Advanced Service / eApproval / Service Flex | Dealer | Yes | "Report card" terminology appears | Hunter tire and alignment data auto-populates the MPI | Photos, video | Tech sends recommended work with pricing. Hunter recommendations auto-added to the RO. | eApproval to phone with pricing, photos, video | Low-medium |
| Xtime Inspect (Cox) | Dealer and independent | Yes | Not published. Dealer convention is G/Y/R. [INF] | Hunter tread depth auto-populates | Photo, HD video | Service Pricing catalog add-on | Online review and approval. Service Financing. | Medium |
| myKaarma ServiceCart Video MPI | Dealer | Video-MPI layer on the DMS | Ford vMPI-certified | n/a | Video-centric. AI "Tech Video Grader." | "Cart" of recommendations with upfront pricing | Text link. Line-by-line cart approval. | Medium |
| Dealer-FX (Snap-on) Technician Inspection / Visual MPI | Dealer (OEM-branded portals) | Yes | Not published. "All Green" landing page exists. | Not published | Recommendation-level and inspection-level media | Recommendations and concerns | Digital MPI message by text or email. Inspection Report PDF. | Medium [DOC] |
| Tekion ARC | Dealer | Yes (mobile MPI and video) | Severity used for deferred follow-up dates | Hunter tread and alignment auto-added. UVeye scans. | Photo, video | Within the ARC RO | Auto-send video and report. Consumer portal approval. | Low-medium |
| OEM programs (Ford, GM, Honda, Toyota) | Dealer | Run on dealer tools | G/Y/R: OK / future attention / immediate attention | OEM thresholds generally not public | Video increasingly required (Ford vMPI) | OEM maintenance menus. MPVI counts reported to the OEM (GM PASE). | Dealer tool | Medium |
| Valvoline / Jiffy Lube | Quick lube | POS checklist | Visual checklist | Valvoline says its check **does not measure tread depth** | Minimal | Manufacturer-schedule recommendations | In-lane, invoice | Low-medium |
| Discount Tire / Les Schwab | Tire | Store systems | Les Schwab: OK / May Require Follow-Up / Requires Immediate Attention | Discount Tire replaces at **4/32"**. Les Schwab gauges brakes. | Minimal | Tire and brake quote | Printed report (Les Schwab) | Medium |
| Fleetio | Fleet | Yes (forms) | Pass/Fail, drop-downs, photo requirements | Configurable | Photo | Failed item creates an **Issue** by default, then a WO or service entry | Internal | High [DOC] |
| Whip Around | Fleet DVIR | Yes | OK / Defect | n/a | Photo | Defect creates a work order (Pro tier). Mechanic certification. | Internal | Medium |
| Samsara DVIR | Fleet DVIR | Yes | Safe / Unsafe / Resolved; per-defect resolution | n/a | Photo | Unresolved defects **carry over** to the next DVIR | Internal | Medium |

---

## 3. Per-platform notes

### 3.1 Mitchell 1 Manager SE and Manager SE Inspections (Snap-on)

Manager SE is the largest legacy Windows shop-management system in this group. Mitchell 1 is a Snap-on company.

**1. How inspections are built**
- Manager SE Inspections launched September 2025 as an MPI built into Manager SE. It covers automotive and Manager SE Truck Edition (Class 4-8). https://mitchell1.com/?p=16796 ; https://www.aftermarketnews.com/mitchell-1-inspection-tool-launch/
- Shops create and reuse **service-specific templates**. Techs mark only problem items. [DOC]
- Before 2025, Manager SE relied on the older **ProSpect** mobile inspection app (around 2018) or third-party DVIs. ProSpect graded tire health from tread depth using shop-set rules. https://www.aftermarketnews.com/mitchell-1-announces-mobile-vehicle-inspection-solution/ [3P summary; direct page returned 403]
- Third-party DVIs also integrate. Which ones Mitchell 1 currently certifies is **[UNVERIFIED]**.

**2. Grading**
- Green, yellow, and red.
- **Everything not marked can default to green.** [DOC] This is the most important audit point for this platform:
  - A green item may only mean "not flagged," not "measured and within spec."
- "Stored notes" can be configured to **trigger red or yellow from details or measurements.** https://autosphere.ca/mechanical/2025/09/09/mitchell-1-launches-manager-se-inspections-feature/

**3. Measurements**
- Measurements are referenced only as triggers for stored notes. The public press materials do not detail tire-by-position or brake-mm fields. **[UNVERIFIED]**
- ProSpect had tire pressure before and after service, plus tread-depth rules. [3P]

**4. Photos and video**
- Photos, videos, and notes per item, with annotation, captured on phone or tablet. [DOC]
- Timestamps are not documented. **[UNVERIFIED]**

**5. Findings to estimate lines**
- Flagged items **automatically become job containers** in Job View for pricing. When the tech marks the inspection "inspected," Workshop View alerts the advisor. [DOC]
- Labor and parts usually come from **ProDemand** through the integration that has existed since 2013. ProDemand content (estimating, maintenance, fluids, TSBs) transfers into the open RO or estimate with one click. https://www.moderntiredealer.com/industry-news/service/article/11509732/mitchell-1-integrates-manager-se-with-prodemand-2013-02-28
- ProDemand's estimate guide presents OEM maintenance **by time and mileage intervals and by dashboard indicator lights**. https://www.fenderbender.com/running-a-shop/finance/article/33034899/mitchell-1-introduces-prodemand-estimate-guide-enhancements
- **Mixing risk [INF]:** One estimate can combine inspection-derived jobs with ProDemand interval maintenance pulled at the same mileage. Unless the advisor labels them, the customer cannot tell a condition finding from a schedule item.
- How Manager SE handles severe versus normal schedules is **[UNVERIFIED]**.

**6. Customer-facing report**
- A **branded** digital report by text or email, with annotated photos, video, and notes.
- Line-item approve/decline in real time through a **secure link**.
- Deferred work is stored for follow-up. [DOC]

**7. Exports and data**
- Manager SE has long-standing RO, history, and reporting functions, plus a fleet integration that receives service requests from fleet systems (FleetNet America, 2021). https://www.worktruckonline.com/news/mitchell-1-enhances-fleet-integration-in-shop-management
- Inspection-specific exports are **[UNVERIFIED]**.

**8. Pitfalls**
- **Default-green:** Uninspected points appear as green.
- Measurement-to-color rules live in shop-configured stored notes, so thresholds vary by shop and may be absent.
- Job containers are created automatically, so every flagged item can turn into a priced job without advisor triage.
- The product is new (2025). Expect template immaturity and mixed adoption: many shops still run a third-party DVI beside Manager SE. **[INF]**

**9. How to recognize the report**
- RO and invoice printouts with "Manager SE" style layout. ProDemand labor operation names often mirror the Mitchell 1 labor guide wording. **[INF]**
- The customer link domain was not found. **[UNVERIFIED]**
- The "Truck Edition" wording appears for heavy-duty work.

### 3.2 RO Writer

**1. How inspections are built**
- **DVI Suite**, now RO Writer DVI (Cloud), is an add-on that went generally available in the cloud in February 2025. https://info.rowriter.com/blog/ro-writer-takes-dvi-to-the-cloud/
- It ships with "best-practice" checklists and configuration settings that the vendor says industry experts created. Mobile-responsive checklists run on phone or tablet. [DOC]

**2. Grading and 3. Measurements**
- Neither is published. **[UNVERIFIED]**

**4. Photos and video**
- Photos and video of concerns. [DOC]

**5. Findings to estimate lines**
- Results sync into RO Writer. [DOC] Mechanics not published.

**6. Customer-facing report**
- Photos and video texted or emailed to the customer. https://info.rowriter.com/software/solutions

**7. Exports**
- **[UNVERIFIED]**

**8. Pitfalls**
- RO Writer has a long history as a Midas-owned product (TBC-owned 2012-2021), so franchise and tire-chain shops may run older on-premise builds and use third-party DVIs instead of the native one. https://info.rowriter.com/about-us/ **[INF]**

**9. How to recognize the report**
- "R.O. Writer" branding on the RO.
- DVI pages from older installs may come from a third-party DVI vendor. **[INF]**

### 3.3 Protractor

**1. How inspections are built**
- Native web DVI launched October 2023 with "color-coded templates." Mileage and VIN are editable from the inspection screen. A VIN scanner handles 2D codes and OCR. https://www.motor.com/2023/10/protractor-adds-digital-vehicle-inspection-and-vin-scanner/
- Third-party DVIs also integrate:
  - BOLT ON: https://www.aftermarketnews.com/bolt-on-technology-now-integrates-with-protractor-shop-management-platform/
  - Autoflow: https://autoflow.com/help-center/training/sms-training/protractor-integration-training/protractor-dvi-setup-and-administration/

**2. Grading**
- Color-coded. The definitions are not published. **[UNVERIFIED]**

**4. Photos and video**
- Images, video, and descriptions per inspection. [DOC]

**5. Findings to estimate lines (Autoflow integration)**
- When a DVI line item is marked **Red or Yellow**, the **mapped service package is added automatically** to the work order, or to **Deferred Services** if that option is enabled. Mapping uses an exact "SMS Code." [DOC, Autoflow]
- **Audit implication [INF]:** Every yellow, even a "monitor" item, can produce a priced line on the estimate. Look for yellow items that appear on the estimate as recommended now.

**8. Pitfalls**
- Template mapping errors: the wrong package code attaches the wrong service and labor to a finding. **[INF]**
- Protractor's ownership was not confirmed in this research. **[UNVERIFIED]**

**9. How to recognize the report**
- "Work Order" terminology plus Protractor branding. A "Deferred Services" list appears on later visits. **[INF]**

### 3.4 NAPA TRACS and NAPA AutoCare tools (AutoServe1)

**1. How inspections are built**
- **AutoServe1** is described as NAPA AutoCare's preferred DVI. It is **embedded within NAPA TRACS** with two-way integration and one-click toggling between the work order and the DVI. https://partner.autoserve1.com/napa-tracs/
- Packages run about $68-$258 per month and include NAPA TRACS Enterprise. [DOC; pricing may be stale]
- Autoflow also integrates with TRACS. https://autoflow.com/napa-tracs/
- NAPA had an older tablet "DVVI" app. Its current status is **[UNVERIFIED]**.

**2-4. Grading, measurements, photos**
- Not detailed on the NAPA-specific pages. AutoServe1 grading details are **[UNVERIFIED]** in this research.

**5. Findings to estimate lines**
- The advisor builds the estimate while the tech inspects, and findings become recommendations. [DOC]

**6. Customer-facing report**
- AutoServe1-branded or NAPA-branded report.
- AutoServe1's own claims for repair-order increases (22%, 23%, 25%) are inconsistent across its pages. Treat them as marketing.

**9. How to recognize the report**
- **NAPA AutoCare branding** on a DVI, often with AutoServe1 styling. NAPA branding is a package option. [DOC]

### 3.5 ALLDATA Manage Online and ALLDATA Inspections (AutoZone)

This platform has the best public documentation in Group B.

**1. How inspections are built**
- Setup path: Vehicle Inspection > Inspection Setup.
- Hierarchy: **List > Categories > Items > optional Sub-items**, each with a sort order.
- Lists can be **linked to symptoms**, so adding a symptom to a work document makes the linked inspection available.
- Optional footer text of up to 350 characters; ALLDATA advises checking state requirements.
- https://www.alldata.com/us/en/manage-online-article/setting-up-inspection
- The ALLDATA Inspections app launched in 2022 with 6 templates (maintenance, multipoint, A/C, brakes, steering/suspension/wheels/tires, pre-trip). The current page says 10 prebuilt templates plus a visual check-in damage template.
  - https://www.alldata.com/us/en/new=alldata-inspections-offers-fast-curbside-check-in-with-digital-inspections
  - https://www.alldata.com/ca/en/digital-vehicle-inspections

**2. Grading**
- In Manage Online, the tech checks a condition box. In the app, the choices are **Red / Amber / Green bubbles, or N/C (Not Checked)**.
- **Inspection Reason Codes** qualify a rating, for example part damage.
- https://www.alldata.com/ca/en/support/manage-online/article/using-inspection-lists

**3. Measurements**
- Items flagged **"Tire?"** get **Outer / Middle / Inner** tread fields **in millimeters**. [DOC]
- Sub-items can enable a **Value/Unit** field, for example "3mm."
- Measurements are optional. No auto-grading from measurements is documented. **[INF]**

**4. Photos**
- Photos are attached **by line item** in the app. [DOC]

**5. Findings to estimate lines**
- During setup, each item can be pre-linked to **custom jobs suggested when the item fails**.
- Marking Red or Amber displays those suggested jobs. The list includes a **generic job with no line items** for tracking.
- **Audit implication [INF]:** A suggested job reflects shop configuration, not tech judgment. Check that the job actually fits the finding.

**6. Customer-facing report**
- Email, text, or print.
- The PDF "View" shows the basic list and notes **without sub-items**. The full print offers "Print" or "Print inc sub items." [DOC]
- **Audit implication:** A customer PDF may omit sub-item detail, such as which position failed.

**7. Exports**
- Inspection Search. Lists show Open (uninvoiced) or Complete (invoiced). [DOC]

**8. Pitfalls**
- **Tread in mm, not 32nds.** Converting can confuse consumers: 3 mm is about 3.8/32".
- N/C items may be omitted or overlooked.
- Subscription gating: Manage Online users without ALLDATA Inspection may produce paper or plain checklists instead.

**9. How to recognize the report**
- "Red / Amber / Green" wording (**"Amber" rather than "Yellow"** is a useful tell). [DOC]
- N/C column, reason codes, and an ALLDATA footer text block. "Estimate" and "Repair Order" document types from Manage Online.

### 3.6 Shop Boss (BOSS Inspect)

- **Features:** Native DVI with two-way customer communication, reports with images and estimates, and notes. MOTOR and Mitchell1 ProDemand labor and diagnostic guidance can be added inside the inspection. BOSS Pay handles payment.
  - https://www.getapp.com/industries-software/a/shop-boss-pro/
  - https://www.capterra.com/p/121909/Shop-Boss-Pro/ [3P]
- **Canned jobs:** Unlimited canned jobs, plus custom fields for inspections. [3P]
- **Approval:** A text or email link lets the customer view the RO online and approve. [3P]
- **Grading:** Not published. **[UNVERIFIED]**
- **How to recognize the report:** "BOSS" product naming (BOSS Inspect, BOSS Pay) on payment or approval pages. **[INF]**

### 3.7 ARI (Auto Repair Software)

- **Profile:** Low-cost, cloud and mobile app for small and mobile mechanics. DVI with claimed "AI damage detection," VIN and plate decode, DTC/TSB info, and labor times. Plans start around $39.99 per month.
  - https://apps.apple.com/app/id1189544427
  - https://www.getapp.ca/software/131559/ari [3P]
- **Grading:** Not published. **[UNVERIFIED]**
- **Pitfall [INF]:** Very small shops on generic tools often have no measurement fields. Findings are mostly narrative.
- **How to recognize the report:** Simple invoice and estimate PDF layouts, often from a single owner-operator. **[INF]**

### 3.8 CDK Global (CDK Inspect / CDK Service / Fixed Operations Suite)

**1. How inspections are built**
- **CDK Inspect** standardizes the MPI and feeds the DMS in real time. It is part of the Fixed Operations Suite, which also offers eSignature and utilization reporting. https://cdkglobal.com/cdk-inspect
- In 2021, CDK Inspect was the first CDK Service app to get a redesigned UI. https://www.businesswire.com/news/home/20210209005198/en/CDK-Global-Reimagines-Its-Service-Layered-Applications
- The suite was extended to non-CDK DMS dealers. https://www.autosuccessonline.com/cdk-fixed-operations-software-dealerships/

**2-3. Grading and measurements**
- Not published by CDK. **[UNVERIFIED]**
- Dealer convention is green, yellow, and red, often driven by the OEM form. [INF]

**4. Photos and video**
- "Interactive service videos" and HD inspection videos. [DOC]

**5. Findings to estimate lines**
- CDK ServicePricing provides consistent pricing, and techs can check parts availability in the bay.
- **Predictive Service** uses history, analytics, and AI to identify components likely to fail and **adds them to the MPI**. [DOC]
- **Audit implication [INF]:** Some MPI lines may be **predicted, not observed**. Ask whether a line came from a physical finding or from the predictive model.

**6. Customer-facing report**
- **Mobile Approvals** by text or email. Vehicle Tracker shows real-time status. [DOC]

**8. Pitfalls**
- AI-suggested items.
- The June 2024 ransomware outage may have caused missing or paper MPIs at CDK dealers during that window. [INF]

**9. How to recognize the report**
- A CDK-style RO with dealer branding. Approval links come from the dealer's CDK messaging. The domain was not found. **[UNVERIFIED]**

### 3.9 Reynolds and Reynolds (ERA-IGNITE, Advanced Service, eApproval, Service Flex)

- **docuPAD is not an inspection tool.** It is an F&I tabletop product. https://www.autodealertodaymagazine.com/news/penske-to-install-reynolds-docupad-in-all-stores

**1. How inspections are built**
- **Service Flex - Technician** (renamed 2025) is an iPad and phone app for MPIs. It works only with **ERA-IGNITE and Advanced Service**.
- A 2025 release added searching **"Report Card Line Items" by opcode**. So Reynolds uses "report card" terminology, and MPI lines are tied to **opcodes**. https://apps.apple.com/us/app/-/id6475359821

**3. Measurements**
- Hunter drive-through tire and alignment data is documented automatically in the MPI. **Recommended services are added automatically to the work order.** https://www.vehicleservicepros.com/industry-news/service-repair/company-association-news/news/21259834/hunter-engineering-announces-inspection-equipment-integration
- UVeye scans also integrate. https://www.uveye.com/reynoldsandreynolds

**4-6. Media, estimate lines, and approval**
- Techs send advisors recommended work with photos, video, and pricing. https://www.autodealertodaymagazine.com/369796/reynolds-unveils-expanded-service-offering-at-nada
- **eApproval** sends vehicle health and recommended work, with pricing, photos, and video, to the customer's phone. https://platform.softwareone.com/product/eapproval/PCP-2371-1078
- A vendor case study (BMW of Tenafly) mentions videos and report cards. https://www.casestudies.com/company/reynolds-and-reynolds/case-study/bmw-of-tenafly-improves-service-trust-with-reynolds-and-reynolds

**8. Pitfalls [INF]**
- Machine-generated recommendations (Hunter, UVeye) land on the RO without a tech's judgment.
- Opcode-driven lines may carry OEM menu pricing.

**9. How to recognize the report**
- "Report Card" wording, opcodes on lines, and an ERA-IGNITE-format RO. **[INF/partly DOC]**

### 3.10 Cox Automotive Xtime Inspect

**1. How inspections are built**
- Digital MPI on iOS and Android with a "uniform" process. Dashboards and scoreboards track tech performance and inspection quality.
- Integrates with Xtime Schedule, other Cox products, and third-party DMSs. Enhanced CDK DMS integration is an add-on. https://xtime.com/solutions/inspect

**3. Measurements**
- Hunter tread depth auto-populates the inspection form (since February 2021). https://www.fleetmaintenance.com/in-the-bay/shop-equipment/press-release/21211157/hunter-engineering-company-hunter-engineering-xtime-partner-to-integrate-inspection-products

**4. Photos and video**
- Photos and HD video. The Service Multimedia Pro add-on extends capture. [DOC]

**5. Findings to estimate lines**
- **Service Pricing** add-on: a central, dealership-approved price catalog.
- **Service Financing** add-on: payment plans offered at approval. [DOC]

**6. Customer-facing report**
- Visual report with photos, video, and notes. The customer approves online, even before returning to the dealer.
- Cox claims approvals in as little as 7 minutes and up to $144 more per RO. These are vendor figures.

**7. Exports**
- Reports on approval rate, engagement, and RO revenue. [DOC]

**8. Pitfalls**
- Reviews describe tedious setup and slow support changes. [3P] https://www.capterra.com/p/187244/Xtime/reviews/
- Financing offers at approval can push customers toward bundling yellow items. [INF]

**9. How to recognize the report**
- Xtime-branded consumer pages under the dealer's name.
- The link domain is likely xtime.com-based. **[UNVERIFIED]**

### 3.11 myKaarma (ServiceCart Video MPI)

- **Video-first MPI:** HD video with pause and resume, and VIN scan from the tech's phone.
- **Delivery and approval:** The advisor sends recommendations as a **"cart."** The customer approves line by line on a phone, with upfront pricing. https://mykaarma.com/oems/ford/
- **AI "Tech Video Grader":** Scores each video for clarity and completeness before it goes to the customer. [DOC]
  - **Audit note [INF]:** The grader measures video quality, not diagnostic accuracy.
- **OEM status:** Ford-certified vMPI vendor and Ford Video Check partner, one of eight per the vendor (https://mykaarma.com/news/mykaarma-selected-as-ford-dealer-technology-preferred-partner-for-video-capability/). Porsche digital-MPI page also exists: https://mykaarma.com/?p=10188
- **Integrations:** UVeye and TraXtion feed underbody, tire, and body findings. https://mykaarma.com/blog/from-inspection-to-approval-streamlining-the-service-process-with-uveye-and-mykaarma/
- **How to recognize the report:** A "cart"-style approval page with per-line video thumbnails and prices. The domain was not found. **[UNVERIFIED]**

### 3.12 Dealer-FX (Snap-on)

- **Ownership and structure:** Snap-on acquired Dealer-FX in March 2021. It runs OEM-branded help portals, for example a **Nissan** Technician Inspection help site, which suggests OEM-specific configurations. https://help.dealer-fx.com/nissan/en-US/technician%20inspection/Content/RNotes/New%20Features%20MPImedia.htm
- **Visual MPI (February 2021):**
  - Techs record video through a QR-code flow, with no app download and no storage on personal devices.
  - RO details attach to the video automatically.
  - Advisors share by text or email.
  - https://dealer-fx.com/visual-mpi-empower-technicians-with-integrated-video/
- **Inspection-level vs recommendation-level media:**
  - **Inspection-level** media, such as an "All Green" video, is **not included in the Inspection Report PDF**.
  - An **"All Green" landing page** goes to the customer automatically if the dealer configures it.
  - The admin toggle "Enable Media Capture" was formerly "Enable Inspection Cam." [DOC]
  - **Audit implication:** The PDF and the online "Digital MPI" can differ in content.
- **Audi program:** Certified vendor for Audi's Technician Video Walk-Around program (2022). https://dealer-fx.com/category/news
- **How to recognize the report:** "Digital MPI" message, "Service Summary" page, "Inspection Report PDF," and OEM-branded styling (Nissan and others). [DOC]

### 3.13 Tekion (Automotive Retail Cloud, ARC)

- **MPI workflow:** Techs complete the MPI form and video on the ARC mobile app.
  - The inspection video and report can be **auto-sent** to customers.
  - **Deferred-service follow-up dates are set by severity.**
  - Source: the Tekion implementation guide (search-result excerpt; the 15 MB PDF could not be parsed locally): https://go.tekion.com/hubfs/Tekion%20One%20-%20Implementation%20Guides/SVC-04.pdf
- **Integrations:**
  - **Hunter** tire measurements and alignment are added to the MPI automatically, and the Hunter sheet and media attach to the RO. https://www.hunter.com/media-center/press-releases/hunter-engineering-and-tekion-partner-to-drive-customer-service-experience-plus-dealer-profitability/
  - **UVeye** reports reach customers by text, email, or the Tekion consumer portal. https://tekion.com/blog/uveye-and-tekion-partner-to-enhance-the-dealership-customer-service-experience
- **Customer portal:** Status, recommendations, approvals, photos and video, and payment. https://tekion.com/blog/top-10-customer-experience-trends-in-automotive-industry-fixed-ops [3P testimonial]
- **How to recognize the report:** A Tekion consumer portal page, with UVeye or Hunter sheets attached to the RO. **[INF]**

### 3.14 Generic dealer DMS MPI pattern (from Dominion DMS documentation; illustrative)

This public help center shows how dealer MPIs typically behave. It is *not* CDK, Reynolds, or Tekion.

- **Green** marks the item OK.
- **Yellow or Red** opens a pop-up for **Op-Code, Concern, Correction, and photo**.
- If the tech saves without text, a **default concern is added automatically**.
- On completion, the RO's "Multi-Point" button turns green, and a PDF is attached for email, text, or print.
- https://help.dominiondms.com/en/knowledge/multi-point-inspections-mpi
- **MPI Results & Upsell Report:** Counts, per advisor, the tech recommendations that were sold, deferred, or voided, and the "updates made by Advisors/Managers." https://help.dominiondms.com/en/knowledge/mpi-results-upsell-report
- **Audit implications [INF]:**
  - (a) Boilerplate "default concern" text can appear on yellow or red items with no tech narrative.
  - (b) Advisors can edit recommendations after the tech, so the customer version may differ from the tech's findings.

### 3.15 Quick-lube and tire chains (public info only)

**Valvoline Instant Oil Change**
- **What the check covers:** An "18-Point Maintenance Check" covering fluids, filters, lights, wipers, battery, tire pressure, and an under-chassis visual. Item lists vary by source. [3P]
- **Tread depth:** Valvoline's own page reportedly says the check does **not** measure tread depth. https://www.vioc.com/faq/what-is-included-in-safety-inspection (page did not render for me; claim relayed via search excerpt) **[partly UNVERIFIED]**
- **Recommendations:** Typically air and cabin filter, wipers, and fluid services by mileage. [INF]
- **Ownership:** Acquired Breeze Autocare in 2025 under an FTC divestiture order (see §1).

**Jiffy Lube**
- **What the check covers:** The Signature Service oil change includes a **visual** checklist used to plan "manufacturer recommended maintenance." https://assets1.jiffylube.com/auto-services/oil-change
- **Point count:** A job posting cites a 17-point inspection. [3P]
- **Historical upsell findings:**
  - A 2006 NBC LA hidden-camera test found services billed but not performed, and a fuel-injection cleaning attributed to Honda that Honda did not recommend. https://www.nbclosangeles.com/local/is_your_mechanic_cheating/1852378/
  - CBC Marketplace reported quick-lube upselling (transmission flushes, air filters). Cited via https://www.aol.com/6-auto-repair-chains-accused-130050737.html [3P]

**Discount Tire**
- **Free checks:** Tread, wear pattern, DOT age, pressure, and damage.
- **Thresholds:** Replace at **4/32"**. Replace at 6 years from manufacture. No service for tires 10 years or older.
- **Manufacturer guidance:** The store's guidance supplements, but does not replace, manufacturer guidance. https://www.discounttire.com/learn/tire-safety
- **Inconsistency:** A road-trip blog post says 3/32". https://www.discounttire.com/blog/road-trip-checklist
- **Audit implication:** Know which threshold the store applied, because 4/32" is more conservative than the 2/32" legal minimum in many states.

**Les Schwab**
- **"Safety Status Check":** Three statuses: Checked and OK, **May Require Follow-Up Attention** (yellow), and **Requires Immediate Attention** (red).
- **Coverage:** Tires and alignment are visual. Brakes include a pad and shoe **gauge** measurement. Battery gets a load test. https://www.lesschwab.com/article/safety-status-check-report.html
- **Brake check:** Free, with a **printed** report. https://counter.lesschwab.com/brakes
- **How to recognize the report:** The "Safety Status Check" title and the three-status icons.

### 3.16 Fleet (brief)

**Fleetio**
- **Forms:** Inspection forms with pass/fail, drop-down, and photo-requirement items.
- **Failures:** By default, **a failed item creates an Issue**. Users can instead "acknowledge" a failure with no action.
- **Resolution:** Issues are resolved only by a Service Entry, a Work Order, or manual close. **Passing an item later does not close an open issue.**
- **Re-inspection:** The next inspector can confirm or reject a resolution, and rejecting creates a new issue.
- https://help.fleetio.com/en_US/inspections-item-failures ; https://help.fleetio.com/en_US/inspections-overview
- **Fleet audit use:** Match vendor invoices to the Issue and WO trail. Watch for "acknowledged" failures that were never repaired.

**Whip Around**
- **DVIR:** Each item is OK or Defect, with notes.
- **Signatures:** Three blocks: driver, mechanic certification of repair or no repair needed, and next driver.
- **Retention:** The form cites 3-month retention under 49 CFR 396.11 and 396.13.
- **Work orders:** On the Pro tier, a defect can become a work order with labor and parts.
- **Integrations:** Samsara defects can flow to Whip Around.
- https://whiparound.com/wp-content/uploads/2026/08/Whip-Around-DVIR-Form-Template.pdf ; https://www.samsara.com/ca/resources/marketplace/whip-around

**Samsara DVIR**
- **Statuses:** Defects are resolved one by one, and the mechanic's signature shows when all are resolved.
- **Carry-over:** **Unresolved defects carry over to the next DVIR.**
- **Separate tracking:** DVIR status (Safe / Unsafe / Resolved) is tracked separately from defect resolution. https://kb.samsara.com/hc/articles/4406022633741 (via search excerpt; page returned 403)

**Regulatory baseline (49 CFR 396.11)**
- **Items covered:** Service and parking brakes, steering, lights and reflectors, tires, horn, wipers, mirrors, coupling, wheels and rims, and emergency equipment.
- **Repair certification:** The carrier must repair safety-affecting defects and certify the repair, or that repair was unnecessary, before the vehicle is operated again.
- **Retention:** 3 months.
- **No-defect reports:** Not required.
- **Format:** Electronic reports are allowed.
- https://www.law.cornell.edu/cfr/text/49/396.11

---

## 4. OEM MPI conventions

### 4.1 Color definitions as published by OEM-affiliated sources

| Source | Green | Yellow | Red |
|---|---|---|---|
| Ford Genuine Service ("Service Excellence") | Checked and OK at this time | May require future attention | Requires immediate attention |
| Les Schwab (tire chain, same pattern) | Checked and OK | May require follow-up; increased wear | Requires immediate attention; significant wear |
| Honda dealer (Casey Honda) | Safe, meets factory standards | Attention needed in the near future | Unsafe, immediate attention |
| Porsche dealer | Checked and OK at this time | Future attention | Immediate attention |
| Kimoby (dealer vendor docs) | Checked OK | May need future attention | Requires immediate attention |

Sources for the table:
- Ford: https://www.caribe.ford.com/en/abw/owners/genuine-service/service-excellence/ (search excerpt; direct fetch was 403)
- Les Schwab: https://www.lesschwab.com/article/safety-status-check-report.html
- Honda dealer: https://www.caseyhonda.com/multi-point-inspection/
- Porsche dealer: https://oklahomacity.porsche.com/en/service/multi-point-inspection
- Kimoby: https://help.kimoby.com/multi-point-inspections

**What this means for audits**
- **The industry norm is three tiers, with yellow meaning "future" and red meaning "now."** An estimate that prices yellow items as due today, without a measurement or explanation, departs from the OEM convention. [INF]
- **"OK at this time" is time-bound.** Green is not a warranty that the part will last until the next visit.
- **Numeric thresholds:**
  - I found **no public OEM-published numeric cut-offs** (for example, brake mm or tread 32nds per color) for Ford, GM, Toyota, or Honda. **[UNVERIFIED]**; these are likely in dealer-only OEM service-lane guides.
  - Third-party "Toyota" checklists claim 5/32" tread. Unofficial; https://goaudits.com/checklist/toyota-multi-point-inspection-checklist/913/124/
  - Brake gauge color bands vary by tool:
    - OTC pencil gauge: green 8 mm or more, yellow 3-8 mm, red 0-3 mm.
    - OTC heavy-duty gauge: green 12 mm or more, yellow 6-12 mm, red under 6 mm.
    - https://otctools.com/node/18673
  - **So the "color" a dealer assigns can depend on which gauge or vendor default the dealer uses.**
- **Consistency:** An owners' forum reports the same tread graded yellow by one tech and green by another at a Toyota dealer. Anecdotal, but it illustrates threshold variability. https://www.toyotaownersclub.com/forums/topic/107157-do-different-mechanics-read-tread-depth-differently/

### 4.2 OEM program pressures that shape MPI reports

- **GM:**
  - PASE counts MPVIs and maintenance-menu presentations by month. Closed ROs are sent to GM nightly through the DMS feed.
  - Red and yellow MPVI items can carry opcodes.
  - GM certifies "Service Lane Tool" vendors (for example Dealerlogix) for MPVI with video and photos.
  - Sources:
    - https://help.dominiondms.com/hubfs/2021%20VUE%20GM%20SLT%20and%20PASE%20Integration%20-%20USER.pdf (search excerpt)
    - https://www.businesswire.com/news/home/20240627793533/en/
  - GM's SAVI dashboard on GlobalConnect can also capture MPVI data from OBD dongles. https://gm-techlink.com/?p=16273
- **Ford:**
  - The Ford Commitment Program includes **video MPI ("Video Check")** with approved vendors: myKaarma, TruVideo, UpdatePromise, Dealerlogix/TCC, and others.
  - Sources: https://mykaarma.com/oems/ford/ ; https://truvideo.com/ford-mpi-program/ ; https://secure.businesswire.com/news/home/20260427424905/en/Vehlos-Solutions-Now-Support-the-Requirements-of-the-Ford-Commitment-Program
  - Ford's customer-facing inspection count varies: 83-point (Canada) versus a 139-point Blue Certified checklist (third-party template). https://goaudits.com/checklist/ford-multi-point-inspection-checklist/913/122/
- **Audi:** Technician Video Walk-Around preferred-provider program (Dealer-FX).
- **Porsche:** Digital MPI requirements (myKaarma page).
- **Implication [INF]:**
  - OEM programs reward **MPI completion and menu presentation counts**, so dealers have an incentive to complete an MPI on every RO and present maintenance menus.
  - That raises the risk of rubber-stamped ("pencil-whipped") all-green MPIs and of OEM-menu items being presented beside condition findings.

### 4.3 Menu maintenance vs condition findings at dealers

- **Motor1 coverage:** Advisors are largely commission-paid. Brake-fluid condition and throttle-body carbon **cannot be visually confirmed** in a standard MPI, and are usually time-and-mileage items. https://www.motor1.com/news/794085/toyota-dealership-service-scam/
- **Audit rule [INF]:** Every recommended line should carry one of two labels:
  - **(a) Observed condition**, with a measurement, photo, or test result, or
  - **(b) Schedule or menu interval**, citing the OEM schedule (normal vs severe).
  - Lines with neither are unsupported.

---

## 5. Common failure modes and detection

| # | Failure mode | Platforms where it is documented or likely | How to detect in a report |
|---|---|---|---|
| 1 | **Default-green / pencil-whipping:** uninspected items show green | Mitchell 1 (documented default-green); dealer MPIs generally (consultant reports of all-green MPIs on 275k-mile trucks: https://digitaldealer.com/news/a-service-process-that-actually-makes-money-right-now/151974/) | All items green with no measurements. Green on items the tech could not access, such as underbody on a lift-less express lane. Green brakes with no mm. Compare against the later invoice. |
| 2 | **Yellow auto-converts to a priced job** | Protractor/Autoflow mapping; Mitchell 1 job containers; ALLDATA suggested jobs; Reynolds/Hunter auto-added recommendations | A yellow ("future") item priced on today's estimate as recommended. Look for the "Deferred" vs "Recommended" split. |
| 3 | **Canned job mismatch:** the pre-mapped job does not fit the finding | ALLDATA (item-to-custom-job links); Protractor package codes | The job description is broader than the finding, for example a full brake job (pads, rotors, fluid, hardware) for a yellow pad reading. |
| 4 | **Boilerplate / default concern text** | Dealer DMS (Dominion auto default concern) | Identical concern wording across many lines or vehicles. No specific location or measurement. |
| 5 | **Machine-generated findings without tech verification** | Hunter/UVeye into Xtime, Tekion, Reynolds; CDK Predictive Service (AI-added items) | Lines that reference a scan or prediction. Tread or alignment values identical to a drive-over printout. Ask whether a tech physically confirmed the finding. |
| 6 | **Unit confusion** | ALLDATA tread in mm; Discount Tire 4/32" policy vs legal 2/32" | mm vs 32nds mix-ups. Store policy thresholds presented as legal or safety requirements. |
| 7 | **PDF vs online report divergence** | Dealer-FX (inspection-level media not in PDF); ALLDATA PDF view omits sub-items | Ask for both the online link and the PDF. Compare item counts and positions. |
| 8 | **Advisor edits after the tech** | Dealer DMS "updates made by Advisors/Managers" | Tech notes and customer-facing recommendations differ. Ask for the tech's original MPI. |
| 9 | **Menu and condition blending** | ProDemand interval maintenance in Manager SE; OEM menus at dealers; quick-lube "manufacturer recommended" | Interval items (fluid exchanges, fuel or induction cleaning) shown alongside condition findings, with no "per schedule" label or schedule citation. Check against the owner's manual. |
| 10 | **Visual-only check presented as measured** | Quick lube (Valvoline reportedly does not measure tread); Jiffy Lube visual checklist | Tread or brake conclusions from a shop that does not measure them. Ask for the measured value. |
| 11 | **Video quality ≠ diagnostic accuracy** | myKaarma AI Tech Video Grader; Ford vMPI | A polished video that does not show the measured condition, such as a gauge reading or the failed part. |
| 12 | **Carry-over / stale defects** | Samsara (unresolved defects carry over); Fleetio (passing doesn't close the issue) | The same defect reappears for weeks, or a repair is invoiced while the issue stays open. Reconcile the WO, issue, and invoice. |
| 13 | **Billed but not performed** | Quick-lube investigations (NBC LA 2006) | Fluid services with no before/after evidence. Filters billed with the old part not shown. |

---

## 6. Audit implications by audience

### Consumer
- **Identify the platform** from the report's tells (§3, item 9 in each subsection). This tells you what the shop's software made easy:
  - auto-converted yellows (Protractor, Mitchell 1, ALLDATA),
  - AI or scan-added items (CDK, Tekion, Reynolds, Xtime),
  - default-green (Mitchell 1).
- **Ask for both formats:** the online link *and* the PDF, plus the technician's original MPI.
- **Treat yellow as "plan for later"** under the published OEM convention. Ask why a yellow item is priced as urgent.
- **Require a measurement or photo** for brake, tire, and battery recommendations. Specifically:
  - brake mm for each position,
  - tread for each position in a stated unit (32nds or mm),
  - a battery test printout with CCA measured vs rated.
- **Ask whether each line is from the OEM schedule or from an observed condition.** For schedule items, compare with the owner's manual (normal vs severe).
- **Quick lube:** Do not accept tire or brake verdicts from a visual check that the chain says does not measure them.

### Shop owner (auditing own techs and advisors)
- **Turn off default-green**, or require explicit tapping of each point, where your platform allows it. Audit the share of all-green MPIs by tech against vehicle mileage.
- **Review the mapping tables** (canned jobs, package codes, suggested jobs) at least quarterly. A bad mapping produces systematic over-recommendation.
- **Require measurements behind color grades.** Use stored-note or threshold rules, such as Mitchell 1's measurement-triggered red and yellow, and document the thresholds you use. Gauge color bands differ by tool.
- **Separate deferred (yellow) from recommended (red)** on the estimate. Confirm that the integration does not auto-push yellows onto the work order.
- **Track advisor edits** to tech recommendations, with upsell and sold reports (e.g., the Dominion-style "updates by advisor" count).
- **For machine or AI items** (Hunter, UVeye, Predictive Service), require tech confirmation before pricing.

### Fleet manager
- **Reconcile vendor DVI and invoice lines** against your own DVIR and Issue trail in Fleetio, Samsara, or Whip Around.
- **Flag vendor work** on items your drivers or techs reported as OK, unless the vendor supplies measurements.
- **Check 396.11 repair certification** on every safety defect before the vehicle returns to service. Watch for acknowledged-but-unrepaired failures (Fleetio) and carried-over defects (Samsara).
- **Normalize thresholds in your vendor agreement:**
  - tread minimums: 4/32" steer, 2/32" drive under FMCSA rules (cross-reference 06-commercial-fleet-specialty.md),
  - brake mm,
  - battery test standards.
- **Require vendor exports**, not just PDFs.

---

## 7. Open questions

1. **Mitchell 1 Manager SE Inspections:** Stock templates, tire-by-position and brake fields, whether measurement thresholds ship with defaults, the customer-link domain, and whether default-green can be disabled.
2. **CDK Inspect, Reynolds, and Tekion:** Exact grading scales, measurement fields, and customer link domains. These vendors publish little openly; dealer help portals require login.
3. **OEM numeric thresholds per color** (Ford, GM, Toyota, Honda brake mm and tread 32nds). Likely in dealer-only OEM service-lane guides. Not public.
4. **RO Writer DVI, Protractor native DVI, and Shop Boss:** Grading definitions, measurement capture, and approval-page formats.
5. **Protractor's current ownership** and any 2024-2026 changes.
6. **Whether NAPA still supports its legacy DVVI app** alongside AutoServe1 and Autoflow.
7. **Valvoline's current customer report format** (digital vs printed) and whether any chain sends DVI links; the Valvoline FAQ did not render.
8. **Customer link domains** for Xtime, myKaarma, Dealer-FX, CDK, and Tekion. These are needed for reliable "recognize the platform" fingerprints and should be confirmed from real sample reports supplied by users. **[UNVERIFIED]**
9. **Whether CDK Predictive Service items are visibly labeled** as predicted on the customer-facing MPI.
10. **The Tekion SVC-04 guide** (15 MB PDF): this environment could not parse it. Re-read it for severity tiers and auto-send rules.

---

## 8. Sources

**Mitchell 1**
- https://mitchell1.com/?p=16796
- https://www.aftermarketnews.com/mitchell-1-inspection-tool-launch/
- https://autosphere.ca/mechanical/2025/09/09/mitchell-1-launches-manager-se-inspections-feature/
- https://www.aftermarketnews.com/mitchell-1-announces-mobile-vehicle-inspection-solution/
- https://www.moderntiredealer.com/industry-news/service/article/11509732/mitchell-1-integrates-manager-se-with-prodemand-2013-02-28
- https://www.fenderbender.com/running-a-shop/finance/article/33034899/mitchell-1-introduces-prodemand-estimate-guide-enhancements
- https://www.worktruckonline.com/news/mitchell-1-enhances-fleet-integration-in-shop-management

**RO Writer**
- https://info.rowriter.com/blog/ro-writer-takes-dvi-to-the-cloud/
- https://info.rowriter.com/software/solutions
- https://info.rowriter.com/about-us/

**Protractor**
- https://www.motor.com/2023/10/protractor-adds-digital-vehicle-inspection-and-vin-scanner/
- https://autoflow.com/help-center/training/sms-training/protractor-integration-training/protractor-dvi-setup-and-administration/
- https://www.aftermarketnews.com/bolt-on-technology-now-integrates-with-protractor-shop-management-platform/

**NAPA TRACS / AutoServe1**
- https://partner.autoserve1.com/napa-tracs/
- https://autoflow.com/napa-tracs/

**ALLDATA**
- https://www.alldata.com/us/en/manage-online-article/setting-up-inspection
- https://www.alldata.com/ca/en/support/manage-online/article/using-inspection-lists
- https://www.alldata.com/ca/en/digital-vehicle-inspections
- https://www.alldata.com/us/en/new=alldata-inspections-offers-fast-curbside-check-in-with-digital-inspections

**Shop Boss and ARI**
- https://www.getapp.com/industries-software/a/shop-boss-pro/
- https://www.capterra.com/p/121909/Shop-Boss-Pro/
- https://apps.apple.com/app/id1189544427
- https://www.getapp.ca/software/131559/ari

**CDK**
- https://cdkglobal.com/cdk-inspect
- https://www.businesswire.com/news/home/20210209005198/en/CDK-Global-Reimagines-Its-Service-Layered-Applications
- https://www.autosuccessonline.com/cdk-fixed-operations-software-dealerships/
- https://www.cdkglobal.com/fixed-ops/service/cdk-service

**Reynolds**
- https://apps.apple.com/us/app/-/id6475359821
- https://www.vehicleservicepros.com/industry-news/service-repair/company-association-news/news/21259834/hunter-engineering-announces-inspection-equipment-integration
- https://www.uveye.com/reynoldsandreynolds
- https://www.autodealertodaymagazine.com/369796/reynolds-unveils-expanded-service-offering-at-nada
- https://platform.softwareone.com/product/eapproval/PCP-2371-1078
- https://www.casestudies.com/company/reynolds-and-reynolds/case-study/bmw-of-tenafly-improves-service-trust-with-reynolds-and-reynolds
- https://www.autodealertodaymagazine.com/news/penske-to-install-reynolds-docupad-in-all-stores

**Xtime**
- https://xtime.com/solutions/inspect
- https://www.fleetmaintenance.com/in-the-bay/shop-equipment/press-release/21211157/hunter-engineering-company-hunter-engineering-xtime-partner-to-integrate-inspection-products
- https://www.capterra.com/p/187244/Xtime/reviews/

**myKaarma**
- https://mykaarma.com/oems/ford/
- https://mykaarma.com/news/mykaarma-selected-as-ford-dealer-technology-preferred-partner-for-video-capability/
- https://mykaarma.com/blog/from-inspection-to-approval-streamlining-the-service-process-with-uveye-and-mykaarma/
- https://mykaarma.com/?p=10188

**Dealer-FX**
- https://www.businesswire.com/news/home/20210308005223/en/Snap-on-Acquires-Dealer-FX-Group-Inc.
- https://help.dealer-fx.com/nissan/en-US/technician%20inspection/Content/RNotes/New%20Features%20MPImedia.htm
- https://dealer-fx.com/visual-mpi-empower-technicians-with-integrated-video/
- https://dealer-fx.com/dealer-fx-strengthens-integration-with-cdk-added-as-publisher-on-fortellis-automotive-exchange-platform/
- https://dealer-fx.com/category/news

**Tekion**
- https://go.tekion.com/hubfs/Tekion%20One%20-%20Implementation%20Guides/SVC-04.pdf
- https://www.hunter.com/media-center/press-releases/hunter-engineering-and-tekion-partner-to-drive-customer-service-experience-plus-dealer-profitability/
- https://tekion.com/blog/uveye-and-tekion-partner-to-enhance-the-dealership-customer-service-experience
- https://tekion.com/blog/top-10-customer-experience-trends-in-automotive-industry-fixed-ops

**Generic dealer MPI (Dominion)**
- https://help.dominiondms.com/en/knowledge/multi-point-inspections-mpi
- https://help.dominiondms.com/en/knowledge/mpi-results-upsell-report
- https://help.dominiondms.com/hubfs/2021%20VUE%20GM%20SLT%20and%20PASE%20Integration%20-%20USER.pdf

**OEM programs**
- https://www.caribe.ford.com/en/abw/owners/genuine-service/service-excellence/
- https://goaudits.com/checklist/ford-multi-point-inspection-checklist/913/122/
- https://truvideo.com/ford-mpi-program/
- https://secure.businesswire.com/news/home/20260427424905/en/Vehlos-Solutions-Now-Support-the-Requirements-of-the-Ford-Commitment-Program
- https://www.businesswire.com/news/home/20240627793533/en/Vehlo%E2%80%99s-Dealerlogix-Becomes-Newest-Participating-Certified-Service-Lane-Tool-Partner-for-General-Motors
- https://gm-techlink.com/?p=16273
- https://www.caseyhonda.com/multi-point-inspection/
- https://oklahomacity.porsche.com/en/service/multi-point-inspection
- https://help.kimoby.com/multi-point-inspections
- https://goaudits.com/checklist/toyota-multi-point-inspection-checklist/913/124/
- https://www.toyotaownersclub.com/forums/topic/107157-do-different-mechanics-read-tread-depth-differently/
- https://otctools.com/node/18673

**Industry failure modes**
- https://digitaldealer.com/news/a-service-process-that-actually-makes-money-right-now/151974/
- https://www.ratchetandwrench.com/columns/article/55366971/french-the-400-air-filter-why-your-mpi-process-is-restricting-profit
- https://autoshopowner.com/forums/topic/19935-do-technicians-give-you-pushback-on-performing-the-multipoint-inspection
- https://www.motor1.com/news/794085/toyota-dealership-service-scam/

**Quick lube and tire**
- https://www.vioc.com/faq/what-is-included-in-safety-inspection
- https://www.ftc.gov/news-events/news/press-releases/2025/11/ftc-requires-divestiture-oil-change-shops-valvoline-greenbriar-deal
- https://assets1.jiffylube.com/auto-services/oil-change
- https://www.nbclosangeles.com/local/is_your_mechanic_cheating/1852378/
- https://www.aol.com/6-auto-repair-chains-accused-130050737.html
- https://www.discounttire.com/learn/tire-safety
- https://www.discounttire.com/blog/road-trip-checklist
- https://www.lesschwab.com/article/safety-status-check-report.html
- https://counter.lesschwab.com/brakes

**Fleet**
- https://help.fleetio.com/en_US/inspections-item-failures
- https://help.fleetio.com/en_US/inspections-overview
- https://whiparound.com/wp-content/uploads/2026/08/Whip-Around-DVIR-Form-Template.pdf
- https://www.samsara.com/ca/resources/marketplace/whip-around
- https://kb.samsara.com/hc/articles/4406022633741
- https://www.law.cornell.edu/cfr/text/49/396.11
