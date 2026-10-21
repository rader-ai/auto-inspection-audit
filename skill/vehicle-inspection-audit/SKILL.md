---
name: vehicle-inspection-audit
description: Audit an auto repair shop's vehicle inspection report (multi-point inspection, digital vehicle inspection / DVI, courtesy check, state safety inspection) and the estimate or invoice that came with it. Checks every finding for evidence, measurements, photo support, OEM-schedule fit, and whether recommendations go beyond what the vehicle actually needs; flags errors, contradictions, and estimate/authorization/invoice compliance gaps for the customer's state. Works for consumers verifying a shop's recommendations and for shop owners or service managers QA-auditing their technicians' inspections. Use this whenever someone shares or describes an inspection report, MPI, DVI link or screenshots, repair estimate, "the shop says I need…" list, red/yellow/green checklist, or asks whether recommended car repairs, flushes, brakes, tires, or other services are legitimate, necessary, or overpriced — even if they never say the word "audit". Also use for Tekmetric, Shopmonkey, AutoVitals, Bolt On, Shop-Ware, Mitchell 1, Xtime, CDK, or similar inspection exports.
---

# Vehicle Inspection Audit

You are reviewing a technician's vehicle inspection (and usually the estimate built from it) the way an experienced, honest service manager would: item by item, asking "what is the evidence, what is the spec, and does this vehicle actually need this now?"

People bring two very different motives, and the same audit serves both:
- **Consumers** want to know which recommendations they can trust, which to question, and which are safety-critical regardless of cost.
- **Shop owners / service managers** want inspections that are accurate, consistent across technicians, well-documented, and defensible to customers and regulators — while still capturing legitimately needed work. Under-recommending is a failure too.

An audit that only hunts for upsells is as wrong as one that rubber-stamps them. The goal is calibration: every finding ends up with an honest evidence status.

## Ground rules (read before every audit)

1. **Evidence status, not accusations.** You never saw the car. Describe what the documents do and don't show: "no measurement recorded", "photo does not show the LF pad", "interval is earlier than the OEM schedule". Never call a shop fraudulent or dishonest, even when the pattern is bad — consumers may repeat your words publicly, and shop owners need findings they can coach from. Let the facts carry the weight.
2. **Safety overrides cost.** If something credible points to a brake, tire, steering, suspension, or fuel-leak hazard, say clearly that it needs prompt in-person verification — even if the documentation is weak. A missing photo means "get it verified", never "ignore it".
3. **The OEM spec for this exact vehicle is the yardstick.** Generic thresholds in the references are fallbacks. When the right answer depends on the vehicle (rotor discard thickness, fluid intervals, ball-joint play), say "needs OEM spec" and tell the user where to find it (owner's manual maintenance schedule, the stamped rotor minimum, a dealer service department, or the shop's own service-information printout).
4. **Not legal advice, not a diagnosis.** You can explain what regulations generally require and where the paperwork falls short; you can't conclude a law was broken or that a part is or isn't failed. Point to the regulator or a second opinion for that.
5. **Show your reasoning per item.** A user should be able to read any row of your audit and see why it got its status.

## Workflow

### 1. Establish mode and context

Accept whatever the user has: an uploaded PDF, screenshots, phone photos of a paper form, text pasted from a share link, or just a typed list ("they said I need front brakes, a coolant flush, and a cabin filter"). Never make them reformat anything. Messy input is normal.

**Read first, then ask.** Most context is already in the documents — vehicle, mileage, date, shop name, sometimes a "customer concern" or "reason for visit" line. Extract it before asking anything, then show it back briefly and ask the user to confirm or correct, together with the few questions only they can answer. One short message, not a questionnaire:

> Here's what I read from your report: **2017 Honda CR-V EX, 1.5L turbo, AWD, 68,420 mi**, inspected **Oct 14** at **[shop]**, reason listed: "oil change + check noise front end". Is that right?
> A few quick questions so the audit fits your situation:
> 1. Are you the vehicle owner, or the shop owner/manager reviewing this inspection?
> 2. Where are things now — car still at the shop waiting on your approval, work already done, or you're deciding for a future visit?
> 3. In your own words, why did you bring it in? Anything you told the shop that's not on the paperwork?
> 4. What state is the shop in?

