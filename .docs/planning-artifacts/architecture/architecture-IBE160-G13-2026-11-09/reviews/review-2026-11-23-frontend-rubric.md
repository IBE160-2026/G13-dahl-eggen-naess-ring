---
title: Rubric review — frontend update to the architecture spine
date: 2026-11-23
reviewer: rubric walker (subagent)
target: ARCHITECTURE-SPINE.md (working tree, uncommitted frontend update for #122)
scope: AD-17 to AD-20, frontend Design Paradigm rows, conventions 'Frontend code', 'Lint and format', 'Review', the Tests extension, frontend Stack rows, frontend Structural Seed, three Capability rows, two Deferred rows, frontmatter scope/binds, AD-12 edits; seams with AD-2, AD-4, AD-10, AD-12, AD-13, AD-14
sources_checked: PRD FR-6, FR-8, FR-15, FR-16, FR-31, NFR-1 to NFR-3, NFR-7, NFR-10; EXPERIENCE.md (IA, State Patterns, Accessibility Floor, Responsive); DESIGN.md frontmatter; .memlog.md last 8 entries; web checks 2026-11-23
---

# Rubric review — frontend update (2026-11-23)

## Verdict

**Pass with fixes. 0 critical, 4 high, 11 medium, 13 low.**

The frontend part makes the right big calls: the game state picks gate screens (AD-17), one client owns the protocol (AD-18), tokens have one source (AD-19), and e2e runs against the real stack (AD-20). Together they close the main ways separately built screens could drift. Four gaps would still let two implementers build incompatible behaviour, or put a rule in conflict with an existing AD:

- gates the client dismisses (recap, year end) can't be worked out from `gateFor(view)` alone;
- AD-18's closed list of fetch triggers contradicts AD-13 and AD-2;
- the transport retry has no trigger AD-10 allows;
- the local frontend dev loop isn't decided.

Several rules state an intent that nothing enforces (frontend layering, the colour rule in TSX and SVG, no third-party loads). Three named Stack versions are out of date.

## Dimension coverage

| Dimension the frontend owns | Status in spine | Note |
| --- | --- | --- |
| Routing | Decided (AD-17) | Dismissal of client-held gates and redirect rules missing (H1, L4) |
| Data access | Decided (AD-18) | Trigger list contradicts AD-13/AD-2 (H2); retry trigger (H3); ordering (M6); quote calls (L10) |
| State | Decided (AD-18 store) | Page-session gate state not placed (H1) |
| Styling | Decided (AD-19) | Naming mapping (M3), enforcement gap (M2) |
| Accessibility | Decided (AD-20 gate + EXPERIENCE floor) | Shared live region/locked control ownership (M8) |
| Testing | Decided (AD-20, Tests row) | Test isolation (M7), fixture realism (L12) |
| Build and deploy | Mostly decided (Stack, Seed, AD-12) | Contract skew between Vercel and Railway deploys (M10); Vercel settings (L9) |
| Environments | Partly decided | Local dev loop missing (H4); client timing config (M4) |
| Lint | Decided (Lint and format row) | No boundary rule (M1) |
| Review | Decided (Review row) | `playtest` branch unprotected (L7) |
| Error and offline handling | Decided for the game client (AD-18) | Render errors / not-found (L6); offline exit (H3) |
| i18n / text ownership | Decided for game text (AD-13) | Form error text and client validation (M5); Norwegian-only not stated (L13) |
| Security headers / third parties | Not decided | NFR-3 "nothing from third parties" unenforced (M11) |

## Contradictions with existing ADs

- **AD-18 vs AD-13 and AD-2:** see H2.
- **AD-18 vs AD-10:** see H3.
- **AD-19 vs DESIGN.md token names:** see M3.
- **The Config convention vs FR-6/FR-8 client timings:** see M4.
- **AD-12 wording:** it uses "middleware", which Next.js 16 renamed (L3).

No contradiction found with AD-4's protocol fields or AD-14's environment rules, apart from the deploy skew in M10.

---

## Critical

None.

## High

### H1 — Client-held gates can't be worked out from `gateFor(view)`; recap and year end would never close, or each screen would close them its own way

- **Location:** AD-17 Rule (`gateFor(view)`, the recap and year-end gates); Design Paradigm row "Frontend: routes".
- **Problem:** `gateFor` takes only the view. Two gates are dismissed without a request:
  - **Recap.** Its condition (`server_time − last_action_at ≥ recap_threshold`) stays true until the next game action. FR-16 also shows the recap "after a login" whatever the gap, which the view can't express.
  - **Year end.** It opens with December (FR-15, EXPERIENCE 23). The player then keeps playing month 12, so the gate can't stay up for the whole month.

  As written, `gateFor` either blocks forever or each implementer adds their own "seen" flag (localStorage, store field, URL). Only the event/crisis result gate is given page-session semantics.
- **Fix:** Make it `gateFor(view, pageSession)`, where `pageSession` is one object in the game store that holds the acknowledged client-held gates keyed by `(playthrough_id, month, kind)` and a "logged in during this page session" flag. For each gate, list the view field that raises it and how it is dismissed: by an action (setup, event, crisis, ending) or by a page-session acknowledgement (result, recap, year end).

### H2 — AD-18's closed list of `GET /api/game` triggers contradicts AD-13 and AD-2, and a refusal can set the store to null

- **Location:** AD-18 Rule ("`GET /api/game` is called only on page load, after login, on the browser's `online` event, and on the player's next input …"; "every other code as a refusal whose `state` replaces the store").
- **Problem:** The list says "only", so it shuts out three fetches other ADs require:
  - AD-13: after `422 invalid_input` (which has `state: null`), the client fetches `GET /api/game`.
  - AD-2: after a lost response to an account or session request, the client fetches `GET /api/game` or shows login.
  - A nickname change changes the view's `nickname` and every rendered text, but no listed trigger refreshes it.

  Refusals with `state: null` (any non-pipeline refusal) would also replace the store with null.
- **Fix:** Add these triggers to AD-18's list:
  - a refusal whose `state` is null, which triggers a fetch and never clears the store;
  - a lost response to an account or session request (AD-2);
  - a successful nickname change, or let that endpoint return the envelope.

  Then say that a refusal replaces the store only when `state` is non-null.

### H3 — No trigger is given for the transport retry; a timed retry would break AD-10's no-timer rule, and offline mode has no way out after a 503

- **Location:** AD-18 Rule ("retries transport failures … with the same `request_id`"; "While offline (`navigator.onLine` false or a transport failure)"); AD-10 Sessions ("The client never calls the API from a timer … no request is made without a player input, a page load, a login or the connection coming back").
- **Problem:** AD-18 doesn't say when a retry fires. `unavailable` (Caddy 503) and `internal_error` happen while the browser is online, so no `online` event ever comes. The only ways to retry are a timer, which AD-10 forbids, or waiting for an input nobody has defined. The same goes for leaving the "offline because of a transport failure" state: nothing clears it while `navigator.onLine` stays true. One implementer will add backoff timers and another will wait forever.
- **Fix:** Say that a pending action is retried on the `online` event and on the player's next input (a «Prøv igjen» control in the «Prøver fortsatt …» state). If timed retries are wanted, allow at most N for the one in-flight action and write this into AD-10 as a named exception. Also say that a successful response clears the offline state.

### H4 — The local frontend dev loop isn't decided, which invites `next.config` rewrites that also run on Vercel

- **Location:** AD-12 "Local and the examiner run"; Stack row Next.js (`output: 'standalone'` for the compose image); Structural Seed `frontend/Dockerfile`; Frontend code row ("it calls only relative `/api` paths").
- **Problem:** Compose runs the frontend as a production standalone build behind Caddy, so there is no hot reload. A developer running `next dev` on :3000 sends relative `/api` calls to the Next dev server, which returns 404. Each developer will then solve this their own way: a `rewrites` entry in `next.config` (which Vercel also runs, giving a second `/api` proxy path around AD-12's `vercel.json` route and origin secret), an absolute backend URL, or a private Caddyfile. That is exactly the kind of divergence AD-12 is meant to stop.
- **Fix:** Add one sentence to AD-12: locally, Caddy's frontend upstream comes from an environment variable that defaults to the compose service and can point at a host `next dev` (websocket passthrough for HMR). Also say that `next.config` defines no `rewrites`, `redirects` or `headers` for `/api`.

## Medium

### M1 — The frontend's layering and its fetch rule have no check

- **Location:** Design Paradigm ("Frontend imports go one way: `app` → `components` → `api`. Only `api` calls `fetch` …"); AD-18 first sentence; Lint and format row.
- **Problem:** The backend's equivalent rule (AD-1) is enforced by import-linter in CI. The frontend rule is prose only, so agents building screens will call `fetch` or import across layers unnoticed. "One way" also leaves open whether `app` may import `api` directly, which `gateFor` reading the store requires.
- **Fix:** Add to the Lint and format row: ESLint `no-restricted-globals`/`no-restricted-syntax` bans `fetch` outside `src/api/`, and `import/no-restricted-paths` (or `eslint-plugin-boundaries`) zones enforce `app` → {`components`, `api`}, `components` → `api`, `api` → nothing, and no imports from `backend/`.

### M2 — "Only file with colour values" isn't enforced for TSX or inline SVG, and the stylelint ban list is incomplete

- **Location:** AD-19 Rule ("It is the only file with colour values; stylelint refuses hex, `rgb()` and named colours elsewhere"; "The scenes are inline SVG … with `--sc-*` colours").
- **Problem:** Stylelint sees only `.css`. Scene SVGs in TSX (`fill="#C7D5C0"`) and `style={{color: …}}` props get past it. `hsl()`, `hwb()`, `oklch()`, `lab()` and `color()` aren't banned either.
- **Fix:** Say that stylelint bans every colour function and named colour outside `tokens.css`. Add an ESLint rule (or a CI grep) that fails on colour literals in `.tsx`/`.svg` under `src/`, so SVG fills use `var(--sc-*)`.

### M3 — The token naming rule contradicts its own examples and DESIGN.md, and the generator's input path isn't named

- **Location:** AD-19 Rule ("every `DESIGN.md` frontmatter token as a CSS variable under the token's own name (`--color-money-in`, `--radius-lg`, `--space-4`; scene colours as `--sc-*`)"); Structural Seed `scripts/`.
- **Problems:**
  - DESIGN.md's groups are `colors`, `rounded`, `spacing`, `typography` and `components`. `--radius-lg` and `--color-…` are therefore renamings, not "own names".
  - Composite tokens (typography objects, `components.*` maps with references) have no single CSS value.
  - The script reads a planning document at an unnamed path, so a new UX version folder silently stops the staleness check from meaning anything.
- **Fix:** State the mapping:
  - `colors.x` → `--color-x`, except `scene-*` → `--sc-*`;
  - `rounded.x` → `--radius-x`; `spacing.x` → `--space-x`;
  - each typography token → `--font-<name>-{family,size,weight,line-height,letter-spacing}`;
  - `components` are not emitted.

  Also name the DESIGN.md path the generator reads.

### M4 — FR-6's 5 s and FR-8's 5 min are "configuration", but the frontend can't read configuration

- **Location:** AD-18 ("after 5 s", "after 5 minutes idle"); the Config convention ("idle times … the recap threshold … in `backend/app/settings.py`"); Frontend code row ("No `NEXT_PUBLIC_*` variables"); AD-13 envelope (`recap_threshold` only).
- **Problem:** The Config convention puts idle times in backend settings. The frontend has no environment variables, and the envelope carries only `recap_threshold`. Hard-coding the values in AD-18 contradicts the convention, and different screens will hard-code them separately.
- **Fix:** Either add `still_trying_after_ms` and `idle_refetch_after_s` to the envelope next to `recap_threshold` (from settings), or name one frontend constants module as their only home and say in the Config convention that these two are frontend constants.

### M5 — Ownership of form error text and client-side validation isn't decided

- **Location:** AD-13 Game text ("The frontend owns only UI chrome text (buttons, labels, offline and saving notices)"); AD-13 Errors (`fields: [{field, code}]`, `message`); EXPERIENCE State Patterns (per-field texts such as «Passordet må ha minst 8 tegn.»).
- **Problems:**
  - One envelope `message` can't carry several field errors. EXPERIENCE writes per-field and login texts, but the spine doesn't say whether the frontend maps `fields[].code` and `login_failed` to its own text or shows the backend's `message`.
  - Nothing says whether the frontend pre-validates forms. If it does, it copies FR-1 limits that live in backend settings (nickname 2-16), so they can drift.
- **Fix:** Extend AD-13's frontend-owned text to "per-field error texts keyed by `fields[].code` and the auth codes, worded as in EXPERIENCE". Also say whether the frontend pre-validates: either "only `required` and `type=email`, limits checked by the server" or "limits from the view".

### M6 — No rule for actions in flight or for out-of-order responses

- **Location:** AD-18 ("every response replaces it whole"); AD-13 Identity ("the client always replaces its view with the latest response").
- **Problem:** Nothing says that only one `sendAction` may be in flight. A double tap on two different options sends two requests, and the server takes one. "Latest response" can mean the last one to arrive or the last one sent. A `GET /api/game` started by an `online` event can arrive after the action's response and roll the store back to an older state. A later continue then sends a stale `plan_version` and gets a `409`.
- **Fix:** Say that the game store allows one request in flight. Options stay locked until it settles, and a `GET` triggered meanwhile is deferred until it settles. A response is applied only if no request sent after it has already been applied.

### M7 — Playwright specs share mutable seeded users

- **Location:** AD-20 ("logged in as the NFR-6 seeded users"); Tests row.
- **Problem:** Specs that continue, take a card, end in a crisis or reach the ending change the seeded users' state. Parallel workers or reruns against the same compose database then collide or depend on order. Each spec author will pick their own workaround.
- **Fix:** Say that each spec owns a named seeded user (or creates its own through sign-up), that the e2e job starts from a freshly seeded database (`cli seed` on an empty DB), and that specs touching the same user don't run in parallel.

### M8 — The Deferred "component structure" row leaves shared primitives open to being built twice

- **Location:** Deferred row "Component structure inside each screen …".
- **Problem:** Screens are built by different people, but the cross-screen primitives aren't owned by anyone:
  - native `<dialog>` sheets (one level deep, never stacked);
  - the locked control (`aria-disabled` plus `aria-describedby`);
  - the one polite live region and its announce function (EXPERIENCE: "one polite region exists from page load");
  - the toast, money chip, wellbeing tile and the saving/still-trying option state.

  Deferring them means two story owners can build two sheets or two live regions, which breaks EXPERIENCE's accessibility floor.
- **Fix:** Add a convention: shared primitives live in `components/ui/` (listed above, including one `announce()` for the single live region) and are built in the first frontend story, before any screen story. Narrow the Deferred row to "layout inside each screen".

### M9 — Three Stack versions are stale against the 2026-11-23 web

- **Location:** Stack rows Next.js + React, TypeScript, Vitest; memlog (version) entry.
- **Problems:**
  - **Next.js 16.4** was released (blog, 2026-10-06; unpkg serves 16.4.3), with React 19.3 features and a mid-October critical fix for `use cache` RCE. "16.3 latest feature release" is wrong.
  - **Vitest 5** was released 2026-09-03 (`clearMocks` true by default; config not looked up from parent directories). "Vitest 4.x" is the old major, and the memlog marked 5.1.0 as unconfirmed.
  - **TypeScript 6.0** has been stable since 2026-03-23, and TypeScript 7 exists. Next.js docs say a TS 7 install needs `experimental.useTypeScriptCli`, otherwise `next build` exits. "TypeScript 5.x" is stale and leaves the 7.x trap open.
- **Fix:** Change the rows to:
  - "Next.js 16.x (16.4 latest feature release, newest security patch at first build), React 19.x";
  - "Vitest 5.x";
  - "TypeScript 6.x, `strict`; not 7 until Next's default checker supports it".

  Re-check openapi-fetch, since only 0.17.0 could be seen.

### M10 — Frontend and backend deploy separately during the playtest, with no contract rule

- **Location:** AD-14 "Deploys during the playtest" (backend only); Stack row Vercel (production branch `playtest`); AD-13 Contract.
- **Problem:** A push to `playtest` deploys Vercel and Railway independently. Open tabs also keep the old bundle. A new action member or a renamed field breaks requests while the two sides run different versions. AD-14 makes only migrations and `state_schema` steps additive.
- **Fix:** Add to AD-14: during the playtest, `openapi.json` changes only add (new optional fields, new action members, new codes); the backend deploys before the frontend; and the frontend treats unknown codes and unknown `status` values as refusals or a reload notice.

### M11 — Nothing enforces NFR-3's "nothing from third parties, no analytics" on the frontend

- **Location:** AD-19 (fonts only); Frontend code row; NFR-3.
- **Problem:** Only fonts are covered. Nothing stops someone enabling Vercel Analytics or Speed Insights, adding a third-party script or image, or pulling a library that phones home. There is no CSP.
- **Fix:** Add to the Frontend code row: "a `Content-Security-Policy` with `default-src 'self'` is sent on every page (vercel.json headers in the playtest, Caddy locally); Vercel Analytics and Speed Insights stay off; the Playwright run fails on any request to another origin."

## Low

### L1 — The spine's name still says backend

- **Location:** Frontmatter `name: 'LifeMode MVP backend'`; H1 "Architecture Spine — LifeMode MVP backend".
- **Problem:** The scope now covers the frontend, so the name is out of date.
- **Fix:** Rename both to "LifeMode MVP".

### L2 — History and rationale wording has crept into the new text

- **Location:**
  - Frontmatter scope "(added 2026-11-23, #122: the group is now the frontend team)";
  - AD-12 "(chosen 2026-11-22; …)";
  - Stack "(supports Node 22, 24, 26)", "7.x and 0.17.x seen", "(maintenance until 2028-04)";
  - Review row "also for AI-generated code" (fine) next to "nobody merges their own PR unreviewed" (repeats the approval rule).
- **Problem:** These are history and rationale, which belong in the memlog, not the spine.
- **Fix:** Move the history and the support notes to the memlog and drop the repeated review clause.

### L3 — AD-12 uses the old name "middleware"

- **Location:** AD-12 Playtest ("server components, middleware, route handlers").
- **Problem:** Next.js 16 renamed `middleware.ts` to `proxy.ts`. The spine's wording invites the deprecated file.
- **Fix:** Write "server components, `proxy.ts` (formerly middleware), route handlers".

### L4 — Routing edge cases are open

- **Location:** AD-17.
- **Problems:**
  - EXPERIENCE treats the menu as a sheet, but AD-17 makes `/meny` a route.
  - The desktop pane mechanism isn't named (parallel routes or a layout that switches on a media query).
  - Nothing says what a logged-in player sees at `/`, `/logg-inn` or `/ny-bruker`, or where the player returns after a `401` and login.
- **Fix:** Add one sentence: `/meny` renders as a sheet over Hjem; the pane is one game layout that switches on the 1100 px media query, with no parallel routes; logged-in visits to logged-out routes go to `/hjem`; after login the player returns to the route that got the `401`.

### L5 — Capability map gaps

- **Location:** Capability map.
- **Problems:**
  - Responsiveness (NFR-10) lists only backend and infra, but "first screen usable in 3 s" and "loading message within 1 s" are frontend.
  - Automated tests (NFR-9) doesn't list AD-20.
  - Privacy (NFR-3) doesn't list AD-19, the Frontend code row or AD-12 `/personvern`.
  - "UX surfaces 01-28" includes the V2 surface 22.
- **Fix:** Add the frontend and AD-20 to those rows and write "UX surfaces 01-28 except 22".

### L6 — Render errors and not-found aren't decided

- **Location:** Frontend code row.
- **Problem:** A render crash or an unknown URL shows Next's default English page, which breaks the Norwegian tone (NFR-8) and offers no way back.
- **Fix:** Add: "`app/error.tsx`, `global-error.tsx` and `not-found.tsx` show Norwegian chrome text with a link to `/hjem`; render errors are never sent to a third party."

### L7 — The deploy branch is unprotected

- **Location:** Review row.
- **Problem:** Only `main` is protected, but the playtest deploys from `playtest`, so a direct push skips review and CI. "Written as comments" can't be enforced.
- **Fix:** Protect `playtest` as well (merges from `main` only), and keep "comments in the PR" as a team rule.

### L8 — The AD-20 artefacts aren't named

- **Location:** AD-20 and the Deferred "Device matrix" row.
- **Problems:**
  - The manual-results file has no path.
  - The axe "main screens" aren't listed.
  - The Deferred row says NFR-10 measurements are "written to the repo (AD-20)", but AD-20 mentions only NFR-1 and NFR-2.
- **Fix:** Name the file (for example `frontend/e2e/manual-checks.md`), list the screens axe covers (or "every route in AD-17 plus each gate"), and add NFR-10 to the file's contents.

### L9 — Vercel project settings aren't fixed

- **Location:** Stack row Vercel; AD-12.
- **Problems:**
  - Root Directory `frontend` isn't stated.
  - The Node version source isn't stated.
  - Preview deployments are public. They get `403` through the proxy because `ORIGIN_SECRET` is set for Production only, and that isn't said to be intended.
- **Fix:** Add "Root Directory `frontend`, Node from `engines.node: 24.x`, preview deployments off (or accepted as `/api`-less)".

### L10 — The quote endpoint isn't placed in AD-18

- **Location:** AD-18; AD-13 Quotes.
- **Problem:** `GET /api/game/quote` is neither the game store nor an account call. AD-18 doesn't say whether it is retried, cached, or debounced while the player types an amount. A debounce is a timer, which AD-10 forbids.
- **Fix:** Add: "quotes are plain typed calls made when the player confirms an amount (not while typing), never retried, and kept out of the game store."

### L11 — Who regenerates the TS types isn't stated

- **Location:** AD-18 staleness check; AD-13 contract check.
- **Problem:** A backend PR that changes `openapi.json` fails the frontend staleness check unless someone regenerates the types. Nobody is named for it.
- **Fix:** Add "the PR that changes `openapi.json` regenerates the frontend types in the same PR (one npm script)."

### L12 — Typed fixtures can still be impossible states

- **Location:** AD-20 ("fixtures are player views typed by the generated API types").
- **Problem:** The memlog's "never hand-shaped" was dropped. A type-correct fixture can still describe a state the engine never produces, for example a gate combination that can't happen.
- **Fix:** Say that component fixtures are player views dumped from the seed states by one backend test or CLI command and committed, with hand edits limited to a named list.

### L13 — Norwegian-only and the source of chrome words aren't stated

- **Location:** Frontend code row.
- **Problem:** `lang="nb"` is set, but nothing says there is no i18n library, or that chrome text follows EXPERIENCE's "Words the player sees" table. One developer may add `next-intl` while another inlines strings.
- **Fix:** Add "Norwegian bokmål only, no i18n library; chrome strings use EXPERIENCE's word table."

---

## Bloat and rationale check

The new ADs are mostly decision-only and compact. The rationale-shaped wording is listed in L2. AD-18 and AD-19 each carry one parenthetical that belongs to EXPERIENCE or DESIGN ("(EXPERIENCE)", "(DESIGN)"); these are fine as references. Nothing calls for moving whole paragraphs out of the spine.

## Web sources (2026-11-23)

- [Next.js 16.4 blog](https://nextjs.org/blog/next-16-4); [AlternativeTo news on 16.4](https://alternativeto.net/news/2026/10/next-js-16-4-boosts-performance-with-turbopack-optimizations-and-react-19-3-integration/); [unpkg next@16.4.3 upgrade doc](https://unpkg.com/next@16.4.3/dist/docs/01-app/02-guides/upgrading/version-16.md)
- [Next.js middleware-to-proxy](https://nextjs.org/docs/messages/middleware-to-proxy); [Next.js TypeScript config](https://nextjs.org/docs/app/api-reference/config/typescript)
- [Vitest 5 blog](https://main.vitest.dev/blog); [OpenReplay: Vitest 5 changes](https://blog.openreplay.com/vitest-5-changes/)
- [Announcing TypeScript 6.0](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)
- [openapi-fetch 0.17.0 package.json](https://cdn.jsdelivr.net/npm/openapi-fetch@0.17.0/package.json)
