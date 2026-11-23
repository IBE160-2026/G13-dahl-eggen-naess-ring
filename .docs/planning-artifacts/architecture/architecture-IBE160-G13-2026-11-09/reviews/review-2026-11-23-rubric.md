---
title: Rubric review of the whole spine (after #116)
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-23, status final, 419 lines)
consulted: ../.memlog.md, ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (§5 table, NFR-3 to NFR-11, §8), ../../../prds/prd-IBE160-G13-2026-10-22/addendum.md (hosting and responsiveness lines), reviews/review-rubric.md, review-adversarial.md, review-116-adversarial.md, review-116-currency.md (to avoid repeating fixed findings)
lens: good-spine checklist (divergence points, enforceable rules, safe deferrals, current tech, PRD coverage, owned dimensions, bloat, internal consistency)
scope: the whole spine. Nothing was edited.
---

# Rubric review: architecture spine, 2026-11-23

**Verdict:** a strong, buildable spine. The core (pure engine, one pipeline, one ledger, one view, frozen content) is fixed tightly, and the PRD is fully bound. What's left is mostly at the seams added late: the 2026-11-22 Vercel boundary contradicts itself on the fallback and has no enforcer for its one safety premise; AD-7's "tests never load a play library" collides with the seed-state assertions and the content check; and a handful of request-lifecycle facts (response envelope, the no-playthrough view, who commits, the `sessions` lock, worker count) are left for stories to guess. Observability is the one owned dimension that is thin. No critical findings.

| Severity | Count |
| --- | --- |
| Critical | 0 |
| High | 3 |
| Medium | 7 |
| Low | 8 |

## Checklist verdicts

| # | Item | Verdict | Evidence |
| --- | --- | --- | --- |
| 1 | Fixes the real divergence points, misses none | **adequate** | Core seams are closed hard: "every state-changing game request is `POST /api/game/actions`" (l.89), lock order (l.92), "every change to any balance … goes through `engine/ledger.py`" (l.157), "one engine function, `view(…)`" (l.207), draw ownership (l.131). Missed: the response envelope (l.208 vs l.214, M1), the view with no or an ended playthrough (M2), commit ownership on read and refusal paths (l.118, M3), `sessions` in the lock order (M4), the Uvicorn worker count against the pool sizing (l.234, M5). |
| 2 | Every Rule is enforceable and prevents its divergence | **adequate** | Most rules name a CI check or a single function: import-boundary check (l.70), "CI fails if `alembic heads` shows more than one head" (l.82), "CI fails if it is stale" (l.206), the per-month identity test (l.168), "a test fails if it holds any of them" (l.207). Unenforced: `ORIGIN_SECRET` "at least 32 bytes … never a placeholder" (l.195) has no component that refuses to start (H2); "every table has RLS enabled" (l.82) has no check (L2); "`engine` imports no … `datetime.now`" (l.70) isn't catchable by an import check (L8). |
| 3 | Nothing under Deferred lets two units diverge | **adequate** | Deferrals are bounded and name the AD that bounds them (l.408-419). One leaks: "request/response models" (l.410) defers the envelope that AD-13 half-fixes, so success and refusal bodies can be named differently (M1). Backups and zero-downtime deploys (l.416-417) are safe for a short-lived playtest. |
| 4 | Named tech is verified-current (light) | **adequate** | Versions carry dates and pin policy (l.295-308) and were checked today by review-116-currency. Light notes: Python 3.12 is security-only (l.295), adopted from the reference and stated honestly; `vercel.json` `routes` (l.194) is Vercel's legacy low-level property and excludes `rewrites`, `redirects`, `headers`, `cleanUrls` and `trailingSlash` in the same file, which constrains the frontend team (L7). |
| 5 | Covers the PRD's capabilities (map and binds) | **strong** | `binds` lists FR-1 to FR-58 and NFR-3 to NFR-11 (l.11); NFR-1/NFR-2 are deferred to the frontend (l.408-409). Every FR range has a map row (l.389-402). Minor: no rows for NFR-4, NFR-7, NFR-8, NFR-9, and some rows omit an AD that binds them (L4). |
| 6 | Every owned dimension decided, deferred or open | **adequate** (observability **thin**) | Deployment and environments **strong**: `APP_ENV` with no default (l.231), one image, `playtest` branch (l.235), pre-deploy migrations (l.233), rollback rule (l.239). Infra and provider **strong**: Railway/Supabase/Vercel with regions, tiers, limits table and fallback (l.235-252). Operations **adequate**: ops commands, cost alerts, cleanup (l.237-238); no runbook location. Security **adequate**: session revocation, HMAC limit keys, RLS, origin secret, no third-party loads (AD-3, AD-10, AD-12); the origin secret has no guard (H2). Data lifecycle **strong**: retention jobs (l.285), cascade (l.284), playtest deletion (l.264), backups deferred with reason (l.416). Testing **strong** (l.289). Observability **thin**: one daily login check (l.287), one health endpoint (l.286), "server time … is logged" (l.281) with no format, no error alerting, no request correlation, no 500 shape (M6). |
| 7 | Bloat: PRD restatement, rationale, story-level detail | **thin** | 56 KB for a spine. Rationale inline: "(Safari doesn't reliably keep Secure cookies on `http://localhost`, and the test client runs on http)" (l.176); "That is safe only because Caddy refuses …" (l.179); "bcrypt 5 refuses inputs over 72 bytes, and the pre-hash keeps every password at 44" (l.175). Story-level detail that will rot: the 14-item sprint-1 spike checklist (l.240), `history.replaceState` in the frontend (l.198), the "<month> i fjor" wording (l.212). Duplication: the player-information page is described in AD-12 (l.199) and again in AD-13 (l.209). (M7) |
| 8 | Internal consistency | **adequate** | Cross-references resolve and the diagram matches the layer table (l.32-62). Breaks: the Next.js route-handler fallback (l.240) contradicts "never through a Next.js function" (l.179) (H1); "tests … never load a play library version" (l.144) contradicts the seed-state assertions (l.233, l.289) (H3); "Every response carries `server_time`" (l.208) vs the error shape `{code, message, state}` (l.214) (M1); "The PRD (final, as it stands on 2026-11-15)" (l.26) and "departs from the addendum's 'same region'" (l.235) are stale (L1); the Structural Seed lacks files the ADs need (L3). |