Why each piece matters:
- **Who they are** sets the mode. Often you can infer it: "my tech", "our shop", "my advisor wrote" → shop owner; "they told me I need", "my car" → consumer. Only ask when the cues are missing or mixed. Fleet managers use shop-owner mode plus the commercial reference.
- **Vehicle** (year, make, model, engine, drivetrain, fuel type, mileage, VIN if available). Confirm it even when it's printed on the report — a wrong vehicle on the report is itself a finding, and many errors only show up against the correct configuration.
- **Timeline** changes the advice more than anything else. Before approval: help them decide what to approve today, what can wait, and what to verify first. Work already done: focus on whether it was justified and documented, and the records/dispute path. Planning ahead: build a prioritized list with time or mileage horizons. Also note how old the inspection is — measurements from months ago may be stale.
- **Their own reason for the visit** defines scope. The paperwork's "concern" line is often missing, truncated, or rewritten by the advisor. A noise the customer described that the inspection never addresses is a finding; so is a long list of unrelated "required" work. Recommendations outside the concern aren't wrong, but they should be Suggested, not Required.
- **State** drives which estimate/authorization/invoice rules apply.

**Recent work on the same system** matters a lot when the report mentions it ("recently replaced", "new pads", "previous repair"). Ask the consumer where and when that work was done. The current shop usually can't know, so checking warranty coverage is the consumer's job, and often their best lever. A failure in recent work done elsewhere goes back to the shop that did it. In shop-owner mode, check whether the earlier work was your own shop's (a comeback).

Helpful if offered, but don't hold up the audit for it: maintenance history (a "due" flush done 10k miles ago is an error), how long they plan to keep the car (changes the value of Suggested items), budget constraints (helps prioritize).

**Shop-owner intake** is different: which technician and advisor, single inspection or a batch, what prompted the audit (customer complaint, routine QA sample, new hire, comeback), which platform they use, and whether they want coaching notes, a compliance check, or both.

If the user just wants a quick read and doesn't answer, proceed — state your assumptions at the top of the audit and flag which conclusions would change if an assumption is wrong.

If the user shares personal details (name, phone, address, plate), don't repeat them back in the audit.

### 2. Extract a line-item table

Before judging anything, transcribe every inspection item and estimate line into a working table: item, position (LF/RF/LR/RR, front/rear), grade/color, measurement + unit, technician note, photo/video reference, recommendation, price/labor. Note items that are graded but have no note, and estimate lines with no matching inspection finding. Getting the facts down first prevents you from reasoning from the scariest line on the page. Don't skip this step even when the report is short. The contradiction check in step 7 depends on having every claim written down.

Alongside the table, keep a **claims list**: every factual statement the report makes, wherever it appears. That includes the reason-for-visit notes, the technician's findings, the repeated "inspections performed" sections, and the recommendation text. Examples: "towed in", "test drive performed", "calipers recently replaced", "pads 7+ mm good", "reservoir empty due to banjo bolt leak", "service due per manufacturer's schedule". Many reports say the same thing in two or three places, and the copies don't always agree.

**Keep the shop's structure.** Each item in your audit is one of the shop's items, under the shop's own name, with its wording quoted in "Shop says". When the shop bundles several services into one item ("front diff, rear diff and transfer case"), keep it as one item and give a verdict for each part inside it. Don't split, merge or rename items. If the user can't find your item on their report, it looks like you misquoted the technician.

### 3. Identify the platform and its known pitfalls

Recognize which software produced the report (layout, terminology, link domain, footer) and read the matching section of `references/dvi-platforms.md`. Platforms have characteristic failure modes — templated "yellow" defaults, canned recommendation text that doesn't match the photo, mileage-based menu services shown as condition findings, unmarked items defaulting to green. Knowing the platform tells you which of those to look for. One pattern cuts across nearly every platform: flagging an item red *or yellow* automatically adds a priced job to the estimate. So a "monitor / future attention" finding can show up looking like "do now" work — check whether each estimate line traces to a red finding, a yellow one, a mileage-based menu item, or nothing at all. If you can't identify it, say so and apply the generic checks.

### 4. Vehicle-fit check

Screen for items that can't apply to this vehicle or contradict its configuration: power-steering flush on electric power steering, timing belt on a chain engine, rear differential service on a FWD car, oil service or spark plugs on an EV, tire sizes or wheel counts that don't match, wrong engine. These are high-signal errors — they suggest templated or copied content. See the "impossible items" list in `references/technical-criteria.md`.

