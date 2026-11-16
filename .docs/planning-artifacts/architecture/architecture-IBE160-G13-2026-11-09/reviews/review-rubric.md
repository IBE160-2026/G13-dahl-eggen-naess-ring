---
title: Rubric review: ARCHITECTURE-SPINE.md (good-spine checklist)
created: 2026-11-13
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-13, after both reconcile passes)
inputs:
  - ../.memlog.md
  - ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (final, 2026-11-13)
  - ../../../prds/prd-IBE160-G13-2026-10-22/addendum.md
  - reconcile-prd.md, reconcile-reference-memlog.md (findings already applied are not repeated)
scope: backend/infra up to the API boundary. The frontend is deferred to the frontend team. The reference setup is adapted, not copied. No new features or services are proposed.
---

# Rubric review: architecture spine

**Verdict:** The spine is close to ready, but four gaps would still let stories or the two teams build things differently: the layer diagram contradicts the wiring the ADs need, money and cause links have no single writer, the content freeze has no trigger, and no one is named to render game text. Eight smaller medium items need tightening. None of the fixes adds a service or a feature.

**Count:** 0 critical · 4 high · 8 medium · 10 low

Line numbers refer to `ARCHITECTURE-SPINE.md` as it stood on 2026-11-13.

## Rubric summary

| Check | Result |
| --- | --- |
| Fixes the real divergence points, misses none | Mostly. It misses the cause-link and ledger writer (H2), how game text is rendered (H4), `plan_version` (M1), the action endpoint style (M2), lock order (M4) and the open-option and content inventory (M6) |
| Every AD Rule is enforceable and prevents its divergence | AD-1's import check contradicts the layer table (H1). AD-7's freeze has no trigger (H3). AD-9 covers charges only (H2). AD-10's sliding lifetime conflicts with a JWT `exp` (M5) |
| Nothing under Deferred can let two units diverge | Three rows let divergence through: "Endpoint list" (M2), "Fields of the engine state document and the player view" (H2, H4, M1) and "Content schemas in detail" (M6) |
| Named tech is verified-current | Not quite. FastAPI is now 0.162.x, not 0.141.x. The "current" notes for Caddy and SQLAlchemy are out of date (M8) |
| Covers the PRD's capabilities | Yes, apart from the gaps above. `binds` and the capability map disagree (L1) |
| Deployment, environments, provider and operations each decided, deferred or open | Yes. The fallback silently drops the course's Supabase requirement (M7). There's no rollback rule for the playtest (L9) |
| Internally consistent (ADs, conventions, diagrams, tree) | No. See H1 (layers vs settings, pipeline, jobs and content models), M3 (money convention vs AD-6) and L5 (address column vs ER) |
| Mermaid diagrams are valid | Yes. All four parse with mermaid 11.4.1 (flowchart, sequence, flowchart, er) |
| Bloat | Small: about 10 lines restate the PRD or are story-level (L11) |

---

## High

### H1. The layer diagram forbids the wiring the ADs need, so AD-1's CI check fails on day one

- **Location:** Design Paradigm table (l.31-39) and dependency diagram (l.41-57); AD-1 Rule (l.65); AD-4 sequence diagram (l.91); AD-14 "One image, one settings file" (l.180); Config convention (l.216); Jobs convention (l.218); source tree (l.283-307).
- **Problem:** AD-1 says a CI import check fails on any import that breaks the diagram. As drawn, the diagram blocks four things the other ADs require:
  - **`settings.py` sits in the ops layer**, and nothing may import ops. But auth (limits, idle times), email (`RESEND_API_KEY`, `APP_ENV`), persistence (`DATABASE_URL`, pool size, `PLAYTEST_RECORDS`) and api (`/docs` gating) all read settings (AD-14, Config convention).
  - **The pipeline lives in persistence and calls `apply(state, action, content, seed)`**, but persistence has no edge to `content`. The AD-4 sequence diagram also runs "auth (AD-10)" inside the pipeline, although the arrow points the other way (auth → persistence).
  - **Content types:** `content/` holds "schemas", and the engine must not import `content/`. So the typed content model the engine reads can't live where the table puts it. The first content-loader story will define the Pydantic schemas in `content/`, and the first engine story will then break AD-1.
  - **No composition root:** daily jobs run "inside the backend process" (Jobs convention), and content loads at startup (AD-7). Neither has an importer in the diagram, and the tree has no `main.py`.

  Each builder will patch this differently: ad-hoc exceptions in the import check, settings passed by hand, or the check switched off.