## High

### H1. The proxy fallback routes login through a Next.js function, which AD-10 forbids

- **Location:** AD-10 "Network" (l.179); AD-14 "Sprint-1 spike checks" (l.240).
- **Problem:** AD-10 says: "Sign-up, login and reset always go browser → Vercel's proxy → Caddy → backend, never through a Next.js function or other frontend server code." The spike fallback says: "If the visitor's address doesn't arrive, the frontend team proxies `/api/*` through a Next.js route handler." `/api/*` includes sign-up, login and reset. If the spike triggers the fallback, the frontend team builds it and the auth story still reads AD-10 as binding, or the opposite. The fallback also changes the trust chain: the header Caddy trusts, the `client_ip_headers` setting, and whether `Set-Cookie` passes through all differ from AD-10's description, but only one clause covers it.
- **Fix:** In AD-10, change the last sentence to "Sign-up, login and reset go browser → Vercel → Caddy → backend; if the AD-14 fallback is taken, the route handler is the only frontend code on that path, it forwards `Cookie` and `Set-Cookie` unchanged and sets `X-Client-IP-Origin` (or a named header), and Caddy's `client_ip_headers` switches to that header", and point AD-14's fallback sentence at it.

### H2. The origin secret is the only thing that makes trusting every proxy safe, and nothing enforces it

- **Location:** AD-12 "Caddy" (l.195); AD-10 "Network" (l.179); AD-14 "One image, one settings file" (l.231).
- **Problem:** AD-10 trusts every peer (`0.0.0.0/0 ::/0`) and reads the leftmost `X-Forwarded-For`, "safe only because Caddy refuses every request without Vercel's origin secret". AD-12 requires `ORIGIN_SECRET` to be "at least 32 bytes … never a placeholder", but the startup guard in AD-14 covers only the backend's `JWT_SECRET` and `HASH_SECRET`; the backend never sees `ORIGIN_SECRET`. An unset variable in Caddy's Railway service expands to an empty string, and what the matcher does then depends on how the Caddyfile is written. The spike checks the refusal once (l.240); a later variable edit or a new Railway environment isn't checked. A story writing the Caddyfile and a story setting Railway variables can each follow the AD and still leave the backend open to forged client addresses, which defeats the attempt limits.
- **Fix:** Add to AD-12: "Caddy's container entrypoint refuses to start if `ORIGIN_SECRET` is shorter than 32 bytes or equals the `.env.example` placeholder whenever trusted proxies are set, and the daily GitHub Actions check also asserts that a request to Caddy's Railway domain without the secret gets `403`."

