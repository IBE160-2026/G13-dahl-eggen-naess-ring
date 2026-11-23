---
title: Adversarial review: compliant pairs that still collide (whole spine, after #116)
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (status final, updated 2026-11-23, after the #116 gate fixes)
consulted: ../.memlog.md (all entries, with the 2026-11-15 to 2026-11-23 amendments read closely), ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (FR-1 to FR-11, FR-12, FR-16, FR-21 to FR-27, FR-31 to FR-33, FR-36 to FR-57, NFR-3, NFR-4, NFR-7), ../../../briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md (Rule Set v1 rules 1-16, worked example 16)
lens: two units one level down (epics or stories built by different people) that each obey every AD to the letter and still build incompatibly
excludes: everything in reviews/review-adversarial.md (2026-11-13) and reviews/review-116-adversarial.md (2026-11-23) that the spine now fixes. Where a parallel review written today (review-2026-11-23-rubric.md, -drift.md, -currency.md) raises the same seam, this report says so and adds only the adversarial angle.
---

# Adversarial review: compliant pairs that still collide

**Verdict:** the spine's structure holds. The 2026-11-13 and #116 seams are closed, and no pair found here needs a new service or a new unit. But eight seams still let two stories each obey every AD and ship incompatible behaviour. Most of them sit where a later amendment added a second path to something the spine fixed once:

- the action *result* is a second projection beside the view
- text placeholders can be filled at two different times
- the "after the plan" previews (#116 bands, FR-49) can be computed in two places
- ledger calls get their tags (#116 flow part, the 2026-11-15 payment-order row) from two sources
- content added after the freeze has no path through the startup check

Each one closes with an AD sentence.

| Severity | Count |
| --- | --- |
| Critical | 0 |
| High | 8 |
| Medium | 13 |
| Low | 11 |

Each finding names Unit A and Unit B, how each obeys the ADs, the collision, and the fix as a sentence for a new or tightened AD.

---

## High

### H1. The action result is a second projection outside the player view

- **Unit A, the pipeline story (AD-4, AD-5):**
  - It returns "result + player view" (sequence diagram), stores "the result part" in `action_log`, and replays it on a repeat `request_id` (NFR-7: "returns the same result as the first time").
  - To make the replay byte-identical, it stores the result as the finished response: rendered Norwegian lines, the figures, the cause links, and the engine's raw result object.
- **Unit B, the view story (AD-13):** it builds `view(...)` with the exclusion test ("a test fails if it holds" the seed, future schedule data, minigame solutions or unpicked wellbeing effects). Nothing makes the result go through that function or that test.
- **Collision:**
  - **Leak.** The engine's result for a boomerang opener holds the drawn follow-up delay, which is future schedule data. A minigame step's result can hold the drawn route. Unit A sends both straight to the client, and AD-13's test never sees them.
  - **Stored text.** The stored result holds the nickname and the relative month placeholder ("januar i fjor") already filled in. That breaks AD-13's "never written into … the action log or a stored text", and a replay a year later reads wrong.
  - **FR-6 on reconnect.** FR-8 makes the client fetch `GET /api/game` when the connection comes back. The view carries no result, so a device that lost the POST response sees the choice applied with no result to show. FR-6 says "the game shows that choice's result when it reconnects".
- **Fix (AD-13, One view function; AD-5):** *"An action's result is engine state, not a separate response: the engine appends it to the open month's results in the state document as ids, integers and cause links, with no rendered text. The view renders the open month's results under the same exclusion test, so `GET /api/game` shows the last result after a reconnect. `action_log` stores only the structured result, and a repeated `request_id` returns the current view with that result marked as the replayed one."*

### H2. Placeholder values can be filled when the text arrives or when it is rendered

- **Unit A, the selection step and messages story (AD-8, FR-54, FR-55):** it stores each arrived message as its content id in the state. The bank message "Du har nådd halvparten av sparemålet ditt" and the interest message ("the interest earned so far passes NOK 50, with the engine's figure") get their figures from the formatting function when the view is built.
- **Unit B, the formatting story (AD-13, Game text):** "finished Norwegian strings with the engine's figures filled in … when the view is built". It fills `{interest_so_far}` and `{progress}` from the current state.
- **Collision:**
  - FR-54 says earlier messages "stay readable for the rest of the playthrough". In month 40, the month-14 interest message shows month 40's interest, and the 50 % message shows today's progress.
  - The same happens to "Hvorfor?" lines and to option result lines that quote a balance.
  - The opposite build stores the rendered string at arrival, which breaks the nickname and relative-month rules (AD-13) and blocks text-only fixes to running playthroughs (NFR-4).
- **Fix (AD-13, Game text):** *"Every figure a text shows is captured as a named parameter when its item enters the state (a message arrives, a result or cause line is created), and the formatting function renders text from the content template plus those stored parameters. Only the nickname and the month placeholder are resolved when the view is built. The content check fails a template whose placeholders aren't supplied by its item kind."*

### H3. "After the plan" figures can be computed by a preview path that differs from continue

The parallel drift review (L2, L3) lists *which* previews the view needs. This finding is about *how* they're computed.

- **Unit A, the view story (#116 Bands; FR-9c, FR-49, FR-57):**
  - It needs the open month's score and parts "with the planned activities applied", the rule 8 trigger status after the plan, goal progress after the plan, and savings-target progress after the plan.
  - It writes a light `preview()` in the view module. The preview sums the planned activities' costs from the current account and adds their capped effects to the parts.
- **Unit B, the month-loop story (AD-4 Months, FR-53):** continue applies the activities in slot order. It re-checks eligibility and payment, pays through `pay()` (card whole-or-nothing, then current account, then savings), drops what fails with a note, and only then runs rule 12 and rule 8.
- **Collision:**
  - A card-payable activity that fits under the limit is previewed as a current-account cost. The preview says "trigger: below zero", and continue finds none.
  - An activity that fails its re-check stays in the preview.
  - The banded score shown before continue differs from the score that month records. The "continue anyway" confirmation (AD-2) then fires on a false trigger.
  - A third build runs the whole continue action on a copy. That opens M+1, draws its event, and makes the view read the draw store, which AD-13 forbids.
- **Fix (AD-4 Months, or AD-9):** *"Continue is composed of one engine function `apply_plan(state, content)`: the planned activities (eligibility, payment, drops), wellbeing and the rule 8 evaluation, with no draws and no month change. This is followed by the December step, `close_month` and `open_month`. The view calls `apply_plan` on a copy to produce every 'after the plan' figure (score, parts, bands, trigger status, goal and target progress), and no other code computes them."*

### H4. Ledger calls can take their flow part and payment-order row from the cause

- **Unit A, the ledger story (AD-9):** "every ledger call also carries one flow class, and a part within it taken from the call's cause". The builder maps the cause kind to the part: an event-option choice gives `purchases`, an activity gives `activities`, a system cause gives `costs`. Since `pay()` "implements the FR-45 payment-order table", the row is inferred from the cause too: an option or activity choice gets the whole-or-nothing card row.
- **Unit B, the fixed-cost step story (rule 1, FR-12 "costs started by a choice", FR-23):** an everyday cost started by an event option (a subscription, moped fuel, borrowing the car) is charged at the fixed-cost step, linked to the option as its cause (FR-36 "effects that continue").
- **Collision:**
  - Under Unit A, the subscription's monthly fee lands in `out.purchases`, not `out.costs`, so the month summary's "fixed costs" line and Året differ between builds.
  - The fee is charged by the event-option row: card whole-or-nothing with a "card was declined" message. The PRD charges it by the card-payable-cost row: card as far as it fits, the rest from the account, no decline message.
  - One-off shift pay is caused by the shift (a slot item), so it could be mapped to `activities` rather than `in.wage`.
- **Fix (AD-9, Flow classes):** *"The calling step passes the payment-order row, the flow class and the part explicitly, from one engine table keyed by what is being paid (cost step, spending step, option, activity, instalment, money action …). The cause is used only for cause parts and cause links, and the ledger never derives a row or a part from it."*

### H5. Money actions in a crisis month have no fixed ledger function, so the rule 8 money-in order applies in one build and not the other

- **Unit A, the money-actions story (AD-9):**
  - "`transfer()` moves money between the player's own accounts". The builder implements savings → current, withdrawing the BSU, and also the extra card payment and early payoff (card and loans are the player's balances, and their class is `internal`) as `transfer()` calls.
  - `transfer()` only moves money and doesn't use "current account, then savings".
- **Unit B, the crisis story (rule 8, FR-32b):** "Money that a crisis choice or a money action brings in during a crisis month goes first to a negative current account, then to overdue card minimums". AD-9 puts that order in `receive()`.
- **Collision:**
  - In a crisis month with an overdue minimum, the player moves NOK 2,000 from savings, or withdraws the BSU, which is a listed crisis action (FR-32). Under Unit A the overdue minimum stays unpaid, so the missed-minimum trigger stays true and the crisis continues. Under Unit B (a `receive()` path) it is paid and the crisis ends.
  - The extra card payment as `transfer()` refuses an amount the current account can't cover alone, while FR-45's row says "current account, then savings".
  - The PRD doesn't say whether moving the player's own savings "brings in" money. The spine must decide it so that the engine is built one way.
- **Fix (AD-9, One writer):** *"Each money action maps to exactly one ledger function and FR-45 row in one engine table: moving money between current account and savings, and BSU deposits, are `transfer()`; extra card payment and early payoff are `pay()` on their FR-45 row; selling and withdrawing the BSU are `receive()` into the current account. In a crisis month, the rule 8 money-in order runs after every money action or crisis choice that raises the current account, whichever function made the call."* If the team wants own-money transfers left out, the sentence says so instead. One of the two must be written.

### H6. A field added to the content model after the freeze stops every later deploy, or forces a hard-coded figure

- **Unit A, an engine story after the playtest freeze (AD-1, AD-7):** the engine owns the content model. A fix or extension adds a required config figure. #116 itself did this, adding `start_year` and the band offset two weeks before the freeze. The new config version folder (`config/v2`) carries the figure.
- **Unit B, the content loader (AD-7 Loading, Freeze):** "all versions are loaded and checked … once at startup, and startup fails on any error". A frozen `config/v1` can't be edited and can't be removed, and running playthroughs pin it.
- **Collision:**
  - The new required field makes `config/v1` invalid, so startup fails. Railway's healthcheck then rejects every deploy for the rest of the playtest.
  - Making the field optional with a default in the engine model puts a game figure in code, which breaks NFR-4 ("never hard-coded") and the Config convention. It also isn't pinned, so changing the default later changes running playthroughs.
  - Each builder picks a different escape: the model default, an unfrozen edit to v1, or a per-version `if`.
- **Fix (AD-7, Loading):** *"A content-model field added after any version is frozen is optional in the model, and `content/config/backfill.yaml` gives its value for each older version, with source and date. The loader fills it before validation, the fingerprint of the frozen folder is unchanged, and the content check fails if a frozen version lacks a value for a field that has no backfill. The engine never supplies a default for a game figure."*

### H7. Draws are reproducible only on the machine that made them

- **Unit A, the content loader (AD-7):** it builds each collection by walking `library/vN/events/` and the other folders with `Path.iterdir()` or `glob()`. Python returns these in arbitrary, filesystem-dependent order (APFS on the team's Macs, overlayfs in the CI container and on Railway).
- **Unit B, the selection step and draws (AD-6, AD-8):** "every draw is derived from `(seed, month, draw key)` by one draw function". It turns the derived number into an index into the eligible list as it receives it. The derivation itself isn't named, so one builder uses `hash()`, which Python salts per process.
- **Collision:**
  - The same seed draws different events and messages on a laptop, in CI and on Railway.
  - The CI seed-state assertions (AD-14) pass in one place and fail in the other.
  - Replay checks (AD-6) fail between builds, and the content check's seeded statistics move without any content change.
- **Fix (AD-6, Seed and draws):** *"The draw function derives its value with SHA-256 over a canonical encoding of `(seed, month, draw key)`, never `hash()` or `random`. The loader returns every collection sorted by content id, and the selection step sorts each eligible list by content id before indexing into it."*

### H8. Screens with no pinned content version have no view

The parallel rubric review (M2) raises the missing answer for "no playthrough" and "ended". This finding adds the content-version and play-again angles.

- **Unit A, the view story (AD-13):** `view(state, content, …)` needs a state and that state's pinned content. With no playthrough (straight after sign-up), or with an `ended` one ("only a `completed` life is shown again", AD-5), it returns a view with `playthrough_id: null` and no game.
- **Unit B, the start and setup stories (AD-4, FR-9, FR-43):**
  - The life-goal screen comes first and must show the three goals with their targets (NOK 100,000, NOK 30,000 buffer, the NOK 60,000 experience). Those are config figures the frontend may not hard-code (NFR-4) and no endpoint may serve (AD-13).
  - A start must name "the playthrough it … replaces".
- **Collision:**
  - **Play again after ending early.** The client sends the view's `playthrough_id: null`. The pipeline finds an `ended` row and refuses with `409 game_changed`, every time, so the player is stuck after "end life early".
  - **Goal figures.** The goal screen either hard-codes the figures or shows figures from a different version than the start pins. In local, newest library; in the playtest, newest frozen.
  - **"Om tallene".** The page is served outside the view (AD-13) and picks its library version on its own, so its disclosure texts can differ from those the game showed from the pinned version.
- **Fix (AD-13, One view function; AD-7, Manifest):** *"With no playthrough or an `ended` one, the view is built from the versions a start would pin now, chosen by one shell function that the start action also uses; it carries the current row's `playthrough_id` (null only with no row), its `status`, and the start screens' texts and figures. 'Om tallene' renders from the current playthrough's pinned library, or from those same start versions when none is shown. Disclosure ids keep their meaning across library versions, and the content check enforces it."*

---

## Medium

### M1. A retried start looks for its `request_id` in a playthrough that no longer exists

- **Unit A, the pipeline (AD-4, AD-5):**
  - `request_id` is "unique per playthrough", and the request names `playthrough_id`. The builder looks the repeat up with `WHERE playthrough_id = :request.playthrough_id AND request_id = :rid`, then checks staleness.
- **Unit B, the life-request story (AD-4 Life requests):** a start's `request_id` "is stored as an `action_log` row of the playthrough it … creates".
- **Collision:**
  - A start whose response was lost is retried with the old `playthrough_id`, which was deleted in the same transaction. The lookup misses, and the retry gets `409 game_changed` instead of the stored result (NFR-7).
  - An account's first start, retried with `playthrough_id: null`, misses too. Depending on the order of checks, it becomes `409` or an insert that hits the unique `user_id` and returns a 500.
- **Fix (AD-4, Protocol fields):** *"Right after the locks, the pipeline looks up `request_id` in the `action_log` of the user's current playthrough, whatever the request names, and returns the stored result on a hit; the `playthrough_id`, month and `plan_version` checks run only on a miss."*

### M2. Account endpoints are retried like game actions but aren't idempotent

- **Unit A, the frontend's FR-6 retry wrapper (AD-2 boundary):** FR-6 says "tries again when the connection is back", so the client wraps every `POST /api/*` in one retry helper.
- **Unit B, the account stories (AD-10, AD-13):** sign-up, login, password change, nickname change and account deletion carry no `request_id`. Only game actions are idempotent (AD-4).
- **Collision:**
  - A sign-up whose response was lost is retried. It gets `409 email_in_use` for the player's own new account, and the first response's session cookie never arrived. FR-1's 2-minute path ends at "address in use".
  - A retried password change answers `403 wrong_password`, because the first try already changed it.
  - A retried deletion answers `401`.
- **Fix (AD-2 or AD-13):** *"Only `POST /api/game/actions` is retried automatically, with the same `request_id`. Account, session and disclosure requests are never retried automatically; after a lost response the client fetches `GET /api/game` or shows the login screen."* The alternative is to give the sign-up and password-change bodies a `request_id` too.

### M3. The inactivity job and `delete_account` can delete the wrong accounts, or miss some, or count one twice

The parallel rubric review (M5) fixes the worker count. These are the collisions that remain with one worker.

- **Unit A, the sign-up and login stories (AD-10, Accounts):** `users.last_active_at` "is written only by the auth dependency". Sign-up and login are not authenticated requests, so a new account starts with `last_active_at` null.
- **Unit B, the daily jobs (Jobs; AD-14 "two instances during a deploy overlap"):** they select `WHERE last_active_at < now − 12 months` and call `delete_account` for each id. The job starts in each instance's lifespan.
- **Collision:**
  - An account that signs up and never makes another authenticated request has `NULL < …`, so it is never deleted (NFR-3).
  - The job selects the candidates before the lock. A player who logs back in between selection and deletion is deleted anyway.
  - During a deploy overlap, both instances run the job. The second `delete_account` for the same id finds no row but still adds one to `testers_left` if it increments unconditionally.
- **Fix (Accounts row; AD-15 Account deletion):** *"`users.last_active_at` is NOT NULL and set to the creation time at sign-up. The inactivity job re-reads `last_active_at` after taking the `users` lock and skips the account if it is recent. `delete_account` adds to `testers_left` only when its `DELETE … RETURNING` removed the row. Each daily job runs at a fixed UTC hour under `pg_try_advisory_xact_lock`, so one instance runs it."*

### M4. The session is checked before the lock, so revocation and deletion race the pipeline

Sessions in the lock order and who commits are in the parallel rubric review (M3, M4). This finding is about the gap that remains after those fixes.

- **Unit A, the auth dependency (AD-10):** it checks the JWT and the `sessions` row first, then hands `user_id` to the pipeline.
- **Unit B, the revocation stories (FR-4, FR-5 "log out on all devices", FR-44, reset):**
  - They delete session rows, or the user, under the `users` lock (AD-4 lists only "account deletion").
  - Password change, "log out on all devices" and reset aren't in AD-4's lock list at all.
- **Collision:**
  - A choice that passed the session check just before "log out on all devices" commits afterwards. FR-5 says "a device that was logged out from somewhere else can't make a choice".
  - After `delete_account` commits, a pipeline that waited on `users FOR UPDATE` finds no row. It returns a 500, or for a first start, inserts a playthrough that fails its foreign key.
  - The same 500 hits a disclosure upsert racing the deletion.
- **Fix (AD-4, Lock order; AD-10, Revocation):** *"Password change, 'log out on all devices' and reset also take the `users` lock first. After taking the `users` lock, the pipeline re-reads the session row and the user row, and answers `401 not_logged_in` if either is gone. A foreign-key violation on a user-keyed insert is answered the same way."*

### M5. The seed script can't pin content versions through the pipeline

The parallel rubric review (H3) covers the seed assertions during tuning. This finding is about the pipeline's input.

- **Unit A, the seed CLI (AD-14):** "seeded users … each with a fixed seed and pinned content versions", submitted "through the pipeline in-process" (AD-4).
- **Unit B, the pipeline's start (AD-4, AD-7):** it takes "for a start an optional seed" and nothing else. It pins "the newest library" in `local` and `ci`.
- **Collision:**
  - When `library/v2` appears, every seeded user silently moves to v2. The stored option ids and minigame answers (FR-51: seeded users "already hold a licence", earned by playing the drawn route) may not exist in v2, so the seed script fails or reaches different states.
  - The CI assertion goes red on a content PR that touched no seeded path.
  - A builder works around it by patching the "newest version" lookup in the seed script, which creates a second pinning rule.
- **Fix (AD-4, One pipeline):** *"For a start, the pipeline takes an optional `(seed, library_version)` pair, and only the CLI seed command passes it; the config version follows the library manifest. Each seeded user names its library version in the seed script."*

### M6. Next.js server code can call `/api`, and the cookie it gets back never reaches the browser

- **Unit A, the frontend team's Next.js app (AD-12, amended 2026-11-22):** it renders the hub with a server component that fetches `GET {PUBLIC_BASE_URL}/api/game`, passing the browser's cookie along. AD-2 ("the client talks only to `/api/*`") is obeyed, and AD-10 forbids only sign-up, login and reset through Next.js code.
- **Unit B, the auth dependency (AD-10):** it slides the session at most once a minute "and whenever it does, it re-issues the cookie with a new JWT".
- **Collision:**
  - The `Set-Cookie` on a server-side fetch stays in the Next.js function and never reaches the browser.
  - If the slide happened on such a fetch, the row moved but the browser kept the old JWT. The next slide may not come within the minute, so the browser's JWT expires while the row is valid.
  - Next.js may also cache the server-side fetch of the player view unless the fetch itself opts out. The backend's `Cache-Control: no-store` doesn't control Next's data cache.
  - The visitor's address on that path is the function's, which is harmless today only because no limited endpoint is called there.
- **Fix (AD-12, Playtest):** *"Every `/api` request is made by the browser through the proxy; Next.js server code (server components, route handlers, middleware) never calls `/api`, so every `Set-Cookie` reaches the browser and no game data passes through a Next.js cache."* If the spike forces the route-handler fallback in AD-14, that handler must forward `Set-Cookie` unchanged and send `cache: 'no-store'`.

### M7. Errors made by Vercel or Caddy don't have the error shape, and the client can't tell them from refusals

The parallel rubric review (M6) covers the backend's own 500 handler.

- **Unit A, the frontend's error handling (AD-13 Errors):** every non-2xx under `/api` is parsed as `{code, message, state}`. `409` means reload with `state`, `422` means show `message`.
- **Unit B, infra (AD-12, AD-14):**
  - Caddy answers `403` with an empty body when the origin secret is missing, for example when the secret is rotated on one side only.
  - During a deploy restart ("the playtest accepts a short restart"), Caddy returns `502` and Vercel returns its own HTML error page.
- **Collision:**
  - The client's JSON parse fails, and it shows a crash instead of FR-6's "still trying" with a retry of the same `request_id`.
  - A `403` without a body could be read as `wrong_password`, which is also a `403` in AD-13's table.
- **Fix (AD-13, Errors; AD-12, Caddy):** *"A response under `/api` without a JSON body that has `code` is a transport failure: the client retries a game action with the same `request_id` and never shows it as a refusal. Caddy answers a missing origin secret with `403 {"code":"origin_refused"}` and an unreachable backend with `503 {"code":"unavailable"}`, both listed in the schema."*

### M8. A malformed game request is refused before anything has loaded the state that the refusal must return

The response envelope and `server_time` are in the parallel rubric review (M1). This finding is about where the state comes from.

- **Unit A, the error handlers (AD-13):** the `RequestValidationError` handler emits `{code, message, state}`, and NFR-7 says "a refusal … returns the current progress". FastAPI raises the error after resolving dependencies and before the endpoint runs.
- **Unit B, the pipeline (AD-4):** it is the only code that loads and locks the state for a game request, and "a refusal builds its response from the state already loaded".
- **Collision:**
  - The validation handler has no loaded state. One builder returns `state: null`.
  - Another queries the playthrough inside the exception handler. That makes a second view-building path, which runs even for a request whose auth dependency failed. FastAPI collects dependency and body errors together, so the handler can't tell whether the caller was authenticated.
- **Fix (AD-13, Errors):** *"A body that fails validation on `POST /api/game/actions` gets `422 invalid_input` with `state: null`, and the client then fetches `GET /api/game`. Only refusals made inside the pipeline carry `state`, and no exception handler reads the database."*

### M9. Pydantic's lax mode accepts the wrongly typed values NFR-7 refuses, and `plan_version` sits in the envelope

- **Unit A, the request-model story (AD-2, AD-4):** the action union "mirrors the engine's action model" with default Pydantic models. In lax mode, `"5000"` and `5000.0` are accepted for an `int` amount, and the field is coerced.
- **Unit B, the refusal tests (AD-2, Tests convention):** "a missing or wrongly typed field is refused; the refusal tests cover a JSON `null` and an omitted field separately".
- **Collision:**
  - A test that sends `"amount": "5000"` expects `422` and gets the transfer applied.
  - The envelope makes `plan_version?` optional for every action. A continue without it gets `409 plan_changed` from one builder (None ≠ 3) and `422 invalid_input` from another (missing field). The refusal test can't be written against both.
  - "Mirrors" also lets the API union and the engine union drift apart member by member.
- **Fix (AD-4, One endpoint):** *"The request body uses the engine's own action models in strict mode (`strict=True`, unknown fields ignored), with no second union in `api/`. `plan_version` is a required field of the continue member and is not in the envelope."*

### M10. FR-8's idle fetch, built as a timer, keeps a shared PC logged in

- **Unit A, the frontend's FR-8 story (AD-10 "or under FR-8's fetch rules"):** FR-8 says the game "fetches the latest progress whenever the player … has left it idle (default 5 minutes)". The builder sets a 5-minute idle timer that calls `GET /api/game` while the tab is visible.
- **Unit B, the auth dependency (AD-10):** the 30-minute idle limit for a session without "stay logged in" slides on every authenticated request.
- **Collision:** a school PC left open on the game fetches every 5 minutes, so the session never idles out. That is the case FR-5 was written for. AD-10's "never polls in the background" bans polling, but this fetch is allowed by name.
- **Fix (AD-10, Sessions):** *"FR-8's idle and tab-return fetches run on the player's next input after the idle time or the return, never from a timer; no request is made without a player input, a page load, a login or the connection coming back."*

### M11. The per-choice totals behind FR-42 don't say which flow classes count, and which inputs are choices

- **Unit A, the per-choice totals (AD-9 Totals):** "a running total of money … effects per choice". The builder adds every ledger call whose cause is the choice. A consumer loan's payout adds +20,000, and the instalments subtract.
- **Unit B, the ending summary (FR-42):** "moving money between the player's own accounts, taking a loan, and paying down debt count as zero, but the interest that follows counts". It expects the #116 flow classes to decide this.
- **Collision:**
  - Under Unit A, a loan ranks as a large "+" choice, and a card bill paid down by a transfer ranks as "−". FR-42's top three differ between builds.
  - The same gap applies to choice ids. A moped sale's income can be caused by the sell action (its own choice, ranked "+8,800, why it paid off") or by the purchase (net −2,845). AD-9 doesn't say which inputs get a sequence number.
- **Fix (AD-9, Totals; Choice ids):** *"A choice's money total is the sum of `in − out + earned − charged` of the ledger calls whose cause is that choice; `internal` and `tax` calls never count. Event options, open options, crisis options, applied activities and the moped sale are choices and get a sequence number. Transfers, BSU deposits and withdrawals, card and loan payments, levels, pins and plan changes are not, and their ledger calls carry a system cause."*

### M12. `Decimal` in the state document has no defined JSON path

- **Unit A, the engine state model (AD-6):** "rates, hourly wages and hours are `Decimal`", so hours this month (for example 43.33 h after a summer-job cut) and running hour totals sit in the state as `Decimal`.
- **Unit B, the persistence story (AD-5):** it writes `state.model_dump()` into a SQLAlchemy JSONB column. The default JSON serializer raises on `Decimal`, so the builder adds `default=float`.
- **Collision:**
  - The JSONB now holds binary floats. On load, `Decimal(43.3333333)` brings back exactly the float drift that AD-6 and NFR-4 ("never binary floating point") exist to prevent. A rounding at a 0.5 boundary can then land differently after a reload than before it, which breaks FR-12's "same result on reload".
  - The view has the same gap. Pydantic serializes `Decimal` as a JSON string, so the frontend receives `"43.33"` where its generated types expect a number.
- **Fix (AD-5; AD-13):** *"The state document and `action_log` payloads are written with `model_dump(mode="json")`, so every `Decimal` is stored as a string and validated back by the model, and a test round-trips a state with every `Decimal` field. The player view carries no `Decimal`: hours and rates are formatted strings from the formatting function."*

### M13. A raw integer in the view can be formatted by the frontend and by the engine in two ways

- **Unit A, the frontend (AD-13: "raw integers where the UI needs a number"):** the hub chips and Året's bars format the month-total parts with `Intl.NumberFormat('nb-NO')`. That uses U+00A0 as the group separator and U+2212 as the minus sign, and the frontend adds the sign the UX shows («−6 593 kr brukt»).
- **Unit B, the engine formatting function (AD-9: "the formatting function adds the sign the UI shows"; AD-13):** it writes the same figure inside game text with an ASCII space and a hyphen-minus.
- **Collision:**
  - The same amount shows two ways on one screen.
  - A screen reader reads "minus" for one and "dash" or nothing for the other. NFR-2 says "a money change has a sign and a word".
  - The frontend is adding signs, which AD-9 gives to the engine.
- **Fix (AD-13, Game text):** *"Every money figure the UI shows as text, signed flows included, comes from the engine formatting function as a string next to its raw integer, with U+00A0 as the group separator, U+2212 as the minus sign and 'kr' after the number. The frontend uses raw integers only for bar lengths and comparisons."*

---

## Low

### L1. The ending view's "current calendar year" is a year with no months

- **Collision:** AD-13 Calendar gives the ending view year `start_year + 5`. "Money per month" and `year_average` use "the current calendar year". After month 60, a literal build sends twelve nulls and an empty `year_average`, while another sends 2030.
- **Fix (AD-13, Money per month):** *"After month 60, money per month, the year so far and `year_average` refer to game year 5 (`start_year + 4`)."*

### L2. "Time … is passed in" invites the engine to store wall time

- **Collision:** AD-1 says "Time, content and seed are passed in". An engine story that stores `now` in the state, for example for FR-50's "first plan change", is pure but makes the state depend on the clock. Replays (AD-6) then differ.
- **Fix (AD-1):** *"`apply` takes no wall-clock time; only the shell uses `now` (`last_played_at`, `action_log.created_at`, records)."*

### L3. A Caddy healthcheck on Railway gets `403`

- **Collision:** the `railway.ts` story copies `/api/health` to the Caddy service too. Caddy refuses every request without the origin secret (AD-12), so the healthcheck fails and Railway rejects the deploy.
- **Fix (AD-14):** *"Only the backend service has a healthcheck; Caddy's Railway service has none, or uses a dedicated path that Caddy answers itself without the secret and without reaching the backend."*

### L4. Without Caddy, `X-Client-IP` is missing

- **Collision:** the backend reads the client address "only from `X-Client-IP`" (AD-10). FastAPI's `TestClient` in CI and a developer's bare `uvicorn` send none. One builder answers with a 500, and another keys every request to `None`. The FR-1 and FR-2 limit tests then pass or fail by accident.
- **Fix (AD-10, Network):** *"If `X-Client-IP` is missing, `local`/`ci` use a fixed placeholder network, and `playtest` answers 500 and logs it; limit tests set the header explicitly."*

### L5. `PUBLIC_BASE_URL` in compose

- **Collision:** AD-14 requires `PUBLIC_BASE_URL` only outside local and ci. Compose may set it to the Next.js port (`:3000`). Locally, reset links (AD-11, AD-12) then bypass Caddy, and the reset page's `POST /api/...` goes to Next.js, which has no `/api`.
- **Fix (AD-14):** *"`compose.yaml` sets `PUBLIC_BASE_URL` to Caddy's local origin, and settings refuse a value that differs from it in `local`."*

### L6. "Newest" version folder

- **Collision:** the start story sorts folder names as strings, so `v10` comes before `v2`. The content check sorts them by number.
- **Fix (AD-7, Manifest):** *"Versions are ordered by the integer after `v`; `test-vN` folders are never candidates."*

### L7. `testers_left` and the export count people who aren't testers

- **Collision:** anyone who finds the Vercel URL can sign up. `delete_account` adds one to `testers_left` for any non-test account. The export writes rows with an empty code. AD-15's "nothing else matches codes" forbids checking the list at deletion.
- **Fix (AD-15):** *"`delete_account` counts a leaver only if the normalized address is in `tester_codes`, the one other permitted lookup; the export skips accounts with no code."*

### L8. The identity pair used as a cache key

- **Collision:** AD-13 makes `playthrough_id` plus `state_version` "identify a state". The frontend's FR-8 story keeps its cached view when the pair is unchanged. A nickname change, a disclosure seen on another device, or a text-only content deploy changes the view without changing `state_version`, so the old view stays.
- **Fix (AD-13, Identity and time):** *"The pair identifies the game state, not the view; the client always replaces its view with the latest response."*

### L9. "Display only" names three rules, and rule 12 isn't one of them

- **Collision:** rule 12's "if interest was charged on any debt" row can read `totals.interest.charged > 0`, or a separate flag. They agree today but can drift, for example if a fee were ever booked as `charged`.
- **Fix (AD-9, Month totals):** *"No game rule reads the month totals; rule 12's debt-interest row reads the month's interest steps directly."*

### L10. The content check runs with settings that the playtest can override, and doesn't enforce the year rule

- **Collision:**
  - The nickname length is an operational setting (Accounts row). The content check verifies "reads correctly with any nickname the rules allow" (FR-1) at the CI default. A playtest override of the maximum is never checked.
  - AD-13's "content authors never write a year" has no gate.
- **Fix (Config row; AD-7 Freeze):** *"The nickname limits are game figures in `content/config/vN/`, not settings. The schema gate fails a text containing a four-digit year or a month name outside the month placeholder."*

### L11. Two meanings of "a day" for reset limits

- **Collision:** the total reset cap counts "the current UTC day" (AD-10). FR-3's per-address "5 a day" isn't defined, so one builder uses a rolling 24 hours and another the UTC day.
- **Fix (AD-10, Limits):** *"Every 'a day' limit in auth is a rolling 24 hours, except the total reset cap, which follows Resend's UTC day."*

---

## Seams checked and found closed

- Life request vs records hook ordering (AD-15: record updated before the old row is deleted).
- The month boundary of the totals, tax as its own class, interest as separate calls, and the per-month identity (#116 fixes hold against rules 3, 4, 5, 9 and 15, worked example 3 and the payment-order amendment of 2026-11-15).
- Calendar formula for months 1-60 and the ending (AD-13, rule 11).
- Origin secret and the leftmost `X-Forwarded-For` (AD-10, AD-12), apart from the spike checks AD-14 already lists.
- Nickname kept out of state, logs, records and export (AD-13, AD-15). H1 and H2 cover the two places it can still leak into stored text.
- The tester code resolved once at export (AD-15), apart from L7.