- **Fix:** keep the paradigm and correct the diagram and table:
  - **`settings`** becomes its own leaf that every layer may import and that imports nothing from `app`. Move it out of the ops row.
  - **Content model in the engine:** the engine owns the content *model* (for example `engine/content_model.py`). `content/` loads the YAML, validates it, fingerprints it and builds engine models. Change the table cell to "YAML loader, YAML validation, fingerprint, content check".
  - **Composition root:** add `backend/app/main.py`, the only module that may import every layer. It builds the FastAPI app, loads content, and starts the jobs in the lifespan. Add it to the tree.
  - **Auth before the pipeline:** auth runs as the api dependency before the pipeline. The pipeline receives the authenticated `user_id` and the loaded content as arguments. Move "auth (AD-10)" in the sequence diagram onto a `C->>API` step before `P`, or label it "api dependency".

### H2. Money movements and cause links have no single writer, so FR-36, FR-38, FR-39, FR-42 and F10 can't be built consistently

- **Location:** AD-9 (l.130-134); AD-1 table row "cause links" (l.33); Deferred row "Fields of the engine state document" (l.335).
- **Problem:** AD-9 covers "every amount the engine *charges*", and then says "no other code moves money between accounts". That leaves open whether income, savings and BSU interest, the BSU deduction, loan payouts, gifts, moped sale proceeds, BSU withdrawal, transfers between the player's own accounts, and the payment-plan conversion go through it. It also leaves out FR-32b's rule for money arriving in a crisis month: a negative current account first, then overdue card minimums.

  Meanwhile FR-36 (Core) requires every effect to carry its causes, with shares that add up exactly. The addendum requires per-cause parts on every balance: interest split in proportion, payments reducing every part in proportion, largest-remainder rounding. FR-42 (Core) ranks choices by their money effect summed over the whole playthrough, with ties broken by confirmation order. The engine can't read `action_log`, so those totals must live in the state.

  The addendum's "For the architecture" asks for "the per-cause parts of each balance". The spine defers all state fields to engine stories. Every money story (wages, tax, costs, card, loans, BSU, activities, crisis, moped) will write balances and causes in its own way. If any movement skips the parts, the shares stop adding up and the ending ranking is wrong.
- **Fix:** widen AD-9 into one ledger:
  - **One ledger for every balance:** every change to any balance (current, savings, BSU, card, each loan or plan) goes through `engine/ledger`. `pay()` implements the FR-45 table, `receive()` implements FR-32b's arrival order, and `transfer()` moves money between the player's own accounts.
  - **Every call carries its cause:** a choice id or a system cause. Each call updates that balance's per-cause parts using the addendum's rounding.
  - **Totals live in the state:** the state keeps a running total of money and wellbeing effects per choice for FR-42.
  - **Choice ids sort in confirmation order:** for example `(state_version, index)`.

  This is one sentence in AD-9 plus one line in the Deferred row: "the ledger and cause-link shape are fixed by AD-9; other fields follow stories". It adds nothing to build, because the payment function already exists.

### H3. AD-7's freeze has no trigger, so the rule either blocks all content work or never applies

