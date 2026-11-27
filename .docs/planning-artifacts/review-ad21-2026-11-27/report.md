---
title: Review of AD-21 (vertical slices with a shared kernel), second round
date: 2026-11-27
method: bmad-review, lenses adversarial + edge-case-hunter + structure + prose (prose ran on top of structure)
content: ARCHITECTURE-SPINE.md lines 325-361 (AD-21) at main 2dbbd4c, after the kernel change in commit 6196f35
previous: review-ad21-2026-11-26 (53 findings, commit 2315bd7)
findings: 83 (adversarial 21, edge-case-hunter 26, structure 14, prose 22)
raw: findings.json
---

# Review of AD-21, second round (2026-11-27)

Unranked findings, as the review method requires. Adversarial, edge-case-hunter and structure each ran on their own without seeing the others' findings, so overlap between them is signal. Prose ran after structure and skipped text that structure proposes to move or merge. Line numbers refer to `ARCHITECTURE-SPINE.md` at commit `2dbbd4c`.

## Status of the 2026-11-26 findings

Both behavioural lenses were asked to check the first round's findings against the current text. Almost all are resolved by commit `6196f35` (the kernel and the extension-point table). One is still partly open: the `fetch` ban misses `window.fetch` and `globalThis.fetch` (adversarial 16, edge-case 24). The missing default for facts with no provider continues an earlier point in narrower form (adversarial 5).

## Contradictions with the rest of the spine

These are not gaps but places where AD-21 and another AD say different things:

- **Interest vs instalments.** AD-21's open phase runs instalments before debt interest; AD-9 says interest comes before any instalment or bill (adversarial 1).
- **Continue phase order.** AD-21 runs the December BSU step before wellbeing; AD-4 and AD-9 run wellbeing first. The rule 13 goal check before the ending has no slot or owner (adversarial 2, edge-case 16 and 17).
- **`on_action` signature.** AD-21 has `session`; AD-15 and Story 10.1 don't (adversarial 18, edge-case 4).
- **`view()` signature.** AD-13's `view()` takes no `kernel`, yet assembles parts from it (adversarial 12, edge-case 3).
- **The playtest slice.** AD-21 maps it to Epic 10 only; `epics.md` maps it to Epics 1 and 10, and uses Slice lines (`shared`, `—`) that AD-21 doesn't allow (adversarial 19).

## Overlap between the lenses

Found by both adversarial and edge-case-hunter on their own:

- **Signatures without context.** Month-step handlers, actions, effect handlers, crisis options and continue guards get no facts, draws or kernel, so slices must read each other's state (adversarial 3 and 4, edge-case 1).
- **Shell paths without the kernel.** Sign-up, `delete_account`, the inactivity job and `/api/game/quote` need the kernel but only the game router gets it (adversarial 9, edge-case 2).
- **Facts with no provider.** No default and no check of 'one provider per fact' (adversarial 5, edge-case 12).
- **Effect handlers.** `possible()` can't see the effect, multi-effect options have no rule, and unknown effect kinds aren't caught (adversarial 6 and 7, edge-case 9, 10 and 11).
- **Missing order and uniqueness.** After-action hooks, extra locks, on-action hooks, crisis options and upcoming costs have no `order`, and nothing rejects duplicate registrations (adversarial 11, edge-case 5, 7 and 8).
- **Silent no-ops.** A forgotten registration makes a slice's steps do nothing without failing (adversarial 8, edge-case 14).
- **Section writes not enforced.** A slice can read or write another slice's section by attribute without any import (adversarial 10, edge-case 13).
- **Upcoming costs drift.** FR-57's preview is computed separately from what the month charges (adversarial 20, edge-case 15).
- **Import checks with holes.** String-based FKs and relationships, features → app imports, unlisted feature folders, and a self-test that doesn't plant every kind of violation (adversarial 14, 15 and 17, edge-case 23, 25 and 26).
- **State sections and upgrades.** Adding or removing a slice section has no upgrade rule, and upgrade steps for slice sections would live in shared (adversarial 21, edge-case 19).

Found only by adversarial: the Touches rule vs the rule of two and Story 6.5 (13). Found only by edge-case-hunter: after-action hooks also running after kernel actions (6), the continue guard's refusal code (18), protocol fields in seed JSON (20), which `APP_ENV` allows seeding (21), and concurrent sign-ups past the tester guard (22).

## Adversarial (21)

### Adversarial 1
- **Location:** AD-21 Extension points, Month-step slots row (spine l.341)
- **Problem:** The open phase puts 'instalments (credit)' in a slot before 'card bill and debt interest (credit)'. AD-9 says each month's interest on the card, a consumer loan or a payment plan is its own interest call made 'before any instalment or bill', and rule 1 groups loan instalments, the card bill and interest on debt as one step.
- **Fix:** Reorder the open phase: debt interest (credit), then instalments (credit), then card bill (credit). Or make one 'debt' slot with explicit orders (interest=10, instalments=20, card_bill=30). Quote AD-9's 'interest before any instalment or bill' in the row.
- **If shipped as-is:** A builder who follows AD-21's slot order charges interest on balances already paid down. Worked examples 17, 20 and 21 miss by a few kroner (the same interest-order error the 2026-11-05 review found), and rule 8 debt triggers and replay can flip.

