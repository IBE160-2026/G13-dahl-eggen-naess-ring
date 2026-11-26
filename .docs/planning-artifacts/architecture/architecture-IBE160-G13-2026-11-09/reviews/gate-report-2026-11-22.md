# Reviewer gate report, 2026-11-22 (#93)

The spine was re-checked after the changes since 2026-11-13: the reconcile fixes, the nickname (#99), the Vercel boundary (#91), and the PRD's new job hours (#105). Three independent reviewers ran in parallel. Their full reviews are beside this file:
- **Rubric:** `review-rubric-2026-11-22.md` (0 critical, 3 high, 5 medium, 6 low)
- **Adversarial:** `review-adversarial-2026-11-22.md` (1 critical, 7 high, 9 medium, 7 low). All 28 findings from 2026-11-13 are closed.
- **Currency:** `review-currency-2026-11-22.md` (27 claims: 19 verified, 2 wrong, 2 stale, 4 unconfirmed)

The deterministic lint is clean. Its one hit, `{client_ip}`, is a known false positive: it's a Caddy placeholder.

**Verdict:** the nickname and email-once changes hold up. The spine isn't safe to build on for two areas yet: the job-hours stories and the Vercel proxy. The job-hours change reached the PRD after the last spine commit and has no AD. The proxy relies on a wrong fact about Railway.

## Needs a decision

| # | Finding | Options |
|---|---|---|
| **D1** (adversarial C1, rubric H1) | **When is a one-off shift paid?** The PRD says "with this month's wage". But month M's wage is paid when M opens, before the shift can be placed, and Rule Set v1 rule 1 says the plan never adds wages to the current month. Builders will pick different payment points: tax in December, month 60, rule 8. | **(a) Recommended:** paid at the next month's income step, like all wages. Rule 1 stays, and the pay counts as wage income in the month it's paid (tax, rule 8 average). A shift placed in month 60 is then never paid, so shifts aren't offered in month 60. **(b)** Paid when the player continues, as the only wage outside the income step. Rule 1 and FR-47 then need an exception. |
| **D2** (currency R1, adversarial H5) | **How the visitor's address reaches the backend.** Railway's edge removes `X-Forwarded-For` and `X-Real-IP` and puts in the address that connected to it (Railway staff, June and October 2026). Behind Vercel that is Vercel's address, so every tester would share a few network keys, and one person could lock everyone out. | **(a) Recommended:** a small Next.js middleware on Vercel proxies `/api/*`. It sets `x-origin-secret` and the visitor's address in its own header, which Railway passes on unchanged, and drops any value the visitor sent. AD-10 then allows this one proxy (no auth logic) and forbids all other Next.js server code on `/api`. **(b)** `X-Vercel-Forwarded-For`: not confirmed that Vercel sends it to external origins. |

## Fixes I can make without a decision (high)

- **No AD for job hours (rubric H2/H3, adversarial H1–H3):**
  - Add `contract_hours` and `paid_hours` as the only hours functions (cap, free time, slots, July cut).
  - Add a `shifts/` content folder, with the selection step deciding the month's shift offers.
  - Plan slots become a tagged activity/shift entry. A shift raises `plan_version`, and "same as last month" doesn't place shifts again.
  - Add one `job.hours_request` with fixed states. It's cancelled on quit, and a request whose offer would apply after month 60 isn't allowed.
  - Add refusal codes for the new job actions.
  - Update the "PRD as of 2026-11-15" line.
- **Secret gate fails open (adversarial H4):** an empty `ORIGIN_SECRET` on Railway must stop Caddy from starting. Fix: a `CADDY_MODE` setting, a start-up refusal, and a backend check of the secret as backup.
- **Preview deployments reach tester data (adversarial H6, rubric M1):** Vercel's production branch is `playtest`, the secret is set in Production only, and a spike check confirms that a preview's `/api` gets 403.
- **Nickname in stored data (adversarial H7):** results and messages are stored as a text id plus parameters and rendered only in `view()`, never as finished text.

## Medium and low (fix in the same pass)

- **Deferred list:** it still lists the frontend framework and the player information page, which are now decided.
- **Caching:** `Cache-Control: no-store` from the backend is the guarantee. The Vercel header is extra, and its place has to be stated.
- **Region:** set `fra1` explicitly with `regions`.
- **The secret:**
  - make it hex, so a `*` can't act as a wildcard
  - Caddy removes it before passing a request on
  - rotation is described
- **Railway healthcheck:** it goes straight to the backend, not through the gate.
- **Validation errors:** they must never log a password or nickname.
- **Shift pay:** it's rounded on its own.
- **CI:** it runs the Caddy playtest mode once.
- **Backend address:** the bind address on Railway's private network is stated.
- **Versions:** FastAPI 0.165.0 and SQLAlchemy 2.1.9.
- **Confirmed current:** using `routes` together with headers and rewrites (no change needed).