- **Location:** AD-7 (l.122); source tree `content/library/v1/` (l.300).
- **Problem:** "A published version is frozen", and CI fails on any fingerprint change. But nothing says when a version becomes *published*. Content is written and tuned throughout the sprints (OQ-8 and OQ-17 are open; tuning freezes before the playtest).
  - If `v1` counts as published from its first merge, every mechanics tweak during authoring needs a new folder (`v2` … `v30`).
  - If nothing marks it, the check never bites.

  The "until tuning is frozen" switch for the soft gates has the same problem: no flag says where the freeze is recorded. "Versions stay while any playthrough uses them" can't be enforced either: nothing stops a PR from deleting a version folder, and the startup check loads only the folders that exist.

  The playtest environment also exists from the sprint-1 spike onwards. So team playthroughs on a still-changing `v1` would sit in the same database the testers later use.
- **Fix:** one flag in each manifest drives everything:
  - **One flag:** `frozen: false` while a version is being authored. Then no fingerprint gate applies, and only the schema, reference and open-option gates fail.
  - **One PR flips it:** the PR that opens the playtest sets `frozen: true`. From then on, the fingerprint and every FR-58 gate fail CI.
  - **Frozen folders can't disappear:** CI fails if a frozen version folder is removed. Folders are never deleted in the MVP.
  - **Clean start for testers:** when `v1` is frozen, the playtest database's game data is cleared once, before testers arrive.

### H4. No one is named to render game text, the main open item at the boundary with the frontend team

- **Location:** AD-13 (l.165); AD-7 (l.122: text sits in the library YAML); Deferred rows "Everything in the frontend" and "Fields of … the player view" (l.332, l.335).
- **Problem:** the PRD puts the engine's figures inside player-facing text:
  - FR-54: "any amount … in a message is the engine's figure", and the message schema says "a placeholder the engine fills in"
  - FR-39 lines such as «… 17 270 kr mer …»
  - FR-38 "Hvorfor?" explanations from the rules
  - FR-42 ending texts per mechanism and sign
  - FR-15 teasers
  - FR-34 room-state texts
  - FR-37 badge text naming the earlier choice
  - FR-40 disclosures and the "Om tallene" page

  The text is also versioned with the playthrough (NFR-4: cause links point to the event version the player saw). AD-13 fixes what the view leaves out, but not whether it carries finished Norwegian strings or ids plus parameters. Nor does it say who formats kroner. The frontend team, working in parallel, may build its own text catalog keyed by ids. That catalog can't follow pinned library versions, and it would put figures into text outside the backend (NFR-4).
- **Fix:** add one boundary fact to AD-13:
  - **The backend renders game text:** the player view carries finished Norwegian strings for all game text, with the engine's figures already filled in and formatted, plus the raw integers where the UI needs a number (balances, wellbeing, slots).
  - **The frontend owns only UI chrome text** (buttons, labels, offline and saving notices).
  - **One formatting function:** formatting kroner in text goes through one engine function.

---

## Medium

### M1. `plan_version` is named but not defined

- **Location:** AD-4 Rule and diagram (l.83, l.90, l.94); AD-13 view contents (l.165).
- **Problem:** FR-49 refuses a continue when the month plan has changed since the device loaded it. The spine never says where `plan_version` lives, what increments it, whether it resets at month open, or that the view exposes it. AD-13 lists `state_version` in the view, but not `plan_version`.
  - **If the frontend sends `state_version`** and the backend compares it with a plan counter, continue is either always refused or never refused.
  - **If the backend reuses `state_version`**, any change on another device refuses the continue, including a money action. NFR-7 doesn't list that refusal.
- **Fix:** AD-4: "`plan_version` is a counter in the state, raised by every plan change (place, remove, same as last month) and reset at month open. The view exposes it; continue sends it back; a mismatch is `409 plan_changed`."

### M2. Whether game actions share one endpoint or get one each is left to stories

