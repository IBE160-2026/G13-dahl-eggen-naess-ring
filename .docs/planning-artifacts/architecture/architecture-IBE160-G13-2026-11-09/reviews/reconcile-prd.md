---
title: Reconcile — ARCHITECTURE-SPINE.md against the PRD and its addendum
created: 2026-11-13
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-13)
inputs:
  - ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (final, 2026-11-13)
  - ../../../prds/prd-IBE160-G13-2026-10-22/addendum.md (2026-11-13)
scope: backend, database, content pipeline, infra and ops up to the HTTP API boundary. Frontend-only items are skipped unless the backend has to enforce or supply something for them.
---

# Reconcile: spine vs PRD + addendum

**Count:** 3 high · 15 medium · 18 low (36 findings)

Line numbers point to the files as they stood on 2026-11-13. "Spine" means `ARCHITECTURE-SPINE.md`. Items the spine correctly defers (frontend, device matrix, endpoint list, state fields, content schemas in detail, go-live email, V2) are not reported.

---

## High

### H1. API `state` is the raw engine document, so it leaks hidden draws and minigame answers

- **Source:** prd.md FR-12 l.600 (every random result is "drawn by the engine once and stored *before the player sees it*"); FR-51 l.1278 (the server "sends one traffic situation at a time, judges each answer"); NFR-4 l.1353, NFR-7 l.1376 (server decides).
- **What didn't land:** AD-5 (l.107) stores the whole engine state as one JSONB document. AD-6 (l.113) stores every drawn result in that state the first time it's drawn. AD-13 (l.155) returns `state` ("the current game state") on game responses and refusals. Nothing says the API returns a player view rather than the document. One builder will serialize the Pydantic state as-is. The client would then see draws the player hasn't met yet: whether family can help before the player asks, the unexpected-expense month, follow-up due months, the car-licence gift result before it's revealed, and the minigame route with its correct answers. That breaks "the server judges every answer" and hands out results early.
- **Fix:** add to AD-13, and cross-reference it from AD-5: *"API responses carry a player view built by one projection function (`engine.view(state) -> PlayerView`). The raw state document is never serialized to the client. The view leaves out the seed, draw-store entries the player hasn't been shown, future schedule data (due follow-ups, drawn expense months) and minigame solutions beyond the current situation."* Add a test that fails if a `PlayerView` field holds any of those keys.

### H2. In the playtest, the email stand-in writes tester addresses and live reset tokens to the log

