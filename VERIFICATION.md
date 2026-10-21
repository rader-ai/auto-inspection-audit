# Verification Status

This skill is built on cited research (see `knowledge/`), compiled 2026-10-20. Most claims were checked against primary sources: statutes, regulations, agency pages and manufacturer documentation. Some could not be. The research hit a web-search budget limit, and several official sites block automated access. Items below are open until someone confirms them against a primary source. Inside the reference files they are marked `[UNVERIFIED]`.

**Verification pass, 2026-10-21:** every item below was re-checked against primary sources. Ticked items are resolved, with the source in the note. Open items carry a note saying why they're still open. Some official sites (leginfo, Shop-Ware's help center, the Connecticut and Texas statute sites) were read in a normal browser after automated fetches were blocked. Nothing was spoofed or bypassed.

Want to help? Pick an item, confirm it against an official source, and open a pull request that updates both the `knowledge/` file and the matching `skill/.../references/` file with the citation.

## Technical criteria
- [ ] **Brake fluid copper limit (200 ppm).** The only sources found are a test-strip vendor and a repair blog. Needs a MAP or OEM primary source.
  - *2026-10-21: still open.* Only the vendor (Phoenix Systems) and 2005 trade press saying MAP adopted it are available. No MAP, UICS or OEM text found.
- [ ] **Battery test cutoff.** Midtronics sources disagree on the healthy threshold: 70%, 80% or 90% of rated CCA.
  - *2026-10-21: still open, files reworded.* No single cutoff exists. GM warranty relies on the tester's Replace code, not a percentage (https://gm-techlink.com/?p=16086). The files now say so.
- [ ] **Current MAP UICS text.** It's member-only. The rotor logic rests on a 1999 trade article.
  - *2026-10-21: still open.* motorist.org's public pages give no rotor guidance, and UICS is still member-only.
