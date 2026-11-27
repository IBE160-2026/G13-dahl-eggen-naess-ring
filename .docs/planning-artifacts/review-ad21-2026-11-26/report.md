---
title: Review of AD-21 (vertical slices with a shared kernel)
date: 2026-11-26
method: bmad-review, lenses adversarial + edge-case-hunter
content: commit 2315bd7 (ARCHITECTURE-SPINE, SOLUTION-DESIGN, DESIGN, diagram 03, epics.md, sprint-change-proposal-2026-11-26)
findings: 53 (adversarial 23, edge-case-hunter 30)
raw: findings.json
---

# Review of AD-21 (2026-11-26)

Unranked findings, as the review method requires. Each lens ran on its own, without seeing the other's findings, so overlap between them is signal.

## Overlap between the lenses

Both lenses found these on their own:

- **Missing extension points.** The five named points (month-step slots, action union, view parts, derived flags, the account-deletion hook) don't cover what the stories need:
  - typed option effects that change another slice's facts
  - crisis options from four slices
  - wellbeing changes from money, work and credit
  - an after-action recheck and continue guards
  - a sign-up check
  - upcoming costs from several slices
  - seeds and daily jobs
- **Kernel tables placed in slices.** `users`, `sessions` and `seen_disclosures` are owned by slices, but the shared auth dependency, pipeline and view must read them.
- **How shared gets registry's types.** The shared routes need the action union and view types, which only `registry.py` builds, and shared cannot import it.
- **No order inside a slot.** Several slices write to the same rule 1 slot with no order between them, and the "no handler" test has no slot-to-owner map.
- **Story 1.1 can't show its checks fail.** One example slice means the independence contract can never fail. Engine purity covers only external packages. Tests inside `app/` that import `app.main` create indirect chains the contracts reject. The ESLint zones need the TypeScript resolver, and `fetch` is a global that the zones can't ban.
- **The epics disagree with themselves.** The Epic 2 notes, the slice table and the Slice lines of 2.2-2.7 disagree on which stories build the kernel. The inventory's AD-4 and Tests bullets are out of date.
- **The deletion hook has no contract.** It doesn't say when it runs or what it receives.
- **Shared UI pieces start in one slice.** The scene, mirror and timeline are built in a slice although several slices use them.


## Adversarial

### Adversarial 1
- **Location:** ARCHITECTURE-SPINE.md AD-21 Extension points; AD-16 Rule ('an option changes such a fact only through its typed effect'); epics.md Stories 2.5, 3.3, 5.4, 6.6, 7.4, 8.2, 8.4
- **Problem:** Options owned by one slice carry typed effects that change facts owned by other slices, and none of the listed extension points covers this. Event options (life) start or stop everyday costs (money, 3.3), offer extra shifts (work, 6.6) and family loans (credit, 7.4). Open options (phone) sell the moped licence (belongings, 8.2). Family messages give a moped (belongings, 8.4).
- **Fix:** Add a 'typed effect handlers' extension point to AD-21. Each slice registers its effect kinds as `effect_kind -> (possible(state, content) -> bool, apply(state, effect, cause) -> state)`, which may write only its own section. The shared option applier used by events, open options and crisis steps dispatches through the registry. Name it in Stories 2.5, 5.4, 6.6, 7.4, 8.2 and 8.4.
- **If shipped as-is:** The first event option that starts extra shifts or buys a licence forces life or phone either to import work or belongings (CI fails) or to write their state section directly. That breaks AD-21's 'never writes another slice's section', and developers will invent ad-hoc workarounds.

### Adversarial 2
- **Location:** epics.md Story 7.7 (credit) and Story 8.3 ('selling it is also a crisis option'); PRD FR-32b 'Options that work'
- **Problem:** The FR-32b crisis options belong to four slices: selling (belongings), extra shifts and taking a job (work), lowering spending and withdrawing BSU (money), payment plan and card off (credit). Each must say whether it is possible now and when it lands. 8.3 adds selling to credit's crisis menu one epic after credit was built. No crisis-option extension point exists.
- **Fix:** Add 'crisis option providers' to AD-21. Each slice registers `crisis_options(state, content, month) -> list[CrisisOption(id, possible, lands_month, effect)]`. Credit's crisis step only collects them, filters those landing after month 60, and applies them through the typed effect handlers. Reference it in 7.7 and 8.3.
- **If shipped as-is:** 7.7 cannot meet its 'only options possible now, each saying when it lands' criterion without importing work, money and belongings. 8.3 cannot add selling without editing credit's code. Either way the boundary check or the isolation promise breaks on the most coupled story in the game.

