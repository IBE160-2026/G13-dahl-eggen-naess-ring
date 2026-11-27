---
title: Sprint Change Proposal, AD-21's kernel and extension points
date: 2026-11-26
status: approved
approved_by: Dahl
approved: 2026-11-26
scope: moderate
mode: incremental
proposals_approved: [1, 2, 3, 4, 5]
follows: sprint-change-proposal-2026-11-26.md
---

# Sprint Change Proposal: AD-21's kernel and extension points

## 1. Issue summary

**Problem.** AD-21 (vertical slices with a shared kernel, adopted earlier the same day) can't be built as written. It names five extension points: month-step slots, action union, view parts, derived flags and the account-deletion hook. The stories need more than that. Without the missing points, a developer must either import one slice into another, which CI forbids, or write another slice's part of the state, which AD-21 forbids. Story 1.1's CI checks also can't show that they fail.

**Discovery.** The AD-21 review on 2026-11-26 (`review-ad21-2026-11-26/report.md`, adversarial and edge-case lenses, 53 findings) ran before any code. Both lenses found the main gaps independently. Issue type: a failed approach, caught on paper.

**Evidence (from the review):**
- An event option (`life`) can give extra shifts (`work`, 6.6), a family loan (`credit`, 7.4) or change spending (`money`, 3.3). An open option (`phone`) can sell the moped licence (`belongings`, 8.2).
- The crisis options in 7.7 come from four slices.
- Wellbeing sits in `life`, but `money`, `work` and `credit` change it.
- The loss ending (4.4, `year`) needs rule 8, which `credit` builds in Epic 7.
- The shared auth dependency, pipeline and view must read `users`, `sessions` and `seen_disclosures`, which belong to slices.
- The shared routes need the action union and view types, which only `registry.py` builds.
- The order inside a slot isn't defined, so FR-45's payment order and replay depend on the order of imports.
- With one example slice, the independence contract in 1.1 can never fail. Tests inside `app/` that import `app.main` break the contracts. ESLint can't see `@/` imports without a resolver, and it can't ban the `fetch` global with import zones.
- The Epic 2 notes, the slice table and the Slice lines disagree on which stories build the kernel.

## 2. Impact analysis

**Epics.** None become obsolete and none are added, and the order is unchanged. Epic 2's kernel grows: wellbeing, rule 8 evaluation, the age unlock table and the kernel actions move there.

**Stories.** The text changes in about 20 stories (Proposal 4). No acceptance criterion is removed. The Slice lines of 2.2, 2.3, 2.5, 2.6 and 2.7 get two parts.

**PRD.** No impact. MVP unchanged.

**Architecture.** The layer table, AD-4, AD-5, AD-10, AD-13, AD-15, AD-16, AD-19 and AD-21, the Tests and Lint conventions, the Structural Seed and the Capability Map. SOLUTION-DESIGN §2, §10 and §12.

**UX.** None. The scene and controls only change folder.

**Technical.** Story 1.1 builds two stub slices and a self-test with planted violations. Tests across slices live in `backend/tests/`.

## 3. Recommended approach

**Direct adjustment (Option 1).** No code exists. The group chose to keep strict isolation (option A of the review) over narrowing AD-21 (option B: the engine as one shared package).

- **Effort:** medium, documents only.
- **Risk:** medium. The kernel and its registration points must be built in Epics 1-2, before the slices that use them, and every point is a contract the group must keep. The trade-off is weighed in SOLUTION-DESIGN §10.
- **Timeline:** no change to the epic order.

## 4. Detailed change proposals

### Proposal 1: The kernel owns what every slice needs (approved)

`ARCHITECTURE-SPINE.md`, layer table, AD-5, AD-10, AD-19, Structural Seed, Capability Map.

- **Kernel engine** (`shared/engine/`) adds:
  - **Kernel state:** month, pending, results, draw store, ledger and wellbeing.
  - **Kernel actions:** start, continue with `plan_version`, end early, play again.
  - **Wellbeing:** the one writer of the three parts, `wellbeing.add(state, part, delta, cause, scope)`, and rule 12 (FR-33).
  - **Rule 8 triggers:** trigger evaluation in `shared/engine/triggers.py`.
  - **The age unlock table** (FR-18).
