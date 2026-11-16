---
title: Reconcile spine against reference setup and memlog
reviewed: ARCHITECTURE-SPINE.md (updated 2026-11-13)
inputs:
  - ../../technology.md (reference setup, Pytagoras Website V2)
  - ../.memlog.md (2026-11-13 entries supersede 2026-11-09 ones)
  - checked against: PRD final (prd.md NFR-3/5/6/10/11, FR-1..5, FR-50) and addendum limits table, old architecture_technical_design.md (memlog L8 lists it as a silently inherited source)
date: 2026-11-13
scope: backend/infra only; frontend is owned by another team
---

# Reconcile: spine vs reference setup and memlog

**How part (b) was filtered (scope correction from the user):** technology.md is a reference to *adapt*, not copy. A reference practice is reported only if (1) the MVP needs it to meet a PRD requirement (NFR-3, NFR-5/6/7/10/11, FR-1..5) or (2) two backend builders would otherwise build incompatibly. Everything else is listed once under "Deliberately left out — fine". Suggested fixes are kept as small as possible for v1.

Line numbers: `S:` = spine, `M:` = memlog, `R:` = technology.md.

## Count

| Severity | Count |
| --- | --- |
| High | 4 |
| Medium | 14 |
| Low | 10 |

---

## High

### H1 — The email stand-in would put addresses and reset tokens in the playtest logs

- **Type:** (a) landed differently + internal contradiction
- **Source:** M:46 ("with no RESEND_API_KEY the stand-in is used (reset link to the local inbox/log)"; "Playtest runs with Resend switched off: no email is sent"); NFR-3 ("Neither the email address nor the password is written to the game's own logs"); R:187 (`[email:mock]` = email is only logged).
- **What didn't land:** S:143 (AD-11) says the stand-in "writes the rendered email to the log or a local inbox", and S:161 (AD-14) says every service falls back to the stand-in when its key is missing. The playtest runs without `RESEND_API_KEY`, so by those two rules the stand-in is active in the playtest: any tester's "forgot password" request writes the recipient address and a live reset link into Railway's logs. That contradicts NFR-3, the spine's own Logging convention (S:178, "no email address ... or reset token in any log"), and "no email is sent" in the playtest. Locally the same convention contradicts the stand-in. Builders will resolve it differently (log everything, log nothing, special-case the playtest).
- **Fix to the spine (AD-11 + Logging row):** Pick the sender by key *and* `APP_ENV`: Resend when the key is set; otherwise, in `local`/`ci`, the stand-in writes the rendered email (with `[email:mock]`) to the backend log; in `playtest` with no key, a "drop" sender sends nothing and logs only the template name and `user_id`. Add to the Logging row: "Exception: the `local`/`ci` email stand-in." README: `docker compose logs backend | grep email:mock`, plus the automated reset test (NFR-6 fallback). No Mailpit needed.

### H2 — Nothing stops the Supabase Data API from exposing the game tables

- **Type:** (a) memlog decision did not land as an enforceable rule
- **Source:** M:21 ("no client access to game tables via PostgREST"; kept by M:41 as "no logic in Supabase"); old architecture doc ("Supabase Row Level Security should be used where relevant for exposed tables"; inherited per M:8); NFR-3 ("A player can reach only their own data").
- **What didn't land:** S:76 (AD-3) bans *using* PostgREST, but it doesn't stop *access* through it. A hosted Supabase project exposes the `public` schema through its Data API with the public anon key by default, and tables that Alembic creates with SQL have RLS switched off. In that state `users` (email addresses), `sessions` and `playthroughs` could be readable, or even writable, from outside the backend. It's a privacy and integrity hole that neither builder would notice locally, because the local Postgres has no Data API.
- **Fix to the spine (AD-3, one sentence plus a spike check):** "In the Supabase project the Data API is switched off, and every app table has RLS enabled with no policies (set by one Alembic helper that every table migration uses). The backend holds no `SUPABASE_URL`, anon or service-role key; it reaches Supabase only through `DATABASE_URL`." Add "Data API off, anon key cannot read `users`" to the sprint-1 spike checklist (see L2).

### H3 — The startup guard fails open if `APP_ENV` is unset

