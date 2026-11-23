---
title: Readiness review of the planning set before epics
date: 2026-11-23
method: bmad-review, lenses adversarial + edge-case-hunter (structure/prose skipped: substance review)
content: PRD + addendum, Rule Set v1 (brief addendum), ARCHITECTURE-SPINE + SOLUTION-DESIGN, UX DESIGN + EXPERIENCE (11-11)
findings: 65 (adversarial 21, edge-case-hunter 44)
raw: findings.json
---

# Readiness review of the planning set before epics (2026-11-23)

Unranked findings, as the review method requires. Overlap between the lenses is noted where it occurs, because it is signal.

## Overlap between the lenses
- One-off shifts and free time (rule 12 vs FR-47): adversarial 5 and edge-case finding on rule 12.
- Loan amounts in steps of NOK 1,000 (AD-13 vs FR-25): adversarial 9b and edge-case finding on AD-13 quotes.
- Password reset in the playtest, where no email is sent: adversarial 9d and edge-case finding on FR-3/surface 04.

## Status of the open issues (adversarial lens)

**Block story writing now:**
- #83: the one-at-a-time rule (finding 11).
- #51 / OQ-16: minigame content model or cut (finding 7).
- #57 / OQ-17: blocks content stories only.

**Block sprint planning, not epics:**
- #73 / #46: dates (finding 1).

**Block the playtest, not stories:**
- #92: spike (finding 14).
- #82, #69, #108 (finding 18), though the #82 answers feed the FR-50 fields.
- #64.

**Verify before engine test stories rely on them:**
- #81 (finding 19).
- #48 (findings 2 and 3).

**Text only, not blocking:**
- #117: D12/D25/D26 wording. Rule 10's wording is already fixed, but finding 4 shows the answer-key problem is larger than #117.

**Effectively resolved, should be closed:**
- #116 and #120 (finding 13).
- #43: most of its figures are now sourced in Rule Set v1. The email-quota item still stands.

**Go-live or delivery only:**
- #24.
- #45 (finding 15).


## Adversarial

### Adversarial 1
- **Location:** `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md` §4.4 Cut order, "Tentative dates (OQ-13)" and "When to cut"; brief addendum Parameters, Deadline column
- **Problem:** The schedule cannot be met from where the project stands. Today (23 Nov) there is zero code, zero content, no epics and no sprint plan. Yet the plan says:
  - Extensions freeze on 26-27 Nov, and its rule ("Extension FRs not started by the freeze are left out") will mechanically drop FR-4, FR-10, FR-16, FR-19, FR-25, FR-37 and FR-40 in 3-4 days.
  - Core playable 1-3 Dec, otherwise the whole Can-be-cut tier drops.
  - Playtest 8 Dec.
  - OQ-13/#73/#46 (the delivery date) is still open and blocks sprint planning.
- **Fix:** Before create-epics:
  - Re-baseline §4.4 against the real delivery date.
  - Name an explicit "playtest slice" (which FRs the first two sprints build).
  - Decide FR-40 and FR-16 on purpose rather than by the "not started" rule, since A-23/SM-2 need FR-40 and SM-6 needs FR-16.
  - Pre-cut what is clearly out of reach now: cut-list item 11 (login hardening) and item 7 (driving game).
  - Record the new dates in the PRD so sprint planning has an input.
- **If shipped as-is:** Epics get written for the full scope. The checkpoint rule then strips features mid-sprint. UX surfaces 06, 24 and 27 and metrics SM-2 and SM-6 lose their FRs without anyone deciding it. The commit history ends up packed into the last weeks, which grading criterion 1 penalises.

### Adversarial 2
- **Location:** `.docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/ARCHITECTURE-SPINE.md` AD-7 "Freeze"; prd.md FR-58 "Until tuning is frozen"; prd.md §4.4 "If the core still isn't playable by the playtest"; prd.md §8 OQ-8 evidence
- **Problem:** The freeze gate contradicts the "start the playtest anyway" policy.
  - AD-7 says the PR that opens the playtest sets `frozen: true`, and from then on every FR-58 hard gate fails CI.
  - The library-minimum gates are hard: 40 events, 8 per year, about 10 crisis events, 8 boomerang pairs, 6 invitations a year, every offer message.
  - The goal-reachability gate is also hard, and OQ-8 shows it passing by only NOK 488 with expenses. Activity prices (9 marked [ASSUMPTION]) and moped service are still undecided.
  - §4.4 says the playtest starts on 8 Dec "on what is playable" and is not postponed.
  - Nothing says what happens when the freeze PR is red.
- **Fix:** Add a decided fallback to AD-7/FR-58. Either:
  - (a) a playtest-minimum gate set in `content/config/vN/` that the freeze PR must meet, or
  - (b) an explicit rule that the playtest may run on an unfrozen library, with the risk stated.

  Also put the tuning deadline before the freeze date instead of on the same day (8 Dec).
- **If shipped as-is:** On playtest day the freeze PR either can't merge, or the playtest opens on an unfrozen library. In that case mechanics can change under testers' running playthroughs, against NFR-4's pinning.

### Adversarial 3
- **Location:** ARCHITECTURE-SPINE.md Deferred, row "Event authoring | Content epic, after OQ-3 and OQ-8"; prd.md §8 OQ-3 and OQ-8 "Blocks"; GitHub #48
- **Problem:** Event authoring and tuning wait on each other.
  - The spine starts event authoring only after OQ-8 (tuning).
  - The PRD says OQ-8 blocks only "Event balancing".
  - #48 says tuning needs written events with real costs and seeded runs.
  - OQ-3 says it blocks "writing those events", but it really only concerns moped and car figures.
