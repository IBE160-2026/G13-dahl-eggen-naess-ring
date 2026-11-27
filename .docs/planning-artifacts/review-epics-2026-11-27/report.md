---
title: Review of epics.md
date: 2026-11-27
method: bmad-review, lenses adversarial + edge-case-hunter + structure + prose (prose ran on top of structure)
content: .docs/planning-artifacts/epics.md at main 2dbbd4c (10 epics, 73 stories)
findings: 139 (adversarial 30, edge-case-hunter 58, structure 16, prose 35)
raw: findings.json
---

# Review of epics.md (2026-11-27)

Unranked findings, as the review method requires. Adversarial, edge-case-hunter and structure each ran on their own without seeing the others' findings, so overlap between them is signal. Prose ran after structure and skipped text that structure proposes to cut or rewrite.

Line numbers refer to `epics.md` at commit `2dbbd4c`.

## Overlap between the lenses

Found by more than one lens on its own:

- **Steady wage is undefined.** Nothing defines the window or what counts for `steady_monthly_wage`, which gates the card and the loan (adversarial 4, edge-case on Story 7.1).
- **Facts with no provider yet.** The ending and Epic 3-4 logic read facts (debt, `experience_bought`, `owns_moped`) whose slice comes later, and no default is defined (adversarial 5, edge-case on Story 4.4).
- **Ended-early lives.** Story 4.6 promises an ending summary for a life that never got an ending (adversarial 10, edge-case on Story 4.6).
- **Open #123 items aren't tied to stories.** Adversarial 3 says no story names its #123 dependency. Edge-case-hunter found about 15 of these gaps one by one (marked #123): reset links after password change, quitting with placed shifts, the month-60 skipped crisis, partial family-loan instalments, the loan's first instalment and more.
- **BSU clawback and the December deduction.** Unclear owner and order (adversarial 12, edge-case on Story 3.2/6.5).
- **`plan_version`.** No kernel story builds it, and place/remove from two devices is undefined (adversarial 11, edge-case on Story 6.1).
- **Affordability: current account vs savings.** 2.5 and 3.4 disagree, and the negative-balance case is undefined (adversarial 18, edge-case on Story 3.4).
- **Tax model.** Monthly vs December, and which tax year a December shift belongs to (adversarial 9, edge-case on Story 6.7).
- **Starting a new life when one exists.** 2.2 refuses any existing playthrough, which blocks 4.6, and the order inside the start transaction is undefined (adversarial 30, edge-case on Story 2.2/4.6).
- **The redirect check deferred from 1.4 to 10.4.** All three: adversarial says to automate it in 1.4, structure asks where it belongs, prose flags the contradicting reason clause.
- **Stories 8.6-8.10.** Structure wants the shared ACs stated once, prose flags the user story, and adversarial says no per-year story owns boomerang pairs, crisis events or offer messages.
- **The readiness-review section goes stale.** Structure wants it moved; prose flags 'this branch' and 'set test states'.
- **Tester list and accounts.** The tester guard leaks membership (adversarial 20), and a returning tester is counted as having left (edge-case on Story 10.1).

## Adversarial (30)
### Adversarial 1
- **Location:** epics.md Epic List order (l.358), Tier table (l.386-392), Epic 9 Notes (l.437)
- **Problem:** The strict order puts the Core stories 9.1 («Hvorfor?», 'never cut') and 9.4 (upcoming costs) after the Can-be-cut stories 8.4 and 8.5 and after the whole content epic. Under time pressure the must-be-in work comes last.
- **Fix:** Add a rule that Core stories are scheduled before Extension and Can-be-cut stories in any epic that runs later. For example, move 9.1 and 9.4 before 8.4, 8.5 and 9.2-9.5, or let them start right after 2.5 and 3.4, which they depend on. Replace the single linear order with a per-story dependency list.
- **If shipped as-is:** If the deadline slips, the Core features the PRD requires (FR-38, FR-57) are the ones left unbuilt, while the optional gift moped and car licence ship.

### Adversarial 2
- **Location:** epics.md Epic List order (l.358) vs Epic 8 Notes (l.432)
- **Problem:** The document says epics run strictly one after another, and in the same breath says that content drafting and the content check can start much earlier. Nothing marks which stories can run in parallel.
- **Fix:** Replace 'one after the other' with an explicit per-story 'Depends on:' line, and derive the order and the allowed parallelism from it (for example '8.11 depends on 2.1, 2.6; 8.6-8.10 depend on 2.1 and #126').
- **If shipped as-is:** A four-person team either serializes work that could run in parallel and misses the delivery, or works in parallel without a stated basis, which leads to rework and broken assumptions.

### Adversarial 3
- **Location:** epics.md Epic 2 Notes (l.402); readiness list (l.214, l.218)
- **Problem:** No story names which #123 or #81 items it depends on: 1.6 (cancelling reset links on password change), 6.3 and 6.7 (quitting with placed one-off shifts or a pending hours request), 7.5 (loss rule when month 60's crisis is skipped at open), 7.1 and 7.3 (the steady-wage window), 4.5 (the sign of the FR-39 line). The gate can't be enforced.
- **Fix:** Add a 'Blocked by:' line to every affected story listing the specific #123 bullet or #81 figure, and add the resolved rule to that story's ACs once the item is settled.
- **If shipped as-is:** Developers implement the edge cases however they guess. The engine then disagrees with the later #123 decisions or the answer key, and stories are reopened after merge.