- **Type:** (b) reference practice (startup guards) incompletely specified
- **Source:** R:64 ("nekter å starte i ikke-lokalt miljø med tom/standard JWT_SECRET"), R:148 (`APP_ENV` "styrer seeding og oppstartsvakter"); M:49.
- **What didn't land:** S:161 says the app refuses to start "outside `local`/`ci`" with a default `JWT_SECRET` and seeds only in `local`/`ci`, but it doesn't say what happens when `APP_ENV` is missing. The usual pydantic-settings pattern defaults it to `local`. One forgotten Railway variable would then switch off the secret guard and run seeding against the playtest database, creating the README's seeded users with published passwords on a public URL. "Default" `JWT_SECRET` is also undefined.
- **Fix to the spine (AD-14):** "`APP_ENV` has no default: the app refuses to start without it (`compose.yaml` sets `local`, CI sets `ci`). Outside `local`/`ci` it also refuses an empty `JWT_SECRET`, the `.env.example` placeholder, or one shorter than 32 bytes."

### H4 — The 'never `rollback()` on the shared session' pitfall sits right in the refusal path

- **Type:** (b) reference pitfall the spine omits, where two builders diverge
- **Source:** R:95 ("Aldri `rollback()` på requestens delte sesjon (utløper identity-map → `MissingGreenlet`); bruk `INSERT … ON CONFLICT DO NOTHING`").
- **What didn't land:** S:94 (AD-4) refuses with "current state, nothing written". The obvious async-SQLAlchemy implementation is `await session.rollback()` followed by serializing `playthrough.state`, and that is exactly what raises `MissingGreenlet`. The same trap waits in sign-up (duplicate normalized email, FR-1), the unique `request_id` in `action_log` (AD-5), attempt counters, and tester-code matching (AD-15). It hits NFR-7's refusal tests and the core pipeline, and each builder would handle conflicts differently.
- **Fix to the spine (AD-4, one bullet):** "One `AsyncSession` per request (`expire_on_commit=False`), opened and closed by one dependency. Handlers and the pipeline never call `rollback()`. A refusal builds its response from the state already loaded and ends without writes. Expected conflicts use `INSERT … ON CONFLICT DO NOTHING … RETURNING` and check the result (sign-up email, `request_id`, tester-code match)."

---

## Medium

### M1 — How migrations run before start was lost

- **Type:** (a) memlog detail dropped
- **Source:** M:49 ("Alembic migrations run before the app starts (Railway preDeployCommand; at compose startup locally)"); R:75 (`preDeployCommand: python -m app.cli schema upgrade`), R:149 ("Alembic bruker samme" `DATABASE_URL`).
- **What didn't land:** S:161 says only "Migrations run before the app starts". The `cli.py` list (S:242) has no schema command. One builder will migrate in the FastAPI lifespan, so every restart and every instance migrates; another will use preDeploy.
- **Fix:** AD-14: "`python -m app.cli schema upgrade` (Alembic `upgrade head` on the same `DATABASE_URL`) runs as the Railway backend `preDeployCommand`. In compose, the backend entrypoint runs it before Uvicorn, after `db` passes a `pg_isready` healthcheck. The app never migrates inside its lifespan." Add `schema upgrade` to the `cli.py` comment.

### M2 — When seeding runs is unspecified (NFR-6: one command)

- **Type:** (b) reference practice needed for NFR-6
- **Source:** R:96 (`seed_if_empty` at startup, demo accounts only in local/dev/test/ci); NFR-6 ("The full stack starts with one command"; the README provides seeded users); M:50(4).
- **What didn't land:** S:161 says *where* seeding may run and S:242 lists "seed users" as a CLI command, but not *when*. If it's a manual step, the examiner needs a second command; if it's automatic, it has to be idempotent.
- **Fix:** AD-14: "In `local`, the backend entrypoint runs `cli seed --if-empty` after migrations. It plays the stored choice scripts through the engine and skips if the seeded users exist. CI fixtures call the same function. It refuses unless `APP_ENV` is `local`/`ci`."

### M3 — Session-pooler connection details are not fixed