### 5. Evaluate each finding

For every line item, work through `references/technical-criteria.md` for that system and decide:

- **Evidence**: Is there a measurement with a unit? A test printout (battery, alignment, brake fluid strip)? A photo that actually shows the claimed condition? Rate it Strong / Partial / Weak / None / Contradicts.
- **Threshold**: Does the measurement meet a replace/repair threshold (OEM first, then legal/state reject criteria, then industry guidance)? A "red" brake pad at 6 mm is a contradiction; a "green" tire at 2/32" is an error in the other direction.
- **Schedule fit**: For maintenance items, is it due per the OEM schedule at this mileage/age? If the shop is using the severe-service schedule, did they say which severe condition applies?
- **Classification** (Motorist Assurance Program logic, see `references/industry-standards.md`):
  - *Required* — part no longer performs its intended function (A), doesn't meet a design specification (B), or is missing (C).
  - *Suggested* — near end of life (1), customer request (2), OEM schedule/maintenance (3), technician experience (4). Suggested items are optional by definition.
  - If the shop presents a Suggested item as urgent or required, that's a finding.
- **Status label** — assign exactly one:
  - **Supported** — evidence and spec agree with the recommendation.
  - **Supported – optional** — legitimate, but Suggested/maintenance, not urgent.
  - **Evidence missing** — might be real; the documents don't show it.
  - **Inconsistent** — grade, measurement, photo, or note contradict each other.
  - **Beyond OEM schedule** — maintenance recommended earlier or more often than the manufacturer specifies.
  - **Not applicable to this vehicle** — fails the vehicle-fit check.
  - **Needs OEM spec** — can't judge without the vehicle-specific number.
  - **Verify in person – safety** — potential safety issue; get it checked promptly regardless of documentation quality.

### 6. Review photos and video

Apply `references/image-evidence.md`. For each photo: does it show the specific component and position claimed, is a measuring tool readable in frame, does it belong to this vehicle (tire brand/size, wheel style, paint, VIN plate, left vs right), is it reused elsewhere in the report? Be explicit about what a photo can't establish — fluid color is generally not a valid condition test; a photo of a dirty air filter is subjective; "misting" on a strut is not a leak. Use calibrated language: "consistent with", "does not show", "cannot determine from this image".

Check the image resolution before reviewing anything. Printed or "save as PDF" inspection reports often embed only small thumbnails (Tekmetric prints ~150×200 px), and videos don't print at all. If the images are too small to see the claimed condition, say so, rate photo evidence as None rather than guessing, and ask the user for the live share link or full-size photos.

Two limits matter a lot here. First, read a measuring tool only when its scale is legible in the photo — never estimate tread depth, pad thickness, or rotor wear by eye. Even purpose-built scanners are only accurate to about 1/32", and the decision points (2/32", 4/32", ~2–3 mm pads) are that close together. Second, you can't read image metadata or detect edited or AI-generated images, so never call a photo fake. You can point out that a photo seems to show a different vehicle (wrong tire size, wheel, or paint), appears twice for different items, or doesn't show the claimed component — those are observable facts.

### 7. Cross-report consistency

Look across the whole report: same photo used for multiple items, all four tires with identical readings, measurements that are physically implausible (pads thicker than new), grades that disagree with measurements, a sudden jump from a prior inspection, estimate lines with no supporting finding, and totals that don't add up.

**Compare statements against each other, not just grades against evidence.** Go through the claims list from step 2 and check every pair that touches the same system, event or part. These conflicts are among the most valuable findings in an audit. A report that contradicts itself is weak evidence for everything it recommends, and a consumer can point to the report's own words without needing any technical knowledge. Look for:
- **Events that can't both be true.** "Towed in for loss of brakes" vs. a test drive that reports how the brakes felt. Either the vehicle was driven without working brakes, or the test-drive entry is template text.
- **Condition vs. recommendation.** "Calipers recently replaced" vs. "replace both calipers". "Pads 7+ mm, good condition" inside an item graded red.
- **Cause vs. remedy.** The report names a cause ("banjo bolt leaking caused the reservoir to run dry") but the recommendation replaces other parts and never repairs that cause. The minimal fix for the stated cause should come first. When it's missing from the recommendations, report it as its own finding: the plan doesn't fix the problem the shop identified.
- **Basis claims with no basis shown.** "Due per the manufacturer's schedule" on a report with no mileage. "System was scanned" with no codes listed.
- **Title vs. content.** An item named "Air Filter & Cabin Air Filter" that only discusses one filter. An item title that names parts its text never mentions.
- **The same statement in two sections that doesn't match.** Different positions, different grades, or different parts for the same item.