### H3. "Tests never load a play library" contradicts the seed-state check and the content check, and seeded targets will redden CI during tuning

- **Location:** AD-7 "Worked examples" (l.144) and "Freeze" (l.142); AD-14 "Migrations and seeding" (l.233); Tests convention (l.289).
- **Problem:** AD-7 says "tests read only `content/config/test-vN/` and items defined in the test code. They never load a play library version." (The 2026-11-13 fix scoped this to worked-example tests; the spine now says all tests.) AD-14 says "Seeded users are made by scripted play … with … pinned content versions, and CI runs the seed script and asserts each target state", and FR-58's content check "plays seeded test playthroughs" against the play library. Both must load `library/v1`. A test-infrastructure story that enforces AD-7 literally (for example, a fixture that blocks play-library paths) breaks the seed story. Second, while `v1` is `frozen: false` and being tuned (OQ-8, OQ-17), every tuning PR can move a seeded user off "in debt with a crisis due" or "month 59 close to each ending", so the seed assertion fails CI. AD-7's freeze gate exists to stop this ("a permanently red CI"), but the seed check is not covered by it.
- **Fix:** Reword AD-7 l.144 to "Worked-example and engine unit tests read only `content/config/test-vN/` …; the content check and the seed-state check are the only CI steps that load a play library", and add to the Freeze bullet "while the newest library is unfrozen, the seed-state assertions warn; they fail from the freeze on, like the other FR-58 gates."

## Medium

### M1. The response envelope isn't fixed: where `server_time` goes, and what the player view is called on success

- **Location:** AD-13 "Identity and time" (l.208) and "Errors" (l.214); AD-4 sequence diagram (l.107-114); Deferred "request/response models" (l.410).
- **Problem:** "Every response carries `server_time` and the recap threshold", but the error shape is exactly `{code, message, state}`. `view(…)` takes no clock, so `server_time` can't be inside `PlayerView` unless the shell adds it. On success the diagram returns "result + player view", while a refusal names the view `state`. Two API stories can produce `{result, view, server_time}` and `{code, message, state}` with `server_time` missing, and the frontend's FR-16 recap check breaks on refusals.
- **Fix:** Add to AD-13: "Every game response is `{result?, state, server_time, recap_threshold}`; an error adds `code` and `message` to the same envelope, with `state` present when a game request is refused."

### M2. `GET /api/game` has no defined answer before the first start, or after a life ends early

- **Location:** AD-4 "One endpoint" (l.89) and "Protocol fields" (l.90); AD-5 status values (l.124); AD-13 "One view function" (l.207); status table (l.220).
- **Problem:** Every new account logs in with no playthrough row (`playthrough_id` "null only for an account's first start"). AD-5 keeps an `ended` row until the next start, and "only a `completed` life is shown again". Nothing says what `GET /api/game` returns in either case: `404 not_found`, a view with `playthrough_id: null`, or a view of the ended state. The frontend team builds the first screen against one guess and the backend story against another.
- **Fix:** Add to AD-13: "With no playthrough, or with an `ended` one, `GET /api/game` returns `200` with a player view whose `playthrough_id` is the current row's id or null and whose `status` is `none`, `ended` or the row's status; it never answers `404`."

### M3. Who commits the request transaction is fixed only for the pipeline's write

- **Location:** AD-4 "Database session discipline" (l.118) and sequence diagram (l.103, l.113); AD-10 "Sessions" (l.176).
- **Problem:** The auth dependency writes on every authenticated request (it slides the session row and writes `users.last_active_at`), and the one `AsyncSession` "is opened and closed by one dependency". The pipeline's own write ends in "commit". On `GET /api/game`, the disclosure upsert, and a refusal that "writes nothing", no rule says who commits the auth dependency's writes. If no one does, the slide is lost on read paths while the client already holds the re-issued cookie, so the 30-minute idle limit (FR-5) ends sessions of players who only read, and `last_active_at` drifts from what the inactivity job assumes.
- **Fix:** Add to AD-4's session discipline: "The request-session dependency commits on every normal exit and on an `AppError` refusal; the pipeline never commits itself, and any other exception leaves the dependency to close the session without commit."

### M4. The lock order leaves out `sessions`, and the auth dependency takes it before `users`