- **Fix:** Change the Deferred row to: "Event authoring starts with the content epic. Tuning (OQ-8) runs on the drafts. OQ-3 blocks only moped and car events." Give the content epic an owner and a throughput target, for example events per week against the 40 minimum.
- **If shipped as-is:** The content epic is ordered after a step that needs its output, so the 40+ events, crisis events and messages are started too late for the freeze.

### Adversarial 4
- **Location:** `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/addendum.md` "UJ-4 month by month"; brief addendum worked examples 17a, 17b, 23 and 26c; prd.md UJ-4 step 4 and UJ-5 persona; prd.md FR-47 and FR-33
- **Problem:** The answer key assumes the player sets weekly hours directly, which FR-47 (#105) no longer allows. Under FR-47, hours change only through +/−2 h offers: request, answer the next month, applied from the month after, one request at a time. Places that break this:
  - The UJ-4 trace pays 12 h already in W+1 (wage 10,142); FR-47 gives W+2. PRD UJ-4 step 4 itself says "from the month after".
  - The trace has "He sets 20 h a week" at W+5.
  - Worked example 23 and UJ-5 have 20 h in months 47-54.
  - The 17b money chaser has 12 h in months 4-18 and 40 h from month 19. That run is the basis of 26c, which FR-33/FR-58 use as a hard CI gate.

  #117 only covers the D12 and rule 10 wording.
- **Fix:** Either:
  - mark 17a, 17b, 23, 26c and the trace explicitly as set test states (hours set directly, not reachable by play), and define the FR-58 hollow-win and seeded-run policies using only legal hour changes; or
  - recompute the trace and examples with FR-47 timing.

  Widen #117 to cover this.
- **If shipped as-is:** Engine tests encode states the pipeline refuses. The hollow-win CI gate is defined on runs no seeded policy can produce. The UJ-4/UJ-5 playtest script can't be followed in the real game.

### Adversarial 5
- **Location:** brief addendum Rules 10 and 12; prd.md FR-47 "One-off shifts", FR-52; worked examples (none covers this)
- **Problem:** One-off shifts (#105/#114) were added with no worked example, although NFR-4 requires examples for new rules, and the free-time rule is ambiguous.
  - Rule 10 says one-off shifts "add hours within the same caps".
  - Rule 12 computes free time from "the month's hours ÷ (52/12)", so a placed shift would lower free time.
  - FR-47 says a shift has "no wellbeing effect of its own".
  - A December shift is paid in January: a new tax year, possibly at a new age rate.
- **Fix:** - Add one sentence to rule 12: one-off shift hours never count in free time.
  - Add a worked example 29 covering: pay rounding, the rate at the age in the month worked, payment at next month's income step, a December shift paid and taxed in January of the next year, the rule 10 / 173 h check, and no shift in month 60.
- **If shipped as-is:** Two engine builders compute different wellbeing and tax for the same plan, and there is no answer key to settle it.

### Adversarial 6
- **Location:** prd addendum "Detail for downstream work" (schemas exist only for event, activity, one-off shift and message); ARCHITECTURE-SPINE.md AD-7 "Layout" and Deferred row "Content schemas in detail"
- **Problem:** Many of AD-7's content folders have no schema, although the spine defers to "the addendum's schemas":
  - `options/` (open options: moped new/used with two prices, licences, card, consumer loan, part-time, full-time and summer jobs, experience)
  - `room/` (layer states and their texts)
  - `texts/` (about 18 ending texts by mechanism and sign, teasers, example purchases, system causes)
  - `expenses/` (one line only)
  - `lists.yaml`

  The event schema also caps options at "2-4" and has no step structure. Crisis months need up to 3 steps whose options are engine actions shown only when possible (sell, BSU withdrawal, payment plan, card off, extra shifts, take a job, lower spending, family, ignore). The card warning (FR-31) is likewise an event with options that depend on the situation and has no schema.
- **Fix:** Before content stories, add schemas for open options, crisis events (steps, plus which options are engine-generated and which are authored), the card warning, room states, texts and expenses to the PRD addendum. Make the FR-58 schema gate list them.
- **If shipped as-is:** Content authors and engine builders invent incompatible shapes. FR-48's "same option" check and the FR-58 schema gate have nothing to check against. Crisis content can't be written.

### Adversarial 7
- **Location:** prd.md FR-51, FR-28, §8 OQ-16; prd addendum Event schema "Option fields" (minigame type); ARCHITECTURE-SPINE.md AD-7 Layout; `.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/EXPERIENCE.md` surface 22; GitHub #51
- **Problem:** The minigame has no content home and its parameters are open.
  - A minigame is defined only as an event-option type ("its situations and right answers").
  - But licences are open options (FR-48) taken from the money view, and AD-7 has no minigame or route folder.
  - OQ-16 (route length, pass mark, retry fee) is open.
  - UX surface 22 is spine-only "until #51".
  - #51 stays open although the PRD already limits MVP minigames to the licences, and FR-30 already decides the gift needs no driving game.
- **Fix:** Decide now: driving game only, with a content folder/schema for routes and situations and OQ-16 defaults in config. Or pre-cut it (cut-list item 7, licences become payment only, D10 changes). Close #51 to match.
- **If shipped as-is:** FR-28/FR-30 stories can't fix when the licence is paid. The minigame epic stalls or gets built without a content model.

### Adversarial 8
- **Location:** ARCHITECTURE-SPINE.md frontmatter `scope`/`binds` (no NFR-1, NFR-2), Deferred row "Everything in the frontend", Consistency Conventions "Tests" row, Structural Seed `ci.yml`; SOLUTION-DESIGN.md §9; EXPERIENCE.md Foundation ("UI system: none is named") and IA "Route (round 3)" column
- **Problem:** No document makes the frontend architecture decisions the epics need. Missing:
  - routing (EXPERIENCE lists hash routes like `#hjem`, while AD-12 uses the path `/nytt-passord` on Next.js)
  - data fetching and client state; the retry / `request_id` client
  - OpenAPI type generation
  - test frameworks and the NFR-9 accessibility check in GitHub Actions: the one `ci.yml` is described by the backend Tests convention only
  - lint/format
  - the frontend Docker/compose service
  - font self-hosting: the mockups load Google Fonts

  Leaving NFR-1/NFR-2 out of the binds is fine for the backend. But parts of NFR-2 are backend game text and are unbound: room-state text alternatives, echo-badge text naming the earlier choice.
- **Fix:** - Write a short frontend architecture spine (FE-AD IDs) binding NFR-1, NFR-2, the NFR-9 accessibility CI check, and FR-6/FR-8 client behaviour, owned by the frontend team, before frontend epics.
  - Add to AD-13 that room-state and echo-badge texts are content strings carried in the view.
  - Give `ci.yml` jobs a named owner per side.
- **If shipped as-is:** Frontend stories have no binding decisions, and the accessibility CI requirement is missed. Grading criterion 5 ("arkitekturen samsvarer med dokumentasjonen") can't be met for half the codebase.

### Adversarial 9
- **Location:** EXPERIENCE.md Component Patterns and IA surface table; ARCHITECTURE-SPINE.md AD-12 "Reset link" and AD-13 "Quotes"; prd.md FR-25, FR-45 money actions, FR-3, NFR-11
- **Problem:** Three UX gaps leave money and reset stories without acceptance criteria.
  - (a) There is no amount-entry pattern for the money actions that take an amount: transfer from NOK 1, BSU deposit with the cap remaining, extra card payment, early payoff, loan amount. There are no states for NFR-7's "not whole kroner / zero or below / outside range" refusals.
  - (b) The UX loan sheet shows quotes only at the maximum amount. The spine offers `/api/game/quote` for other amounts "in steps of NOK 1,000", a step the PRD never states.
  - (c) There is no surface for the `/nytt-passord#token=` set-new-password page.
  - (d) There is no playtest text for "Glemt passord", where no email will ever arrive (NFR-11).
- **Fix:** - Add an amount-input component with its refusal states.
  - Add a "Nytt passord" surface with used/expired states.
  - Put the NOK 1,000 loan step into FR-25, or drop it from AD-13.
  - Add playtest-specific copy for surface 04 ("Ta kontakt med teamet for ny lenke").
- **If shipped as-is:** Money-action stories are built without agreed validation UX. Reset links the team hands out in the playtest land on an unspecified page. Testers wait for emails that never come.

### Adversarial 10
- **Location:** prd.md NFR-3 "Playtests" and "Scope of the privacy work"; prd.md FR-50; ARCHITECTURE-SPINE.md AD-15 "Tester codes", AD-12 "Playtest"
- **Problem:** Nothing restricts who can sign up on the playtest site. The playtest frontend is a public Vercel URL with open sign-up. The privacy scoping that needs no approval rests on "only 18-20-year-olds take part". Yet:
  - nothing limits sign-up to invited testers;
  - accounts without a tester code are still created, logged (Railway logs IPs in the US for 90 days) and processed, and are only skipped at export.
- **Fix:** Add to FR-50/NFR-3 and AD-15: while `PLAYTEST_RECORDS` is on, sign-up accepts only normalized addresses present in `tester_codes`, and others get a neutral refusal. Optionally add `noindex` on the playtest frontend.
- **If shipped as-is:** Minors or strangers create accounts outside the assessed privacy scope. Data the team never meant to hold ends up in US logs, and the metrics base is polluted.

### Adversarial 11
- **Location:** prd.md FR-48 ("opens again when its one-at-a-time rule allows another"), FR-55 "Offers always arrive"; GitHub #83
- **Problem:** The "one-at-a-time rule" is still not defined per open option.
  - Can a second credit card be taken, or the card again later?
  - Can the experience be bought twice?
  - Can a moped be bought again after selling?
  - Can a new consumer loan follow a payoff?

  Offer suppression (FR-55) and open-option availability depend on the answers.
- **Fix:** Add a table to FR-48: for each open option, once per playthrough, one at a time (can be repeated after it ends), or repeatable. Close #83 with it.
- **If shipped as-is:** FR-48 and FR-55 stories pick different rules, and the offer-message tests disagree with the money view.

### Adversarial 12
- **Location:** prd.md §4.1 In Scope ("Wellbeing, room layers, and visible future opportunities"), §4.4 Extension list, FR overview row FR-35 (tier "Extension"), §3 Glossary "Flag" ("what a choice opened or closed (FR-35)"), §8 OQ-9
- **Problem:** Several places still list FR-35 as in scope, although the 2026-11-23 decision (#115) left it out. OQ-9 (avatar contents) is still open although EXPERIENCE settled it (six preset looks).
- **Fix:** - Set FR-35's tier to "Left out (#115)" in the overview, and remove it from §4.1, the §4.4 Extension list and the Glossary.
  - Close OQ-9, citing EXPERIENCE surface 06.
- **If shipped as-is:** create-epics-and-stories reads the overview and §4.1 and produces FR-35 stories plus an avatar question that no longer exists.

### Adversarial 13
- **Location:** EXPERIENCE.md Open Questions and the intro paragraph / `sources`; DESIGN.md `sources`; GitHub #116 and #120
- **Problem:** The UX documents carry stale references.
  - EXPERIENCE "Open Questions" still says the PRD texts for #111/#114/#115 are missing, and that start year, monthly totals and bands "are not in the player view yet (#116)". PRD FR-33/FR-47/FR-35 and spine AD-13 now carry them.
  - Both spines cite or "build on" the superseded `ux-IBE160-G13-2026-11-17/` folder: EXPERIENCE builds on "saegg1205's shared spine", and DESIGN sources Speilet's DESIGN.md.
  - #116 and #120 are still open although their content has landed (commits 8812ce7, f2fdf4d).
- **Fix:** - Update Open Questions to only #117, #51 and the 320 px sticker check.
  - Replace the inheritance sentence with "self-contained; the 11-17 folder is history only".
  - Close #116 and #120 when PR #119 merges.
- **If shipped as-is:** Story writers chase questions that are already answered, or treat superseded documents as binding.

### Adversarial 14
- **Location:** `.docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/SOLUTION-DESIGN.md` §6, §11, §12; ARCHITECTURE-SPINE.md AD-14 "Sprint-1 spike" ("The checklist lives in #92"); GitHub #92 body
- **Problem:** The spike checklist and the solution design lag the spine.
  - AD-14 has about 14 spike checks. #92, which AD-14 names as the checklist, lists only the original 7. Missing from #92: the visitor-IP header through Vercel and Railway's edge (`x-vercel-forwarded-for`, forged headers ignored), cookies passed through, no `/api` caching, the origin-secret refusal, `railway config plan` changing nothing, and `server_version`.
  - SOLUTION-DESIGN §6's content tree omits `shifts/` and `lists.yaml`.
  - §11 has the old 7 spike checks.
  - §12 doesn't mention the 2026-11-23 validation.
- **Fix:** Copy AD-14's spike list into #92 as checkboxes, and bring SOLUTION-DESIGN §6, §11 and §12 in line with the spine.
- **If shipped as-is:** The spike passes on an incomplete list and the IP-header fallback is never exercised, so every tester could share one login limit (validation H1). The examiner-facing companion contradicts the spine.

### Adversarial 15
- **Location:** prd addendum "Changes from the proposal"; `.docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/brief.md` (Scope paragraph, cut-order paragraph); `docs/sensorveiledning/sensorveiledning-ibe160-del1.md` §3 step 1, criterion 2, §5 warning signs
- **Problem:** The examiner reads the brief first, and it describes things the plan no longer does:
  - "Supabase for database and authentication" and "Supabase runs self-hosted via Docker";
  - "events down to the minimum of 50";
  - cut steps in "PRD (§4.1)".

  The plan uses its own login, plain postgres:17, a minimum of 40 events and §4.4. The "Changes from the proposal" table also omits Supabase Auth → own login, local Postgres instead of self-hosted Supabase, Vercel/Railway hosting and testers aged 18-20 only. The proposal itself is not in the repo (#45, OQ-15).
- **Fix:** - Add these rows with reasons to the changes table.
  - Add a dated note at the top of brief.md pointing to the PRD and spine where they differ.
  - Commit the approved proposal.
- **If shipped as-is:** Grading criterion 2 requires deviations to be described and justified, and §5 flags plans that "beskriver en annen app". This costs marks on the 20 % and 30 % criteria.

### Adversarial 16
- **Location:** prd addendum Event schema, "Option fields" ("a loan (allowed range and terms)"); brief addendum Parameters row "Consumer loan terms" ("the loan option takes its range and terms from configuration, never its own"); ARCHITECTURE-SPINE.md AD-13 "Quotes"
- **Problem:** The two addenda contradict each other. The PRD addendum lets each loan option define its own range and terms. The Rule Set says terms come only from config, and AD-13's quotes use the config list.
- **Fix:** Change the option type to "a loan (amount bounds from FR-25, terms from config; no per-option values)" and add a content-check rule rejecting per-option terms.
- **If shipped as-is:** An event offers a 6- or 48-month loan that the quote endpoint and the UX's 12/24/36 toggles can't show, and the schema gate accepts it.

### Adversarial 17
- **Location:** EXPERIENCE.md Key Flows, Flow 1 step 4 and Flow 4; prd.md UJ-3 persona and context, FR-55 bank messages
- **Problem:** The UX flows contradict the PRD persona and the message rules.
  - Flow 1 has Markus put all 18,500 kr in savings («Sett alt på sparekontoen»). UJ-3 says he "spent most of his pengegave … put a little into savings".
  - Flow 4 fires the one-time «tjent over 50 kr i rente» message "mid-game" with month-35 figures (23,500 kr) and «I januar i fjor». Under FR-55, an 18,500 kr deposit passes NOK 50 of interest in month 3. The pengegave month (January 2026) would also be formatted «januar 2026» by AD-13's month placeholder in 2028, not «i fjor».
- **Fix:** Align Flow 1 with UJ-1/UJ-3 (a small deposit). Re-time Flow 4 to the month the threshold is actually crossed, with figures and month text that match AD-13's formatter.
- **If shipped as-is:** Stories, playtest scripts and formatter tests copied from the flows encode an impossible sequence and wrong date text.

### Adversarial 18
- **Location:** prd.md §7.1 SM-2, SM-6, SM-10 and "Counted from records"; prd.md FR-11 vs FR-50 "How time is measured"; `.docs/planning-artifacts/playtest/rubric-written-explanations.md` (status: draft); GitHub #82, #69, #108
- **Problem:** Metric definitions that FR-50's record fields depend on are still undecided.
  - SM-2's "Higher after" has no minimum, so it can't fail.
  - SM-6's 3-day window sits inside a test of at least 3 days.
  - SM-10/FR-50 measure from creating the user, while FR-11 measures from "opening the game".
  - The rubric is a draft and the quiz awaits teacher review.
- **Fix:** Before the FR-50 story:
  - set SM-2's minimum gain;
  - set the playtest length relative to the 3-day window;
  - align the SM-10 and FR-11 start points;
  - approve the rubric;
  - book the teacher review with a date before the quiz.
- **If shipped as-is:** Records are built with the wrong fields or start points, and the metrics can't be measured, or can't fail, after the one-shot playtest.

### Adversarial 19
- **Location:** brief addendum, the closing paragraph of "Worked examples" (examples 17a, 22, 23 and the UJ-4 trace recalculated with moped fuel by "Claude's script only, with no independent check yet"); prd.md NFR-4 "Frozen test figures"; GitHub #81
- **Problem:** Answer-key figures changed without the process NFR-4 requires. NFR-4 says the key changes only after a second, independent calculation, but 17a, 22, 23 and the UJ-4 trace changed on a single AI recomputation. (17a and 23 are also hit by finding 4.)
- **Fix:** Have a team member reproduce the four in a spreadsheet, as in #78, before engine stories cite them. Until then, mark them provisional in the addendum.
- **If shipped as-is:** The engine is built and tested against an unverified key. A later correction rewrites tests and forces Dahl to arbitrate mid-sprint.

### Adversarial 20
- **Location:** ARCHITECTURE-SPINE.md Consistency Conventions (Tests row; no lint/format or review row); `docs/sensorveiledning/sensorveiledning-ibe160-del1.md` criteria 3 and 5
- **Problem:** The plan has no linter or formatter policy beyond one ruff banned-api rule for `engine`, nothing for the frontend, and no pull-request review policy. Grading criterion 5 looks for "konsekvent stil, gjerne støttet av linter", and criterion 3 for traces of code review of AI-generated code.
- **Fix:** Add conventions:
  - `ruff check` + `ruff format` (and optionally a type checker) on the backend, and ESLint + Prettier on the frontend, all as CI jobs;
  - every story PR gets a named reviewer plus a recorded code review before merge.
- **If shipped as-is:** Inconsistent AI-generated code and no visible review trail, which lowers two graded criteria (25 % combined).

### Adversarial 21
- **Location:** prd addendum "Privacy measures in the MVP", "Player information covers"; prd.md NFR-3; ARCHITECTURE-SPINE.md AD-12 "Player information"; EXPERIENCE.md Component Patterns "Info box"
- **Problem:** Three documents define the player information page differently, and none is named the source.
  - The addendum lists processors as "the database host and any email relay" (stale) and includes "who to contact", "no marketing, no other sharing, no AI" and "who the game is for".
  - AD-12 names only processors and log notes.
  - EXPERIENCE omits contact, purpose limits and audience.
- **Fix:** Make NFR-3 the single list of required contents (including a contact point and the 15-20 audience), update the addendum's processor line to Vercel/Railway/Supabase, and point AD-12 and EXPERIENCE to it.
- **If shipped as-is:** The frontend team ships a page with no contact point or audience statement. That is the one privacy text minors and testers see before sign-up.


## Edge-Case Hunter

### Edge-Case Hunter 1
- **Location:** .docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md: Rules, rule 9 (BSU deduction); PRD FR-22
- **Problem:** Player deposits in BSU, then withdraws and closes it before December continue
- **Fix:** deduction = 0 if bsu.closed_in_year(year) else min(round2(0.10*min(deposits,27500)), year_tax)
- **If shipped as-is:** Deduction paid for a closed BSU, after the clawback at withdrawal already ran

### Edge-Case Hunter 2
- **Location:** Rule Set v1 rule 9 vs .docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/ARCHITECTURE-SPINE.md: AD-6 Money
- **Problem:** The year's BSU deposits aren't a multiple of 10 (e.g. 1,235 gives 123.5)
- **Fix:** rule 9: deduction = round_rule2(Decimal(deposits_capped) * Decimal('0.10')); add to AD-6 named rounding points
- **If shipped as-is:** AD-6 forbids rounding points it doesn't name, so builders truncate or round differently

### Edge-Case Hunter 3
- **Location:** Rule Set v1 rule 5; PRD FR-26; EXPERIENCE.md Component Patterns: Credit card
- **Problem:** Fixed card payment set earlier falls below a later month's higher minimum
- **Fix:** pay = max(fixed, minimum + overdue) or define fixed<minimum as missed minimum; and if fixed >= balance: pay balance, no interest
- **If shipped as-is:** Fixed setting silently becomes missed minimums and a crisis trigger, or overpays the balance

### Edge-Case Hunter 4
- **Location:** PRD FR-26 (choose payment when taking the card); EXPERIENCE.md Credit card stepper
- **Problem:** Card taken with balance 0, so minimum is 0 and stepper range is empty
- **Fix:** fixed_amount in {100*k : k>=1}; validate against minimum only at bill time; define step base (multiples of 100 vs minimum+100k)
- **If shipped as-is:** Fixed mode can't be chosen at card opening; step base differs between frontend and engine

### Edge-Case Hunter 5
- **Location:** PRD FR-45 payment order row 'Extra card payment, and early payoff'
- **Problem:** Extra card payment amount larger than the current card balance
- **Fix:** if amount > card.balance + card.overdue: refuse invalid_input  # range upper bound = balance
- **If shipped as-is:** Negative card balance; interest, minimum and trigger formulas meet an undefined sign

### Edge-Case Hunter 6
- **Location:** PRD FR-45 ('A negative current account ... can't pay for choices'), FR-48 'Can't pay yet'
- **Problem:** Current account negative while savings hold money, and player picks a paid option
- **Fix:** affordable = max(0, current + savings) >= cost  # or: savings usable only above the deficit; state missing = cost - that
- **If shipped as-is:** Engine and UI disagree on affordability and the 'Mangler … kr' amount

### Edge-Case Hunter 7
- **Location:** PRD FR-57 Progress; FR-9c; FR-55 bank messages
- **Problem:** Current account plus savings, or goal-1 net savings, is negative
- **Fix:** progress_pct = clamp(numerator / price, 0, 1)  # lower bound 0 stated for target and goal 1
- **If shipped as-is:** Negative percentages shown, or threshold logic fires oddly after recovery

### Edge-Case Hunter 8
- **Location:** PRD FR-55 Bank messages ('passes 25, 50, 75, or 100%')
- **Problem:** Progress lands exactly on a threshold; progress is capped at 100%
- **Fix:** sent_when progress >= threshold  # 'passes' can never exceed the 100% cap
- **If shipped as-is:** The 100% message never sends, or exact-threshold cases differ between builders

### Edge-Case Hunter 9
- **Location:** Rule Set v1 rule 8 (loss ending); PRD FR-41; FR-49 month-60 warning
- **Problem:** Trigger true at end of 59, month-60 crisis skipped at open, true again at end of 60
- **Fix:** loss = trig in end59_true and trig in end60_true  # state explicitly whether a false month-60 open check resets it
- **If shipped as-is:** Loss vs non-loss decided differently in engine, F9 tests and warning copy

### Edge-Case Hunter 10
- **Location:** EXPERIENCE.md Component Patterns: Crisis check, State Patterns: Confirm before continuing; PRD FR-32a cooldown
- **Problem:** A trigger is true while a cooldown runs, so no crisis starts next month
- **Fix:** status = cooldown_true ? 'Krise i <first month after cooldown> hvis …' and confirm: skip or explain; view carries cooldown flag
- **If shipped as-is:** UI says 'Krise i <next month>' and asks to confirm a crisis that won't come

### Edge-Case Hunter 11
- **Location:** Rule Set v1 rule 12 (free time from the month's hours) vs PRD FR-47 one-off shifts ('no wellbeing effect of its own')
- **Problem:** Player places a one-off shift, which adds hours to the month
- **Fix:** free_time_hours = weekly_hours_setting + extra_shifts  # explicitly exclude one-off shift hours from rule 12
- **If shipped as-is:** Placing a shift lowers free time and score in one build but not another

### Edge-Case Hunter 12
- **Location:** PRD FR-47 One-off shifts, NFR-7 Month plan refusals
- **Problem:** Player quits or changes job after placing one-off shifts in the same month
- **Fix:** on quit: drop placed shifts with note, or keep and pay next income step; recheck shifts at continue like FR-53
- **If shipped as-is:** Pay with no job, or shift silently lost; steady-wage and rule 8 figures diverge

### Edge-Case Hunter 13
- **Location:** PRD FR-47 Hours offers; FR-18 full-time job row (offered 54, starts 55)
- **Problem:** Hours request pending when player quits or the full-time job replaces part-time
- **Fix:** on job change/quit: cancel pending hours request and open hours offer; answer message not sent
- **If shipped as-is:** Next month's employer offer applies 2 h to a job that no longer exists

### Edge-Case Hunter 14
- **Location:** PRD FR-47 Hours offers ('2 h a week', floor 4 h, full-time 37.5 to 40)
- **Problem:** A 2 h step crosses the limit or floor (37.5 to 39.5, then 41.5; 5 to 3)
- **Fix:** offer_delta = min(step, limit - hours) for more; min(step, hours - floor) for fewer; no only if delta == 0
- **If shipped as-is:** Full-time can't reach 40 h as FR-47 promises, or exceeds rule 10

### Edge-Case Hunter 15
- **Location:** PRD FR-47 Monthly cap; Rule Set v1 rule 10 ('If the cut would leave 0 h when the offer is made')
- **Problem:** Summer job blocked at June offer, then player quits or lowers hours in June
- **Fix:** summer_job.takeable = remaining_cap(july_hours_now) > 0  # re-evaluate on each request until July income step
- **If shipped as-is:** Player who freed the cap still can't take the job, or engines differ

### Edge-Case Hunter 16
- **Location:** ARCHITECTURE-SPINE.md AD-6 Money (Decimal); Rule Set v1 rule 10 (×52/12)
- **Problem:** Non-terminating 52/12 products computed in different operation order or context precision
- **Fix:** hours = Decimal(weekly) * 52 / 12 computed as (weekly*52)/12 with fixed getcontext().prec; compare caps on that exact form
- **If shipped as-is:** 12 h × 52/12 gives 51.999…; cap checks and half-up pay rounding drift

### Edge-Case Hunter 17
- **Location:** Rule Set v1 rule 4, rule 15; PRD FR-25, FR-27
- **Problem:** Loan, payment plan or family loan taken mid-month after that month's debt step
- **Fix:** first_instalment_month = taken_month + 1; first interest accrues at month+1 debt step  # state in rule 4
- **If shipped as-is:** Only derivable from worked example 18g; plans may charge twice or skip a month

### Edge-Case Hunter 18
- **Location:** Rule Set v1 rule 4 ('One they can't cover moves to the end'); PRD FR-27
- **Problem:** Accounts cover part of a family-loan instalment (e.g. 800 of 833)
- **Fix:** if current+savings < instalment: pay 0 and postpone whole instalment  # or pay partial and postpone remainder; pick one
- **If shipped as-is:** Instalment schedule and stress +5 differ between builds

### Edge-Case Hunter 19
- **Location:** ARCHITECTURE-SPINE.md AD-13 Quotes (steps of NOK 1,000) vs PRD FR-25
- **Problem:** Take-loan action sends an amount not a multiple of 1,000 (e.g. 7,500)
- **Fix:** loan.amount % 1000 == 0 and 5000 <= amount <= cap else invalid_input  # same rule for quote and action
- **If shipped as-is:** Loan can be taken at an amount no quote could show

### Edge-Case Hunter 20
- **Location:** ARCHITECTURE-SPINE.md AD-13 Quotes; EXPERIENCE.md Consumer loan
- **Problem:** Quote requested or view built when no loan is possible (under 18, no steady wage, 59-60, cap<5,000, status none)
- **Fix:** view.loan_quotes = [] with reason code; GET /quote -> 409 <code> when loan unavailable, 422 only for bad params
- **If shipped as-is:** Endpoint returns misleading 422s or quotes for loans the action refuses

### Edge-Case Hunter 21
- **Location:** PRD §3 Glossary 'Steady wage', FR-25 ('last three months') vs Rule Set v1 rule 8 ('this month and the two before')
- **Problem:** Card or loan requested in month M after M's income step
- **Fix:** steady_wage = all(wage[m] > 0 for m in (M, M-1, M-2))  # define window once, shared with loan cap
- **If shipped as-is:** Month-37 card eligibility and loan cap differ by one month between builds

### Edge-Case Hunter 22
- **Location:** ARCHITECTURE-SPINE.md AD-9 One writer ('Wages and other income never pay the card outside the debt step')
- **Problem:** Sale or open-option payout in a crisis month pays overdue card minimums
- **Fix:** reword: 'outside the debt step and the rule 8 crisis money-in order'
- **If shipped as-is:** Sentence contradicts the crisis money-in rule beside it; builders pick one

### Edge-Case Hunter 23
- **Location:** Rule Set v1 Parameters table; ARCHITECTURE-SPINE.md AD-7 Loading ('engine never supplies a default'), Config convention
- **Problem:** Game figures named as configuration lack a parameter row
- **Fix:** add rows: pengegave range+step, active months, hours-offer step/floor, part/full-time hours, 3x debt/loan multiplier, parents' insurance share+chance, expenses per year, shifts per month
- **If shipped as-is:** Config files have no sourced value; startup fails or values get invented

### Edge-Case Hunter 24
- **Location:** PRD FR-11; ARCHITECTURE-SPINE.md AD-4 Months ('A start opens month 1, and setup steps … are game requests for month 1')
- **Problem:** Month-1 steps (unexpected expense) or money actions run before the pengegave choice
- **Fix:** credit pengegave at start before open_month(1) or exclude month 1 from expense draw; refuse money/plan actions until setup_done
- **If shipped as-is:** Account negative at 15 before first choice, or pengegave moved before its event

### Edge-Case Hunter 25
- **Location:** ARCHITECTURE-SPINE.md AD-4 Life requests; PRD FR-43 Starting over before 20
- **Problem:** Start action sent while the current playthrough is still active
- **Fix:** if action.type == 'start' and current.status == 'active': refuse 409 <code>  # end early first
- **If shipped as-is:** Active life deleted without the confirm and end-early record FR-43 and FR-50 expect

### Edge-Case Hunter 26
- **Location:** PRD FR-45, FR-17 (regular event options); FR-32b defines possibility only for crisis options
- **Problem:** Regular event option's typed effect conflicts with state (second job, family loan, extra shifts, moped)
- **Fix:** option.available = typed_effect_allowed(state) and affordable; show reason; keep at least one available free option
- **If shipped as-is:** Options shown as pickable then refused, or no rule for 'shown as unavailable'

### Edge-Case Hunter 27
- **Location:** ARCHITECTURE-SPINE.md AD-4 Protocol fields (plan_version only on continue); PRD FR-52
- **Problem:** Stale device places on or removes from an evening another device already changed
- **Fix:** place/remove carry plan_version or target item id; mismatch -> 409 plan_changed
- **If shipped as-is:** Stale remove deletes a different activity than shown; evening overwritten

### Edge-Case Hunter 28
- **Location:** PRD FR-52 Same as last month; EXPERIENCE.md Same as last month
- **Problem:** This month has fewer free evenings than last month's placed activities
- **Fix:** place in last month's slot order until free slots run out; report the rest as not placed
- **If shipped as-is:** Which activities get dropped is undefined

### Edge-Case Hunter 29
- **Location:** ARCHITECTURE-SPINE.md AD-7 Freeze (text-only edits allowed) and AD-13 Game text (captured parameters)
- **Problem:** Text-only edit of frozen item adds a placeholder that stored past items didn't capture
- **Fix:** content check: frozen item's template placeholder set may not grow; render missing param -> fail check, never 500
- **If shipped as-is:** Old messages and results fail to render in running playthroughs

### Edge-Case Hunter 30
- **Location:** ARCHITECTURE-SPINE.md AD-7 Freeze/Manifest (unfrozen version may change freely; local/ci pin newest)
- **Problem:** Item id referenced by a running playthrough's state is removed from an unfrozen version
- **Fix:** loader/view: unknown content id -> upgrade step or clear-game-data; never resolve to KeyError
- **If shipped as-is:** Dev, examiner or pre-freeze playtest games crash on load

### Edge-Case Hunter 31
- **Location:** ARCHITECTURE-SPINE.md AD-9 Month totals ('A state document upgraded to this schema starts the list empty'); AD-13 Money per month
- **Problem:** Mid-year state_schema upgrade leaves closed months with no totals entry
- **Fix:** view: closed month without totals -> marked 'unknown', excluded from year so far with a note
- **If shipped as-is:** Året and year so far show wrong sums, or null for closed months

### Edge-Case Hunter 32
- **Location:** ARCHITECTURE-SPINE.md AD-14 Speed and fallback (switch to Railway Postgres by changing DATABASE_URL)
- **Problem:** Fallback switch during the playtest with live tester data in Supabase
- **Fix:** fallback runbook: pg_dump Supabase -> restore Railway Postgres before switching DATABASE_URL
- **If shipped as-is:** All tester accounts, playthroughs and FR-50 records lost mid-playtest

### Edge-Case Hunter 33
- **Location:** PRD FR-3; EXPERIENCE.md surface 04 and 'Reset link used or expired'; ARCHITECTURE-SPINE.md AD-11 null sender
- **Problem:** Tester requests a reset, or a new link, in the playtest where nothing is sent
- **Fix:** if sender == null: forgot screen copy says 'Ta kontakt med teamet for ny lenke'; expired-link page same
- **If shipped as-is:** Tester waits for an email that never comes; 'offers a new one' does nothing

### Edge-Case Hunter 34
- **Location:** PRD addendum 'Login with email' limits table (login per network 300/h) vs PRD FR-2 and ARCHITECTURE-SPINE.md AD-10 Limits
- **Problem:** Many logins from one school network within an hour
- **Fix:** AD-10: login_per_network = 300/h counting failed only (or all), answered 429 rate_limited
- **If shipped as-is:** Limit unbuilt or built counting successes, blocking classes behind one NAT

### Edge-Case Hunter 35
- **Location:** ARCHITECTURE-SPINE.md AD-13 Errors fields codes; EXPERIENCE.md State Patterns: Nickname invalid, Password too short
- **Problem:** Nickname over 16 characters or password over 128 characters submitted
- **Fix:** add field code too_long and UX messages for nickname and password maximums
- **If shipped as-is:** Server refuses with no code or copy to show; field can't be marked

### Edge-Case Hunter 36
- **Location:** ARCHITECTURE-SPINE.md AD-10 Limits; PRD FR-4, FR-44
- **Problem:** Repeated wrong current password on change-password or delete-account
- **Fix:** count wrong_password per (user, network) in auth_attempts; pause after N like failed login
- **If shipped as-is:** Session left open on a school PC lets someone guess the password unlimited

### Edge-Case Hunter 37
- **Location:** ARCHITECTURE-SPINE.md AD-10 Reset links / Revocation; PRD FR-4, FR-5
- **Problem:** Password changed or 'log out on all devices' while a reset link is outstanding
- **Fix:** on password change and logout-all: DELETE FROM reset_links WHERE user_id = :uid
- **If shipped as-is:** Old link still resets the password after the player secured the account

### Edge-Case Hunter 38
- **Location:** PRD FR-5 'Log out on all devices'; ARCHITECTURE-SPINE.md AD-10 Revocation; EXPERIENCE.md Menu
- **Problem:** Player chooses Log out on all devices on the current device
- **Fix:** state explicitly: delete all session rows including current (or all except current) and the resulting screen
- **If shipped as-is:** Current device logged out in one build, kept in another

### Edge-Case Hunter 39
- **Location:** ARCHITECTURE-SPINE.md AD-15 Account deletion / Tester codes
- **Problem:** Tester deletes account, then re-creates it with the same address
- **Fix:** on sign-up with address in tester_codes after a counted deletion: decrement testers_left (or count distinct addresses)
- **If shipped as-is:** testers_left counts a returning tester as having left

### Edge-Case Hunter 40
- **Location:** .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/DESIGN.md Scene (marker at most 27% wide); PRD FR-1 (16 characters)
- **Problem:** 16-character nickname in the Kalam hub marker at 320 px
- **Fix:** marker: wrap to two lines or scale font with a minimum; else truncate with full name in alt text
- **If shipped as-is:** Marker overflows the frame or covers the window

### Edge-Case Hunter 41
- **Location:** PRD FR-1 ('text reads correctly with any nickname the rules allow'); AD-13 Game text
- **Problem:** Template uses the nickname in genitive and nickname ends in s, x or z
- **Fix:** provide {nickname_gen} placeholder (Markus' / Maks) or content check bans genitive use of {nickname}
- **If shipped as-is:** Ungrammatical text like «Markuss» for allowed nicknames

### Edge-Case Hunter 42
- **Location:** PRD FR-39 Money kept; EXPERIENCE.md Flow 7 copy
- **Problem:** Compared option has a worse direct kroner effect than the chosen one
- **Fix:** template by sign: mer when diff>0, mindre when diff<0; skip line when diff==0
- **If shipped as-is:** Line claims 'X kr mer' when the other choice would have left less

### Edge-Case Hunter 43
- **Location:** EXPERIENCE.md State Patterns: Can't afford vs PRD FR-53, FR-45 (card pays card-payable activities)
- **Problem:** Accounts short but a card-payable activity fits under the card limit
- **Fix:** affordable = fits_on_card(item, planned) or current+savings >= cost  # UX copy follows engine flag
- **If shipped as-is:** UI shows 'Mangler … kr' for an activity the engine would accept

### Edge-Case Hunter 44
- **Location:** EXPERIENCE.md State Patterns (Saving covers choices only); ARCHITECTURE-SPINE.md AD-2 (account requests not retried)
- **Problem:** Change-password or delete form submitted twice, or response lost
- **Fix:** account forms lock while saving; on 403 wrong_password after a lost response, refetch session before showing error
- **If shipped as-is:** Second submit shows «Feil passord» though the change succeeded
