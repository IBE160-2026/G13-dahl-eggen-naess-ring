# Validation Report — LifeMode PRD

- **PRD:** `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md` (with `addendum.md`, and Rule Set v1 in `briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md` where cited)
- **Rubric:** `.claude/skills/bmad-prd/assets/prd-validation-checklist.md`
- **Run at:** 2026-11-13T12:36
- **Grade:** Fair. Every dimension is strong or adequate, and there are no critical findings, but there are high findings.

## Overall verdict

This is a strong, unusually testable PRD. One protagonist carries six journeys, nearly every FR has numbered consequences tied to the worked-example answer key, and the glossary and IDs are clean enough for UX and architecture to extract from directly. The risk is in delivering it, not in defining it. The tier-and-date scheme added on 2026-11-13 (§4.4) contradicts itself, and as written it leaves the Extension tier unbuilt in the expected case. Meanwhile 46 of 57 FRs stay Core, and nothing says what happens if the core isn't playable before the 8 Dec playtest. A few stale figures, and architecture notes in the addendum that are only half superseded, should be cleaned up before the architecture run extracts them.

The three extra reviewers sharpen that picture rather than overturn it.

**Engine arithmetic is sound.** The independent figure check reproduced all 28 worked examples in Rule Set v1 with no mismatches, about 210 values in all. That includes examples 19–23, which so far only Claude's script had checked. It also found two real defects. FR-29 and the UJ-4 trace still use the old moped price. And a consumer loan in month 56 lets careless runs reach goal 3, despite "Borrowing never helps".

**Bård's feedback is largely handled.** The feedback-coverage review found 21 of 36 points applied and verified, 7 partly applied, and only one not addressed: OQ-11 hasn't been taken to the lecturer. Every change the memlog claims is present in the documents.

**The adversarial review is the harshest.** It finds that §3.1 states rules 5 and 8 as "or" where they mean "the larger of". Built as written, that puts UJ-4's Markus into crisis at once. It also finds that:
- the ending summary can't show the spending level and working hours, which are the two levers that decide the ending
- UJ-4 works only because it leaves out fuel that Markus's own story says he pays
- the card minimum of NOK 5,508 depends on a rounding rule that is never written down

**Where reviewers agree.** Several reviewers reached the same conclusions independently:
- the §4.4 cut rules contradict each other (3 of 4 reviewers)
- FR-29 and the UJ-4 trace have stale moped values (3)
- moped fuel has a figure that the examples say doesn't exist (all 4)
- the §0 status block is stale (3)
- Core FRs point at Extension or Can-be-cut features with no fallback (3)

## Dimension verdicts

- Decision-readiness — adequate
- Substance over theater — strong
- Strategic coherence — strong
- Done-ness clarity — strong
- Scope honesty — adequate
- Downstream usability — strong
- Shape fit — strong

## Findings by severity

### Critical (0)

None.

### High (5)

**[Decision-readiness]** — The §4.4 cut rules contradict each other, and on plan the Extension tier is never built (§4.4 "When to cut", checkpoint table, "Tiers")
The "When to cut" paragraph applies the first six cut items at the first checkpoint. The table drops only unstarted Extension FRs there, and drops the whole Can-be-cut tier at the second checkpoint. Extensions freeze about 26–27 Nov, but they're built only "once the core is playable", which is about 1–3 Dec. So all eight Extension FRs drop in the planned case. Also flagged by the adversarial review (AG-01, AG-04) and the feedback-coverage review (F1).
Fix: Keep one rule set, written as a decision table: checkpoint → the condition tested → the exact consequence. Either move the Extension freeze after core-playable, or say plainly that Extension is expected to drop. Delete or adopt the "first six items" example, and say whether the 1–11 order still matters.

**[Scope honesty]** — Core is nearly the whole product, and there's no playtest fallback (§4.4 "Tiers"; FR overview; §7.1 "Dates")
Core holds 46 of 57 FRs. If core-playable on 1–3 Dec is missed, the only response is dropping three FRs, 5–7 days before the 8 Dec playtest. Nothing says what the playtest does then, and SM-5 and SM-11 need full playthroughs. Also flagged by the adversarial review (AG-02).
Fix: Add a "playable spine" checkpoint about a week earlier. Write down a playtest fallback, for example testers playing from NFR-6-style seeded states, with SM-5 and SM-11 reported as not measured. Mark which Core FRs could ship in a reduced form.