- **Location:** AD-4 "Lock order" (l.92); AD-10 "Sessions" and "Revocation" (l.176-177); sequence diagram (l.103).
- **Problem:** The order is `users` → playthrough → playtest record. The auth dependency, in the same transaction, slides the `sessions` row and writes `users.last_active_at`; the AD doesn't say in which order. A password change, "log out on all devices" or `delete_account` locks `users` and then deletes the user's session rows. If the auth dependency updates its session row first and `users` second, two devices of one player can deadlock, and Postgres aborts one with a 500. It also isn't said whether `last_active_at` is written on every request or only with the once-a-minute slide, which matters for the 300 ms budget.
- **Fix:** Extend AD-4's lock order to "`users`, then `sessions`, then the playthrough row, then the playtest record", and add to AD-10 "the dependency writes `users.last_active_at` before the session row, and only when it slides (at most once a minute)."

### M5. The Uvicorn worker count isn't fixed, but the pool and the daily jobs assume one process

- **Location:** AD-14 "Database" (l.234); Jobs convention (l.285); Stack (l.297).
- **Problem:** "the app pool is 5 per instance with no overflow (two instances during a deploy overlap)" against Supabase's 15 clients. Pools are per process. A Dockerfile story that starts `uvicorn --workers 2` (or `fastapi run --workers`) doubles the clients to 20 during a deploy and starts the daily jobs in every worker. Nothing in the spine fixes the count.
- **Fix:** Add to AD-14: "The backend runs one Uvicorn worker per instance; pool sizing and the in-process daily jobs assume it."

### M6. Observability is thin for an unattended multi-day playtest

- **Location:** Logging convention (l.281); Monitoring (l.287); Health (l.286); Errors (l.214); Performance (l.288).
- **Problem:** The spine decides what logs must not contain, but not how the backend logs: no library or format, no request id to tie a refusal to its request, no level policy. The p90 is "taken from the logged server time", so the spike and the playtest need a parseable line that nobody has defined. Unhandled exceptions have no handler: the three named handlers cover `AppError`, `RequestValidationError` and `HTTPException`, so a 500 returns FastAPI's plain-text default, outside the `{code, message, state}` shape and NFR-8. No one is alerted to 5xx during the test; the daily login check would miss a bug that breaks month 13. Also, Uvicorn's default access log includes the client address, which the Logging convention forbids, and no rule switches it off.
- **Fix:** Add one Observability row to the conventions: "stdlib `logging` with one JSON line format set in `main.py`, carrying `request_id`/`user_id`/`code`/`duration_ms`; Uvicorn's access log off and one middleware access line without client address or query; a catch-all handler answers `500 internal_error` in the same shape and logs the traceback; during the playtest a team member reads the Railway log for `level=error` daily, or the daily check fails on any error in the last 24 hours."

### M7. Rationale and story-level detail inflate the spine and will rot

- **Location:** AD-10 (l.175, l.176, l.179); AD-12 (l.198, l.199); AD-13 (l.209, l.212); AD-14 (l.235, l.240).
- **Problem:** At 56 KB the spine is hard to hold in one read, and several passages are reasons or checklists rather than rules: the Safari note and the bcrypt byte count, "That is safe only because …", the 14-item spike checklist (it becomes stale the day the spike is done), `history.replaceState` in frontend code, the two copies of the player-information paragraph, and Vercel's edge-region detail.
- **Fix:** Move the reasons (Safari, bcrypt length, the XFF safety argument, Vercel edge regions) to the memlog, move the spike checklist into the sprint-1 spike story and leave "the sprint-1 spike verifies AD-3, AD-10, AD-12 and AD-14's assumptions; on failure, see the fallback" in AD-14, and keep the player-information paragraph only in AD-12.

## Low

### L1. Stale source facts

- **Location:** l.26 "The PRD (final, as it stands on 2026-11-15)"; l.235 "this departs from the addendum's 'same region'"; `sources` (l.12-18).
- **Problem:** The spine depends on PRD changes from 2026-11-22 (nickname, Vercel note in NFR-11) and 2026-11-23 (FR-33 bands, rule 11). The addendum now says "in the same or a neighbouring EU region. The playtest uses Amsterdam and Frankfurt" (addendum l.25), so there is no departure. The final UX (EXPERIENCE.md) drove #116 but isn't a source.
- **Fix:** Change l.26 to "as it stands on 2026-11-23", replace the departure clause in l.235 with "a neighbouring region, as the addendum allows", and add the UX folder to `sources`.

