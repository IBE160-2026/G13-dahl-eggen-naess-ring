---
title: Review of AD-21, round 2 (after giving rule 13 an owner)
date: 2026-11-27
method: bmad-review, lenses adversarial + edge-case-hunter + structure + prose (prose ran on top of structure)
content: ARCHITECTURE-SPINE.md lines 325-361 (AD-21) in the working tree of docs/sara-review-epics, with the uncommitted rule 13 change (kernel owns rule 13 in shared/engine/goals.py; epics Stories 3.6, 4.4, 5.4)
previous: report.md in this folder (round 1, same day, 83 findings)
findings: 54 (adversarial 14, edge-case-hunter 10, structure 10, prose 20)
raw: findings-round2.json
---

# Review of AD-21, round 2 (2026-11-27)

Unranked findings, as the review method requires. Adversarial, edge-case-hunter and structure each ran on their own; prose ran after structure. The two behavioural lenses were asked to check the rule 13 change for consistency and to mark findings that also came up in round 1 ("also in round 1"). Line numbers refer to the working tree.

Round 2 is not a re-check of round 1's list: each lens reviewed AD-21 afresh, so a round 1 finding that is not repeated here is not thereby fixed. Only the rule 13 owner was changed between the rounds.

## The rule 13 change

Most new findings are about the change itself. It gives rule 13 one owner, but leaves these open:

- **When the lowest available money from month 49 is recorded.** The month close is the ledger's step, and goals.py reads the ledger, so who calls whom and in what order is unstated; AD-4 and AD-9 don't name the step (adversarial 1).
- **Its start value and upgraded documents.** Unset before month 49, and documents already past month 49 have no record (adversarial 3, edge-case 2).
- **Progress before continuing in months 49-60.** The view's copy never runs the month close, so the bar leaves out this month's end (adversarial 2, edge-case 1). Progress before month 49 and before the experience is bought is also undefined (edge-case 3).
- **What "the result" holds.** The ending screen shows saved and debt, but the result's shape isn't defined (adversarial 4).
- **Who may call goals.py.** Handlers get no facts, so phone's purchase check needs a facts-free part of goals.py: `available_money(state)` and `net_savings(state)` separate from `check(state, facts, content)` (adversarial 5).
- **Facts with no provider.** `experience_bought` comes from phone in Epic 5, but goals.py is built in Epic 3 (adversarial 6, edge-case 5; also in round 1).
- **Two definitions of debt.** Story 5.4 still reads a `debt` fact from credit while goals.py computes debt from the ledger (adversarial 7).
- **Small gaps.** goals.py is missing from the rule-of-two list (adversarial 8); "reading the ledger" should say balances, never the display totals, and BSU's treatment should be stated in Story 3.6 (adversarial 10); after-action hooks may change balances after the result is stored (edge-case 6); the experience fact has no month, which is safe only as long as the offer expires after month 56 as FR-48 says (edge-case 4).

## Other findings

- **The after-month-60 slot.** It should be required, and the month it receives (60 or 61) is undefined (adversarial 9 and 14, edge-case 7). The loss check needs to know which triggers were true at the end of month 59 (edge-case 8).
- **New since round 1.** Delete behaviour for slice FKs to `playthroughs` (adversarial 11); the composed state type is untyped for slices (adversarial 12); 'stable' order has no reference (adversarial 13); the start action writing life's section (edge-case 9); month 1's open-phase order (edge-case 10).
- **Structure.** Overlaps round 1 (slot order as a list, Shared surfaces merged, the Imports paragraph split) and adds: move the enforcement mechanics to Conventions and the engine contract to AD-1, put Wiring before Extension points, and define Slice and Touches lines. If accepted, AD-21 shrinks by about 11%.

## Adversarial (14)