**[Figure check H1]** — FR-29 quotes the old used-moped resale value (FR-29 "Resale value")
"Fetches NOK 9,625 (worked example 19)" is 13,750 × 0.70. Example 19 now gives 11,645 × 0.70 = NOK 8,152. An acceptance test written from FR-29 would assert the wrong value. Also flagged by the rubric walker (Done-ness clarity, medium) and the feedback-coverage review (F6).
Fix: Replace NOK 9,625 with NOK 8,152.

**[Figure check H2]** — A consumer loan lets careless runs reach goal 3, despite "Borrowing never helps" (rule 13; FR-9a; FR-9b; NFR-7; example 21 note)
Rule 13 requires only payment "from the current and savings accounts" and available money of NOK 0 or more at 20. Two full-time months raise the loan cap to NOK 71,000. Runs 21a–a5 and 21d can then borrow in month 56, buy the NOK 60,000 experience, and end at NOK 8,175–25,588: a real win. The rule 8 debt trigger doesn't fire.
Fix: Decide what "on credit" means in rule 13. Options: refuse the experience while a loan is outstanding; require available money net of debt to be at least the price; or count loans taken in months 44–56 as credit. Then add a goal-3 row to example 18, and qualify the FR-9b and example 21 claims.

**[Feedback coverage F1]** — The §4.4 cut rules contradict each other (feedback 4.1-e/f/g)
This is the same defect as the first high finding, seen against Bård's request for a date that triggers the cut "without new discussion". "About 1–3 Dec" is a range, so someone still has to decide which day counts.
Fix: Point "When to cut" at the table. State the Extension-versus-Core order outright. Give each checkpoint a single date and name who confirms it.

### Medium (22)

**[Decision-readiness]** — The status block reads as a changelog and is partly stale (§0 "Status", frontmatter)
"Final for UX and architecture" sits next to `status: draft`, and "tiers, dates and hosting wait for the team" is out of date. Also flagged by the feedback-coverage review (F2) and the adversarial review (AG-27).
Fix: Write three lines: the current status, what is still open downstream (OQ-4, OQ-13, OQ-14), and a pointer to `.memlog.md`. Align the frontmatter.

**[Decision-readiness]** — Whether players see an option's wellbeing effect before choosing is a game-design decision filed as UX (OQ-9; FR-13; FR-33; FR-53)
FR-13 says every option "states its wellbeing effect", yet OQ-9 calls this open, owned by UX, and "Blocks: Nothing". This decides between quiz-like and discovery-based play. Also flagged by the adversarial review (AG-15).
Fix: The team decides this before the event screen is designed, and FR-13 records it. Mark OQ-9 as blocking the event UI.

**[Strategic coherence]** — Cut items 1 and 8 remove the motivation behind UJ-6 and UJ-4 (§4.4; UJ-6; UJ-4)
UJ-6's pinned target and bank message depend on FR-57, the first cut item. UJ-4's setup depends on FR-30, cut item 8. Also flagged by the feedback-coverage review (F5).
Fix: Add an "if cut" line to each affected journey, or take the savings-target pin out of item 1.

**[Strategic coherence]** — SM-6 can't separate a voluntary return from finishing the assigned playthrough (§7.1 SM-5, SM-6)
A full game takes about an hour, so most testers come back anyway. Also flagged by the adversarial review (AG-21).
Fix: State what testers are told. Count as a return only a sitting after the instructed part, or a replay after an ending.

**[Strategic coherence]** — The "careful player with some free time" check hasn't been run, and its margin is thin (FR-9b; example 20; OQ-17)
The figure check ran it: one NOK 100 café visit a month gives NOK 100,488 with expenses, only NOK 488 above goal 1. Any extra monthly cost, such as fuel, tips it.
Fix: Record the run as a worked example. Replace "expected to need tuning" with the result and any tuning decision under OQ-8, before 26–27 Nov.

**[Done-ness clarity]** — FR-29's resale test contradicts worked example 19 (FR-29)
This is the same defect as figure check H1.
Fix: NOK 8,152. Search for other values derived from NOK 13,750.