- **Kernel shell:**
  - `shared/persistence/models/` holds `users`, `sessions` and `seen_disclosures` (AD-5, AD-10).
  - `shared/api/auth.py` holds the session check: JWT, sliding expiry and `last_active_at`.
- **Slices:**
  - `account` keeps the account flows: sign-up, login, logout, password change and reset, attempt limits, reset links, email and `delete_account`.
  - `life` keeps start, goal, avatar, pengegave, events and their options, and the wellbeing view part.
  - `explain` keeps the disclosures and their view, while the seen table is in the kernel.
- **Frontend, AD-19 Components:** known shared pieces are built in `shared/ui/` the first time, never moved there later:
  - the scene, with named group slots that routes in `src/app/` fill
  - the timeline
  - the result and outcome list
  - the «Hvorfor?», «Tidligere valg» and «Forenklet» controls
- **Capability Map:**
  - FR-33 moves to `shared/engine`, with the view part in `features/life`.
  - Disclosures seen (FR-40) moves to `shared/persistence`, with the view in `features/explain`.

### Proposal 2: AD-21 lists every extension point (approved)

The Extension points bullet in AD-21 is replaced by a table. Each point has one signature and one owner, and nothing is registered at module level.

| Point | A slice registers | Used by |
| --- | --- | --- |
| Month-step slots | `(slot, order, handler)`. Slots in order, open phase: income, tax, fixed costs, everyday costs and spending, unexpected expense, instalments, card bill and debt interest, savings interest, crisis re-check, selection. Continue phase: planned activities, wellbeing, December BSU, rule 8, close. After month 60: ending | The month loop |
| Actions | Its action members and their handlers | The one union (AD-4) |
| Effect handlers | `effect_kind → (possible(state, content), apply(state, effect, cause))`, writing only its own section; `lists.yaml` names each kind's owner | Event options, open options, messages, crisis options |
| Crisis options | `crisis_options(state, content) → [CrisisOption(id, possible, lands_month, effect)]` | `credit`'s crisis step, which collects, filters and applies them through the effect handlers |
| Selection proposers | Drawn and triggered proposers: events, messages, shifts, crisis events, card warning | The one selection step (AD-8), which alone writes the month's pending items and active or quiet |
| After-action hooks | `after_action(state, action, content)` | `apply()` after every action: `credit`'s crisis recheck and rule 8 money-in order (AD-9), and `explain`'s reactions (9.5) |
| Continue guards | `continue_guard(state) → refusal or None`, in fixed order | The continue action (`cannot_continue`) |
| Facts | Typed facts declared by name and type in `shared/engine/facts.py` and provided by one slice each (`owns_moped: bool`, `steady_monthly_wage: int or None`, …). Derived flags are the facts content may see | AD-16, other slices' rules, the content check |
| View parts | A named Pydantic part model and its builder; rows for the shared surfaces (Hjem, year end, recap, ending) in named row slots with a fixed order | `view()` (AD-13); single-winner fields (`pending`, `continue_warning`, the teaser) by a precedence table in the kernel |
| Upcoming costs | `upcoming_costs(state, content) → [Cost]` | FR-57 (9.4) |
| Shell hooks | On-action (AD-15), extra locks after the playthrough lock, on-account-deleted, sign-up guard | The pipeline, `delete_account`, sign-up |
| CLI, daily jobs, seeds | Commands, jobs, and seed scenarios as JSON action lists validated by the `GameRequest` adapter | `cli.py`, `main.py`'s job runner |