- **Type:** (b) reference practice needed for NFR-10/NFR-11, and builders would diverge
- **Source:** R:149 (`postgresql+asyncpg://…`, session pooler port 5432, SSL, Alembic uses the same URL); R:130; M:47, M:48.
- **What didn't land:** S:161 says "through the session pooler" only. Session mode holds one server connection per client connection, and the pooler's pool on Supabase Free is small (on the order of 15; verify). SQLAlchemy's default pool (5 + 10 overflow), plus the preDeploy migration and a second instance during a deploy, can exhaust it, and logins then fail with "max clients". It's also unspecified whether Alembic uses a separate direct URL, and the Railway Postgres fallback hands out `postgresql://` URLs without `+asyncpg`, so "switched by `DATABASE_URL` only" would fail.
- **Fix:** AD-14: "`DATABASE_URL` = Supabase session pooler (port 5432, SSL required), one URL for app and Alembic. SQLAlchemy `pool_size=5`, `max_overflow=0` (settings). Settings normalize `postgres://`/`postgresql://` to `postgresql+asyncpg://`." Add "pooler pool limit" to the spike (L2).

### M4 — NFR-11's limits and the full cost aren't named

- **Type:** (a) memlog version facts not landed; PRD requirement
- **Source:** NFR-11 ("names the provider and tier, and the limits that matter for the test: pausing or sleeping when idle, storage, number of users, and email quota"); M:43 (Supabase Free 500 MB, paused after 1 week; Resend Free 3,000/month, 100/day; Railway Hobby $5 incl. $5 usage); M:45 (a separate frontend server may push usage above $5).
- **What didn't land:** The spine names provider, tier and region, but not storage, pause, users or email quota. The USD 5-8 estimate doesn't say whether it includes a frontend server.
- **Fix:** Add a five-row "Playtest limits" table to AD-14:

  | Limit | Value |
  | --- | --- |
  | Sleep | Railway sleeping off |
  | Pause | Supabase pauses after 1 week idle; the daily login check prevents it |
  | Storage | 500 MB |
  | Users | No Supabase Auth, so no MAU limit applies; 10-20 testers expected |
  | Email | None sent in the playtest; Resend Free 100/day at go-live, reset cap 80/day |

  Also add: "A separate frontend server adds Railway usage beyond the estimate."

### M5 — The cross-region deviation, and the latency trigger for the fallback

- **Type:** (a) landed differently
- **Source:** M:16 / addendum ("backend and DB same region"); M:47 ("Fallback if Supabase fails (pause, latency, region)"); M:48 (spike).
- **What didn't land:** S:161 puts the backend in Amsterdam and the database in Frankfurt (Supabase has no Amsterdam region; M:43) without saying this departs from the addendum's same-region rule. It also gives the fallback trigger only as "if Supabase fails", which leaves open whether a missed 300 ms budget counts.
- **Fix:** AD-14: "Backend and database are in neighbouring regions (Amsterdam/Frankfurt), not the same one; the spike measures the p90. If p90 > 300 ms, Supabase pauses, or the region fails, switch to Railway Postgres **17** in EU West via `DATABASE_URL`." Pinning 17 keeps the "same major version" rule true in the fallback.

### M6 — "Reset always works" did not land

- **Type:** (a) memlog decision dropped
- **Source:** M:50(5) ("failed-login counter keyed by (address, network); reset always works"); FR-2 ("a reset link (FR-3) always lets the player in, so a classmate can't lock a player out").
- **What didn't land:** S:137 (AD-10) has the per-(address, network) key, but not the escape route. A builder could apply the login pause to reset or to the login right after a reset.
- **Fix:** AD-10: "The failed-login pause never applies to reset. Requesting and redeeming a link count only against the reset limits, and a redeemed link clears that address's failed-login counters."

### M7 — Session cookie lifetime and JWT claims are unspecified

- **Type:** (a) partly landed; (b) incompatible builds likely
- **Source:** M:44; FR-5 ("Unticked, the login ends when the browser is closed or after 30 minutes with no activity"); R:62 (HS256 with `JWT_SECRET`), R:155 (`ACCESS_TOKEN_EXPIRE_MINUTES` default 43,200).
- **What didn't land:** S:137 sets the idle limits on the row but not the cookie. A cookie with a 30-day `Max-Age` for everyone breaks "ends when the browser is closed"; a short JWT `exp` copied from elsewhere logs out "stay logged in" users. Writing `last_seen_at` on every request adds a write to the 300 ms path.
- **Fix:** AD-10: "JWT: HS256 with `JWT_SECRET`; claims `sid` and `exp` (30 days); the session row is authoritative. Unticked: cookie without `Max-Age` (browser-session cookie), row idle limit 30 min. Ticked: cookie `Max-Age` 30 days, row idle limit 30 days. `last_seen_at`/`expires_at` slide on authenticated requests, written at most once a minute."