### Adversarial 4
- **Location:** epics.md Story 7.1 (l.1682, l.1685), Story 7.3 (l.1736), Story 6.3 facts (l.1540)
- **Problem:** 'Steady wage' gates the card and the loan and is provided as the `steady_monthly_wage` fact, but no story defines it: not the window, not the threshold, not whether summer jobs or one-off shifts count. #123 lists the steady-wage window as open.
- **Fix:** In 6.3, add an AC that defines `steady_monthly_wage` (for example 'a part- or full-time job with weekly hours > 0 in each of the last N months, N in config; summer jobs and one-off shifts don't count'), with tests at the boundaries.
- **If shipped as-is:** The work and credit slices interpret eligibility differently. A card or loan is refused or allowed inconsistently, and the related NFR-7 refusal tests can't be written.

### Adversarial 5
- **Location:** epics.md Story 4.4 Extension points (l.1260); Story 3.3 (l.1068)
- **Problem:** Facts that the ending and Epic 3-4 logic read (debt from `credit`, `experience_bought` from `phone`, `owns_moped`, licences) have no provider until a later epic exists. AD-16 says each fact has exactly one registered provider, but nothing says what the kernel returns when none is registered.
- **Fix:** Add an AC to Story 2.2 or 2.6, where `facts.py` is built: 'Each fact declared in `facts.py` carries a typed default used while no provider is registered; the merge fails at startup if two providers register the same fact; a test asserts the defaults (no debt, not bought, no moped).'
- **If shipped as-is:** Epics 3-6 crash on missing facts or each slice invents its own fallback, so the ending check and goal progress give different answers before and after the providing slice lands.

### Adversarial 6
- **Location:** epics.md Story 3.6 (l.1156, l.1166) vs Story 4.4 (l.1260, l.1273-1275)
- **Problem:** `money` computes `goal_measure` 'the same way as the check after month 60', while the ending in `year` separately reads debt and `experience_bought` to apply rule 13. The goal check is split across two slices with no single function, and FR-9a's 'family loans and payment plans included' is missing from 4.4.
- **Fix:** Put one rule 13 function in the kernel or in `money` that both progress (3.6) and the ending (4.4) call, with all inputs as facts. Spell out 'no debt at 20, including family loans and payment plans' in 4.4's AC, and test that progress at the end of month 60 equals the ending's verdict.
- **If shipped as-is:** The progress bar says the goal is reached while the ending says it isn't, or the reverse. A player with a remaining family loan gets the real win.

### Adversarial 7
- **Location:** epics.md Story 2.6 (l.901) vs FR-49 (l.55) and Story 4.4 (l.1270)
- **Problem:** In 2.6 the kernel sets `completed` after month 60 before any ending exists. FR-49 says a playthrough counts as completed only once its ending is calculated. From Epic 2 until 4.4 and 4.6, a finished life has no ending gate and no way to play again.
- **Fix:** In 2.6, make status `completed` depend on the after-month-60 slot having stored an ending, or add an interim 'ending pending' gate. Add an AC that `gateFor` shows a placeholder and the menu's «Nytt liv» until 4.4 and 4.6 land.
- **If shipped as-is:** Seeded runs, testers or reviewers who reach month 60 in an intermediate build hit a dead end, and `completed` differs from FR-49, which breaks the FR-50 'completed playthroughs' metric.

### Adversarial 8
- **Location:** epics.md Story 4.1 (l.1190-1199), Story 6.5 (l.1609-1611), Story 4.4 (l.1268-1271)
- **Problem:** Month 60 is a December. No story says whether the year end shows in month 60, or whether the year's tax and the BSU deduction ('paid when December is continued') are applied before or after the goal and loss checks.
- **Fix:** Add an AC to 4.4 giving the exact order for month 60's continue: tax and the December BSU step, then rule 8, then `close_month`, then the ending. Add one to 4.1 saying whether surface 23 shows in month 60 or is replaced by the ending, with a test for a goal measure that crosses the target only because of the BSU deduction or the tax.
- **If shipped as-is:** The goal verdict depends on implementation order, and a player exactly at the threshold gets a different ending from the one the worked examples predict.

### Adversarial 9
- **Location:** epics.md Story 6.5 (l.1603-1611) vs FR-12 rule 1 order (l.54) and FR-21 (l.92)
- **Problem:** 6.5 says tax is 'charged at its rule 1 step' each month and also that December 'carries the year's tax… paid when December is continued'. It is unclear whether tax is withheld monthly, paid once in December, or both.
- **Fix:** State the single model in 6.5's ACs, for example 'tax is computed on the calendar year's wages and charged once at December's tax step; no monthly withholding' (or the opposite), with an engine test for a July summer job plus December payment.
- **If shipped as-is:** Tax charged twice or never, WE 5 and WE 1 passing for the wrong reason, and month summaries contradicting the year end.

### Adversarial 10
- **Location:** epics.md Story 4.6 (l.1334-1336 vs l.1329-1331)
- **Problem:** An `ended` (ended-early) life has no calculated ending, yet 4.6 says that after a life 'has ended' the player sees 'the ending summary with «Spill på nytt»'. What an ended-early life shows is undefined.
- **Fix:** Split the AC: `completed` shows the ending summary; `ended` shows a start screen or a short 'Livet ble avsluttet' screen with «Spill på nytt» and no ending facts. Add a gate test for each status.
- **If shipped as-is:** The frontend renders an ending from missing data and crashes, or invents an ending for a life that was never finished.

### Adversarial 11
- **Location:** epics.md Story 6.1 Slice and Extension points (l.1483-1484); Shared table (l.384); Story 2.6 (l.879-901); Story 2.8 (l.951)
- **Problem:** `plan_version` is called kernel state, and AD-21 puts 'continue with `plan_version`' in the kernel, but no kernel story builds it: 2.6 never mentions it, 6.1's Slice line lacks `shared (…)`, and the shared table doesn't list 6.1.
- **Fix:** Either add `plan_version` and `409 plan_changed` to 2.6's ACs (a kernel field always present and bumped by any plan action), or change 6.1's Slice line to `shared (plan_version) + work` and add 6.1 to the shared table.
- **If shipped as-is:** The work slice writes kernel state against the AD-21 boundary, or the protocol field arrives late and changes the continue request after the frontend is built, breaking the `openapi.json` contract.

### Adversarial 12
- **Location:** epics.md Story 6.5 Touches (l.1595) vs the slice rule (l.370)
- **Problem:** 6.5 puts real behaviour in `money`: the December BSU step reads `tax_this_year`, and a full withdrawal claws back recorded deductions. That is logic, not a registration. 3.2 also defers the clawback to Epic 6 without owning it.
- **Fix:** Move the clawback AC and the 'December BSU reads `tax_this_year`' AC into a `money` story (3.2, with a fact default of 0 until 6.5), or rewrite the Touches rule to allow fact consumption in the touched slice and name who owns the test.
- **If shipped as-is:** Unclear ownership of the BSU clawback: both stories assume the other did it and it ships missing, or `work` edits `money`'s logic, against AD-21.

### Adversarial 13
- **Location:** epics.md Story 8.11 Slice `shared` (l.2111) and its seeded-run ACs (l.2124-2126)
- **Problem:** The content check plays full seeded runs under careless and careful policies, which needs every slice's registrations (jobs, card, moped). But it is placed in `shared`, which by AD-21 must never import a slice.
- **Fix:** Put the seeded-run part of 8.11 in a composition root (`cli.py`, or `backend/tests/` using `registry.build_kernel()`). Keep only the single-item schema function in `shared/content`, and update the Slice line and the shared table.
- **If shipped as-is:** The import-linter fails the PR, or someone weakens the boundary contract to let the check run, undermining AD-21.

### Adversarial 14
- **Location:** epics.md Story 8.11 (l.2126); FR-9b (l.47)
- **Problem:** The 'careless and careful policies' the seeded runs follow are never defined: which choices, transfers, spending level, job hours or activities each policy takes.
- **Fix:** Add an AC to 8.11 defining each policy as a deterministic decision function (for example careful: 'always the cheapest option, move all spare money to savings, spending Lite, take every summer job'), versioned with the content and reviewed against WE 20 and WE 21.
- **If shipped as-is:** The hard gates for goal reachability and hollow wins depend on an arbitrary bot. Tuning (#48) is done against an undocumented policy, and gate failures can't be reproduced.

### Adversarial 15
- **Location:** epics.md Story 2.9 (l.969-976) and Story 10.5 (l.2362-2365)
- **Problem:** Seeded users are fixed scripted action lists replayed with a fixed seed against the newest unfrozen library. Every content PR that adds an event changes the uniform draw, so the scripted choices hit different events and the assertions break.
- **Fix:** Pin the seeds to `config/test-v1` and a fixed test library that content PRs don't touch, or make the scripts choose by policy ('first free option') instead of by option id. Add an AC that content-only PRs never need seed edits.
- **If shipped as-is:** CI goes red on every content PR in Epic 8, authors re-record seeds by hand, and the examiner's seeded states drift from what the README describes.

### Adversarial 16
- **Location:** epics.md Story 1.4 last AC (l.584) and Story 10.4 (l.2340-2342)
- **Problem:** The entry-check redirect behaviour is deferred to a manual check in Epic 10 'since there is no app to run the test against', although Story 1.2 already runs Playwright against the compose stack. This contradicts NFR-9 (automated) and AD-20.
- **Fix:** Replace the deferral with an AC in 1.4 for a Playwright test of `/`, `/logg-inn` and `/ny-bruker` when logged in and when the session has expired (no redirect loop), on the compose stack, and drop the manual duplicate from 10.4.
- **If shipped as-is:** A redirect loop or a bypassed login screen goes unnoticed for nine epics and is found only at the playtest gate, when fixing it costs the most.

### Adversarial 17
- **Location:** epics.md Story 1.6 Tier (l.621) vs Tier table (l.390)
- **Problem:** The story is listed as Extension in the tier table but contains the Core nickname change (FR-1). Cutting the Extension story removes a Core requirement.
- **Fix:** Split 1.6 into '1.6a Change nickname (Core)' and '1.6b Change password (Extension)', or list 1.6 under Core and mark only the password part as cuttable.
- **If shipped as-is:** A scope cut removes nickname editing, breaking FR-1's 'can be changed in settings' and UX-DR33's menu.

### Adversarial 18
- **Location:** epics.md Story 2.5 (l.855-857) vs Story 3.4 (l.1114-1117)
- **Problem:** 2.5 defines affordability as current account only and adds a refusal test for it, yet 2.3 already lets the pengegave go to savings. Until 3.4 a saver can't afford events, and 3.4 must invert 2.5's test.
- **Fix:** In 2.5, state the final FR-45 rule now ('payable from current account + savings'), with the automatic transfer added in 3.4, or mark the 2.5 test explicitly as interim with the 3.4 change named.
- **If shipped as-is:** Intermediate builds lock players out of free-looking options after they save, and a shipped refusal test encodes behaviour that contradicts FR-45.

### Adversarial 19
- **Location:** epics.md Story 7.5 (l.1792) vs FR-49 (l.55); Stories 3.3, 6.3, 6.6, 3.2
- **Problem:** The month-60 rule ('next-month actions and previews hidden or marked as no effect') appears only in the credit story 7.5. The slices that own next-month actions (spending level 3.3, quit or take a job 6.3, hours requests and extra shifts 6.6, a December BSU deposit) never state it.
- **Fix:** Add a kernel AC in 2.6: 'the view marks every action whose effect starts next month as `no_effect_in_month_60`'. Add a line to each of 3.3, 6.3 and 6.6 requiring their actions to declare that property, with a test per action.
- **If shipped as-is:** In month 60 players change spending, ask for hours or take jobs that silently do nothing, and the FR-49 promise holds only for credit actions.

### Adversarial 20
- **Location:** epics.md Story 1.8 (l.680-682) vs Story 1.3 (l.539-541)
- **Problem:** The order between the tester-list guard and the `409 email_in_use` check is unspecified. A non-tester gets a different refusal from a tester whose address is taken, which reveals tester-list membership. 1.3 claims `email_in_use` is the only revealing response.
- **Fix:** Add an AC to 1.8: 'the sign-up guard runs before the email-in-use check; a non-listed address gets the same response whether or not a user exists', plus a test.
- **If shipped as-is:** Someone can probe whether an address belongs to an invited 18-20-year-old tester, leaking personal data from the playtest list (NFR-3).

### Adversarial 21
- **Location:** epics.md Story 10.6 (l.2383-2385)
- **Problem:** Clean-up deletes Railway and Vercel but not the Supabase project, which holds all player data. It also doesn't cover the email-to-code list, the exports on team members' machines (10.2), or disabling the daily GitHub Actions check and its Railway token.
- **Fix:** Extend the AC: delete the Supabase project, delete the email-code list and every local export, disable `daily-check.yml` and revoke its secrets, and record the deletion date in the repo.
- **If shipped as-is:** Personal data outlives the project, against NFR-3, and the daily check keeps failing and alerting, or keeps a database alive, after delivery.

### Adversarial 22
- **Location:** epics.md Story 10.3 (l.2315-2316) with #126 (l.216)
- **Problem:** `cli clear-game-data` runs once at the freeze. If #126 lets the playtest start unfrozen, that command wipes running testers' lives and possibly their records mid-test. Its scope (records? accounts?) is unstated.
- **Fix:** Add an AC defining exactly what `clear-game-data` deletes (playthroughs and action_log only, never users, records or tester_codes), and forbid it once any tester account exists, or require the freeze before the first tester invite.
- **If shipped as-is:** Tester data is lost mid-playtest and the SM metrics are corrupted, or the command deletes records that FR-50 requires to survive.

### Adversarial 23
- **Location:** epics.md Story 10.1 (l.2266) vs Epic 10 Notes (l.442) and readiness #82/#69/#108 (l.219)
- **Problem:** 10.1 hard-codes metric definitions such as 'time to first real choice (from sign-up)' and 'session lengths (… within an in-game year)' that the notes say must wait for the open metric-definition issues, including the SM-10 vs FR-11 start point.
- **Fix:** Mark the contested fields 'Blocked by #82/#108' and fill them from the decision, or move the definitions into config so a late decision doesn't change the record schema.
- **If shipped as-is:** The records collect the wrong measure, and since records are never rebuilt from `action_log`, the playtest's success metrics can't be recovered after the test.

### Adversarial 24
- **Location:** epics.md Consistency conventions, Performance (l.193); Story 10.4 (l.2344-2347)
- **Problem:** The convention requires 'a CI regression bound with headroom' for month process and save time, but no story builds it. Performance is checked only by hand right before the playtest.
- **Fix:** Add an AC to 2.6 (or 8.11): 'CI times month process + save over a seeded run and fails above <bound> ms p90', with the bound in config.
- **If shipped as-is:** Performance regressions pile up unnoticed through Epics 3-9 and surface only at the pre-playtest measurement, with no time left to fix them.

### Adversarial 25
- **Location:** epics.md UX-DR40 (l.276) vs Stories 6.1, 6.3 and 6.6
- **Problem:** The bare coral dot on Plan (free evenings left) and Jobb (unanswered offer), with the screen-reader text «, noe nytt», is in no story's ACs. Only the Mobil badge is covered (5.1).
- **Fix:** Add an AC to 6.1 (Plan dot when free evenings are left) and 6.6 (Jobb dot while an hours or extra-shift offer is unanswered), each with the «, noe nytt» text and an axe and keyboard check.
- **If shipped as-is:** The 'something new' cues are never built, offers lapse unseen, and the UX coverage claim is false.

### Adversarial 26
- **Location:** epics.md Story 3.1 (l.1029) with UX-DR44 (l.286); Story 1.5 (l.617) with UX-DR45 (l.287)
- **Problem:** Core stories in Epics 1 and 3 require UX patterns the document itself marks as undecided (#125): the amount-entry visual pattern, and how the frontend knows email is off in the playtest. The ACs aren't testable as written ('by the mechanism #125 decides').
- **Fix:** Add 'Blocked by #125' to 1.5 and 3.1, or decide inline: for example the view carries `email_enabled: bool`, and amount entry is a labelled input plus stepper with an error state per NFR-7 code. Then write concrete ACs.
- **If shipped as-is:** The first money-action story invents a pattern every later money action copies, and the playtest reset copy ships wrong or missing.

### Adversarial 27
- **Location:** epics.md Story 7.1 Tier (l.1671) vs its AC (l.1685) and FR-19 (l.67)
- **Problem:** The tier line says the card offer's tip is Extension, but the AC unconditionally requires 'the offer message carries a tip', and FR-19 says card and loan offers 'always carry a tip'. It is unclear whether cutting FR-19 removes it.
- **Fix:** Make the tier line and the AC agree, either 'tip is Core for card and loan offers' or 'tip only if FR-19 is built', and align the FR-19 row in the coverage map.
- **If shipped as-is:** Reviewers block or pass the story inconsistently, and a tier cut silently drops a teaching point the PRD treats as mandatory.

### Adversarial 28
- **Location:** epics.md Requirements Inventory FR-18 (l.65), FR-48 (l.66) vs Story 5.3 (l.1411), Story 5.4 (l.1450)
- **Problem:** The inventory, which claims to be the planning summary, leaves out that the experience is only for goal-3 players. The stories add the restriction and cite FR-18 and FR-48 as the source, so summary and stories disagree.
- **Fix:** Add 'for goal-3 players' to the FR-18 and FR-48 inventory lines (PRD l.739, l.753).
- **If shipped as-is:** Readers who rely on the inventory, such as test authors or the content check's open-option gate, treat the goal-3 refusal as an invented rule or omit it.

### Adversarial 29
- **Location:** epics.md Stories 8.6-8.10 (l.1989-2101) and Story 7.7 (l.1837)
- **Problem:** No per-year story owns writing boomerang pairs (≥ 8), follow-ups (≥ 3 per seeded run), crisis events (about 10, buried in an engineering story in the `credit` slice) or offer messages for every FR-18 row. The minimums appear only as an aggregate check in 8.10.
- **Fix:** Give each per-year content story a share of the boomerang pairs and the crisis and offer content (for example '≥ 2 boomerang openers whose follow-ups land within the playthrough'), and move crisis-event authoring from 7.7 into a content story with its own reviewer.
- **If shipped as-is:** The aggregate gate fails late in Epic 8 with no story accountable, and crisis texts written by engineers skip the NFR-8 tone review.

### Adversarial 30
- **Location:** epics.md Story 4.6 (l.1327) and Story 10.1 (l.2269-2271)
- **Problem:** The finished playthrough is deleted 'in the same transaction' as the start. 10.1 says the record is updated before the deletion, but 4.6 has no hook ordering for that, and AD-5's `action_log` rows are deleted with it. A failure between the update and the delete is not addressed.
- **Fix:** In 4.6, state the order inside the start transaction (on-action hooks with the old state, then delete the old playthrough, then create the new one) and add a test that a failure rolls back all three.
- **If shipped as-is:** The 'playing again' and 'completed' metrics are lost or double-counted, or a crash leaves an account with two playthroughs, breaking the one-life invariant.


## Edge-case hunter (58)
### Edge case 1
- **Location:** epics.md Story 1.1, lines 465-468
- **Problem:** APP_ENV set to an unknown value, or a short/placeholder secret in playtest
- **Fix:** APP_ENV: Literal['local','ci','playtest']; if env not in (local,ci) and (len(secret)<32 or secret==PLACEHOLDER): refuse start
- **If shipped as-is:** Backend starts with an unknown mode or weak secrets; only Caddy checks this, in 1.9

### Edge case 2
- **Location:** epics.md Story 1.3, lines 543-547
- **Problem:** Nickname over 16 characters or password over 128 characters submitted
- **Fix:** fields: too_short | too_long | invalid_chars | invalid_email; password 8-128 per AD-10
- **If shipped as-is:** No error code exists for over-length input; the 422 list is incomplete

### Edge case 3
- **Location:** epics.md Story 1.3, lines 533-541
- **Problem:** Sign-up confirm submitted twice (double tap or retry) for the same new address
- **Fix:** lock the confirm button single-flight; on a unique violation by the same caller within N s, return the first session and do not send 409
- **If shipped as-is:** The second submit gets 409 email_in_use, and the new user is told the address is taken

### Edge case 4
- **Location:** epics.md Story 1.3, line 535 (FR-1 nickname function)
- **Problem:** Nickname typed with decomposed æ/ø/å (NFD) or combining marks
- **Fix:** nick = unicodedata.normalize('NFC', raw).strip(); count len after NFC
- **If shipped as-is:** A valid Norwegian nickname is rejected as invalid_chars or counted too long

### Edge case 5
- **Location:** epics.md Story 1.4, lines 565-568
- **Problem:** Correct password entered after fewer than 10 failures in the window
- **Fix:** on successful login: clear failure count for (address, network)
- **If shipped as-is:** Earlier failures still count after a success, so the address is paused sooner than intended

### Edge case 6
- **Location:** epics.md Story 1.4, lines 575-578
- **Problem:** «Logg ut på alle enheter» deletes the current device's session row too
- **Fix:** after 2xx: reset(); route to /logg-inn (or keep current session and state that explicitly)
- **If shipped as-is:** Where the current device lands is unspecified (#123 lists it as open)

### Edge case 7
- **Location:** epics.md Story 1.5, lines 608-612
- **Problem:** /nytt-passord opened with no token fragment, or the new password is too short or too long
- **Fix:** if !token: show invalid-link state; validate new password with FR-1 length -> 422 invalid_input
- **If shipped as-is:** Missing token and invalid new password have no defined state or code

### Edge case 8
- **Location:** epics.md Story 1.5, lines 608-612; Story 1.6, lines 631-634
- **Problem:** Reset link still outstanding when the password is changed or log-out-everywhere is used
- **Fix:** on password change / logout-all: DELETE reset_links WHERE user_id=…
- **If shipped as-is:** An old reset link still works after the player secured the account

### Edge case 9
- **Location:** epics.md Story 1.5, lines 610-611 (and Story 1.3 sign-up)
- **Problem:** Browser logged in as player A completes a reset or sign-up as player B
- **Fix:** on reset/sign-up success: store.reset() before the first GET /api/game
- **If shipped as-is:** Player A's envelope or late responses can show in B's session (AD-18 calls reset() only on logout/401)

### Edge case 10
- **Location:** epics.md Story 1.6, lines 636-639
- **Problem:** Nickname change submitted with invalid characters or wrong length
- **Fix:** 422 invalid_input with fields.nickname too_short|too_long|invalid_chars, shown in the sheet
- **If shipped as-is:** The refusal path for an invalid nickname is not specified or tested

### Edge case 11
- **Location:** epics.md Story 1.6, line 634; Story 1.7, line 657
- **Problem:** Repeated wrong current password on change-password or delete-user
- **Fix:** count wrong_password in auth_attempts per user; pause after N within window
- **If shipped as-is:** Someone with a hijacked session can guess the password without limit

### Edge case 12
- **Location:** epics.md Story 1.8, lines 676-682
- **Problem:** Tester list loaded twice, has duplicates, or a sign-up is refused by the guard
- **Fix:** upsert by normalized email; guard refusal -> 403 sign_up_closed with an NFR-7 test
- **If shipped as-is:** Duplicate or failed reloads; the guard refusal has no code or status

### Edge case 13
- **Location:** epics.md Story 2.1, lines 734-746
- **Problem:** Running playthrough is pinned to an unfrozen library and an item it stored is renamed or removed
- **Fix:** on load: if stored content id missing in pinned version -> fallback/refuse with known error, tested
- **If shipped as-is:** Loading the state crashes or shows a missing event during pre-freeze play

### Edge case 14
- **Location:** epics.md Story 2.2, lines 773-775 vs Story 4.6, lines 1324-1332
- **Problem:** Start sent while a completed or ended playthrough exists
- **Fix:** refuse only if status=='active'; completed/ended -> delete and create in one transaction
- **If shipped as-is:** 2.2 refuses any existing playthrough, which blocks Play again in 4.6

### Edge case 15
- **Location:** epics.md Story 2.2, lines 782-784
- **Problem:** Same request_id reused with a different action body
- **Fix:** if logged.request_id==rid and hash(action)!=logged.hash: 422 request_id_reused
- **If shipped as-is:** A different action silently returns the first action's result as a replay

### Edge case 16
- **Location:** epics.md Story 4.4, lines 1281-1283; Story 2.4, lines 816-831
- **Problem:** Avatar step cut (Extension) or never picked, then the scene or ending renders 'chosen look'
- **Fix:** look = state.look ?? 'look-1' default in the view
- **If shipped as-is:** Scene and ending have no defined look colours

### Edge case 17
- **Location:** epics.md Story 2.5, lines 859-862 (Extension points line 842)
- **Problem:** Option effect whose kind has no registered handler yet, or conflicts with state
- **Fix:** if kind not in kernel.effect_handlers or handler.precheck(state) fails: content-check error / refuse option
- **If shipped as-is:** Starter events referencing later slices crash or apply nonsense effects

### Edge case 18
- **Location:** epics.md Story 2.8, lines 939-951
- **Problem:** Own action applied, response lost, then tab return or idle GET sees changed state_version
- **Fix:** if pending.request_id in envelope.last_request_ids: show its result, not other-device notice
- **If shipped as-is:** Player's own saved choice is shown as 'updated on another device' and its result is lost

### Edge case 19
- **Location:** epics.md Story 3.2, lines 1049-1052
- **Problem:** BSU deposit larger than the current account, or from a negative account
- **Fix:** if amount > current_account or current_account<=0: refuse NFR-7 (cap cut applied after)
- **If shipped as-is:** BSU deposit can overdraw the current account; only the cap and closed cases are specified

### Edge case 20
- **Location:** epics.md Story 3.2, lines 1058-1061; Story 6.5, lines 1609-1612
- **Problem:** BSU fully withdrawn in the same calendar year, before December's deduction
- **Fix:** december_bsu: if bsu_closed_this_year: deduction=0 (and claw back), tested
- **If shipped as-is:** A deduction is paid for a closed BSU, or the clawback is skipped (#123)

### Edge case 21
- **Location:** epics.md Story 3.4, lines 1114-1122
- **Problem:** Current account negative with money in savings when an option is priced
- **Fix:** payable = max(current,0)+savings >= price ? and negative paid first : refuse
- **If shipped as-is:** Undefined affordability; a negative balance may pay for a choice through savings

### Edge case 22
- **Location:** epics.md Story 3.4, lines 1119-1121
- **Problem:** Fixed cost exceeds the current account while savings hold enough
- **Fix:** payment-order table row: fixed cost -> current, then savings cover?, then negative
- **If shipped as-is:** Unclear whether savings cover always-charged items or the account goes negative and triggers a crisis

### Edge case 23
- **Location:** epics.md Story 3.5, lines 1141-1149
- **Problem:** No expense kind fits the state, or the owned item is sold between the draw and the expense month
- **Fix:** at expense month: re-check kind eligibility; if none fits -> redraw generic or skip, stored
- **If shipped as-is:** Repair charged for a moped already sold, or the draw fails with no kind

### Edge case 24
- **Location:** epics.md Story 3.5, lines 1141-1148
- **Problem:** Unexpected expense drawn for month 1, before setup_gift completes
- **Fix:** exclude month 1 from the expense-month draw, or order it after the pengegave
- **If shipped as-is:** Expense deducted before the gift lands; month-1 setup order unspecified (#123)

### Edge case 25
- **Location:** epics.md Story 3.6, lines 1164-1171; Story 9.5, line 2237
- **Problem:** Available money negative, or above the target
- **Fix:** progress = clamp(measure/target, 0, 1)
- **If shipped as-is:** Negative progress shown for goal and savings target (only 9.5 caps at 100 %)

### Edge case 26
- **Location:** epics.md Story 3.6, lines 1164-1167
- **Problem:** Goal 3 progress before the month-44 offer, or after month 56 unbought
- **Fix:** goal3_progress: before 44 -> saved/price; after 56 unbought -> 'not reachable' state
- **If shipped as-is:** The experience goal's progress has no defined meaning for most of the game

### Edge case 27
- **Location:** epics.md Story 4.4, lines 1268-1279
- **Problem:** Trigger true at end of 59, month-60 crisis skipped at open, trigger true again at end of 60
- **Fix:** loss requires a crisis not skipped in 60, or the rule states explicitly that it is a loss, with a test
- **If shipped as-is:** A skipped crisis in month 60 gives an undefined loss outcome (#123)

### Edge case 28
- **Location:** epics.md Story 4.4, line 1260
- **Problem:** Ending reads experience_bought or debt before phone/credit register providers
- **Fix:** facts.declare(name, type, default=False/0) used when no provider is registered
- **If shipped as-is:** Ending check fails on a missing fact in Epics 4-6 played states

### Edge case 29
- **Location:** epics.md Story 4.5, lines 1307-1310
- **Problem:** Chosen option beat the alternative, or the choice was an open option with no sibling options
- **Fix:** sign = cmp(chosen, alt) -> 'mer'/'mindre'; open option -> fixed text line
- **If shipped as-is:** FR-39 line has the wrong direction or no comparison for top-3 open options

### Edge case 30
- **Location:** epics.md Story 4.6, lines 1334-1336
- **Problem:** Life ended early (status ended), player logs in again
- **Fix:** if status=='ended': show ended screen with Spill på nytt, no ending summary
- **If shipped as-is:** The AC asks for an ending summary that is never calculated for ended lives

### Edge case 31
- **Location:** epics.md Story 4.6, lines 1329-1332
- **Problem:** End early during setup (setup_gift) after seeing a low pengegave
- **Fix:** refuse end-early while pending in (setup_avatar, setup_gift), or keep the drawn gift
- **If shipped as-is:** Player re-rolls the pengegave by ending early and starting again

### Edge case 32
- **Location:** epics.md Story 5.1, lines 1365-1367
- **Problem:** Month opens with several new messages
- **Fix:** toast shows the first by fill order plus '+n til'
- **If shipped as-is:** Which message the single toast shows is undefined

### Edge case 33
- **Location:** epics.md Story 5.2, lines 1387-1393
- **Problem:** Savings jump past several thresholds in one month, or a deferred bank message meets next month's
- **Fix:** mark all passed thresholds done; deliver only the highest; drop deferred if superseded
- **If shipped as-is:** Lower thresholds arrive later out of order, or two bank messages arrive in one month

### Edge case 34
- **Location:** epics.md Story 5.5, lines 1465-1468
- **Problem:** Follow-up due, but its age range or blocking flags fail in the due month
- **Fix:** at due month: if !eligible(followup): push or drop and report
- **If shipped as-is:** An ineligible follow-up is either shown wrongly or dropped silently

### Edge case 35
- **Location:** epics.md Story 6.1, lines 1501-1503
- **Problem:** «Samme kvelder» with fewer evenings this month or some activities ineligible
- **Fix:** place in slot order until slots are full; report which were not placed
- **If shipped as-is:** Undefined which activities are dropped (#123)

### Edge case 36
- **Location:** epics.md Story 6.1, line 1503
- **Problem:** Each activity affordable alone but not with the others already planned
- **Fix:** affordable(price + planned_total) when placing
- **If shipped as-is:** Plan shows affordable, and activities then drop at continue

### Edge case 37
- **Location:** epics.md Story 6.1, lines 1498-1504
- **Problem:** Place or remove sent from two devices on the same plan
- **Fix:** place/remove carry plan_version or item id; mismatch -> 409 plan_changed
- **If shipped as-is:** A remove deletes the wrong evening after a concurrent change (#123)

### Edge case 38
- **Location:** epics.md Story 6.2, lines 1520-1522
- **Problem:** Planned activity dropped at month 60's continue
- **Fix:** show dropped notes on the ending summary or before continue in month 60
- **If shipped as-is:** «Ble ikke noe av» has no next month to appear in

### Edge case 39
- **Location:** epics.md Story 6.3, lines 1548-1551
- **Problem:** Quit with placed one-off shifts, a pending hours request or an open hours offer
- **Fix:** on quit: remove placed shifts, cancel request and offer, with notes
- **If shipped as-is:** Shifts are paid or a request is answered for a job the player no longer has (#123)

### Edge case 40
- **Location:** epics.md Story 6.3, lines 1548-1550
- **Problem:** Full-time offer in month 54 to a player with a part-time job
- **Fix:** taking full-time replaces part-time from next month, or refuse with 'quit first'
- **If shipped as-is:** One-job rule blocks the full-time offer, or both jobs run

### Edge case 41
- **Location:** epics.md Story 6.6, lines 1627-1630
- **Problem:** ±2 h step crosses the limit or floor (11 h at a 12 h limit; 39.5 to 41.5)
- **Fix:** offer = clamp(hours±2, floor, limit); 'no' only if offer==hours
- **If shipped as-is:** Undefined: offer above the limit or an unjustified 'no' (#123)

### Edge case 42
- **Location:** epics.md Story 6.7, lines 1660-1663
- **Problem:** One-off shift worked in December; shift hours vs free time
- **Fix:** December shift: taxed in the next tax year (state it); shift hours excluded from rule 12 free time
- **If shipped as-is:** Tax year and free-time effect of shifts are unspecified (#123, WE 29)

### Edge case 43
- **Location:** epics.md Story 7.1, lines 1682-1685 (also 7.3 line 1736)
- **Problem:** Steady wage only from summer job or one-off shifts, or wage started last month
- **Fix:** steady_monthly_wage := part/full-time job paid in each of last N months (config)
- **If shipped as-is:** Card and loan eligibility differ between implementations (#123 steady-wage window)

### Edge case 44
- **Location:** epics.md Story 7.1, lines 1684-1695
- **Problem:** Fixed payment falls below a later minimum, or extra payment exceeds the balance or the accounts
- **Fix:** pay max(fixed, minimum); extra: max=min(balance, current+savings) else refuse
- **If shipped as-is:** Fixed mode silently misses the minimum; overpayment creates a credit balance (#123)

### Edge case 45
- **Location:** epics.md Story 7.2, lines 1710-1713
- **Problem:** Card-payable monthly cost does not fit under the card limit
- **Fix:** pay() row: card-payable cost not fitting -> accounts per FR-45 order, noted
- **If shipped as-is:** Only event purchases have a defined fallback

### Edge case 46
- **Location:** epics.md Story 7.3, lines 1736-1744
- **Problem:** 3x average wage minus debt below NOK 5,000 (no loan possible), or quote for out-of-range amount
- **Fix:** if max<5000: loan sheet locked with reason; quote out of range -> 422 with min/max
- **If shipped as-is:** Sheet shows an invalid range; quote endpoint behaviour undefined (#123)

### Edge case 47
- **Location:** epics.md Story 7.3, line 1744; Story 7.8, line 1866
- **Problem:** Early payoff of a loan or payment plan with less money than the remaining amount
- **Fix:** if remaining > current+savings: refuse NFR-7 (as in 7.4)
- **If shipped as-is:** Payoff overdraws or partially pays; only family-loan payoff is specified

### Edge case 48
- **Location:** epics.md Story 7.3, lines 1741-1743
- **Problem:** Loan taken mid-month M
- **Fix:** first instalment in M+1 (FR-12), stated and tested
- **If shipped as-is:** First instalment month is unspecified (#123)

### Edge case 49
- **Location:** epics.md Story 7.4, lines 1764-1767
- **Problem:** Accounts can cover only part of a family-loan instalment
- **Fix:** pay the covered part, move the rest to the end; or move the whole instalment, stated
- **If shipped as-is:** Partial coverage is undefined (#123)

### Edge case 50
- **Location:** epics.md Story 7.4, lines 1759-1762
- **Problem:** Player asks family in a regular event and family can't help
- **Fix:** asking is not the real choice; the event stays open for another option
- **If shipped as-is:** The real choice is used up with nothing, or the player can't continue

### Edge case 51
- **Location:** epics.md Story 7.5, lines 1787-1791
- **Problem:** Trigger true during cooldown, and the band text is chosen
- **Fix:** in cooldown: band says the trigger is true but there is no crisis next month
- **If shipped as-is:** «Krise i <måned>» is shown when no crisis will come (#123)

### Edge case 52
- **Location:** epics.md Story 7.5, lines 1794-1796
- **Problem:** Skipped crisis month is a non-active (quiet) month
- **Fix:** re-choose only if the month is in active_months, else quiet
- **If shipped as-is:** Quiet month gets a drawn event after the skip

### Edge case 53
- **Location:** epics.md Story 7.7, lines 1835-1837
- **Problem:** No crisis event fits the urgent trigger and age at runtime
- **Fix:** fallback: next-urgent trigger's events, else generic crisis event; content check reports it
- **If shipped as-is:** Crisis month opens with no event, and continue may stay blocked

### Edge case 54
- **Location:** epics.md Story 8.3, line 1930
- **Problem:** Moped sold and a second moped bought later
- **Fix:** parents_share drawn per moped with draw key including the moped seq, or once per playthrough, stated
- **If shipped as-is:** Ambiguous redraw lets the player buy again to get a better share

### Edge case 55
- **Location:** epics.md Story 8.5, lines 1984-1986
- **Problem:** Player owns a moped and borrows the car in the same month
- **Fix:** transport row: moped and car fuel both charged / car borrow refused while owning a moped
- **If shipped as-is:** How transport costs combine is undefined

### Edge case 56
- **Location:** epics.md Story 9.3, lines 2194-2197
- **Problem:** «Skjønner» call fails or the device is offline
- **Fix:** on failure: keep note visible, show error, allow retry; never mark seen locally
- **If shipped as-is:** Failure path is unspecified; the note may vanish locally but return elsewhere

### Edge case 57
- **Location:** epics.md Story 9.5, lines 2234-2236
- **Problem:** Goal 1/2 player pins the experience, which never opens for them
- **Fix:** pinnable = options that can open for this playthrough
- **If shipped as-is:** Target shows 'opens in month 44' but never opens

### Edge case 58
- **Location:** epics.md Story 10.1, lines 2273-2276
- **Problem:** Tester deletes the account and signs up again with the same address
- **Fix:** testers_left counts distinct codes; on re-sign-up of a counted code, decrement or flag
- **If shipped as-is:** A returning tester is counted as having left (#123)


## Editorial structure (16)

Structure model: Reference/Database (readers jump to one story; each follows a fixed schema). The front matter is judged as Strategic/Context. Word count: 36,719 in total; Requirements Inventory 14,659 (40%), Epic List 1,898, stories 19,386. If all changes are accepted the document shrinks by about 8,350 words (about 23%). No length target was given.

Trade-offs: rows 1 and 2 make readers open the PRD and the architecture spine for detail; row 7 means the shared ACs for 8.6-8.10 must be copied back when story files are generated. Nothing that serves engagement (summaries, examples, orientation paragraphs) is removed.

| # | Location | Original | Recommendation | Why |
|---|---|---|---|---|
| 1 | epics.md §Requirements Inventory → Functional Requirements (5,831 words) + §FR Coverage Map (589 words) | Full FR inventory plus a separate coverage map | MERGE + CONDENSE: one FR table (ID, title, tier, epic, stories). The full rules stay in the PRD's 'Consequences (testable)' lists and in the story ACs. | The Overview says each line is 'a summary for planning', but many are not summaries: FR-45, FR-47 and FR-48 run about 150-250 words each. Every FR then appears a third time in the story ACs, and the coverage map repeats the titles. Saves about 5,400 words. Trade-off: readers must open the PRD to read an FR's rules. |
| 2 | epics.md §Additional Requirements → Architecture decisions AD-1 to AD-21 (2,693 words) | AD-1 to AD-21 restated almost in full | CONDENSE: one line per AD (ID, name, short summary, the stories that implement it), plus one pointer to ARCHITECTURE-SPINE.md | Repeats an input document almost in full, and the stories repeat the testable parts again. The AD-21 boundary checks appear in AD-21 (l.180), the 'Rule for every story: code goes in its slice' (l.370), the Epic 1 Notes (l.397) and the ACs of 1.1 and 1.2. Saves about 2,150 words. Trade-off: less complete on its own. |
| 3 | epics.md §Readiness review 2026-11-23: findings still open that shape stories (661 words, including a 272-word bullet for #123) | Status list of open readiness findings | MOVE to the readiness report and the GitHub issues. Leave one line: 'Open findings that block stories are named in each epic's Notes.' | Status tracking that goes stale (#122 'closes when this branch is merged'; 'Fixed since the review…' is change history). The epic Notes already name the blockers. The #123 bullet is a wall of text. Saves about 620 words. |
| 4 | epics.md §Epic List: the three 'Rule for every story' paragraphs (463 words) plus the Slice and Tier tables (l.356, after the inventory) | Rules for every story placed after ~15,000 words of inventory, under 'Epic List' | MOVE: own H2 'Rules for every story' directly after the Overview; Epic List next; Requirements Inventory (with 'How to read the inventory') at the end as the ID lookup. | Rules every story must follow (refusals, no links to unbuilt pages, slice boundaries) are buried under a heading that doesn't signal them. Someone implementing a story needs them first. Word impact: 0. |
| 5 | epics.md Overview, first paragraph | This document provides the complete epic and story breakdown … UX Design if it exists … | CONDENSE: 'Ten epics and 73 stories, built in order 1 → 10. Read Rules for every story first, then your epic. The Requirements Inventory at the end is the lookup for FR, NFR, AD and UX-DR IDs.' | Template boilerplate ('if it exists') in the most visible spot. The replacement says what the document holds and how to navigate it. About +10 words. |
| 6 | epics.md missing scaffolding: no story index; the Tier table and the Slice table's `shared` row are partial indexes | No story index for 73 stories | MERGE into one story index table (Story, Title, Tier, Slice) in the Epic List | In a 36,700-word document the only way to find a story or check its tier or slice is to scroll. One index replaces two partial lists. Net about +300 words. |
| 7 | epics.md Stories 8.6-8.10 (961 words) | Tip AC and tone/NFR-8 AC identical in all five stories; free-option/LK20 AC nearly identical | CONDENSE: state the shared ACs once under an 'Applies to 8.6-8.10' block in Epic 8 or 8.6; each story keeps its own year, months, age and minimums. | Five near-copies hide the one thing that differs: the year. Saves about 360 words. Trade-off: shared ACs must be copied back when each story file is generated. |
| 8 | epics.md Story 8.10, last two Given/When/Then blocks (library totals; zero AI calls, F6) | Library-wide ACs inside the year-5 story | MOVE to Story 8.11 or a closing note for Epic 8 | These ACs cover the whole library, not year 5. Word impact: 0. |
| 9 | epics.md **Extension points** lines in Stories 3.3, 6.2, 7.1, 7.3, 7.4, 8.5 | Items that aren't extension points (e.g. 'calls `wellbeing.add()` (a kernel call, not an extension point)') | MOVE those items to a Notes line or into the ACs | The line itself says some items aren't extension points, which breaks the scannable story layout (Tier → Slice → Extension points → Touches). Word impact: 0. |
| 10 | epics.md Epic 2 Notes: list of kernel parts per story | the pipeline, envelope, the start action … (2.2); the ledger, draws, scene and timeline (2.3); … wellbeing (2.7) | CUT the list; keep '2.2, 2.3, 2.5, 2.6 and 2.7 build their kernel parts in `shared/`, named on their Slice lines.' | Repeats each story's Slice line and the Slice table's `shared` row. Saves about 70 words. |
| 11 | epics.md Epic 9 Notes | Story 9.1 … and Story 9.4 … are Core, are always built and are never cut. 9.2 and 9.3 are Extension and 9.5 is Can be cut… | CUT | Repeats the Tier table and the Tier lines on 9.1-9.5. Saves about 45 words. |
| 12 | epics.md Epic 10 Notes | NFR-11's environment and daily check are set up in Story 1.9. | CUT | Already said in the Epic 10 description, the FR Coverage Map's closing line (l.354) and the Epic 1 Notes. Saves about 12 words. |
| 13 | epics.md Story 10.4 AC 'Given the first version of the app is built … opens `/hjem` … (Story 1.4)' | Login-redirect check filed under 'Check devices, accessibility and speed by hand' | QUESTION: retitle 10.4 to cover checks moved there from earlier stories, or keep this check under Story 1.4 and mark it deferred | A reader looking for where Story 1.4's redirect is verified won't look here. Word impact: 0. |
| 14 | epics.md '## Epic N' intro paragraphs (repeat the Epic List entries, ~357 words) | Epic goal paragraph repeated under each epic | PRESERVE | Readers often jump straight to an epic; the one-paragraph goal orients them without scrolling back. |
| 15 | epics.md story ACs that restate inventory detail (e.g. 5.1 toast / UX-DR18; 7.3 loan figures / FR-25; 4.4 goal targets / FR-9a) | Inventory detail restated in ACs | PRESERVE | Each story must stand alone when lifted into a dev session, and the ACs are the testable form. This is why rows 1 and 2 shorten the inventory instead of the stories. |
| 16 | epics.md §UX Design Requirements (3,572 words) and §NonFunctional Requirements (992 words) | Full UX-DR and NFR lists | PRESERVE | UX-DR numbers are defined only here (DESIGN.md and EXPERIENCE.md have no UX-DR IDs), and NFRs apply across the product with no single story to live in. |

## Editorial prose (35)

Style to preserve: terse, semicolon-heavy summary style; IDs in brackets (FR-, AD-, UX-DR, #issue); Norwegian UI strings in «»; Norwegian loanwords on purpose (pengegave, trivselsmål, kroner); Given/When/Then/And; first-person story voice. Text that the structure lens proposes to cut or rewrite was not copy-edited. These rows are close to word-neutral.

| # | Location | Original | Revised | Why |
|---|---|---|---|---|
| 1 | epics.md Story 10.4 (l.2346) | the first visit is usable within 3 s, and a loading message shows within 1 s and the game is usable within 10 s (NFR-10) | the first visit is usable within 3 s, and when the server was asleep, a loading message shows within 1 s and the game is usable within 10 s (NFR-10) | Restored the missing condition from NFR-10; without it the 10 s clause seems to contradict 'usable within 3 s'. |
| 2 | epics.md Epic List → Epic 10 (l.440) and Epic 10 intro (l.2249) | Sign-up limited to testers, the playtest environment and the daily check are in Epic 1. | Epic 1 covers the tester-only sign-up, the playtest environment and the daily check. | Garden path: first reads as 'sign-up limited to [testers, the environment and the check]'. Same fix in both places. |
| 3 | epics.md Story 1.1 CI AC (l.476) | **Then** it runs `ruff check`, `ruff format --check`, the import-boundary checks (…), …; two stub slices, `account` and `life`, each with an empty `engine/`, and a self-test that plants … ; the banned-api rules (…), pytest with … , and fails if any fails | Split into And lines: ruff check + format; the import-boundary checks (AD-1, AD-21, settings/shell/composition roots barred from engines); the two stub slices and the self-test that plants each violation in a temporary copy; the banned-api rules; pytest with `--import-mode=importlib` against Postgres 17; the `openapi.json` staleness and single-Alembic-head checks, and CI fails if any check fails. | One ~150-word sentence in which 'runs' governs nouns it can't run ('two stub slices…'). No content removed. |
| 4 | epics.md Story 1.7 (l.656) | **Then** one `delete_account(user_id)` deletes … and runs every slice's registered on-account-deleted hook after its `DELETE … RETURNING`, in the same transaction, each called as … (Story 10.1 registers the playtest records' one), every device is logged out, and I land on `/` | **Then** one `delete_account(user_id)` deletes the user row and every child row by cascade (…) / **And** after its `DELETE … RETURNING`, in the same transaction, it runs every slice's registered on-account-deleted hook, each called as `hook(session, deleted)` (Story 10.1 registers the playtest records' hook) / **And** every device is logged out, and I land on `/` | Split an overloaded Then clause; replaced the unclear 'one' with 'hook'. |
| 5 | epics.md Story 4.5 (l.1300) | (… with own-account transfers, taking a loan and paying down debt counting zero but the interest that follows counting) | (…; own-account transfers, taking a loan and paying down debt count as zero, but the interest they lead to counts) | The 'with … counting … counting' construction is hard to parse; changed to finite verbs. |
| 6 | epics.md Story 7.7 (l.1842) | it offers only options possible now, each saying when it lands, always asking family (Story 7.4) and doing nothing | it offers only options possible now, each saying when it lands, always including asking family (Story 7.4) and doing nothing | As written, the step itself seems to be 'always asking family'. |
| 7 | epics.md Story 7.7 (l.1847) | the crisis ends when none is true, when I ignore it, or after the third step, the end screen lists what changed, continue is refused (`cannot_continue`) until then, and … | the crisis ends when none is true, when I ignore it, or after the third step; until it ends, continue is refused (`cannot_continue`); the end screen lists what changed, and a crisis never ends the game before 20 | The comma splice put 'until then' far from the event it refers to. |
| 8 | epics.md Story 6.4 (l.1582) | hours above the offer's and extra shifts are prepared states until Story 6.6 | until Story 6.6, raised hours and extra shifts are tested with prepared states | Cryptic ellipsis ('above the offer's'); clarified that this is about test setup. |
| 9 | epics.md Story 5.4 (l.1449) | and buying it with less available money after debt than its price is refused | and buying it is refused when available money after debt is less than its price | Untangled the nested comparison. |
| 10 | epics.md Story 1.4 (l.567), Story 6.1 (l.1504), Story 6.4 (l.1578) | that the reset link still works is tested in Story 1.5; (that planning works in crisis months is tested in Story 7.7); that no tax is due is checked in Story 6.5 | Story 1.5 tests that the reset link still works; (Story 7.7 tests planning in crisis months); Story 6.5 checks that no tax is due | A 'that'-clause as subject is a garden path; made the story the subject. One pattern, three places. |
| 11 | epics.md Story 1.4 (l.584) | **And** this is tested once the first version of the app (the prototype) is built, in Story 10.4, since there is no app to run the test against before that | Consider: **And** Story 10.4 tests these redirects end to end once the prototype is built | The reason clause seems to contradict the story, which builds these pages itself. Ties in with structure QUESTION on Story 10.4. |
| 12 | epics.md Story 6.3 (l.1551) | **And** I can quit in any month, from the next month, which also ends any extra shifts | **And** I can quit in any month; quitting takes effect from the next month and also ends any extra shifts | 'from the next month' was attached to nothing. |
| 13 | epics.md Story 8.11 (l.2130), Story 10.3 (l.2316) | from the freeze before the playtest every gate fails the check; every FR-58 gate fails the content check from then on | from the freeze before the playtest, any failing gate fails the check; any failing FR-58 gate fails the content check from then on | Both read as 'every gate fails'; the meaning is that every gate becomes blocking. |
| 14 | epics.md Story 10.1 (l.2266) | session lengths (time between confirmed actions within an in-game year, gaps above 10 minutes, config, not counted) | session lengths (time between confirmed actions within an in-game year, not counting gaps above the configured 10 minutes) | The comma list inside the brackets hid the verb 'not counted'. |
| 15 | epics.md Story 2.6 (l.896) | the stickers on the mirror are real links with their count or state in text (UX-DR9), for the areas that are built, and the hub keeps … | the stickers on the mirror, for the areas that are built, are real links with their count or state in text (UX-DR9), and the hub keeps … | Moved the dangling qualifier next to 'stickers'. |
| 16 | epics.md Epic List, Tiers (l.386) | Extension is built when it is started before the freeze | Extension is built only if work on it starts before the freeze | 'built when it is started' is circular. |
| 17 | epics.md Story 10.2 (l.2296) | **Then** it starts with `pg_dump` and a restore, and is recorded as a deviation from the course requirement | **Then** the switch starts with `pg_dump` and a restore and is recorded as a deviation from the course requirement | Unclear antecedent: 'it' could be the team or the database. |
| 18 | epics.md Story 9.5 (l.2230) | So that I can follow my progress towards it (FR-57). | So that I can follow my progress towards the target (FR-57). | 'it' could also refer to 'activities'. |
| 19 | epics.md Story 8.3 (l.1934) | insurance (flat NOK 3,000 a year in the MVP, per month) | insurance (a flat NOK 3,000 a year in the MVP, charged monthly) | 'a year … per month' reads as a contradiction. |
| 20 | epics.md Overview (l.23) | the licences are a payment only | the licences are payment-only (no driving game) | Unclear phrase; matches the '[Core, payment only]' tag and Story 8.2's wording. |
| 21 | epics.md Story 8.1 Tier (l.1874) | Core; with 3 layers; more can be cut | Core with 3 layers; more can be cut | The first semicolon split the qualifier from its tier; now matches FR-34. |
| 22 | epics.md Story 1.5 (l.617) | by the mechanism #125 decides | by whichever mechanism #125 settles on | Missing relative pronoun made it read as 'the mechanism #125'. |
| 23 | epics.md Story 1.4 (l.573) | the session lasts until I log out or 30 days without play | the session lasts until I log out or until 30 days pass without play | Not parallel: the second branch has no verb. |
| 24 | epics.md Story 1.4 (l.576-577) | **When** I open `/meny` and choose «Logg ut» or «Logg ut på alle enheter» (with a confirmation) / **Then** (from the menu's 56 px rows, UX-DR33) my session row, … | **When** I open `/meny` and choose «Logg ut» or «Logg ut på alle enheter» from its 56 px rows (with a confirmation, UX-DR33) / **Then** my session row, … | The UI detail belongs to the action, not the outcome. |
| 25 | epics.md Story 6.5 (l.1612) | a full BSU withdrawal takes any deductions received from the payout at once | a full BSU withdrawal claws back any deductions received, taking them from the payout at once | Ambiguous (taking deductions vs. giving them); uses Story 3.2's term 'clawed back'. |
| 26 | epics.md Stories 8.6-8.10 user story | So that this year of my life feels different | Consider: So that this year of my life feels different from the others | 'different' has no point of comparison. Attach to the story that survives the structure condense of 8.6-8.10. |
| 27 | epics.md percent signs (Stories 3.1, 3.2, 3.3, 5.2, 6.5, 7.3, 8.3, 8.10, 9.5; Epic List) vs UX-DR7, UX-DR32 | '2.87 %', '15 %', '60 %, 75 % or 95 %', '100 %' … vs '27%', '55%', '50%' | '2.87%', '15%', '60%, 75% or 95%', and so on | Inconsistent; the Microsoft Writing Style Guide puts no space before %. Outside the inventory and AD lines. |
| 28 | epics.md 'user' vs 'account' (Epic 1 intro, Stories 1.3, 1.6, 1.7, 10.1; FR-44) | Create a user / delete my user vs Delete account / keep my account safe / tester account | Consider: use 'account' in English prose ('Create an account', 'Delete my account') and keep «Lag bruker» / «Slett bruker» as UI strings | In English 'user' reads as the person, and the document switches terms for the same concept. May be a deliberate calque of «bruker»; judgment call. |
| 29 | epics.md Readiness review (l.213) | closes when this branch is merged | Consider: name the branch or PR instead of 'this branch' | Goes stale once merged (PR #143 already is). The structure lens also proposes moving this passage. |
| 30 | epics.md Readiness review (l.211) | the answer key marked as set test states (#117, answer-key part) | Consider: the answer-key figures marked as fixed test states | 'set test states' could mean fixed or prepared states. |
| 31 | epics.md Epic 8 Notes (l.432) | The full library (8.6-8.10, one story per year) and the content check (8.11) come last … Story 8.11 needs only the engine and the starter set, so it can be built before 8.6 | Consider: The full library (8.6-8.10, one story per year) comes last …; the content check (8.11) is listed with it but needs only the engine and the starter set, so it can be built before 8.6 | 'come last' and 'can be built before 8.6' contradict each other when read in sequence. |
| 32 | epics.md Story 5.1 (l.1362) | the Mobil tab shows «Mobil, 2 nye» to screen readers | screen readers announce the Mobil tab as «Mobil, 2 nye» | Nothing is 'shown' to a screen reader. |
| 33 | epics.md Story 10.4 (l.2334) | including 2.5.7 dragging, 2.5.8 target size and 3.3.7 redundant entry | including WCAG 2.5.7 dragging, 2.5.8 target size and 3.3.7 redundant entry | Bare criterion numbers have no referent here. |
| 34 | epics.md Story 9.1 (l.2157) | is built only if the team keeps the in-play lines (cut list) | is built only if the team keeps the in-play lines (they are on the cut list) | The tag '(cut list)' is cryptic. |
| 35 | epics.md Story 5.1 (l.1356) | (surface 11) (UX-DR17) | (surface 11, UX-DR17) | Two adjacent bracket groups; merge them. |