- **Ordering.** Every registration that takes part in an order carries an explicit `order` constant, unique within its slot. A test asserts that the orders are unique and stable, so registry import order never matters. A slot with no handler is a no-op. The worked-example tests catch a missing step, which replaces "a test fails if a slot has no handler".
- **Wiring.** `registry.build_kernel()` returns one frozen `Kernel` with every table.
  - `main.py` calls `create_app(kernel)`. `shared/api/game.py` exposes `build_game_router(kernel)`, so `shared` never imports `registry`.
  - The engine is `apply(state, action, content, seed, kernel)`.
  - `PlayerView` is built from named part models, so the generated TS names stay stable.
  - `GET /api/game/quote` lives in `features/credit/api.py`.
- **On-account-deleted.** Hooks run after `DELETE … RETURNING`, in the same transaction, and receive `DeletedUser(user_id, normalized_email, is_test, removed)`.
- **State.** Each slice defines its own section model in its `engine/`, and `registry.py` composes the state document. State upgrades are one ordered list in `shared/persistence`, and CI fails on a duplicate or missing step number.
- **AD-16** changes "computed by one engine function" to "provided by one registered fact provider each, merged by one kernel function".
- **AD-4** names start, continue, end early and play again as kernel members, and the union as `kernel.game_request_type`.
- **AD-13**'s `view()` gets `seen_disclosure_ids` and `nickname` from kernel tables.

### Proposal 3: CI and tests (approved)

**Story 1.1:**
- The scaffold has two real stub slices, `account` and `life`, each with an empty `engine/`.
- A CI self-test copies `backend/app` to a temp folder, plants each violation and asserts that `lint-imports` exits non-zero. The violations: `features.account` → `features.life`, `shared` → `features`, an engine → `fastapi`, and an engine → `app.settings`.

**Engine purity (AD-1, AD-21).** A forbidden contract with the sources `app.shared.engine` and `app.features.*.engine`. It forbids:
- `app.settings`, `app.main`, `app.cli` and `app.registry`
- `app.shared.content`, `.persistence`, `.api` and `.jobs`
- every slice's `api`, `models`, `jobs` and `cli`

A ruff banned-api rule on `importlib.import_module` and `__import__` under `app/`.

**Tests convention:**
- A slice's own tests that import only the slice and `shared` stay in `features/<slice>/tests/`.
- Tests that build the real app, use the database or cross slices live in `backend/tests/`, outside the `app` package. These are worked examples across slices, replay, AD-9 reconciliation, seed assertions, the per-member test in AD-4, and 2.10.
- pytest runs with `--import-mode=importlib`.

**Frontend (Story 1.2, Lint convention, AD-20):**
- `eslint.config.mjs` generates one `import/no-restricted-paths` zone per slice from the slice list (target `features/<s>`, from `features`, except `./<s>`), plus `shared` → `features` and `app` denied.
- The rule uses `import/resolver: typescript`.
- `fetch` is banned with `no-restricted-globals`, with an override for `src/shared/api/**`.
- The fixtures move to `src/shared/test/fixtures/`.
- A lint fixture file must fail, and CI checks that it does.

**Structural Seed:** `cli.py` lists `clear-game-data` again, and `backend/tests/` is added.

### Proposal 4: `epics.md` (approved)

- **Slice lines:** two-part lines where a story builds kernel parts:
  - 2.2 `shared (pipeline, envelope, game store, focus manager) + life`
  - 2.3 `shared (ledger, draws, scene, timeline) + life`
  - 2.5 `shared (cause links, results, result list) + life`
  - 2.6 `shared (month loop, selection step, kernel actions) + life`
  - 2.7 `shared (wellbeing) + life`
- **Tables and notes:**
  - The slice table's `shared` row lists 1.1, 1.2, 2.1-2.3, 2.5-2.10 and 8.11.
  - The `playtest` row lists Epics 1 and 10 (1.8).
  - The Epic 2 notes list the same stories.
