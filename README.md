# Vehicle Inspection Audit

An open Agent Skill for Claude that audits auto repair inspections, the multi-point or digital vehicle inspection (DVI) report a shop sends you, plus the estimate or invoice that comes with it.

- **Consumers** use it to check what the shop is recommending. Which items are backed by evidence, which are optional, which look out of scope, and which are safety items you shouldn't put off.
- **Shop owners and service managers** use it to quality-check their technicians' inspections. Are they accurate, consistent and documented well enough to defend to customers and regulators? It also flags work that was missed, not only work that was oversold.

## Why not just paste the PDF into a chatbot?

A general-purpose AI will read your inspection and give you a plausible opinion. This skill gives Claude a structured audit method and a sourced knowledge base:

1. **It asks about your situation first.** It reads what's already on the report (vehicle, mileage, date, stated concern), confirms it with you, and asks only what the documents can't tell it:
   - why you actually brought the car in
   - whether the work is still waiting on your approval or already done
   - what state the shop is in
   - whether you're the customer or the shop
2. **It checks every line item the same way.** For each one: what evidence is there, what does the spec or manufacturer schedule say, and is it Required or only Suggested? It uses the Motorist Assurance Program's classification for that last question.
3. **It knows the inspection software.** Tekmetric, Shopmonkey, AutoVitals, Shop-Ware, Mitchell 1, ALLDATA, CDK, Xtime, myKaarma and others each have quirks that show up in reports. Some examples:
   - a yellow "watch this" item automatically becomes a priced job on the estimate
   - mileage-based menu services get shown as if they were condition findings
   - items nobody checked default to green
   - customer notes get rewritten by AI
4. **It's careful with photos.** It reads a measurement only when a gauge is visible and legible. It never estimates wear by eye, and it checks that the photo matches your vehicle (tire size, wheels, paint, left vs. right).
5. **It checks the paperwork for your state.** Estimate, authorization, overage and invoice rules for all 50 states plus DC, with California's Bureau of Automotive Repair rules in depth. It also covers federal rules (catalytic converters, safety systems, odometer, warranty) and commercial and fleet requirements.
6. **It's fair to both sides.** Findings carry evidence labels (Supported, Evidence missing, Inconsistent, Beyond OEM schedule, Not applicable to this vehicle, Needs OEM spec, Verify in person – safety), never accusations. Safety items always come first, even when the documentation is weak.

## What you can give it

Anything you have: a PDF, screenshots of the inspection link, phone photos of a paper form, text pasted from the shop's message, or a typed list of what they told you. Add any photos or videos the shop sent.

Remove your name, phone number, address and license plate before sharing. Keep the year, make, model, engine, mileage and, if you're comfortable, the VIN. The audit needs those.

## What you get

A structured audit report:
- the bottom line
- a scorecard
- safety items to verify promptly
- a line-by-line review with the reasoning for each item
- photo and documentation findings
- a paperwork and compliance check for your state

It ends with either specific questions to ask the shop (consumer) or coaching notes and configuration fixes (shop owner).

## Install

**Claude.ai / Claude desktop:** download or zip the `skill/vehicle-inspection-audit/` folder. Then add it in Settings → Capabilities → Skills (upload a skill).

**Claude Code:** copy the folder into your skills directory:

```bash
cp -r skill/vehicle-inspection-audit ~/.claude/skills/
```

Then start a conversation by sharing your inspection, for example: "Can you check this inspection my shop sent? They say I need $1,800 of work."

## What's in this repo

```
skill/vehicle-inspection-audit/
  SKILL.md                    # the audit workflow Claude follows
  references/                 # condensed, cited reference material the skill looks up
    technical-criteria.md     # per-system tests, thresholds, red flags, upsell patterns
    image-evidence.md         # how to review inspection photos and video
    dvi-platforms.md          # how each inspection platform works and where it goes wrong
    industry-standards.md     # MAP Required/Suggested codes, certifications, shop QA programs
    consumer-protection.md    # enforcement history, red flags, dispute playbook, digital-approval law
    state-repair-laws.md      # 50-state + DC estimate/authorization/invoice rules
    california-bar.md         # California Bureau of Automotive Repair in depth
    state-inspection-programs.md  # state safety/emissions inspections and official fail criteria
    federal.md                # EPA, NHTSA, FTC and other federal rules
    commercial-fleet.md       # FMCSA, CVSA, rideshare, school bus, fleet
knowledge/                    # the full research notes behind the references, with sources
VERIFICATION.md               # what is confirmed vs. still open
```

## Limits — please read

- **It audits documents, not cars.** It can tell you a recommendation is poorly supported. It can't tell you a part is fine. When safety is involved, get the car checked in person.
- **It's not legal advice.** It explains what regulations generally require and where the paperwork falls short. For a dispute, contact your state's regulator or an attorney.
- **The research is current as of October 2026 and some items are unverified.** See [VERIFICATION.md](VERIFICATION.md). Laws, inspection programs and software change. Corrections are welcome.
- **Vehicle-specific specs come first.** Generic thresholds are fallbacks. Where the answer depends on your exact vehicle, the skill will say so and tell you where to find the spec.

## Contributing

Corrections and confirmations with primary-source citations are the most valuable contribution. Start with the open items in [VERIFICATION.md](VERIFICATION.md). Redacted sample inspections from different platforms, with no personal information, would also help with platform recognition and testing.
