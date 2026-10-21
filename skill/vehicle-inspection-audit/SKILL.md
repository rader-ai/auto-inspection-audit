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

Helpful if offered, but don't hold up the audit for it: maintenance history (a "due" flush done 10k miles ago is an error), how long they plan to keep the car (changes the value of Suggested items), budget constraints (helps prioritize).

**Shop-owner intake** is different: which technician and advisor, single inspection or a batch, what prompted the audit (customer complaint, routine QA sample, new hire, comeback), which platform they use, and whether they want coaching notes, a compliance check, or both.

If the user just wants a quick read and doesn't answer, proceed — state your assumptions at the top of the audit and flag which conclusions would change if an assumption is wrong.

If the user shares personal details (name, phone, address, plate), don't repeat them back in the audit.

### 2. Extract a line-item table

Before judging anything, transcribe every inspection item and estimate line into a working table: item, position (LF/RF/LR/RR, front/rear), grade/color, measurement + unit, technician note, photo/video reference, recommendation, price/labor. Note items that are graded but have no note, and estimate lines with no matching inspection finding. Getting the facts down first prevents you from reasoning from the scariest line on the page.

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

Two limits matter a lot here. First, read a measuring tool only when its scale is legible in the photo — never estimate tread depth, pad thickness, or rotor wear by eye. Even purpose-built scanners are only accurate to about 1/32", and the decision points (2/32", 4/32", ~2–3 mm pads) are that close together. Second, you can't read image metadata or detect edited or AI-generated images, so never call a photo fake. You can point out that a photo seems to show a different vehicle (wrong tire size, wheel, or paint), appears twice for different items, or doesn't show the claimed component — those are observable facts.

### 7. Cross-report consistency

Look across the whole report: same photo used for multiple items, all four tires with identical readings, measurements that are physically implausible (pads thicker than new), grades that disagree with measurements, a sudden jump from a prior inspection, estimate lines with no supporting finding, and totals that don't add up.

### 8. Paperwork and compliance

Check the estimate/authorization/invoice against the rules for the user's jurisdiction: `references/state-repair-laws.md` (all states, comparison table), `references/california-bar.md` (deepest coverage — California has the most detailed rules), `references/federal.md` (emissions/catalytic converters, safety-system disabling, odometer, warranty), and `references/commercial-fleet.md` for commercial, rideshare, school bus, or fleet vehicles. State-mandated safety/emissions inspections have their own pass/fail criteria in `references/state-inspection-programs.md` — when available, those official reject criteria are a useful objective benchmark for a shop's "red" findings even outside a state inspection.

Typical checks: written estimate before work, documented authorization (who/when/how, including for text-link approvals), authorization for any overage, itemized invoice, used/rebuilt parts disclosed, old parts offered back, shop registration number where required, vague "shop supplies" fees.

### 9. Write the audit

Use the report template below. Lead with what matters most to this user, keep jargon explained, and make next steps concrete.

## Report template

```
# Inspection Audit — [Year Make Model], [mileage] mi — [Shop name if given], [date]

## Bottom line
2–4 sentences: overall evidence quality, how many recommendations are well supported vs. questionable, and anything safety-related that needs attention now.

## Scorecard
| | Count |
|---|---|
| Items reviewed | |
| Supported (required) | |
| Supported – optional | |
| Evidence missing | |
| Inconsistent | |
| Beyond OEM schedule | |
| Not applicable to this vehicle | |
| Needs OEM spec | |
| Verify in person – safety | |
Estimated $ by status (if prices given): Supported $__ / Optional $__ / Questionable $__

## Safety items — verify promptly
(Anything with a credible safety implication, whatever its documentation quality.)

## Line-item review
| # | Item / position | Shop says | Evidence (rating) | Spec / schedule | Status | Why |
|---|---|---|---|---|---|---|

## Photo & documentation findings
Platform identified (and what that implies), photo issues, cross-report inconsistencies.

## Paperwork & compliance ([state])
What the rules generally require vs. what the documents show. Not legal advice.

## [Consumer] Questions to ask the shop / Next steps
## [Shop owner] Coaching notes, process fixes, and what to verify
```

**Consumer next steps** typically include: specific questions per questionable item ("What was the LF pad measurement in mm, and what's the minimum for this vehicle?"), asking for the old parts or photos, checking the owner's manual schedule, getting a second opinion on large or safety items, approving only Supported items now, and — if a dispute arises — the escalation path in `references/consumer-protection.md` (written request to the shop, then the state regulator, card dispute, small claims).

**Shop-owner next steps** typically include: per-technician coaching points, template/configuration fixes in the DVI platform (required measurement fields, removing default grades, separating menu maintenance from condition findings), advisor presentation issues (Suggested items sold as Required), documentation gaps that create regulatory exposure, and under-recommendations that missed needed work. For multi-inspection QA programs (sampling, second-tech verification, scoring rubrics, accuracy-based KPIs), see `references/industry-standards.md`.

## Auditing several inspections (shop-owner mode)

When given multiple inspections, audit each, then summarize patterns: findings per technician, how often grades lack measurements, recommendation rate normalized by mileage, repeated canned text, and the share of each status. The point is to separate one-off mistakes from template or incentive problems. Report rates, not just anecdotes.

## Reference files

Read only what the audit needs:

| File | Read when |
|---|---|
| `references/technical-criteria.md` | Every audit — per-system tests, thresholds, red flags, impossible items, commonly upsold services |
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