**[Scope honesty]** — Extension FRs have no fallback text, so Core FRs refer to features that may not exist (FR-25, FR-16, FR-19, FR-40, FR-37)
For example, the FR-18 consumer-loan row, the FR-55 month-49 offer and the NFR-7 loan refusals all assume FR-25 exists. A-23 calls the disclosures (FR-40) a requirement. Also flagged by the adversarial review (AG-03) and the feedback-coverage review (F5).
Fix: Add an "If left out:" line to every Extension FR. Reconsider FR-40, and the card-offer tip in FR-19, for Core.

**[Scope honesty]** — The content check is major build work with no FR, tier or owner (glossary; FR-9b, FR-17, FR-33, FR-43, FR-46b, FR-48, FR-52, FR-55; NFR-9)
It is a seeded playthrough simulator plus schema validation plus about a dozen gates, all run in CI. Also flagged by the adversarial review (AG-18).
Fix: Give it its own FR (for example FR-58) with its gates listed, a tier and an owner.

**[Downstream usability]** — The architecture handoff in the addendum is only half superseded (addendum "For the architecture", "Reset email routes")
A "Superseded" banner sits over bullets that still discuss Supabase login limits and zero cost. Also flagged by the adversarial review (AG-27).
Fix: Rewrite the bullets for the reference setup: own Python login, Railway with Supabase Postgres, NFR-6 stand-ins, NFR-5 low cost. Delete the superseded text.

**[Figure check M1]** — The UJ-4 trace still uses the old moped sale value (addendum "UJ-4 month by month", two places)
"About NOK 9,300" should be about NOK 7,860. The story still holds, since that's less than the NOK 9,314 he owes. Also flagged by the rubric walker (mechanical notes) and the feedback-coverage review (F6).
Fix: "About NOK 7,900", and soften "the sale alone would nearly clear the debt".

**[Figure check M2]** — Moped fuel has a figure, but the rules and examples say it has none (parameter table; rule 14; D9; examples 22, 23, 25; UJ-4 trace; OQ-3)
If NOK 186 a month in April–October is charged, 22a flips from reached to missed, and UJ-4 payoff takes one month longer. Also flagged by the adversarial review (AG-09), the feedback-coverage review (F7) and the rubric walker (mechanical notes).
Fix: Either (a) set fuel to NOK 0 in V1 and say so in the parameter row and rule 14, or (b) charge it, add the season to rule 14 and D9, and recompute examples 22, 23 and 25, the UJ-4 trace and 17a.

**[Figure check M3]** — Rounding 0.5 up needs exact arithmetic, and floats get example 19 wrong (rule 2; rule 14; NFR-4)
In double precision, 11645 × 0.70 = 8151.4999…, which gives 8,151, not 8,152.
Fix: Require exact decimal or integer arithmetic for money and rates (for example `Decimal`, or øre with rates in basis points). Keep example 19 as a regression test.

**[Figure check M4]** — Example 22's purchase wording contradicts its own months (Rule Set example 22)
Read literally, "first choice step the player can pay" gives a licence in month 19 and a moped in month 25, and 22a misses goal 1.
Fix: "The licence from month 20 and a moped from month 32, each at the first choice step from then on at which the player can pay."

**[Figure check M5]** — Rounding and tax-base rules that the published figures need aren't written down (rule 3; rule 10; FR-47)
These are: separate rounding of part-time and summer pay, the year's tax rounded once, and trinnskatt on the gross wage. Without them, results are off by 1–3 kr or by NOK 251 in year-5 tax.
Fix: Write all three into rules 3 and 10.

**[Feedback coverage F2]** — The status line is stale and contradicts itself (frontmatter; §0; Rule Set and memlog frontmatter)
This is the same defect as the rubric's status-block finding. The `updated` dates also weren't changed for the 2026-11-13 edits.
Fix: One current status sentence plus a short trailing history. Update the dates.