### Adversarial 1
- **Location:** AD-21 Month-step slots row, 'the kernel then runs wellbeing, rule 8 … and the month close' (spine l.341); spine l.38; epics Story 3.6
- **Problem:** Spine l.38 and Story 3.6 say the month close keeps the lowest available money from month 49, but AD-21's slot row doesn't name that step. AD-9 makes `ledger.close_month` the ledger's own step and only ledger.py writes the totals; goals.py reads the ledger. If close_month calls goals.py the two import each other; if it's a separate kernel step, it has no place in AD-21's or AD-4's order.
- **Fix:** In the slot row, after 'the month close', add: 'then, from month 49, `goals.record_month_end(state)` (kernel) stores the lowest available money in kernel state; ledger.py never calls goals.py'. Add the same step to AD-4 Months and AD-9 Month totals.
- **If shipped as-is:** Builders place the tracker differently, so the buffer goal passes or fails on a different month-end balance than FR-9a defines, or shared.engine hits a circular import.

### Adversarial 2
- **Location:** AD-21 Month-step slots row, after month 60 (spine l.341); AD-4 Months (spine l.92); epics Story 3.6, FR-9c
- **Problem:** The view runs only apply_plan, the December step and rule 8 on a copy, never the month close, and the lowest available money is updated only at the close. In months 49-60 the progress shown before continuing leaves out the current month's projected end, while the check after month 60 includes it. Story 3.6 claims the bar uses the same function.
- **Fix:** State that the view's copy also runs the tracker step (not the rest of close_month), or that goals.py's progress takes the projected month-end balance as the lowest value for the open month. Add a worked-example test in months 49-60 where the plan drops available money below 30,000.
- **If shipped as-is:** The bar says the debt-free goal is on track, the player continues, and the goal is lost that month; FR-9c ('worked out the same way') breaks.

