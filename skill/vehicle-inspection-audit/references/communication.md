# Turning the Audit into Action

Finding problems is half the job. This file covers the other half: helping the user say the right thing to the right person so the findings change what happens next. Read it at step 9, every time you write the report.

## Contents
1. Action buckets (how statuses become decisions)
2. Consumer: talking to the shop
3. Shop owner: talking to the technician
4. Shop owner: talking to the service advisor
5. Shop owner: talking to the customer
6. Shop owner: fixing the system
7. Tone rules for every message

---

## 1. Action buckets

Status labels are for reasoning. People decide in buckets. Every line item lands in exactly one:

| Bucket | Meaning | Statuses that usually land here |
|---|---|---|
| **Fix now** | Safety. Don't drive until it's handled. | Verify in person – safety, when the finding itself is credible (e.g., brake leak + low pedal) |
| **Approve** | Evidence supports it. Fine to say yes. | Supported; Supported – optional when the customer wants it done now |
| **Ask first** | Might be real. Get an answer before paying. | Evidence missing, Inconsistent, Needs OEM spec, Verify in person (non-urgent) |
| **Skip or defer** | Optional, overlapping, not due, or not applicable. | Beyond OEM schedule, Not applicable to this vehicle, overlapping work, Supported – optional (low value now) |

Use judgment over the table. A "Needs OEM spec" coolant service with generic interval text is a reasonable *defer*. A "Needs OEM spec" brake hose is an *ask first*. The bucket answers "what should I do?", not "how good is the evidence?"

Every item gets a **Next step** that is one concrete action or question. "Ask why" is too vague. Write the actual question: "What was the LF pad measurement in mm, and what's the minimum for this truck?"

---

## 2. Consumer: talking to the shop

### Goals of the message
1. Get the safe, supported work moving right away. Don't hold the car hostage to a debate.
2. Get specific answers on the questionable items, in writing.
3. Protect the customer's rights without picking a fight.

### Structure (text or email)
1. **Thanks and context.** One line identifying the visit (vehicle, date, RO if known).
2. **What I approve.** Numbered, specific, with any condition (price cap, "diagnosis only").
3. **Ask for a written estimate** for the approved work before it starts. Most states require one above a threshold (see `state-repair-laws.md`). California requires one for all work (see `california-bar.md`).
4. **Questions before I approve anything else.** One bullet per item, each a direct, answerable question. Ask for the evidence that would settle it: the measurement, the code, the test result, the OEM interval, the photo.
5. **Rights requests, phrased as preferences.** Example: "I'd like the replaced parts returned." Where the state gives a right to old parts, it usually has to be requested at authorization.
6. **Friendly close.**

### Recent repairs and warranty
When a finding involves recent work, such as parts the report calls "recently replaced" or a leak at a fitting someone else just installed, the consumer's first move is usually with the shop that did that work, not the current one:
- **Consumer next step:** "Call [the shop that did the earlier work] and ask whether the parts and labor are under warranty. A leak at a fitting they installed is usually a workmanship claim."
- **In the message to the current shop,** don't ask them who did the earlier work or whether it's under warranty. They can't know. Ask them to **document** the failure so the claim can be made: which fitting or part, what they found (washer condition, thread damage, wrong part), photos, and a written note. Ask them to hold off replacing the earlier parts until the warranty question is settled, unless it's unsafe to wait.
- If the current shop *did* the earlier work, it's a comeback. Ask them directly how they'll handle it under their warranty.

### Fix the stated cause first
When the shop names a cause but recommends replacing other or bigger parts, write the message so it approves the **minimal repair of the stated cause** and makes the bigger parts conditional on a test afterward. For example: "Please fix the leak at the right-front fitting and bleed the brakes, then check whether the pedal holds before replacing the master cylinder."

### Responding to the shop's explanation
When the shop answers a question in a way that doesn't hold together, the reply should do three things:
1. Thank them.
2. Ask for the one specific thing that would verify the claim: part number and supplier, code, measurement, OEM interval.
3. Keep the questionable work on hold while the customer checks.

Don't argue the mechanics in the message. A request for specifics does the job and keeps things friendly.

> "Thanks for explaining. Could you tell me which part is discontinued, with the part number and supplier? I'd like to understand why the fitting can't be resealed with a new bolt and washers. In the meantime, please hold off on the calipers and master cylinder while I check with the shop that installed them."