- **Location:** Deferred row "Endpoint list and request/response models" (l.334); Naming convention (l.210).
- **Problem:** AD-4 fixes the protocol fields, and AD-13 fixes the response. But about 25 action kinds (choice, transfers, BSU, card settings, loans, hours, sell, take option, place or remove activity, same as last month, pin, minigame start and answer, continue) can each become their own route, with ad-hoc REST verbs. Or they can all be one union. The engine already takes a single `action`. Stories built by different people will produce an uneven contract for the frontend team, and each route has to re-wire the pipeline.
- **Fix:** one line in AD-4: "State-changing game requests go to `POST /api/game/actions` with `{request_id, month, plan_version?, action}`. `action` is a discriminated union (`type`) mirroring the engine's action model. `GET /api/game` returns the player view. Account, session and disclosure endpoints are separate." The endpoint *list* can stay deferred.

### M3. The money type is either/or, and the convention contradicts AD-6

- **Location:** AD-6 (l.116: "the state document holds money as integer øre"); Money convention (l.213: "Integer øre *or* `Decimal` inside the engine *and the state document*").
- **Problem:** Two engine stories can pick different types: one passes øre `int`s, another `Decimal` kroner. They meet in the state model and the ledger.
  - **The convention contradicts AD-6:** it allows `Decimal` in the state document, which AD-6 rules out.
  - **Rule 2 makes øre unnecessary:** every amount is whole kroner. Only rates and hourly wages (for example NOK 139.40) carry decimals, and only intermediate products reach .5 (8,151.5).
- **Fix:** pick one: "Amounts are `int` whole kroner everywhere (engine, state, API). Rates and hourly wages are `Decimal` (quoted strings in YAML). Any product of an amount and a rate is a `Decimal` that goes back to `int` only through the rule 2 rounding function." Update AD-6 and the Money convention to match.

### M4. Lock order between `users` and `playthroughs` can deadlock

- **Location:** AD-4 Rule (l.83: game requests lock the playthrough row; start, restart and end lock the `users` row "instead"); Accounts convention (l.217: `last_active_at` is set by the auth dependency *and the pipeline*).
- **Problem:** When the two requests overlap, they take the same two locks in opposite order:
  - **A game request** locks the playthrough row, then updates `users.last_active_at`.
  - **A restart or account deletion (FR-44)** locks `users`, then deletes the playthrough (directly or by cascade).

  Postgres aborts one of them with a deadlock error. That error lands in the refusal and session path that AD-4 says never calls `rollback()`. The trigger is the double-tap or second-device case that AD-4 exists to handle.
- **Fix:** one sentence in AD-4: "Every state-changing transaction locks the `users` row first. Since there is one playthrough per user, game requests lock `users … FOR UPDATE` as their single lock point. Only the auth dependency writes `last_active_at`, before any lock." The Accounts convention drops "and the pipeline".

### M5. A JWT `exp` conflicts with the sliding lifetimes

- **Location:** AD-10 "Sessions" (l.142).
- **Problem:** The JWT carries `sid` and `exp`, while the row and the cookie "slide" with activity. No `exp` value is given, and nothing says the token is re-issued when the row slides.
  - **If `exp` is set to the idle limit at login**, an unticked player who keeps playing is logged out after 30 minutes. FR-5 says "30 minutes with no activity", and a full playthrough takes about an hour.
  - **If `exp` is 30 days from login**, a ticked player who keeps playing is logged out after 30 days, while the cookie keeps sliding.
- **Fix:** add "`exp` is the session row's `expires_at`. Whenever the dependency slides the row (at most once a minute), it re-issues the cookie with a fresh JWT". Alternatively: "`exp` is fixed at 30 days and the row alone enforces idle time; the ticked cookie is re-set on slide."

### M6. Open options and several content kinds have no place in the library

