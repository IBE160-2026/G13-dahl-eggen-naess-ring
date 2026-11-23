---
title: Update check — closure of the 2026-11-23 validation findings, and an adversarial pass on the delta
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (working copy on docs/arkitektur-116, uncommitted; 68 KB, was 56 KB)
inputs:
  - validation-report-2026-11-23.md and its four sources (review-2026-11-23-rubric, -adversarial, -drift, -currency)
  - ../.memlog.md (the last seven entries, 2026-11-23)
  - git diff of the spine, SOLUTION-DESIGN.md §9, PRD prd.md and addendum.md, Rule Set v1 (brief addendum), EXPERIENCE.md
lens: (1) closure per critical/high/medium finding; (2) two units one level down that obey every AD and still build incompatibly because of the new or changed text
method: independent read; no file other than this one was edited. Line numbers are the working copy's.
---

# Update check, 2026-11-23

**Verdict:** the update closes every high finding and all but three mediums, as the memlog says, but the new text opens five high seams of its own. Two sit in the continue composition (rule 8 now runs before the December BSU deduction, and `open_month` names the wrong function). One is the result envelope (the result is now both engine state and a separate `result` field). One is the transport-failure rule (it reads Caddy's new JSON bodies as refusals). The last is the new year/month gate, which fails the Rule Set's own disclosure texts. Each needs one sentence. Fix them before epics and stories.

| | Count |
| --- | --- |
| Critical/high/medium findings in the four reviews | 39 (+ 6 currency items) |
| Closed | 36 (+ 6 currency) |
| Partly | 3 |
| Open | 0 |
| New findings | 0 critical · 5 high · 13 medium · 13 low |

## 1. Closure

"Closed*" means the fix was applied as specified, and a new finding in section 2 attacks the new text.

### Rubric (review-2026-11-23-rubric.md)

| Finding | Status | Closed by |
| --- | --- | --- |
| H1 proxy fallback vs AD-10 | Closed* | AD-10 Network l.181 (route handler is the only frontend server code on `/api`, forwards cookies, `no-store`, `x-client-origin-ip`); AD-12 l.196 ("route handlers other than the AD-10 fallback"). See N-M7 |
| H2 origin secret not enforced | Closed* | AD-12 Caddy l.197 (entrypoint guard, daily check asserts `403`); Monitoring l.296. See N-M7 (the guard keys on "trusted proxies set") |
| H3 tests vs play library | Closed* | AD-7 Worked examples l.146; Freeze l.144 (seed assertions warn until the freeze). See N-M11 (replays) |
| M1 response envelope | Closed* | AD-13 Identity l.212, Errors l.220. See N-H3, N-H4 |
| M2 no-playthrough view | Closed | AD-13 No playthrough l.211 |
| M3 who commits | Closed* | AD-4 session discipline l.120. See N-M13 |
| M4 sessions in lock order | Closed | AD-4 Lock order l.94; AD-10 Sessions l.178 (last_active_at before the session row, only on a slide) |
| M5 worker count | Closed | AD-14 l.239 |
| M6 observability | Closed | Observability row l.290; catch-all `500` l.220 |
| M7 bloat | **Partly** | Safari, bcrypt, XFF-safety and edge rationale moved to the memlog; spike list moved to #92; `history.replaceState` and the duplicate player-information text removed. But the file grew from 56 KB to 68 KB (N-M12) |
| L1-L8 | Closed | l.28 and sources; l.84 (RLS CI test); tree l.380-397; map l.405-421; Deletion l.293; Ops l.246; AD-12 l.196 (Production only; the `routes` question is moot, since currency item 36 says `routes` works next to `headers`); AD-1 l.72 |

### Adversarial (review-2026-11-23-adversarial.md)

| Finding | Status | Closed by |
| --- | --- | --- |
| H1 result as a second projection | Closed* | AD-13 Results l.210; AD-5 l.126. See N-H3, N-M9 |
| H2 when placeholders are filled | Closed* | AD-13 Game text l.213. See N-M2 |
| H3 after-the-plan preview path | Closed* | AD-4 Months l.96. See N-H1, N-H2 |
| H4 ledger tags from the cause | Closed | AD-9 Flow classes l.163 |
| H5 crisis money actions | Closed* | AD-9 One writer l.159. See N-M3 (open-option payouts) |
| H6 fields added after a freeze | Closed* | AD-7 Loading l.145; Config row l.291. See N-M1 |
| H7 draws per machine | Closed | AD-6 Seed and draws l.133 |
| H8 no view before a start / after ended | Closed | AD-13 No playthrough l.211; AD-4 One pipeline l.93 |
| M1 retried start's request_id | Closed | AD-4 Protocol fields l.92 |
| M2 account requests retried | Closed | AD-2 l.78 |
| M3 inactivity job | Closed | AD-10 Sessions l.178; Jobs l.294; AD-15 l.269 |
| M4 session checked before the lock | Closed | AD-4 Lock order l.94 |
| M5 seed can't pin versions | Closed | AD-4 One pipeline l.93 |
| M6 Next.js server code calls `/api` | Closed | AD-12 Playtest l.196 |
| M7 Vercel/Caddy errors lack the shape | **Partly** | Caddy bodies added (AD-12 l.197), and the transport-failure rule added (l.220). The two conflict: Caddy's `503` has a `code`, so it reads as a refusal (N-H4) |
| M8 malformed request vs state | Closed | AD-13 Errors l.220 |
| M9 lax mode, plan_version | Closed* | AD-4 One endpoint l.91. See N-M6 |
| M10 FR-8 timer | Closed | AD-10 Sessions l.178 |
| M11 FR-42 totals and choices | Closed* | AD-9 Choice ids l.161, Totals l.162. See N-M3 |
| M12 Decimal JSON path | Closed | AD-5 l.126; AD-13 l.213 |
| M13 two money formats | Closed* | AD-13 Game text l.213. SOLUTION-DESIGN still contradicts it (N-M10) |
| L1-L9, L11 | Closed | l.217; l.72; l.243; l.181; l.239; l.143; l.269-270; l.212; l.170; l.180 |
| L10 | **Partly, deliberate** | The year/month gate was taken (l.144; see N-H5). Nickname limits as game figures were not taken: they stay settings (Accounts row l.292) |

### Drift (review-2026-11-23-drift.md)

| Finding | Status | Closed by |
| --- | --- | --- |
| H1 one-off shifts, hours answer | Closed | AD-7 Layout l.142 (`shifts/`); AD-8 l.152; PRD addendum one-off shift schema and message `links to` row; FR-54 |
| H2 loan quote read path | Closed* | AD-13 Quotes l.219; AD-4 l.91; binds FR-25. See N-M4, N-M5 |
| M1 AD-2 parameters | Closed | AD-2 l.78; PRD NFR-7 input sentence |
| M2 NFR-7 refusals for #105 | Closed | PRD NFR-7 (three new bullets); AD-13 table `request_pending`. An answer with no open offer has no listed code (N-L6) |
| M3 shift pay rounding | Closed | AD-6 Money l.134; PRD FR-47 ("age in the month the shift is worked, rounded once") |
| M4 field-level errors | Closed* | AD-13 Errors l.220. See N-M8 |
| M5 nickname preview | Closed | AD-13 Game text l.213 |
| M6 rule 10 "player sets hours" | **Partly** | Rule Set rule 10, PRD addendum P3 and the UJ-6 note fixed. D12, D25 and D26 stay with #117, as the PRD memlog says |
| L1-L8 | Closed | l.11 and l.28 (FR-35 dropped from binds); binds and map; l.218; l.213; l.170; l.28; l.209; PRD FR-25 narrowed to 12/24/36 |
| L9 | Closed by the diff | You expected partly, but both bullets are edited: PRD NFR-3 now names the hosts, and EXPERIENCE says "the server stores it". Nothing in L9 is left open |

### Currency (review-2026-11-23-currency.md)

| Item | Status | Closed by |
| --- | --- | --- |
| 27 Railway edge overwrites XFF (contradicted) | Closed | AD-10 Network l.181 (the spike picks the header); AD-14 spike l.248 |
| 3 FastAPI stale | Closed | Stack l.306 (0.165.x; refusal tests against the lock) |
| 6 SQLAlchemy stale | Closed | Stack l.308 |
| 21 `railway.ts` not read at deploy | Closed | AD-14 l.241 |
| 19 Serverless default | Closed | AD-14 l.241 (dashboard toggle), spike l.248 |
| 25 log retention source | Closed | AD-14 l.243 (cites the staff answer) |
| Optional notes (`max_body_size`, where the caching header goes, `regions: ["fra1"]`) | Partly taken | `fra1` "set explicitly" taken; the rest left out, which is fine |

## 2. New findings on the delta

### High

#### N-H1. Continue now runs the rule 8 check before December's BSU deduction, which reverses the PRD's order

- **Where:** AD-4 Months l.96: "`apply_plan` (… wellbeing, and the rule 8 evaluation …), then the December step, `close_month` and `open_month`".
- **Source:** PRD FR-12 (prd.md:598): "… then wellbeing, and in December the BSU deduction (rule 9). The rule 8 check runs at the end of the month." Rule 9 pays the deduction into the current account.
- **Collision:**
  - **Engine story:** builds continue as written. A player at −NOK 500 in December with a NOK 1,200 deduction gets a crisis month in January.
  - **Worked-example story:** follows FR-12. The deduction clears the trigger, so there is no crisis.
  - **View:** the trigger status and goal progress "after the plan" come from `apply_plan` alone, so in December they leave out the deduction, which the year end shows as coming (l.217).
- **Fix (AD-4 Months):** *"`apply_plan` ends with wellbeing. Continue then runs the December step, the rule 8 evaluation and `close_month`. The view's after-the-plan figures run `apply_plan` and, in December, the December step on a copy (neither draws)."*

#### N-H2. The continue composition names AD-9's totals-only `open_month`, and leaves out the new month and the ending

- **Where:** AD-4 Months l.96 lists continue as exactly `apply_plan`, the December step, `close_month` and `open_month` "(AD-9)". AD-9 Month totals l.170 defines `open_month(M+1)` as the ledger call that opens the totals "before M+1's income step".
- **Collision:**
  - **Month-loop story:** reads AD-4 as the full list. M+1's rule 1 steps (income, tax, costs, unexpected expense, instalments and interest, savings interest), the crisis re-check when a crisis month opens (rule 8) and the AD-8 selection step have no caller.
  - **Another builder:** treats `open_month` as "open the whole month" and puts the income step inside `ledger.py`, which breaks "only `ledger.py` writes the totals" in the other direction.
  - **Month 60:** continue from month 60 calls `open_month(61)`. Rule 13 and the ending aren't named.
- **Fix (AD-4 Months):** *"… then the December step, `ledger.close_month(M)`; after month 60, the rule 13 check and the ending; otherwise `ledger.open_month(M+1)` followed by M+1's opening steps (rule 1 up to the event, the crisis-month re-check, and the AD-8 selection step)."*

#### N-H3. The result is now both engine state and a separate `result` field in the envelope

- **Where:** AD-13 Results l.210 says the result is "engine state, not a separate response", and a repeat `request_id` gets "the current view with that result marked as replayed". AD-13 Identity l.212 says every game response is `{result?, state, …}`. SOLUTION-DESIGN §9 repeats both.
- **Collision:**
  - **API story:** fills `result` with a rendered result next to `state`. That is a second rendering path outside the view's exclusion test, which is the leak adversarial H1 closed.
  - **Frontend story:** reads `state`'s open-month results. It either shows the result twice or ignores `result`.
  - **Replay after the month has moved on:** another device has continued, so the retried action's result is no longer in the open month. "Marked as replayed" has nothing to mark. One builder renders the stored `action_log` result, a third path. Another returns nothing, which breaks NFR-7's "returns the same result as the first time".
- **Fix (AD-13 Results):** *"The envelope's `result` is only a reference `{result_id, replayed}` to an entry in `state`'s results, never rendered text. When that entry is no longer in the open month, a replay returns `result: null, replayed: true` with the current view, and the client shows the current state. NFR-7's 'same result' is met by the action being applied once."* (The PRD's NFR-7 wording should note this.)

#### N-H4. Caddy's new JSON bodies make a `503` count as a refusal, so the client never retries it

- **Where:** AD-12 Caddy l.197: `403 {"code":"origin_refused"}` and `503 {"code":"unavailable"}`. AD-13 Errors l.220: "A response under `/api` without a JSON body that has `code` is a transport failure: the client retries … and never shows it as a refusal."
- **Collision:**
  - **Frontend error story:** follows l.220 to the letter. Caddy's `503` during a deploy restart has a `code`, so it is a refusal. The client shows a refusal with no `message` (Caddy sends none, though the envelope requires Norwegian text) and doesn't retry with the same `request_id`. That is the FR-6 "still trying" case M7 was meant to fix.
  - **`500 internal_error`:** in the same position. It is always a rolled-back transaction, safe to retry, but it is classed as a refusal.
  - **Caddy story:** sends exactly the bodies AD-12 names.
- **Fix (AD-13 Errors):** *"The client classifies by `code`, not by body: `unavailable`, `internal_error`, and any response without a JSON `code` are transport failures, retried with the same `request_id` (`internal_error` at most once). Every other code is a refusal. Caddy's bodies also carry a fixed Norwegian `message`."*

#### N-H5. The new year/month-name gate fails the Rule Set's own disclosure texts, and fails CI even before the freeze

- **Where:** AD-7 Freeze l.144: the schema gate (which fails CI while unfrozen) "fails a text that writes a four-digit year or a month name outside the month placeholder".
- **Source:** the disclosure texts live in `texts/` (AD-7 Layout l.142) and are served as "Om tallene" (l.209, l.211). Rule Set D1 "satsene for 2026", D2 "fra 1. april 2026", D3 "i august 2026", D6 "2026-tall", D9 "fra april til oktober", D17 "bursdag i januar … august til juni, og juli er sommerferie". These are real-world dates, not game months.
- **Collision:**
  - **Content-check story:** builds the gate over every text. The first PR that adds the 26 D-texts turns CI red, and the gate is not one that warns.
  - **Content authors:** have to choose between dropping the sources' dates, which NFR-4 and FR-40 want, and misusing the month placeholder, which renders "april i fjor".
- **Fix (AD-7 Freeze):** *"The year and month-name gate applies to game text (events, messages, results, cause lines, endings, room). Disclosure texts and `source` fields name real dates and are exempt."*

### Medium

#### N-M1. `backfill.yaml` sits outside every fingerprint, so it can change frozen mechanics silently

- **Where:** AD-7 Loading l.145. `content/config/backfill.yaml` lies outside every version folder. The fingerprint and the "fails if the fingerprint changes" gate cover the folders only (l.143-144).
- **Collision:** an engine-fix story corrects a backfilled value for `v1`, and the CI story's fingerprint gate passes. Running playthroughs pinned to frozen `v1` change mechanics mid-life, which is exactly what AD-7 prevents.
- **Fix (AD-7 Loading):** *"A frozen version's fingerprint includes its backfill values. Backfill entries are append-only, and CI fails if an existing (version, field) entry changes."*

#### N-M2. "Only nickname and month at view time" forces live figures to go stale

- **Where:** AD-13 Game text l.213: figures are captured when the item enters the state, and "only the nickname and the month placeholder are resolved when the view is built". Other statuses l.218 and Quotes l.219 need live figures.
- **Collision:**
  - **Content authors:** put the hours offer's "kroner left after spending" into the employer's answer template (FR-47 says the offer shows it). It is captured at arrival, so it is stale after a change of spending level.
  - **View story:** shows the live preview as a status, and the two figures disagree on one card.
  - **"Hvorfor?" cause lines:** these show a balance's cause shares, which change every month. Captured when the line is created, they also go stale.
- **Fix (AD-13 Game text):** *"Captured parameters apply to texts of past items (arrived messages, results, closed-month lines). Figures of open items (offer previews, cause shares of a current balance, quotes, teasers, available activities) are view statuses shown next to the text, never placeholders in its template, and the content check rejects such placeholders."*

#### N-M3. The choice and money-in lists are now exhaustive, but they leave out #105's actions and open-option payouts

- **Where:** AD-9 Choice ids l.161 names what is and isn't a choice. AD-9 One writer l.159 runs the rule 8 money-in order "after every money action or crisis choice".
- **Collision:**
  - **One-off shifts:** in neither list. FR-47 links shift pay "to the shift as its cause (FR-36)", which needs a choice id. One build ranks a NOK 558 shift in FR-42. Another gives it a system cause, which breaks FR-36.
  - **Other #105 actions:** accepting extra shifts or an hours offer, saying no, quitting, the card switch and the payment mode are in neither list either.
  - **Consumer loan in a crisis month:** it is an open option, neither a money action nor a crisis choice. One build lets the payout pay overdue minimums, another doesn't, so the crisis ends in one build and continues in the other.
- **Fix (AD-9 Choice ids, One writer):** *"Placed one-off shifts and accepted extra-shift and hours offers are choices; a no, quitting, the card switch and the payment mode are not. The money-in order also runs after an open option raises the current account."*

#### N-M4. The quote endpoint's input, refusals and response shape aren't fixed

- **Where:** AD-13 Quotes l.219 (`GET /api/game/quote?kind=loan&amount=&term=`); AD-4 One endpoint l.91 (strict models); AD-13 Identity l.212 ("every game response is the envelope").
- **Collision:**
  - **API story:** reuses the take-loan action's strict model for the query. In strict mode `"20000"` from a query string is a string and refused, so every quote request fails.
  - **Another builder:** uses lax parsing. A `term=48` or an amount above the cap then gets an undefined error code.
  - **Response shape:** one build returns the full envelope with `state`, another a bare quote.
- **Fix (AD-13 Quotes):** *"Quote parameters are query-string integers parsed in lax mode. A term outside the config list, or an amount outside 5,000 to the cap in steps of 1,000, is `422 invalid_input`. The response is `{quote, server_time}` with no `state`, and the quote is not an action and shares only the engine's quote function."*

#### N-M5. Loan terms now have two content homes

- **Where:** AD-13 Quotes l.219 and the Config row l.291 put the terms in `content/config/vN/`. The PRD addendum option types (addendum.md:128) still give an option "a loan (allowed range and terms)". Rule Set v1 has no parameter row for consumer loan terms, though the Config row requires one.
- **Collision:** a content author gives the month-49 loan option its own terms, the quote reads the config list, and the sheet and the option disagree.
- **Fix (PRD addendum and Rule Set):** *"The loan option type takes its range and terms from config, never its own. Rule Set v1 gets a 'Consumer loan terms: 12, 24, 36 months' parameter row."*

#### N-M6. Strict mode covers only `action`, and strict Python-mode validation refuses valid enum and UUID strings

- **Where:** AD-4 One endpoint l.91 ("the engine's own action models in strict mode"); AD-2 l.78 (wrongly typed fields refused).
- **Collision:**
  - **Envelope fields:** `month`, `request_id` and `playthrough_id` aren't said to be strict, so `"month": "5"` passes in one build and is refused in another.
  - **Enum and UUID fields:** FastAPI validates the parsed body in Python mode, where strict Pydantic refuses a `str` for an `Enum` or `UUID` field. An action model using `Enum` for the card payment mode refuses every valid request.
- **Fix (AD-4 One endpoint):** *"The whole request body is strict. Choices use `Literal` and ids use `str` or a UUID field with JSON-mode validation, and the refusal tests include one valid request per action member."*

#### N-M7. Caddy's mode is three independent variables, and the fallback isn't closed

- **Where:** AD-10 Network l.181 (`trusted_proxies` and `CLIENT_IP_HEADERS` from environment variables; "locally no proxy is trusted"); AD-12 Caddy l.197 (the guard runs "if trusted proxies are set"); AD-12 Local l.198 (no origin secret).
- **Collision:**
  - **Playtest:** with the trusted-proxies variable left unset, the guard passes and `{client_ip}` becomes the edge's address. Every tester shares one network key, which is the currency C1 failure.
  - **Local:** empty `{$CLIENT_IP_HEADERS}` or `{$TRUSTED_PROXIES}` makes the Caddyfile fail to parse.
  - **Fallback:** it doesn't say that the `vercel.json` `routes` entry is removed (Vercel's `routes` match before functions, so the handler is never reached) or that the handler sets `x-origin-secret` itself. If the `routes` proxy stays, a visitor's own `x-client-origin-ip` passes through it with the secret, and Caddy trusts it.
- **Fix (AD-10 Network, AD-12 Caddy):** *"One `CADDY_MODE` (`local` or `playtest`) sets trusted proxies, client-IP headers and the secret check, and the entrypoint refuses `playtest` unless all three are set and valid. In the fallback the `routes` entry is removed, the route handler sets `x-origin-secret` and overwrites `x-client-origin-ip`, and the spike sends a forged `x-client-origin-ip`."*

#### N-M8. The account-form `fields` codes cut across status codes

- **Where:** AD-13 Errors l.220: "An input refusal on an account form also carries `fields`" with `email_in_use` and `wrong_password`. In the table, `email_in_use` is `409` and `wrong_password` is `403`, not input refusals (`422`).
- **Collision:**
  - **Sign-up story:** returns `422 invalid_input` with `fields: [{email, email_in_use}]`.
  - **Frontend:** handles `409 email_in_use` as the table says.
  - **Nickname validation:** built as a Pydantic validator, it arrives as `RequestValidationError` with no field codes. Built as an `AppError`, it carries them.
- **Fix (AD-13 Errors):** *"Every account-form refusal carries `fields`, whatever its status: `409 email_in_use` and `403 wrong_password` carry their one field, and `422 invalid_input` lists every failing field. The one FR-1 validation function raises `AppError`, and the `RequestValidationError` handler maps type errors to `fields` too."*

#### N-M9. It isn't said which month's results hold continue's result

- **Where:** AD-13 Results l.210 ("appends it to the open month's results"); AD-9 l.170 (`close_month` stores the summary lines).
- **Collision:** continue closes M and opens M+1. One build appends its result to M's list, which is no longer shown, so a reconnect after continue shows nothing (FR-6). Another starts M+1's list with it. A third clears results at `open_month`.
- **Fix (AD-13 Results):** *"`ledger.open_month` starts an empty results list. Continue's result is the first entry of M+1's list and refers to M's stored summary lines."*

#### N-M10. SOLUTION-DESIGN §9 contradicts the spine and itself on signs

- **Where:** SOLUTION-DESIGN §9 "Money per month" row: "Amounts come without a sign, and you show the sign the screen needs". The new "Amounts" row and spine AD-13 l.213 say "signed flows included, is a string from that function".
- **Collision:** the frontend team builds against the old row, adds signs with `Intl` (adversarial M13 again), and the engine's strings and the frontend's disagree.
- **Fix (SOLUTION-DESIGN §9):** *"Each part comes as a raw integer and a signed, formatted string; show the string, and use the integer only for bar lengths."*

#### N-M11. Replay checks load a play library, but AD-7 now names only two steps that may

- **Where:** AD-7 Worked examples l.146 ("the content check and the seed-state check are the only CI steps that load a play library"); AD-6 Replay l.135; Tests convention l.298 ("replays … run on every PR"); AD-9 l.170 (identity test "for every … replay").
- **Collision:** a test-infrastructure story blocks play-library paths outside the two named steps, and the replay story's logs (event and option ids) fail to load.
- **Fix (AD-7 Worked examples):** *"… the content check, the seed-state check and the replay check are the only CI steps that load a play library."*

#### N-M12. The spine grew from 56 KB to 68 KB, and rubric M7 regressed

- **Where:** the whole file. Rubric M7 asked for less rationale and story-level detail.
- **Problem:** the update moved four rationales out but added more story-level detail: field-code lists, the quote query string, Caddy body literals, the `railway config apply` mechanics, the `pg_try_advisory_xact_lock` name, `model_dump(mode="json")`. Stories will copy these, and they will rot.
- **Fix:** *"Move the field-code list, the Caddy bodies, the quote query string and the Railway apply mechanics into SOLUTION-DESIGN §9 or the stories, and keep in the spine only the rule each one serves."*

#### N-M13. Committing on `AppError` makes any pipeline write made before a refusal durable

- **Where:** AD-4 session discipline l.120: the dependency commits on an `AppError` refusal (needed so failed-login rows count). The same paragraph lists `request_id` among the `INSERT … ON CONFLICT … RETURNING` conflicts.
- **Collision:** a pipeline builder claims the `request_id` with that insert before calling the engine, and the engine then refuses. The commit keeps an `action_log` row for a refused request, and a retry "returns the stored result" of something that never happened.
- **Fix (AD-4 session discipline):** *"The pipeline raises every refusal before its first write, and the `action_log` insert is its last write."*

### Low

- **N-L1. The advisory lock scope** (Jobs l.294): `pg_try_advisory_xact_lock` is released when the first per-account `delete_account` transaction commits, so another instance can take over halfway. **Fix:** *"Each job holds a session-level advisory lock on its own connection for the whole run."*
- **N-L2. A stale sequence diagram** (AD-4 l.107-111): it shows "lock users row, then playthrough row" without `sessions`, and returns the "current player view" for an invalid body, which is now `state: null`. **Fix:** *"Update the diagram to the l.94 lock order and the l.220 validation path."*
- **N-L3. The re-read applies only to the pipeline:** on GET, the quote, the disclosure upsert and the nickname change, a user deleted after the dependency's check gets a `none` view, and the slide re-issues a cookie for a row its `UPDATE` didn't find. **Fix:** *"The dependency answers `401` when its slide `UPDATE` changes no row."*
- **N-L4. "Om tallene" with an `ended` row** (l.211): it is unclear whether the "shown playthrough" is the ended row (not shown, per AD-5) or the start versions. **Fix:** *"With `status: ended`, 'Om tallene' uses the start versions."*
- **N-L5. Goal figures can change between the view and the start:** a freeze between the `none` view and the start pins other goal figures than those shown. **Fix:** *"The start action carries the library version the view showed, and a mismatch is `409 game_changed`."*
- **N-L6. No code for an answer with no open offer:** PRD NFR-7's "answer to an hours offer that isn't open" has no code in the table (`request_pending` covers only "already open"). **Fix:** *"List it under `409` as `offer_not_open`, or say it is `already_chosen`."*
- **N-L7. Observability gaps:** `request_id` in the log line is ambiguous (account requests have none), and the daily check reading Railway's error lines needs a Railway token in GitHub. **Fix:** *"The middleware makes a server request id and logs the game `request_id` beside it; the daily check uses a read-scoped Railway token stored as a GitHub secret."*
- **N-L8. "Only POST … is retried automatically"** (l.78) literally forbids re-fetching `GET /api/game` when the connection comes back (FR-8). **Fix:** *"… only POST `/api/game/actions` among state-changing requests."*
- **N-L9. Stale SOLUTION-DESIGN rows:** §9 "Text" still says "nickname on its own, for the settings"; "Knowing if the view is stale" still lists a 5-minute idle fetch; §3 says a retry "returns the first result"; "Loan sheet" hard-codes 12/24/36. **Fix:** *"Align these rows with l.178, l.210, l.213 and l.219."*
- **N-L10. A field added after a freeze may be left out of an unfrozen version,** since it is optional in the model, so the engine gets `None`. **Fix:** *"The content check fails an unfrozen version that leaves out a backfilled field."*
- **N-L11. The seed warning keys on the newest library** (l.144), not on the version each seeded user pins (l.93). **Fix:** *"The seed assertions warn while the seeded user's pinned library is unfrozen."*
- **N-L12. `state: null` vs NFR-7:** `state: null` for a malformed body (l.220) departs from NFR-7's "returns the current progress". **Fix:** *"Add to NFR-7 that a malformed request returns no state, and the client fetches it."*
- **N-L13. One view function, but no state to call it with:** with no playthrough, `view(state, …)` has no state. A second start-view function would escape the exclusion test. **Fix:** *"`view` takes an optional state, and the exclusion test covers the `none` and `ended` views."*

## 3. Spine vs edited sources (summary)

| Pair | Status |
| --- | --- |
| PRD FR-25 / AD-13 Quotes | Consistent (12/24/36, config). Rule Set row missing, and the addendum's option type still has its own terms (N-M5) |
| PRD FR-47 / AD-6 | Consistent (rate for the month worked, rounded once at placement) |
| PRD FR-54, FR-55 / AD-8 | Consistent (hours answer as an offer) |
| PRD FR-56 (a no is stored) / AD-2, AD-9 | Input covered. The choice status is unset (N-M3) |
| PRD NFR-7 / AD-2, AD-13 | Inputs consistent. A no-open-offer code is missing (N-L6). "Same result" vs replay (N-H3). `state: null` (N-L12) |
| PRD NFR-3 / AD-14 | Consistent |
| PRD FR-12 order / AD-4 Months | **Contradiction** (N-H1) |
| PRD addendum shift schema / AD-7, AD-8 | Consistent. "Per month … configuration-backed" has no Rule Set row (low, with N-M5) |
| Rule Set rule 10 / AD-6 | Consistent. D12/D25/D26 stay with #117 |
| Rule Set D-texts / AD-7 gate | **Contradiction** (N-H5) |
| SOLUTION-DESIGN §9 / AD-13 | Envelope, errors, quotes and nickname rows match. Signs contradict (N-M10). The `result` duplication is copied (N-H3). Minor stale rows (N-L9) |
| EXPERIENCE.md | Consistent ("the server stores it") |
