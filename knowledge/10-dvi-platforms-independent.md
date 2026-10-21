# 10 — DVI Platforms, Independent Shops (Group A): Tekmetric, Shopmonkey, Shop-Ware, AutoVitals, Bolt On

## 1) Scope & as-of date

- **As of:** 2026-10-20. Research used public help-center articles (pulled through their public Zendesk / Salesforce Knowledge endpoints), vendor product pages, vendor blogs, release notes and trade press. I did not log in, request demos or contact anyone.
- **Platforms covered in depth:** Tekmetric, Shopmonkey, Shop-Ware (owned by Vehlo since March 2024), AutoVitals (a DVI/workflow add-on that sits on top of a shop-management system, or "POS"), and Bolt On Technology (DVI add-on, owned by Performant Capital since 2021).
- **Labor-guide integrations covered:** Tekmetric (its own guide, ProDemand, ALLDATA, Smart Jobs), Shopmonkey (MOTOR, ALLDATA), Shop-Ware (its "Estimator" guide, parts e-commerce). Also the AutoVitals-to-Tekmetric canned-job bridge and the AutoFlow-to-Tekmetric import.
- **Brief notes only:** Shopgenie and Steer. Both are CRM/marketing tools, not DVI engines (see 3.6).
- **Evidence tags:** "Documented" means stated in a vendor help article or release note, with the URL cited. **[INFERENCE]** marks my own reasoning. **[UNVERIFIED]** marks claims I could not confirm in a public source. Vendor performance claims (ARO lift, close rates) are vendor-reported and not independently verified.
- **Coverage is uneven:**
  - Tekmetric, Shopmonkey and AutoVitals publish deep, current help centers.
  - Shop-Ware's help center is public but thinner on inspection mechanics.
  - Bolt On publishes almost nothing about mechanics. Its help desk is a customer portal, so its section relies on marketing pages and trade press and carries many [UNVERIFIED] tags.

---

## 2) Cross-platform comparison table

