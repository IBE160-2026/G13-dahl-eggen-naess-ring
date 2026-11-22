---
title: Adversarial review (2026-11-22) — compliant pairs that still collide
created: 2026-11-22
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-22: nickname in AD-2/AD-13/conventions/AD-15; AD-12 Vercel → Caddy on Railway with x-origin-secret; AD-10 leftmost X-Forwarded-For; reset token in the URL fragment)
consulted: ../.memlog.md, ../SOLUTION-DESIGN.md, ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (FR-1, FR-47, FR-52 to FR-56, NFR-3, updated 2026-11-22), ../../../briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md (Rule Set v1 rules 1, 3, 8, 10, 12), reviews/review-adversarial.md (2026-11-13)
lens: Two units one level down, each obeying every AD to the letter, that still build incompatibly. Each hole names the pair and the smallest AD tightening that closes it.
prior review: all 28 findings of review-adversarial.md (2026-11-13) are closed in the spine text; none is repeated here.
---

# Adversarial review 2026-11-22: compliant pairs that collide

**Verdict:** not safe to build the job-hours stories or deploy the Vercel proxy as written. The 2026-11-22 PRD change to job hours (FR-47: hours offers and one-off shifts) reached the spine only through its `binds:` list. No AD says when a one-off shift is paid, what kind of thing it is, whose hours it counts in, or where an hours request lives, and Rule Set v1 rule 1 contradicts the PRD on the first of these. The Vercel → Caddy chain has a fail-open origin gate, an internal contradiction between AD-10 and AD-14's fallback, and no rule tying Vercel's deploy branch and preview deployments to the playtest backend. The nickname rule leaks through stored results and messages. Every fix is a sentence or two. None adds a service.

| Severity | Count |
| --- | --- |
| Critical | 1 |
| High | 7 |
| Medium | 9 |
| Low | 7 |

---

## Critical

### C1. A one-off shift has two legal payment points, in different months and different tax years

- **Location:** AD-9 (one writer), AD-4 (months: continue closes M and opens M+1), AD-6 (rounding points). Rule Set v1 rule 1 against PRD FR-47 "One-off shifts" and "Never in a slot, except one-off shifts".
- **Unit A, the month-plan / activities story (FR-52, FR-53):** a one-off shift sits in a slot and is applied like an activity "at the end of the choice step" when the player continues. FR-47 says its pay comes "with this month's wage", so the story calls `ledger.receive(amount, cause=shift choice id)` at the close of month M. It obeys AD-9 (the ledger moves the money) and AD-4 (same transaction).
- **Unit B, the income-step story (rule 1, rule 3, FR-47 "no wage is paid outside the income step"):** month M's wage was already paid when M opened (AD-4: continue opens M+1 with rule 1 from income onward), before the player could place the shift. Rule 1 says "Wages are paid only at the income step. Activities and the month plan never add hours or wages to the current month." So this story pays the shift at the income step that opens M+1, together with that month's wage. It also obeys every AD.
- **Collision:**
  - The player gets the money a month apart depending on who built it. The month summary, FR-57 progress, and the "missing amount" for activities planned after the shift all disagree.
  - Under A, a shift placed in December is paid after December's tax step and after the year's tax is final (rule 3), so it is never taxed, although FR-47 says "taxed as wage income". Under B, it is taxed in the next in-game year.
  - Under A, the pay lands in the current account at the activities step. In a crisis month that is "money a money action brings in" and AD-9's `receive()` sends it to overdue card minimums first. Under B it is ordinary wage income, which AD-9 says never pays the card outside the debt step.
  - Month 60 has no later income step, so under B a month-60 shift is unpaid. Extra shifts are blocked in month 60 for exactly this reason (FR-47); one-off shifts have no such rule.
  - Rule 8's wage income ("this month and the two before") counts the shift in M under A and in M+1 under B, so a crisis trigger can fire in one build and not the other.
