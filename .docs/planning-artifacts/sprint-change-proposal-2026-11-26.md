---
title: Sprint Change Proposal, vertical slices in the code
date: 2026-11-26
status: approved
approved_by: Dahl
approved: 2026-11-26
scope: moderate
mode: incremental
proposals_approved: [1, 2, 3, 4]
---

# Sprint Change Proposal: vertical slices in the code

## 1. Issue summary

**Problem.** The group wants the epics built as vertical slices in the code, not only in delivery: each feature's code kept as isolated as possible, with reuse (DRY) through shared folders for common components and libraries. The planning said "vertical slice" only about delivery (backend, frontend and tests for the same player outcome). The architecture placed the code in horizontal layers: `backend/app/{engine,content,persistence,api,auth,email,jobs}/` and `frontend/src/{app,components,api}/`. A story such as "take a consumer loan" would write into four or five shared layer folders.

**Discovery.** Found by the group on 2026-11-26 while running sprint planning, before `sprint-status.yaml` was generated and before any code existed. Type: new requirement from the team (a planning gap, not a failed approach).

**Evidence.**
- `ARCHITECTURE-SPINE.md:34-69` (layer table and diagram), `:430-477` (Structural Seed), `:479-501` (Capability Map).
- `epics.md:154, 160, 165, 168, 177, 178, 194` (inventory paths), `:357` (Epic List intro), `:380` (Epic 1 notes), `:457` (Story 1.1 CI), `:477-487` (Story 1.2 paths).
- `SOLUTION-DESIGN.md:201`, `DESIGN.md:171`, `diagrams/03-lagene.svg`.

## 2. Impact analysis

**Epics.** None become obsolete and none are added; the order is unchanged. Each epic gets one slice folder (its domain). Epic 1 sets up the slice structure and the CI boundary checks; Epic 2 builds the shared kernel. Later epics that add to earlier surfaces (Epic 4's year end and recap from Epics 5 and 6; Epic 7's crisis options using shifts and jobs) now do it through the kernel's extension points instead of direct imports.

**Stories.** Changed text in 1.1, 1.2 and 1.7; a **Slice** line on all 73 stories; a new rule in the Epic List. No acceptance criteria are removed.

**PRD.** No impact (it names no code paths). MVP unchanged.

**Architecture.** A new AD-21 and a new layer table; paths in AD-1, AD-4, AD-6, AD-7, AD-9, AD-15, AD-18, AD-19, the Lint and Tests conventions, the mermaid layer diagram, the Structural Seed and the Capability Map; `SOLUTION-DESIGN.md:201`; diagram `03-lagene.svg`. Every "one X" rule (one ledger, one union, one selection step, one view, one pipeline) still holds, because X lives in the shared kernel.

**UX.** Only the tokens path in `DESIGN.md:171`.