### Adversarial 3
- **Location:** ARCHITECTURE-SPINE.md layer table (wellbeing dropped from the shared engine list); Structural Seed `life/ ... wellbeing`; epics.md Stories 2.7, 3.3, 6.2, 7.4; PRD FR-33
- **Problem:** Wellbeing now belongs to the life slice, but other slices change it. Money changes social life (spending Lite -2 / Mye +2, 3.3). Work changes stress and social life (activities +-15 and the 'Vanligvis n' tile, 6.2). Credit raises stress (postponed family-loan instalments, 7.4; crisis months and debt interest, FR-33). AD-9 also keeps per-choice wellbeing totals in the shared ledger.
- **Fix:** Make wellbeing a kernel writer like the ledger: `shared/engine/wellbeing.py` with `apply_effect(state, part, delta, cause, scope='month'|'base')` as the only writer. Life keeps rule 12's weighting and view part, and other slices call the shared writer. Alternatively, each slice registers a wellbeing-contribution provider that life's rule 12 slot sums. Pick one, put it in AD-21, and correct the layer table.
- **If shipped as-is:** Three later slices must write life's state section, which AD-21 forbids, or import life's wellbeing code, which CI forbids. The probable outcome is a quietly duplicated wellbeing formula or an exception nobody recorded.