| Dimension | Tekmetric | Shopmonkey | Shop-Ware | AutoVitals | Bolt On |
|---|---|---|---|---|---|
| Product type | All-in-one shop-management system with built-in DVI | All-in-one shop-management system with built-in DVI | All-in-one shop-management system; customer portal called DVX | DVI and workflow add-on, integrated two-way with many POS systems | DVI and communications add-on; "NextGear" standalone web version |
| Template unit | Inspection > Groups > Tasks, with preset Findings ([src](https://support.tekmetric.com/hc/en-us/articles/360037472174-Creating-Inspections)) | Inspection > Items ([src](https://support.shopmonkey.io/hc/en-us/articles/38743088738452-Inspection-Templates)) | Inspection attached to a *service* on the RO; templates made in the "Cannery" ([src](https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/)) | Inspection Sheet > Sections > Topics > Conditions > Actions ([src](https://support.autovitals.com/hc/en-us/articles/4406522377876-AutoVitals-Inspection-Builder)) | Customizable checklists [details UNVERIFIED] |
| Rating labels | Check & Okay / May Require Attention Soon / Requires Immediate Attention / Not Applicable (green/yellow/red/N/A) ([src](https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection)) | Passed / Needs Attention / Failed / N/A (green check, yellow !, red X, grey) ([src](https://support.shopmonkey.io/hc/en-us/articles/38743049848852-Perform-Inspections)) | Inspection line: green / orange(yellow) / red. Recommendations get a *separate* urgency: white (not set) / green low / yellow medium / red high ([src](https://support.shop-ware.com/s/article/Recommendations-Urgency-Sorting-and-Viewing-Totals)) | Shop-defined statuses (name, color, icon), each mapped to Good / Needs Future Attention / Requires Immediate Action / Hidden ([src](https://support.autovitals.com/hc/en-us/articles/4406522377876-AutoVitals-Inspection-Builder)) | Green good / yellow non-urgent ("OK") / red urgent ([src](https://blog.boltontechnology.com/what-are-digital-vehicle-inspections)) |
| Can a rating be set without technician judgment? | Yes: "Rate All Tasks" bulk-fill; copy prior inspection with ratings; Recommended Maintenance auto-rates by mileage interval (overdue = Red, due soon = Yellow) | Not documented [UNVERIFIED] | Swipe-to-green shortcut in TechApp ([src](https://shop-ware.com/features/techapp/)) | Yes: each Condition carries a Default Status and Default Action; Carry Forward re-confirms last visit | [UNVERIFIED] |
| Structured measurements | None documented in DVI (findings are text). Units setting exists for Canada ([src](https://support.tekmetric.com/hc/en-us/articles/44090257340311-Mobile-App-What-s-New)) | None documented | None documented | Measurement fields exist and need advisor approval ([src](https://support.autovitals.com/hc/en-us/articles/27719371914388-AutoVitals-Basic-Training-6-Inspection-Editing)); device imports (Groove Glove tread scanner, Hunter Quick Check/WinAlign incl. battery) | Not documented |
| Measurement auto-sets color? | No (interval-based auto-rating only) | Not documented | Not documented | Groove Glove readings map to sheet Conditions, which carry default statuses ([src](https://support.autovitals.com/hc/en-us/articles/5909835783956-How-To-Set-Up-Tire-Profiles-Groove-Glove-with-AutoVitals)) [threshold logic lives with the vendor, UNVERIFIED] | Not documented |
| Media tied to item | Yes, per task row (photo/video/PDF); markup on photos only, not video | Yes, per item (jpeg/png/PDF/mp4, max 50 MB) | Yes, per inspection item and per finding; TechApp video up to 500 MB (since July 2025) | Yes, per topic; photos and videos can be **moved or copied between topics and between ROs** | Photos and video per inspection [per-item linkage UNVERIFIED] |
| Image timestamps shown to customer | Not documented | Not documented | Not documented | Date always shown; time-of-day optional (shop setting) ([src](https://support.autovitals.com/hc/en-us/articles/4418702821524-Timestamps-on-Customer-Inspection-Results)) | Vendor says each inspection makes a timestamped record ([src](https://napatracs.com/extension/bolt-on-technology/)) |
| Finding to estimate | Canned job mapped to task; auto-added when task is red/yellow and inspection marked complete | Canned services aligned manually; "Estimate Requested" / "Deferred by Customer" actions on yellow/red items | Clipboard-and-wrench icon on line turns finding into a Recommendation (search service or build one) | Actions = canned jobs (default or selectable); sent to POS as unapproved labor lines on "UPDATE WO" | Canned jobs [mapping UNVERIFIED] |
| Recommended vs declined tracking | Draft (unchecked, not presented) vs Declined (presented and declined); Declined Jobs report; Job History | "Recommended" services excluded from total until authorized; Deferred Services list and report | Approve / "Decline for Now" / Pending / Postpone / Done; past recommendations shown on new estimates | Depends on host POS declined-job fields; AutoVitals CRM reuses them | [UNVERIFIED] |
| Customer delivery | Text/email link; "Vehicle Health Report" sent as second tab with estimate | SMS/email with PDF attachment plus live link | "DVX" share link by text/email | "Inspection Results" link (3 templates) by text/email | Text/email to phone |
| Approval record | Point-in-time authorization snapshots on RO Summary; method dropdown (digital signature, paper, in-person, phone, text, email) | Per-service authorize with optional e-signature; signed PDF in Activity; separate inspection e-signature (2026) | "Authorization Summary" (opt-in) with method, contact, phone/email, signature; CA BAR-format summary | Approvals live in host POS [INFERENCE] | Vendor says techs can capture signature on tablet ([src](https://lp.boltontechnology.com/mitchell-1)) |
| Owner KPIs | Inspection Report: completion rate, avg inspection time, avg findings, % sent / % viewed, ARO and close ratio vs attachment count | Vehicle Inspections Summary/Detail: completion rate, items rated %, Avg Finding % | Technician report (efficiency/productivity); unfulfilled-recommendations export | BCP: inspection rate, sent rate, avg pictures per RO, edited-picture rate, recommendation rate, customer research time | "Reporting" module [metrics UNVERIFIED] |
| AI text tools on findings | "Smart DVI" (video narration to AI-built DVI) announced April 2026, "coming soon" | Voice notes in mobile app | "AutoWrite" AI rewrite/translate on Notes/Findings (announced Oct 2025, early adoption) | "Otto Notes" AI rewrite of customer notes (rolled out Feb–Mar 2026) | AI phone advisor "MILES" (not a DVI tool) |

---

## 3) Per-platform deep dive

### 3.1 Tekmetric

**1. How inspections are built**
- **Who builds them and the structure.** Users with Inspection permissions build templates under Inspections / Settings → Inspection Templates. A template has a Title, one or more **Inspection Groups** (e.g., Exterior, Brakes, Fluids) and **Tasks** inside each group ([Creating Inspections](https://support.tekmetric.com/hc/en-us/articles/360037472174-Creating-Inspections)).
- **Findings.** Findings come in two kinds:
  - *General findings*: a shared dropdown list for any task.
  - *Task-specific findings*: e.g., pads are "worn," never "leaking."
  - Technicians can always type a custom finding instead ([same](https://support.tekmetric.com/hc/en-us/articles/360037472174-Creating-Inspections)).
- **Default templates.** Templates marked **Default** are auto-added to every new RO; several can be default and their order is configurable ([Mark Inspections as Default](https://support.tekmetric.com/hc/en-us/articles/16773448793751-Mark-Inspections-as-Default)). Default ordering was released Sept 2026 ([Release Notes](https://support.tekmetric.com/hc/en-us/articles/360041785434-Release-Date-Feature-Notes)).
- **Internal inspections.** A template can be "internal by default." Internal inspections are done by techs but hidden from all customer-facing documents and links. Typical uses are check-in damage photos and QA ([Internal Inspections](https://support.tekmetric.com/hc/en-us/articles/18139709709719-Internal-Inspections)).
- **Item types.** I found no documented item types beyond rating + finding + media. In particular, there are no numeric measurement fields, multiple-choice items or pass/fail-only items.
- **Stock templates.** No stock template library is documented. A 2023 marketing guide implies shops build their own templates ([DVI guide](https://tours.tekmetric.com/answers/digital-vehicle-inspection-guide)). [UNVERIFIED whether onboarding seeds templates]

**2. Grading scheme**
- **Four ratings.** Check & Okay; May Require Attention Soon; Requires Immediate Attention; Not Applicable. The two attention ratings prompt the tech to report the item ([Performing an Inspection](https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection)). Elsewhere these are called green / yellow / red ([Link Canned Jobs](https://support.tekmetric.com/hc/en-us/articles/1500011364982-Link-Canned-Jobs-to-Inspections)).
- **Unrated tasks.**
  - Unrated tasks used to show as "Incomplete" on the customer report. Tekmetric tells shops to use N/A as positive confirmation ([Performing](https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection)).
  - Since Sept 2025 the customer Vehicle Health chart drops N/A and incomplete tasks. "Not found" findings are also hidden ([DVI Enhancements](https://support.tekmetric.com/hc/en-us/articles/35205687782423-DVI-Enhancements-That-Drive-Impact)).
- **Ratings that are not free-chosen.** Three mechanisms set ratings without a per-item judgment:
  - **"Rate All Tasks"** fills every blank line with one chosen rating (feature since April 2019) ([Performing](https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection); [Release Notes](https://support.tekmetric.com/hc/en-us/articles/360041785434-Release-Date-Feature-Notes)).
  - **Copy prior inspection**: Inspection History can copy a previous inspection *including ratings and findings* onto the current RO ([DVI History](https://support.tekmetric.com/hc/en-us/articles/5178699794455-Digital-Vehicle-Inspection-History)).
  - **Recommended Maintenance on DVI** (Scale tier, Aug–Sept 2026). When an odometer is entered, Tekmetric checks OEM / Shop / "Shortest" intervals (OEM data plus Tekmetric and Carfax history) and **pre-rates matching tasks: Overdue → Red, Due Soon → Yellow**. Shops can change those defaults (Overdue: Red or Yellow; Due Soon: Red, Yellow or Green). The note text follows the pattern "[Task] is overdue by X miles. Recommended every Y." Techs can override ([Recommended Maintenance on DVI](https://support.tekmetric.com/hc/en-us/articles/42955960801943-Recommended-Maintenance-on-DVI); [Recommended Jobs](https://support.tekmetric.com/hc/en-us/articles/41093244754199-Recommended-Jobs)).
- **No measurement-driven color logic** is documented.

**3. Measurements**
- No structured tread/pad/rotor/battery fields are documented in the DVI. Any readings live in free-text findings, photos or attached PDFs.
- Tekmetric suggests attaching scan-tool / Mode 6 screenshots ([Performing](https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection)).
- The Sept 2026 mobile release added country-specific units for Canadian shops ([Mobile What's New](https://support.tekmetric.com/hc/en-us/articles/44090257340311-Mobile-App-What-s-New)).
- No Midtronics integration found [UNVERIFIED either way].
- Tire DOT capture and tire quoting exist outside the DVI ([Tire DOT#](https://support.tekmetric.com/hc/en-us/articles/17119553542167-Tire-DOT-Management-in-Tekmetric)).

**4. Photos/video**
- **Capture.** Camera, video and PDF icons on each task row; on phone/tablet they open the camera. Videos have been supported on DVIs since May 2020. Many PDFs can be attached per finding ([Performing](https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection)).
- **Markup.** Circle, arrow, text and rotate tools. The annotated image replaces what the customer sees. Draw/zoom/crop tools were added Aug–Oct 2025 ([Image Markup](https://support.tekmetric.com/hc/en-us/articles/34327534094871-DVI-Image-Markup); [Release Notes](https://support.tekmetric.com/hc/en-us/articles/360041785434-Release-Date-Feature-Notes)). Videos cannot be edited.
- **Printing.** PDFs print with or without photos; videos never print.
- **Uploads from files.** Desktop upload opens a file browser, so media need not be captured live on the vehicle. Drag-and-drop media upload was added March 2026.
- **Media outside an inspection.** Since Feb 2026, media can also attach to a Technician Concern that is not tied to an inspection. Since Jan 2026, it can attach to the Customer Concern ([Release Notes](https://support.tekmetric.com/hc/en-us/articles/360041785434-Release-Date-Feature-Notes); [Mobile](https://support.tekmetric.com/hc/en-us/articles/44090257340311-Mobile-App-What-s-New)).
- **Timestamps.** No documented capture-timestamp overlay.

**5. Canned jobs / recommendations**
- **Mapping and auto-add.** A canned job can be mapped to any task (wrench icon). When the task is rated **red or yellow** and the inspection is marked complete, the canned job is **auto-added to the Estimate**. Shared canned jobs appear only once ([Link Canned Jobs](https://support.tekmetric.com/hc/en-us/articles/1500011364982-Link-Canned-Jobs-to-Inspections)). Auto-add arrived May 2021 for the Scale tier.
- **Technician Concerns.** Red and yellow items automatically appear in a "Technician Concerns" table on the Inspection and Estimate tabs.
- **Smart Jobs / Smart Canned Jobs.** These resolve labor (Tekmetric guide) and parts by decoded VIN ([Smart Jobs 101](https://support.tekmetric.com/hc/en-us/articles/27373807531287-Smart-Jobs-101)).
- **Labor sources.** Tekmetric's own guide plus maintenance schedule; ProDemand and ALLDATA on Grow/Scale tiers. Tekmetric itself cautions that guide times are reference only ([Labor Guide](https://support.tekmetric.com/hc/en-us/articles/360063488693-Labor-Guide); [ALLDATA](https://support.tekmetric.com/hc/en-us/articles/25868623867927-ALLDATA-Labor-Guide-Integration)).
- **Recommended Jobs tab** (Scale). Interval-based maintenance suggestions, with presets from Tekmetric or **BG** (fluid-service brand) when the BG integration is on ([Recommended Jobs](https://support.tekmetric.com/hc/en-us/articles/41093244754199-Recommended-Jobs)).
- **Declined vs Draft.** Declined jobs were presented and declined: they count in close ratio, appear in the Declined Jobs report and show in Job History once the RO is posted. Draft jobs were never presented and are excluded from both ([Declined vs Draft](https://support.tekmetric.com/hc/en-us/articles/360039270153-What-is-the-difference-between-declined-jobs-draft-jobs)). Declined work can be re-added from Job History ([Add Declined Work](https://support.tekmetric.com/hc/en-us/articles/360056145094-How-Do-I-Add-Previously-Declined-Work-to-a-Repair-Order)).

**6. Customer-facing report**
- **Name.** "Inspection Report" / "Vehicle Health Report." It is sent automatically as a second tab with the estimate ([Performing](https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection)).
- **Layout since Sept 2025.** Smaller header; "Visit Details" tab; Customer Concern shown first with related findings; Vehicle Health chart; "Not found" findings hidden ([DVI Enhancements](https://support.tekmetric.com/hc/en-us/articles/35205687782423-DVI-Enhancements-That-Drive-Impact)).
- **Customer Concern block.** Has "Customer States," "Finding" and media; it can be hidden via Transparency Settings ([Customer Concern](https://support.tekmetric.com/hc/en-us/articles/36897066105111-The-Customer-Concern)).
- **Default texts.**
  - Inspection: tells the customer the vehicle was inspected at the shop and links to results. This wording replaced a "ready" phrasing in Feb 2024 because customers thought the car was ready for pickup.
  - Estimate and invoice texts follow a similar pattern.
  - Scale-tier shops can edit the wording ([Adjust Verbiage](https://support.tekmetric.com/hc/en-us/articles/25416840474135-Adjust-Verbiage-for-Inspection-Estimate-Invoice-Texts)).
- **Approval.**
  - The authorization screen is identical to the customer's view; customers approve or decline per job.
  - The shop records the method: Digital Signature, Paper Signature, Verbal In-Person, Phone Call, Text Message or Email.
  - "Require Digital Signature for Digital Authorization" is optional.
  - Point-in-time authorization copies are kept on the Summary tab.
  - Jobs can be un-approved ([Digital Signature](https://support.tekmetric.com/hc/en-us/articles/4421125978391-Digital-Signature-Authorization-Process)).
- **Transparency Settings** control which fields appear on the estimate/invoice. They can differ between estimate and invoice and can be overridden per RO ([Transparency](https://support.tekmetric.com/hc/en-us/articles/360035798334-Estimate-and-Invoice-Transparency-Settings)).
- **Links can be unshared** (May 2021). An "inspection viewed" indicator exists (Aug 2022) ([Release Notes](https://support.tekmetric.com/hc/en-us/articles/360041785434-Release-Date-Feature-Notes)).

**7. Exports and audit data**
- **Inspection Report** (all tiers since Feb 2026). It covers:
  - ARO and close ratio with vs without inspections;
  - completion rate, average inspection time, average findings, % sent and % viewed;
  - graphs by attachment count;
  - grouping by tech, writer or inspection name.
  - Exports to PDF/CSV (graphs excluded). Only **posted** ROs count. **Internal inspections are excluded** ([Inspection Report](https://support.tekmetric.com/hc/en-us/articles/9864603066519-Inspection-Report); [Internal](https://support.tekmetric.com/hc/en-us/articles/18139709709719-Internal-Inspections)).
- **Inspection History** per vehicle shows RO#, PDF, technician, rating counts, created and completed dates, and a vehicle-transferred flag ([History](https://support.tekmetric.com/hc/en-us/articles/5178699794455-Digital-Vehicle-Inspection-History)).
- **Public API** has had an Inspection endpoint since June 2019 ([Release Notes](https://support.tekmetric.com/hc/en-us/articles/360041785434-Release-Date-Feature-Notes)) [field list UNVERIFIED].

**8. Known pitfalls (documented mechanics, auditor framing)**
- **Bulk-rated lines.** Rate All Tasks can mark untouched lines green or N/A, which looks like a full inspection.
- **Copied ratings.** A copied prior inspection carries forward old ratings and findings. If the tech edits nothing, findings may describe the last visit.
- **Mileage-driven yellow/red.** Recommended Maintenance pre-rates tasks from mileage intervals, not condition. A red "Engine Air Filter" with interval-pattern wording plus no photo is an interval recommendation, not an observed defect.
- **Auto-added estimate lines.** Red/yellow plus a mapped canned job auto-creates estimate lines. Price and labor come from canned or Smart Job templates (labor guide), not from what the tech saw.
- **Hidden context.** The customer chart now hides N/A and incomplete items, so a sparse customer report may hide skipped items. Internal inspections are hidden from customer and report alike.
- **Videos never print**, so printed copies under-represent evidence.
- **Free-text findings only.** With no structured measurements, findings like "worn" may lack mm or 32nds values.

**9. How to recognize a Tekmetric report**
- Terminology: "Vehicle Health Report"/"Inspection Report"; the rating phrases "Check & Okay," "May Require Attention Soon," "Requires Immediate Attention"; "Technician Concerns"; "Customer Concern"/"Customer States"; "Visit Details" tab; estimate and inspection as tabs.
- Texts open with "Hello, your vehicle has been inspected at <Shop>…" when the default is kept.
- Share-link domain: [UNVERIFIED]. I expect a tekmetric.com subdomain but could not confirm it publicly.

---

### 3.2 Shopmonkey

**1. How inspections are built**
- **Where they come from.** An inspection is created from an estimate's Inspections tab, either from scratch or from a saved template. A template is saved from an existing inspection or built under Lists → Inspection Templates ([Perform Inspections](https://support.shopmonkey.io/hc/en-us/articles/38743049848852-Perform-Inspections); [Inspection Templates](https://support.shopmonkey.io/hc/en-us/articles/38743088738452-Inspection-Templates)).
- **Item contents.** Each item has a name, a status color, and attached photos, videos, PDFs, notes and recommendations.
- **Ad-hoc items.** Ad-hoc items can be added during the inspection. Mobile techs cannot create templates, only add them ([Mobile App](https://support.shopmonkey.io/hc/en-us/articles/38743122026388-Inspections-in-Shopmonkey-for-Techs-Mobile-App)).
- **Shopmonkey's framing.** Shopmonkey positions inspections partly as check-in/check-out documentation ([Perform](https://support.shopmonkey.io/hc/en-us/articles/38743049848852-Perform-Inspections)).
- **Quick Notes.** Saved text snippets with a title (not visible to the customer) and content (visible). Editing a Quick Note after inserting it changes only that instance ([Quick Notes](https://support.shopmonkey.io/hc/en-us/articles/38743018176148-Manage-Inspection-Quick-Notes)).
- **Multi-location.** HQ (multi-location) can share inspection templates ([HQ Templates Data Sharing](https://support.shopmonkey.io/hc/en-us/articles/43357106322964)).
- **Item types.** I found no documented types beyond status + notes + media.
- **Stock templates.** A DVI Master Series features a sample check-in template ([DVI Master Series: Templates](https://support.shopmonkey.io/hc/en-us/articles/43553316659092-DVI-Master-Series-Inspection-Templates)). [UNVERIFIED whether stock templates ship by default]

**2. Grading scheme**
- **Statuses.** Passed (green check), Needs Attention (yellow !), Failed (red X), N/A (grey) ([Perform](https://support.shopmonkey.io/hc/en-us/articles/38743049848852-Perform-Inspections)).
- **Custom statuses.** The report docs refer to "custom statuses other than Green/Yellow/Red/N/A," so custom statuses appear possible ([Summary Report](https://support.shopmonkey.io/hc/en-us/articles/44632022471060-Vehicle-Inspections-Summary-Report)) [configuration UNVERIFIED].
- **Review actions.** Optional actions on yellow/red items, "Estimate Requested" or "Deferred by Customer," are enabled under Settings → Customer Authorization → "Show inspection review options."
- **No measurement-driven or default color** is documented.

**3. Measurements**
- No structured measurement fields are documented in DVI. Tread depth is a *tire inventory spec*, not an inspection field ([Tires](https://help.shopmonkey.io/en/articles/5564534-how-do-tires-work-in-shopmonkey)).
- The mobile app has TIN/DOT scanning ([Improvements: April 2026](https://support.shopmonkey.io/hc/en-us/articles/51946021436692)).
- No battery-tester import found [UNVERIFIED].

**4. Photos/video**
- **Per-item uploads.** jpeg, png, PDF or mp4, **max 50 MB** each ([Perform](https://support.shopmonkey.io/hc/en-us/articles/38743049848852-Perform-Inspections)).
- **Mobile.** The app captures photo and video. Shopmonkey's marketing also mentions **voice notes** ([DVI demo page](https://www.shopmonkey.io/demo-digital-vehicle-inspections)).
- **Upload reliability.** The upload system was rebuilt in April 2026 after reliability problems ([Improvements: April 2026](https://support.shopmonkey.io/hc/en-us/articles/51946021436692)).
- **Markup.** No markup tool documented [UNVERIFIED].
- **Image order and orientation.** Since spring 2026, images in the customer view and prints follow **upload order**, and a fix stopped large images printing upside-down ([Improvements: May 2026](https://support.shopmonkey.io/hc/en-us/articles/51950286356756); [April 2026](https://support.shopmonkey.io/hc/en-us/articles/51946021436692)).
- **Audit trail.** An info-icon tooltip shows inspection created / performed / completed dates and the user for each ([Perform](https://support.shopmonkey.io/hc/en-us/articles/38743049848852-Perform-Inspections)).

**5. Canned jobs / recommendations**
- **Linking.** Canned services are aligned to common inspection findings by hand. No automatic red-to-estimate rule is documented. The DVI Master Series advises creating canned services that match inspection items ([Aligning](https://support.shopmonkey.io/hc/en-us/articles/43553515271572-DVI-Master-Series-Aligning-Inspection-Items-with-Canned-Services)).
- **Recommended services.** These are flagged with a "Recommended" icon, excluded from the estimate total until authorized, and shown to the customer in a separate section ([Recommend Services](https://support.shopmonkey.io/hc/en-us/articles/38742880884756-Recommend-Services-on-an-Estimate)).
- **Maintenance Schedules.** MOTOR data filtered by mileage, time or indicator, plus "Suggestions" driven by mileage and time ([Maintenance Schedules](https://support.shopmonkey.io/hc/en-us/articles/38743045057172-Maintenance-Schedules)).
- **Labor.** MOTOR Parts & Labor Lookup; ALLDATA integration since March 2026 ([Parts & Labor](https://support.shopmonkey.io/hc/en-us/articles/38743038698388-Vehicle-Parts-Labor-Lookup); [ALLDATA](https://support.shopmonkey.io/hc/en-us/articles/46833875823124-ALLDATA-Integration)).
- **Deferred services.** Created when an order is invoiced or an estimate archived with recommended, declined or unauthorized services. Tracked per customer and in a Deferred Services by Customer report ([Deferred Services](https://support.shopmonkey.io/hc/en-us/articles/38743421091988-Deferred-Services)).

**6. Customer-facing report**
- **Delivery.** "Share Inspection" by SMS or email sends a **PDF attachment plus a URL** to the order's live inspection tab. All inspections on the order are shared together ([Send Inspections](https://support.shopmonkey.io/hc/en-us/articles/38744430526612-Send-Inspections-to-Customers)).
- **Customer actions.** Customers can comment ([Shopmonkey support](https://support.shopmonkey.io/hc/articles/38744406930068)).
- **Inspection e-signature** (rolled out April–May 2026). Requires an Inspection Footer (terms). The customer signs by drawing or typing. The signed PDF and response are logged in the order's Activity tab ([E-Signatures on Inspections](https://support.shopmonkey.io/hc/en-us/articles/47883995635476-Customer-E-Signatures-on-Inspections)). Adding or removing an attachment invalidates an existing signature (fix, April 2026) ([Improvements: April 2026](https://support.shopmonkey.io/hc/en-us/articles/51946021436692)).
- **Estimate authorization.**
  - Per-service checkboxes with optional e-signature; the shop can authorize on the customer's behalf and record the method.
  - Optional setting: **reset authorization when a service price increases**, with prior authorizations kept in history.
  - Signed estimate/invoice PDFs are under Authorizations ([Request Authorization](https://support.shopmonkey.io/hc/en-us/articles/38743372579988-Request-Customer-Authorization); [E-Signatures](https://support.shopmonkey.io/hc/en-us/articles/38743424357652-Customer-E-Signatures-to-Authorize-Services)).
- **Order PDFs.** Each status change creates an updated PDF link in the order activity log (April 2025) ([Updates April 2025](https://support.shopmonkey.io/hc/en-us/articles/40018217207316)).

**7. Exports and audit data**
- **Vehicle Inspections Detail report** (one row per inspection, Excel export):
  - inspectors who rated items, plus "Completed By" (who tapped Complete);
  - Items Rated and Items Rated %;
  - Passed / Needs Attention / Failed / N/A counts;
  - **Avg Finding %** = (yellow + red) ÷ (green + yellow + red).
  - "Unassigned" means items were rated without a credited tech ([Detail Report](https://support.shopmonkey.io/hc/en-us/articles/44632017228948-Vehicle-Inspections-Detail-Report)).
- **Summary report** adds Orders with Inspection %, per-tech volume and ARO ([Summary Report](https://support.shopmonkey.io/hc/en-us/articles/44632022471060-Vehicle-Inspections-Summary-Report)).
- **Public REST API.** Covers customers, orders, users, vehicles and inventory, plus webhooks ([API](https://support.shopmonkey.io/hc/en-us/articles/38743124485780-Shopmonkey-API)). Inspection objects in the API: [UNVERIFIED].

**8. Known pitfalls**
- **Completion is a button.** "Completed" counts only if someone taps Complete, so fully rated inspections can look incomplete.
- **Completed By can differ from the rater.** The person who completes need not be the person who rated, so tech vs advisor edits can be separated in the Detail report.
- **Multi-recipient sends are not remembered.** A later resend goes only to the primary contact ([Send](https://support.shopmonkey.io/hc/en-us/articles/38744430526612-Send-Inspections-to-Customers)).
- **Recommended lines sit outside the total.** A customer reading only the total may miss them [INFERENCE].
- **Free-text findings.** No structured measurements, so condition claims rest on notes and photos. Quick Notes mean identical canned wording may appear across vehicles.

**9. How to recognize a Shopmonkey report**
- Status words: "Passed / Needs Attention / Failed / N/A" with check, exclamation and X icons.
- "Estimate Requested" / "Deferred by Customer" labels; "Recommended" services in a separate block.
- The email/SMS carries a PDF attachment plus a link; an inspection footer/terms block appears when e-signature is used.
- Link domain: [UNVERIFIED].

---

### 3.3 Shop-Ware (Vehlo)

**1. How inspections are built**
- **Templates and attachment.** Inspections are created in the "Shop-Ware Cannery," added on the fly and tailored by vehicle or job. An auto-populated safety inspection is added to every work order ([Shop-Ware DVX innovations, Oct 2024](https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/)).
- **Inspections live inside services.** Inspections sit under a **service** on the RO, alongside labor, parts, fees and sublet lines, and are added in Edit Mode ([Getting Started](https://support.shop-ware.com/s/article/Getting-Started-Repair-Orders-and-Appointments)).
- **Item types.** I found no documented types beyond status color + notes + images.

**2. Grading scheme**
- **Two separate color layers:**
  - **Inspection line status:** green/orange/red in TechApp ([What is TechApp](https://support.shop-ware.com/s/article/What-is-TechApp-by-Shop-Ware)); help articles describe yellow or red "based on urgency" ([Create a Recommendation](https://support.shop-ware.com/s/article/How-Do-I-Create-a-Recommendation)).
  - **Recommendation urgency**, set separately by the advisor in Edit Mode: default **white = not set**, then green (low), yellow (medium), red (high). Recommendations can be re-sorted by creation date, custom order or urgency ([Urgency](https://support.shop-ware.com/s/article/Recommendations-Urgency-Sorting-and-Viewing-Totals)).
- **Swipe shortcut.** A swipe in TechApp marks a line green without opening it. Yellow/red open a "Create Findings" screen ([TechApp](https://shop-ware.com/features/techapp/)).

**3. Measurements**
- None documented in DVI. Tire work in 2026 concerns parts fields such as size and brand ([Release Notes v13.x](https://support.shop-ware.com/s/product-updates)).
- Shop-Ware's API partner list includes AutoVitals, AutoFlow and others, so measurement-capable DVI add-ons may be layered on top ([API Partners](https://support.shop-ware.com/s/article/API-Partner-Integrations)).

**4. Photos/video**
- **Capture and markup.** TechApp uses the native camera. Photo markup (arrows, circles, squares, text) arrived March 2024. Video upload limit rose from 50 MB to 500 MB in July 2025 ([Product Updates index](https://support.shop-ware.com/s/product-updates); see v11.04.0 and v12.4.0).
- **Display.** Notes and attachments show as icons under each inspection item. PDFs can be printed without pictures (Jan 2024).
- **MMS.** MMS texting of photos and videos arrived May 2026 (v13.4.0).

**5. Canned jobs / recommendations**
- **Three ways to make a recommendation:** the clipboard-and-wrench icon on an inspection line, "Create a Finding" in the Notes Feed, or converting an existing service ([Create a Recommendation](https://support.shop-ware.com/s/article/How-Do-I-Create-a-Recommendation)).
- **Draft/publish control.** A recommendation must be **published** to be visible to the customer. Since Jan 2024, shops can limit some users to "save as draft only," so an advisor reviews before publishing ([v10.12.0 release note](https://support.shop-ware.com/s/product-updates)). Shop-Ware says technicians enter details while advisors write customer-facing text ([DVX innovations](https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/)).
- **Recommendation states:** Approve, Add to RO, Reset to Pending, Decline (customer-facing label "Decline for Now"), Mark as Done, Postpone. An out-the-door preview shows the cost of selected recommendations ([Urgency/Totals](https://support.shop-ware.com/s/article/Recommendations-Urgency-Sorting-and-Viewing-Totals)).
- **Carry-forward.** Pending and declined recommendations reappear at the top of new estimates and in an unfulfilled-recommendations export ([Declined tracking](https://support.shop-ware.com/s/article/Are-You-Able-to-Track-Declined-Work-Or-Estimated-Work-per-Invoice-Can-You-Look-at-Daily-and-Weekly-Declined-Sales)). There are no automatic declined-work reminder texts ([FAQ](https://support.shop-ware.com/s/article/If-a-Customer-Declines-Work-Will-Shop-Ware-Still-Send-an-Email-or-Text-Remind-Them-of-Needed-Work)).
- **Closed-RO caveat.** A recommendation added to a *closed* RO will not carry forward ([Create](https://support.shop-ware.com/s/article/How-Do-I-Create-a-Recommendation)).
- **Labor.** Canned jobs, past services, or the "Estimator" labor/maintenance guide ([Getting Started](https://support.shop-ware.com/s/article/Getting-Started-Repair-Orders-and-Appointments)). Good/better/best options can be offered ([DVX innovations](https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/)).
- **AI rewriting.** "AutoWrite" AI can summarize, improve, change tone or translate text in Notes/Findings (inspection and RO), customer-visit reason and messages. It was announced in v12.7.0 (Oct 2025) for early adoption ([v12.7.0](https://support.shop-ware.com/s/product-updates)).

**6. Customer-facing report**
- **"DVX" (Digital Vehicle Experience).** The full RO with inspection report, photos, recommendations ranked by urgency, out-the-door totals, approve / "Decline for Now," online signature and payment ([DVX](https://shop-ware.com/features/dvx/); [DVI vs DVX](https://shop-ware.com/features/dvx/digital-vehicle-inspection-vs-dvx/)).
- **Sharing.** The advisor clicks "Share with Customer" to send the link by email or text. Customer responses trigger a real-time notification ([Customer Respond](https://support.shop-ware.com/s/article/How-Can-A-Customer-Respond-to-a-Recommendation)).
- **Viewing and totals.** The shop is notified when the customer opens DVX. A fix in April 2026 corrected the logged viewer when an additional contact opened the link (v13.2.0). The customer sees the grand total of approved work ([FAQ](https://support.shop-ware.com/s/article/When-a-Client-Approves-Repairs-Online-Do-They-See-the-Total-Revised-Amount)).
- **Approval capture** (opt-in, off by default, since July 2024):
  - in-person: contact plus signature;
  - phone: contact plus phone number;
  - email: email address.
  - Stored in an "Authorization Summary," which is *not* in PDFs unless the checkbox is ticked. A CA BAR "Write it Right"-format approval summary is also available ([Approval Capture](https://support.shop-ware.com/s/article/Does-Shop-Ware-Capture-Recommendation-Approvals); v11.08.0).
- **Signature before work.** An optional setting blocks job start until a signature exists (v11.04.0).

**7. Exports and audit data**
- Technician Report: efficiency, productivity, parts application ([Tech Report](https://support.shop-ware.com/s/article/What-is-the-Technician-Report-in-Shop-Ware)).
- Unfulfilled recommendations export; public API ([API Partners](https://support.shop-ware.com/s/article/API-Partner-Integrations)).
- Vendor-reported DVX metrics: median RO share rate 56%; close rate about 56% with DVX ([DVI vs DVX](https://shop-ware.com/features/dvx/digital-vehicle-inspection-vs-dvx/)).
- An inspection-specific KPI report (photos per inspection, etc.): [UNVERIFIED].

**8. Known pitfalls**
- **Two color scales.** Inspection-line color and recommendation urgency are independent. A red-urgency recommendation may come from a green or unrated inspection line, or the reverse. Auditors should compare both.
- **White urgency.** White (not set) recommendations have no stated urgency.
- **Advisor-written text.** Draft/publish means customer text may be advisor-written, not tech-written. AutoWrite may also have rephrased it.
- **Swipe-to-green** lets techs clear lines quickly without evidence.
- **Hidden authorization details.** The Authorization Summary is opt-in and left out of PDFs by default, so a consumer's PDF may lack approval-method detail.

**9. How to recognize a Shop-Ware report**
- "DVX™" branding; recommendations with "Approve" / "Decline for Now"; urgency-colored circles; "out the door" totals; optional pay button.
- The app lives at app.shop-ware.com ([DVX innovations links](https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/)). Customer share-link domain: [UNVERIFIED].

---

### 3.4 AutoVitals (DVI/workflow add-on)

**1. How inspections are built**
- **Inspection Builder hierarchy.** Inspection Sheet → **Sections** → **Topics** → **Conditions** → **Actions** ([Inspection Builder](https://support.autovitals.com/hc/en-us/articles/4406522377876-AutoVitals-Inspection-Builder)).
- **Library and naming.** A **library** of prebuilt sheets can be searched by category, name or the *shop that built it*. Sheets can carry a customer-facing "Friendly Name" (2025), or the sheet name can be hidden. Sheets export to PDF; canned jobs export to CSV (2025) ([2025 Release Notes](https://support.autovitals.com/hc/en-us/articles/33931313088532-2025-Release-Notes)).
- **Topic options:**
  - mandatory before submit (per topic or whole sheet);
  - image required;
  - auto-open arrow/caption editor;
  - alert the advisor on each tapped recommended action.
- **Condition options:**
  - **Default Status**;
  - **Default Action** (canned job or text);
  - **Default Customer Note** and **Default Image Caption**;
  - Educational Note ("Why is this important") plus an educational video (AutoVitals library or custom);
  - tech reference image;
  - Guided Mode skip settings (skip image, notes or arrow prompts).
- **Read-only library sheets** must be copied before editing ([Smart Canned Jobs](https://support.autovitals.com/hc/en-us/articles/51041681108628-Using-Smart-Canned-Jobs-with-AutoVitals-Tekmetric-Integration)).
- **Tablet check-in.** Inspections can start on the tablet before an RO exists. They are matched to the POS RO **by VIN**, so a wrong VIN means a wrong match ([Start from Tablet](https://support.autovitals.com/hc/en-us/articles/24804398734868-Starting-an-Inspection-from-the-Mobile-App-Tablet)).

**2. Grading scheme**
- **Shop-defined statuses.** Name, color and icon are the shop's choice. Each maps to one meaning: Good (only one status can be Good), Needs Future Attention, Requires Immediate Action, or **Hidden** (status suppressed from the customer report) ([Inspection Builder](https://support.autovitals.com/hc/en-us/articles/4406522377876-AutoVitals-Inspection-Builder)).
- **Implicit "future" status.** The CRM treats any status *containing the word "future"* as future attention ([Recommendations From Inspections](https://support.autovitals.com/hc/en-us/articles/4415124929812-Recommendations-From-Inspections-on-TVP-X)).
- **Tap a condition, get everything.** Selecting a Condition applies its default status, action, customer note and caption in one tap. The color follows the *canned condition*, not a measured value.
- **Carry Forward** (tablet only). Techs can **Confirm** last visit's topic result, or update the condition (which resets the topic), edit notes or replace images ([Carry Forward](https://support.autovitals.com/hc/en-us/articles/4401760600340-Carry-Forward-AutoVitals-X-app)).

**3. Measurements**
- **Measurement fields exist.** Advisors "review, edit, and approve/disapprove Measurements" in the Images/Notes Editor ([Basic Training 6](https://support.autovitals.com/hc/en-us/articles/27719371914388-AutoVitals-Basic-Training-6-Inspection-Editing)). The "untouched" filter includes measurements awaiting approval ([Images/Notes Editor](https://support.autovitals.com/hc/en-us/articles/4408845974420-The-Images-Notes-Editor)). Field-level details (per-position tread inner/middle/outer, units): [UNVERIFIED].
- **Groove Glove (Tire Profiles).** The handheld tread scanner sends per-tire scans. Tire topics must map to the axle and to the sheet's Conditions (e.g., edge/shoulder wear maps to an alignment condition). If topics are not configured, **no Groove Glove data appears**. Groove Glove notes arrive **unapproved by default** for advisor review. Scans attach by VIN, or create a new tile if VIN matching fails ([Groove Glove](https://support.autovitals.com/hc/en-us/articles/5909835783956-How-To-Set-Up-Tire-Profiles-Groove-Glove-with-AutoVitals)). The BCP tracks a "Groove Glove Inspection Rate" ([BCP KPIs](https://support.autovitals.com/hc/en-us/articles/6535417910164-Business-Control-Panel-BCP-List-of-KPIs)).
- **Hunter Quick Check / WinAlign.**
  - Results embed per topic: tread depth, alignment, battery health, diagnostic check.
  - Customer view shows only the Quick Check summary and **after-alignment** values. Shop view also shows before values and technical details.
  - Results show only if the mapped topic has a condition selected, and the VIN must be entered on the Hunter machine ([Hunter](https://support.autovitals.com/hc/en-us/articles/4414874909716-How-to-Set-Up-Hunter-Alignment-With-AutoVitals)).
- **Battery and fluid tests.** The photo best practice asks for photos of battery test results and brake-fluid moisture tests ([Photo Best Practices](https://support.autovitals.com/hc/en-us/articles/8754627477012-AutoVitals-DVI-Photo-Best-Practices)). A direct Midtronics integration: [UNVERIFIED]. Battery data via Hunter Quick Check is documented.

**4. Photos/video**
- **Defaults and editing.** All photos are **auto-approved and visible** unless the advisor hides them (eye icon) or deletes them. The editor has arrows, circles, text, crop, rotate, a checkmark and a suppressor ([Images/Notes Editor](https://support.autovitals.com/hc/en-us/articles/4408845974420-The-Images-Notes-Editor)).
- **Moving and copying media.** Photos can be **moved or copied to another topic, the work order, or a different open RO**. Whole inspections can be **moved to a different RO** ([Basic Training 8](https://support.autovitals.com/hc/en-us/articles/27703698371476-AutoVitals-Basic-Training-8-Moving-Inspections-Photos); [Move Inspection](https://support.autovitals.com/hc/en-us/articles/4410220960788-How-to-Move-an-Inspection-to-a-Different-RO-on-TVP-x)).
- **Uploads.** PDFs can be added (2025). Images can be uploaded from the Today's Vehicle Page (TVP, the advisor's web screen), not just the tablet ([Basic Training 6](https://support.autovitals.com/hc/en-us/articles/27719371914388-AutoVitals-Basic-Training-6-Inspection-Editing)).
- **Timestamps.** Date is always shown on customer images. Time-of-day shows only if "Display Image Timestamps in Customer View" is on ([Timestamps](https://support.autovitals.com/hc/en-us/articles/4418702821524-Timestamps-on-Customer-Inspection-Results)).
- **Photo standards.** Recommended minimums include: plate/front photo, 4 corners, VIN tag, cluster with mileage, fluids on drip tray, brake-fluid moisture test, battery test results, all 4 treads plus size (5 minimum), and brake lining if yellow or red on gauges ([Photo Best Practices](https://support.autovitals.com/hc/en-us/articles/8754627477012-AutoVitals-DVI-Photo-Best-Practices)).

**5. Canned jobs / recommendations**
- **Actions.** Actions are POS canned jobs (synced roughly every 2 hours) or text.
  - A **Default Action** recommends the job *every time* the condition is marked.
  - A **Selectable Action** is optional.
  - "UPDATE WO" pushes recommended canned jobs to the POS (e.g., Tekmetric) as **unapproved labor lines**, with customer notes, photos and the inspection URL ([Tekmetric 2-Way](https://support.autovitals.com/hc/en-us/articles/17938877792404-Tekmetric-2-Way-Integration); [Smart Canned Jobs](https://support.autovitals.com/hc/en-us/articles/51041681108628-Using-Smart-Canned-Jobs-with-AutoVitals-Tekmetric-Integration)).
- **Tekmetric Smart Canned Jobs.** These resolve labor (Tekmetric guide) and parts per vehicle. AutoVitals shows no visual difference between smart and standard jobs, and the job name is customer-facing.
- **Recommendations in service reminders.** Three CRM modes:
  - declined jobs only;
  - unsold inspection recommendations;
  - all "Needs Immediate Attention" items, which AutoVitals warns may include work already done ([Recommendations From Inspections](https://support.autovitals.com/hc/en-us/articles/4415124929812-Recommendations-From-Inspections-on-TVP-X)).
- **Declined-job sources.** These depend on each POS's fields. Changes made after invoice close are not detected ([Recommendations & Declined Jobs](https://support.autovitals.com/hc/en-us/articles/4416143388308-Recommendations-Declined-Jobs)).
- **Otto Notes (AI).** Rewrites customer notes for clarity and grammar; it is not used on shop notes or measurements. It was auto-enabled for eligible packages from Feb 12, 2026, and shops can opt out ([Otto Notes](https://support.autovitals.com/hc/en-us/articles/46150691759124-Otto-Notes-AI-Powered-Customer-Notes)).

**6. Customer-facing report ("Inspection Results")**
- **Templates and layout.** Three layout templates, each with shop info, vehicle info, up to 4 "Offerings" (promos and financing) and results grouped by status, with expandable statuses ([Results Templates](https://support.autovitals.com/hc/en-us/articles/12869672914708-Inspection-Results-Templates); [Offerings](https://support.autovitals.com/hc/en-us/articles/12869700549780-Offerings-on-Inspection-Results)).
- **Template changes are retroactive.** Changing the template restyles all **historical links** too.
- **Jobs on the RO.** Optional "Services Being Performed" (relabelable) list of RO jobs ([Jobs Performed](https://support.autovitals.com/hc/en-us/articles/37727459578516-Display-Jobs-Performed-on-Inspection-Results)).
- **Per-topic content.** Photos with captions, customer notes and a "Why is this important" educational note/video.
- **Shop-eyes-only content.** Tech notes stay hidden until moved to customer notes and approved. A note-conflict icon flags tech-vs-advisor discrepancies ([Images/Notes Editor](https://support.autovitals.com/hc/en-us/articles/4408845974420-The-Images-Notes-Editor)).
- **Default vehicle image.** If no vehicle photo was taken, a stock car-with-stethoscope image appears ([2025 Release Notes](https://support.autovitals.com/hc/en-us/articles/33931313088532-2025-Release-Notes)).
- **Approval.** Handled through the host POS, or AutoVitals' estimate/payments features [INFERENCE; not fully documented].

**7. Exports and audit data**
- **Business Control Panel (BCP) KPIs** ([BCP KPIs](https://support.autovitals.com/hc/en-us/articles/6535417910164-Business-Control-Panel-BCP-List-of-KPIs)):
  - Inspection Rate and Inspection Sent Rate (repeat visits within 2 weeks excluded);
  - Avg Pictures per RO;
  - Edited Pictures per Inspection;
  - Avg Recommended Jobs per Inspection;
  - Recommendation Rate (canned jobs only);
  - Avg Customer Research Time (time customers spend on the results);
  - Canned Jobs Approved;
  - Jobs Completed on Tablet.
- **How the BCP counts.** Data is counted on RO **close date**, closed ROs only. The **highest revision number** of an inspection counts even if a lower revision was edited last ([BCP Inspection Data](https://support.autovitals.com/hc/en-us/articles/4454837777172-Business-Control-Panel-Inspection-Data)).
- **Built-in audit tool.** Rate images 0–5 on focus, arrow/circle, caption naming the part, caption naming the service, and reason to buy today. AutoVitals suggests auditing 2 inspections per staff member per pay period. Deactivating an inspection hides it unless "include deactivated" is checked ([Audit](https://support.autovitals.com/hc/en-us/articles/4406164881556-How-to-Audit-Digital-Inspections-on-TVP-x)).
- **Historical access after leaving.** A shop that leaves AutoVitals gets a historical URL, but **POS-embedded inspection links stop working** ([Historical](https://support.autovitals.com/hc/en-us/articles/11734690213524-Historical-Inspection-Results)).

**8. Known pitfalls**
- **Canned conditions.** Default status, action and note on conditions mean one tap produces color, recommendation and polished text. Wording identical across vehicles is a sign of this.
- **Mismatched evidence.** Photos can be moved or copied across topics and ROs, and inspections moved across ROs, so the "wrong vehicle media" risk is real. Check the plate/VIN photo and timestamps.
- **Auto-approved photos.** All photos show unless hidden; captions and notes need approval.
- **Carry Forward Confirm** can re-issue last visit's result unchanged.
- **Hidden status** silently removes items from the customer report.
- **Groove Glove notes** need approval and may not match the graphics if left unreviewed.
- **Hunter view differences.** Customer view omits "before" alignment values.
- **Over-inclusive reminders.** The "Needs Immediate Attention" reminder mode can re-recommend completed work.
- **Retroactive restyling.** A template change re-renders old links, so the current look is not proof of what was originally sent.

**9. How to recognize an AutoVitals report**
- Sections titled by shop-defined statuses (often "Needs Immediate Attention" / "Needs Future Attention" / "Good").
- "Why is this important" educational videos; an Offerings carousel; a "Services Being Performed" block.
- Image captions with arrows; date stamps on images; a car-with-stethoscope placeholder.
- Shop settings live at shop.autovitals.com ([Groove Glove](https://support.autovitals.com/hc/en-us/articles/5909835783956-How-To-Set-Up-Tire-Profiles-Groove-Glove-with-AutoVitals)). Customer result domain: [UNVERIFIED].

---

### 3.5 Bolt On Technology

**Company and product.**
- Founded in Pennsylvania. Its "Mobile Manager Pro" DVI shipped in 2013. Acquired by Performant Capital in 2021 ([Wikipedia, flagged for possible COI](https://en.wikipedia.org/wiki/Bolt_On_Technology)).
- "NextGear" is a standalone web DVI not tied to a POS ([Brake & Front End](https://www.brakeandfrontend.com/bolt-on-technology-introduces-nextgear/)). Protractor integration came in 2021 ([MOTOR](https://www.motor.com/2021/05/bolt-on-technology-now-integrates-with-protractor-shop-management-platform/)).
- The current site lists modules (Communications, Digital Inspections, Payments, Reporting, Reviews, Workflow), claims about 25 POS integrations and an AI phone advisor "MILES," and shows ©2026 ([boltontechnology.com](https://www.boltontechnology.com/)).
- A new iOS app shipped in 2026 ([App Store](https://apps.apple.com/us/app/bolton-technology/id6755896971)).

1. **Building:**
   - Documented: customizable inspections, from a tire report to a 50-point multipoint; canned notes and recommendations; techs on tablets ([What are DVIs](https://blog.boltontechnology.com/what-are-digital-vehicle-inspections)).
   - Template builder details: [UNVERIFIED].
2. **Grading:** green good / yellow OK or non-urgent / red bad or urgent ([blog](https://blog.boltontechnology.com/what-are-digital-vehicle-inspections); [Ratchet+Wrench 2018](https://ratchetandwrench.com/sponsored-content/bolt-on-technology/article/11476185/an-inside-look-at-your-vehicle-2018-10-24)). Measurement thresholds: [UNVERIFIED].
3. **Measurements:** none documented.
4. **Media:** photos and videos captured on mobile; a timestamped visual record per inspection; works offline then syncs ([NAPA TRACS listing](https://napatracs.com/extension/bolt-on-technology/)). Markup ("graphics") added to images ([blog](https://blog.boltontechnology.com/what-are-digital-vehicle-inspections)).
5. **Recommendations:** canned jobs speed estimates ([Optimizing DVI](https://blog.boltontechnology.com/optimizing-digital-vehicle-inspection-software)). Mapping to POS: [UNVERIFIED].
6. **Customer report:** sent by text or email; approval from the phone; tablet signature capture ([Mitchell 1 page](https://lp.boltontechnology.com/mitchell-1)). Layout: [UNVERIFIED].
7. **Exports/KPIs:** "Reporting" module exists; specific inspection KPIs: [UNVERIFIED].
8. **Pitfalls:** Bolt On's own content warns about unprioritized findings, poor photos, inconsistent tech standards and "problems-only" reports ([5 DVI Mistakes, Apr 2026](https://blog.boltontechnology.com/dvi-mistakes-that-kill-trust)). That doubles as an audit checklist.
9. **Fingerprint:** "BOLT ON" branding; green/yellow/red bars per system ([Ratchet+Wrench](https://ratchetandwrench.com/sponsored-content/bolt-on-technology/article/11476185/an-inside-look-at-your-vehicle-2018-10-24)). Link domain: [UNVERIFIED].

### 3.6 Integrations and add-ons (brief)

- **AutoVitals ↔ Tekmetric** (two-way, since Aug 2023). Pushes VIN, odometer, tech assignment, recommended canned jobs (as unapproved labor lines), customer notes/photos and the inspection URL. Nothing is sent until the advisor clicks UPDATE WO ([Tekmetric 2-Way](https://support.autovitals.com/hc/en-us/articles/17938877792404-Tekmetric-2-Way-Integration)).
- **AutoFlow → Tekmetric.** Only green/yellow/red items appear in Tekmetric's inspection tab. Image **markups do not carry over** (2023) ([AutoFlow help](https://autoflow.com/?p=21995446)). So the same inspection can look different in each system.
- **Tekmetric "Smart DVI"** (announced April 2026, coming soon). The tech narrates a video walkthrough; AI transcribes it, organizes images and drafts estimate items ([Ratchet+Wrench](https://www.ratchetandwrench.com/news/article/55370320/tekmetric-unveils-new-platform-innovations-at-tektonic-2026)).
- **Shopgenie.** CRM, online booking and an AI virtual advisor. Acquired by Tekmetric in Oct 2024 ([Axios](https://www.axios.com/pro/retail-deals/2024/10/16/tekmetric-acquires-shopgenie-auto-repair)). Not a DVI.
- **Steer.** CRM/marketing; listed as a Shop-Ware API partner ([API Partners](https://support.shop-ware.com/s/article/API-Partner-Integrations)). Not a DVI. Relevant only because declined-work reminders may come from these CRMs.

---

## 4) Common configuration/reporting failure modes and how an auditor detects each

| # | Failure mode | Platform mechanism (documented) | Detection signals |
|---|---|---|---|
| 1 | **Bulk "all green" / pencil-whipped inspection** | Tekmetric Rate All Tasks; Shop-Ware swipe-to-green | Many green/N/A items with no photos or findings; very short inspection time (Tekmetric Inspection Report avg time); Shopmonkey Items Rated % = 100 with zero media |
| 2 | **Carried-forward or copied results** | Tekmetric "Copy to this RO"; AutoVitals Carry Forward "Confirm" | Findings identical to the prior visit; photos dated a previous visit (AutoVitals date stamp); mileage in the cluster photo doesn't match the RO odometer |
| 3 | **Interval-driven color presented as condition** | Tekmetric Recommended Maintenance pre-rates Red/Yellow; Shopmonkey/MOTOR maintenance suggestions; BG presets | Overdue/due-soon pattern wording; filter, fluid or flush items red with no photo or measurement; ask "what did you observe?" and check the owner's manual interval and service history |
| 4 | **Canned condition text not matching the photo** | AutoVitals default customer note/caption; Shopmonkey Quick Notes; Tekmetric preset findings | Identical sentences across items or vehicles; caption names a part not visible; note describes the wrong side or axle |
| 5 | **Auto-added estimate lines** | Tekmetric red/yellow + mapped canned job auto-adds; AutoVitals Default Action pushes job | Estimate line for every yellow item; Smart Job labor from the guide; check each estimate line has a matching observed finding |
| 6 | **Wrong-vehicle or moved media** | AutoVitals move/copy photo or inspection to another RO; desktop file uploads (Tekmetric) | Plate/VIN/paint color/interior differ across photos; image timestamps outside the visit window; duplicate images across customers |
| 7 | **Hidden items or evidence** | AutoVitals Hidden status and image suppressor; Tekmetric internal inspections and hidden N/A; Shop-Ware unpublished drafts | Report item count lower than template size; ask the shop for the full (shop-view) inspection and the internal check-in inspection |
| 8 | **Missing measurements** | No structured fields in Tekmetric/Shopmonkey/Shop-Ware | "Worn"/"low" with no mm or 32nds; ask for gauge readings; compare to doc 07 technical criteria |
| 9 | **Advisor-edited or AI-polished text** | AutoVitals note-conflict icon and Otto Notes; Shop-Ware draft/publish and AutoWrite; Shopmonkey "Completed By" ≠ inspector | Polished, uniform prose; ask for tech notes/shop view; compare tech vs advisor versions |
| 10 | **Severity mismatch between layers** | Shop-Ware line color vs recommendation urgency; AutoVitals CRM "Needs Immediate" mode | Red urgency on a recommendation whose line is green/unrated; reminder emails for already-completed work |
| 11 | **Approval record gaps** | Shop-Ware Authorization Summary opt-in and off PDFs by default; Tekmetric method dropdown (phone/text with no signature); Shopmonkey price-increase reset is optional | Ask for the authorization history / point-in-time copy; check price at approval vs invoice |
| 12 | **Report re-rendering / link changes** | AutoVitals template change restyles old links; links stop after leaving; Tekmetric unshare | Don't treat the current link as the original; keep PDFs and screenshots with retrieval date |
| 13 | **Integration loss** | AutoFlow→Tekmetric drops markups; AutoVitals→POS sends only approved notes/photos | Compare DVI-native report to the POS copy |
| 14 | **Completion/KPI artifacts** | Shopmonkey "Complete" button; Tekmetric reports need posted RO; AutoVitals counts by close date and highest revision | Use the per-inspection detail rows, not dashboards, when reconstructing what happened |

---

## 5) Audit implications — consumer vs shop owner

**Consumer (has the report link/PDF, estimate, invoice):**
1. **Identify the platform** with section 9 fingerprints. That tells you which failure modes in section 4 apply.
2. **For each red/yellow item,** look for item-specific evidence: a photo of *your* car (plate, VIN, mileage photo) and a measurement where the item is measurable (tread, pads, rotors, battery). On Tekmetric, Shopmonkey and Shop-Ware, readings exist only if typed into notes, so ask for them.
3. **Check whether a recommendation is mileage/interval-based** ("overdue by…", maintenance schedule) or condition-based. Both may be legitimate, but they are different claims.
4. **Ask for the full inspection** (including N/A/hidden items and internal check-in photos) and the authorization record: method, time and price at approval.
5. **Save copies.** Links can be unshared or re-rendered.

**Shop owner (has system access):**
1. **Pull the platform's per-inspection data:**
   - Tekmetric: Inspection Report (time, findings, attachments, % viewed).
   - Shopmonkey: Vehicle Inspections Detail (inspectors vs Completed By, Items Rated %, Avg Finding %).
   - AutoVitals: BCP (pictures/RO, edited-picture rate, recommendation rate) plus the built-in audit tool.
   - Shop-Ware: unfulfilled-recommendation export.
2. **Review configuration:**
   - templates with default statuses/actions (AutoVitals);
   - mapped canned jobs that auto-add (Tekmetric/AutoVitals);
   - Recommended Maintenance rating defaults (Tekmetric Scale);
   - Hidden statuses;
   - Quick Notes/preset findings wording;
   - who may publish (Shop-Ware);
   - timestamp display (AutoVitals).
3. **Flag outliers:** techs with very high Avg Finding % or recommendation counts, very low inspection times, or very low photos per red item.
4. **Turn on stronger records:**
   - require digital signature (Tekmetric);
   - capture approval method/contact and include the Authorization Summary in PDFs (Shop-Ware);
   - reset authorization on price increase (Shopmonkey);
   - show image timestamps (AutoVitals);
   - make photos mandatory on red/yellow topics (AutoVitals topic options).

---

## 6) Open questions

1. Customer share-link domains and URL patterns for all five platforms. I could not confirm them publicly; a sample real report from each would settle it.
2. Do Tekmetric, Shopmonkey or Shop-Ware have any structured measurement item type (numeric tread/pad fields), even hidden or beta? None is documented, but absence of documentation is not proof.
3. AutoVitals measurement-field design: per-position tread (inner/middle/outer), units, whether readings auto-select a Condition/status, and whether a direct Midtronics integration exists (versus Hunter Quick Check battery data).
4. Bolt On's actual template builder, measurement support, customer report layout, approval record contents and KPIs. Public docs are minimal.
5. Shopmonkey custom statuses: how they are created and how they render to customers.
6. Whether Tekmetric's interval-based pre-ratings are visibly labeled as such on the customer report, or only show as red/yellow.
7. Whether AI rewrite tools (Otto Notes, AutoWrite, Tekmetric Smart DVI) leave any marker in the customer-facing output or audit log.
8. API field lists for inspection objects: Tekmetric public API inspection endpoint, Shop-Ware public API, and Shopmonkey v3 (inspection objects not confirmed).
9. Shop-Ware inspection-line color naming. The TechApp article says orange; web articles say yellow. Likely the same tier [INFERENCE].

---

## 7) Sources

**Tekmetric**
- Creating Inspections — https://support.tekmetric.com/hc/en-us/articles/360037472174-Creating-Inspections
- Performing an Inspection — https://support.tekmetric.com/hc/en-us/articles/360037472154-Performing-an-Inspection
- Mark Inspections as Default — https://support.tekmetric.com/hc/en-us/articles/16773448793751-Mark-Inspections-as-Default
- Link Canned Jobs to Inspections — https://support.tekmetric.com/hc/en-us/articles/1500011364982-Link-Canned-Jobs-to-Inspections
- DVI Enhancements That Drive Impact (Sept 2025) — https://support.tekmetric.com/hc/en-us/articles/35205687782423-DVI-Enhancements-That-Drive-Impact
- Recommended Maintenance on DVI — https://support.tekmetric.com/hc/en-us/articles/42955960801943-Recommended-Maintenance-on-DVI
- Recommended Jobs — https://support.tekmetric.com/hc/en-us/articles/41093244754199-Recommended-Jobs
- DVI: Image Markup — https://support.tekmetric.com/hc/en-us/articles/34327534094871-DVI-Image-Markup
- Inspection Report — https://support.tekmetric.com/hc/en-us/articles/9864603066519-Inspection-Report
- Internal Inspections — https://support.tekmetric.com/hc/en-us/articles/18139709709719-Internal-Inspections
- Digital Vehicle Inspection History — https://support.tekmetric.com/hc/en-us/articles/5178699794455-Digital-Vehicle-Inspection-History
- Digital Signature & Authorization Process — https://support.tekmetric.com/hc/en-us/articles/4421125978391-Digital-Signature-Authorization-Process
- Declined vs Draft Jobs — https://support.tekmetric.com/hc/en-us/articles/360039270153-What-is-the-difference-between-declined-jobs-draft-jobs
- Add Previously Declined Work — https://support.tekmetric.com/hc/en-us/articles/360056145094-How-Do-I-Add-Previously-Declined-Work-to-a-Repair-Order
- Mobile App: What's New — https://support.tekmetric.com/hc/en-us/articles/44090257340311-Mobile-App-What-s-New
- Tekmetric Mobile — https://support.tekmetric.com/hc/en-us/articles/26781766611351-Tekmetric-Mobile
- Labor Guide — https://support.tekmetric.com/hc/en-us/articles/360063488693-Labor-Guide
- ALLDATA Labor Guide Integration — https://support.tekmetric.com/hc/en-us/articles/25868623867927-ALLDATA-Labor-Guide-Integration
- Smart Jobs 101 — https://support.tekmetric.com/hc/en-us/articles/27373807531287-Smart-Jobs-101
- Estimate and Invoice Transparency Settings — https://support.tekmetric.com/hc/en-us/articles/360035798334-Estimate-and-Invoice-Transparency-Settings
- Adjust Verbiage for Texts — https://support.tekmetric.com/hc/en-us/articles/25416840474135-Adjust-Verbiage-for-Inspection-Estimate-Invoice-Texts
- The Customer Concern — https://support.tekmetric.com/hc/en-us/articles/36897066105111-The-Customer-Concern
- Tire DOT# Management — https://support.tekmetric.com/hc/en-us/articles/17119553542167-Tire-DOT-Management-in-Tekmetric
- Release Date & Feature Notes — https://support.tekmetric.com/hc/en-us/articles/360041785434-Release-Date-Feature-Notes
- DVI guide (2023) — https://tours.tekmetric.com/answers/digital-vehicle-inspection-guide
- Tektonic 2026 Smart DVI — https://www.ratchetandwrench.com/news/article/55370320/tekmetric-unveils-new-platform-innovations-at-tektonic-2026
- Tekmetric acquires Shopgenie (Axios) — https://www.axios.com/pro/retail-deals/2024/10/16/tekmetric-acquires-shopgenie-auto-repair

**Shopmonkey**
- Perform Inspections — https://support.shopmonkey.io/hc/en-us/articles/38743049848852-Perform-Inspections
- Inspection Templates — https://support.shopmonkey.io/hc/en-us/articles/38743088738452-Inspection-Templates
- Inspections in Techs Mobile App — https://support.shopmonkey.io/hc/en-us/articles/38743122026388-Inspections-in-Shopmonkey-for-Techs-Mobile-App
- Send Inspections to Customers — https://support.shopmonkey.io/hc/en-us/articles/38744430526612-Send-Inspections-to-Customers
- Customer E-Signatures on Inspections — https://support.shopmonkey.io/hc/en-us/articles/47883995635476-Customer-E-Signatures-on-Inspections
- Customer E-Signatures to Authorize Services — https://support.shopmonkey.io/hc/en-us/articles/38743424357652-Customer-E-Signatures-to-Authorize-Services
- Request Customer Authorization — https://support.shopmonkey.io/hc/en-us/articles/38743372579988-Request-Customer-Authorization
- Recommend Services on an Estimate — https://support.shopmonkey.io/hc/en-us/articles/38742880884756-Recommend-Services-on-an-Estimate
- Deferred Services — https://support.shopmonkey.io/hc/en-us/articles/38743421091988-Deferred-Services
- Manage Inspection Quick Notes — https://support.shopmonkey.io/hc/en-us/articles/38743018176148-Manage-Inspection-Quick-Notes
- Vehicle Inspections Detail Report — https://support.shopmonkey.io/hc/en-us/articles/44632017228948-Vehicle-Inspections-Detail-Report
- Vehicle Inspections Summary Report — https://support.shopmonkey.io/hc/en-us/articles/44632022471060-Vehicle-Inspections-Summary-Report
- DVI Master Series (Templates / Aligning / Reports) — https://support.shopmonkey.io/hc/en-us/articles/43553316659092 ; https://support.shopmonkey.io/hc/en-us/articles/43553515271572 ; https://support.shopmonkey.io/hc/en-us/articles/43553591811348
- HQ Inspection Templates Data Sharing — https://support.shopmonkey.io/hc/en-us/articles/43357106322964
- Maintenance Schedules — https://support.shopmonkey.io/hc/en-us/articles/38743045057172-Maintenance-Schedules
- Vehicle Parts & Labor Lookup — https://support.shopmonkey.io/hc/en-us/articles/38743038698388-Vehicle-Parts-Labor-Lookup
- ALLDATA Integration — https://support.shopmonkey.io/hc/en-us/articles/46833875823124-ALLDATA-Integration
- Shopmonkey API — https://support.shopmonkey.io/hc/en-us/articles/38743124485780-Shopmonkey-API
- Updates/Improvements (Apr 2025, Aug 2025, Apr 2026, May 2026) — https://support.shopmonkey.io/hc/en-us/articles/40018217207316 ; https://support.shopmonkey.io/hc/en-us/articles/42346343428628 ; https://support.shopmonkey.io/hc/en-us/articles/51946021436692 ; https://support.shopmonkey.io/hc/en-us/articles/51950286356756 ; https://support.shopmonkey.io/hc/en-us/articles/49055039153044
- Tires — https://help.shopmonkey.io/en/articles/5564534-how-do-tires-work-in-shopmonkey
- DVI demo page — https://www.shopmonkey.io/demo-digital-vehicle-inspections

**Shop-Ware**
- What is TechApp — https://support.shop-ware.com/s/article/What-is-TechApp-by-Shop-Ware
- How Do I Create a Recommendation — https://support.shop-ware.com/s/article/How-Do-I-Create-a-Recommendation
- How Can a Customer Respond — https://support.shop-ware.com/s/article/How-Can-A-Customer-Respond-to-a-Recommendation
- Recommendations: Urgency, Sorting, Totals — https://support.shop-ware.com/s/article/Recommendations-Urgency-Sorting-and-Viewing-Totals
- Recommendation Approvals — https://support.shop-ware.com/s/article/Does-Shop-Ware-Capture-Recommendation-Approvals
- Getting Started — https://support.shop-ware.com/s/article/Getting-Started-Repair-Orders-and-Appointments
- eCommerce for Estimates and Recommendations — https://support.shop-ware.com/s/article/Using-eCommerce-for-Estimates-and-Recommendations
- API Partner Integrations — https://support.shop-ware.com/s/article/API-Partner-Integrations
- Declined work tracking FAQ — https://support.shop-ware.com/s/article/Are-You-Able-to-Track-Declined-Work-Or-Estimated-Work-per-Invoice-Can-You-Look-at-Daily-and-Weekly-Declined-Sales
- Declined work reminders FAQ — https://support.shop-ware.com/s/article/If-a-Customer-Declines-Work-Will-Shop-Ware-Still-Send-an-Email-or-Text-Remind-Them-of-Needed-Work
- Approved total FAQ — https://support.shop-ware.com/s/article/When-a-Client-Approves-Repairs-Online-Do-They-See-the-Total-Revised-Amount
- Technician Report — https://support.shop-ware.com/s/article/What-is-the-Technician-Report-in-Shop-Ware
- Product Updates (release notes v10.10 to v13.4, 2023–2026) — https://support.shop-ware.com/s/product-updates
- DVX feature page — https://shop-ware.com/features/dvx/
- DVI vs DVX — https://shop-ware.com/features/dvx/digital-vehicle-inspection-vs-dvx/
- TechApp feature page — https://shop-ware.com/features/techapp/
- DVX innovations (Oct 2024) — https://shop-ware.com/digital-vehicle-inspections-dvi-innovations-shop-ware/
- Best DVI software (Mar 2025) — https://shop-ware.com/best-digital-vehicle-inspection-software/
- Vehlo acquires Shop-Ware (Mar 2024) — https://www.vehicleservicepros.com/industry-news/news/53099000/shop-ware-acquired-by-vehlo

**AutoVitals**
- Inspection Builder — https://support.autovitals.com/hc/en-us/articles/4406522377876-AutoVitals-Inspection-Builder
- Starting an Inspection from Tablet — https://support.autovitals.com/hc/en-us/articles/24804398734868-Starting-an-Inspection-from-the-Mobile-App-Tablet
- Recommendations From Inspections — https://support.autovitals.com/hc/en-us/articles/4415124929812-Recommendations-From-Inspections-on-TVP-X
- Recommendations & Declined Jobs — https://support.autovitals.com/hc/en-us/articles/4416143388308-Recommendations-Declined-Jobs
- Timestamps on Customer Inspection Results — https://support.autovitals.com/hc/en-us/articles/4418702821524-Timestamps-on-Customer-Inspection-Results
- How to Audit Digital Inspections — https://support.autovitals.com/hc/en-us/articles/4406164881556-How-to-Audit-Digital-Inspections-on-TVP-x
- Inspection Results Templates — https://support.autovitals.com/hc/en-us/articles/12869672914708-Inspection-Results-Templates
- Offerings on Inspection Results — https://support.autovitals.com/hc/en-us/articles/12869700549780-Offerings-on-Inspection-Results
- Historical Inspection Results — https://support.autovitals.com/hc/en-us/articles/11734690213524-Historical-Inspection-Results
- Carry Forward — https://support.autovitals.com/hc/en-us/articles/4401760600340-Carry-Forward-AutoVitals-X-app
- Images/Notes Editor — https://support.autovitals.com/hc/en-us/articles/4408845974420-The-Images-Notes-Editor
- BCP Inspection Data — https://support.autovitals.com/hc/en-us/articles/4454837777172-Business-Control-Panel-Inspection-Data
- BCP List of KPIs — https://support.autovitals.com/hc/en-us/articles/6535417910164-Business-Control-Panel-BCP-List-of-KPIs
- DVI Photo Best Practices — https://support.autovitals.com/hc/en-us/articles/8754627477012-AutoVitals-DVI-Photo-Best-Practices
- Groove Glove setup — https://support.autovitals.com/hc/en-us/articles/5909835783956-How-To-Set-Up-Tire-Profiles-Groove-Glove-with-AutoVitals
- Hunter Alignment setup — https://support.autovitals.com/hc/en-us/articles/4414874909716-How-to-Set-Up-Hunter-Alignment-With-AutoVitals
- Move Inspection to Different RO — https://support.autovitals.com/hc/en-us/articles/4410220960788-How-to-Move-an-Inspection-to-a-Different-RO-on-TVP-x
- Basic Training 6 (Inspection Editing) — https://support.autovitals.com/hc/en-us/articles/27719371914388-AutoVitals-Basic-Training-6-Inspection-Editing
- Basic Training 8 (Moving Inspections & Photos) — https://support.autovitals.com/hc/en-us/articles/27703698371476-AutoVitals-Basic-Training-8-Moving-Inspections-Photos
- Tekmetric 2-Way Integration — https://support.autovitals.com/hc/en-us/articles/17938877792404-Tekmetric-2-Way-Integration
- Smart Canned Jobs with Tekmetric — https://support.autovitals.com/hc/en-us/articles/51041681108628-Using-Smart-Canned-Jobs-with-AutoVitals-Tekmetric-Integration
- Display Jobs Performed — https://support.autovitals.com/hc/en-us/articles/37727459578516-Display-Jobs-Performed-on-Inspection-Results
- 2025 Release Notes — https://support.autovitals.com/hc/en-us/articles/33931313088532-2025-Release-Notes
- 2026 Release Notes — https://support.autovitals.com/hc/en-us/articles/45299274011540-2026-Release-Notes
- Otto Notes — https://support.autovitals.com/hc/en-us/articles/46150691759124-Otto-Notes-AI-Powered-Customer-Notes

**Bolt On Technology**
- Home — https://www.boltontechnology.com/
- Digital Inspections product page — https://www.boltontechnology.com/products/digital-vehicle-inspections/
- What are DVIs (blog) — https://blog.boltontechnology.com/what-are-digital-vehicle-inspections
- Optimizing DVI Software (blog) — https://blog.boltontechnology.com/optimizing-digital-vehicle-inspection-software
- 5 DVI Mistakes (Apr 2026) — https://blog.boltontechnology.com/dvi-mistakes-that-kill-trust
- Mitchell 1 + Bolt On — https://lp.boltontechnology.com/mitchell-1
- NAPA TRACS extension listing — https://napatracs.com/extension/bolt-on-technology/
- App Store listing — https://apps.apple.com/us/app/bolton-technology/id6755896971
- Wikipedia (COI-flagged) — https://en.wikipedia.org/wiki/Bolt_On_Technology
- NextGear launch — https://www.brakeandfrontend.com/bolt-on-technology-introduces-nextgear/
- Protractor integration (2021) — https://www.motor.com/2021/05/bolt-on-technology-now-integrates-with-protractor-shop-management-platform/
- Ratchet+Wrench sponsored (2018) — https://ratchetandwrench.com/sponsored-content/bolt-on-technology/article/11476185/an-inside-look-at-your-vehicle-2018-10-24

**Cross-platform**
- AutoFlow → Tekmetric integration (2023) — https://autoflow.com/?p=21995446