- **Location:** AD-7 (l.122: "one YAML file per event, activity, message or room layer"); source tree (l.300); Deferred row "Content schemas in detail" (l.336).
- **Problem:** The addendum's "For the architecture" explicitly asks for "the open-option model (FR-48)". FR-48 requires an open option to be the same option, with all its effects, flags and texts, whether it's taken from the offer message, the money view or the job view. The layout has no home for open options (licences, moped, card, loan, jobs, experience). Nor does it place:
  - unexpected expenses (a separate list with amounts and flags)
  - the fixed lists (flags, mechanisms, activity kinds, senders, LK20 codes)
  - the ending texts per mechanism and sign
  - the system-cause explanations
  - the example purchases
  - the disclosures D1-D26

  Each placement decides whether a change is "mechanics" (inside the fingerprint) and whether the engine or the content owns it. For example, the engine sets `owns_moped`, while content options set other flags. Content authors and engine builders will split this differently.
- **Fix:** extend the AD-7 layout line:
  - **Folders:** `library/vN/` also holds `options/` (each open option defined once, referenced by id from its offer message and listed in the money and job views), `expenses/`, `texts/` (endings, system causes, purchases, disclosures, teasers), and `lists.yaml` (flags, mechanisms, kinds, senders, LK20).
  - **Fingerprint:** all of these except the text fields are inside the fingerprint.
  - **Flags the engine sets** are declared in `lists.yaml` too.
  - **Simpler FR-48 gate:** the gate then only checks that every reference resolves.

### M7. The database fallback silently drops the course's Supabase requirement

- **Location:** AD-3 (l.77: "The course's Supabase requirement is met by Supabase Postgres alone"); AD-14 "Fallback" (l.185); AD-14 "Ops commands" (l.187).
- **Problem:** The fallback trigger is "spike p90 over 300 ms". Railway and Supabase can't share a region, and AD-4 makes several round trips per mutation, so that trigger is plausible. Switching to Railway Postgres then leaves Supabase used nowhere, and the course requirement (memlog l.9: "Fixed, not open") isn't met. The spine doesn't say which of the two gives way. The 300 ms is the addendum's server budget. NFR-10's 1 s p90 end-to-end is the requirement, and NFR-10 calls its figures "starting values".

  Separately, on the fallback `railway run` from a team machine can't reach Railway's private database hostname. The ops commands need the public proxy URL.
- **Fix:** AD-14:
  - **Fallback trigger:** switch to Railway Postgres only if Supabase pauses or fails, or if the *end-to-end* NFR-10 target (1 s p90 on throttled 4G) fails after round trips are cut.
  - **Record the deviation:** if the switch happens, record it as a deviation from the course's Supabase requirement, for the delivery report (OQ-15).
  - **Ops on the fallback:** the ops commands use the database's public URL.

### M8. Stack versions are out of date, and FastAPI is 21 minor versions behind