- **Source:** prd.md NFR-3 l.1339 (no email address in the game's logs); NFR-11 l.1455 and FR-3 l.445 (no email is sent in the playtest); addendum l.294 (the reset command "writes no email address to the log").
- **What didn't land:** AD-14 (l.161) says "every external service falls back to a local stand-in when its key is missing". AD-11 (l.143) says that stand-in "writes the rendered email to the log or a local inbox", and that the playtest runs without the Resend key. So in the playtest, a tester pressing "forgot password" gets the stand-in, and the rendered email (recipient address plus a working reset link) lands in Railway's logs. The spine's own logging convention (l.178: "no email address, password or reset token in any log") also clashes with the stand-in logging a reset link locally.
- **Fix:** state one sender per environment in AD-11:
  - `local`/`ci`: the stand-in writes to a local inbox (a file or directory volume that the README names). If it writes to stdout at all, it writes only the link line, never the address. Record this as the one explicit exception in the Logging convention.
  - `playtest`: a null sender. It sends nothing and logs only `reset_requested user_id=…`, with no address and no token.
  - Resend: only when `RESEND_API_KEY` is set.

  Also make the app refuse to start with the log-writing stand-in when `APP_ENV=playtest`.

### H3. The attempt counters are tied to `users`, so the limits would reveal whether an address has a user

- **Source:** prd.md FR-2 l.432-433 (failed login doesn't reveal email vs password; the pause message "still doesn't reveal whether the address has a user"); FR-3 l.442 (same message whether sent, held back, or no user); FR-1 l.422 (sign-up limit per network); addendum limits table l.283-287.
- **What didn't land:** the structural seed ER (l.229) draws `login_attempts }o--|| users`, a mandatory link to a user. Sign-up attempts have no user, and neither do failed logins or reset requests for unknown addresses. A builder following the ER can only count attempts for existing accounts. Unknown addresses would then never get the pause or the reset cap, so the pause message itself shows that the address exists. The spine is also silent on timing: an unknown address that skips bcrypt answers measurably faster.
- **Fix:** in the ER and AD-10, replace `login_attempts` with `auth_attempts(kind: signup | login | login_failed | reset_request, address_key NULL, network_key, created_at)`, with **no FK to users**, keyed by the normalized address (or its HMAC). Add to AD-10: *"Unknown addresses do the same work as known ones: login verifies against a dummy bcrypt hash, and reset requests write the same rows and return the same response."*

---

## Medium

### M1. Unknown request fields: the PRD ignores them, the spine rejects them

- **Source:** prd.md NFR-7 l.1376 ("The server ignores anything else"); l.1405 (refuse only a *malformed* request: missing field or wrong type); l.1417 (each refusal case has its own test).
- **What didn't land:** AD-2 (l.70) says "Unknown fields are rejected by the request model" (`extra="forbid"`). That adds a refusal case NFR-7 doesn't list, and it contradicts "ignores".
- **Fix:** either change AD-2 to "unknown fields are ignored (`extra="ignore"`); missing or wrongly typed fields are refused", or keep `forbid`, mark it in AD-2 as a deliberate deviation, and ask for NFR-7 to be updated. Either way, add the case to the NFR-7 test list.

### M2. bcrypt's 72-byte limit vs "the maximum allowed is at least 64" characters

- **Source:** addendum limits table l.284 (minimum 8 characters, "the maximum allowed is at least 64"); prd.md FR-1 l.417 and FR-4 l.453 (paste and password managers work).
- **What didn't land:** AD-10 (l.137) picks bcrypt but sets no length rule. bcrypt only uses 72 bytes. A 64-character password with æ/ø/å, or one from a password manager, can exceed that. Current bcrypt releases (5.x) raise an error over 72 bytes, and older ones silently truncate. Builders will diverge: reject, truncate, or pre-hash.
- **Fix:** add to AD-10: *"Passwords are pre-hashed (HMAC-SHA256 with a server key, base64) before bcrypt, so any length up to the configured maximum (default 128 characters) works."* Alternatively, cap at 72 UTF-8 bytes and get the PRD changed. The current spine allows neither.

### M3. Exact money can slip through float at the YAML and JSONB boundaries

- **Source:** prd.md NFR-4 l.1360 (exact decimals or øre, never float; the 8,151.5 → 8,152 example).
- **What didn't land:** AD-6 (l.113) bans float inside the engine. But AD-7 loads Rule Set figures from YAML, and YAML parses `0.0287` or `22.6` as float. AD-5 stores the state as JSONB, which asyncpg/SQLAlchemy decode with `json.loads`, also floats. Both are default behaviours that put float into the engine's inputs.
- **Fix:** add to AD-6 or AD-7: *"Rates and fractions in content YAML are quoted strings, parsed to `Decimal` by the content schema; the loader fails on any float. The state document holds money as integer øre and any non-integer as a string; persistence decodes JSONB with `parse_float=Decimal` (or validates from raw JSON text)."* Add one CI test that round-trips a state containing 8,151.5 → 8,152.

### M4. Token lifetimes and cookie persistence aren't fully named

- **Source:** addendum "For the architecture" l.19 ("Name the token lifetimes"); prd.md FR-5 l.468 (unticked: ends "when the browser is closed, or after 30 minutes with no activity"; ticked: until logout or 30 days without play); addendum l.289-290.
- **What didn't land:** AD-10 (l.137) names the idle limits and the `sessions` columns. It doesn't say:
  - the JWT `exp`
  - whether `expires_at` is absolute or sliding
  - when `last_seen_at` is written (every request is a write per request)
  - what counts as "play" for the 30 days
  - that the cookie must be a *session cookie* (no `Max-Age`) when unticked, so that closing the browser ends the login

  One builder will set a 30-day `Max-Age` for everyone.
- **Fix:** extend AD-10:
  - Unticked: no `Max-Age`/`Expires`.
  - Ticked: `Max-Age` of 30 days, renewed on activity.
  - `expires_at = last_seen_at + idle limit`, sliding.
  - `last_seen_at` is written at most once a minute.
  - The JWT has no `exp` of its own (the session row is the authority), or `exp` equals the idle limit and is re-issued.
  - "Play" means any authenticated request.

### M5. A reset must get the player past the failed-login pause

- **Source:** prd.md FR-2 l.433 ("a reset link (FR-3) always lets the player in, so a classmate can't lock a player out"); addendum l.285 (AG-26).
- **What didn't land:** AD-10 keys the pause by (address, network). A classmate on the same school Wi-Fi can still pause the player's address on that network. The spine doesn't say what a completed reset does: create a session, or clear the pause. If it does neither, the player resets and is still refused for 15 minutes.
- **Fix:** add to AD-10: *"Completing a reset logs that device in directly (new session row) and deletes the address's failed-login rows."*

### M6. Network addresses: granularity, retention, and access logs

- **Source:** prd.md NFR-3 l.1335 ("the attempt limits *briefly* process network addresses"); FR-1 l.422 and FR-2 l.433 (per-network limits that must not block a class).
- **What didn't land:**
  - The Jobs convention (l.180) purges sessions and reset links but not attempt rows, so IP data stays indefinitely.
  - "Network" isn't defined. A full IPv6 address gives every device its own network, which makes the sign-up limit trivial to bypass.
  - Caddy and Uvicorn access logs (Railway keeps stdout) record client IPs, and also query strings.
  - AD-10 says Caddy trusts "only the hosting edge" but doesn't say how. Railway's edge IPs and its header behaviour (append or overwrite) are unverified, so the limits are either spoofable or count everyone as one network.
- **Fix:**
  - AD-10: network key = IPv4 /32 or IPv6 /64, stored as a keyed hash.
  - Jobs convention: purge attempt rows older than the longest window (24 h).
  - Logging convention: access logs off, or without client IP and query string.
  - Add "which header Railway's edge sets, and `trusted_proxies` + `trusted_proxies_strict` in Caddy" to the sprint-1 hosting spike.

### M7. Where the PRD's "configuration" values live is undecided

- **Source:** prd.md FR-1 l.417/422, FR-2 l.433, FR-3 l.441-442, FR-5 l.468, NFR-3 l.1343 (12-month deletion), FR-50 l.1298 (10-minute session gap), FR-16 l.650 (an hour away). All are marked "configuration".
- **What didn't land:** the Config convention (l.179) says "All figures in `content/config/`; all deploy settings in environment variables". These values are neither game figures nor deploy settings. Put in `content/config/vN`, they would be frozen and pinned per playthrough, which is wrong for login limits. Builders will split them differently.
- **Fix:** add a Config row: *"Game figures (pinned per playthrough) in `content/config/vN`. Account, login, privacy and playtest limits in pydantic-settings, with the PRD defaults as code defaults, listed in `.env.example`."*

### M8. "Disclosures seen" is per account, but the spine only has per-playthrough state

- **Source:** prd.md FR-40 l.1212 (seen once per account, across devices *and later playthroughs*); FR-43 l.1258 (the only thing that survives a new life).
- **What didn't land:** AD-2 lists "disclosure seen" as an input, but AD-4 and AD-5 hold state only in the playthrough document, and the ER has no account-level store. A builder who puts it in the playthrough document loses it on FR-43's restart. FR-40 isn't in `binds`.
- **Fix:**
  - AD-5 and ER: add `seen_disclosures(user_id, disclosure_id, seen_at)`, or a column on `users`. It sits outside the playthrough document, survives FR-43, and is deleted with the account.
  - AD-4: write it with an idempotent upsert outside the game pipeline (no `month`, no `plan_version`).
  - Add FR-40 to `binds`.

### M9. Starting a playthrough is outside the pipeline, and "one life at a time" isn't enforced

- **Source:** prd.md FR-43 l.1262-1264 (at most one playthrough in progress; the ended or finished one is deleted when a new life starts); FR-11 l.564-565 (pengegave drawn once, when the goal is confirmed); NFR-3 l.1345.
- **What didn't land:** AD-4 locks an *existing* playthrough row and keys `request_id` per playthrough. Creating one (confirming the goal), ending early, and starting again have no row to lock and no idempotency key. A double tap, or two devices, can create two playthroughs with two pengegave draws. The ER label "current + last finished" also reads as two rows.
- **Fix:** add to AD-4/AD-5:
  - Start, restart and early end run in the pipeline under `SELECT … FOR UPDATE` on the `users` row, with `request_id` idempotency per user.
  - A unique index on `playthroughs(user_id)`: one row per user, with the finished or ended one deleted in the same transaction that creates the new one.
  - The shell makes the seed with `secrets`.

### M10. FR-50 records: the write path and time source are undecided

- **Source:** prd.md FR-50 l.1297-1299 (time measured on the server; records survive FR-43 deletion); FR-43 l.1263.
- **What didn't land:** AD-15 says records are "written" when `PLAYTEST_RECORDS` is on, but the AD-4 pipeline diagram has no records step. The memlog says the action log "serves playtest records", yet FR-43 deletes the action log along with the playthrough. Builders will diverge between updating records in routes, in the pipeline, or deriving them from `action_log` at export, which loses every restarted life.
- **Fix:** add to AD-4/AD-15: *"When `PLAYTEST_RECORDS` is on, the pipeline calls one `records.on_action(user, before, after, action, now)` in the same transaction, after the engine step. Early end and restart update the record before deleting the playthrough. Records are never rebuilt from `action_log`."*

### M11. Account deletion: the record goes, and an unlinked leaver count stays (dropped)

- **Source:** prd.md FR-50 l.1300 (on account deletion the record goes, "and only a count of testers who left is kept, with no link to anyone"); §7.1 l.1485 (testers who deleted their account are reported as a separate count).
- **What didn't land:** AD-15 (l.167) covers surviving *playthrough* deletion and tester-code reuse, but not account deletion. Nothing holds the anonymous leaver count.
- **Fix:** add to AD-15: *"Account deletion deletes the record in the same transaction and increments `playtest_counters.testers_left` (no user or code link). The `tester_codes` row stays, so a re-created account gets the same code."*

### M12. Error codes and HTTP status classes aren't named

- **Source:** addendum l.20 ("the error format **and codes**"); prd.md FR-5 l.467 (a logged-out device's next action shows the login screen); FR-8 l.511; NFR-7 l.1415.
- **What didn't land:** AD-13 fixes the body shape but not the status per class or a starting code list. FastAPI's default validation error (422 `{detail: [...]}`) doesn't match the shape unless it's overridden. One builder returns 400 for a stale month, another 409, another 200 with a flag.
- **Fix:** extend AD-13 with a status map:

  | Status | Codes |
  | --- | --- |
  | 401 | `not_logged_in` (session missing or revoked) |
  | 404 | Another player's or a deleted playthrough |
  | 409 | `wrong_month`, `plan_changed`, `already_chosen`, `game_ended` |
  | 422 | `invalid_input` (custom `RequestValidationError` handler) |
  | 429 | `rate_limited`, with the neutral message |

  The NFR-7 categories form the starting code list.

### M13. Storing `response` in `action_log` can exceed the Supabase Free storage limit

- **Source:** prd.md NFR-11 l.1456 (name the storage limit); NFR-7 l.1416 (a repeat "returns the same result as the first time").
- **What didn't land:** AD-5 stores "response" in every `action_log` row. If that's the full game response (AD-13 puts `state` in it), every row copies the whole state document. A playthrough has a few hundred actions, and the document grows to tens of KB, so 10-20 testers with restarts can approach Supabase Free's 500 MB. Builders will decide differently.
- **Fix:** add to AD-5: *"`action_log.response` stores the result part and `state_version` only. A repeated `request_id` returns that result plus the current player view."* Add a storage estimate to AD-14.

### M14. NFR-11 asks the architecture to name the playtest limits, and the spine doesn't

- **Source:** prd.md NFR-11 l.1456 ("names the provider and tier, and the limits that matter for the test: pausing or sleeping when idle, storage, number of users, and email quota"); OQ-14 l.1536; addendum l.22.
- **What didn't land:** AD-14 and Stack name provider, tier and "sleeping off". They don't name:
  - storage: Supabase Free 500 MB
  - the Supabase pause after 7 days without activity (only implied by the login check)
  - the connection or pooler limits
  - the email quota: none sent in the playtest; Resend Free 100 a day and 3,000 a month at go-live

  The figures are in `.memlog.md` (l.43) but not in the spine.
- **Fix:** add a "Playtest limits" line to AD-14 (or a column in Stack) with these figures and the expected use against each (10-20 testers, storage estimate from M13).

### M15. Backend and database are in different regions, against the addendum's stated condition

- **Source:** addendum "Responsiveness" l.23 ("at most 300 ms … *with the backend and database in the same region*"); prd.md NFR-10; OQ-14 l.1536.
- **What didn't land:** AD-14 puts the backend in Railway EU West (Amsterdam) and the database in Supabase Frankfurt, because Supabase has no Amsterdam region. The spine doesn't say it deviates. The fallback trigger is only "if Supabase fails". Each mutation makes several round trips (session check, `FOR UPDATE`, `request_id` lookup, update, insert, commit), each about 8-10 ms plus pooler overhead.
- **Fix:** record the deviation in AD-14. Cap round trips per mutation (session check and pipeline in one transaction). Make "spike p90 > 300 ms" the explicit trigger for the named fallback (Railway Postgres in the same region, switched by `DATABASE_URL`).

---

## Low

### L1. Cost: "nothing keeps costing" and the whole-period figure

- **Source:** prd.md NFR-5 l.1366; NFR-11 l.1451; addendum l.22.
- **What didn't land:** AD-14 deletes the projects after the analysis. Deleting projects doesn't by itself end Railway's Hobby subscription. The cost is named "for the playtest month", but the environment runs from the sprint-1 spike (November) to the analysis (mid-December), which is likely two billing months. There's no guard if usage passes the USD 5 credit (for example, if the frontend team adds a server).
- **Fix:** AD-14:
  - expected cost for the whole hosted period
  - a Railway usage hard limit
  - after the analysis: delete both projects **and** downgrade or cancel the Hobby plan, with an ops checklist line

### L2. The `Secure` cookie in the local http run

- **Source:** prd.md NFR-6 l.1370 (the examiner's clean-machine run); NFR-1 l.1316 (Safari on Mac is supported).
- **What didn't land:** AD-10 makes the cookie `Secure` unconditionally, and Caddy serves the local stack. Safari has historically refused `Secure` cookies over `http://localhost`, so verify. If it still does, an examiner on Safari can't log in.
- **Fix:** AD-10/AD-14: a `COOKIE_SECURE` setting, true outside `local`. Alternatively, document Caddy's local HTTPS trust step in the README. Test the README run on Safari.

### L3. "Log out on all devices": the spine keeps the current device logged in

- **Source:** prd.md FR-5 l.466.
- **What didn't land:** AD-10 makes **Log out on all devices** delete the user's *other* rows. The PRD's name, and its school-PC example, suggest every device including this one. Only FR-4 (l.455) keeps the current device logged in.
- **Fix:** in AD-10, either delete all rows for this action, or keep it and ask for FR-5 to say "other devices".

### L4. AD-2's input list doesn't match the requests the spine itself needs

- **Source:** prd.md NFR-7 l.1376; FR-49 l.612 (confirm when the plan would set off a trigger; R10); FR-9/FR-10 (goal, avatar); FR-52 l.785 (same as last month); FR-51 (start an attempt).
- **What didn't land:** AD-2 says requests carry "only" the NFR-7 inputs. AD-4 adds `request_id`, `month` and `plan_version`. Continue, the confirm-despite-trigger flag, life goal, avatar, start new life, "same as last month", starting a minigame and the auth form fields aren't listed. Together with `extra="forbid"`, a strict reading refuses them.
- **Fix:** AD-2 lists the full input set, including protocol fields. It also says whether the server requires `confirm: true` to continue with a trigger set, or whether confirmation is client-only.

### L5. The per-item `version` field vs AD-7's folder versions

- **Source:** addendum event, activity and message schemas, l.103, l.141, l.155 ("version rises on any change").
- **What didn't land:** AD-7 versions by folder (`library/vN`) and allows text-only edits in place. It doesn't say whether a text edit bumps the item's `version`, or whether `version` is part of the fingerprint. The content check could fail one way or the other.
- **Fix:** AD-7 states: item `version` rises on mechanics changes only (inside the fingerprint); text edits don't bump it. Alternatively, drop the field and let the folder be the version.

### L6. The replay invariant vs "engine code fixes apply to all playthroughs"

- **Source:** addendum l.185; prd.md FR-12 l.601.
- **What didn't land:** AD-6 says "Replaying the action log from the start values must reproduce the snapshot". After an engine fix, a live playthrough's snapshot (made by the old code) won't replay to the same result, and AD-5 deliberately keeps it. The scope of the invariant is unclear.
- **Fix:** AD-6: *"Replay checks run on action logs generated in the same CI build. Live playthroughs aren't replayed against a newer engine."*

### L7. "Engine tests can … force a result"

- **Source:** addendum l.183.
- **What didn't land:** AD-6 has one draw function and stores draws in the state, but doesn't say how a test forces a result, so builders may monkeypatch.
- **Fix:** AD-6: *"Tests force a draw by pre-filling the state's draw store for that key; the draw function is never patched."*

### L8. Seeded examiner users need fixed seeds and a CI run

- **Source:** prd.md NFR-6 l.1372 (scripted from month 1 to named states); FR-51 l.1285 (seeded users hold a licence).
- **What didn't land:** AD-14 requires scripted play but not fixed seeds or a pinned library version. With a different seed, the stored choices may hit options that aren't offered, or miss the target state ("crisis due", "month 59 close to each ending"). It also doesn't say whether `docker compose up` seeds automatically or the README runs a second command.
- **Fix:** AD-14:
  - each seeded user has a fixed seed and a pinned library version
  - the seed script runs in CI and asserts each target state
  - say whether local compose seeds on start

### L9. 12-month inactivity: no account-level timestamp

- **Source:** prd.md NFR-3 l.1343.
- **What didn't land:** only `playthroughs.last_played_at` exists, and session rows are deleted when they expire. An account that never confirmed a goal, or whose life was ended, has no "last play" to measure.
- **Fix:** add `users.last_active_at`, set by the auth dependency and the pipeline. The Jobs convention deletes on it.

### L10. Day boundaries for FR-50 and SM-6

- **Source:** prd.md FR-50 l.1297 ("the days the tester played"); §7.1 l.1481 (first 3 days).
- **What didn't land:** the Time convention stores UTC. Bucketing by UTC day moves late-evening Norwegian sessions to the wrong day.
- **Fix:** Time convention: "day" metrics are bucketed in Europe/Oslo at export.

### L11. The recap trigger needs a server-side last-action time

- **Source:** prd.md FR-16 l.650 (after a login, or when the game is opened after at least an hour away, across devices).
- **What didn't land:** a phone opened two hours after play on the PC can't know the gap from its own clock. The spine names no field.
- **Fix:** AD-13: the player view carries `last_action_at` (server time) or a server-computed `show_recap`. Add FR-16 to `binds`.

### L12. `/docs` in the playtest loads third-party assets

- **Source:** prd.md NFR-3 l.1344 ("loads nothing from third parties").
- **What didn't land:** AD-12 routes `/docs` to the backend in every environment. FastAPI's Swagger UI loads its JS and CSS from a CDN by default.
- **Fix:** AD-12: `/docs` only in `local`/`ci` (keep `/openapi.json`), or self-host the Swagger assets.

### L13. The reset-email daily total cap when Resend is on

- **Source:** prd.md FR-3 l.442; addendum l.287 (80% of the relay quota, so 80 a day on Resend Free); §4.4 l.321 (cut list item 11).
- **What didn't land:** AD-11 builds Resend in, switched on by key, but nothing says the total cap is enforced whenever that sender is active. The Deferred row for OQ-4 covers the relay choice only.
- **Fix:** AD-11: the email module enforces `RESET_EMAIL_DAILY_CAP` (default 80) whenever the Resend sender is active. Otherwise, list the cap explicitly in Deferred as "before go-live" per cut list item 11.

### L14. How ops commands reach the playtest

- **Source:** addendum l.294; prd.md NFR-11 l.1455 (team-made reset links); FR-50 l.1301 (tester-code load).
- **What didn't land:** AD-11 and AD-15 name CLI commands, but not how they run against Railway and Supabase (`railway run` locally vs `railway ssh`), where printed output goes (a one-off Railway job would put the reset token into Railway logs), or the base-URL setting for links.
- **Fix:** AD-14: ops commands run from a team machine with `railway run` (output stays local), plus a `PUBLIC_BASE_URL` setting.

### L15. Test-account marking: mechanism and scope

- **Source:** prd.md FR-50 l.1303 ("accounts used for checks (NFR-11) are marked"); NFR-10 l.1444 and NFR-1 l.1318 (throttled and device tests against the playtest).
- **What didn't land:** AD-15 marks only the daily login-check account. It names no mechanism, and doesn't cover the team's device-matrix, throttled-test or other accounts.
- **Fix:** AD-15: a `users.is_test` flag set by a CLI command (or by the tester-code list). Records and export skip flagged accounts, and the scope covers every team or check account.

### L16. The PRD's deletion deadline was dropped

- **Source:** prd.md NFR-3 l.1347 (code list, records and playtest accounts deleted "no later than the December delivery").
- **What didn't land:** AD-14 and AD-15 say only "after the analysis".
- **Fix:** add the deadline to AD-15.

### L17. Content-check reports "for the examiner" have no home

- **Source:** prd.md FR-17 l.664 (LK20 coverage "for the examiner"); FR-58 l.689 (reports); NFR-9 l.1434.
- **What didn't land:** AD-7 runs the content check on every PR, but its reports (LK20 coverage, warnings) would live only in CI logs and artifacts, which expire.
- **Fix:** AD-7: the content check writes a report file, and the final one is committed before delivery. Alternatively, the README names the command that prints it.

### L18. Small binding and wording gaps

- **Source:** prd.md FR-34 l.1145 (room built from flags, the same on every device); FR-40; FR-16; NFR-8 (Norwegian `message`, tone); §7.3 l.1519 (F5 moved to V2); NFR-3 l.1342 (the player information names "the database host and any email relay").
- **What didn't land:**
  - FR-16, FR-34, FR-40 and NFR-8 aren't in `binds`, though the backend stores or supplies something for each. It's undecided who maps flags to room-layer states (content vs frontend).
  - The Tests convention says "F1-F10", which includes F5, now V2.
  - The services that handle player data in the playtest (Railway EU West, Supabase Frankfurt; no email relay) aren't stated as the list the player information must name.
- **Fix:**
  - Add the four IDs to `binds` and to the Capability map.
  - Put room-layer definitions in content (`library/vN/room/`) and send the layer states in the player view.
  - Change the Tests convention to "F1-F4, F6-F10".
  - Add one AD-14 sentence naming the data processors for the NFR-3 text.