**Other.** CI gains import-linter contracts (an independence contract over `app.features.*`, a forbidden contract from `app.shared` to `app.features`, AD-1's purity contracts on every `engine` package) and ESLint `import/no-restricted-paths` zones. No deployment or infrastructure impact.

## 3. Recommended approach

**Option 1, direct adjustment.** No code exists, so nothing is rolled back (option 2 not applicable), and the MVP needs no review (option 3 not applicable).

- **Effort:** low to medium, documents only.
- **Risk:** low. The main trade-off is that the game is a tightly coupled simulation (rule 1 runs every mechanism in a fixed order, one ledger, crises use jobs), so the shared kernel is large and is built early (Epics 1 and 2). The alternative, letting later slices import earlier ones, was rejected for weaker isolation.
- **Timeline:** no change to the epic order. Sprint planning runs again after the edits.

**Decisions made in this session:**
1. One slice per epic domain (about ten), not one per mechanism.
2. Slices import only themselves and `shared`; cross-slice behaviour only through the kernel's extension points.
3. DRY by the rule of two: code stays in its slice until a second slice needs it, then moves to `shared` in that PR, never copied.

## 4. Detailed change proposals

### Proposal 1: Spine, new AD-21 and layer table (approved)

`ARCHITECTURE-SPINE.md`, Design Paradigm (`:34-69`), new AD-21 after AD-20.

Replace the layer table with:

| Part | Directory | Holds |
|---|---|---|
| Shared kernel: engine | `backend/app/shared/engine/` | State document model (one section per slice, data only), content model, month loop with rule 1's fixed step slots, ledger (AD-9), draws (AD-6), selection step (AD-8), derived flags (AD-16), view assembly and text formatting (AD-13), refusal codes |
| Shared kernel: shell | `backend/app/shared/{content,persistence,api,jobs}/` | YAML loader and the one item check (AD-7), one `Base`, the mutation pipeline, `playthroughs` and `action_log` (AD-4, AD-5), `AppError`, the envelope, `POST /api/game/actions` and `GET /api/game`, the auth dependency, the job runner |
| Slices | `backend/app/features/<slice>/` | One per epic domain: `account`, `life`, `money`, `year`, `phone`, `work`, `credit`, `belongings`, `explain`, `playtest`. Each holds `engine/` (pure: its actions, month steps, rules, view part) and, when needed, `api.py`, `models.py`, `jobs.py`, `cli.py`, `tests/` |
| Composition roots | `backend/app/main.py`, `cli.py`, `registry.py` | `registry.py` imports every slice and builds the action union, the month-step table, the view parts and the CLI commands |
| Leaf | `backend/app/settings.py` | Unchanged |
| Frontend | `frontend/src/shared/{api,ui,styles,fonts,gates}/`, `frontend/src/features/<slice>/`, `frontend/src/app/` | Shared: game client, primitives, tokens, `gateFor`. Features: a slice's screens and components with CSS Modules. `app/`: thin routes that compose slices |

New **AD-21 — Vertical slices with a shared kernel**:
- **Prevents:** one feature's code spread across five layer folders; a change to the card touching the job's code; slices quietly depending on each other until nothing can be built or cut alone.
- **Rule:**
  - A slice imports only itself and `shared`; `shared` never imports a slice; only the composition roots (`main.py`, `cli.py`, `registry.py`, and in the frontend `src/app/`) import slices. CI checks this with an import-linter `independence` contract over `app.features.*`, a `forbidden` contract from `app.shared` to `app.features`, and AD-1's purity contracts on `app.shared.engine` and every `app.features.*.engine`. In the frontend, ESLint `import/no-restricted-paths` zones enforce `app` → `features` → `shared`, no `features/X` → `features/Y`, and `fetch` only in `shared/api/`.
  - Cross-slice behaviour goes only through the kernel's extension points, never a direct import: a slice registers its handlers in rule 1's fixed slots (income, tax, fixed costs, …, planned activities, wellbeing, December BSU), so the order still lives in one place; its action members in the one union (AD-4); its view part (AD-13); and it reads another slice's typed facts only as derived flags or through the shared state model (AD-16), never writing another slice's section of the state.
  - Surfaces that collect from several slices (Hjem, year end, recap, ending) get rendered rows the view assembles, or a route in `src/app/` that composes the slices' components.
  - DRY by the rule of two: code lives in the slice that uses it; when a second slice needs it, the PR that adds that need moves it to `shared`. No copies.
  - Content data stays in `content/` by kind (AD-7); slices are code, not content.

### Proposal 2: Paths in the rest of the spine, SOLUTION-DESIGN and DESIGN (approved)

| Place | Old | New |
|---|---|---|
| AD-1 `:77` | `engine` imports none of … (scoped to `engine`); `engine/content_model.py` | `shared.engine` and every `features.*.engine` import none of …; the banned-api rule is scoped to the same modules; `shared/engine/content_model.py` |
| AD-4 `:96` | the engine's own action models, with no second union in `api/` | the slices' action models, joined into one union by `registry.py`, with no second union anywhere |
| AD-6 `:138` | `engine/draws.py` | `shared/engine/draws.py` |
| AD-7 `:150-151` | `content/` (the code) | `shared/content/` (the repo-root data folder `content/` is unchanged) |
| AD-9 `:167`, `:178` | `engine/ledger.py` | `shared/engine/ledger.py` |
| AD-15 | one `delete_account(user_id)` deletes the records | `delete_account` lives in `features/account` and runs every slice's registered on-account-deleted hook in the same transaction; `playtest` registers the records' deletion and the `testers_left` count there |
| AD-18 `:305-306`, SOLUTION-DESIGN `:201` | `frontend/src/api/`; "Only `api/` writes it" | `frontend/src/shared/api/`; "Only `shared/api/` writes it" |
| AD-19 `:318-320`, DESIGN `:171` | `frontend/src/styles/tokens.css`, `components/ui/` | `frontend/src/shared/styles/tokens.css`, `shared/ui/` |
| Conventions, Lint `:353` | bans `fetch` outside `src/api/`, import direction `app` → `components` → `api` | bans `fetch` outside `src/shared/api/`; import zones `app` → `features` → `shared`, no feature → feature (AD-21) |
| Conventions, Tests `:355` | — | + "Each slice's tests live in `features/<slice>/tests/`; kernel tests in `shared/tests/`; e2e stays in `frontend/e2e/`" |
| Mermaid diagram `:51-67` | 8 layers | `main / cli / registry` → `features.*` → `shared.{api, persistence, content, jobs}` → `shared.engine`; `features.*.engine` → `shared.engine` |
| Structural Seed `:430-477` | the layer tree | the tree below |
| Capability Map `:479-501` | Lives in: `auth`, `api`, `engine` … | Lives in: the slice, plus `shared` where the kernel carries it |
| `diagrams/03-lagene.svg` | layer diagram | redrawn to match the new mermaid diagram |

New Structural Seed (backend app and frontend src; the rest unchanged):

```text
backend/app/
  main.py  cli.py  registry.py  settings.py
  shared/
    engine/        # state + content model, month loop (rule 1 slots), ledger.py, draws.py,
                   #   selection.py, flags.py, view.py + text formatting, refusals
    content/       # loader, check_item(), fingerprint, content check runner (AD-7)
    persistence/   # Base, pipeline, playthroughs, action_log, state upgrades (AD-3/4/5)
    api/           # AppError + envelope, /api/game routes, auth dependency (AD-2, AD-13)
    jobs/          # daily job runner with advisory locks
    tests/
  features/
    account/       # passwords, sessions, attempt limits, reset links, email, delete_account (AD-10, AD-11)
    life/  money/  year/  phone/  work/  credit/  belongings/  explain/  playtest/
                   # each: engine/ (pure), and api.py, models.py, jobs.py, cli.py, tests/ when needed
frontend/src/
  app/             # thin routes and layouts that compose features (AD-17)
  shared/
    api/           # generated types, client, store, sendAction, config.ts (AD-18)
    ui/            # sheet, locked control, live region, money figure, bar (AD-19)
    gates/         # gateFor, focus manager (AD-17)
    styles/  fonts/
  features/<slice>/  # the slice's screens and components with .module.css, plus tests
  test/fixtures/
```

### Proposal 3: `epics.md`, rules, inventory and Epic 1 (approved)

- **A. Epic List intro (`:357`):** "… (the group builds both sides)" → "… (the group builds both sides), with the code in the epic's own slice folder (AD-21)".
- **B. New rule after "no link to what isn't built" (`:367`):** "Rule for every story: code goes in its slice (AD-21)", with the slice table (`account` 1, `life` 2, `money` 3, `year` 4, `phone` 5, `work` 6, `credit` 7, `belongings` 8, `explain` 9, `playtest` 10, `shared` for the kernel), the rule of two, and cross-slice additions only through the extension points or a composing route.
- **C. Inventory:** `:154` the Structural Seed tree; `:160` AD-1 to `shared/engine/` and the slices' pure `engine/` folders; `:165`, `:168` to `shared/engine/…`; `:177`, `:178`, `:194` the Proposal 2 paths; a new AD-21 bullet.
- **D. Epic notes:** Epic 1 (`:380`) scaffold with `shared/` and `features/` and the slice boundary checks, `shared/styles/tokens.css`, `shared/ui/`; Epic 2 (`:385`) Stories 2.1-2.8 build the kernel in `shared/`; Epic 4 (`:395`) additions from Epics 5 and 6 arrive as those slices' view parts or rows.
- **E. Story 1.1 (`:457`):** the import-boundary checks become "`shared.engine` and every `features.*.engine` pure (AD-1); slices independent of each other, `shared` never importing a slice (AD-21), with one empty example slice so the contracts have something to check".
- **F. Story 1.2 (`:477`, `:480`, `:487`):** `shared/styles/tokens.css`, `shared/ui/`, ESLint with `fetch` only in `shared/api/` and the AD-21 import zones.
- **G. Story 1.7 (`:624`):** + "and runs every slice's registered on-account-deleted hook in the same transaction (Story 10.1 registers the playtest records' one)".

### Proposal 4: A Slice line on every story (approved)

A `**Slice:**` line under each story's Tier line:

| Slice | Stories |
|---|---|
| `shared` | 1.1, 1.2, 2.1, 2.8, 2.9, 2.10, 8.11 |
| `account` | 1.3-1.7 |
| `playtest` | 1.8, 10.1, 10.2, 10.5, 10.6 |
| `life` | 2.2-2.7 |
| `money` | 3.1-3.6 |
| `year` | 4.1-4.6 |
| `phone` | 5.1-5.5 |
| `work` | 6.1-6.7 |
| `credit` | 7.1-7.8 |
| `belongings` | 8.1-8.5 |
| `explain` | 9.1-9.5 |
| `— (infra)` | 1.9 |
| `— (content)` | 8.6-8.10, 10.3 |
| `— (manual checks)` | 10.4 |

## 5. Implementation handoff

**Scope: moderate.** It changes the architecture and reorganizes the backlog, with no replan of the PRD or MVP.

| Role | Responsibility |
|---|---|
| Architect (spine) | Proposals 1 and 2: AD-21, the layer table and diagram, path updates, Structural Seed, Capability Map, `03-lagene.svg`, `SOLUTION-DESIGN.md`, `DESIGN.md` |
| PO / Developer (epics) | Proposals 3 and 4: rules, inventory, notes, Stories 1.1, 1.2, 1.7, the Slice lines |
| Developer | Builds the structure in Story 1.1 and the boundary checks in CI |

**Success criteria:**
- No rule in the spine or epics points to a layer folder that no longer exists (a search for `app/engine/`, `src/api/`, `src/components/`, `components/ui/` finds only historical documents).
- Every story has a Slice line, and the Epic List rule and table agree with it.
- Story 1.1's CI fails on an import from one slice into another and from `shared` into a slice.
- `bmad-sprint-planning` runs again on the updated epics.

## 6. Approval and execution

Approved by Dahl on 2026-11-26, all four proposals as presented. Applied the same day on branch `docs/vertikale-skiver`: the spine (layer table and diagram, AD-21, paths, Structural Seed, Capability Map, memlog), `SOLUTION-DESIGN.md`, `DESIGN.md`, `diagrams/03-lagene.svg` and `epics.md`. Next: rerun `bmad-sprint-planning`.