- **Rule for every story (AD-21):** names the extension points by the Proposal 2 table.
- **Stories that name their extension point:**
  - Effect handlers: 2.5, 3.3, 5.4, 6.5, 6.6, 7.4, 8.2, 8.4.
  - Crisis options: 7.7 and 8.3.
  - The kernel wellbeing writer: 3.3, 6.2, 7.4.
  - Sign-up guard: 1.8.
  - The kernel triggers: 4.4 builds `shared/engine/triggers.py` for the triggers that exist, and 7.5 adds the card and loan triggers.
  - Continue guard: 7.7.
  - `plan_version` in the kernel: 6.1.
  - The kernel's `shared/ui` controls: 9.1-9.3.
  - Cost providers: 9.4.
  - After-action hook: 9.5.
  - The deletion hook's signature: 1.7.
  - Seed scenarios in the slice whose state they target: 10.5.
- **Story 1.1:** the two stub slices and the self-test from Proposal 3.
- **Story 1.2:** the resolver, the `fetch` rule and the failing lint fixture.
- **Inventory:**
  - The AD-4 bullet: the slices' action members and the kernel members, joined by `registry.build_kernel()`.
  - The AD-16 bullet: fact providers.
  - The AD-21 bullet: the extension-point table.
  - The Tests bullet: the import-boundary checks (AD-1, AD-21), test locations and `backend/tests/`.

### Proposal 5: SOLUTION-DESIGN and memlog (approved)

- **§10 row:** "Vertical slices with a shared kernel and registered extension points".
  - Weighed against: horizontal layers; later slices importing earlier ones; one slice per mechanism; the engine as one shared package (option B).
  - Why: each domain can be built, reviewed and cut alone, and CI keeps it so.
  - Cost: a larger kernel built in Epics 1-2, and a dozen registration contracts.
- **§2:** one sentence on the kernel and the slices.
- **§12:** the AD-21 review and this proposal.
- **`.memlog.md`:** the event and the decision.

## 5. Implementation handoff

**Scope: moderate.** It changes the architecture and story text, with no replan of the PRD or MVP.

| Role | Responsibility |
| --- | --- |
| Architect (spine) | Proposals 1, 2, 3 and 5 |
| PO / Developer (epics) | Proposal 4, then `bmad-sprint-planning` to refresh `sprint-status.yaml` |
| Developer | Builds the kernel tables in Story 1.1 and Epic 2, and the self-test in Story 1.1 |

**Success criteria:**
- Every cross-slice need named in the review maps to a row in the extension-point table.
- No story's criteria need an import from one slice into another or a write to another slice's section.
- Story 1.1's self-test fails on each planted violation.
- The Slice lines, the slice table and the Epic 2 notes list the same kernel stories.
- `sprint-status.yaml` is still in sync after a rerun.

## 6. Verification after applying

Two read-only checks ran on the edited documents the same day.

- **Findings check:** each of the 53 review findings was checked against the documents. 40 were fixed and 13 partly fixed, and the check found eleven new ambiguities.
- **Story check:** all 73 stories were read against the new AD-21. It found 46 problems, 40 in stories and 6 in the inventory, the Structural Seed, SOLUTION-DESIGN and README.

The fixes applied:

- **Extension-point table:** every point has a signature, every slot an owner and an order, and message actions are added. Rule 8 is kernel code that reads facts, not a slot.
- **Imports:** foreign keys and `relationship()` only to kernel tables.
- **Kernel stories:**
  - Two-part Slice lines for 1.3, 1.4, 1.8, 3.4, 4.1, 4.6, 7.2 and 9.1-9.3.
  - 10.5's seeds moved to `year`, gated by `APP_ENV`.
- **Kernel actions:** start, end early and play again are kernel actions. The `life` and `year` slices own their screens.
- **Story lines:** Extension points lines on 44 stories, naming the facts each one provides or reads. Touches lines on 6.5, 7.7 and 9.4.
- **Ownership:** `completed` has one owner, the kernel's continue action.
- **Signatures:** the deletion hook is `hook(session, deleted)`, and `wellbeing.add()` is in the layer table.
- **Engine signature:** `apply(…, kernel)` everywhere.
- **README and SOLUTION-DESIGN:** the review text now matches the hand review in the spine. SOLUTION-DESIGN §2 also gets a sentence on the kernel and the slices.

`bmad-sprint-planning --dry-run` reports `sprint-status.yaml` in sync, with no new or dropped stories.