### Adversarial 2
- **Location:** AD-21 Extension points, Month-step slots row, continue phase (spine l.341)
- **Problem:** AD-21's continue phase runs planned activities, then the December BSU step, then the kernel's wellbeing, then rule 8 and the close. AD-4 and AD-9 say apply_plan is 'planned activities … then wellbeing', and only then the December step. AD-21 doesn't mark which continue slots make up apply_plan, which the view runs on a copy without the close. The rule 13 goal check before the ending has no owner.
- **Fix:** Align with AD-4: planned activities (work), then wellbeing (kernel) as apply_plan; then December BSU (money); then rule 8 and close. Name the phase boundary the view preview runs (e.g. `preview_until='rule8'`). Give the after-month-60 step two named entries: the rule 13 goal check (owner) and the ending (year).
- **If shipped as-is:** Two architecture sections give different month orders, so the view's 'after the plan' figures (score, bands, trigger status, goal progress) can disagree with the real continue.

### Adversarial 3
- **Location:** AD-21 Extension points: Month-step slots, Actions, Effect handlers rows (spine l.341-343)
- **Problem:** The signatures `handler(state, content, month)`, `handler(state, action, content)` and `apply(state, effect, cause)` get no seed or draw access; only selection proposers get `draws`. Yet money's unexpected-expense slot draws, and rule 14's parents-pay-insurance share is drawn when the player gets the moped, inside belongings' effect.
- **Fix:** Add a draws accessor (the AD-6 draw store plus the draws.py functions bound to the seed) to the month-step, action and effect-handler signatures, or state that the kernel pre-draws every key and handlers only read the draw store. Name which is the rule.
- **If shipped as-is:** Slices reach for the seed another way (stash it in state, or call draws.py with a seed they don't have), and draw ownership and replay determinism (AD-6) break per slice.

### Adversarial 4
- **Location:** AD-21 Extension points: Facts row vs Month-step slots, Effect handlers, Continue guards, Crisis options, Upcoming costs rows (spine l.341-351)
- **Problem:** Facts are merged by one kernel function over registered providers, but only view parts receive `facts`. Month-step handlers, actions, effect handlers, crisis options, continue guards and upcoming-cost providers get neither facts nor the kernel. Money's fixed-cost step must read `owns_moped`, and its December BSU step must read `tax_this_year`. `continue_guard(state)` also lacks `content`, though the crisis choice limit is configuration.
- **Fix:** Give every engine-side extension signature a `facts` argument, or a `ctx` holding facts, draws and content computed once per step by the kernel; or state that facts are materialised into a kernel section after every step. Fix `continue_guard(state, content, facts)`.
- **If shipped as-is:** Money reads belongings' or work's section by attribute name instead: cross-slice coupling invisible to import-linter, and exactly what AD-16 forbids.

### Adversarial 5
- **Location:** AD-21 Extension points: Facts row (spine l.349); Order (spine l.355)
- **Problem:** 'One provider per fact' is unchecked, and nothing says what happens when a declared fact has no provider. Money (Epic 3) reads `tax_this_year`, which work provides only from Epic 6; a cut slice (belongings, holding the Can-be-cut 8.4) leaves `owns_moped` unprovided. Slots define 'no handler = no-op', facts have no such rule. Continues a 2026-11-26 point in narrower form.
- **Fix:** Declare a default in facts.py for each fact, used when no provider is registered (`owns_moped=False`, `tax_this_year=0`). Add a kernel test that fails on two providers for one fact and on a provider for an undeclared fact.
- **If shipped as-is:** Money's December BSU step crashes with KeyError or reads None until Epic 6 lands, or each reader invents its own fallback and FR-21's deduction differs between builds.

### Adversarial 6
- **Location:** AD-21 Extension points: Effect handlers row (spine l.343)
- **Problem:** `possible(state, content) → bool` doesn't receive the effect, so possibility can't depend on its parameters (amount, which loan, price, target month). AD-21 also doesn't say what happens for an option with effects from several slices: must every `possible` hold, and in what order are effects applied?
- **Fix:** Change it to `possible(state, effect, content, facts) → bool`. State that an option is possible only if every effect's `possible` is true, and that its effects apply in content order under one choice sequence number (AD-9).
- **If shipped as-is:** Unaffordable options, or ones landing after month 60, are shown; or slices register one effect kind per parameter value. Multi-slice options (sell moped plus money in) apply in builder-dependent order, changing the rule 8 money-in result.

### Adversarial 7
- **Location:** AD-21 Rule: Content is not code (spine l.360); Effect handlers row (spine l.343)
- **Problem:** The content model and item check stay in `shared/`, but effect kinds, crisis events, shifts and room layers are slice-owned. Their parameter schemas must then live in shared (which then knows every slice) or in the slices (where `check_item` can't validate them). Nothing checks that the kinds `lists.yaml` names have a registered handler owned by the named slice.
- **Fix:** Make the effect-handler registration carry its parameter model: `effect_kind → (ParamModel, possible, apply)`. Let the loader and `check_item` validate effects against the kernel's registered models (main.py and cli.py pass the kernel). Fail startup and the content check on a kind with no handler, or when `lists.yaml`'s owner differs from the registering slice.
- **If shipped as-is:** A frozen library references an effect kind no slice handles and fails at runtime mid-playthrough, or shared's content model becomes the merge hotspot every slice PR edits.

### Adversarial 8
- **Location:** AD-21 Rule: Wiring and Order (spine l.355-356)
- **Problem:** AD-21 doesn't define how a slice exposes its registrations to `build_kernel()` ('nothing is registered at module level'), so registry.py must hand-list every handler, part, provider and hook from every slice. A forgotten entry is silent because a slot with no handler is a no-op. 'Frozen Kernel' doesn't say the tables inside are immutable.
- **Fix:** Give every slice one entry point, e.g. `features/<s>/contrib.py: def contribute(b: KernelBuilder) -> None`, called once per slice from registry.py. Test that each slice's declared contributions appear in the built kernel. Store tables as tuples and MappingProxyType.
- **If shipped as-is:** Parallel PRs conflict in registry.py, a dropped registration line merges green, and the kernel's lists can be mutated after build, bringing back the import-order dependence AD-21 claims to remove.

### Adversarial 9
- **Location:** AD-21 Extension points: Shell hooks and CLI, jobs, seeds rows (spine l.352-353); Wiring (spine l.356)
- **Problem:** Only `shared/api/game.py` is said to receive the kernel (`build_game_router(kernel)`). Account's sign-up must run the sign-up guards, `delete_account` must run the extra locks and on-account-deleted hooks, and credit's `/api/game/quote` must run the engine. The daily job signature `run(session, now)` has no kernel, yet the inactivity job calls `delete_account`.
- **Fix:** State that every slice router is built by `build_router(kernel)` called from main.py, that daily jobs and CLI commands receive the kernel (`run(session, now, kernel)`), and that `delete_account(session, user_id, kernel)` takes it explicitly.
- **If shipped as-is:** Account imports registry (independence fails through the indirect chain) or reads a module global; or the inactivity job deletes accounts without the playtest hook, so `testers_left` drifts (FR-50) and the AD-4 lock order is skipped.

### Adversarial 10
- **Location:** AD-21 Extension points intro and State (spine l.337, l.357)
- **Problem:** 'Never a write to another slice's section' and 'writing only its own section' are not enforced. Every handler receives and returns the whole state, and since the document model is composed at runtime, a slice can read or write `state.work.tax_this_year` by attribute with no import, so import-linter sees nothing.
- **Fix:** Pass each handler the kernel sections plus only its own section and merge back only that section; or add a kernel test harness that runs every registered handler in the worked examples and fails if any non-owned section changed.
- **If shipped as-is:** Cross-slice reads and writes creep in invisibly, and AD-21's main promise (a slice can be reviewed and cut alone) quietly stops holding.

### Adversarial 11
- **Location:** AD-21 Rule: Order (spine l.355); After-action hooks, Shell hooks, Crisis options, Upcoming costs rows (spine l.344, 347, 351, 352)
- **Problem:** The order rule covers only registrations that carry `order`. After-action hooks have none, though credit's rule 8 money-in and explain's reactions must run in a fixed sequence. Extra locks have none, so two locks have undefined order against AD-4's deadlock rule. On-action hooks, crisis option display and upcoming-cost list order are unordered too. Nothing asserts uniqueness of effect kinds, view part names or action `type` literals.
- **Fix:** Add `order` to after-action hooks, extra locks, on-action hooks, crisis options and upcoming costs. Extend the order test to every ordered table, and add uniqueness assertions for effect_kind, part name, row_slot+order and action discriminator.
- **If shipped as-is:** Registry import order decides whether explain reacts before or after credit moves money, and in what order locks are taken: the replay and deadlock risk the Order rule says it removes.

### Adversarial 12
- **Location:** AD-21 Extension points: View parts row (spine l.350); AD-13 view signature (spine l.208)
- **Problem:** `build(state, content, facts)` lacks the view's other inputs (`seen_disclosure_ids`, `nickname`, `last_action_at`) and the after-the-plan copy AD-4 requires for projected figures. AD-13's `view(state, content, last_action_at, seen_disclosure_ids, nickname)` has no `kernel`, yet assembles parts from it.
- **Fix:** Define `build(ctx) → PartModel` with ctx holding state, projected state, content, facts, seen_disclosure_ids, nickname and last_action_at. Change AD-13 to `view(state, content, kernel, last_action_at, seen_disclosure_ids, nickname)`.
- **If shipped as-is:** Explain's disclosure part can't filter seen disclosures, so FR-40's 'never shown again' fails; or parts compute projections themselves outside the one apply_plan run, and score or band figures diverge.

### Adversarial 13
- **Location:** AD-21 Rule: Slices and DRY by the rule of two (spine l.330, l.359); epics.md Story 6.5 Touches line
- **Problem:** A story may touch another slice's folder 'only as registrations that its Touches line names', but the rule of two requires the PR to move code out of slice A into shared, editing more than registrations. Story 6.5's Touches line describes a change to money's BSU withdrawal logic, not a registration. AD-21 doesn't define what a Touches line may contain.
- **Fix:** Widen the rule: another slice's folder may be edited for (a) registrations and (b) a rule-of-two move to shared, both named on the Touches line with slice, file and reason. Rewrite 6.5's Touches line to name a registration, or move the clawback into money's own story.
- **If shipped as-is:** Reviewers either block legitimate rule-of-two moves or stop treating the Touches rule as binding, and the line no longer describes a story's real footprint.

### Adversarial 14
- **Location:** AD-21 Rule: Imports, paragraph after the contracts (spine l.336)
- **Problem:** 'A slice's models.py declares foreign keys and relationship() only to kernel tables' has no check. String-based `relationship('OtherModel')` and `ForeignKey('other_table.id')` resolve on the shared Base with no import. The ruff ban covers only `importlib.import_module` and `__import__`, not `importlib.util`, `pkgutil`, `runpy` or `sys.modules` lookups.
- **Fix:** Add a test in `backend/tests/` that walks `Base.metadata` and the mappers and fails on any FK or relationship from a slice table to another slice's table. Extend the banned-api list to `importlib.util.spec_from_file_location`, `pkgutil.iter_modules`, `runpy` and `sys.modules`.
- **If shipped as-is:** Cross-slice table coupling merges green and shows up only as a cascade or migration surprise when a slice is cut or reordered.

### Adversarial 15
- **Location:** AD-21 Rule: Imports, frontend sentence (spine l.336)
- **Problem:** The generated zones deny feature-to-feature, shared → features and shared → app, but not features → app, so a slice can import a route or layout from `src/app/`. The slice list the zones are generated from isn't tied to the folders, so a new `src/features/<x>` missing from the list gets no zone.
- **Fix:** Add a zone with target `src/features`, from `src/app`. Generate the slice list with `fs.readdirSync('src/features')` in `eslint.config.mjs` (or assert it equals the folder list). Add a features → app import to the lint fixture.
- **If shipped as-is:** Slices couple to routes, and a newly added slice is silently unrestricted while CI stays green.

### Adversarial 16
- **Location:** AD-21 Rule: Imports, frontend sentence (spine l.336)
- **Problem:** Still open from 2026-11-26 (finding 16, partly): `fetch` is banned only with `no-restricted-globals`, which doesn't catch `window.fetch(...)` or `globalThis.fetch(...)`; `XMLHttpRequest`, `EventSource` and `navigator.sendBeacon` aren't covered.
- **Fix:** Add `no-restricted-properties` for `window.fetch`, `globalThis.fetch` and `self.fetch`, and `no-restricted-globals` for `XMLHttpRequest` and `EventSource`, all off for `src/shared/api/**`. Put one of each in the lint fixture.
- **If shipped as-is:** A feature component calls the API around the game client, skipping AD-18's single protocol owner (retries with the same `request_id`, envelope handling) with no lint error.

### Adversarial 17
- **Location:** AD-21 Rule: Imports, CI self-test (spine l.336)
- **Problem:** The self-test plants only four kinds of violation: slice to slice, shared to slice, engine to fastapi, engine to app.settings. The third contract also lists `app.shared.content`, `.persistence`, `.api`, `.jobs`, the composition roots and every slice's api, models, jobs and cli. A typo or wildcard matching nothing in these targets is never shown to fail, and the ruff importlib ban has no planted case.
- **Fix:** Generate one planted violation per forbidden target of each contract (each listed module, and a slice's own api/models/jobs/cli from its engine), plus one `importlib.import_module` call for ruff. Assert each fails.
- **If shipped as-is:** A misspelled target (e.g. `app.shared.jobs` vs a real `app.shared.job`) leaves an engine free to import shell code while CI reports the boundary as proven.

### Adversarial 18
- **Location:** AD-21 Extension points: Shell hooks row (spine l.352) vs AD-15 Records (spine l.268) and epics.md Story 10.1
- **Problem:** AD-21 defines the hook as `on_action(session, user, before, after, action, now)`. AD-15 and the epics story give it as `records.on_action(user, before, after, action, now)`, with no session.
- **Fix:** Pick one signature, most likely the one with `session`, since the hook writes the records table in the same transaction, and use it in AD-15, the epics inventory and the playtest story.
- **If shipped as-is:** The playtest builder follows AD-15 or the story, gets no session, and opens its own outside the pipeline's transaction, breaking AD-15's 'in the same transaction'.

### Adversarial 19
- **Location:** AD-21 Rule: Slices (spine l.330); Binds (spine l.327)
- **Problem:** AD-21 maps `playtest` to Epic 10 only, but the epics table maps it to Epics 1 and 10 (Story 1.8). Several stories carry Slice lines '— (infra)', '— (content)' and '— (manual checks)', and many Epic 2 stories carry `shared`. 'Each names its slice' and 'one per epic domain' cover none of these.
- **Fix:** Write `playtest (1, 10)`. Add that a Slice line may also be `shared` (with its parts in parentheses) or `—` with a reason, for stories that add no backend or frontend code.
- **If shipped as-is:** AD-21 and epics.md disagree; a reviewer applying AD-21 literally flags valid stories, or treats `—` stories as unbound.

### Adversarial 20
- **Location:** AD-21 Extension points: Upcoming costs row (spine l.351)
- **Problem:** Each slice computes next month's costs in a separate `upcoming_costs` provider that repeats its month-step cost logic (fixed costs, moped fuel by season, instalments, card bill). Nothing ties the two together.
- **Fix:** Compute FR-57's list by dry-running next month's open-phase cost slots on a copy, or require a test that for every worked example and seed run the upcoming costs for M+1 equal the costs charged when M+1 opens (absent new choices).
- **If shipped as-is:** The FR-57 list (Core) says one figure and the month charges another (moped fuel switching on in April, a payment-plan instalment): the drift the 2026-11-26 review warned about.

### Adversarial 21
- **Location:** AD-21 Rule: State (spine l.357)
- **Problem:** Slice sections are defined in the slices, but the ordered state-upgrade list lives in `shared/persistence/`. Shared can't import slice models, so each upgrade step for a slice section hard-codes that section's field names and defaults as raw dicts: slice knowledge in shared that import-linter can't see, duplicating the slice's defaults.
- **Fix:** Add an extension point 'state upgrades: (schema_step, section, upgrade(dict) → dict)', registered by the owning slice; the kernel builds the single ordered list from the registrations, and CI checks for duplicate or missing step numbers.
- **If shipped as-is:** A slice changes a field default while the shared upgrade writes the old one, so upgraded documents differ from new ones, and replay and seed assertions diverge by schema version.


## Edge-case hunter (26)

### Edge case 1
- **Location:** AD-21 Extension points, Month-step slots / Actions / Effect handlers / Crisis options rows vs Facts row (spine l.341-344, l.349)
- **Problem:** A slice handler needs facts, effect handlers or crisis providers; its signature passes no kernel
- **Fix:** handler(state, content, month, ctx) where ctx = KernelContext(facts=kernel.facts(state), effects=kernel.effects, crisis_options=kernel.crisis_options), built by apply() and passed to every slice callable
- **If shipped as-is:** Money can't read owns_moped, and credit can't collect crisis options without importing slices or registry.

### Edge case 2
- **Location:** AD-21 Wiring + Shell hooks + CLI, jobs, seeds rows (spine l.352-353, l.356)
- **Problem:** Account's delete_account, sign-up router and inactivity job need the Kernel's hooks and locks
- **Fix:** create_app(kernel) calls each slice's build_router(kernel); jobs registered as run(session, now, kernel); delete_account(session, user_id, kernel)
- **If shipped as-is:** Account imports registry (independence chain fails), or it skips playtest's hooks and extra locks.

### Edge case 3
- **Location:** AD-21 Wiring (spine l.356) vs AD-13 One view function (spine l.208)
- **Problem:** view() assembles registered view parts, but its declared signature takes no kernel
- **Fix:** view(state, content, last_action_at, seen_disclosure_ids, nickname, kernel) -> PlayerView, named next to apply() in Wiring
- **If shipped as-is:** View parts get read from a module-level registry, which Wiring forbids.

### Edge case 4
- **Location:** AD-21 Shell hooks row (spine l.352) vs AD-15 Records (spine l.268)
- **Problem:** AD-21 declares on_action(session, user, before, after, action, now); AD-15 declares on_action(user, before, after, action, now)
- **Fix:** Use one signature in both: on_action(session, user, before, after, action, now)
- **If shipped as-is:** The pipeline calls the records hook with the wrong arguments, so every game action fails in the playtest.

### Edge case 5
- **Location:** AD-21 Order (spine l.355); After-action hooks, Crisis options, Upcoming costs, Shell hooks, CLI/jobs, Actions, View parts rows (spine l.342-353)
- **Problem:** Several slices register into a point whose registration shape carries no order constant
- **Fix:** Add order to after_action, crisis_options, upcoming_costs, on_action, on_account_deleted, sign_up_guard and daily jobs; sort union members and PlayerView parts by name in build_kernel
- **If shipped as-is:** Reordering imports in registry.py changes post-action state, the crisis menu order or openapi.json, despite the stated claim.

### Edge case 6
- **Location:** AD-21 After-action hooks row (spine l.347) vs Month-step crisis re-check slot (spine l.341)
- **Problem:** after_action runs 'after every action', including continue, start and end early
- **Fix:** after_action runs only after slice action members and option choices, never after kernel members (start, continue, end early, play again)
- **If shipped as-is:** Credit's crisis recheck runs twice when M+1 opens, or runs on an ended life.

### Edge case 7
- **Location:** AD-21 Shell hooks row, extra locks (spine l.352); AD-4 Lock order (spine l.90)
- **Problem:** Two extra locks are registered, or the user has no playthrough row to lock after
- **Fix:** extra_locks sorted by an order constant; taken right after the playthrough lock, or right after the sessions lock when no playthrough row exists
- **If shipped as-is:** The pipeline and delete_account take locks in opposite orders and deadlock, or the extra lock is skipped.

### Edge case 8
- **Location:** AD-21 Wiring, build_kernel (spine l.356); Extension points table (spine l.341-353)
- **Problem:** Duplicate effect_kind, fact name, action type, crisis option id or job/seed/CLI name; unknown slot name
- **Fix:** build_kernel raises on any duplicate key across slices and on a slot or row_slot not in the kernel's enum
- **If shipped as-is:** Dict last-wins silently drops a slice's handler, or a handler on a misspelled slot never runs.

### Edge case 9
- **Location:** AD-21 Effect handlers row (spine l.343)
- **Problem:** Content uses an effect kind with no registered handler, or lists.yaml owner differs from registrant
- **Fix:** Content check fails on an effect kind without a kernel handler; build_kernel fails if the registering slice is not the lists.yaml owner
- **If shipped as-is:** Choosing the option raises KeyError and a 500 mid-month, or the wrong slice owns the write.

### Edge case 10
- **Location:** AD-21 Effect handlers row (spine l.343)
- **Problem:** possible(state, content) never sees the effect instance; apply(state, effect, cause) gets no content
- **Fix:** possible(state, content, effect) -> bool; apply(state, content, effect, cause) -> state
- **If shipped as-is:** An unaffordable or already-held effect reports possible, and apply lacks the pinned config figures.

### Edge case 11
- **Location:** AD-21 Effect handlers row (spine l.343)
- **Problem:** An option has several effects; an earlier effect's apply makes a later one impossible
- **Fix:** Check every effect's possible() on the pre-option state, apply in listed order, and refuse the whole option if any check fails
- **If shipped as-is:** The option is half-applied, and no rule says whether to refuse or roll back.

### Edge case 12
- **Location:** AD-21 Facts row (spine l.349)
- **Problem:** A declared fact has no provider (slice not built yet or cut), or a provider returns undeclared names
- **Fix:** kernel.facts() asserts each provider returns exactly its declared facts with declared types; build_kernel fails on a declared fact with no provider, or facts.py gives it a declared default
- **If shipped as-is:** Content requiring owns_moped hits a KeyError, or the flag reads as false silently.

### Edge case 13
- **Location:** AD-21 Extension points intro and Effect handlers row (spine l.337, l.343)
- **Problem:** A handler writes another slice's state section; no check enforces 'only its own section'
- **Fix:** In tests, the kernel wraps each slice callable and asserts that every section other than the owner's and the kernel's is unchanged
- **If shipped as-is:** Cross-slice writes pass CI, and AD-21's core isolation promise breaks unnoticed.

### Edge case 14
- **Location:** AD-21 Order, 'A slot with no handler is a no-op' (spine l.355)
- **Problem:** A slice folder exists, but build_kernel omits its registrations
- **Fix:** Test: the slices registered in build_kernel equal the folders under app/features (except slices explicitly marked cut)
- **If shipped as-is:** The slice's month steps all no-op silently, caught only if a cross-slice worked example covers them.

### Edge case 15
- **Location:** AD-21 Upcoming costs row (spine l.351)
- **Problem:** upcoming_costs computes next month's costs separately from the month-step handlers that charge them
- **Fix:** Test for every worked example and month M: upcoming_costs at M equals the costs the open-phase handlers charge when M+1 opens
- **If shipped as-is:** The FR-57 preview disagrees with what next month actually charges.

### Edge case 16
- **Location:** AD-21 Month-step slots, continue phase (spine l.341) vs AD-4 Months (spine l.92) and AD-9 Month totals (spine l.169)
- **Problem:** AD-21 runs December BSU before kernel wellbeing; AD-4 and AD-9 run wellbeing before it
- **Fix:** Continue phase: planned activities (work), kernel wellbeing, December BSU (money), rule 8, close_month; or change AD-4 and AD-9 to match
- **If shipped as-is:** Builders order the steps differently, so the view's copy and the real continue diverge.

### Edge case 17
- **Location:** AD-21 Month-step slots, 'After month 60: ending (year)' (spine l.341) vs AD-4 Months (spine l.92)
- **Problem:** AD-4's rule 13 check before the ending has no slot or owner in AD-21
- **Fix:** After month 60: rule 13 check (named owner, order 10), then ending (year, order 20)
- **If shipped as-is:** The rule 13 check gets skipped or built twice.

### Edge case 18
- **Location:** AD-21 Continue guards row (spine l.348)
- **Problem:** A guard returns a refusal code, but continue always refuses with cannot_continue
- **Fix:** continue_guard(state) -> bool, or the action refuses with the guard's returned code; state which, and list allowed codes
- **If shipped as-is:** A guard's code is dropped or sent unexpected, so the client can't render the reason.

### Edge case 19
- **Location:** AD-21 State (spine l.357)
- **Problem:** A new slice section is added to existing documents, or a cut slice's section remains
- **Fix:** Each section model defaults every field, or adding or removing a section requires a state_schema step; CI fails if the composed model's schema changes without one
- **If shipped as-is:** Loading a stored playtest document fails validation, or the lax model silently drops a section.

### Edge case 20
- **Location:** AD-21 CLI, jobs, seeds row (spine l.353)
- **Problem:** Seed action JSON is validated as a full GameRequest, whose protocol fields are unknown when authored
- **Fix:** Store only action members; the CLI fills request_id, playthrough_id, month and plan_version from the current state, then validates with kernel.game_request_type
- **If shipped as-is:** Seeds fail validation, or stale protocol fields are refused with game_changed or plan_changed.

### Edge case 21
- **Location:** AD-21 CLI, jobs, seeds row, 'seeding is gated by APP_ENV' (spine l.353)
- **Problem:** Which APP_ENV values allow seeding is unstated (local, ci, playtest)
- **Fix:** Seeding allowed when APP_ENV in {local, ci}; the CLI refuses otherwise with a named error
- **If shipped as-is:** Examiner seeds get refused locally, or seed users get created on the playtest database.

### Edge case 22
- **Location:** AD-21 Shell hooks row, sign_up_guard (spine l.352)
- **Problem:** Two concurrent sign-ups both pass the guard before either commits; no row is locked
- **Fix:** sign_up_guard locks the testers_left counter row FOR UPDATE and runs after the users ON CONFLICT insert, in the same transaction
- **If shipped as-is:** The FR-50 sign-up limit is exceeded, or the guard counts a sign-up that email_in_use refuses.

### Edge case 23
- **Location:** AD-21 Imports, frontend zones (spine l.336)
- **Problem:** A feature imports from src/app, or a features folder missing from the slice list
- **Fix:** Add zone target ./src/features from ./src/app; build zones from readdirSync('src/features') and fail lint config if it differs from the slice list
- **If shipped as-is:** A feature imports a route, or an unlisted folder imports every slice unchecked.

### Edge case 24
- **Location:** AD-21 Imports, fetch ban (spine l.336)
- **Problem:** window.fetch, globalThis.fetch or self.fetch used in a feature (no-restricted-globals misses these)
- **Fix:** no-restricted-properties for window.fetch, globalThis.fetch and self.fetch, off for src/shared/api/** (raised on 2026-11-26, still open)
- **If shipped as-is:** A feature calls the API directly, bypassing the game client, and lint passes.

### Edge case 25
- **Location:** AD-21 Imports, CI self-test and lint fixture (spine l.336)
- **Problem:** The planted violations don't include an @/ aliased import, the fetch ban or a dynamic import
- **Fix:** Lint fixture imports @/features/<other> and calls fetch; backend plants features.x.engine -> features.x.api and importlib.import_module, and asserts each fails
- **If shipped as-is:** A broken resolver or rule passes green; the alias part of the 2026-11-26 resolver finding stays unproven.

### Edge case 26
- **Location:** AD-21 Imports, models.py rule (spine l.336)
- **Problem:** ForeignKey('loans.id') or relationship('Loan') strings reach another slice's table
- **Fix:** Test over Base.metadata and mappers: every FK target and relationship target is in the same slice's models or a kernel table
- **If shipped as-is:** Cross-slice table coupling passes import-linter, and cutting a slice breaks migrations.

## Editorial structure (14)

Structure model: Reference/Database (the spine is a register of decisions, each Binds / Prevents / Rule). AD-21 follows the shared pattern; the issues are inside the Rule. 1,185 words. If all changes are accepted the length is roughly unchanged (about -30 words, +35-40 words); the gain is scannability: the slot order becomes a list, backend and frontend checks get their own entry points, the table columns follow one schema, and "kernel" is defined up front. No trade-offs: nothing that helps understanding is cut.

| # | Location | Original | Recommendation | Why |
|---|---|---|---|---|
| 1 | AD-21 Month-step slots cell (spine l.341, 88 words) | The full order of the open phase, the continue phase and month 60 inside one table cell | MOVE the slot order into a numbered list below the table (or into the Order bullet, l.355), grouped Open phase / Continue phase / After month 60. The cell keeps `(slot, order, handler)` with `handler(state, content, month) → state` and 'in the order listed below'. | The hardest passage to scan: about 14 steps read as one run-on cell. About 0 words net, plus about 4 for the pointer. |
| 2 | AD-21 Imports (spine l.336, 128-word unbulleted paragraph) | One paragraph mixing six mechanisms: the FK/relationship rule, the ruff importlib ban, the CI self-test, the ESLint zones and resolver, the fetch ban, the lint fixture | CONDENSE by splitting into labelled sub-bullets like the contracts above it: Backend checks (ruff ban, CI self-test) and Frontend checks (eslint.config.mjs zones and resolver, fetch ban, failing fixture checked in CI). | The densest block in the AD, with no list markers though the lines above have them. 0 words. |
| 3 | AD-21 Imports (spine l.336) | A slice's `models.py` declares foreign keys and `relationship()` only to kernel tables (`users`, `playthroughs`), never to another slice's tables. | MOVE to the State bullet (l.357) or a new Tables sub-bullet beside it. | A data-coupling rule, not an import rule; readers looking for table ownership won't find it here. About 22 words moved. |
| 4 | AD-21 Wiring (spine l.356) | `GET /api/game/quote` lives in `features/credit/api.py`. | MOVE to the Slices bullet (l.330) as a placement example, or to the Capability → Architecture Map. | About where one route lives, not how the kernel is wired. 8 words moved. |
| 5 | AD-21 Wiring (spine l.356) | `PlayerView` is built from named part models, so the generated TS names stay stable. | MOVE into the View parts row (l.350) or the Shared surfaces bullet (l.358). | About view assembly, already covered there. 14 words moved. |
| 6 | AD-21 Shared surfaces (spine l.358, 47 words) | First half repeats the View parts row (Hjem, year end, recap, ending as rendered rows) and the Message actions row (phone thread buttons) | MERGE: keep only 'or from a route in `src/app/` that composes the slices' components' as a frontend clause in the View parts row, or shorten the bullet to that point. | Repeats the table almost exactly; the one new fact gets buried. Saves about 25-30 words. |
| 7 | AD-21 'Used by' column, rows l.342, l.345, l.350 | Rules inside 'Used by': 'start, continue, end early and play again are kernel members'; the selection step 'which alone checks eligibility…'; 'single-winner fields … follow one precedence table in the kernel' | MOVE the rule clauses into a short note under the table or into the matching Rule bullets, so 'Used by' names consumers only, like the Facts and Upcoming costs rows. | The columns don't follow one schema, and binding rules sit where readers expect a list of callers. 0 words net. |
| 8 | AD-21 Shell hooks and CLI, jobs, seeds rows (spine l.352-353) | Shell hooks bundles four hooks; CLI, jobs, seeds bundles three points | QUESTION: split into one row per point, each with its own 'Used by'. | Every other row is one point; the bundled rows make readers untangle semicolon lists. About +10 words. |
| 9 | AD-21 start of Rule (spine l.330) | 'the kernel' is never defined as `shared/` in AD-21 | QUESTION: open the Rule or the Slices bullet with 'The kernel is `shared/` (`backend/app/shared/`, `frontend/src/shared/`); …' | Readers who jump straight to AD-21 meet the term in the title before it is defined. About +12 words. |
| 10 | AD-21 Binds (spine l.327) | backend and frontend code layout, CI; every epic and story (each names its slice) | QUESTION: add the ADs AD-21 extends or constrains (AD-1, AD-4, AD-5, AD-7, AD-8, AD-9, AD-13, AD-15, AD-16, AD-19), as nearby ADs do. | Consistent with the pattern, and shows which decisions the extension points change. About +12 words. |
| 11 | AD-21 Imports (spine l.336) | bans the `fetch` global with `no-restricted-globals` outside `src/shared/api/` | QUESTION: add '(AD-18)'. | The rule is AD-18's; AD-21 only enforces it. +1 word. |
| 12 | AD-21 Slices (spine l.330); Design Paradigm (l.40); Structural Seed (l.475) | The list of 10 slices appears three times | PRESERVE AD-21's list as the authoritative copy (only it maps slices to epics). QUESTION whether l.40 and l.475 should point to AD-21 instead. | Three copies can drift. The l.60 restatement next to the diagram is useful; keep it. |
| 13 | AD-21 DRY by the rule of two (spine l.359) | 62 words | PRESERVE | Overlaps AD-19's 'built in shared/ui/ the first time', but AD-19 cites AD-21 for the general rule, so this is the source. |
| 14 | AD-21 Content is not code (spine l.360) | 33 words | PRESERVE | Looks like a repeat of AD-7, but draws the slice boundary for content; without it readers would make a content folder per slice. |

## Editorial prose (22)

Style to keep: terse specification register, semicolon-chained lists, inline code identifiers, arrows in signatures and rules, Norwegian UI names (Hjem, `/mobil`). The spine leaves out the serial comma and uses British "behaviour"; both look like house choices and are flagged once each, to apply spine-wide or not at all. Fixes for text the structure lens moves travel with that text. Note: the View parts row is l.350, not l.349 (l.349 is Facts).

| # | Location | Original | Revised | Why |
|---|---|---|---|---|
| 1 | AD-21 spine l.337 | cross-slice behaviour goes only through the kernel, never a direct import and never a write to another slice's section of the state. A slice registers into these points, and nothing else: | cross-slice behaviour goes only through the kernel, never through a direct import or a write to another slice's section of the state. A slice registers only into these points: | 'and nothing else' can read as 'nothing else registers'; also makes 'only through … never through' parallel. |
| 2 | AD-21 spine l.356 (Wiring) | `registry.build_kernel()` returns one frozen `Kernel` holding every table | `registry.build_kernel()` returns one frozen `Kernel` holding every registration table | 'table' means database tables at l.336, l.481 and l.485. |
| 3 | AD-21 spine l.331 + l.334 | l.331: CI checks this with import-linter: … l.334: …every slice's `api`, `models`, `jobs` and `cli`, beside AD-1's external-package contracts. | l.331: CI checks this with import-linter, in addition to AD-1's external-package contracts: … l.334: …every slice's `api`, `models`, `jobs` and `cli`. | 'beside' means 'next to'; placed there it seems to belong only to the third contract. |
| 4 | AD-21 spine l.345 (Selection proposers 'Used by'; travels with structure MOVE) | writes the month's pending items and whether it is active or quiet | writes the month's pending items and whether the month is active or quiet | 'it' could be the selection step or the month. |
| 5 | AD-21 spine l.348 (Continue guards) | The continue action, which refuses with `cannot_continue` on the first refusal in order | The continue action, which runs the guards in order and refuses with `cannot_continue` at the first guard that returns a refusal code | 'refuses … on the first refusal' is circular. |
| 6 | AD-21 spine l.330 | and in another slice's folder only as registrations that its Touches line names. | and in another slice's folder only as registrations that the story's Touches line names. | 'its' reads as the other slice's; the Touches line belongs to the story. |
| 7 | AD-21 spine l.336, frontend (travels with structure split) | A lint fixture that breaks each zone must fail, and CI checks that it does. | CI runs a lint fixture that breaks each zone and asserts that ESLint fails on each. | One fixture or one per zone? 'it' has no clear antecedent. Mirrors the backend self-test sentence. |
| 8 | AD-21 spine l.336, frontend | generates one `import/no-restricted-paths` zone per slice from the slice list (target `src/features/<s>` …) … so `@/` paths are seen, | generates one `import/no-restricted-paths` zone per slice `<s>` from the slice list (target `src/features/<s>` …) … so the zones also catch `@/` alias imports, | Defines `<s>` where it first appears; 'paths are seen' is a vague passive. |
| 9 | AD-21 spine l.341 (travels with structure MOVE) | fixed costs (`money` 10, `belongings` 20) … the kernel then runs wellbeing, rule 8 … | fixed costs (`money` order 10, `belongings` order 20) … the kernel then runs the wellbeing step, rule 8 … | Bare numbers aren't explained until l.355; 'runs wellbeing' reads as an action. |
| 10 | AD-21 spine l.341 and l.347 | crisis re-check / crisis recheck | crisis recheck (both) | Two spellings for one step; the spine also has 're-check' twice outside AD-21. |
| 11 | AD-21 spine l.349 (Facts) | derived flags are the facts content may see | Consider: content may see only facts (derived flags), never raw state | 'facts content' can parse as a compound noun. Phrased as a question; meaning not certain. |
| 12 | AD-21 spine l.328 (Prevents) | a change to the card touching the job's code | Consider: a change to the credit card touching the job code in `work` | 'the card' can read as a UI card, 'the job's code' as a scheduled job (l.353). |
| 13 | AD-21 spine l.350 (View parts 'Used by'; travels with structure MOVE) | single-winner fields (`pending`, `continue_warning`, the teaser) follow one precedence table in the kernel | Consider: fields that only one slice's value can fill (`pending`, `continue_warning`, the teaser) are decided by one precedence table in the kernel | 'single-winner fields' is defined nowhere in the spine. |
| 14 | AD-21 spine l.346 (Message actions) | A message kind's buttons (the action member each sends, its label and locked state) as part of its view part | A message kind's buttons (for each button: the action member it sends, its label and its locked state), declared as part of the message kind's view part | Three 'its' point at two things; adds the missing verb. |
| 15 | AD-21 spine l.342 (Actions 'Used by'; travels with structure MOVE) | start, continue, end early and play again are kernel members | the start, continue, end-early and play-again actions are kernel members | Without hyphens and a head noun it reads as instructions. |
| 16 | AD-21 spine l.356 (moved per structure) | so the generated TS names stay stable | so the generated TypeScript type names stay stable | Spells out the abbreviation and says which names. |
| 17 | AD-21 spine l.356 | The engine is `apply(state, action, content, seed, kernel)`. | Consider: The engine's entry point is `apply(state, action, content, seed, kernel)`. | The engine is a package (`shared/engine/`), not one function. |
| 18 | AD-21 spine l.355 (Order) | A test asserts that the orders are unique and stable. | A test asserts that the `order` values are unique and stable. | 'the orders' can mean sequences or the constants. |
| 19 | AD-21 spine l.360 (Content is not code) | the content data stays in the repo-root `content/` by kind (AD-7) | the content data stays in the repo-root `content/` folder, organized by kind (AD-7) | 'stays … by kind' reads as a condition. Light edit; the passage is PRESERVE in structure. |
| 20 | AD-21 spine l.328, 334, 341, 343, 344, 345, 350 | 'built, reviewed or cut alone'; 'collects, filters and applies them' | Consider spine-wide: 'built, reviewed, or cut alone'; 'collects, filters, and applies them' | The Microsoft style guide requires the serial comma; the spine leaves it out almost everywhere, so apply spine-wide or not at all. |
| 21 | AD-21 spine l.337 | behaviour | behavior | US spelling per the Microsoft style guide; the spine uses 'behaviour' twice, so spine-wide or not at all. |
| 22 | AD-21 spine l.331 | a slice imports only itself | a slice imports only its own modules | Clearer subject of the import. |