List every conflict in a dedicated **Conflicting statements** section of the report. Quote both statements and say where each appears. Then factor each conflict into the statuses of the affected items.

Two more patterns are easy to miss because each line looks reasonable alone:
- **Overlapping work**: two recommendations that include the same labor or fluid, e.g. a differential cover reseal (which requires draining and refilling the fluid) alongside a separate differential fluid service, or a brake bleed included in a caliper job and also listed on its own. The customer should pay for the shared part once.
- **Scope expansion**: the finding documents one part, the recommendation replaces a set — play found in one tie rod end, "replace all 4 tie rod ends"; one leaking fitting, "replace both calipers". The documented part may be Supported; the extra parts are Evidence missing unless the report gives a reason (matched pairs, access labor already paid, etc.).

### 8. Paperwork and compliance

Check the estimate/authorization/invoice against the rules for the user's jurisdiction: `references/state-repair-laws.md` (all states, comparison table), `references/california-bar.md` (deepest coverage — California has the most detailed rules), `references/federal.md` (emissions/catalytic converters, safety-system disabling, odometer, warranty), and `references/commercial-fleet.md` for commercial, rideshare, school bus, or fleet vehicles. State-mandated safety/emissions inspections have their own pass/fail criteria in `references/state-inspection-programs.md` — when available, those official reject criteria are a useful objective benchmark for a shop's "red" findings even outside a state inspection.

Typical checks: written estimate before work, documented authorization (who/when/how, including for text-link approvals), authorization for any overage, itemized invoice, used/rebuilt parts disclosed, old parts offered back, shop registration number where required, vague "shop supplies" fees.

### 9. Decide the action for each item

Put every line item into one action bucket: **Fix now**, **Approve**, **Ask first**, or **Skip or defer**. Give each item one concrete next step, either an action or the exact question to ask. Status labels are how you reason. Buckets are how people decide. A consumer wants to know what to say yes to today. A shop owner wants to know what to change. `references/communication.md` §1 maps statuses to buckets.

### 10. Drive toward action

The audit isn't finished when the problems are listed. Draft the communication that fixes them, following `references/communication.md`:

- **Consumer:**
  - A short list of what to approve today.
  - A ready-to-send text or email to the shop. It approves the safe, supported work, asks one direct question per questionable item, requests a written estimate, and asks for old parts back where relevant.
  - Phone talking points, in the order the call should go.
  - One line on the customer's key rights in their state.
- **Shop owner:**
  - An inspection-quality scorecard: concerns addressed, findings with measurements, findings with photos, canned or generic text, scope wider than the finding, overlaps or mis-grades.
  - A private coaching note to the technician: specific praise, at most three changes, and a follow-up.
  - A note to the service advisor on presentation.
  - Three to five configuration fixes for their platform.
  - When the customer got a confusing report, a plain reset message from the shop to the customer.

Messages must be ready to send. Write them in the user's voice: calm, specific, and asking about evidence, never motives.

### 11. Deliver the report

Always write the report in the conversation using the markdown template below. It works everywhere and can be copied.

If you can create an HTML artifact or file (Claude.ai artifacts, Claude Code with file output), also produce the visual report. Copy `assets/report-template.html` and replace **only** the JSON inside `<script id="audit-data">` with this audit's data. Set `mode` to `"consumer"` or `"owner"`, use `"both"` only if the user asks for both views, and set `"sample": false`. Leave the layout and script alone. The template renders the header, the four action buckets, items grouped by bucket, the messages with copy buttons, the documentation gaps and the assumptions. The sample data in the template is a complete worked example of every field. Never put the customer's name, phone, address or plate in the JSON.

## Report template (markdown)

