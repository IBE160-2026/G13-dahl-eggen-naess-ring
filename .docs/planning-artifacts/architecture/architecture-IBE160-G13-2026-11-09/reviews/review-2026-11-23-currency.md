---
title: Review (currency lens): ARCHITECTURE-SPINE.md re-checked against live sources
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-23, status final)
previous: review-currency.md (2026-11-13), review-116-currency.md (2026-11-23, #116 only), .memlog.md entry of 2026-11-22 (Vercel amendment)
lens: Was every committed decision web-researched or reality-checked, not asserted from training data? Are versions current, does each named technology or service still exist and fit as described, and do the platform behaviours the spine relies on still hold?
method: PyPI JSON API, GitHub releases API and raw source at release tags, Docker Hub tags API, vendor docs (Railway, Supabase, Vercel, Resend, Caddy, Python devguide), vendor forums only where the docs are silent. Every source below was read on 2026-11-23 unless marked "carried".
---

# Currency review of the spine, 2026-11-23

**Verdict:** The spine still holds up for sprint 1. Most of it is confirmed, but there is one real problem and two stale version notes. The problem: AD-10 assumes Railway's edge *appends* to `X-Forwarded-For`. Railway's accepted forum answer says the edge *overwrites* it. If that's true, the visitor's address never reaches Caddy. Separately, the Vercel side of the 2026-11-22 amendment is now confirmed by Vercel's own docs, and that settles the "docs disagree" note in the memlog.

**Counts:** 40 confirmed (item 21 with gaps; items 26, 32 and 44 carried from 2026-11-13) · 3 contradicted · 2 unconfirmed (45 items)

## Top items

1. **Railway's edge and `X-Forwarded-For` (item 27, contradicted).** AD-10 says "Railway's edge appends its own peer". The accepted moderator answer (2026-09-29) says Railway overwrites `X-Real-IP` and `X-Forwarded-For`. One Railway employee says the edge strips XFF; another says it appends. The docs say nothing. If the edge overwrites, Caddy's leftmost XFF entry is Vercel's egress address, not the visitor's. All testers would then share a handful of network keys, so the sign-up and login limits would hit everyone at once. The spike check and the Next.js fallback in AD-14 already cover this, but the rule states the uncertain behaviour as fact.
2. **FastAPI pin is stale (item 3).** 0.165.0 came out 2026-11-18. 0.163.2 refactored query, header and form parameter extraction, which is NFR-7 territory. 0.164.0 added opt-in `max_body_size`.
3. **`.railway/railway.ts` isn't read at deploy (item 21).** It is applied with `railway config plan` / `railway config apply`, or with the `railwayapp/config` GitHub Action. In a single-file project, any resource the file leaves out is deleted. It has no Serverless field, and the region goes in `replicas`. Railway stops reading `railway.json`/`railway.toml` in 8 days (2026-12-01). The repo has neither file yet, so nothing needs migrating.
4. **Railway log retention (item 25, unconfirmed).** The docs give Hobby 7 days and name no storage region. A staff forum answer gives 90 days in US West, and says 7 days is only how far back the dashboard shows. The spine's disclosure follows the stricter reading, which is safe, but it should cite where the figure comes from.
5. **SQLAlchemy note is stale (item 6).** 2.1.9 came out 2026-11-16, with ORM bug fixes only.

## Findings

### A. Stack table (spine lines 293-308)

| # | Claim | Spine line | Status | Source + date read | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| 1 | Python 3.12, security-only until 2028-10 | 295 | confirmed | devguide.python.org/versions: 3.12 security, EOL 2028-10 (scheduled); 3.13 security, EOL 2029-10; 3.14 bugfix. Docker Hub `python:3.12-slim` updated 2026-11-08. Read 2026-11-23 | None |
| 2 | uv pinned in the Dockerfile, `uv.lock`, `--locked` | 296 | confirmed | github.com/astral-sh/uv/releases: 0.13.9 (2026-11-17). Read 2026-11-23 | None. Pin `0.13.9` or later at first build |
| 3 | FastAPI 0.162.x (0.162.7, 2026-11-13) | 297 | **contradicted** (stale) | pypi.org/pypi/fastapi/json: **0.165.0 (2026-11-18)**, Python ≥3.11. GitHub releases: 0.163.0 adds `Depends(max_concurrency=…)`; 0.163.1 fixes OpenAPI for a nested computed field; **0.163.2 refactors query, header and form parameter extraction**; 0.164.0 adds `max_body_size` (default `None`, unlimited, 413 on overflow, enforced by Starlette's `RequestBodyLimitMiddleware`); 0.165.0 adds form parsing limits. PR #16781 diff. Read 2026-11-23 | "FastAPI 0.165.x (0.165.0, 2026-11-18); exact pin in `uv.lock`", or drop the dated note. Run the NFR-7 null-vs-omitted tests against the locked version, since 0.163.2 touched parameter extraction. Optional hardening: `FastAPI(max_body_size=…)` (e.g. 64 KiB) with a 413 row in AD-13's table. If you add it, check that the 413 comes out in the `{code, message, state}` shape: the 413 is sent by middleware, which may bypass the `AppError` handlers |
| 4 | Uvicorn | 297 | confirmed | PyPI: 0.54.0 (2026-09-25). Read 2026-11-23 | None |
| 5 | Pydantic + pydantic-settings 2.x | 298 | confirmed | PyPI: pydantic 2.14.4 (2026-11-19), pydantic-settings 2.16.3 (2026-11-13, ≥3.11). Read 2026-11-23 | None |
| 6 | SQLAlchemy 2.1.x (2.1.8, 2026-11-04) | 299 | **contradicted** (minor, stale) | PyPI and GitHub: **2.1.9 (2026-11-16)**, also 2.0.58. The release notes list only ORM bug fixes, none touching asyncpg. Read 2026-11-23 | "SQLAlchemy 2.1.x (2.1.9, 2026-11-16)", or drop the dated note and rely on `uv.lock` |
| 7 | asyncpg 0.32.x | 299 | confirmed | PyPI: 0.32.0 (2026-10-06). Read 2026-11-23 | None |
| 8 | Alembic 1.20.x (1.20.1, 2026-10-22) | 300 | confirmed | PyPI: 1.20.1 (2026-10-22), still current. Read 2026-11-23 | None |
| 9 | PyJWT 2.x refuses empty HMAC keys | 301 | confirmed | PyPI: 2.15.1 (2026-09-28). pyjwt CHANGELOG v2.13.0: "Reject empty HMAC keys outright in `HMACAlgorithm.prepare_key` with `InvalidKeyError`". Short keys only warn (`InsecureKeyLengthWarning`) unless `enforce_minimum_key_length=True`. Read 2026-11-23 | None. Optional: pass `enforce_minimum_key_length=True` to back up AD-14's 32-byte rule |
| 10 | bcrypt 5.x refuses inputs over 72 bytes; `bcrypt(base64(sha256(pw)))` is always 44 bytes | 175, 301 | confirmed | pyca/bcrypt CHANGELOG 5.0.0: "Passing `hashpw` a password longer than 72 bytes now raises a `ValueError`". PyPI 5.0.0 (2025-09-25) is still the latest release. base64 of 32 bytes = 44 ASCII bytes. Read 2026-11-23 | None |
| 11 | Jinja2, latest at first build | 302 | confirmed | PyPI: 3.1.6 (2025-03-05). Read 2026-11-23 | None |
| 12 | resend with the `async` extra, `send_async` (AD-11) | 187, 302 | confirmed | PyPI: 2.55.0 (2026-11-19); `provides_extra: ['async']` → `httpx>=0.25.1`. resend-python `resend/emails/_emails.py` defines `async def send_async`. Read 2026-11-23 | None |
| 13 | PostgreSQL 17 is the Supabase platform default | 303 | confirmed (indirect) | supabase.com/changelog.md: no entry on Postgres 18 or a default change through 2026-11-17. The 2026-10-30 entry recommends 15.19.0.003 / 17.11.0.003+. A web search summary points to a May 2026 Supabase changelog entry naming 17 as the platform default. Read 2026-11-23 | None. Keep the spike step `SHOW server_version` |
| 14 | Local image and Railway fallback on Postgres 17 | 234, 236, 303 | confirmed | Docker Hub `postgres:17.12` updated 2026-11-21. `postgres:18.7` also exists. Read 2026-11-23 | None. Keep `postgres:17` pinned, never `latest` |
| 15 | Caddy 2.11.x (2.11.9; at least 2.11.8) | 304 | confirmed | GitHub releases: v2.11.9 (2026-11-05) is still the latest. Docker Hub 2.11.9 tags rebuilt 2026-11-16 and 2026-11-23. Read 2026-11-23 | None |
| 16 | Docker Compose plugin, 5.x current | 305 | confirmed | github.com/docker/compose/releases: v5.8.0 (2026-11-17). Read 2026-11-23 | None |

### B. Railway (AD-14, AD-10, Stack lines 306)

| # | Claim | Spine line | Status | Source + date read | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| 17 | Hobby plan, USD 5 a month with USD 5 of usage included; cost about USD 5-8 | 237, 306 | confirmed | docs.railway.com/pricing/plans: "$5 / month"; "includes $5 of resource usage per month"; RAM $10/GB/month, CPU $20/vCPU/month. Read 2026-11-23 | None |
| 18 | EU West = Amsterdam | 235, 306 | confirmed | docs.railway.com/deployments/regions: "EU West Metal, Amsterdam, Netherlands, `europe-west4-drams3a`". No plan restriction is stated. Read 2026-11-23 | None |
| 19 | Serverless (sleeping) off for every service | 235, 246 | unconfirmed (default) | docs.railway.com/pricing/cost-control: the toggle is Settings → Deploy → Serverless → "Enable Serverless". The page doesn't state the default. The IaC reference has no serverless or sleep field. Read 2026-11-23 | Keep the spike check. Add: "Serverless is a dashboard toggle, not in `railway.ts`; check after every `railway config apply`" |
| 20 | Config as Code (`railway.json`/`railway.toml`) stops being read on 2026-12-01 | 233 | confirmed | docs.railway.com/reference/config-as-code banner: "Config as Code is deprecated… Existing files keep working for legacy services until 2026-12-01". docs.railway.com/infrastructure-as-code: "new services can't opt in". Read 2026-11-23 | None |
| 21 | Pre-deploy and healthcheck in `.railway/railway.ts` (`preDeploy`), or the service setting | 233, 306, 378 | confirmed, **with gaps** | docs.railway.com/infrastructure-as-code/reference: `service()` fields `start`, `preDeploy`, `healthcheck`, `healthcheckTimeout`, `replicas`, `env`, `domains`… with no region or serverless field. Region is set as `replicas: {"europe-west4": 1}`; the example key differs from the regions page id `europe-west4-drams3a`. docs.railway.com/infrastructure-as-code: "Railway doesn't read `.railway/` during deploys"; it is applied with `railway config plan` / `railway config apply`, or with the `railwayapp/config` GitHub Action. In a single-file project, "omitting a resource means deleting it". Read 2026-11-23 | AD-14: "`.railway/railway.ts` declares both services (Caddy and backend), each with `replicas` in EU West, and is applied with `railway config apply` (or the `railwayapp/config` Action), never automatically on deploy." Spike: run `railway config plan` and confirm the region key and that Serverless and the public domain stay as set. Or keep everything in the dashboard and drop the file from the seed tree |
| 22 | Usage alert USD 6, hard limit USD 10 (Railway's minimum), which takes workloads offline | 237 | confirmed | docs.railway.com/pricing/cost-control: "The minimum amount you can specify as the hard limit is $10"; workloads are taken offline at the limit; reminders at 75/90/100%. Read 2026-11-23 | None |
| 23 | Backend healthcheck `/api/health` | 235 | confirmed | IaC reference `healthcheck`, `healthcheckTimeout`. Read 2026-11-23 | None |
| 24 | Railway's HTTP logs carry client IPs | 179, 235, 281 | confirmed | docs.railway.com/observability/logs: "`@srcIp:<ip>` → Filter by source IP (The client's IP address that made the request)". Read 2026-11-23 | None |
| 25 | Railway stores all logs in US West for 90 days under its DPA | 235, 251 | **unconfirmed** (docs and staff disagree) | docs.railway.com/observability/logs retention table: Free 3 days, Trial 7, **Hobby 7**, Pro 30, Enterprise up to 90. "Upgrading plans will immediately restore logs…". The page names no storage region. Forum station.railway.com/questions/log-retention-and-data-processing-agreem-223bf7c1, employee sam-a, 2026-10-08: "All of those logs are stored in US West…"; "On Hobby, 7 days is how far back you can view logs in the dashboard, not when they are deleted". Read 2026-11-23 | Keep the stricter disclosure. Add the source in the memlog or AD-14: "(Railway staff answer 2026-10-08; the docs show 7 days' visibility on Hobby and name no region)". The upgrade-restores note backs the 90-day reading |
| 26 | `railway run` for ops; `railway ssh` on the Postgres fallback | 236, 238 | confirmed (carried) | Checked in review-currency.md item 35 (2026-11-13). Not re-fetched. The spine already says the fallback image tag is checked when switching | None |
| 27 | "Railway's edge appends its own peer" to `X-Forwarded-For`, so Caddy's leftmost entry is the visitor | 179 | **contradicted** (conflicting vendor statements) | docs.railway.com/networking/public-networking/specs-and-limits lists `X-Real-IP`, `X-Forwarded-Proto`, `X-Forwarded-Host`, `X-Railway-Edge`, and says nothing about XFF. Forum, **accepted** answer by moderator 0x5b62656e5d, 2026-09-29 (station.railway.com/questions/which-client-address-headers-does-the-ra-fb9e36d7): "X-Real-IP, X-Forwarded-For, X-Forwarded-Proto, X-Forwarded-Host are all overwritten at Railway's edge". Forum station.railway.com/questions/does-the-edge-strip-client-x-forwarded-f-613e5cb6: employee phin "We do strip X-Forwarded-For at our edge"; employee sam-a "our edge proxy appends to the chain"; the poster measured that a client-supplied XFF didn't reach the app. Read 2026-11-23 | Don't state "appends" as fact. AD-10 Network: "Whether the visitor's address survives Railway's edge is settled in the spike. Overwrite is the documented-by-moderator default. If the leftmost XFF at Caddy is Vercel's egress address, Caddy reads `client_ip_headers` from a header Railway leaves alone: first try Vercel's `x-vercel-forwarded-for` (if Vercel forwards it to external origins, which Vercel doesn't document), else the Next.js route-handler fallback already in AD-14." The spike's forged-header test should also send a forged `X-Real-IP` and `x-vercel-forwarded-for` |

### C. Supabase (AD-3, AD-14, NFR-11 table)

| # | Claim | Spine line | Status | Source + date read | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| 28 | Free session pooler allows 15 clients; app pool 5 per instance, no overflow; `NullPool` for Alembic and CLI | 234, 249 | confirmed | supabase.com/docs/guides/platform/compute-and-disk: Nano (free) max DB connections 60, pooler max clients 200, **default pool size 15**. Supavisor FAQ: "Session mode can queue clients for up to a minute". The `EMAXCONNSESSION … max clients are limited to pool_size: 15` error is reported in Supabase discussion #22305 and on the Retool community. Read 2026-11-23 | Optional: note that the pool size can be raised in Database settings (within the 60-connection cap), and that a client over the limit waits up to a minute before the error |
| 29 | Free pauses after 1 week without database activity; the daily login check prevents it | 247 | confirmed | supabase.com/pricing: "Free projects are paused after 1 week of inactivity". docs/guides/platform/free-project-pausing: "a few user requests to the database each day over the previous week" is enough; warning email about a week ahead; restorable for 1 year. Read 2026-11-23 | None |
| 30 | 500 MB on Free | 248 | confirmed | supabase.com/pricing: "500 MB database size per project included"; no automatic backups; 2 active projects. Read 2026-11-23 | None |
| 31 | Data API switched off in the dashboard; `/rest/v1/` then stops answering | 82, 240 | confirmed | supabase.com/docs/guides/database/data-api: "Turn **Enable Data API** off… none of the auto-generated REST endpoints respond, regardless of grants or RLS". Read 2026-11-23 | None |
| 32 | RLS on with no policies; backend and Alembic connect as the owner, which bypasses RLS; no `FORCE` | 82 | confirmed (carried) | review-currency.md item 25 (2026-11-13). Not re-fetched; no changelog entry since touches RLS | None |
| 33 | Frankfurt `eu-central-1`; Supabase has no Amsterdam region | 235, 307 | confirmed | supabase.com/docs/guides/platform/regions: Ireland `eu-west-1`, Paris `eu-west-3`, Frankfurt `eu-central-1`, Stockholm `eu-north-1`; no Netherlands. Read 2026-11-23 | None |
| 34 | Session pooler on port 5432, host copied from the Connect dialog, SSL `require` | 234 | confirmed | supabase.com/docs/guides/database/connecting-to-postgres: `aws-[INDEX]-[REGION].pooler.supabase.com:5432`, "copy the exact host from the Connect dialog"; IPv4-only on every plan; session mode supports prepared statements; "Set SSL to `require`" (as `sslmode=require`). Read 2026-11-23 | None |
| 35 | Settings rewrite `sslmode=` to `ssl=` because asyncpg takes `ssl` | 234 | confirmed | SQLAlchemy rel_2_1_9 `dialects/postgresql/asyncpg.py` `create_connect_args`: `opts.update(url.query)`. asyncpg v0.32.0 `connection.py` `async def connect(…, ssl=None, …)` has no `sslmode` keyword. Read 2026-11-23 | None |

### D. Vercel (AD-12, AD-14; the 2026-11-22 amendment)

| # | Claim | Spine line | Status | Source + date read | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| 36 | A `routes` entry in `vercel.json` proxies `/api/(.*)` to Caddy, setting `x-origin-secret` from `ORIGIN_SECRET` with a `request.headers` `set` transform, so a visitor can't supply their own | 194 | confirmed | vercel.com/docs/rewrites (last updated 2026-08-11), "Restricting your origin to Vercel traffic": exactly this pattern (`"type": "request.headers", "op": "set", "args": "$ORIGIN_SECRET", "env": ["ORIGIN_SECRET"]`); "Because the `set` operation replaces any existing value, a visitor can't supply their own". vercel.com/docs/project-configuration/vercel-json: `routes` isn't legacy and "can be used alongside `rewrites`, `redirects`, `headers`…"; an unset variable "stays as a literal string". Read 2026-11-23 | None. That literal fallback fails closed, since Caddy refuses `$ORIGIN_SECRET`, which isn't the real secret. Note for the frontend team: when `routes` and `headers` share one file, `src` matching becomes case-sensitive |
| 37 | Rewrite caching off for `/api/*` (`x-vercel-enable-rewrite-caching: 0`), and the backend sends `Cache-Control: no-store` | 194 | confirmed | vercel.com/docs/rewrites: projects created on or after 2026-04-06 honour upstream `cache-control`/`CDN-Cache-Control` by default; "set the `x-vercel-enable-rewrite-caching` header to `0`" in a `headers` rule to opt out. Read 2026-11-23 | Optional: say where the header goes (a top-level `headers` rule for `/api/(.*)`, as the docs show). `no-store` already stops caching on its own, so this is defence in depth |
| 38 | Vercel overwrites `X-Forwarded-For` with the visitor's address and forwards it to the external origin | 179 | confirmed | vercel.com/docs/rewrites, "Identifying the visitor at your origin": Vercel forwards `x-real-ip` and `x-forwarded-for` = "The public IP address of the visitor", plus `x-forwarded-host` and `x-forwarded-proto`. vercel.com/docs/headers/request-headers (2025-12-13): Vercel overwrites XFF and doesn't forward external IPs. The trusted proxy needed to change that is Enterprise-only. Read 2026-11-23 | Update the memlog. The "docs disagree" note of 2026-11-22 is resolved on the Vercel side. The open question is Railway's edge (item 27) |
| 39 | Functions in `fra1` (Frankfurt) | 194, 235 | confirmed | vercel.com/docs/regions: `fra1` = `eu-central-1`, Frankfurt. Functions default to `iad1`. vercel-json docs: Hobby can pick one region. Read 2026-11-23 | Optional: say it's set with `"regions": ["fra1"]` (or the project setting), because the default is `iad1` |
| 40 | Vercel's edge network may handle a request in the region nearest the visitor | 235 | confirmed | vercel.com/docs/regions: 126 PoPs "route requests over a private network to the nearest Vercel region"; TLS terminates in that region. Read 2026-11-23 | None |
| 41 | Hobby keeps runtime logs for 1 hour | 235, 251 | confirmed | vercel.com/docs/plans/hobby (2026-11-12): Runtime Logs "1 hour of logs". Read 2026-11-23 | None |
| 42 | Hobby is for non-commercial use, "as a school project is"; costs nothing | 235, 237 | confirmed (terms); the fit is an interpretation | vercel.com/legal/terms §4: "You shall only use the Services under a Hobby plan for your personal or non-commercial use". "Commercial" isn't defined. vercel.com/docs/plans/hobby: free; going over a limit usually pauses the feature for 30 days. Read 2026-11-23 | Optional: note that going over a Hobby limit pauses the feature rather than billing. The playtest's traffic is far below the limits |

### E. Resend and Caddy

| # | Claim | Spine line | Status | Source + date read | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| 43 | Resend Free allows 100 emails a day (UTC); reset cap 80 counted per UTC day | 178, 252, 308 | confirmed | resend.com/pricing: 3,000/month, "limited to 100 emails per day", 3 domains. resend.com/docs/api-reference/rate-limit: "resets at midnight UTC — not a rolling 24-hour window"; 429 `daily_quota_exceeded`; 10 req/s per team. Read 2026-11-23 | None |
| 44 | Go-live needs a verified domain | 187 | confirmed (carried) | review-currency.md item 32 (2026-11-13). Not re-fetched | None |
| 45 | Caddy trusts every peer (`trusted_proxies static 0.0.0.0/0 ::/0`) with `client_ip_headers X-Forwarded-For` and takes the leftmost address | 179 | confirmed (Caddy behaviour) | caddyserver.com/docs/caddyfile/options: `trusted_proxies static [private_ranges] <ranges...>`; `client_ip_headers` is a `servers` option, by default only `X-Forwarded-For`, parsed left to right unless `trusted_proxies_strict`. Source caddy v2.11.9 `modules/caddyhttp/server.go` `trustedRealClientIP`: when the peer is trusted, it returns the "first valid left-most IP address". Read 2026-11-23 | None for Caddy. Whether the leftmost entry is the visitor depends on item 27 |

Count rule: each row counts once, under the status in its Status column. Item 21 counts as confirmed, though its fix is still needed. Two sub-points inside confirmed or contradicted rows are open and go to the spike rather than counting as separate items: the `replicas` region key (item 21) and whether Vercel forwards `x-vercel-forwarded-for` (item 27).

## What changed since 2026-11-13

| Item | 2026-11-13 | 2026-11-23 |
| --- | --- | --- |
| FastAPI | 0.162.7 | 0.165.0 (2026-11-18) |
| SQLAlchemy | 2.1.8 | 2.1.9 (2026-11-16) |
| pydantic | 2.14.3 | 2.14.4 (2026-11-19) |
| resend | 2.53.2 | 2.55.0 (2026-11-19) |
| uv | 0.13.8 | 0.13.9 (2026-11-17) |
| Docker Compose | 5.7.1 | 5.8.0 (2026-11-17) |
| postgres:17 image | 17.12 (2026-11-12) | 17.12, rebuilt 2026-11-21 |
| Caddy, Alembic, asyncpg, PyJWT, bcrypt, Jinja2, Uvicorn | unchanged | unchanged |
| Railway Config as Code cutoff | 2026-12-01 | 2026-12-01, now 8 days away; `railway.ts` is applied by CLI or Action, not at deploy |
| Vercel visitor IP to an external origin | docs disagree (memlog 2026-11-22) | Confirmed by the rewrites docs: `x-forwarded-for` and `x-real-ip` carry the visitor's address |

## Suggested memlog lines (for the architect; not added by this review)

- (version) Checked on PyPI/GitHub/Docker Hub 2026-11-23: FastAPI 0.165.0, SQLAlchemy 2.1.9, pydantic 2.14.4, resend 2.55.0, uv 0.13.9, Compose 5.8.0. Unchanged: Caddy 2.11.9, Alembic 1.20.1, asyncpg 0.32.0, PyJWT 2.15.1, bcrypt 5.0.0, postgres:17.12.
- (constraint) `.railway/railway.ts` isn't read during deploys. It is applied with `railway config apply` or the `railwayapp/config` Action. In a single-file project, resources the file leaves out are deleted. Region goes in `replicas`, and Serverless stays a dashboard toggle.
- (question) Does Railway's edge overwrite, strip or append to `X-Forwarded-For`? The accepted forum answer says overwrite, and the staff answers conflict. The spike decides which header Caddy reads the visitor's address from.