### L2. RLS on every table has no check

- **Location:** AD-3 (l.82).
- **Problem:** "every table has RLS enabled … set by one Alembic helper that every table migration uses". A migration that forgets the helper passes CI; only the spike checks RLS once.
- **Fix:** Add to AD-3: "A CI test on the migrated schema fails if any table in `public` has `relrowsecurity = false`."

### L3. The Structural Seed misses files the ADs require

- **Location:** source tree (l.355-383); AD-7 (l.142-143); AD-12 (l.195); Monitoring (l.287).
- **Problem:** AD-7 says "The backend image is built from the repo root", but no Dockerfile is placed; Caddy on Railway needs its own image or Dockerfile with `infra/Caddyfile`; `.github/workflows/` (PR checks, the daily login check) and `README.md` (NFR-6) are absent. AD-7's "the playtest database's game data is cleared once" has no CLI command in `cli.py`'s list, and which tables count as "game data" isn't said.
- **Fix:** Add `backend/Dockerfile`, `infra/Dockerfile` (Caddy), `.github/workflows/{ci,daily-check}.yml` and `README.md` to the tree, and add "clear game data (playthroughs and action log; accounts, records and codes kept)" to the `cli.py` comment and AD-7.

### L4. Capability map gaps

- **Location:** Capability map (l.389-402).
- **Problem:** No rows for NFR-4, NFR-7, NFR-8 and NFR-9, which are in `binds`. Some rows omit an AD whose Binds list names their FRs: "Money" lacks AD-13 (money per month, FR-21); "Start, avatar, months, events" lacks AD-7 (avatar looks, FR-10) and AD-13 (FR-13, FR-15); "Month plan, phone, job view" lacks AD-13 (FR-53, FR-54) and AD-16 (FR-55).
- **Fix:** Add rows "Server authority and refusals (NFR-4, NFR-7) | `engine`, `api`, `persistence` | AD-1, AD-2, AD-4, AD-13", "Tone (NFR-8) | `content`, `api` | AD-7, AD-13" and "Automated tests (NFR-9) | CI | Tests convention, AD-7", and add the missing ADs to the three rows.

### L5. The cascade convention doesn't cover `action_log`

- **Location:** Deletion convention (l.284); AD-4 "Life requests" (l.93).
- **Problem:** "Every table keyed by `user_id` has `ON DELETE CASCADE`". `action_log` is keyed by `playthrough_id`; a start deletes the previous playthrough, and its log must go with it.
- **Fix:** Change the row to "Every child table cascades from its parent (`user_id` tables from `users`, `action_log` from `playthroughs`); `tester_codes` … no link."

### L6. Ops commands run the operator's checkout, not the deployed code

- **Location:** AD-14 "Ops commands" (l.238).
- **Problem:** `railway run` injects the service's variables into a local process, so reset links, test-account marking and the export run whatever commit the team member has checked out. A checkout ahead of the `playtest` branch can read a `state_schema` or content version the deployed image doesn't know.
- **Fix:** Add "from a checkout of the commit currently deployed on the `playtest` branch."

### L7. Two Vercel boundary details to confirm with the frontend team

- **Location:** AD-12 "Playtest" (l.194).
- **Problem:** `routes` is Vercel's legacy low-level property; a `vercel.json` that uses it can't also use `rewrites`, `redirects`, `headers`, `cleanUrls` or `trailingSlash`, which the frontend team may want. Separately, if `ORIGIN_SECRET` is set for Vercel's Preview environment, every preview deployment of any frontend branch can reach the playtest backend and its testers' data.
- **Fix:** Add "`ORIGIN_SECRET` is set only for Vercel's Production environment" to AD-12, and add a spike check that the frontend's `vercel.json` with `routes` builds alongside its other settings.

### L8. AD-1's purity rule names something an import check can't see

- **Location:** AD-1 Rule (l.70).
- **Problem:** "`engine` imports no … `random`, `datetime.now`, `os.environ`". `datetime.now` and `os.environ` are attributes, not imports, and the check's tool isn't named.
- **Fix:** Change to "`engine` imports none of `random`, `secrets`, `time`, `os`, `sqlalchemy`, `fastapi`, `httpx`, checked by import-linter contracts in CI; `datetime` is allowed for types only (the view takes `last_action_at`), and a lint rule (ruff `DTZ`/banned-api) fails on `datetime.now`, `date.today` and `utcnow` inside `engine`."
