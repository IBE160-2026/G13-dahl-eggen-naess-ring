---
title: Adversarial review — two compliant units that still collide
created: 2026-11-13
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-13, after both reconcile passes)
consulted: ../.memlog.md, ../../../prds/prd-IBE160-G13-2026-10-22/prd.md, addendum.md
lens: For each hole, two units one level down (epics or stories built by different developers) that each obey every AD to the letter and still build incompatibly.
scope: backend and infra only. Frontend is flagged only where the backend boundary itself is ambiguous. Each fix is the smallest tightening, with no new services or features. Items already fixed by reconcile-prd.md and reconcile-reference-memlog.md are not repeated.
---

# Adversarial review: compliant pairs that collide

**Verdict:** the spine is not yet safe to build on. Four seams let two separately built stories each obey every AD and still build incompatible systems. Each seam closes with a sentence or two, and none needs a new service.

| Severity | Count |
| --- | --- |
| Critical | 0 |
| High | 4 |
| Medium | 12 |
| Low | 12 |

Each hole below names Unit A and Unit B, what each does while obeying the ADs, where they collide, and the smallest fix: which AD changes and the exact sentence to add.

---

## High

### H1. Requests don't name their playthrough, so a stale device can act on a new life or delete one

- **Unit A, the "Play again / start over" story:** it follows AD-4 (locked on the `users` row, `request_id` stored) and AD-5 (one row per user, and a new life deletes the old row in the same transaction). It locks the user, deletes whatever playthrough exists, and inserts a new one.
- **Unit B, the game endpoints (choice, money action, continue):** they follow AD-4. The body carries `request_id`, `month` and `plan_version`, and the pipeline loads "the playthrough row". AD-5 guarantees one row per user, so the pipeline loads it by `user_id`.
- **Collision:**
  - Device 1 starts a new life and reaches month 3. Device 2 still shows the old life at month 3 and sends a choice for month 3. The month check passes against the new life, so the choice is applied to a life that device never showed, which breaks FR-8.
  - Device 2, on a stale ending screen, presses **Play again**. Unit A deletes the life device 1 is playing and draws a new pengegave.
  - `state_version` restarts with each playthrough, so a client that compares version numbers (AD-13, FR-8) can miss the switch.
  - AD-13's 404 "another player's or a deleted playthrough" only makes sense if requests name a playthrough, and AD-4 never says they do.
- **Fix:**
  - AD-4, add: *"Every game request, and every end, restart or start, names the `playthrough_id` it acts on or replaces (null only for an account's first start). The pipeline proceeds only if that id is the user's current row. Otherwise it refuses with 404 `not_found` for a game request, or 409 `game_changed` for a life request."*
  - AD-13, add: *"The player view carries `playthrough_id` next to `state_version`. The pair, not the number alone, identifies a state."*

### H2. Content can reach the client by a path that bypasses the player view, leaking answers and hidden effects