### M8 — How the client network is identified is under-specified, and the frontend-server path is open

- **Type:** (b) builders would build incompatibly; FR-1/FR-2 per-network limits
- **Source:** S:137 ("forwarded header set by Caddy ... Caddy trusts only the hosting edge"); R:226 (`API_INTERNAL_URL`: the Next.js server calls the backend directly at `http://backend:8000`); S:149 (AD-12 leaves the frontend server choice open); addendum limits table (AG-26).
- **What didn't land:** No header name, no backend-side rule (Uvicorn proxy headers), no IPv6 granularity, and no word on Railway's edge, which publishes no fixed IP list (verify). If the frontend team copies the reference's server-side calls, every login reaches the backend from one internal address and counts as one network. That is exactly what AD-10's "Prevents" line rules out.
- **Fix:** AD-10/AD-12: "Caddy sets `X-Client-IP` from `{client_ip}`, with `trusted_proxies` for the Railway edge (exact config verified in the spike). The backend reads only that header and is reachable only from Caddy. Network key = IPv4 address or IPv6 /64. Sign-up, login and reset are always browser → Caddy → backend, never called from a frontend server."

### M9 — The attempts table in the ER diagram can't hold what it must count, and isn't cleaned up

- **Type:** (a) landed differently
- **Source:** M:50(5) (keyed by *address* and network, not user); FR-1 (sign-up attempts per network, with no user yet); FR-2 (neutral message, so failed logins for unknown addresses must count too); NFR-3 ("the attempt limits briefly process network addresses").
- **What didn't land:** S:229 draws `login_attempts }o--|| users` (each attempt tied to exactly one user). A builder adds a `user_id NOT NULL` foreign key, and then can't record sign-up attempts or failed logins for unknown addresses. The Jobs row (S:180) deletes sessions and reset links, but not attempt rows that hold network addresses.
- **Fix:** ER: `auth_attempts` (`kind` signup|login_failed|reset_request, normalized address nullable, network, `created_at`), no foreign key to `users`. Jobs row: "...and attempt rows older than the longest window (24 h)". Jobs are idempotent deletes, so a run on two instances during a deploy does no harm.

### M10 — Base URL and format of the reset link (backend/frontend boundary)

- **Type:** (b) needed for FR-3/NFR-11; boundary between two teams
- **Source:** R:151 (`FRONTEND_URL`, "brukes i ... e-postlenker"); NFR-11 (the CLI prints a one-time link); S:143.
- **What didn't land:** The CLI has no request to take a host from, and the page the link opens is a frontend route. The spine names neither the base URL setting nor the link shape, so the backend and frontend teams can't agree on it from the spine alone.
- **Fix:** AD-14: setting `PUBLIC_BASE_URL` (required outside `local`/`ci`; compose sets the local URL). AD-12 boundary fact: "Reset link = `{PUBLIC_BASE_URL}/<reset path>?token=<token>`. The path is agreed with the frontend team, and the frontend page posts token + new password to `/api/...`."

### M11 — Operational limits have no home ("all figures in `content/config/`")

- **Type:** (b) builders would diverge
- **Source:** S:179 (Config row); addendum limits table ("all configuration"); FR-5 idle times, FR-3 link lifetime, FR-50 10-minute gap, NFR-3 12-month deletion.
- **What didn't land:** Read literally, the Config row puts sign-up and login limits, idle times and the reset cap into versioned, frozen content that is pinned per playthrough (AD-7), which makes no sense for them. Another builder puts them in environment variables.
- **Fix:** Config row: "Game figures (pinned per playthrough) live in `content/config/`. Operational limits (auth limits, idle times, reset link lifetime and caps, inactivity deletion, the FR-50 gap, pool size) are pydantic-settings fields in one `backend/app/settings.py` with the PRD defaults, overridable by env and listed in `.env.example`."

### M12 — The local URL scheme vs the `Secure` cookie

- **Type:** (b) builders would build incompatibly; NFR-6 login must work locally
- **Source:** R:43, R:128 (Caddy `tls internal` locally, plain HTTP behind Railway); S:137 (`Secure` cookie).
- **What didn't land:** The spine doesn't say whether local Caddy serves HTTPS. If the Caddy builder uses `http://localhost` while the auth builder always sets `Secure`, login may fail in browsers that refuse `Secure` cookies over plain HTTP. If the Caddy builder copies `tls internal`, the examiner sees a certificate warning the README must explain.
- **Fix (smallest):** AD-12: "Locally Caddy serves `http://localhost:<port>`; on Railway it listens on plain HTTP on `$PORT` behind the edge. The cookie's `Secure` flag is on except when `APP_ENV=local`."