- **Location:** Stack table (l.230, l.232, l.236); memlog l.55 ("FastAPI: newest exact release not confirmed").
- **Problem:** Checked on 2026-11-13:
  - **FastAPI:** the latest is **0.162.7** (PyPI, uploaded 2026-11-13; requires Python ≥ 3.11). The spine says "0.141.x" (0.141.1 is from 2026-07-29). FastAPI 0.x minor releases can include breaking changes. A builder who takes "0.141.x" literally pins a line four months old, and another who takes "latest at first build" gets 0.162. The two will diverge.
  - **SQLAlchemy:** the latest is 2.1.8. The spine says "2.1.6 current". The 2.1.x range is still right.
  - **Caddy:** the latest is v2.11.9 (2026-11-05). The spine says "2.11.7 current". The 2.11.x range is still right.
  - **Alembic** 1.20.1 and **PostgreSQL** 17 (Supabase's platform default) are confirmed. Python 3.12 is supported, in security-fix mode, and it matches the reference, which is fine as a deliberate choice.
- **Fix:**
  - **FastAPI:** change the row to "FastAPI 0.162.x (0.162.7, 2026-11-13); exact pin in `uv.lock` at first build".
  - **Stale "current" notes:** drop or refresh the notes on the SQLAlchemy and Caddy rows.
  - **Memlog:** add one `(version)` memlog entry.
  - Sources: [PyPI fastapi 0.162.7](https://pypi.org/pypi/fastapi/0.162.7/json), [PyPI fastapi 0.141.1](https://pypi.org/pypi/fastapi/0.141.1/json), [PyPI sqlalchemy](https://pypi.org/pypi/sqlalchemy/json), [PyPI alembic](https://pypi.org/pypi/alembic/json), [Caddy latest release](https://api.github.com/repos/caddyserver/caddy/releases/latest).

---

## Low

### L1. `binds` and the capability map disagree

- **Location:** frontmatter `binds` (l.11); Capability map (l.309-326).
- **Problem:**
  - **Missing from `binds`:** FR-10, FR-19, FR-35, FR-37, FR-38, FR-39 and FR-56. FR-38 and FR-39 are Core engine calculations, and FR-56 shows engine figures. The map covers FR-35 to FR-39 and FR-56 only by range.
  - **Missing from the map:** FR-10 (the avatar is a start input in AD-2) and FR-19 (tips are content, with costs from the engine).
- **Fix:** add the seven IDs to `binds`. Add FR-10 to the "Start" row and FR-19 to the "Content and scheduling" row.

### L2. Repeats of start, restart and end have nowhere to store their `request_id`

- **Location:** AD-4 Rule (l.83); AD-5 (`request_id` unique per playthrough, l.110); ER (l.261-279).
- **Problem:** A life end deletes the playthrough and its `action_log`, so a repeated "end" can't return "the same result". It would find no playthrough and get `404`.
- **Fix:** AD-4: "Life operations are idempotent by state, not by log. A repeated start returns the existing playthrough if its first `action_log` row has that `request_id`; a repeated end with no playthrough returns `200` with the current view." Alternatively, add a `last_life_request_id` column on `users`.

### L3. The seed script must use the pipeline, not just the engine

- **Location:** AD-14 "Migrations and seeding" (l.182: "scripted play … through the engine") vs AD-4 (l.83: "nothing else writes game state").
- **Problem:** NFR-6 needs seeded users whose cause links and replay work, so they need `action_log` rows. A seed script that runs the engine in memory and then writes the snapshot and the log is a second writer.
- **Fix:** "Seed scripts submit each stored action through the AD-4 pipeline in-process."

### L4. Account deletion relies on every table cascading

- **Location:** ER (l.261-279); AD-15 (l.204).
- **Problem:** FR-44 says the address and the game data "are gone". Nothing says how a future table keyed by `user_id` is cleaned up. App-level deletes and FK cascades will mix.
- **Fix:** one line under the ER: "Every table keyed by `user_id` has `ON DELETE CASCADE`. The only exception is `tester_codes`, which is keyed by address."

### L5. The `auth_attempts` address column is named two ways, and the hash key is unnamed

- **Location:** AD-10 "Limits" (l.144: "normalized address or null") vs ER (l.273: `address_key`); AD-10 "Network" (l.145: "keyed hash").
- **Problem:** It's unclear whether the address is stored in clear or hashed. Also, no setting names the key for the keyed hashes, and the startup guard in AD-14 covers only `JWT_SECRET`.
- **Fix:** "Address and network are stored as HMAC-SHA256 with `JWT_SECRET`." Or name a second secret and add it to the AD-14 guard.

### L6. Two small gaps at the API boundary: GET requests and auth error codes

- **Location:** AD-10 cookie (l.142: `SameSite=Lax`); AD-13 status table (l.167-173).
- **Problem:**
  - **GET requests:** Lax still sends the cookie on top-level cross-site GETs, and nothing forbids a state change on GET (a logout link, for example).
  - **Auth error codes:** the table has no codes for auth form failures (wrong password on login, change or delete; a used or expired reset link, FR-3).
- **Fix:**
  - **GET:** "No request changes state on GET."
  - **Codes:** add `401 login_failed` (neutral), `403 wrong_password` (change or delete) and `410 reset_link_invalid` (used or expired).

### L7. `docker compose up` should not need a copied `.env`

- **Location:** AD-14 "One image, one settings file" (l.180).
- **Problem:** `APP_ENV` has no default, and the app refuses to start without it. The reconcile fix "compose.yaml sets `local`" didn't land. If compose reads `APP_ENV` from `.env`, the examiner's one-command start (NFR-6) fails until they copy `.env.example`.
- **Fix:** "`compose.yaml` sets `APP_ENV=local` and every local default inline; `.env` is optional."

### L8. The 300 ms CI test can't measure the real budget

- **Location:** Performance convention (l.221).
- **Problem:** In CI the database sits on the same host, so the test says nothing about Amsterdam to Frankfurt. On shared runners it will also be flaky.
- **Fix:** "The CI test is a regression bound with headroom. The p90 is taken from the logged server time in the playtest environment (spike and playtest)."

### L9. There's no rollback rule for playtest deploys

- **Location:** AD-14 (l.182-188); Deferred "Zero-downtime deploys" (l.341).
- **Problem:** Redeploying an earlier image after a deploy that ran a migration or a `state_schema` upgrade leaves the old code facing tables or documents it can't read. That's an operations gap, though not a divergence between stories.
- **Fix:** one line in AD-14: "During the playtest, migrations and `state_schema` steps only add. Rollback means redeploying the previous image, and only if the deploy had neither."

### L10. Supabase's pause depends on database activity, so the spike should confirm it

- **Location:** Playtest limits table (l.195); Monitoring convention (l.220).
- **Problem:** Supabase pauses Free projects after a week of too little *database* activity. Its own FAQ says a few requests a day is "usually enough … not guaranteed". AD-3 turns the Data API off, so the daily login check's database queries are the only activity.
- **Fix:** add to the sprint-1 spike checks: "Supabase counts the pooled database traffic from the daily check as activity (project not marked idle after 7 days)". Sources: [Supabase: Project Pausing](https://supabase.com/docs/guides/platform/free-project-pausing), [Supabase FAQ](https://supabase.com/kb/faqs/platform/free-project-pausing).

### L11. Bloat: lines that restate the PRD or are story-level

These cost readers attention without fixing anything that could diverge. They can be cut or shortened (about 10 lines):
- **AD-7:** "Dahl decides engine-vs-key disagreements, and the key changes only after an independent second calculation" (PRD NFR-4 process), and "The check writes a report file, and the final one is committed before delivery" (a delivery task).
- **AD-8:** "Bank progress is measured at month open, after interest on savings", and the fill-order parenthesis. Both restate FR-55. Keep "under FR-55's cap and fill order".
- **AD-9:** "Order inside the month follows FR-12 exactly, including …". This restates FR-12 and isn't a payment-step invariant.
- **AD-10 "Revocation":** this restates FR-3, FR-4 and FR-5. Shorten it to "Revocation deletes session rows as FR-3, FR-4, FR-5 and FR-44 say; a completed reset also creates a new row and clears the address's failed-login count."
- **AD-15:** "buckets day-based metrics in Europe/Oslo time" duplicates the Time convention. Keep one.

---

## Checked and passing

- **Mermaid:** all four diagrams parse with mermaid 11.4.1 (flowchart-v2, sequence, flowchart-v2, er).
- **Sources:** every path in `sources` exists.
- **Already fixed:** the items from both reconcile passes are applied and correct (player view, sender per environment, Data API and RLS, `APP_ENV` guard, session discipline, attempt table, limits table, region deviation, records hook, migrations and seeding, and so on). They aren't repeated here.
- **Deferred rows that are sound:** frontend, device matrix, event authoring, go-live email, privacy review, backups, zero-downtime deploys, V2 and real-time minigames. Each one is bounded by an AD or has no consumer in the MVP.
- **Superseded memlog decisions don't reappear:** Supabase Auth, GoTrue, Koyeb, Brevo, the backend serving the frontend, and the zero-cost NFR-5 are all absent from the spine.
