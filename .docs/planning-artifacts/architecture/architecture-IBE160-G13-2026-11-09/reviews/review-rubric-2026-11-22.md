---
title: Rubric review — ARCHITECTURE-SPINE.md (amended 2026-11-22)
reviewer: rubric lens (BMad architecture reviewer gate)
date: 2026-11-22
spine: ARCHITECTURE-SPINE.md (status final, updated 2026-11-22)
driving PRD: prds/prd-IBE160-G13-2026-10-22/prd.md (final, updated 2026-11-22)
---

# Rubric review — spine as amended 2026-11-22

## Scope and method

The review covers what changed since the 2026-11-13 gate: commits cc24ef5 (2026-11-15 follow-up), 9b5e61e (nickname, #99) and 75d1503 (Vercel frontend, reset link, player information, email once, #91/#50). It also covers the PRD commit 7079911 (#105), which came **after** the spine's last change. That commit replaced the hours setting with employer hours offers and added one-off shifts placed in activity slots. The whole spine was then read against the good-spine checklist. Sources read: the spine, the `.memlog.md` tail, the SOLUTION-DESIGN.md headings, the PRD diffs of 75d1503 and 7079911, the PRD addendum (schemas, P3), and Rule Set v1 rules 1 and 10 in the brief addendum.

**Verdict: not yet ready for epics and stories on the job and hours area. The rest holds.** The nickname and Vercel amendments are sound and well bounded. Today's PRD change to hours (#105) was never reconciled with the spine (no memlog entry, and the spine still cites "PRD as it stands on 2026-11-15"). It also conflicts with Rule Set v1 and the PRD addendum, which the spine treats as authorities. That leaves real divergence points for the engine, content and job-view stories. There are also two gaps in the operational envelope around Vercel: preview and production environments, and a fallback that breaks a rule.

Counts: 0 critical, 3 high, 5 medium, 6 low.

---

## High

### H1 — One-off shift pay contradicts Rule Set v1 rule 1 and addendum P3, and the spine is silent

- **Location:** AD-9 (ledger, `receive()`), AD-6 (money and rounding), Design Paradigm month loop (rule 1); PRD FR-47 "One-off shifts", FR-52; Rule Set v1 rule 1; PRD addendum P3.
- **Problem:** PRD FR-47 (today) says a one-off shift placed in this month's plan is "paid with this month's wage, taxed as wage income". Rule Set v1 rule 1 says "Wages are paid only at the income step. Activities and the month plan never add hours or wages to the current month." Addendum P3 gives the reason: "This month's income and tax are already calculated when the month opens." FR-47's own bullet "no wage is paid outside the income step" still stands next to the new one. The engine has three ways to read this: pay at continue together with the planned activities (this breaks rule 1 and P3), pay at next month's income step (this contradicts "this month's wage"), or recompute this month's income step (this breaks the month loop). Two engine stories will choose differently, and worked examples built on rule 1 may fail. The spine says the PRD and Rule Set v1 decide *what* the game does, so this is a conflict between its two authorities that it has to surface.
- **Suggested fix:** Add an open question to the memlog and resolve it with Dahl before engine stories start. Then amend Rule Set v1 rule 1 (or FR-47) and record the outcome in AD-9 in one sentence, for example "one-off shift pay enters the ledger through `receive()` with the shift's choice id at <step>, and counts as wage income for rule 3 and rule 8". Also say whether the pay counts towards rule 8's "wage income" average and towards the frikort or tax sum (rule 3). FR-47 implies both, but it doesn't state them.

### H2 — Hours offers and one-off shifts have no content kind, schema or layout slot

- **Location:** AD-7 Layout (library folders), AD-16, the Deferred row "Content schemas in detail" (which says "the addendum's schemas apply"); PRD addendum message schema ("links to": open option, extra shifts, one-time gift only).
- **Problem:** FR-47 says one-off shifts come "from the content library" with a name and hours. FR-55 adds employer answers to hours requests as triggered offers. Neither exists in the addendum's schemas, and the AD-7 layout (`events/ activities/ messages/ room/ options/ expenses/ texts/ lists.yaml`) has no place for shifts. Since the Deferred row defers to schemas that don't cover them, content authors and engine builders will diverge. A shift could become an activity of a "shift" kind in `activities/`, a new `shifts/` folder, or an item in `lists.yaml`. The hours answer could become an open option in `options/` (FR-48 machinery) or an engine-generated message with a text template in `messages/` or `texts/`. The fingerprint and the content check (FR-58) can't gate a kind nobody has defined.
- **Suggested fix:** Amend AD-7 Layout with one line that names where one-off shifts live and which schema they use. The smallest change is `activities/` with an activity kind `shift` in `lists.yaml`, since FR-52 already treats a shift as a placement. Also state that the hours-offer answer is an engine-generated triggered message whose text lives in `messages/` (yes and no variants) and is not an FR-48 open option. Hand the matching schema rows to the PRD addendum.

### H3 — Spine not reconciled with today's PRD (#105). Its stated basis is stale

- **Location:** spine intro line 26 ("The PRD (final, as it stands on 2026-11-15)"); `.memlog.md` (no #105 entry); AD-4 `plan_version`; AD-6; AD-8; AD-13 view; Capability map.
- **Problem:** The PRD commit 7079911 (21:06) came after the last spine commit 75d1503 (21:01). No memlog entry records that the spine was checked against FR-47, FR-52, FR-55 and FR-56 as rewritten. Several smaller points are now unstated where stories need them:
  - **Pending hours request.** "One request at a time", the answer next month, and lapsing at the end of the month all need state (a pending request, an offer with an expiry month). The Deferred row "Other fields of the engine state" covers the fields, but no AD says the hours offer is a state-triggered item of the AD-8 selection step. FR-55 implies that it is outside the message cap.
  - **`plan_version`.** AD-4 lists the plan changes that raise it as "place, remove, same as last month". It doesn't say that placing or removing a one-off shift counts, or whether "same as last month" places last month's shifts again. FR-52 says plans don't carry over, and shifts are "for this month".
  - **Rounding.** AD-6 names "each job's pay on its own (rule 10)". It doesn't say whether one-off shift pay is rounded on its own or added to the part-time hours before rounding. That is a NOK 1 difference that fails worked examples.
  - **Cap check.** The one-off shift check is weekly limit × 52 / 12 and the 173 h cap, against "this month's hours". AD-6 lists the monthly hour cap as rounded down, but nothing says whether a July summer-job cut, already applied at the income step, counts in "this month's hours".
  - **Stale wording in the spine and its companions.** Rule Set v1 rule 10 still says "the player sets weekly hours". SOLUTION-DESIGN.md has no hours wording to fix.
- **Suggested fix:** Run a short reconcile of the spine against 7079911 and log it in `.memlog.md`. Update the intro to "as it stands on 2026-11-22". Add three things to the relevant ADs: (a) AD-8: hours-offer answers are state-triggered, outside the cap, and only answerable in their month; (b) AD-4: placing or removing a one-off shift is a plan change, plus whether "same as last month" includes shifts; (c) AD-6: one-off shift pay is rounded on its own (or not) under rule 2. Raise the Rule Set v1 rule 10 wording with the PRD owner.

---

## Medium

### M1 — Vercel preview and production environments aren't decided. The frontend and the playtest backend can deploy from different branches

- **Location:** AD-14 Playtest host ("The playtest deploys from a `playtest` branch; `main` is the working branch"), AD-12 Playtest.
- **Problem:** Railway deploys the playtest from `playtest`. Nothing says which Git branch is Vercel's production branch. By default Vercel builds production from the repo's default branch (`main`) and makes a preview deployment for every other branch and PR. Two divergences follow. First, a frontend built from `main` can run against a backend on `playtest` with a different committed OpenAPI contract. Second, if `ORIGIN_SECRET` is set for all Vercel environments, every preview URL also proxies into the playtest database from an origin that isn't `PUBLIC_BASE_URL`. The session cookie and the reset links then point elsewhere. The spike checks don't cover either case.
- **Suggested fix:** In AD-14, add that Vercel's production branch is `playtest`, `ORIGIN_SECRET` is set for the Production environment only, and preview deployments have no `/api` proxy target (or point to no backend). Add a spike check that a preview URL's `/api` gets `403`.

### M2 — The visitor-IP fallback contradicts AD-10's own rule

- **Location:** AD-14 Sprint-1 spike checks (fallback: "the frontend team proxies `/api/*` through a Next.js route handler"), AD-10 Network (last sentence: "Sign-up, login and reset always go browser → Vercel's proxy → Caddy → backend, never through a Next.js function or other frontend server code").
- **Problem:** If the spike fails on the visitor address, the named fallback is exactly what AD-10 forbids. The rule as written then can't be followed, and stories built on either sentence diverge. A route-handler proxy also moves credentials and cookies through frontend function code and its logs, which AD-10 was guarding against. Vercel's runtime logs are a processor note in AD-14.
- **Suggested fix:** Qualify the AD-10 sentence ("unless the AD-14 fallback is taken; then the route handler only forwards, logs no body or headers, and sets the client-address header"), or choose a fallback that keeps the proxy-only path. Log the choice.

### M3 — The `vercel.json` mechanism is named in a detail that is easy to get wrong and not verified

- **Location:** AD-12 Playtest (`routes` entry, `request.headers` `set` transform, `x-vercel-enable-rewrite-caching: 0`).
- **Problem:** `routes` is Vercel's legacy low-level routing key. It can't be combined with `rewrites`, `redirects`, `headers`, `cleanUrls` or `trailingSlash` in the same `vercel.json`, and a Next.js project normally does its routing in `next.config`. If the frontend team later adds `headers` or `rewrites`, the deploy fails, or they move the proxy into `next.config` rewrites, where the header transform isn't available. The spine also doesn't say who sends `x-vercel-enable-rewrite-caching` (a routes header or a response header from Caddy or the backend). The memlog notes that the docs disagree on visitor-IP forwarding. The currency of these keys was not re-checked by the 2026-11-13 currency lens.
- **Suggested fix:** Have the currency lens verify `routes` plus `transforms` and the rewrite-caching header against vercel.com/docs as of 2026-11-22. Add to AD-12 that the frontend's `vercel.json` uses no `rewrites`, `redirects` or `headers` keys alongside `routes`. State that the backend's `Cache-Control: no-store` is the binding control and the Vercel header is belt-and-braces.

### M4 — Deferred still defers what AD-12 now decides

- **Location:** Deferred row 1 ("Everything in the frontend: framework, …, the player information page (NFR-3) …; nothing in the backend depends on it").
- **Problem:** AD-12 now fixes the framework (Next.js on Vercel Hobby, functions in `fra1`), the `vercel.json` proxy, the reset-link page path and behaviour (`/nytt-passord#token=`, `history.replaceState`), and the player information page as a static frontend page. The local Caddy and `compose.yaml` now depend on a Next.js server service. A story writer reading Deferred will think these are open.
- **Suggested fix:** Reword the row: "Frontend internals (screens, client structure, TS types, fetching and idle timings FR-6/FR-8, fonts, accessibility CI); the framework, host, `/api` proxy, reset page and player information page are fixed in AD-12." Remove "nothing in the backend depends on it", or limit it to internals.

### M5 — Hours-offer slot preview and after-spending figure: no single source is named

- **Location:** AD-13 One view function; AD-1; FR-47 ("The offer shows what it would leave after spending each month and the next month's slot count"), FR-56 ("Each shows the next month's slot count").
- **Problem:** Hours offers, "ask for more or fewer" and one-off shifts each need a computed preview of next month's slots, pay after spending, and the free time below 50 warning. AD-1 says such figures are computed only in the engine, but nothing says the preview is one engine function shared by the view and the action check. A job-view story could compute the slot count in the view while the month-open step computes it differently. The 2026-11-13 gate's general rule covers it in spirit, but it is a new, repeated preview in three places (hours offer, extra shift, one-off shift).
- **Suggested fix:** In AD-13 (or AD-6), add: "Slot count and after-spending previews come from the same engine functions that the month-open step and the ledger use. The view never derives them."

---

## Low

### L1 — `ORIGIN_SECRET` sits outside the settings rule

- **Location:** AD-14 "All settings are pydantic-settings fields in `settings.py` … listed in `.env.example`"; AD-12 Caddy.
- **Problem:** `ORIGIN_SECRET` is read by Caddy and by Vercel, not by the backend, so it isn't covered by the "never a placeholder, at least 32 bytes" refusal. A placeholder could ship.
- **Fix:** State that `ORIGIN_SECRET` and `trusted_proxies` live in Caddy's env (listed in `.env.example` with a local-unused note). Have the Caddyfile refuse to start on Railway when the value is empty (`{$ORIGIN_SECRET}` with an error matcher), or check the length in the deploy check.

### L2 — Railway healthcheck vs the origin-secret refusal

- **Location:** AD-12 Caddy (403 without the secret), AD-14 (healthcheck only on the backend service).
- **Problem:** If anyone adds a Railway healthcheck to the Caddy service, it gets `403` and the deploy never goes healthy. It isn't stated that Caddy has none, or that it uses a path exempt from the secret.
- **Fix:** One clause in AD-14: "the Caddy service has no Railway healthcheck", or "Caddy answers `/caddy-health` without the secret and without proxying".

### L3 — Nickname placeholder isn't checked by the content check

- **Location:** AD-13 Game text; AD-7 content check.
- **Problem:** Authors write a nickname placeholder in texts. Nothing names its syntax or has the FR-58 schema gate reject unknown placeholders, so a typo shows raw braces to players.
- **Fix:** Name the placeholder token in AD-13 and add "unknown placeholders fail the schema gate" to AD-7.

### L4 — Email once (FR-1) needs no backend change. Say so

- **Location:** AD-2 ("auth form fields").
- **Problem:** None in substance. The FR-1 change is UI-only (confirm screen). A story writer might still look for a confirm-email field in the sign-up model.
- **Fix:** Optional half-sentence in AD-2: "sign-up takes the address once; the confirm step is frontend only (FR-1)".

### L5 — One-off shift and free time (FR-33)

- **Location:** AD-1 and the engine; FR-47 ("no wellbeing effect of its own: the slot it takes is its cost").
- **Problem:** It's unclear whether a one-off shift's hours reduce this month's free time under rule 12 and FR-33, which feeds wellbeing. The slot count is fixed at month open, so the slot cost is clear, but the free-time wellbeing figure is not. This is a PRD question, but engine stories will hit it.
- **Fix:** Add it to the H3 reconcile as a question for the PRD owner.

### L6 — SOLUTION-DESIGN.md dates

- **Location:** SOLUTION-DESIGN.md line 229 (reconciliations listed to 2026-11-15).
- **Problem:** After the H3 reconcile, the rendering will list an outdated history.
- **Fix:** Update it when H3 is done.

---

## Checklist summary

| Check | Result |
| --- | --- |
| Fixes the real divergence points for epics and stories | Mostly. Gaps on one-off shifts and hours offers (H1-H3, M5) |
| Every AD's rule enforceable and prevents its divergence | Yes, except AD-10 vs the AD-14 fallback (M2) |
| Nothing under Deferred lets two units diverge | No: "content schemas … addendum applies" doesn't cover the new kinds (H2); the frontend row is stale (M4) |
| Named tech verified-current | Backend stack checked on 2026-11-13. Vercel `routes`, transforms and caching header not independently verified (M3) |
| Covers the PRD's capabilities (today's changes) | Nickname: yes (AD-13, Accounts convention, AD-15). Email once: yes, UI only (L4). Vercel / NFR-11: yes (AD-12, AD-14, limits table). Hours offers, asking for more or fewer hours, employer answers: only implicitly (H3). One-off shifts in slots, pay and cap checks: contradicted by Rule Set v1 and not decided (H1, H2) |
| Operational envelope decided, deferred or open | Railway, Supabase, cost, logs, monitoring and ops: yes. Vercel environments and branches: no (M1). Caddy health and secret hygiene: minor (L1, L2) |