- **Unit A, a content-delivery story:** the Norwegian texts for events, options, messages and activities live only in backend YAML (AD-7). The frontend needs them, so this story adds a read-only `GET /api/content/{library_version}` that returns the parsed library. It follows AD-2 (no figures computed on the client), AD-13 (the route is in the committed schema, and it isn't a game response) and AD-7.
- **Unit B, the player-view story:** it builds `view(state) → PlayerView` exactly as AD-13 says. That signature has no `content` argument, so the view carries ids and figures but no texts.
- **Collision:** the parsed library contains:
  - every option's wellbeing effect, which FR-13 and team decision #79 hide until the pick
  - every minigame's "situations and right answers" (addendum, option type "minigame"), which makes "the server judges every answer" (FR-51) meaningless
  - every future event, follow-up and boomerang link

  AD-13's exclusion list is bypassed entirely, and the spine allows it.
- **Fix (AD-13):** replace "`view(state) → PlayerView`" with: *"`view(state, content) → PlayerView`, which resolves texts only for the items currently visible to the player. No endpoint serves library or config files, or their parsed form. The disclosure texts ('Om tallene', FR-40) are the only content served outside the view. The view also leaves out the wellbeing effects of options not yet picked (FR-13)."*

### H3. "Published" content version is undefined, so the CI freeze and the content epic can't both work

- **Unit A, the fingerprint gate in CI (AD-7):** "A published version is frozen" needs a test for "published", and the spine gives none. The CI developer treats every version folder merged to `main` as published, so the fingerprint is frozen at merge.
- **Unit B, the content epic:** 40-60 events, activities and messages are added over several sprints, PR by PR, to `library/v1`. AD-7 says a mechanics change needs a new version folder.
- **Collision:**
  - Under Unit A, every content PR either fails CI or opens `v2`, `v3`, … one per PR.
  - Local playthroughs and seeded users pin these intermediate versions, and "versions stay while any playthrough uses them" keeps them for good.
  - If Unit A instead treats nothing as published until the playtest, nothing is frozen at all.
  - AD-7's "until tuning is frozen" gate switch also has no home. It could be an env var in CI, a manifest field, or a date, and different builders will pick differently.
- **Fix (AD-7), add:** *"Each version manifest has `published: true|false`. An unpublished version may change freely and can be pinned only in `local`/`ci`. It becomes published in the PR that first sends it to the `playtest` branch, and from then on its fingerprint is frozen. The same flag is the tuning freeze: for a published version, every content-check gate fails CI."*

### H4. Content flags and typed engine state are two owners of the same fact

- **Unit A, the moped story (FR-29, likewise the licence, job and BSU stories):** AD-5 defers the state fields to the engine stories. This story owns `state.belongings.moped`. The "sell the moped" money action clears it, and NFR-7's refusal "selling something the player doesn't have" reads it.
- **Unit B, the content and option-effects story:** event options "set or clear flags" (addendum, option fields). Required and blocking flags drive eligibility (FR-46b, FR-55), and room layers follow flags (FR-34). A "buy a used moped" option, or the gift moped, sets the flag `har_moped`.
- **Collision:**
  - Selling through the money action clears the field but not the flag. The room keeps showing the moped, and moped events are still drawn.
  - A moped bought through an event sets the flag but not the field. Selling it is then refused, and no fuel or insurance is charged.
- **Fix (AD-8, or AD-1), add:** *"A fact the engine holds as a typed field (belongings, licences, job, BSU, card, loans, payment plan) is visible to content only as a derived flag, computed from that field by one engine function. Content may require or block derived flags but never set or clear them. An option changes such a fact only through its typed effect. The content flag list marks which flags are derived, and the content check rejects an option that sets one."*

---

## Medium

### M1. The lock order between the users row and the playthrough row is open, so requests can deadlock

- **Unit A, the game pipeline (AD-4):** it runs `FOR UPDATE` on the playthrough row, then the engine step and the writes, then `records.on_action` (AD-15), then `users.last_active_at` (Accounts convention), then commit. The auth dependency writes at most once a minute (AD-10), so it often takes no users-row lock first.
- **Unit B, end, restart and account deletion (AD-4 "locked on the `users` row instead"; FR-44):** it locks `users`, then updates the record before the playthrough is deleted (AD-15), then deletes the playthrough.
- **Collision:** with two devices, A holds the playthrough row and waits for `users` or `playtest_records`, while B holds those and waits for the playthrough. Postgres aborts one request with a deadlock error, a 500 that AD-13 has no shape for.
- **Fix (AD-4), add:** *"Every pipeline call, game or life, and every account deletion first takes `SELECT … FROM users WHERE id = :uid FOR UPDATE`, then the playthrough row, then the record. No code locks them in another order."*

### M2. Ending a life early, and where life requests store their `request_id`

- **Unit A, the "End life early" story:** FR-43 says the ended life "can't be resumed and is deleted", and AD-5 doesn't forbid deleting at end, so this story deletes the row immediately. AD-4 says the `request_id` is "stored", but AD-5 keeps request ids only in `action_log`, which goes with the row.
- **Unit B, the "Start new life" story:** it expects the ended or finished row to still exist. The records hook needs it to tell "starting over before 20" from "playing again after an ending" (FR-50), and the story deletes the row itself in the same transaction.
- **Collision:**
  - A retried end request (response lost) finds no playthrough and gets 404 instead of the same result, which breaks NFR-7.
  - The records hook can't tell the cases apart.
  - Each story stores life request ids somewhere different (a `users` column or `action_log`).
- **Fix (AD-4), add:** *"Ending early sets `status = ended` and keeps the row. Only a start deletes the previous row. A life request's `request_id` and result are stored as an `action_log` row of the playthrough it ends or creates, and a repeat is looked up there."*

### M3. A state upgrade written back by a read path overwrites a confirmed choice

- **Unit A, the state-upgrade story (AD-5, "upgraded on load"):** a shared `load_playthrough()` upgrades old documents and saves the result so the upgrade runs once. `GET /api/…` uses the same loader.
- **Unit B, the pipeline (AD-4):** it locks with `FOR UPDATE` and writes.
- **Collision:** after a deploy that bumps `state_schema`, a GET loads the old document without a lock while a choice commits. The GET then writes the upgraded old document over it. The confirmed choice is lost (FR-6), and `state_version` doesn't change.
- **Fix (AD-5), add:** *"Upgrades run in memory on every load. Read paths never write the playthrough row, and the upgraded document is saved only by the pipeline's own write."*

### M4. `view(state)` has no inputs for data that lives outside the state document

- **Unit A, the player-view story:** it builds `view(state)` (AD-13), which must include "the server time of the last action", and the view is pure (AD-1: no clock).
- **Unit B, the recap/pipeline story and the disclosures story:** the first writes `playthroughs.last_played_at` (a column, AD-5). The second writes `seen_disclosures` per account, outside the state (AD-5).
- **Collision:**
  - The view can't see the column or the account table. One builder puts a timestamp into the state through `apply`, so the state now depends on wall-clock time (AD-6). Another lets the API patch the view afterwards, which makes a second view builder.
  - Which disclosures are new gets decided in three places.
  - Nothing marks which draws the player "has been shown", although AD-13 must leave out the ones they haven't.
  - The 1-hour recap threshold (FR-16, "configuration") has no home. Content config, settings and the frontend are all candidates, and the client ends up comparing a server timestamp with the phone's own clock.
- **Fix (AD-13), add:** *"`view(state, content, last_action_at, seen_disclosure_ids)`. `last_action_at` is `playthroughs.last_played_at`, which the pipeline sets from the transaction time (`now()`). The same `now` goes to `records.on_action` and `action_log.created_at`. The view reads only the visible parts of the state and never the draw store. Every response carries `server_time` and the recap threshold from settings, and the client measures the gap as `server_time − last_action_at`, never against the device clock."*

### M5. `plan_version` has two readings

- **Unit A, the month-plan story (FR-52/53):** it keeps `state.plan_version` and raises it on place, remove, and "same as last month".
- **Unit B, the continue story (AD-4, "for continue, `plan_version`"):** AD-13's view lists `state_version` and nothing called `plan_version`, so this story compares the request's `plan_version` with `state_version`.
- **Collision:**
  - Under B, any money action, pin or minigame answer on the same device between planning and continuing produces `plan_changed` on that same device.
  - Under A, the view has no field for the client to echo back.
- **Fix (AD-4), add:** *"`plan_version` is a counter in the state. Every month-plan change (place, remove, same as last month) raises it, and nothing else does. The player view carries it."*

### M6. Balance changes other than charges have no owner

- **Unit A, the money-actions story (FR-45):** transfers, BSU deposit and withdrawal, extra card payment, early loan payoff, and selling the moped.
- **Unit B, the payment-step story (AD-9: "No other code moves money between accounts").**
- **Collision:**
  - A must either route a transfer through `pay()`, which applies the charge order (card, then current account, then savings) and is wrong for a transfer, or write its own balance code, which breaks AD-9.
  - Income landing, loan payouts, and FR-32b's money-in order (negative account first, then overdue minimums) have no owner.
  - Each builder updates the per-cause parts of each balance its own way (addendum: "payments and withdrawals reduce every part in proportion"). Cause links (FR-36) and the FR-42 ranking then diverge.
- **Fix (AD-9), replace the "No other code…" sentence with:** *"The payment module owns every balance change: `pay()` for charges, `transfer()` between the player's own accounts, and `credit()` for money arriving, which applies FR-32b's money-in order. All three update the per-cause parts, and no other code changes a balance."*

### M7. Draw keys are free-form, and one result can have two creators

- **Unit A, the selection step (AD-8):** it decides the month-37 family message that reports the car-licence gift (FR-30), so it draws the gift under `car-gift:E-xxx`.
- **Unit B, the car-licence story (FR-30):** the gift "applies automatically", so it draws the gift to apply it, under `car-licence-gift`.
- **Collision:**
  - Two creators of one random result: the message says "gift", but the licence isn't granted.
  - Separately, two units that pick the same free-form key in the same month read each other's stored result, because the draw store is keyed by key alone.
- **Fix (AD-6), add:** *"Draw keys are built only by functions in one engine module, one function per draw kind (`<kind>:<content id or slot>`). Each drawn result has one owner, the unit that applies its effect. Any other unit, such as the selection step or a message, reads it from the draw store and never draws it."*

### M8. Config and library versions can be pinned in a pair nobody checked

- **Unit A, the start-life story:** AD-5 and AD-7 pin `config_version` and `library_version`, and this story picks the newest folder of each independently.
- **Unit B, a content author:** they add `config/v2` (renaming a figure key) without a new library version.
- **Collision:** new playthroughs pin (`config v2`, `library v1`), a pair that neither the startup check nor the content check ever validated together. References then fail at runtime.
- **Fix (AD-7), add:** *"Each library manifest names the config version it is built for. A new playthrough pins the newest published library version and that config version, and the content check validates each library version against its named config."*

### M9. Worked-example tests can depend on the play library

- **Unit A, the worked-example test story:** it uses the frozen `config/test-v1` (AD-7). Worked examples 25-28 need activities with given costs and effects, so it loads them from `library/v1`.
- **Unit B, a content author:** they tune activity prices and effects in the unpublished library during OQ-8 tuning.
- **Collision:** the answer key goes red again, which is exactly what the frozen test config was meant to prevent.
- **Fix (AD-7), add:** *"Worked-example tests read only `config/test-vN` and items defined in the test code. They never load a play library version."*

### M10. Two model bases, and two migration heads

- **Unit A, the auth story:** the layer table gives auth "passwords, sessions, attempt limits", so it declares `users`, `sessions`, `auth_attempts` and `reset_links` in `auth/models.py` on its own `DeclarativeBase`.
- **Unit B, the persistence story:** the layer table gives persistence the "SQLAlchemy models", so it declares the playthrough tables on another base in `persistence/models.py`.
- **Collision:**
  - The `playthroughs.user_id → users.id` foreign key crosses two metadata objects and fails at mapper setup.
  - Alembic's `env.py` points at one metadata, so autogenerate misses or drops the other base's tables, and the RLS helper (AD-3) skips them.
  - Separately, two stories that add revisions in parallel create two Alembic heads. `cli schema upgrade` then fails in `preDeployCommand`.
- **Fix (AD-3), add:** *"All tables are declared on one `Base` in `persistence/models/`, which every layer imports and Alembic uses. CI fails if `alembic heads` shows more than one head."*

### M11. The tester code is matched in three places

- **Unit A, the sign-up story:** FR-50 says "a new user whose address is on the list gets that code", and AD-4 lists "tester-code match" as an `ON CONFLICT` write, so this story matches at sign-up.
- **Unit B, the CLI loader story (AD-15):** it loads the list as typed (" Markus@Eksempel.no") and also matches users who already exist.
- **Unit C, the export story:** it joins on email at export time.
- **Collision:**
  - Addresses that weren't normalized never match.
  - Accounts created before the list was loaded have no code under A.
  - The code ends up stored in up to three places that can disagree.
- **Fix (AD-15), replace the tester-code sentences with:** *"The tester code is resolved once, at export, by joining the user's normalized address to `tester_codes`. The loader normalizes each address with the FR-1 function, and nothing else stores or matches codes."* Then drop "tester-code match" from AD-4's `ON CONFLICT` list.

  If the team wants records to carry the code, as the memlog says, the alternative is: "copied into the record when the record row is created, and the loader back-fills existing records".

### M12. The JWT `exp` and the sliding session row disagree

- **Unit A, the login story:** it mints the JWT with `exp` set to 30 minutes, or to 30 days with "stay logged in" (AD-10: the token carries `sid` and `exp`).
- **Unit B, the auth-dependency story:** it slides `expires_at` on the row at most once a minute (AD-10) and renews the cookie's `Max-Age`, but reuses the token.
- **Collision:** a player who keeps playing is logged out when the token's `exp` passes, even though the row is valid. That breaks FR-5's "until … hasn't played for 30 days" and the 30-minute idle rule.
- **Fix (AD-10), add:** *"Whenever the auth dependency writes `expires_at`, it re-issues the cookie with a new JWT whose `exp` equals the new `expires_at`. With 'stay logged in', it renews the cookie's `Max-Age` at the same time."*

---

## Low

### L1. The indexed columns duplicate facts that the state document also holds

- **Unit A, the pipeline:** it sets `current_month = month + 1` on continue, and sets `status` itself.
- **Unit B, the engine:** it holds `month`, the ending, the seed and the content versions in the state, as the addendum's "engine state" list requires.
- **Collision:** the two copies drift on month 60, on endings and on life ends, and the pipeline may load content by the column while the engine uses its own copy.
- **Fix (AD-5), add:** *"The state document is the authority. One persistence function copies the indexed columns from the new state on every write, and no game logic reads them."*

### L2. Whether Caddy strips the `/api` prefix

- **Unit A, Caddy:** it uses `handle_path /api/*`, which strips the prefix.
- **Unit B, the backend:** it declares its routes with the `/api` prefix.
- **Collision:** every request returns 404.
- **Fix (AD-12), add:** *"Caddy forwards `/api/*` and `/openapi.json` with the path unchanged, and the backend's routes carry the `/api` prefix."*

### L3. The `Secure` cookie under `APP_ENV=ci`

- **Unit A, auth:** it sets `Secure` everywhere except `local` (AD-10).
- **Unit B, the CI test harness:** it runs with `APP_ENV=ci` (AD-14) and FastAPI's `TestClient` on `http://testserver`.
- **Collision:** httpx's cookie jar doesn't send `Secure` cookies over http, so every authenticated API test fails.
- **Fix (AD-10):** *"`Secure` everywhere except `APP_ENV=local` and `ci`."*

### L4. The client-address header has no name

- **Unit A, the Caddy story:** it relies on Caddy's default, an appended `X-Forwarded-For`.
- **Unit B, the auth-limits story:** it reads `X-Real-IP`, or falls back to the socket peer.
- **Collision:**
  - If the header is missing, every tester counts as Caddy's own address.
  - If the backend reads the first `X-Forwarded-For` entry, a client can spoof it.
- **Fix (AD-10):** *"Caddy overwrites `X-Client-IP` with `{client_ip}`, and the backend reads only that header for the network key."*

### L5. Attempt keys and the reset cap have several writers

- **Unit A, the login unit:** it writes `address_key` as an HMAC.
- **Unit B, the reset unit:** it clears failed logins with `WHERE address_key = <plain address>`, so FR-2's "reset clears the count" silently fails.
- **Separately:** the email module enforces the daily total cap (AD-11) with its own counter, which may be in memory, while auth counts `reset_request` rows.
- **Fix (AD-10):** *"`address_key` and `network_key` are HMAC-SHA256 under one settings key, computed by one auth function that every writer and reader uses. The daily total reset cap counts `reset_sent` rows, which the email module writes only when Resend accepts an email."*

### L6. Account deletion has two paths

- **Unit A, the inactivity job:** per the Jobs convention ("idempotent deletes") it runs a bulk `DELETE FROM users WHERE last_active_at < …`.
- **Unit B, the FR-44 story:** it deletes the account following AD-15's records and `testers_left` rule.
- **Collision:**
  - The job skips the counter and the lock order (M1).
  - An `UPDATE` on a `playtest_counters` row that doesn't exist yet adds nothing.
- **Fix (AD-15):** *"Every account deletion, by the player or by the inactivity job, goes through one `delete_account(user_id)`. It increments `testers_left` only when `PLAYTEST_RECORDS` is on and the account isn't `is_test`. The counter row is created by its migration."*

### L7. How the CLI seed command enters the pipeline

- **Unit A, the pipeline:** step 1 in AD-4's diagram is "auth", and a start makes its seed with `secrets` (AD-6).
- **Unit B, the CLI seed (AD-14):** it has no session and needs fixed seeds.
- **Collision:** B calls `engine.apply` and writes snapshots itself, which makes a second writer (against AD-4), or patches `secrets`.
- **Fix (AD-4):** *"The pipeline function takes an authenticated `user_id` and, for a start, an optional seed. Routes pass the session's user and never a seed. Only the CLI seed command passes one."*

### L8. Refusal codes and error handlers

- **Unit A, the engine stories:** each one invents its own refusal codes (`option_not_offered` vs `not_offered`).
- **Unit B, the auth story:** it raises FastAPI's `HTTPException(401)`, which returns `{detail}`. Starlette's 404 and 405 do the same, although AD-13 replaces only the 422 handler.
- **Fix (AD-13):** *"Engine refusals are one enum of stable codes, each tagged turn (409) or input (422). Errors are raised only as one `AppError(code, status)`, and the handlers for it, for `RequestValidationError` and for Starlette's `HTTPException` all emit `{code, message, state}`."*

### L9. Which request opens a month, and the month for setup steps

- **Unit A, the continue story:** it closes month M and leaves "when the month opens" (AD-8) for later.
- **Unit B, the GET/view story:** it opens the month lazily on read, so a read writes. Alternatively, the avatar step (FR-10, which comes after the playthrough exists) carries no `month`.
- **Fix (AD-4):** *"Continue is one engine action that closes month M and opens M+1 (rule 1 through interest on savings, then the selection step) in the same transaction. A start opens month 1. Setup steps before the first choice are game requests for month 1. No read path opens a month."*

### L10. What identifies a choice

- **Unit A, the cause-links story (FR-36):** it points at choices by `request_id`.
- **Unit B, the ending-summary story (FR-42):** it breaks ties by "the order the server confirmed them", meaning `action_log` order, which the pure engine can't read (AD-1).
- **Fix (AD-5):** *"Each applied choice gets a sequence number from the state. Cause links and FR-42's tie-break use it, never `request_id` or log order."*

### L11. "In the playtest only" is read as two different settings

- **Unit A, the tester-code loader:** it gates on `APP_ENV == playtest`.
- **Unit B, the records hook:** it gates on `PLAYTEST_RECORDS` (AD-15).
- **Collision:** FR-50's "a test covers both states" can't reach the loader in `ci`.
- **Fix (AD-15):** *"Everything playtest-only (the records hook, the tester-code table and loader, `testers_left`) is gated by `PLAYTEST_RECORDS` alone, never by `APP_ENV`."*

### L12. Where kroner become øre

- **Unit A, the API route:** it converts the player's whole-kroner amount to øre, following "øre inside the engine" (Money convention).
- **Unit B, the engine's money-action story:** it treats action amounts as player inputs in kroner (NFR-7) and converts them itself.
- **Collision:** amounts are converted twice, so everything is 100 times too large. The same risk applies to the view.
- **Fix (Money convention):** *"Engine actions and `PlayerView` carry whole kroner (`int`). Øre exists only in the state document and engine arithmetic, and the conversion happens only inside the engine."*