### M13 — Database tests must use Postgres, not the reference's aiosqlite

- **Type:** (b) copying the reference would break incompatibly
- **Source:** R:86 (pytest + aiosqlite, in-memory SQLite per test); S:82-107 (AD-4/AD-5 use `FOR UPDATE`, JSONB and `ON CONFLICT`); S:183 (Tests row says nothing about DB tests).
- **What didn't land:** A builder copying the reference's fixtures can't test the mutation pipeline, idempotency or the JSONB state, and two test setups grow side by side.
- **Fix:** Tests row: "Tests that touch the database run against Postgres 17 with the Alembic-migrated schema (compose `db` locally, a service container in GitHub Actions). aiosqlite is not used."

### M14 — bcrypt's 72-byte limit vs the PRD's maximum of "at least 64" characters

- **Type:** (b) reference choice (bcrypt) meets a PRD requirement; builders would diverge
- **Source:** addendum limits table (minimum 8; "the maximum allowed is at least 64"); R:77 (bcrypt); FR-1 (no other rules on content).
- **What didn't land:** Norwegian letters take 2 bytes in UTF-8, so 64 characters can exceed bcrypt's 72-byte input. Recent bcrypt releases raise an error on that; older ones silently truncate. One builder gets crashes or rejections, another gets silent truncation.
- **Fix:** AD-10: "Passwords 8-64 characters (settings). The hash is `bcrypt(base64(sha256(password)))`, so length and non-ASCII letters never hit bcrypt's 72-byte limit."

---

## Low

### L1 — Sources and the course constraint

- **Source:** M:8 (old `architecture_technical_design.md` is a source); M:9 ("Supabase (database + auth). Fixed, not open"); old doc ("Supabase: the required database").
- **Gap:** The spine's `sources` don't list the old architecture doc, and nothing says the course requirement is met with Supabase as the database only. Someone could re-add Supabase Auth "because the course says so".
- **Fix:** In AD-3, add: "The course's Supabase requirement is met by Supabase Postgres." List the old doc in `sources` as superseded, or drop it from M:8.

### L2 — Assumptions to verify aren't carried into the spine

- **Source:** M:48 (p90 Amsterdam↔Frankfurt; Railway sleeping off; usage near the $5 credit).
- **Gap:** Only the p90 check appears (S:182).
- **Fix:** Add one line to AD-14: "Sprint-1 spike verifies: p90 ≤ 300 ms, sleeping off, usage near $5, pooler pool limit (M3), Data API off (H2), Railway edge trusted-proxy config (M8)."

### L3 — Stack versions and pins aren't recorded in the memlog; uv is unpinned

- **Source:** R:46 (Postgres 16); S:189-201 (Postgres 17, SQLAlchemy 2.1.6, Alembic 1.20.1, Caddy 2.11.7, uv "latest").
- **Gap:** Postgres 17 departs from the reference's 16. The spine gives the reason inline (it matches Supabase), but the memlog has no version entry for it or for the other dated versions. "uv latest" in the image makes builds unreproducible.
- **Fix:** Add one `(version)` memlog entry. Change the uv row to "pinned version in the Dockerfile; `uv.lock` committed; `--locked`".

### L4 — Healthcheck

- **Source:** R:129 (Railway healthchecks on `/api/health`); NFR-11 (stays available for the whole test).
- **Gap:** Without a healthcheck, Railway switches traffic to a broken deploy, and the playtest goes down.
- **Fix:** Conventions: "`GET /api/health` (no auth): 200 once content has loaded and `SELECT 1` succeeds. Railway backend `healthcheckPath=/api/health`." No overlap or draining tuning in v1: accept a short restart, and don't deploy during playtest hours.

### L5 — Content loading and the image build context

- **Source:** M:34 ("loaded at backend start"); S:161 ("One backend image"); S:245-248 (`content/` sits outside `backend/`).
- **Gap:** The spine doesn't say when content is loaded or how `content/` gets into the image.
- **Fix:** AD-7: "All versions are loaded and checked against their fingerprints once at startup; startup fails on error. The backend image is built from the repo root and copies `content/`."