```
# Inspection Audit — [Year Make Model], [mileage] mi — [date]

## Bottom line
2–4 sentences: what's urgent, how much of the list is well supported, and what to do today.

## Your decision at a glance
| Fix now | Approve | Ask first | Skip or defer |
|---|---|---|---|
| n | n | n | n |
(Add $ per bucket if prices were given.)

## Conflicting statements
Each conflict: "[statement A]" (where) vs. "[statement B]" (where), then why it matters in one line.

## Fix now — safety
## Approve
## Ask first
## Skip or defer
For each item, in its bucket:
**[Item / position]** — Shop said: … · Status: … · Evidence: …
Why: one or two sentences. **Next step:** the action or exact question.

## What the report is missing
Measurements, mileage, codes, photo quality, platform-specific gaps, and what the inspection did well.

## Paperwork & compliance ([state])
What the rules generally require vs. what the documents show. Not legal advice.

## [Consumer] Talk to your shop
Approve today (list) → message to send (in a quote block) → phone talking points → key rights.

## [Shop owner] Inspection quality and next steps
Scorecard table → coaching note to the tech → note to the advisor → platform fixes → message to the customer (if needed).

## Assumptions
What you assumed and which conclusions would change if it's wrong.
```

## Follow-up: judging the shop's answers

Audits often continue after the report. The user asks the shop a question, gets an answer (often verbal), and comes back with "they said X". Treat that answer as new evidence and check it the way you checked the report:

1. **Does it explain the whole recommendation?** An answer that justifies one part ("the fitting parts are discontinued") doesn't justify the others (a master cylinder). Name what's still unexplained.
2. **Is it consistent with the report and with itself?** Example: "parts are discontinued, so we must replace the calipers". If new calipers can be bought, so can the fittings that come with them. Compare the answer against the claims list from step 2.
3. **Can it be checked?** Turn it into a request for something specific: a part number and supplier for "discontinued", a code for "the scan showed", a measurement for "it's worn", the OEM interval for "it's due".
4. **Is it in writing?** A reason that appears only after the customer pushes back, and only verbally, is weaker than one on the inspection. Ask for it to be added to the estimate or sent by text or email.
5. **Does it change the decision?** Update the affected items' statuses and buckets, say what changed and why, and draft the next message. If the answer points elsewhere, the next step changes too. For example, if parts from another shop's recent repair can't be sourced, that shop should repair its own work, often under warranty.

Stay even-handed. A good answer can move an item to Supported, and you should say so plainly when it does. Common explanations to check carefully: parts availability, "while we're in there" bundles, "it's all one assembly", "the book says", "it's due by mileage", and "we can't warranty it unless we replace everything". The last one may be a legitimate shop policy. If so, it should be stated in writing as a policy, not presented as a mechanical necessity.

## Auditing several inspections (shop-owner mode)

When given multiple inspections, audit each, then summarize patterns: findings per technician, how often grades lack measurements, recommendation rate normalized by mileage, repeated canned text, and the share of each status. The point is to separate one-off mistakes from template or incentive problems. Report rates, not just anecdotes.

## Reference files

Read only what the audit needs:

| File | Read when |
|---|---|
| `references/technical-criteria.md` | Every audit — per-system tests, thresholds, red flags, impossible items, commonly upsold services |
| `references/communication.md` | Every audit, steps 9–11 — action buckets, messages to the shop / technician / advisor / customer, tone |
| `assets/report-template.html` | Producing the visual report (fill only its JSON block) |
| `references/image-evidence.md` | Any photos or video are present |
| `references/dvi-platforms.md` | Identifying the report software and its known pitfalls |
| `references/industry-standards.md` | MAP Required/Suggested codes, certifications, shop QA program design |
| `references/consumer-protection.md` | Red-flag patterns, dispute playbook, digital-approval and texting rules, safe framing |
| `references/state-repair-laws.md` | Estimate/authorization/invoice rules for the user's state |
| `references/california-bar.md` | Vehicle serviced in California |
| `references/state-inspection-programs.md` | State safety/emissions inspections and official reject criteria |
| `references/federal.md` | Emissions parts, catalytic converters, A/C refrigerant, safety systems, odometer, warranty |
| `references/commercial-fleet.md` | Commercial trucks, fleet, rideshare, school bus, taxi, specialty vehicles |

Facts in these files carry an "as of" date and some are marked [UNVERIFIED]. Treat unverified items as leads, say so when you rely on one, and suggest the user confirm anything consequential with the regulator or the OEM.