### Adversarial 4
- **Location:** epics.md Story 4.4 (year: loss = rule 8 trigger true at months 59 and 60), Story 7.5 (credit builds rule 8 triggers), Story 2.6 (life sets `completed` after month 60); AD-21 slot list
- **Problem:** The year slice's ending check (Epic 4) needs the rule 8 trigger evaluation that the credit slice builds in Epic 7, and year cannot import credit. The ending check runs after rule 8 and close_month(60), and none of the listed rule 1 slots covers that point. Who sets `completed` and stores the ending is split between 2.6 (life) and 4.4 (year).
- **Fix:** Put rule 8 trigger evaluation in `shared/engine/` from Story 4.4 (credit's 7.5 adds crisis handling around it), or state that 4.4 builds it in shared. Add post-month phases after the rule 1 slots to AD-21: `after_close` (ending check, year_end flag) and `life_completed`, each with one named owner. Fix 2.6 and 4.4 so only one slice writes playthrough status and ending.
- **If shipped as-is:** 4.4 cannot be built as written without importing a slice that doesn't exist yet. Or the trigger logic gets built twice (year in Epic 4, credit in Epic 7) and drifts, giving a loss ending that disagrees with the crisis band (FR-32a vs FR-41).

### Adversarial 5
- **Location:** ARCHITECTURE-SPINE.md layer table (shared shell holds 'the auth dependency'; `account` holds 'passwords, sessions, ...'); AD-4 Lock order; Consistency 'users.last_active_at written only by the auth dependency'
- **Problem:** The shared auth dependency and pipeline must read and lock `users` and `sessions`, re-read them after the lock, and write `users.last_active_at`. They must also lock the playtest record. But sessions belong to features/account and records to features/playtest, so shared cannot import their models.
- **Fix:** Move the `users` and `sessions` models and session verification (JWT check, sliding expiry) to `shared/persistence/models` and `shared/api/auth.py`. Account keeps the flows: sign-up, login, reset, password change, deletion. For the playtest record lock, add a registered `extra_locks` hook that the pipeline calls after the playthrough lock. Update the layer table and Structural Seed.
- **If shipped as-is:** Story 2.2's pipeline and Story 1.4's auth dependency fail the `forbidden app.shared -> app.features` contract the day they are written. Otherwise teams duplicate session models or skip the lock, breaking AD-4's deadlock-free lock order.

### Adversarial 6
- **Location:** ARCHITECTURE-SPINE.md AD-13 `view(state, content, last_action_at, seen_disclosure_ids, nickname)`; Structural Seed `explain/ ... disclosures + seen_disclosures`; epics.md Story 9.3
- **Problem:** The shared view needs `seen_disclosure_ids` from a table that the spine puts in the explain slice, and the nickname from account's `users` table. Shared `/api/game` therefore cannot load its own view inputs.
- **Fix:** Either keep `seen_disclosures` in `shared/persistence/models` (it is per-account kernel data, AD-5), or add a registered 'view input loader' extension point that `GET /api/game` and the pipeline call. State which in AD-21 and Story 9.3.
- **If shipped as-is:** Story 9.3 cannot feed the view without shared importing explain, or the disclosure ids get passed in some ad-hoc way per route. FR-40's 'never shown again on any device' then becomes inconsistent across endpoints.

### Adversarial 7
- **Location:** epics.md Story 1.8 (Slice `playtest`) vs Story 1.3 (account sign-up); AD-15 `users.is_test` set by CLI
- **Problem:** The playtest slice must refuse sign-ups inside account's sign-up flow and set `users.is_test` on account's table, but no sign-up hook exists. Story 1.8 is also in Epic 1 while the slice table maps `playtest` to Epic 10 only.
- **Fix:** Add an `on_sign_up_check(normalized_email) -> AppError | None` extension point, registered by playtest through registry.py and called by account's sign-up. Or move the tester gate to the account slice. Put `is_test` in the shared users model and give its CLI command an owner. List 1.8 in the slice table.
- **If shipped as-is:** Story 1.8's refusal can only be built by account importing playtest (CI fails) or by copying the `tester_codes` lookup into account. The second breaks AD-15's 'nothing else stores or matches codes'.

### Adversarial 8
- **Location:** ARCHITECTURE-SPINE.md AD-8 (one selection step) and AD-21 Extension points; epics.md Stories 6.2, 6.3, 6.4, 6.6, 7.1, 7.5, 7.6, 8.4, 9.5
- **Problem:** The phone slice owns the inbox, but other slices produce messages and need action buttons on them. Work: job offers, hours answers, invitations with «Legg i planen», a summer job with the cap full. Credit: card offer with cost. Belongings: gift moped. Explain: bank messages for the savings target. Credit also changes life's event state: the card warning 'makes a quiet month active' (7.6), and a skipped crisis re-chooses the month's event (7.5). There is no proposer or message-kind registration, and nothing for actions on a message.
- **Fix:** Add 'selection proposers' to AD-21. Each slice registers drawn and triggered proposers (event, message, shift, crisis event, card warning) into the shared selection step, which alone writes the month's pending items and active-or-quiet status. Add a 'message action' view part, and render a message's buttons through a slot that the `/mobil` route in `src/app/` fills.
- **If shipped as-is:** Phone's message screen ends up importing work and credit components, or work and credit write phone's section. Card warning and crisis skip then mutate life's pending state behind AD-8's back. The 'one selection step' rule erodes in Epics 6 to 9.

### Adversarial 9
- **Location:** epics.md Slice lines 9.1-9.5 (`explain`); AD-21 Slices
- **Problem:** Explain is cross-cutting, not a vertical slice. «Hvorfor?» (9.1) sits on results and money changes in life, money and credit screens. «Tidligere valg» (9.2) sits on the hub and the bank. «Forenklet» (9.3) sits under every screen heading. 9.4 lists next month's costs, which requires money, credit and belongings cost rules. 9.5 reacts when an option is taken, gifted or closed.
- **Fix:** Build the «Hvorfor?», «Tidligere valg» and «Forenklet» components in `frontend/src/shared/ui/` and their view data in the shared view (mark 9.1-9.3 as `shared` plus explain). For 9.4, add a 'projected costs' provider each slice registers. For 9.5, add an engine-level post-action reaction hook (domain event) to the extension points.
- **If shipped as-is:** Every explain story either imports explain components into other slices (ESLint zones fail) or re-implements fixed-cost, instalment and moped rules in explain. FR-57's upcoming costs then disagree with what the month actually charges.

### Adversarial 10
- **Location:** AD-21 Prevents ('a change to the card touching the job's code'); epics.md Stories 8.3, 3.3, 6.2, 8.1
- **Problem:** Several stories have to edit another slice's code even with no import. 8.3 (belongings) charges moped costs 'instead of the transport ticket' in money's 3.3 fixed-cost rule. 6.2 (work) changes life's wellbeing tile. 8.1 (belongings) adds layers to life's mirror scene from 2.3. 3.3's 'Mye gives nothing in a month with debt interest' reads credit. The Slice line hides these edits.
- **Fix:** Add a '**Touches:**' line to each story naming other slices and kernel files it edits. Rewrite 8.3 so belongings registers its own fixed-cost handler and money's transport cost checks a derived flag (`owns_moped`) that 3.3 reads from the start. Move the mirror and timeline to `shared/ui` in 2.3.
- **If shipped as-is:** Reviewers read the Slice line as the story's footprint and miss edits to other slices. The isolation AD-21 promises (cut or review a slice alone) doesn't hold for exactly the stories that are 'Can be cut'.

### Adversarial 11
- **Location:** ARCHITECTURE-SPINE.md AD-21 Extension points (slot list, 'a test fails if a rule 1 slot has no handler once its slice exists')
- **Problem:** Several slices register handlers in the same slot, with no order inside the slot. Fixed costs: money, moped insurance and fuel, car fuel. Income: wages, one-off shifts, a summer job sharing the 173 h cap. Debt step: consumer loan, family loan, payment plan, card. Event and choices: life event, crisis, card warning. Order inside a slot decides the FR-45 payment order, the rule 10 cap and replay determinism. Slot-to-slice ownership is also undefined, and month-open versus continue phases are missing.
- **Fix:** Add a slot table to AD-21 with: slot, phase (open or continue), owning slices, and in-slot order as explicit priority constants (e.g. `FIXED_COSTS: money=10, belongings=20`). A slot may have several handlers. 'Slice exists' means the slice has registered at least one action. A test asserts the order is total and stable.
- **If shipped as-is:** Two developers register handlers in import order. A registry import reorder then changes which payment drives the account below zero, which flips rule 8 triggers and breaks replay (FR-12). Or the 'no handler' test fails from Story 1.1, because the scaffold creates all ten folders.

### Adversarial 12
- **Location:** epics.md Story 1.1 CI criterion ('one empty example slice'); sprint-change-proposal success criterion 'CI fails on an import from one slice into another'
- **Problem:** An import-linter `independence` contract over one module is always satisfied, so CI cannot fail on a slice-to-slice import as claimed. Nothing proves the contracts catch a planted violation. It is also unclear whether the example slice is one of the ten names or is deleted later.
- **Fix:** Scaffold two stub slices (e.g. `account` and `life`, each with an empty `engine/`). Add a CI self-test that writes planted violations into a temp copy (features.a -> features.b, shared -> features, features.a.engine -> fastapi or random) and asserts `lint-imports` exits non-zero for each. Do the same for ESLint with a fixture file expected to error. Say the stubs are real slices, not a throwaway `example`.
- **If shipped as-is:** A wrong wildcard (`app.features.*` matching nothing, or the engine subpackage missing) passes green from day one. Slices start depending on each other unnoticed until a story's CI suddenly fails or never does.

### Adversarial 13
- **Location:** ARCHITECTURE-SPINE.md Consistency 'Tests' (`backend/app/features/<slice>/tests/`, `backend/app/shared/tests/`); AD-4 'a test posts one valid request per action member through the real app'; Story 2.10 'every endpoint a later story adds'
- **Problem:** Tests that build the real app import `app.main`, which imports registry and every slice. Placed inside `app.shared` or `app.features.<slice>`, they create indirect imports shared -> features and slice -> slice. import-linter's independence and forbidden contracts check indirect chains, so legitimate tests fail CI. If the test folders skip `__init__.py` to dodge this, pytest's default import mode fails on duplicate basenames (e.g. `test_api.py` in ten slices).
- **Fix:** Keep integration and API tests in `backend/tests/<slice>/`, outside the `app` package. Or add explicit `ignore_imports` (e.g. `app.**.tests.** -> app.main`) to every contract, and set pytest `--import-mode=importlib`. Write the choice into the Tests convention and Story 1.1.
- **If shipped as-is:** The first DB-backed test in Story 1.3 or 2.2 turns CI red against the contracts, and the team silences them with broad ignores, so the boundary check stops meaning anything.

### Adversarial 14
- **Location:** ARCHITECTURE-SPINE.md Design Paradigm ('a slice's engine imports only its own engine and shared.engine', 'not even settings'); AD-21 Imports contract list
- **Problem:** The listed contracts (independence, forbidden shared -> features, AD-1's external-package bans) do not catch a slice engine importing `app.settings`, `app.shared.content` (pyyaml), its own `cli`, or `app.registry`, because none of these pull in a banned external package. The stated purity rule is wider than what CI checks.
- **Fix:** Add a forbidden contract with source `app.shared.engine` and `app.features.*.engine`. Its forbidden modules: `app.settings`, `app.main`, `app.cli`, `app.registry`, `app.shared.content`, `app.shared.persistence`, `app.shared.api`, `app.shared.jobs`, and `app.features.*.api`, `.models`, `.jobs`, `.cli`. Or use a `layers` contract per slice with `containers = app.features.*`.
- **If shipped as-is:** Engine code reads settings or loader helpers directly, which defeats 'content and seed are passed in' (AD-1). Engine tests then need environment setup, while CI stays green.

### Adversarial 15
- **Location:** ARCHITECTURE-SPINE.md AD-21 Imports (frontend) and Lint convention; epics.md Story 1.2 CI criterion; Structural Seed `frontend/src/test/fixtures/`
- **Problem:** `import/no-restricted-paths` cannot say 'features/X not features/Y' generically. It needs one zone per slice with `except`, kept in sync with ten names. It only fires on imports its resolver can resolve, so `@/` aliases need the TypeScript resolver. It cannot ban `fetch`, a global call the spine attributes to the same zones. Vitest tests in `features/*` importing `src/test/fixtures/` would also be refused. Story 1.2 has no frontend example slice and no expected-failure test.
- **Fix:** Generate the zones from the slice list in `eslint.config.mjs`: for each slice, `target: ./src/features/<s>`, `from: ./src/features`, `except: ['./<s>']`, plus `shared` -> {features, app} denied. Set `import/resolver: { typescript: true }`. Ban `fetch` with `no-restricted-globals` and `no-restricted-properties` outside `src/shared/api/`. Move fixtures to `src/shared/test/fixtures/`. Add a lint fixture expected to error.
- **If shipped as-is:** Aliased cross-feature imports pass lint silently, or the fixtures zone blocks every component test. The frontend half of AD-21 then gives a false sense of isolation.

### Adversarial 16
- **Location:** ARCHITECTURE-SPINE.md AD-4 ('joined into one union by registry.py', `TypeAdapter(GameRequest).validate_json`, 'OpenAPI schema comes from the same adapter'); layer table (shared/api holds `POST /api/game/actions` and `GET /api/game`)
- **Problem:** The action union and the view parts exist only once registry.py runs. The shared routes need `GameRequest` and the response `PlayerView` types when the router is defined, for validation, OpenAPI and the committed `openapi.json` staleness check, and shared cannot import registry. The mechanism is unspecified. Ownership of `GET /api/game/quote` is not stated either.
- **Fix:** State it in AD-21: `shared/api/game.py` exposes `build_game_router(game_request_type, player_view_type)`, and `main.py` calls it with the types from registry. `PlayerView` is built with stable model names (one named part model per slice) so generated TS type names don't churn. The quote route lives in `features/credit/api.py` and is covered by 2.10's two-player tests.
- **If shipped as-is:** Developers import registry from shared/api, creating a cycle and failing the forbidden contract. Or they build anonymous models dynamically, so `openapi.json` and the generated TS types change names on unrelated PRs and the staleness check flaps.

### Adversarial 17
- **Location:** ARCHITECTURE-SPINE.md layer table ('State document model (one section per slice, data only)' and 'derived flags (AD-16)' in shared/engine); AD-16 'computed ... by one engine function'; epics.md slice table row `shared` ('built by Stories 1.1, 1.2, 2.1 and the parts of Epic 2...')
- **Problem:** Every slice's state section and the single derived-flag function sit in `shared/engine`. So nearly every story in Epics 3 to 9 edits shared files (state model, AD-5 state upgrades, flags.py). That contradicts the table saying shared is built in Epics 1-2. AD-21 also calls derived flags an extension point, while AD-16 says one function.
- **Fix:** Pick one approach for derived flags. Either flags stay one function in `shared/engine/flags.py` that later stories extend, or each slice registers a flag provider and AD-16's text changes. Rewrite the `shared` row to say later stories add their own state section and flags under `shared/engine/state/<slice>.py`. Add a Touches line (see the earlier finding).
- **If shipped as-is:** Shared becomes a merge-conflict hotspot that every PR touches. Sprint estimates based on 'code goes in its slice' are wrong, and AD-16 and AD-21 give two builders incompatible instructions for the same flag.

### Adversarial 18
- **Location:** epics.md Epic 2 Notes ('Stories 2.1-2.8 build the kernel in shared/') vs Slice lines 2.2-2.7 (`life`); slice table `shared` row vs sprint-change-proposal Proposal 4 (`shared`: 1.1, 1.2, 2.1, 2.8, 2.9, 2.10, 8.11)
- **Problem:** The three sources disagree about which stories build the kernel. Stories labelled `life` build kernel parts. 2.2 builds the pipeline, the envelope, the game store and the focus manager. 2.3 builds the ledger, draws and the reusable mirror and timeline. 2.5 builds cause links and the result gate. 2.6 builds the month loop and the selection step.
- **Fix:** Allow a two-part Slice line (e.g. 2.2 `shared (pipeline, envelope, store, focus manager) + life (start, goal)`), or relabel 2.2, 2.3, 2.5 and 2.6 as `shared`. Make the Epic 2 Notes, the slice table and Proposal 4 list the same stories.
- **If shipped as-is:** Developers put the pipeline or month loop under `features/life`. Every later slice then needs to import life, and CI forbids it, so a large move to shared lands mid-Epic 3.

### Adversarial 19
- **Location:** AD-21 'DRY by the rule of two'; epics.md Stories 2.3 (mirror, timeline), 4.1 (FR-18 unlock table), 4.4, 5.3, 8.1
- **Problem:** Pieces that are known up front to have several users get built inside one slice and must move to shared later, in a story about something else. Examples: the mirror and timeline (2.3, life), later used by the ending (year, 4.4) and room layers (belongings, 8.1); the unlock table (4.1, year), later used by phone (5.3). No story's criteria mention the move or its test changes.
- **Fix:** In AD-21 or the Epic 2 Notes, list the pieces known to be shared and build them in `shared/` the first time: mirror scene, timeline, result and outcome list, unlock table, rule 8 triggers, «Hvorfor?». Add 'moves X to shared' to the criteria of 4.4, 5.3 and 8.1 where it remains.
- **If shipped as-is:** Later stories carry unplanned refactors of earlier slices' code and tests, or copy the code to dodge the move, which is exactly what the rule of two forbids.

### Adversarial 20
- **Location:** ARCHITECTURE-SPINE.md AD-15 Account deletion / AD-21 on-account-deleted hook
- **Problem:** The hook's contract is undefined. It doesn't say where the hook list lives (playtest can't register into account), whether hooks run before or after `DELETE ... RETURNING`, or what they receive. Counting `testers_left` needs the removed row's normalized address and `is_test`, which exist only in that RETURNING.
- **Fix:** Define it in AD-21: `shared/persistence/hooks.py: on_account_deleted: list[Callable[[AsyncSession, DeletedUser], Awaitable[None]]]`. Hooks run after the `DELETE ... RETURNING` in the same transaction and receive `DeletedUser(user_id, normalized_email, is_test, removed: bool)`. registry.py appends playtest's hook.
- **If shipped as-is:** Playtest's hook runs before the delete (it counts accounts that weren't removed) or after without the address (it can't match `tester_codes`). The sign-up limit (FR-50, #125) then drifts during the playtest.

### Adversarial 21
- **Location:** AD-21 Extension points; registry.py description; epics.md Stories 2.9, 7.1, 7.7, 10.5 (Slice `playtest`), 1.7 daily jobs
- **Problem:** Seeded users added by later slices (7.1 and 7.7 in credit, 10.5 in playtest) and slice daily jobs (account's session, attempt and inactivity cleanup) need registration with the shared seed CLI and job runner. Neither is among the extension points. 10.5's examiner seeds sit in the `playtest` slice, although AD-15 gates everything playtest-only by `PLAYTEST_RECORDS` and seeds are gated by `APP_ENV`.
- **Fix:** Add 'seed scenarios' and 'daily jobs' to AD-21's extension points and to registry.py's list. Move 10.5 to a seeds module of the slice whose state it targets, or to `shared`, so the examiner's seeds don't live in the playtest slice.
- **If shipped as-is:** Developers wire jobs and seeds by importing slices from shared (CI fails), or the examiner's month-59 seeds end up conditioned on the playtest switch and vanish from the local run (NFR-6).

### Adversarial 22
- **Location:** epics.md Requirements Inventory: AD-4 bullet and Tests bullet
- **Problem:** The inventory still says '`action` a discriminated union of the engine's action models' (no registry.py, no 'no second union anywhere') and 'the import-boundary check' in the singular, with no slice or kernel test locations. The spine was updated on both points.
- **Fix:** Change the AD-4 bullet to 'a discriminated union of the slices' engine action models joined by registry.py (AD-21)'. Change the Tests bullet to 'the import-boundary checks (AD-1, AD-21)' and add the slice and kernel test locations.
- **If shipped as-is:** Story writers who work from epics.md alone define the union in the wrong place and miss where tests go. It also fails the proposal's own success criterion that the documents agree.

### Adversarial 23
- **Location:** SOLUTION-DESIGN.md §2 diagram, §10 'Why these choices', §12 'How this was checked'
- **Problem:** AD-21 gets one bullet and one sentence. §10 has no row weighing the alternatives (horizontal layers, later slices importing earlier ones, one slice per mechanism). §12 records no review of AD-21. §2's diagram doesn't show the kernel and slices. SOLUTION-DESIGN says the examiner should read §§1, 2, 8 and 10.
- **Fix:** Add a §10 row: 'Vertical slices with a shared kernel | horizontal layers; slices importing earlier slices; one slice per mechanism | ...why, and the cost: a large kernel built in Epics 1-2'. Add a §12 entry for this review. Mention the kernel and slice split in §2.
- **If shipped as-is:** The examiner sees a major structural decision with no stated trade-off. The rejected alternatives are recorded only in a .memlog, which CLAUDE.md marks as history.

## Edge-Case Hunter

### Edge-Case Hunter 1
- **Location:** ARCHITECTURE-SPINE.md:39-40, 89-90, 208
- **Problem:** Shared auth dependency, pipeline locks and view need account's users/sessions and explain's seen_disclosures tables
- **Fix:** Keep users, sessions and seen_disclosures models in shared/persistence/models/, or have registry inject loader callables (load_session, load_nickname, load_seen_ids) into shared at startup
- **If shipped as-is:** The forbidden shared-to-features contract fails from Story 2.8/2.10 on, or models get duplicated.

### Edge-Case Hunter 2
- **Location:** epics.md:1806-1809 (Story 7.7); ARCHITECTURE-SPINE.md:332
- **Problem:** Crisis options sell moped, take job/extra shifts, lower spending, withdraw BSU belong to other slices
- **Fix:** Add kernel point: slices register crisis option providers {kind, available(state, content), lands_month(state), apply(state)}; credit only counts steps and rechecks
- **If shipped as-is:** Credit imports work/money/belongings or writes their state sections, which breaks AD-21.

### Edge-Case Hunter 3
- **Location:** epics.md:1612 (6.6), 1729 (7.4), 1528 (6.3), 1655 (7.1); Epic 5 notes
- **Problem:** Life's event options and phone's open options trigger work/credit/belongings effects (extra shifts, family loan, job, card)
- **Fix:** Shared effect-handler table keyed by effect kind; life/phone dispatch each option effect through it, and the owning slice registers the handler
- **If shipped as-is:** Option handlers write another slice's section, or every new effect edits life/phone.

### Edge-Case Hunter 4
- **Location:** epics.md:1505-1508 (6.2), 1737 (7.4)
- **Problem:** Work's activities and credit's moved family instalment change stress/social, which belong to life's wellbeing
- **Fix:** Shared per-month wellbeing_effects list in state that any slice appends {part, delta, cause}; only life's wellbeing slot folds it in
- **If shipped as-is:** Work and credit write life's section directly, which the rule forbids.

### Edge-Case Hunter 5
- **Location:** epics.md:1809 (7.7); ARCHITECTURE-SPINE.md:332
- **Problem:** Credit must recheck triggers after money, phone and work actions taken in a crisis month
- **Fix:** Add an engine after_action hook list in shared apply(); credit registers recheck_triggers and the rule 8 money-in order there
- **If shipped as-is:** No named extension point covers it, so the recheck is skipped or slices import credit.

### Edge-Case Hunter 6
- **Location:** epics.md:881 (2.6), 1813 (7.7)
- **Problem:** cannot_continue raised by credit's unfinished crisis, but the continue action is owned by life
- **Fix:** Shared continue_guards registry: each slice returns an optional refusal; the continue handler refuses on the first non-null result in a fixed order
- **If shipped as-is:** Life must read crisis rules itself, or continue proceeds mid-crisis.

### Edge-Case Hunter 7
- **Location:** epics.md:1485 (6.1); ARCHITECTURE-SPINE.md:87
- **Problem:** Work story adds required plan_version to the continue member that Story 2.6 builds in life
- **Fix:** Define the continue action model and the plan_version counter in shared/engine, not in features/life
- **If shipped as-is:** A work-slice PR edits life's action model and breaks the slice ownership rule.

### Edge-Case Hunter 8
- **Location:** ARCHITECTURE-SPINE.md:332
- **Problem:** Slot test runs 'once its slice exists'; no slot-to-slice map; slots filled mid-epic
- **Fix:** Shared SLOT_OWNERS = {slot: (slice, story)}; test asserts a handler only when the owning story is marked done
- **If shipped as-is:** CI fails in Story 3.1 (unexpected-expense slot empty until 3.5) or the test checks nothing.

### Edge-Case Hunter 9
- **Location:** ARCHITECTURE-SPINE.md:332
- **Problem:** Several slices register in one slot: fixed costs (money 3.3, belongings 8.3), December BSU (money/work)
- **Fix:** Order handlers by an explicit (slot, order_key) declared in shared, never by registry import order; test that the order is stable
- **If shipped as-is:** The FR-45 payment sequence and replay results change when registry imports are reordered.

### Edge-Case Hunter 10
- **Location:** ARCHITECTURE-SPINE.md:333; epics.md:1180-1181, 1587
- **Problem:** Year end and recap rows come from year, work and phone; teaser and pending are single-valued fields
- **Fix:** Per-surface named row slots with fixed order in shared view assembly, plus explicit precedence for single-winner fields (teaser, pending, continue_warning)
- **If shipped as-is:** Row order and teaser winner are undefined, so fixtures and screens drift between builds.

### Edge-Case Hunter 11
- **Location:** epics.md:2161-2176 (9.4)
- **Problem:** Explain's upcoming costs need next-month costs from money, credit, belongings and work
- **Fix:** Add an upcoming_costs provider per slice in registry, or compute the list from a shared month-loop projection; list it among AD-21 shared surfaces
- **If shipped as-is:** Explain imports four slices, or FR-57 (Core, never cut) shows incomplete costs.

### Edge-Case Hunter 12
- **Location:** ARCHITECTURE-SPINE.md:358, 331
- **Problem:** Slice or shared tests import app.main for real-app tests (AD-4 per member, 2.10)
- **Fix:** Put real-app tests outside app/ (backend/tests/integration), or add ignore_imports '*.tests.** -> app.main' to the independence and forbidden contracts
- **If shipped as-is:** import-linter's indirect-chain check fails CI (features.X->main->registry->features.Y), or tests are excluded silently.

### Edge-Case Hunter 13 (deletion, high confidence)
- **Location:** ARCHITECTURE-SPINE.md:447 (removed backend/tests/)
- **Problem:** Old top-level tests/ was the home for cross-layer worked examples, replay and reconciliation
- **Fix:** Re-add backend/tests/ at composition-root level for worked examples spanning slices (WE 25, 27), replay, AD-9 reconciliation, seed assertions
- **If shipped as-is:** Cross-slice tests can't live in a slice or in shared without breaking the contracts.

### Edge-Case Hunter 14
- **Location:** ARCHITECTURE-SPINE.md:42, 87, 208; epics.md Story 8.11
- **Problem:** Shared pipeline, TypeAdapter route, month loop, view and content-check runner need registry's tables
- **Fix:** registry.build_kernel() returns a Kernel; create_app(kernel), pipeline(kernel, ...), apply(state, action, content, seed, kernel); no module-level registration in shared
- **If shipped as-is:** Global mutable registration makes the engine depend on import order; shared importing registry fails CI.

### Edge-Case Hunter 15
- **Location:** ARCHITECTURE-SPINE.md:269; epics.md:655, 2229
- **Problem:** The testers_left hook needs 'row removed', the normalized address and is_test, but the hook signature is undefined
- **Fix:** on_account_deleted(conn, user_id, removed: bool, normalized_email, is_test), called after DELETE ... RETURNING in the same transaction
- **If shipped as-is:** A hook called before the delete or on a re-run job double-counts, or can't join tester_codes.

### Edge-Case Hunter 16
- **Location:** epics.md:678-684 (1.8)
- **Problem:** Playtest slice must refuse account's sign-up and set users.is_test on account's table
- **Fix:** Add a sign_up_guards hook in account that playtest registers via registry, or put the tester-code check in account behind PLAYTEST_RECORDS
- **If shipped as-is:** No named extension point exists, so account imports playtest or the gate is skipped.

### Edge-Case Hunter 17
- **Location:** epics.md:476 (Story 1.1 CI criterion)
- **Problem:** An independence contract over one empty example slice; slice name and lifetime unspecified
- **Fix:** Scaffold two stub slices with engine/ subpackages, plus a CI self-test that plants a cross import and asserts lint-imports exits non-zero
- **If shipped as-is:** The contract can never fail (import-linter may also reject it), so violations go unnoticed until Epic 2.

### Edge-Case Hunter 18
- **Location:** ARCHITECTURE-SPINE.md:60, 68
- **Problem:** 'Engine imports only engine packages, not even settings' is not covered by the listed contracts
- **Fix:** forbidden: source app.shared.engine, app.features.*.engine -> app.settings, app.shared.(api|persistence|content|jobs), app.features.*.(api|models|jobs|cli)
- **If shipped as-is:** An engine importing settings or shared.content passes CI, because only external packages are banned.

### Edge-Case Hunter 19
- **Location:** ARCHITECTURE-SPINE.md:331
- **Problem:** importlib.import_module or string-based SQLAlchemy relationship() across slices on one Base
- **Fix:** ruff banned-api on importlib.import_module and __import__ under app/features and app/shared; review rule: no cross-slice relationship() strings
- **If shipped as-is:** Hidden cross-slice coupling passes import-linter without being flagged.

### Edge-Case Hunter 20
- **Location:** ARCHITECTURE-SPINE.md:331, 356
- **Problem:** 'fetch only in shared/api/' is assigned to import/no-restricted-paths, but fetch is a global
- **Fix:** no-restricted-globals: ['error', 'fetch'] with an override that turns it off for src/shared/api/**
- **If shipped as-is:** fetch in a feature component passes lint.

### Edge-Case Hunter 21
- **Location:** epics.md:694 (Story 1.2 CI); ARCHITECTURE-SPINE.md:356
- **Problem:** Imports via the @/ alias that the import resolver can't resolve
- **Fix:** settings: {'import/resolver': {typescript: {project: 'tsconfig.json'}}}, one zone per slice (target features/X, from features, except ./X), and a planted-violation lint test
- **If shipped as-is:** Unresolved aliased cross-feature imports are skipped silently, so the zones enforce nothing.

### Edge-Case Hunter 22 (deletion, medium confidence)
- **Location:** ARCHITECTURE-SPINE.md:41-46 (removed 'Frontend: UI ... the scene SVGs' row)
- **Problem:** The scene SVGs (AD-19) had a home; the mirror mixes avatar (life), room (belongings) and stickers
- **Fix:** Place the scene in shared/ui/scene with named group slots that src/app routes fill from the life, belongings, phone and work components
- **If shipped as-is:** The scene has no owner; the mirror or year end forces a feature-to-feature import.

### Edge-Case Hunter 23 (deletion, medium confidence)
- **Location:** ARCHITECTURE-SPINE.md:438 (cli.py comment)
- **Problem:** The old cli.py list named clear-game-data; the new list and the slices omit it
- **Fix:** cli.py # schema upgrade, seed, dump view fixtures, clear-game-data (AD-7), plus each slice's commands
- **If shipped as-is:** Story 10.3 (Slice: content) runs a command no slice or story builds.

### Edge-Case Hunter 24
- **Location:** epics.md:965-970 (2.9), Story 10.5
- **Problem:** Seed scripts in shared and playtest play actions from every slice
- **Fix:** Define seeds as JSON action dicts validated by registry's GameRequest adapter, collected and run from cli.py
- **If shipped as-is:** Typed seed scripts import other slices' action models, which fails the contracts.

### Edge-Case Hunter 25
- **Location:** epics.md:1588 (6.5)
- **Problem:** A work story changes money's BSU withdrawal so it takes back deductions received
- **Fix:** Store deductions_received in shared state; money's withdrawal reads it, and the work story edits only shared
- **If shipped as-is:** A work-slice PR edits money's handler, outside its Slice line.

### Edge-Case Hunter 26
- **Location:** ARCHITECTURE-SPINE.md:39 (state upgrades in shared)
- **Problem:** Slices add state sections in parallel PRs, each bumping the one state_schema
- **Fix:** An ordered upgrade list in shared with one step per section change, and a CI check for duplicate or missing upgrade numbers
- **If shipped as-is:** Two upgrades take the same number, and loaded documents skip a slice's upgrade.

### Edge-Case Hunter 27
- **Location:** epics.md:163, 197
- **Problem:** Inventory AD-4 still says 'the engine's action models'; Tests line still says 'import-boundary check'
- **Fix:** AD-4: '... slices' action models joined by registry.py'; Tests: add slice/shared test locations and 'the import-boundary checks (AD-1, AD-21)'
- **If shipped as-is:** The story developer follows the stale inventory instead of the spine.

### Edge-Case Hunter 28 (claim, high confidence)
- **Location:** epics.md:384, 402
- **Problem:** Proposal: 'Every story has a Slice line, and the Epic List rule and table agree'
- **Fix:** Epic 2 notes say 2.1-2.8 build shared, but 2.2-2.7 are life and 2.9/2.10 are shared; the table omits 2.8-2.10 and 8.11
- **If shipped as-is:** Developers disagree on whether month-loop work in 2.6 belongs in shared or life.

### Edge-Case Hunter 29 (claim, medium confidence)
- **Location:** ARCHITECTURE-SPINE.md:42, 87
- **Problem:** Proposal: every 'one X' rule holds 'because X lives in the shared kernel'
- **Fix:** The one action union is built in registry.py (composition root), not in shared, yet shared/api's TypeAdapter route needs it
- **If shipped as-is:** Developers place GameRequest in shared, which then needs slices and breaks the forbidden contract.

### Edge-Case Hunter 30 (claim, high confidence)
- **Location:** sprint-change-proposal-2026-11-26.md (success criteria); epics.md:476
- **Problem:** Success criterion: 'Story 1.1's CI fails on an import from one slice into another'
- **Fix:** Story 1.1 scaffolds one empty example slice, so no slice-to-slice import can exist or be detected
- **If shipped as-is:** Story 1.1 is accepted without the independence check ever having been shown to fail.