- [ ] **Practitioner claims with no primary source found:**
  - flushing a neglected high-mileage transmission is risky
  - OEM bulletins tell dealers not to sell fuel-system cleaning services
  - regen braking reduces brake wear by some amount
  - the bounce test is unreliable
  - *2026-10-21: partly resolved.* Fuel-system cleaning is now sourced to GM TechLink (https://gm-techlink.com/?p=16530) and regen braking wear to DOE AFDC (https://afdc.energy.gov/vehicles/electric-maintenance). Still unsourced: transmission flush risk (GM bulletin 04-06-01-029 is a lead only) and the bounce test (only a KYB interview found).
- [x] **Utah R714-160-10 (CV boots advisory).** Replaced with Virginia as the main example; Utah is kept only as a historical note.
- [ ] **Hunter's ±2.4 mm handheld-gauge variance figure.** It's a vendor claim.
  - *2026-10-21: still open.* The figure isn't in the cited release or on current hunter.com pages. It stays labeled as an unverified vendor claim.

## Image and evidence review
- [ ] **Scanner accuracy figures (Anyline, UVeye, ProovStation, Hunter) are vendor claims.** No independent accuracy studies were found.
  - *2026-10-21: still open.* No academic, insurer or agency study found, only vendor datasheets and patents.
- [ ] **Claude's accuracy reading gauges in real DVI photos is untested.** Needs a labeled test set.
  - *2026-10-21: still open.* Web research can't settle this. It needs an actual test.
- [ ] **Unknown whether DVI platforms strip or recompress image metadata,** or add watermarks.
  - *2026-10-21: still open.* No Tekmetric, Shopmonkey or AutoVitals help article mentions EXIF, compression or watermarks.

## DVI platforms
- [ ] **Customer share-link domains are unconfirmed for every platform.** Real sample reports would settle it.
  - *2026-10-21: still open.* Not published in public docs. Needs redacted sample reports.
- [ ] **Bolt On:** template, measurement and approval details. Its documentation is customer-only.
  - *2026-10-21: still open.* The help desk is still customer-only.
- [ ] **Dealer DMS internals (CDK, Reynolds, Tekion)** and OEM numeric color thresholds.
  - *2026-10-21: still open.* Dealer-only documentation.
- [x] **Shop-Ware help-center details should be re-checked through normal browser access.** The research fetched them with a crawler user agent.
  - *2026-10-21: confirmed in a normal browser.* Two corrections: AutoWrite was released in v13.1.0 (Mar 2026), and MMS texting in v13.4.0 is only "coming soon" (https://support.shop-ware.com/s/product-updates).
- [ ] **Whether AI-rewritten notes or mileage-based ratings are labeled on customer reports:**
  - AI-rewritten notes: AutoVitals Otto Notes, Shop-Ware AutoWrite
  - mileage-based ratings: Tekmetric Recommended Maintenance
  - *2026-10-21: still open.* None of the three vendor docs mentions a customer-facing label, and Otto Notes overwrites the note in place. Needs a real customer report.

## Federal
- [x] **Right-to-repair bill status after June 2026:** H.R. 7389 and H.R. 8870.
  - *2026-10-21: confirmed.* Numbers and titles are correct, and neither bill has had floor action (govinfo BILLSTATUS: https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr7389.xml).
- [x] **EPA enforcement posture after July 2026,** the 2020 tampering-policy OBD exception, and whether the 1986 converter policy has been revised.
  - *2026-10-21: confirmed.* EPA still lists the 2020 Tampering Policy, including the OBD carve-out, and the 1986 and 2004 converter policies unchanged. No formal deprioritization for individuals (https://www.epa.gov/enforcement/air-enforcement-policy-guidance-and-publications).
- [ ] **Any NHTSA interpretation on skipped ADAS calibration as "make inoperative."**
  - *2026-10-21: still open.* No ADAS-specific interpretation found on nhtsa.gov, only general repair-shop letters.
- [x] **TCPA "revoke-all" provision.** Unclear whether it took effect in April 2026 or was delayed to January 2027. The one-to-one consent vacatur is confirmed (11th Cir., 2025-01-24).
  - *2026-10-21: resolved.* It never took effect. DA 26-12 waived it to 2027-01-31. FCC 26-67 (Oct 2026) partly rolls it back, effective 30 days after Federal Register publication, which is still pending (https://docs.fcc.gov/public/attachments/FCC-26-67A1.pdf).

## State repair laws
- [x] **Tennessee § 66-19-104.** The official text was blocked, so the figures come from news sources.
  - *2026-10-21: confirmed.* The 2001 bill amendment and TN AG Op. 09-187 confirm the $250 written-estimate right, the 25% cap and the good-faith call (https://www.capitol.tn.gov/Bills/102/Amend/SA0240.pdf). The current codified text wasn't read.
- [x] **Maine.** Unknown whether an AG motor-vehicle-repair rule exists.
  - *2026-10-21: resolved.* Maine has a repair statute, 29-A M.R.S. §§1801–1811, enforced through the UTPA (https://legislature.maine.gov/statutes/29-A/title29-Ach15sec0.html). No separate AG rule was looked for.
- [ ] **States with UDAP-only coverage that weren't searched exhaustively:** AL, AR, DE, GA, IN, KY, LA, MS, MO, MT, ND, SD, WY, VT, WV, OK, TX.
  - *2026-10-21: still open.* Only a light pass was done. It found that Louisiana has a dealer-only LMVC estimate rule (LAC 46:V.1103), so LA is no longer UDAP-only. The other states were not searched.
- [x] **Connecticut and Michigan estimate threshold wording at exactly $50.**
  - *2026-10-21: confirmed.* Both exempt only jobs under $50, so an estimate is required at exactly $50 (CGS 14-65f(f); https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-257-1334a).
- [x] **New Mexico's overage figure** appears on only one copy of the text.
  - *2026-10-21: confirmed.* The official SRCA copy of 12.2.6.10.A says the greater of 10% or $50, though the drafting is loose (https://srca.nm.gov/parts/title12/12.002.0006.html).
- [ ] **Record-retention periods:** CT, MA, MI, NJ, DC.
  - *2026-10-21: partly resolved.* MI is 3 years (MCL 257.1318). The NJ 26C rules and the CT statute set no period. CT DMV regulations, MA and DC are still not found.
- [x] **Michigan:** what 2025 PA 59 changed, and the status of HB 5149.
  - *2026-10-21: resolved.* PA 59 (effective 2026-02-01) changed facility, licensing, fee and record rules but left the estimate rules alone. HB 5149 is still in committee (https://legislature.mi.gov/documents/2025-2026/publicact/htm/2025-PA-0059.htm).
- [x] **Ohio:** what the 2026 amendment changed.
  - *2026-10-21: resolved.* The change was gender-neutral wording only. The $50 threshold dates from 2015, and the AG guide's $25 is outdated (https://codes.ohio.gov/assets/laws/administrative-code/authenticated/109/4/3/109$4-3-13_20150810.pdf).
- [ ] **Local licensing:** Florida counties, Montgomery County MD, NYC and Westchester.
  - *2026-10-21: partly resolved.* Miami-Dade and Broward license shops. Montgomery County requires registration. NYC has no license (DCWP list). Hillsborough and Westchester are unconfirmed.

## California
- [x] **Statute text was read from a mirror** because the official site blocked access. Re-check §§ 9884.7 and 9884.9 against leginfo.
  - *2026-10-21: confirmed on leginfo in a normal browser.* Neither section has a 2024–2026 amendment (§9884.9 last changed eff. 2019, §9884.7 eff. 2022), and every stated detail matches.
- [x] **Smog Check readiness-monitor rule (Oct 2025).** Only a BAR newsletter was found.
  - *2026-10-21: resolved.* BAR's Order of Adoption amends §3340.42.2(a)(9): gas MY1996+ and diesel MY1998+ fail with any incomplete monitor (https://www.bar.ca.gov/pdf/regulatory-actions/readiness-monitor-limits-2024/approved-text.pdf).
- [x] **CARB used-converter ban and approval requirement.** The source page returned 404.
  - *2026-10-21: confirmed.* 13 CCR §2222(h) requires a CARB EO for new aftermarket converters, and §2222(i)(1) has banned used and recycled converters since 2008 (https://www.law.cornell.edu/regulations/california/13-CCR-2222).
- [x] **Garage-lien caps ($1,500 / $1,025).** It's unclear exactly when they apply.
  - *2026-10-21: resolved on leginfo.* Civ. §3068(c)(1) applies the caps only when someone other than the legal owner or lessor ordered the work. Storage is capped at $1,250 if a lien-sale application is filed within 30 days. Files corrected.

## State inspection programs
- [ ] **Reject criteria for HI, RI, WV, DE, MO and ME passenger vehicles.**
  - *2026-10-21: mostly resolved.* HI (HAR 19-133.2), RI (280-RICR-30-15-3), MO (11 CSR 50-2; no 2/32 tire rule), DE and ME tread (29-A §1917) are now cited. Still open: the WV manual (wvsp.gov certificate error) and the ME brake-pad minimum.
- [x] **Status after May 2026:**
  - New Hampshire litigation
  - Missouri HB 1838
  - West Virginia HB 4719 / 4882
  - North Carolina emissions removal
  - *2026-10-21: resolved.*
    - Missouri HB 1838 was not enacted. SB 1408 as signed only changes speed limits.
    - West Virginia's bills died in committee.
    - New Hampshire: court stay entered 2026-04-30; EPA proposed conditional approval 2026-08-11, not final.
    - North Carolina: only EPA's 2026-05-08 proposal exists so far.
    - Sources: Federal Register 2026-16330 and 2026-09146 (https://www.federalregister.gov).
- [x] **Whether Connecticut has a safety inspection,** and Delaware's frequency.
  - *2026-10-21: resolved.*
    - Connecticut has no periodic passenger safety inspection. Under CGS §14-16a, checked on cga.ct.gov, DMV may require one at transfer for vehicles 10+ model years old.
    - Delaware inspects before each 1–2-year registration renewal (21 Del.C. §2143).
- [ ] **Fees and waivers:** NY, MA, NC and PA.
  - *2026-10-21: partly resolved.*
    - Confirmed: NY (form VS-77), NC (G.S. 20-183.7), MA $35 fee, and the PA waiver of $450 from 2023-09-01.
    - Still open: PA's 2026 waiver amount, MA's current waiver caps, and PA's safety fee.

## Commercial and fleet
- [ ] **Uber/Lyft official inspection form items;** Colorado and Illinois statewide rideshare rules.
  - *2026-10-21: still open.* No public Uber or Lyft form exists. Colorado's PUC site returned 403, and ilga.gov failed its certificate check.
- [x] **Full Appendix A steering-lash table,** and whether the definition is cited as § 390.5 or § 390.5T.
  - *2026-10-21: resolved on eCFR.* The table has only 16, 18, 20 and 22 in. rows. §390.5 is suspended, so cite §390.5T (https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-390/subpart-A/section-390.5T).
- [x] **NYC for-hire vehicle inspection frequency.** Sources conflict.
  - *2026-10-21: resolved.* 35 RCNY 59A-26(a) sets three inspections a year, at least every 4 months (https://www.nyc.gov/assets/tlc/downloads/pdf/rule_book_current_chapter_59.pdf).
- [x] **California BIT subdivision (j) scope.** Sources conflict.
  - *2026-10-21: resolved.*
    - Subdivision (j) covers other regulated motortrucks, not hazmat (hazmat is (g)).
    - CHP's Feb 2025 bulletin removed (j) trucks from BIT and the 90-day rule (https://www.chp.ca.gov/siteassets/policy/ib/ib-removal-of-motortrucks-identified-in-sec.-34500j-of-the-cvc.pdf).
- [x] **Texas commercial passenger threshold wording.**
  - *2026-10-21: confirmed.* The statute says "more than 15 passengers, including the driver" (Tex. Transp. Code 548.001(1)(B), https://statutes.capitol.texas.gov/Docs/TN/htm/TN.548.htm).
- [ ] **NFPA 1910 intervals;** TMC tire practices.
  - *2026-10-21: still open.* Both are paid or member-only standards with no public primary text.