### L6 — FR-50: "a count of testers who left" is missing

- **Source:** FR-50 ("the record goes with it, and only a count of testers who left is kept"); M:50(3) ("records carry the code").
- **Gap:** AD-15 doesn't say what happens to records when an account is deleted.
- **Fix:** AD-15: "Account deletion deletes its records and increments an unlinked `testers_left` counter."

### L7 — The reset link has two creators

- **Source:** FR-3 (single use, 60 min, a new link cancels older ones); S:143 (CLI) and the reset endpoint.
- **Gap:** The CLI and the API could implement links differently.
- **Fix:** AD-10: "One auth function creates links for both the CLI and the endpoint. Only the token's SHA-256 is stored; a new link cancels older ones."

### L8 — Deploy trigger

- **Source:** R:136 (a `production` branch deploys); old doc ("CD not required for MVP"); NFR-11 ("same version as local").
- **Gap:** The spine doesn't say what deploys the playtest.
- **Fix:** One line in AD-14: "The playtest deploys from `main` via Railway's GitHub integration" (or manually; pick one).

### L9 — One Caddyfile for local and Railway

- **Source:** R:254 (`BACKEND_UPSTREAM`/`FRONTEND_UPSTREAM` for the proxy on Railway); S:250 (one `infra/Caddyfile`).
- **Gap:** The spine doesn't say whether there is one Caddyfile or two.
- **Fix:** "One Caddyfile, with upstreams and the listen address from environment variables (`BACKEND_UPSTREAM`, `FRONTEND_UPSTREAM`, `PORT`)."

### L10 — The not-taken list is incomplete

- **Source:** M:49 (lists Redis, Storage, Stripe/Vipps, AI, Fiken, capability tokens, backup, watchdog, Cloudflare worker, plugins).
- **Gap:** These are also skipped silently, and builders copying the reference may bring them in: `FEATURE_*` flags, `CORS_ORIGINS`, `ADMIN_EMAILS`, `SUPABASE_JWT_SECRET` (dual-token acceptance), `SUPABASE_URL`/keys, aiosqlite, vertical-slice `app/modules/`, `click`-specific CLI patterns.
- **Fix:** Extend M:49's not-taken list with these. Nothing to add to the spine.

---

## Deliberately left out — fine

These are not needed by any PRD requirement and don't cause incompatible builds. No change needed:

- Redis, Supabase Storage, payments, AI, Fiken, capability tokens/JWKS, plugins, content/services/video split, cutover modes
- `FEATURE_*` flags (the only switches are key presence and `PLAYTEST_RECORDS`)
- Watchdog (replaced by the GitHub Actions daily login check)
- Backup service (already reasoned in the spine's Deferred section)
- Cloudflare worker and DNS (Railway's domain is enough)
- `watchPatterns`, overlap and draining tuning, pytest-xdist
- The reference's vertical-slice module layout (the spine's layered functional core is a recorded decision, M:22)
- CORS (same origin, M:45)

## Checked and landed (no finding)

These memlog entries are in force and match the spine:

- Paradigm (M:22 → Design Paradigm)
- No logic in the database (M:21 → AD-3, apart from H2)
- Single mutation path (M:31 → AD-4, with `plan_version` added per the addendum)
- Snapshot + action log and the playthrough row (M:32, M:33 → AD-5)
- Content YAML, fingerprint and CI gates (M:34, M:50(1)(2) → AD-7)
- Selection and payment step (M:50(6) → AD-8, AD-9)
- Single entry through Caddy (M:45 → AD-12)
- OpenAPI contract (M:30 → AD-13)
- Error shape, daily jobs, `PLAYTEST_RECORDS`, 300 ms logging and test (M:52 → AD-13, conventions, AD-15)
- Email via Resend + Jinja2 (M:51 → AD-11)
- Hosting choice, sleeping off, deletion after analysis, daily check (M:47 → AD-14 / Monitoring)
- Sessions table, logout and revocation (M:44 → AD-10, apart from M6, M7)
- Tester codes (M:50(3) → AD-15)
- Seeding by scripted play (M:50(4) → AD-14)
- Stack items (M:49 → Stack)

The superseded 2026-11-09 entries (Supabase Auth, GoTrue/Mailpit compose, Koyeb/Brevo/Render, the backend serving the frontend, zero cost, the 7-day playtest) correctly appear nowhere in the spine.