- **Fix:** this needs a decision by Dahl, because the PRD (new today) and Rule Set v1 rule 1 disagree. Add one of these to AD-9 and fix the losing document to match:
  - **(a) Paid at the next income step (fits rule 1, keeps one wage point):** *"A one-off shift placed in month M is recorded in the state as earned wage of M. It is paid by `receive()` at the income step that opens M+1, with its own cause, as wage income of M+1 for rule 3, rule 8 and rule 16. One-off shifts aren't offered in month 60."* The PRD's FR-47 wording changes from "with this month's wage" to "with next month's wage".
  - **(b) Paid when the player continues (fits today's PRD wording):** *"One-off shift pay is the only wage outside the income step. It is paid by `receive(kind=wage)` when the shift is applied at the end of the choice step, is never routed by the crisis money-in order, and counts as wage income of month M for rule 3 (the tax step of M+1 picks it up, and December's shift is added to December's tax before the year closes), rule 8 and rule 16."* Rule Set v1 rule 1's last two sentences change, and worked example 24/25 gets a case.
  - Either way, add a worked example with a December shift and one in a crisis month.

---

## High

### H1. "This month's hours" has no single definition, so the cap, free time, slots and pay each count a one-off shift differently

- **Location:** AD-1 (rules only in the engine), AD-6 (hours `Decimal`, cap rounded down). PRD FR-47 (cap check: "this month's hours with it stay within rule 10 and the 173 h monthly cap"; "no wellbeing effect of its own"), FR-52 (slots fixed at month open from "that month's hours, extra shifts included"), rule 12 (free time from hours).
- **Unit A, the shift-placement validator:** it adds every placed shift to "this month's hours" for the cap check, as FR-47 says. It writes a helper `month_hours(state)` that includes shifts.
- **Unit B, the wellbeing story (rule 12) and the slots story (FR-52):** they reuse the engine's `month_hours(state)` because AD-1 wants one place per figure. Free time falls with every shift, so the shift has a wellbeing effect that FR-47 forbids, and the next "same hours" preview in FR-56 shows a different slot count from the one month open computes.
- **Unit C, the July cut (rule 10):** it cuts the summer job "using that month's hours, extra shifts included" at July's income step, before any shift is placed, so it never sees shifts. A shift placed in July is then checked against a cap the cut already filled, by a different formula.
- **Rounding drift:** in grunnskole the cap is 12 × 52 / 12 = 52 h. At 11 h a week the month is 47.67 h. A 5 h shift is allowed if one builder rounds the hours down (47 + 5 = 52) and refused if another keeps the `Decimal` (52.67 > 52). AD-6 says how the cap rounds, not how the compared hours do.
- **Fix (AD-6, add under Money):** *"The engine has two hour functions and nothing else computes hours: `contract_hours(state, month) → Decimal` (weekly hours plus running extra shifts, × 52 / 12, plus summer-job hours after July's cut), used for free time (rule 12), slots (FR-52), rule 10's weekly check and every preview; and `paid_hours(state, month) → Decimal` = `contract_hours` plus the month's placed one-off shifts, used for the 173 h cap and pay. Both compare unrounded against `monthly_cap(month) → int` (rounded down). One-off shifts never enter `contract_hours`."*

### H2. A one-off shift is an activity to the content authors and a work item to the ledger

- **Location:** AD-7 (layout lists `activities/`, no shift kind), AD-8 (decides only the event and messages), AD-9, AD-4 (`plan_version`). PRD FR-47, FR-52, FR-53 ("no activity pays money in the MVP", cost NOK 0 or more, effects ±10), FR-57 (activity spend by kind).
- **Unit A, content authors:** "each has a name and its hours, from the content library", and it is placed "like an activity", so they add `activities/A-vakt-*.yaml` with a kind `vakt`, cost 0, effects 0, and an `hours` field the activity schema doesn't have.
- **Unit B, the engine's job story:** a shift is work. It models shifts as config entries of the job, keyed by workplace, and the plan as a list of activity ids.
- **Collision:**
  - The content check rejects A's files (unknown field, an activity that pays), or accepts them and FR-57's "activity spend by kind" and FR-52's "plan total covers activities' costs only, never wages" now count shifts.
  - "Same as last month" (FR-52) re-places last month's activities "where they're still available". Under A it re-places last month's shift; under B it can't, because B's plan holds no shift.
  - FR-53's "once a month" and the activities' ±15 wellbeing cap apply to A's shifts and not to B's.
  - Which shifts are on offer this month is not decided anywhere. One builder lists every eligible shift, another draws some. If drawn at view time, the offer changes on reload (FR-12); AD-8 owns only the event and messages.
- **Fix:**
  - AD-7 layout, add: *"`shifts/` holds one-off shifts (id, name, hours, age range, flags), with their own schema in the addendum. They are not activities."*
  - AD-8, add: *"The selection step also decides the month's one-off shift offers when the month opens, from the player's job and eligibility, and stores them in the state; nothing else decides them."*
  - Engine state convention (AD-5 or AD-9), add: *"A month-plan slot holds a tagged entry, `activity` or `shift`. Placing or removing either raises `plan_version`. 'Same as last month' places only activities. Activity totals, the ±15 cap, once-a-month and FR-57's spend read only `activity` entries."*

### H3. An hours request and its answer have two owners

- **Location:** AD-8 (messages decided at month open, stored), AD-5 (state shape deferred to engine stories), AD-4 (action union deferred). PRD FR-47 "Hours offers", FR-55 "Answers about hours", FR-56.
- **Unit A, the job story:** it keeps `job.hours_request = {direction, asked_in}` and, at month open, computes the offer itself (`job.hours_offer = {delta, applies_from}`). The accept action names the job.
- **Unit B, the selection step (AD-8):** it owns "the messages" and sees a triggered offer, so it computes the answer text and the offer when it builds the message, storing the offer payload in `messages[i]`. The accept action names the message id.
- **Collision:**
  - Two stored copies of the offer, computed at different points: B checks rule 10 against the month the message arrives (M+1), A against the month the change applies from (M+2), which FR-47 requires. A request made in month 18 gets a 12 h or a 40 h ceiling depending on the builder.
  - The player quits or takes a new job in M. A clears the request; B still sends the employer's answer for a job that's gone, and its accept action changes the new job's hours.
  - Month 59: the answer arrives in 60 and would apply from 61. Neither unit refuses the request; extra shifts have a month-60 rule, hours requests don't.
  - The refusal for "one request at a time" is invented twice, with different codes (AD-13 deferred the enum, but not who owns the check).
  - The lapse at month end ("an offer not answered by the end of the month lapses") is done by A at continue and by B at the next month open; a retry across that boundary finds different states.
- **Fix (AD-8, add):** *"An hours request has one owner, `job.hours_request` in the engine state, with states `asked(M) → offered(M+1, delta, applies_from=M+2) | declined(reason) → accepted | lapsed`. The offer is computed once, when M+1 opens, against rule 10's limit for M+2, before the selection step runs. The selection step only adds a message that points to it. The accept and decline actions name the request, not the message. Quitting or changing job cancels a request in any state, and a request can't be made when M+2 would be after month 60. The request lapses when M+1 closes."*

### H4. The origin-secret gate fails open when `ORIGIN_SECRET` is missing on Railway

- **Location:** AD-12 (Caddy, one Caddyfile with the secret from env; locally "no origin secret is required"), AD-14 (secret checks are the backend app's: `JWT_SECRET`, `HASH_SECRET`).
- **Unit A, the Caddy story:** one Caddyfile for every environment, as AD-12 says. Locally no secret is required, so the check is written as "403 unless `x-origin-secret` equals `{$ORIGIN_SECRET}`", and an empty variable means "off". That is how the local stack passes.
- **Unit B, ops (AD-14):** the playtest setup checklist covers the backend's settings, and the backend refuses to start without a strong `JWT_SECRET`, `HASH_SECRET` and `PUBLIC_BASE_URL`. `ORIGIN_SECRET` belongs to the Caddy service and Vercel, and nothing refuses to start without it.
- **Collision:** a Caddy service deployed without the variable, or with it renamed, accepts every request on its Railway domain. Then AD-10's trust in the leftmost `X-Forwarded-For` lets anyone pick their network key, so the login limits can be bypassed by rotating a header, and the backend is reachable around Vercel. Nothing fails, and the spike check runs only once.
- **Fix (AD-12, Caddy):** *"The Caddyfile selects its mode from `CADDY_MODE` (`local | railway`), never from whether a secret is set. In `railway` mode the container's entrypoint refuses to start unless `ORIGIN_SECRET` is at least 32 bytes and not a placeholder, and the site block refuses every request without it. The backend also requires `ORIGIN_SECRET` when `APP_ENV=playtest` and checks it, in constant time, in one middleware before routing, so the gate holds even if Caddy's doesn't."* (If the backend checks it, Caddy passes the header on; the logging rule then covers it, see L2.)

### H5. AD-10 forbids frontend server code in the auth path; AD-14's fallback puts it there, and nothing keeps Next.js off `/api`

- **Location:** AD-10 Network ("Sign-up, login and reset always go browser → Vercel's proxy → Caddy → backend, never through a Next.js function or other frontend server code"), AD-14 Sprint-1 spike ("If the visitor's address doesn't arrive, the frontend team proxies `/api/*` through a Next.js route handler that sets it in a header Caddy trusts only with the origin secret"), AD-2 ("the client talks only to `/api/*`").
- **Unit A, the frontend team after a failed spike check:** it follows AD-14 and builds `app/api/[...path]/route.ts`, which forwards every `/api` call, including login, and holds `ORIGIN_SECRET` in a function.
- **Unit B, the auth story:** it follows AD-10, which says that path never exists, and designs the network key and the `Set-Cookie` handling on that assumption.
- **More compliant frontend moves that break the backend's assumptions:**
  - Next.js middleware with the default matcher runs on `/api/*` too, and can read and rewrite the session cookie.
  - A server component or server action calls `GET /api/game` on the player's behalf. To pass Caddy it needs the origin secret in server code; a developer who needs it in the browser for local testing names it `NEXT_PUBLIC_ORIGIN_SECRET`, which ships it in the bundle. Locally, a server-side `fetch("/api/game")` needs an absolute URL that differs from the playtest one, so local and playtest diverge.
  - The visitor's address seen by Caddy for those calls is a Vercel function's, so every player shares one network key.
- **Fix:**
  - AD-10, replace the last sentence of Network with: *"Every `/api` request comes from the browser, through Vercel's edge proxy, to Caddy. The frontend has no `app/api` or `pages/api` routes, its middleware matcher excludes `/api`, and no server component, server action or route handler calls the API. `ORIGIN_SECRET` exists only in Vercel's project settings and Railway's Caddy service; no `NEXT_PUBLIC_` variable holds it, and CI fails if the built client bundle contains it."*
  - AD-14, replace the fallback with: *"If the visitor's address doesn't arrive, the team decides before the playtest between (a) a network key that ignores the address (address-only limits) and (b) a Next.js proxy, which then replaces this rule in AD-10 with its own written rules for cookies, the client address and the secret."*

### H6. Vercel's deploy branch and preview deployments aren't tied to the playtest backend

- **Location:** AD-14 ("The playtest deploys from a `playtest` branch; `main` is the working branch"), AD-12 (`ORIGIN_SECRET` "set in both Vercel and Railway"), AD-13 (committed OpenAPI contract).
- **Unit A, ops on Railway:** the backend and Caddy deploy from `playtest`, as AD-14 says.
- **Unit B, the frontend team on Vercel:** the project keeps Vercel's default production branch, `main`, and `ORIGIN_SECRET` is added for "all environments", the default in the dashboard.
- **Collision:**
  - The production frontend is built from `main` and talks to a backend built from `playtest`. A new action type or response field merged to `main` reaches testers before the backend has it, and the committed contract no longer describes the pair that's live. AD-13's stale-schema check runs per commit, not across the two deploys.
  - Every preview deployment (every frontend PR and branch) carries the secret and proxies `/api/*` to the playtest backend with real tester accounts. Unreviewed frontend code can log testers in; team members testing previews write playtest records unless their accounts are `is_test`. The preview origin also differs from `PUBLIC_BASE_URL`, so cookies and reset links behave differently there.
- **Fix (AD-14, Playtest host, add):** *"Vercel's production branch is `playtest`, the same branch Railway deploys from, and the two deploy from the same commit. `ORIGIN_SECRET` is set only for Vercel's Production environment; preview deployments have no `/api` target on the playtest (they point nowhere, or at a separate non-playtest backend). During playtest hours the team merges to `playtest` only when both deploys can follow at once."*

### H7. The nickname leaks into stored results and stored messages through "store the result once"

- **Location:** AD-13 Game text (nickname "never written into the state document, the action log or a stored text"), AD-4 ("request_id already in action_log → stored result + current player view"), AD-5 (`action_log` holds the "result part"), AD-8 (selection result "stored in the state"), FR-54 (figures in a message are the engine's).
- **Unit A, the pipeline story:** AD-4 says a repeat returns the stored result. The simplest compliant reading is to store the response's result section as it was sent: month summary lines, cause notes, "dropped activity" notes, crisis texts, already rendered by the one formatting function, nickname filled in.
- **Unit B, the selection step:** FR-54's bank message must keep the figure it had when it arrived ("Du har nådd halvparten av sparemålet ditt" with that month's amount), and FR-55 says messages are stored. The builder freezes the figure by storing the rendered text in `state.messages`, nickname included, because the text is rendered by the one function at that point.
- **Collision:** both obey "one formatting function" and "store once", and both put the nickname in the state or the action log, which AD-13 forbids. A renamed player sees the old nickname in old messages and in every repeated response. CI replay fixtures and the seed script's target states then contain nicknames, and replay breaks when a fixture's nickname changes.
- **Fix (AD-13, add after the nickname sentence):** *"What is stored, in the state (messages, notes, summaries) or in `action_log`, is a text id plus a parameter map of ints, content ids and choice ids, never rendered text. Figures are frozen by storing them in the map. Rendering, nickname included, happens only in `view()` and in the response builder, from the stored id and map. The content check fails a text whose placeholders aren't all supplied by its map or the nickname."* AD-15, add: *"`records.on_action` receives `user_id` and `is_test`, not the `users` row."*

---

## Medium

### M1. The secret's form in `vercel.json` and its rotation are undefined

- **Location:** AD-12 Playtest ("sets `x-origin-secret` from the `ORIGIN_SECRET` environment variable with a `request.headers` `set` transform"), AD-14 spike checks.
- **Pair:** the frontend team writes the transform; if `vercel.json` can't read an environment variable at that point, the compliant way to "set the header" is the literal value in a committed file. Ops sets the Railway side and never sees the frontend repo. Nothing checks that the literal isn't in git, and the spike list doesn't include it.
- **Rotation:** changing the secret means changing Vercel and Railway at the same moment; whichever deploys first refuses the playtest.
- **Fix (AD-12):** *"The secret's value is never in the repo; CI's secret scan covers `vercel.json` and the frontend build. If `vercel.json` can't take it from an environment variable, that's a spike failure handled under AD-14, not a reason to commit it. Caddy accepts `ORIGIN_SECRET` or `ORIGIN_SECRET_NEXT` during a rotation, and the rotation order is: add the next secret to Caddy, switch Vercel, remove the old one."* Add "secret not in the repo or bundle" to the spike checks.

### M2. Who turns off caching, and for which responses

- **Location:** AD-12 ("turns rewrite caching off for `/api/*` (`x-vercel-enable-rewrite-caching: 0`). The backend also sends `Cache-Control: no-store` on every `/api` response").
- **Pair:** the frontend team reads the header as something the backend sends (it reads like a response header); the backend team reads it as a `vercel.json` setting. Neither sets it. Separately, responses Caddy makes itself (403 without the secret, 502 while the backend restarts during a deploy) don't come from the backend and carry no `no-store`, and a cached 502 or 403 on `/api/game` keeps the playtest down after the backend is back. Also, a legacy `routes` array can't be combined with `headers`, `rewrites` or `redirects` in the same `vercel.json`, so a frontend developer who adds a `headers` block for fonts breaks the proxy build.
- **Fix (AD-12):** *"The `vercel.json` `/api` route entry sets the request header and the caching opt-out itself. The backend sends `Cache-Control: no-store` and `CDN-Cache-Control: no-store`, and Caddy adds the same to every response it makes itself. The frontend's `vercel.json` uses only `routes` (no `headers`, `rewrites` or `redirects` keys); other headers go in `next.config`."*

### M3. Railway health checks meet the origin gate

- **Location:** AD-14 ("The backend service's healthcheck is `/api/health`"), AD-12 (Caddy refuses everything without the secret), Health convention.
- **Pair:** ops adds the same healthcheck to the Caddy service, because AD-14 says sleeping is off "for every service" and a Caddy that never passes would never deploy. Railway's checker sends no secret, gets 403, and the Caddy deploy fails. The Caddy builder then exempts `/api/health` from the secret, and the next one widens it to `/api/*` "for health".
- **Fix (AD-12, Caddy):** *"Caddy answers `GET /caddy-health` itself with 200, before the secret check, without proxying it; that is the Caddy service's Railway healthcheck. No `/api` path is exempt from the secret. The backend service's healthcheck is `/api/health` on its own port inside Railway."*

### M4. Validation errors can log passwords, emails and nicknames

- **Location:** Logging convention ("no email address, password, nickname or reset token"), AD-13 (one handler for `RequestValidationError`), AD-2 (refusal tests).
- **Pair:** the error-handler story logs `exc.errors()` at warning level to make 422s debuggable, which is the usual FastAPI pattern. Pydantic v2 errors carry the rejected `input` and often `ctx`. The auth story validates a too-short password, a bad email or an invalid nickname, so each 422 writes the typed value into Railway's 90-day logs in the US. Both obey their ADs.
- **Fix (Logging convention, add):** *"Error handlers log only the `loc` and `type` of each validation error, never `input`, `ctx` or the request body. A test posts a known password, email and nickname that fail validation, and asserts none of them appear in the captured log."*

### M5. Personal data in paths or query strings reaches logs we don't control

- **Location:** Logging convention ("Our access logs leave out … query strings; Railway's own HTTP logs are outside our control"), AD-13 (endpoints deferred to stories).
- **Pair:** an account story builds `GET /api/account/email-available?email=…` for the sign-up form, or `PUT /api/account/nickname/{nickname}`. That's allowed: our logs drop query strings. Railway's HTTP logs and Vercel's edge logs record full paths and queries, so addresses and nicknames sit in two processors' logs, which the player information page (NFR-3) doesn't name.
- **Fix (AD-13, Contract, add):** *"Email addresses, passwords, nicknames and tokens travel only in JSON bodies, never in a path or query string. There is no endpoint that tells whether an address has an account."*

### M6. Shift pay is rounded, counted and linked in more than one way

- **Location:** AD-6 ("each job's pay on its own (rule 10)"), AD-9 (causes, per-choice totals), rule 3 (year's wage income), rule 8 (wage income over 3 months), rule 16 (spending level).
- **Pair:** the shift story rounds each shift's pay on its own and books it with its cause (FR-36). The income story adds shift hours to the part-time job's hours and rounds once, because the shift is "with this month's wage" at the same employer. Two shifts at NOK 139.40 for 3.5 h each differ by a krone. The tax story sums `receive()` calls marked `wage`; the rule 8 story sums the job's pay records. One counts shifts, the other doesn't.
- **Fix (AD-6, add):** *"Each one-off shift's pay is rounded on its own under rule 2, like a separate job. The state keeps one wage-income record per month (each job and each shift, with its cause), written only by the step that pays wages, and rule 3, rule 8 and rule 16 read only that record."*

### M7. The Railway Caddy mode is never run before the playtest

- **Location:** AD-12 (local Caddy: no proxy trusted, no secret), AD-10 (playtest: all peers trusted, leftmost XFF), Tests convention (CI covers the pipeline, not Caddy).
- **Pair:** CI and every developer run only the local block. The Railway block (secret check, trusted proxies, `client_ip_headers`, `X-Client-IP` overwrite) is first exercised in the spike, then changed by hand when something fails. A later edit to the local block isn't mirrored, and nothing notices.
- **Fix (Tests convention, add):** *"CI starts Caddy in `railway` mode against a stub upstream and asserts: 403 without the secret, the leftmost `X-Forwarded-For` arriving as `X-Client-IP`, a client-sent `X-Client-IP` overwritten, `/docs` not served, and `no-store` on Caddy's own responses."*

### M8. The backend's bind address on Railway's private network isn't fixed

- **Location:** AD-12 (Caddy upstreams from env), AD-14 (backend has no public domain).
- **Pair:** the backend Dockerfile runs `uvicorn --host 0.0.0.0`, the usual default. Caddy's upstream is `backend.railway.internal:<port>`, which resolves to IPv6 on Railway's private network in environments created before dual-stack. The backend listens on IPv4 only, so every request is a 502, while the backend's own healthcheck passes.
- **Fix (AD-14, Playtest host, add):** *"The backend listens on `::` (dual-stack) on `PORT`; Caddy's upstream is `{$BACKEND_UPSTREAM}` (`backend.railway.internal:${PORT}` on Railway, `backend:8000` in compose)."* Add "Caddy reaches the backend over the private network" to the spike checks.

### M9. New job actions have no refusal codes and no continue-time re-check

- **Location:** AD-13 (one enum of codes, tagged turn or input), AD-4 (action union deferred), FR-53 (activities re-checked at continue), FR-47.
- **Pair:** the job story refuses a second hours request, a shift over the cap, or a shift for a player without a job with `invalid_input` (422); the shift-placement story, copying activities, uses a new `cannot_place` it tags as turn (409). Separately, activities are re-checked at continue; the activity builder re-checks shifts as activities (eligibility, payment) and the shift builder doesn't re-check at all, so a shift placed before a job change in the same month is paid by one build and dropped by the other.
- **Fix (AD-13, Errors, add):** *"Job and shift refusals are input refusals (422) with their own codes in the enum: `hours_request_pending`, `over_hours_cap`, `no_job`, `shift_not_offered`."* AD-8 or FR-53 note: *"At continue, a placed shift is re-checked only against `paid_hours` and the cap; a failure drops it with a note, like an activity."*

---

## Low

### L1. `/openapi.json` on Railway: "only `/api/*`" vs "`/openapi.json` goes to the backend"

- **Location:** AD-12 Caddy. One sentence says Caddy on Railway serves only `/api/*`; the next routes `/openapi.json` to the backend. Vercel proxies only `/api/(.*)`, so the file is unreachable there anyway.
- **Fix:** *"On Railway, `/openapi.json` isn't served; the committed contract is the source."*

### L2. The secret travels past Caddy, and the comparison isn't constant-time

- **Location:** AD-12, Logging convention.
- **Pair:** Caddy forwards every header by default; a backend debug log of request headers then holds the secret. A header matcher compares in ordinary time.
- **Fix (Logging convention):** *"Request headers are never logged. If the backend checks the secret (H4), it compares with `hmac.compare_digest`; otherwise Caddy removes `x-origin-secret` before proxying."*

### L3. Nickname placeholder namespace and edge cases

- **Location:** AD-13 Game text, AD-7, FR-58 content check.
- **Pair:** content authors write `{kallenavn}`, the formatting function expects `{nickname}`, and a figure placeholder named `navn` exists elsewhere. A 16-character nickname overflows a heading the UX sized for 8.
- **Fix (AD-13):** *"The nickname placeholder is `{kallenavn}`, reserved: no figure placeholder uses it. The content check renders every text with a 2-character and a 16-character nickname and fails on any unknown placeholder."*

### L4. The reset page can leak the fragment to frontend scripts

- **Location:** AD-12 Reset link.
- **Pair:** the fragment never reaches a server, but the frontend's analytics or error reporter (Vercel Web Analytics, Speed Insights, a Sentry SDK) can read `location.href` before the page calls `history.replaceState`.
- **Fix (AD-12):** *"The frontend loads no analytics, monitoring or third-party scripts (NFR-3), and `/nytt-passord` reads and removes the token before anything else runs."*

### L5. The daily GitHub check: which path, which account, what it proves

- **Location:** Monitoring convention, Structural Seed (GH → Vercel), AD-15 (`is_test`).
- **Pair:** ops points the check at Caddy's Railway domain for speed, which needs `ORIGIN_SECRET` as a GitHub secret (a third copy). The check account is created by hand and never marked `is_test`, so it adds a tester to records and to the export. A login-only check also passes when cookie passthrough is broken.
- **Fix (Monitoring convention):** *"The check goes through `PUBLIC_BASE_URL` only and never holds `ORIGIN_SECRET`. Its account is `is_test`. It logs in, then calls `GET /api/game` with the returned cookie, and alerts if either fails."*

### L6. Local `next dev` without Caddy splits the `/api` namespace

- **Location:** AD-12 Local ("Caddy … routes everything outside `/api/*` … to the frontend's Next.js server").
- **Pair:** frontend developers run `next dev` on port 3000 directly, as Next.js expects. `/api/game` then hits Next.js and returns 404, so they add a `next.config` rewrite to the backend that bypasses Caddy, and with it `X-Client-IP` and the cookie origin that the backend expects.
- **Fix (AD-12, Local):** *"Developers open the app only through Caddy's origin; `next dev` runs as Caddy's upstream, not as the address the browser uses. The frontend has no `next.config` rewrite for `/api`."*

### L7. Hours-change and shift previews in the view have no named function

- **Location:** AD-13 (one view function), FR-47 (each offer shows money left after spending and next month's slot count), FR-56.
- **Pair:** the job-view builder computes "next month's slot count" for an offer by calling the slot formula with the offer's hours; the month-open builder computes slots from `contract_hours` including extra shifts that end next month. The preview and the real slot count differ in the month extra shifts end.
- **Fix (AD-13, add):** *"Every preview of a future month (slots, money left, free-time warning) is the engine's projection of that month's `contract_hours`, the same function month open uses, never a separate formula in the view."*
