# Verification Status

This skill is built on cited research (see `knowledge/`), compiled 2026-10-20. Most claims were checked against primary sources: statutes, regulations, agency pages and manufacturer documentation. Some could not be. The research hit a web-search budget limit, and several official sites block automated access. Items below are open until someone confirms them against a primary source. Inside the reference files they are marked `[UNVERIFIED]`.

Want to help? Pick an item, confirm it against an official source, and open a pull request that updates both the `knowledge/` file and the matching `skill/.../references/` file with the citation.

## Technical criteria
- [ ] **Brake fluid copper limit (200 ppm).** The only sources found are a test-strip vendor and a repair blog. Needs a MAP or OEM primary source.
- [ ] **Battery test cutoff.** Midtronics sources disagree on the healthy threshold: 70%, 80% or 90% of rated CCA.
- [ ] **Current MAP UICS text.** It's member-only. The rotor logic rests on a 1999 trade article.
- [ ] **Practitioner claims with no primary source found:**
  - flushing a neglected high-mileage transmission is risky
  - OEM bulletins tell dealers not to sell fuel-system cleaning services
  - regen braking reduces brake wear by some amount
  - the bounce test is unreliable
- [x] **Utah R714-160-10 (CV boots advisory).** Replaced with Virginia as the main example; Utah is kept only as a historical note.
- [ ] **Hunter's ±2.4 mm handheld-gauge variance figure.** It's a vendor claim.

## Image and evidence review
- [ ] **Scanner accuracy figures (Anyline, UVeye, ProovStation, Hunter) are vendor claims.** No independent accuracy studies were found.
- [ ] **Claude's accuracy reading gauges in real DVI photos is untested.** Needs a labeled test set.
- [ ] **Unknown whether DVI platforms strip or recompress image metadata,** or add watermarks.

## DVI platforms
- [ ] **Customer share-link domains are unconfirmed for every platform.** Real sample reports would settle it.
- [ ] **Bolt On:** template, measurement and approval details. Its documentation is customer-only.
- [ ] **Dealer DMS internals (CDK, Reynolds, Tekion)** and OEM numeric color thresholds.
- [ ] **Shop-Ware help-center details should be re-checked through normal browser access.** The research fetched them with a crawler user agent.
- [ ] **Whether AI-rewritten notes or mileage-based ratings are labeled on customer reports:**
  - AI-rewritten notes: AutoVitals Otto Notes, Shop-Ware AutoWrite
  - mileage-based ratings: Tekmetric Recommended Maintenance

## Federal
- [ ] **Right-to-repair bill status after June 2026:** H.R. 7389 and H.R. 8870.
- [ ] **EPA enforcement posture after July 2026,** the 2020 tampering-policy OBD exception, and whether the 1986 converter policy has been revised.
- [ ] **Any NHTSA interpretation on skipped ADAS calibration as "make inoperative."**
- [ ] **TCPA "revoke-all" provision.** Unclear whether it took effect in April 2026 or was delayed to January 2027. The one-to-one consent vacatur is confirmed (11th Cir., 2025-01-24).

## State repair laws
- [ ] **Tennessee § 66-19-104.** The official text was blocked, so the figures come from news sources.
- [ ] **Maine.** Unknown whether an AG motor-vehicle-repair rule exists.
- [ ] **States with UDAP-only coverage that weren't searched exhaustively:** AL, AR, DE, GA, IN, KY, LA, MS, MO, MT, ND, SD, WY, VT, WV, OK, TX.
- [ ] **Connecticut and Michigan estimate threshold wording at exactly $50.**
- [ ] **New Mexico's overage figure** appears on only one copy of the text.
- [ ] **Record-retention periods:** CT, MA, MI, NJ, DC.
- [ ] **Michigan:** what 2025 PA 59 changed, and the status of HB 5149.
- [ ] **Ohio:** what the 2026 amendment changed.
- [ ] **Local licensing:** Florida counties, Montgomery County MD, NYC and Westchester.

## California
- [ ] **Statute text was read from a mirror** because the official site blocked access. Re-check §§ 9884.7 and 9884.9 against leginfo.
- [ ] **Smog Check readiness-monitor rule (Oct 2025).** Only a BAR newsletter was found.
- [ ] **CARB used-converter ban and approval requirement.** The source page returned 404.
- [ ] **Garage-lien caps ($1,500 / $1,025).** It's unclear exactly when they apply.

## State inspection programs
- [ ] **Reject criteria for HI, RI, WV, DE, MO and ME passenger vehicles.**
- [ ] **Status after May 2026:**
  - New Hampshire litigation
  - Missouri HB 1838
  - West Virginia HB 4719 / 4882
  - North Carolina emissions removal
- [ ] **Whether Connecticut has a safety inspection,** and Delaware's frequency.
- [ ] **Fees and waivers:** NY, MA, NC and PA.

## Commercial and fleet
- [ ] **Uber/Lyft official inspection form items;** Colorado and Illinois statewide rideshare rules.
- [ ] **Full Appendix A steering-lash table,** and whether the definition is cited as § 390.5 or § 390.5T.
- [ ] **NYC for-hire vehicle inspection frequency.** Sources conflict.
- [ ] **California BIT subdivision (j) scope.** Sources conflict.
- [ ] **Texas commercial passenger threshold wording.**
- [ ] **NFPA 1910 intervals;** TMC tire practices.