### Adversarial 3
- **Location:** AD-21 Month-step slots row, 'its result is kernel state' (spine l.341); State rule (spine l.357); spine l.38 kernel state list
- **Problem:** Two new kernel-state fields appear (lowest available money from month 49, the rule 13 result), but the kernel-state list at l.38 doesn't name them and no state-upgrade step is mentioned. A document already past month 49 has no recorded lowest value; AD-9's precedent ('starts the list empty') would take the minimum over too few months.
- **Fix:** Name both fields in the kernel state with types; add an upgrade step in shared/persistence/; define the backfill for documents past month 49 (e.g. the next close's balance with an 'incomplete' flag), or state that the field ships before any playthrough can reach month 49.
- **If shipped as-is:** Upgraded playtest or seeded lives reach month 60 with an unrecorded lowest value, the buffer goal is judged on missing months, and the ending is wrong.

### Adversarial 4
- **Location:** AD-21 Month-step slots row, 'its result is kernel state' (spine l.341); epics Story 4.4
- **Problem:** The shape of 'its result' is undefined (a reached flag, or the measures too?). Story 4.4 now reads only 'the kernel's rule 13 result', yet its ending screen shows saved against the livsmål and debt. 'result' also clashes with the kernel's 'results' (AD-13).
- **Fix:** Define `GoalResult(goal, reached, measure, target, debt, lowest_available_from_49)` in goals.py, stored under a named field (e.g. `state.goal_result`). Reword the slot row to 'its outcome is stored in `state.goal_result`'. Restore what Story 4.4 reads.
- **If shipped as-is:** year recomputes 'saved' and 'debt' its own way, and the ending screen can disagree with the outcome that decided the ending.

### Adversarial 5
- **Location:** AD-21 Facts row and Effect handlers row (spine l.343, l.349); epics Story 5.4
- **Problem:** goals.py reads 'the ledger and facts', but only View parts receive facts. Story 5.4's purchase check runs in phone's action or effect handler, whose signatures get neither facts nor the kernel, and goals.py's own signature is never given. (also in round 1 of 2026-11-27)
- **Fix:** Split goals.py into `available_money(state) -> int` and `net_savings(state) -> int` (ledger only, callable from any handler) and `check(state, facts, content) -> GoalResult` (kernel and view parts only). State the split in AD-21 or the kernel description.
- **If shipped as-is:** phone imports the fact merger or reads life's section for `life_goal`, or re-implements available money, which goals.py was introduced to prevent.

### Adversarial 6
- **Location:** AD-21 Facts row, 'one provider per fact' (spine l.349); epics Story 3.6
- **Problem:** Story 3.6 (Epic 3) makes goals.py read `experience_bought`, provided only by phone in 5.4 (Epic 5). AD-21 doesn't say what a declared fact with no provider returns, and a 'prepared state' can't supply a fact computed from a section that doesn't exist yet. (also in round 1 of 2026-11-27)
- **Fix:** State in the Facts row: 'a declared fact with no registered provider takes the default declared with it in facts.py (`experience_bought: bool = False`); tests inject facts through a test kernel with a stub provider'. Have build_kernel log each unprovided fact.
- **If shipped as-is:** Story 3.6 can't be done as written, or every continue after month 60 and every goal-3 bank view raises KeyError until Epic 5.

### Adversarial 7
- **Location:** AD-21 Facts row (spine l.349) vs goals.py; epics Story 5.4 Extension points
- **Problem:** Story 5.4's Extension points still read 'debt' as a fact (from credit), while its AC now takes available money after debt from goals.py, which computes debt from the ledger (card, consumer loans, payment plans, family loans). Two definitions of debt, with no rule that they agree.
- **Fix:** Remove the `debt` fact and have every reader use `goals.available_money` / `goals.debt(state)`, or make the `debt` fact kernel-provided from goals.py. Fix 5.4's Extension points line.
- **If shipped as-is:** A credit `debt` fact without family loans disagrees with goals.py, so offer previews, eligibility and the purchase check disagree on whether the player can afford the experience.

### Adversarial 8
- **Location:** AD-21 DRY by the rule of two (spine l.359)
- **Problem:** The list of pieces known up front to have several users names AD-19's list, the unlock table, the rule 8 triggers and ledger.pay(), but not goals.py, which has three users from the start.
- **Fix:** Add 'goals.py's available money, net savings and goal check (rule 13)' to that sentence.
- **If shipped as-is:** A builder reading only AD-21 starts the logic inside money (3.6), as the old `goal_measure` fact did, reopening the drift.

### Adversarial 9
- **Location:** AD-21 Month-step slots, after month 60 (spine l.341); Order, 'A slot with no handler is a no-op' (spine l.355)
- **Problem:** If the ending slot has no handler (year not built, cut, or missing from registry.py), it is a silent no-op and continue still sets `completed`; the playthrough ends with a goal outcome but no ending. (also in round 1 of 2026-11-27)
- **Fix:** Mark the after-60 ending slot as required: build_kernel fails without a handler, and continue sets `completed` only after asserting an ending is stored.
- **If shipped as-is:** A completed life shows an ending gate with nothing in it.

### Adversarial 10
- **Location:** AD-21 Month-step slots row, 'reading the ledger' (spine l.341); AD-9 Month totals (spine l.169); Stories 3.6 and 4.4
- **Problem:** 'Reading the ledger' doesn't say balances or AD-9's per-month totals (display-only; 'no game rule reads them'). Story 3.6 doesn't state BSU's treatment in available money and net savings, while 4.4 says 'BSU not counted' for the buffer.
- **Fix:** Write 'reading ledger balances (never the month totals) and facts'. In 3.6, state BSU's treatment for each measure, matching 4.4 and FR-9a.
- **If shipped as-is:** The goal check is computed from display totals or counts BSU in the buffer, and the reference run (WE 20) fails a goal it should reach.

### Adversarial 11
- **Location:** AD-21 Imports, models.py rule (spine l.336); AD-4 Life requests (spine l.91)
- **Problem:** Slice tables may have an FK to `playthroughs`, but delete behaviour is unstated, while AD-4 deletes the previous playthrough on a new life and AD-15 needs records to survive.
- **Fix:** Add: 'a slice FK to `playthroughs` is ON DELETE CASCADE unless the data must survive a new life, in which case it keys on `users` only; a migration test starts a new life with a row in every slice table'.
- **If shipped as-is:** Starting a new life fails with IntegrityError (500) once a slice adds a playthrough-keyed table, or needed data cascades away.

### Adversarial 12
- **Location:** AD-21 State rule (spine l.357); Wiring (spine l.356)
- **Problem:** The composed state type exists only at runtime after build_kernel(), so handlers can't name it without importing registry; each slice's `state.<section>` access is untyped, and the type checker can't catch typos or cross-section writes.
- **Fix:** Give handlers typed accessors `section(state, MoneySection)` and `with_section(state, section)` in shared/engine; slices use only these, and a test asserts each handler changed no other section.
- **If shipped as-is:** Misspelled or cross-slice attribute access passes the linters and type checker and fails only at runtime.

### Adversarial 13
- **Location:** AD-21 Order, 'A test asserts that the orders are unique and stable' (spine l.355)
- **Problem:** 'Stable' has no reference; kernel steps (selection, wellbeing, rule 8, month close, the rule 13 check) have no order constants, so their position against slice handlers rests on prose.
- **Fix:** Commit a golden file (`tests/kernel_order.txt`) listing every slot including the kernel steps, with order and owner; the test diffs build_kernel() against it.
- **If shipped as-is:** The rule 13 check or the tracker can be reordered against the month close or rule 8 without a test failing.

### Adversarial 14
- **Location:** AD-21 Month-step slots, handler signature applied to the after-month-60 slot (spine l.341)
- **Problem:** The `month` passed to the after-month-60 handler is undefined: 60 or 61.
- **Fix:** State: 'the after-month-60 slot receives month = 60, the last closed month'.
- **If shipped as-is:** The ending computes age, year or the month 59 vs 60 loss comparison off by one, and the WE 11 boundary tests fail.


## Edge-case hunter (10)

### Edge case 1
- **Location:** AD-21 Month-step slots row, rule 13 and month close (spine l.341); View parts row (spine l.350)
- **Problem:** In months 49-60 the view projects goal progress on a copy that never runs the month close
- **Fix:** goals.progress(copy, facts): low = min(state.kernel.lowest_available_49, available(copy)) if month >= 49 else None
- **If shipped as-is:** The debt-free bar shows the buffer kept while this month's end falls below it.

### Edge case 2
- **Location:** AD-21 Month-step slots row, 'the month close keeps the lowest available money from month 49' (spine l.341, l.38); State (spine l.357)
- **Problem:** The minimum is unset before month 49, or a document past month 49 is upgraded
- **Fix:** lowest_available_49: int | None = None; close sets it from month 49; the upgrade step marks a partial window; goals.check treats a missing month as not reached
- **If shipped as-is:** Goal 2 passes on months 55-60 only, or a default of 0 always fails it.

### Edge case 3
- **Location:** AD-21 Facts row 'goals.py' reader (spine l.349); Month-step slots after month 60 (spine l.341)
- **Problem:** money's progress bar calls goals.py's after-60 check in months 1-48 or before purchase
- **Fix:** goals.progress(state, facts, month) with explicit branches: debt-free before month 49, experience not yet bought; goals.check only when month 60 is closed
- **If shipped as-is:** The bar reads None as the minimum, or shows 0% or 100% at random.

### Edge case 4
- **Location:** AD-21 Facts row (spine l.349); Month-step slots, rule 13 check (spine l.341)
- **Problem:** The experience is bought in months 57-60; the fact experience_bought carries no month
- **Fix:** facts.py: experience_bought_month: int | None; goals.check requires experience_bought_month <= 56
- **If shipped as-is:** Goal 3 counts as reached after a purchase after month 56, contrary to rule 13. (Mitigated by PRD FR-48: the offer expires at the end of month 56, so this needs the expiry to hold; the guard is defence in depth.)

### Edge case 5
- **Location:** AD-21 Facts row (spine l.349); Month-step slots, rule 13 goal check (spine l.341)
- **Problem:** goals.py runs at month 60 before phone provides experience_bought, or after phone is cut (also in round 1 of 2026-11-27)
- **Fix:** facts.py declares experience_bought with a default for a missing provider; build_kernel fails when a fact that goals.py reads has no provider
- **If shipped as-is:** Every month-60 continue fails with KeyError until Epic 5, or each reader picks its own default.

### Edge case 6
- **Location:** AD-21 After-action hooks row (spine l.347) vs Month-step slots, after month 60 (spine l.341)
- **Problem:** after_action hooks run after month 60's continue, after the rule 13 result is stored (also in round 1 of 2026-11-27)
- **Fix:** apply(): if state.status == 'completed': skip after_action hooks; or run the rule 13 check and the ending after the hooks
- **If shipped as-is:** credit's money-in order changes balances after the check; the stored goal result is stale.

### Edge case 7
- **Location:** AD-21 Order, 'A slot with no handler is a no-op' (spine l.355); Month-step slots, after month 60 (spine l.341)
- **Problem:** The after-month-60 slot has no handler (year not built or cut), or two (also in round 1 of 2026-11-27)
- **Fix:** build_kernel(): assert len(slots['after_60']) == 1
- **If shipped as-is:** The life is completed with no ending stored, or two handlers overwrite the ending.

### Edge case 8
- **Location:** AD-21 Month-step slots, continue phase 'rule 8 (triggers.py)' and after month 60 (spine l.341)
- **Problem:** year's loss check needs to know which triggers were true at month 59's end; only rule 13's result is defined as kernel state
- **Fix:** triggers.py stores state.kernel.true_triggers[M] for each month; the ending compares true_triggers[59] & true_triggers[60]
- **If shipped as-is:** year recomputes month 59 or reads only a crisis flag, and gives the wrong loss when 59's and 60's triggers differ.

### Edge case 9
- **Location:** AD-21 Actions row, 'start … kernel members' (spine l.342); Facts row, life_goal (spine l.349); Extension points intro (spine l.337)
- **Problem:** The kernel's start action receives the life goal and avatar that life's section owns
- **Fix:** add an on_start(state, start_action, content) -> state point per slice, or keep life_goal in kernel state with a kernel provider
- **If shipped as-is:** The kernel writes life's section directly, or life_goal ends up held in two places.

### Edge case 10
- **Location:** AD-21 Month-step slots row, open phase (spine l.341); Actions row, start (spine l.342)
- **Problem:** Month 1 is opened by start, not continue; open-phase slots and setup order unstated
- **Fix:** start: ledger.open_month(1); run setup steps; then the open-phase slots and the selection step, or state the opposite order explicitly
- **If shipped as-is:** Month 1 skips income or costs, or charges them before the pengegave setup.

## Editorial structure (10)

| # | Location | Original | Recommendation | Why |
|---|---|---|---|---|
| 1 | AD-21 Month-step slots cell (spine l.341, ~107 words) | The whole open-phase, continue-phase and after-month-60 sequence in one cell | MOVE the sequence into a numbered sub-list below the table (Open phase / Continue phase / After month 60); the cell keeps `(slot, order, handler)`, the signature and 'in the order listed below the table'. | The only strictly ordered list in the AD is the hardest thing to scan. Net ~0 words; the cell shrinks by ~90. |
| 2 | AD-21 Shared surfaces (spine l.358, ~47 words) | Shared surfaces bullet | MERGE into the View parts row (l.350) and Message actions row (l.346); keep only '…or a route in `src/app/` that composes the slices' components' as a clause in View parts. | Same information twice within 12 lines. Saves ~35 words. |
| 3 | AD-21 Imports, unlabelled paragraph after the contracts (spine l.336, ~128 words) | Five unrelated sentences in one paragraph | MOVE the models.py FK sentence to the State bullet (l.357); split the rest into nested lists: backend checks, frontend checks, self-tests. | Hides a table-ownership rule under 'Imports'. ~0 words. |
| 4 | AD-21 Imports, enforcement mechanics (spine l.334 + l.336, ~100 words) | CI self-test planting violations, ESLint zone generation, resolver, lint fixture | MOVE the mechanics to Consistency Conventions, Lint and format (l.381); leave one sentence: 'CI enforces this with import-linter in the backend and ESLint `import/no-restricted-paths` in the frontend; each has a self-test that must fail on planted violations.' | Too much detail for the Rule; neighbouring ADs name their lint rules but not how they're tested. Trade-off: rule and check separated; condensing in place is an alternative. Saves ~70 words in AD-21. |
| 5 | AD-21 Imports, third forbidden contract (spine l.334, ~30 words) | engine packages → settings, roots, shell packages, slice api/models/jobs/cli | MOVE to AD-1 (l.68); leave 'plus AD-1's engine contracts'. | Enforces AD-1's invariant, not slice independence; engine purity is split across two ADs. Saves ~25 words. |
| 6 | AD-21 Wiring (spine l.356) | `PlayerView` is built from named part models, so the generated TS names stay stable. `GET /api/game/quote` lives in `features/credit/api.py`. | MOVE the PlayerView sentence to View parts (l.350) and the quote route to the Capability map (l.534) or AD-18's 'Other calls'. | Placement facts unrelated to wiring. Saves ~20 words. |
| 7 | AD-21 order of Rule sub-bullets (l.337, l.355, l.356) | Extension points, then Order, then Wiring | MOVE Wiring before Extension points (or merge Order into Wiring): Slices → Imports → Wiring → Extension points → State → DRY → Content. | l.337 says 'a slice registers' before the reader learns how registration works. 0 words. |
| 8 | AD-21 l.327, l.330 | 'each names its slice'; 'its Slice line names … its Touches line names' | QUESTION: define them where first used, e.g. '(each story in `epics.md` carries a Slice line naming its slice and a Touches line naming any other slice it registers into)'. | Slice and Touches lines are epics.md conventions, undefined in the spine. ~+20 words. |
| 9 | AD-21 l.330, 331, 356, 357 vs Design Paradigm (l.36-60) | Restated slice list, import direction, composition roots, build_kernel(), section model | PRESERVE | The Paradigm is the overview; AD-21 is the binding rule and adds epic numbers and registration limits. Reinforcement, not redundancy. |
| 10 | AD-21 Extension points table (l.341-353), DRY (l.359), Content (l.360) | Three-column table; two short bullets | PRESERVE | Right shape for lookup; each short bullet guards a distinct failure. |

## Editorial prose (20)

| # | Location | Original | Revised | Why |
|---|---|---|---|---|
| 1 | AD-21 spine l.337 | A slice registers into these points, and nothing else: | A slice registers only into these points: | 'and nothing else' can read as 'nothing else registers'. |
| 2 | AD-21 spine l.349 (Facts) | derived flags are the facts content may see | derived flags are the facts that content may see | 'facts content' reads as a compound noun. |
| 3 | AD-21 spine l.345 (Selection proposers) | writes the month's pending items and whether it is active or quiet | writes the month's pending items and records whether the month is active or quiet | Unclear 'it'; 'writes … whether' needs a fitting verb. |
| 4 | AD-21 spine l.346 (Message actions) | A message kind's buttons (the action member each sends, its label and locked state) as part of its view part | A message kind's buttons (for each button: the action member it sends, its label, and its locked state) as part of the slice's view part | Unclear 'its' and bare 'each'. |
| 5 | AD-21 spine l.343 (Effect handlers) | `…apply(state, effect, cause) → state)`, writing only its own section | `…apply(state, effect, cause) → state)`; `apply` writes only the slice's own section | Dangling participle. |
| 6 | AD-21 spine l.341 (travels with structure MOVE) | fixed costs (`money` 10, `belongings` 20) | fixed costs (`money` at order 10, `belongings` at order 20) | The bare numbers are the `order` constants defined later. |
| 7 | AD-21 spine l.337 | cross-slice behaviour goes only through the kernel, never a direct import and never a write to another slice's section of the state | cross-slice behaviour goes only through the kernel: never through a direct import, and never through a write to another slice's section of the state | Parallel structure. |
| 8 | AD-21 spine l.347 (After-action hooks) | `apply()` after every action: `credit`'s crisis recheck and rule 8 money-in order (AD-9), `explain`'s reactions | Consider: `apply()`, after every action (registered by `credit` for the crisis recheck and rule 8 money-in order (AD-9), and by `explain` for its reactions) | After the colon the cell lists registrants, not users. |
| 9 | AD-21 spine l.341, l.347 | crisis re-check / crisis recheck | crisis recheck (both) | Inconsistent spelling of one term. |
| 10 | AD-21 spine l.352 (Shell hooks) | On-action `on_action(…)` (AD-15); extra locks `lock(session, user_id)` …; on-account-deleted `hook(session, deleted)` (AD-15); sign-up guard `sign_up_guard(…)` | on-action: `on_action(…)` (AD-15); extra locks: `lock(session, user_id)` …; on-account-deleted: `hook(session, deleted)` (AD-15); sign-up guard: `sign_up_guard(…)` | Inconsistent label capitalization; nothing marks where a label ends. |
| 11 | AD-21 spine l.336 (travels with structure MOVE) | A lint fixture that breaks each zone must fail, and CI checks that it does. | A lint fixture that breaks every zone must fail on each one, and CI checks that it does. | One fixture or one per zone? What has to fail? |
| 12 | AD-21 spine l.336 (travels with structure MOVE) | resolves imports with `import/resolver: typescript` so `@/` paths are seen | Consider: resolves imports with `import/resolver: typescript` so that the zones also catch imports through `@/` paths | The passive hides who sees the paths and why. |
| 13 | AD-21 spine l.331 | a slice imports only itself and `shared` | a slice imports only from itself and from `shared` | 'imports itself' is odd read literally. |
| 14 | AD-21 spine l.330 | A story's code lives in the slice its Slice line names, plus `shared/` where the kernel needs it, and in another slice's folder only as registrations that its Touches line names. | A story's code lives in the slice that its Slice line names, in `shared/` where the kernel needs it, and in another slice's folder only as the registrations that its Touches line names. | The series mixed 'plus' with 'and in'. |
| 15 | AD-21 spine l.328 | a change to the card touching the job's code | Consider: a change to the card (`credit`) touching the job's (`work`) code | 'job' can read as the background-job mechanism (l.353). |
| 16 | AD-21 spine l.360 | the content data stays in the repo-root `content/` by kind (AD-7) | the content data stays in the repo-root `content/` folder, organized by kind (AD-7) | 'by kind' was a dangling modifier. |
| 17 | AD-21 spine l.359 | the PR that adds that need moves it to `shared` … are built in `shared` the first time. | the PR that adds the second use moves it to `shared` … are built in `shared` from the start. | 'adds that need' is awkward; 'the first time' can read as 'correctly at first attempt'. |
| 18 | AD-21 spine l.355 | A test asserts that the orders are unique and stable. | A test asserts that the `order` constants are unique and stable. | The plural 'orders' is ambiguous. |
| 19 | AD-21 spine l.356 (Wiring) | returns one frozen `Kernel` holding every table … The engine is `apply(state, action, content, seed, kernel)`. | Consider: returns one frozen `Kernel` holding every registration table … The engine's entry point is `apply(state, action, content, seed, kernel)` | Which tables? And 'the engine is' equates a package with one function. |
| 20 | AD-21 spine l.328, 334, 341, 342, 343, 344, 345, 349, 350, 352 | 'built, reviewed or cut alone'; 'collects, filters and applies'; 'AD-16, other slices' rules, `triggers.py`, `goals.py`, the content check'; 'The pipeline, `delete_account`, sign-up' | Add the serial comma; in l.349 and l.352 also add 'and' before the last item | Microsoft style requires the serial comma, and two series lack a conjunction. The spine omits the serial comma throughout: apply spine-wide or not at all. |