### Phone version
Give 4–6 short talking points in the order the call should go: approve first, then ask, then defer. People forget questions on the phone, so keep it to a short checklist.

### What to avoid in consumer messages
- Words like "scam", "ripoff", "fraud", "lying", or "upsell". They end the conversation and may create defamation risk if repeated publicly (see `consumer-protection.md`).
- Quoting the audit as an authority ("an AI said..."). Ask the questions in the customer's own voice.
- Long messages. A shop will answer five clear questions. It won't answer a twenty-item essay.
- Declining safety items outright because documentation is weak. Say "please verify" instead.

### If the shop's answers don't satisfy
Point to the escalation path in `consumer-protection.md`:
1. Ask for a second opinion elsewhere.
2. Send a written request for records.
3. Contact the state regulator (BAR in California).
4. Pay under protest if needed to recover the car.
5. Dispute the card charge, or go to small claims.

Draft the next message only if the user asks.

---

## 3. Shop owner: talking to the technician

The technician note is private coaching, not a write-up. Its job is to make the next inspection better.

### Structure: what went right, then up to three changes, then a check-in
1. **Specific praise first, and real.** Name what the tech did well on *this* inspection: found the root cause, good photos, correct N/A use, addressed the customer's concern. A note that's only criticism teaches techs to stop documenting.
2. **No more than three changes**, each written as:
   - **What happened.** The observable fact: "pads are the only measurement on the inspection".
   - **Why it matters.** Customer trust, comebacks, regulatory exposure, or the advisor not being able to sell needed work.
   - **What to do next time.** Concrete: "tread per tire in 32nds; battery test printout attached; list scan codes".
3. **A follow-up.** "Let's look at your next one together." That turns feedback into calibration.

### Separate the person from the system
If a problem comes from a canned job, a template default or a pay plan, say so in the note: "the canned air-filter text defaults to red; I'm changing that". Then put the fix in the system section (6). Don't coach a tech out of a habit the software forces on them.

### Under-recommendation counts too
If the audit found missed work, such as an uninspected item graded green or a safety issue left at yellow, include it. Consistency in both directions is the goal.

---

## 4. Shop owner: talking to the service advisor

The advisor sits between the inspection and the customer, so the note covers presentation:
- Present Required items first, then Suggested items, labeled as optional, with the reason (OEM interval at this mileage, measured wear).
- Remove overlapping lines before the estimate goes out.
- Missing facts (mileage, codes, measurements) must be filled in before presenting, not after the customer asks.
- **Comebacks and warranty.** If a recommendation repairs our own recent work, it's a warranty conversation, not a sale.
- Authorization records: who approved, when, and how, for each line, under the state's rules.

---

## 5. Shop owner: talking to the customer

When the audit shows the customer received a confusing or over-scoped report, give the owner a short, plain message that resets things:
1. What's urgent, and why, in one or two sentences.
2. What we'll do next and what we need their OK for.
3. What can wait, framed as the customer's choice.
4. A promise of a written estimate before work.

No jargon, no blame on the technician, no defensiveness. The customer should come away trusting the shop more than before the audit.

---

## 6. Shop owner: fixing the system

Turn repeated findings into configuration and process changes for the shop's platform (see `dvi-platforms.md` §5.3):
- Require measurement fields, or prompt for numbers in canned findings, on platforms without structured fields.
- Remove default colors and replace generic interval text with OEM-based maintenance tied to the odometer.
- Make the odometer reading required before sending an inspection.
- Separate menu maintenance from condition findings on the customer report.
- Flag overlapping jobs on the same estimate.
- Review AI-rewritten customer text before it's sent.
- **Incentives.** If pay or bonuses reward sold hours alone, consider tying part of it to verified accuracy (see `industry-standards.md`).

Limit the list to the changes this audit actually supports, typically three to five.

---

## 7. Tone rules for every message

- Write like a calm, knowledgeable person. Use short sentences and plain words.
- Ask about the evidence, not the person's motives.
- Be specific: part, position, number, interval.
- Every message should be ready to send, with no placeholders the user has to fill in. Exception: details you don't have, like a name. Leave those out rather than writing "[name]".
- Don't include the customer's personal details unless the user put them in the draft themselves.