**[Feedback coverage F3]** — Hosting is still an open question in the PRD (OQ-14, OQ-4, NFR-6, FR-3; #47)
The reference setup was decided on 2026-11-12, but OQ-14 still reads as undecided. EU/EEA storage and the 10 s wake-up are unverified.
Fix: Reword OQ-14 as decided, with only the EU region and wake-up time left open, and cite #68. Narrow OQ-4. Retitle or close #47. Make NFR-6's "If that fails" precise.

**[Feedback coverage F4]** — Building login in-house raised its cost, and the tier marks are incomplete (§4.4 item 11; FR-1, FR-3, FR-5; NFR-3)
The item-11 parts aren't marked on FR-1, FR-3 or FR-5. The team's own bcrypt and JWT login now has to provide rate limits, reset tokens and session revocation. Also flagged by the adversarial review (AG-05) and the rubric walker (mechanical notes).
Fix: Mark the cut parts in the overview. Log why login stays Core. Consider a reset link the team issues by hand as the Core minimum for FR-3 in the playtest.

**[Feedback coverage F5]** — The tiers conflict with the journeys, A-23 and the metrics (UJ-2, UJ-4, UJ-6; FR-16, FR-30, FR-40, FR-51, FR-57; SM-2, SM-6, SM-9)
This overlaps the rubric's findings on cut items versus journeys and on missing Extension fallbacks.
Fix: Move FR-40 (and possibly FR-16) to Core, or amend A-23. Add an "if cut" line per journey. Make sure each SM row validates at least one Core FR.

**[Feedback coverage F6]** — FR-29 and the UJ-4 trace still use the old used-moped price
This is the same defect as figure check H1 and M1.
Fix: As in H1 and M1.

**[Feedback coverage F7]** — Fuel has a figure, but the rules and examples say it has none
This is the same defect as figure check M2. OQ-8 also calls car fuel a tuning value, while the table calls it an Assumption.
Fix: As in M2, and align OQ-8.

**[Feedback coverage F8]** — The new figures haven't been checked independently by a person (memlog 162, 168; reflection; #67)
The reflection names a team member's spreadsheet recheck as the control. This review's figure check reproduced every example, but it is another AI check, not the team's.
Fix: A team member rechecks examples 19, 20 and 22 in a spreadsheet and logs it before the PRD is set final.

**[Feedback coverage F9]** — OQ-6 is closed without naming who holds the playtest data (NFR-3; §4.3; addendum line 414)
Also flagged by the rubric walker (low, "needs no approval" has no basis).
Fix: One sentence in NFR-3 on who holds the data and what basis the testers are told. Record who confirmed that no approval is needed. Mark addendum line 414 as superseded.

### Low (20)

**[Decision-readiness]** — OQ-11 has no deadline and "Blocks: Nothing" (§8 OQ-11)
Also flagged by the feedback-coverage review (F10) and the adversarial review (AG-16).
Fix: Set a date to ask the lecturer, before sprint planning. Name the smallest AI scope to fall back on if AI is required.

**[Substance over theater]** — The comparison with Koll på cashen has no measure (§1; §7.1)
Fix: Add a survey item for testers who know it, or recast the sentence as a design aim.

**[Strategic coherence]** — SM-2's "Higher after" has no bound (§7.1 SM-2)
Also flagged by the adversarial review (AG-21).
Fix: Set a minimum mean rise, or a share of testers who improve. Report the distribution.

**[Done-ness clarity]** — The 2-minute target has two start points (FR-11; FR-1; SM-10; FR-50)
Also flagged by the adversarial review (AG-21).
Fix: Pick one start point: either the load of the create-user screen, or user creation.

**[Done-ness clarity]** — Three phrases a story writer will have to ask about (FR-9c; FR-40; §4.4 item 3)
Fix: Write "lowest available money at a month-end from month 49"; "shown once without being asked for, then kept behind the info icon"; and either set an info-message minimum or say there is none.

**[Done-ness clarity]** — Some NFR wording is adjectives, not bounds (NFR-1; NFR-10)
Fix: For example, body text of at least 16 CSS px, usable at 200% zoom, and a named DevTools throttle profile on a named reference phone.

**[Scope honesty]** — "Needs no approval" has no basis (NFR-3; §4.3)
Fix: Say who confirmed it and when, or make it a team-owned OQ that blocks the playtest.

**[Downstream usability]** — §3.1 misstates the rule 8 debt trigger (§3.1 row 8)
Also flagged by the adversarial review (AG-07, together with rule 5).
Fix: "Net debt above the larger of 3× the 3-month average wage and NOK 5,000."

**[Figure check L1]** — Several example setups are only implied (examples 17b, 23)
Fix: Add "as in example 20: pengegave saved in month 1, surplus moved to savings each month", and for 23, "10 h a week in months 37–40".

**[Figure check L2]** — Rule 12's "If none of these apply" is ambiguous
Fix: "If none of the stress rises above apply…"

**[Figure check L3]** — The consumer-loan source cites a range the research doesn't give, and D5 disagrees with the parameter row
Fix: Quote the effective rates the research gives, and align D5 with the parameter row.

**[Figure check L4]** — "Six estimated prices" is actually nine [ASSUMPTION] prices, and the NOK 450 concert in examples 25–28 matches no catalogue price
Fix: Write "nine", list them in OQ-17, and either declare NOK 450 a test placeholder or align examples 25–28 with the catalogue.

**[Figure check L5]** — Some status labels claim more than the research supports (experience, used moped, moped insurance)
Fix: Mark the experience Partly sourced, write "probably including the transfer fee" for the moped, and cite the insurance figures as published.

**[Figure check L6]** — FR-32 leaves out netting against the current account
Fix: "After subtracting savings and a positive current account."

**[Figure check L7]** — Provenance and `updated` dates are out of date (Rule Set v1; prd.md)
Fix: Add one sentence on the 2026-11-13 recalculation and this independent check, and update the dates.

**[Feedback coverage F10]** — OQ-11 hasn't been taken to the lecturer (#39)
Fix: Ask before the architecture run and record the answer, or log a decision not to ask.

**[Feedback coverage F11]** — D1–D26 and F1–F10 are still cited only by number (glossary; §7.3)
Fix: Add a 10-row F-criteria table to §7.3.

**[Feedback coverage F12]** — Parameter table: the owner is always "Team", and "Feature freeze" isn't a PRD term
Fix: Name a person per row or per group of rows, use the §4.4 checkpoint names, and add "revisit after playtest" to the Tuning rows.

**[Feedback coverage F13]** — Tracking hygiene (#46, #47, #72, #73; OQ-13, OQ-14 rows; quota placeholder)
Fix: Close #73 as a duplicate and #46 as superseded, retitle #47, cite #72 and #68 in the OQ rows, and repoint the quota placeholder to OQ-4 and #30.

**[Feedback coverage F14]** — The 3-day return window doesn't fit a 3-day test period (NFR-11; §7.1; §4.4)
Fix: Have every tester start on day 1, or lengthen the test period to about 5 days.

### Unranked — adversarial lens (28)

This lens deliberately assigns no severity.

**[Adversarial AG-01]** — The Extension tier can never start under the PRD's own sequencing (§4.4 Tiers, dates table)
Fix: Decide FR by FR: promote to Core, or move to Can be cut with a fallback. Or move the freeze after Core.

**[Adversarial AG-02]** — Core isn't a minimal version, and the schedule isn't achievable for a student team (§4.4; NFR-1 to NFR-11; FR-17; content check)
About 18–20 days to core-playable, with UX, architecture and epics not yet written, and no checkpoint for content authoring.
Fix: Define a "Core-0" walking skeleton for about 24 Nov. Tier the NFRs. Schedule content authoring and the content-check harness with owners.

**[Adversarial AG-03]** — Core FRs depend on non-Core FRs with no "if not built" behaviour (FR-28→FR-16, FR-42→FR-19, FR-18/48/45/55/NFR-7→FR-25, FR-12/49/55→FR-57, FR-53→FR-37)
Fix: Add an "If not built" block to every Extension and Can-be-cut FR.

**[Adversarial AG-04]** — The cut rule contradicts the checkpoint table, and nothing covers a Core miss (§4.4)
Fix: Use one table. Add "No Can-be-cut work starts before Core is playable", plus a rule for when Core is missed.

**[Adversarial AG-05]** — The cut order protects login hardening ahead of the game itself (§4.4 item 11)
Fix: Move item 11 to position 1 or 2, or to a before-go-live list.

**[Adversarial AG-06]** — NFR-3 promises a 12-month deletion that the cut list removes (NFR-3; item 11; FR-5)
Fix: Make NFR-3's text conditional on the job, or keep the job. Do the same for FR-5's "Log out on all devices".

**[Adversarial AG-07]** — The §3.1 summaries misstate rules 5 and 8 as "or", where they mean "the larger of" (§3.1 rows 5, 8)
Built as written, the NOK 10,000 card in UJ-4 puts Markus into crisis immediately.
Fix: Rewrite both rows with "the larger of" and the full netting.

**[Adversarial AG-08]** — The card minimum has no rounding rule, and the answer key depends on one (rule 5; UJ-4; FR-26; FR-31; example 12)
Half-up gives 5,508, floor gives 5,512 and ceiling gives 5,503.
Fix: Add to rule 5: "The minimum is rounded under rule 2." Add a fractional-minimum example.

**[Adversarial AG-09]** — UJ-4 works only by leaving out fuel its own story says Markus pays (UJ-4; addendum trace; examples 17a, 23)
With moped fuel, payoff takes W+6 and NOK 771 of interest. Adding car fuel too gives a missed minimum and a payoff of about 15 months.
Fix: Recompute with every cost the story names, or rewrite the story.

**[Adversarial AG-10]** — The extra hours in UJ-4 use three different mechanisms, and the card warning has no specified options (UJ-4; trace; 17a; FR-47; FR-55; FR-31)
Fix: Pick one mechanism, recompute 17a, and specify the card warning's source, options and effects in FR-31.

**[Adversarial AG-11]** — No FR guarantees "The game always shows why" (FR-38; FR-13; FR-14; FR-54)
Fix: Add a coverage table to FR-38 listing every effect type that carries "Hvorfor?", and test it.

**[Adversarial AG-12]** — The ending summary can't show the levers that decide the ending (FR-36; FR-42; glossary; UJ-5; examples 17b, 21)
Spending level and hours are system causes and aren't ranked. The glossary contradicts FR-36.
Fix: Make level and hour changes choices with linked effects, or add a "Your settings" block to the ending. Fix the glossary.

**[Adversarial AG-13]** — FR-39 has no comparison for open options, and the goal-3 purchase gets an "avoid this cost" tip (FR-39; FR-42; FR-48; message schema)
Fix: Define FR-39's comparison for open options as "not taking it". Give goal purchases their own text. Add an ending-text field to the schema.

**[Adversarial AG-14]** — FR-47 and FR-55 contradict each other on the summer-job offer
Fix: Add an exception to FR-55, or reword FR-47.

**[Adversarial AG-15]** — FR-13 states a requirement that OQ-9 calls undecided, and OQ-9 claims to block nothing
Fix: Decide now, and mark OQ-9 as blocking the event UI.

**[Adversarial AG-16]** — Open questions that can sink the delivery are marked "Blocks: Nothing" (OQ-11; OQ-12; A-26)
Fix: Give OQ-11 a deadline and a pre-scoped contingency. Make OQ-12 block FR-1's acceptance.

**[Adversarial AG-17]** — FR-9b's reference run isn't the run in example 20, and FR-33 mislabels 21c as careless
Fix: Write "exactly the run in worked example 20" and correct the 21c label.

**[Adversarial AG-18]** — The content check is an unnamed Core deliverable, and the PRD expects it to fail CI (FR-9b; NFR-9; addendum)
Fix: Make it an epic. In CI, separate hard gates from balance reports, and let balance checks only warn until a tuning freeze.

**[Adversarial AG-19]** — The worked examples are the answer key, but their tuning values are finalized on playtest day (NFR-4; parameter table)
Fix: Freeze a separate test configuration. Name who triages engine-versus-key disagreements, and require a second independent computation before the key changes.

**[Adversarial AG-20]** — The pace target conflicts with four game areas visited every month (FR-46a; SM-11; CM-4; CM-5)
Fix: Set a time budget per month, and agree in advance what to do if CM-4 or CM-5 fires.

**[Adversarial AG-21]** — Several metrics can't fail, or can't be measured as defined (SM-2, SM-6, SM-10, SM-12)
Fix: Set a minimum gain for SM-2, redefine SM-6 as a later calendar day, measure SM-10 from first screen load, and define or remove SM-12.

**[Adversarial AG-22]** — The playtest validates nothing about the primary persona (testers 18–20; persona 15–17)
Fix: Mark SM rows as valid for ages 18–20 only, and add a check of the Norwegian text for 15–17-year-olds before 8 Dec, with an owner.

**[Adversarial AG-23]** — Under the PRD's own rules, a tester code can't be attached to an account (FR-50; §4.2; NFR-3)
Fix: Pre-load email-to-code in the playtest environment, or use a signed invitation link. Define how a deleted and re-created account is counted.

**[Adversarial AG-24]** — Seeded test users clash with cause links and replay (NFR-6; FR-51; FR-36/F10; FR-12; FR-42)
Fix: Produce seeded users from scripted playthroughs, or define a "seeded" system cause with explicit exemptions.

**[Adversarial AG-25]** — The pengegave event is unspecified, and the schema can't express it (FR-11; FR-46a; FR-39; option schema)
Fix: Specify its options in FR-11 as shares of the drawn amount, plus a transfer to savings or BSU. Add those effect types to the schema.

**[Adversarial AG-26]** — The failed-login pause lets classmates lock a player out (FR-2; FR-1)
Fix: Pause per address and network pair, or document the risk as accepted.

**[Adversarial AG-27]** — Status and precedence are unreadable, and active-month positions live only in the addendum (§0; addendum)
Fix: Use one status line, move months 1, 4, 7 and 10 into FR-46a, and delete superseded addendum text.

**[Adversarial AG-28]** — Parts of the monthly loop still have to be guessed (FR-12; FR-23; FR-30; FR-55; FR-49; rule 1)
The gaps: when an option-started cost is first charged, the priority of bank messages, the BSU step in the processing order, and drawn versus triggered messages.
Fix: Add the four rules listed in the adversarial review.

## Mechanical notes

- **ID continuity is clean.** FR-1–57, NFR-1–11, SM-1–12 and CM-1–5 are contiguous. Every FR, NFR, UJ, OQ and worked-example reference resolves.
- **The tier column misses partial cuts.** FR-1 (per-network limit, item 11), FR-3 (daily email cap, item 11), FR-5 (Log out on all devices, item 11), FR-38 (BSU comparison, item 4) and FR-23 (borrowing the car and car fuel, item 8) aren't marked. NFR-3's 12-month deletion job is also on item 11.
- **One ID prefix, two meanings.** The addendum's 2026-11-11 decisions D1–D12 collide with disclosures D1–D26 ("D10" and "D11" each mean two things). Rename the decisions, for example to R1–R12.
- **Stale figures:** FR-29 (NOK 9,625), the UJ-4 trace (about NOK 9,300), and A-30's "left out until it has a source" for fuel.
- **Dates and frontmatter:** `prd.md` (`updated: 2026-11-12`, `status: draft`), `addendum.md` (`updated: 2026-11-11`) and `.memlog.md` frontmatter are all behind their content.
- **Cross-reference drift:**
  - §4.4 still says "checkpoints the team sets under OQ-13".
  - The addendum row "OQ-6 blocks the first playtest, and OQ-11 is widened and blocks epics" isn't marked superseded.
- **Glossary drift:**
  - "Feature freeze" (parameter table) against "Extensions frozen" (§4.4).
  - The tier names and "cut list" aren't in the glossary.
- **Literal conflict:** FR-1 says sign-up "asks only for an email address and a password", while FR-5 adds the "stay logged in" box at sign-up.
- **Assumptions Index roundtrip OK.** There are no inline `[ASSUMPTION]` tags, §9 repeats A-26, and A-1–A-30 resolve.
- **Encoding:** clean UTF-8, with no mojibake.

## Reviewer files

- `review-rubric.md`: the rubric walker, 7 dimensions, 19 findings
- `review-adversarial-general.md`: the adversarial lens, 28 findings
- `review-figures.md`: the independent figure check, 14 findings. Scripts are in the session scratchpad (`figcheck/run_all.py`), which is temporary.
- `review-feedback-coverage.md`: coverage of Bård's feedback, 36 points, 14 findings
