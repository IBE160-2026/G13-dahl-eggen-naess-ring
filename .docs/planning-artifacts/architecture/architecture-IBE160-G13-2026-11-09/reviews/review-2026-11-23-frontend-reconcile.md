---
title: Frontend reconcile — AD-17 to AD-20 and the frontend rows against EXPERIENCE, DESIGN, the PRD, technology.md §4, the readiness review and #122
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (working copy on docs/epics-and-stories, uncommitted; frontend added 2026-11-23, #122)
inputs:
  - ../../../ux-designs/ux-IBE160-G13-2026-11-11/EXPERIENCE.md (IA 01-28, Component Patterns, State Patterns, Accessibility Floor, Responsive)
  - ../../../ux-designs/ux-IBE160-G13-2026-11-11/DESIGN.md (frontmatter tokens, Typography, Components)
  - ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (FR-6, FR-8, FR-16, FR-40, FR-43, FR-49, NFR-1, NFR-2, NFR-3, NFR-6, NFR-9, NFR-10; also FR-5, FR-11, FR-15, FR-31, FR-32b, FR-34, FR-44 where the frontend rows touch them)
  - ../../technology.md §4 (reference setup, adapted, not copied)
  - ../../../readiness-review-2026-11-23/report.md (Adversarial 8, 9, 20, 21)
  - GitHub issue #122 ("Lag en kort frontend-arkitektur (FE-AD) før frontend-epicene")
  - ../.memlog.md entries 107-114 (the frontend decisions as agreed)
lens: reconcile; what didn't land, what contradicts an input, and quiet requirements the new rules break. The spine was not edited.
---

# Frontend reconcile, 2026-11-23

**Verdict: revise before the frontend epics.** The #122 checklist landed in full: routing, data access and client state, the `request_id` retry client, OpenAPI type generation, test frameworks, the NFR-9 accessibility gate, the compose service, self-hosted fonts, lint/format and the PR review rule. The reference setup was adapted, not copied. The problem is in AD-17, which makes the game state decide the screen. As written, a gate replaces *every* area route. That contradicts FR-32b (money actions, open options and the plan stay available in a crisis month), EXPERIENCE's navigation (Hendelse, the card warning, crisis and the year end count as Hjem and keep their tabs) and the menu that FR-5 and FR-44 need. Because `gateFor(view)` is a pure function of the view, it also can't express FR-16's "after a login" recap, and it brings the year end back after every response in December. Four high findings sit in the client protocol (AD-18) and the gate model. Each can be fixed with one or two sentences.

| Tier | Count |
| --- | --- |
| Critical | 1 |
| High | 4 |
| Medium | 14 |
| Low | 13 |

## 1. What landed

| Input | Item | Where in the spine |
| --- | --- | --- |
| #122 / Adv 8 | Routing; hash routes dropped; `/nytt-passord` consistent | AD-17 |
| #122 / Adv 8 | Data fetching and client state; the retry and `request_id` client | AD-18 |
| #122 / Adv 8 | OpenAPI type generation with a staleness check | AD-18, Tests row |
| #122 / Adv 8 | Test frameworks; NFR-9 accessibility gate in CI | AD-20, Tests row |
| #122 / Adv 8 | Frontend compose service | AD-12 (local), Stack (`standalone`), seed `frontend/Dockerfile` |
| #122 / Adv 8 | Self-hosted fonts | AD-19, seed `fonts/` |
| #122 / Adv 20 | Lint/format on both sides; PR review rule | Lint and format row, Review row |
| FR-6 | 5 s «Prøver fortsatt», same `request_id`, never applied twice | AD-18 (+ AD-4, AD-13) |
| FR-8 / AD-10 | Fetch triggers incl. 5 min idle and tab return on the next input; no timers; offline locks, nothing queued | AD-18 |
| FR-49 | `month` on every request, `plan_version` on continue | AD-18 |
| NFR-2 | axe serious/critical fails CI; manual keyboard and screen-reader results in the repo | AD-20 |
| NFR-1 | 320/390/1280 px, no horizontal scroll | AD-20 |
| DESIGN | Tokens from the frontmatter, `--sc-*` scene colours, inline SVG with named groups, Bricolage + Kalam, light only, native `<dialog>` | AD-19 |
| technology.md §4 | Kept: Next.js 16, React 19, TS, npm, standalone Docker, Vitest, Playwright. Dropped with reasons in memlog 111-114: Tailwind, shadcn/Radix, TanStack Query, NEXT_PUBLIC flags, Node 22 | Stack, memlog |

Surfaces 01-08, 10-12, 14-19, 21, 22 (V2), 26 and 27 each map to a gate, an area route, a tile or inline content. Surfaces 09 (toast), 13 (result), 20 (card warning), 23 (year end), 24 (recap), 25 (ending) and 28 (offline) are covered only in part. See C1, H1, H2, M4, M5 and L1.

## 2. Findings

### Critical

**C1 — Gates replace every area route, which blocks the bank during a crisis and blocks the menu everywhere**
- **Location:** AD-17 Rule ("A gate renders in place of the area content whatever the URL").
- **Problem:** Under this rule, while a crisis step, an event, the card warning or the year end is pending, `/penger`, `/plan`, `/jobb`, `/mobil`, `/meny` and `/om-tallene` all show the gate. Three inputs say otherwise:
  - **FR-32b:** "money actions and open options stay available, use no crisis step", and "activities can be planned in a crisis month". Flow 6's edge case also relies on the bank during a crisis.
  - **EXPERIENCE IA and Navigation:** "Året, Hendelse, Resultat, the card warning, crisis and year end are reached from Hjem and count as Hjem in the navigation". Only log in, sign-up, the gift, the recap and the ending have no tabs or rail. So the tabs are visible during an event or a crisis, and AD-17 makes them dead.
  - **Timeline:** the menu is "reachable from every screen". Under AD-17 a player on the ending (FR-43 keeps it until a new life starts), on a setup step or in a crisis can't log out (FR-5), log out everywhere, delete the account (FR-44), end the life (FR-43) or open «Om tallene».

  The server already refuses `continue` while a real choice or crisis is unfinished (`cannot_continue`, AD-13), so the frontend doesn't need to fence the other areas.
- **Fix:** Split AD-17's gates into two kinds:
  - **Full-screen gates:** start or setup, recap, ending. They have no tabs. `/meny`, `/om-tallene` and `/personvern` stay reachable over them.
  - **Hjem gates:** event (including the card warning), crisis step, result, year end. They replace only the content of `/hjem` (and the desktop centre). Every other area route stays reachable, and the server's `cannot_continue` alone keeps the month from closing.

### High

**H1 — The recap trigger misses "after a login" and fires again after idle refetches**
- **Location:** AD-17 ("the recap (FR-16, from `server_time − last_action_at` against `recap_threshold`)"); AD-13 Identity and time.
- **Problem:**
  - FR-16 and EXPERIENCE 24 show the recap "after a login, **or** when the game is opened after at least an hour away". A login 10 minutes after playing on another device must show it (UJ-2), but the gap rule never does.
  - Because the gate is computed from every envelope, a player who reads the bank for over an hour without acting gets the recap on the next idle or tab-return fetch (AD-18). That is mid-session, not "when the game is opened".
- **Fix:** Pass a page-session flag into `gateFor` and state the rule in AD-17: show the recap once per page session, when that session began with a login or when the first envelope after page load has `server_time − last_action_at ≥ recap_threshold`. Never show it from an idle, tab-return or `online` refetch, and never when the view is `completed` (FR-16 → FR-43).

**H2 — `gateFor(view)` can't clear the year end (or the recap), so they come back after every response**
- **Location:** AD-17 ("maps the player view to the gate screen it requires"); EXPERIENCE 23 Year end ("Two buttons: continue, or «Ferdig for nå»"; "Nothing locks the player out", FR-15).
- **Problem:** No action dismisses the year end, and nothing in the view changes when the player taps «Fortsett» on it. So `gateFor` returns «year end» for every envelope in December, including the response to each plan placement or money action. The player is thrown back to the year end after every input. The recap has the same flaw until the first action changes `last_action_at`. Only the result has a stated page-session dismissal.
- **Fix:** State in AD-17 that the recap and the year end are dismissed in page-session UI state keyed by (`playthrough_id`, month), like the result. `gateFor(view, session)` reads that state, and a reload may show them once again. The alternative is a no-op "seen" action, but that would write per-month UI state into the game and is not recommended.

**H3 — "Every response replaces it whole" lets an older view overwrite a newer one**
- **Location:** AD-18 ("every response replaces it whole"); AD-13 ("the client always replaces its view with the latest response").
- **Problem:** AD-18 lets a `GET /api/game` (page load, `online`, idle) run alongside a `sendAction`, and it doesn't serialise actions. The same applies to quick plan taps on two evenings. The response that arrives last wins, even when it was sent first. The player can then see figures from before their own confirmed choice and act on them. FR-13 ("Tapping an option twice applies it only once") is safe on the server through `already_chosen`. In the client, though, the second tap's refusal replaces the store and can trigger the FR-8 "updated on another device" notice by mistake (see H4).
- **Fix:** Add to AD-18:
  - At most one `sendAction` is in flight. Every option stays locked (`aria-disabled`) until it settles, as EXPERIENCE's Saving state already requires.
  - The store ignores an envelope whose `playthrough_id` equals the held one and whose `state_version` is lower.
  - A `GET` sent before a pending action's response is discarded.

**H4 — FR-8's "before it accepts the next choice" and the "updated on another device" notice are undefined**
- **Location:** AD-18 fetch triggers and refusal handling; EXPERIENCE State "Updated on another device"; FR-8 consequence 2.
- **Problem:**
  - AD-18 fetches "on the player's next input after 5 minutes idle or a return to the tab", but doesn't say what happens to that input. If the client sends it after the `GET`, a stale screen's choice is applied whenever `month` and `plan_version` still match, for example a money transfer after another device changed the balance. FR-8 requires the fetch to come *before* the choice is accepted, so the player sees the new state first.
  - Nothing says when «Spillet ble oppdatert på en annen enhet.» is shown.
- **Fix:** Add to AD-18:
  - On such an input, `GET` first. If (`playthrough_id`, `state_version`) changed, drop the input, replace the view and show the notice. Otherwise send it.
  - Also show the notice on the turn refusals `wrong_month`, `plan_changed`, `game_changed` and `already_chosen`, unless the refusal answers this device's own earlier pending request.

### Medium

**M1 — No retry schedule or request timeout, and AD-10's list of allowed requests doesn't include retries**
- **Location:** AD-18 ("retries transport failures … with the same `request_id`"); AD-10 ("no request is made without a player input, a page load, a login or the connection coming back").
- **Problem:**
  - It isn't said when a retry runs: immediately, with backoff, or only on `online`.
  - A hung `fetch` (a dead mobile link while `navigator.onLine` stays true) never fails, so nothing retries. That breaks FR-6's "tries again when the connection is back".
  - A backoff retry while the player waits is a timed request that AD-10's list doesn't allow.
- **Fix:** In AD-18, give each request an abort timeout. Retry a pending action with bounded backoff while the page is open, and again on `online`. Add "a retry of the player's pending action" to AD-10's list.

**M2 — "`GET /api/game` is called only on …" contradicts AD-13 and AD-2, and leaves account changes stale**
- **Location:** AD-18 (the "only" list); AD-13 Errors (a `422 invalid_input` with `state: null` → "the client then fetches `GET /api/game`"); AD-2 ("after a lost response the client fetches `GET /api/game` or shows the login screen").
- **Problem:** The "only" list forbids the fetches AD-13 and AD-2 require. It also leaves out:
  - sign-up and a completed reset, which both log the device in (AD-10);
  - a nickname change, after which the view's `nickname` and every rendered sentence are stale (AD-13);
  - «Skjønner» on a disclosure, after which the view's seen ids are stale.

  AD-18 also doesn't say that a refusal with `state: null` must not blank the store.
- **Fix:** Extend AD-18's list:
  - after a game refusal with `state: null`;
  - after a lost account, session or disclosure response;
  - after sign-up, login and a completed reset;
  - after a nickname change.

  Also state that a disclosure's seen id is applied to the page state at once, and that a `null` state never replaces the store.

**M3 — FR-6's 5 s and FR-8's 5 min are "configuration", but the frontend has no configuration**
- **Location:** AD-18; Frontend code row ("No `NEXT_PUBLIC_*` variables"); Config row (operational limits in `settings.py`).
- **Problem:** FR-6 ("within 5 seconds (configuration)") and FR-8 ("idle (default 5 minutes, configuration)") name these as configuration, and the recap threshold already travels in the envelope from settings. The saving and idle times have no home, so they will be hard-coded literals in the client.
- **Fix:** Add `saving_notice_ms` and `idle_refetch_s` to backend settings and the game envelope next to `recap_threshold`. Or name one frontend constants module as their single configured source, and say so in the Config row.

**M4 — Page-session UI state has no home and can be wiped when the envelope is replaced**
- **Location:** AD-18 (one store, "every response replaces it whole"); AD-17 (the result held "only in the page session"); EXPERIENCE Message (#112: the opened dot clears "in the open page only"), Toast (09, closed with × and never by itself), Recap and Year end dismissal (H1, H2).
- **Problem:** Several pieces of state must live beside the envelope, survive its replacement and be cleared on reload or a new `playthrough_id`. These are: the result reference, dismissed gates, opened messages, the closed toast, the "this session began with a login" flag, and the pending action. None of them is named, so each screen will keep its own copy in a different way.
- **Fix:** Add one sentence to AD-18. The store holds a page-session part beside the envelope (result reference, dismissed recap and year end, opened message ids, toast closed, login flag, pending action). It is kept across envelope replacement, cleared when the `playthrough_id` changes, and never persisted.

**M5 — After a reload the result is lost, and the memlog's "results stay reachable" didn't land**
- **Location:** AD-17 ("after a reload the hub shows"); memlog 110 ("after a reload the hub shows *and the open month's results stay reachable*"); AD-13 Results; FR-6 consequence 4.
- **Problem:**
  - FR-6: "If the connection drops after the server saved a choice, the game shows that choice's result when it reconnects." AD-13 renders the open month's results in the view for exactly this case. A player who reloads during «Prøver fortsatt …» (the bus case in Flow 5) gets the hub and never sees the result. The spine doesn't say where the open month's results are shown.
  - AD-18 doesn't handle `result: null, replayed: true`.
- **Fix:** In AD-17, state where the open month's results are reachable after a reload: the hub's «Denne måneden» or a "last result" link. Also say that a `replayed` reply with `result: null` shows the hub without the result gate.

**M6 — Gate precedence is unspecified**
- **Location:** AD-17 (the list of gates).
- **Problem:** Several gates can be due at once:
  - a December that opens with an event and also has the year end;
  - a recap due when an event is pending (FR-16: "recap … then … the next choice");
  - a crisis month whose first screen shows the card warning's figures (FR-31);
  - a `completed` view after login (the ending must win over the recap, FR-16 → FR-43).

  Each screen builder would choose its own order.
- **Fix:** Fix one order in AD-17, for example: start/setup > ending > recap > crisis step > event (incl. card warning) > result > year end. Check the year-end position against EXPERIENCE 23 ("December opens").

**M7 — Gate changes aren't route changes, so focus, title and announcements won't follow them**
- **Location:** AD-17; EXPERIENCE Accessibility Floor (route change → focus to the screen's `h1`; «<screen> · LifeMode» on every route; one polite live region from page load).
- **Problem:** The result, the event after «Fortsett», the year end and the recap appear without a URL change. App Router's per-route `metadata` and any route-change focus hook won't fire, so focus stays on a removed control and the title is wrong. That is a WCAG 2.4.3/2.4.2 risk in exactly the screens the axe gate can't judge.
- **Fix:** Add to AD-17: a gate entering or leaving counts as a route change. The one layout that renders `gateFor` moves focus to the new `h1`, sets `document.title` and sends the screen change to the single live region that the root layout creates.

**M8 — «Spill på nytt» from a completed life has no start-screen content**
- **Location:** AD-17 ("the start screens when the view's `status` is `none` or `ended`"); AD-13 No playthrough; FR-43; FR-11 ("the playthrough starts when the player confirms a life goal"); EXPERIENCE Flow 7 («Spill på nytt» → 05).
- **Problem:** A `completed` view carries the ending from the pinned library. Only `none` and `ended` views carry the start screens' texts and the library version a start must echo (`409 game_changed` otherwise). From the ending, the client therefore can't render the life-goal screen or build a valid start request.
- **Fix:** In AD-13, also put the start screens' texts and start versions on a `completed` view. Or state that «Spill på nytt» first sends a play-again action that returns a `none`-shaped view. Then name that path in AD-17.

**M9 — The scene's text alternative, marker text and room-layer states aren't named as view content**
- **Location:** AD-19 (scene SVGs with named groups); AD-13 Game text; Readiness Adversarial 8 fix ("Add to AD-13 that room-state and echo-badge texts are content strings carried in the view"); FR-34 ("Each room state has a short text"); EXPERIENCE Scene and Room layers; NFR-2.
- **Problem:** The text alternative («Mopeden står utenfor vinduet, og hjelmen ligger på esken.»), the Kalam marker («Mobilen gikk i bakken», «Hel igjen») and the layer states are game text and game state. Under AD-13 they must come from the engine, but neither AD-13 nor AD-19 says the view carries them. The frontend will either hard-code Norwegian scene sentences, which breaks AD-13's "frontend owns only UI chrome", or have no text at all, which breaks NFR-2.
- **Fix:** In AD-13's view rule, state that the view carries each room layer's state id, the rendered scene text alternative and the marker text. In AD-19, state that layer groups are switched only from those state ids.

**M10 — The six avatar looks have no colours**
- **Location:** AD-19 ("`tokens.css` … the only file with colour values"; `--sc-*` from DESIGN); AD-7 (avatar looks for FR-10 in `lists.yaml`); DESIGN frontmatter (one `scene-hoodie` and one `scene-hoodie-shade`); EXPERIENCE 06 ("Six preset looks; the choice recolours the mirror figure").
- **Problem:** The view can only carry a look id from `lists.yaml`. DESIGN defines one hoodie colour, content may not hold colours, and `tokens.css` is generated from DESIGN alone. So there is nowhere to map six look ids to `--sc-hoodie` and `--sc-hoodie-shade` (and skin or hair, if a look changes them).
- **Fix:** Add the six looks as DESIGN tokens (for example `scene-look-<id>-hoodie`, `-shade`), keyed by the `lists.yaml` look ids. AD-19 then states that the avatar picker and the scene set `--sc-hoodie` from the view's look id.

**M11 — Amount inputs have no bounds or step in the view (Adversarial 9a/9b)**
- **Location:** AD-13 Derived figures → Other statuses and Quotes; EXPERIENCE Credit card (a stepper "in 100 kr steps from the minimum up to the balance"), Consumer loan; FR-22, FR-25, FR-45 money actions; NFR-7 range refusals.
- **Problem:** Several money actions take an amount: transfers, a BSU deposit up to the remaining cap, an extra card payment, early payoff and the loan amount. The frontend may not derive their minimums, maximums or steps (AD-13: "the frontend never derives one"), but the view doesn't carry them. The NOK 1,000 loan step is still only in AD-13, not in FR-25 (Adversarial 9b, open). Without bounds, every out-of-range input becomes a server round trip and a `422`, and the stepper has no limits.
- **Fix:** Add one line to AD-13's Other statuses: each amount action in the view carries its `min`, `max` and `step` as raw integers plus formatted strings. Either write the 1,000 step into FR-25 or carry it only as this view field.

**M12 — The reference setup's CSP was dropped, and nothing enforces NFR-3's "loads nothing from third parties"**
- **Location:** Stack; AD-19 (fonts); technology.md §4 "Sikkerhet: … CSP i `next.config.ts`"; NFR-3.
- **Problem:** AD-19 forbids third-party fonts, and NFR-3 forbids any third-party script, font, image or tracking. Only review enforces this. One stray `<link>` or a Vercel add-on (Analytics, Speed Insights, the preview toolbar) would break it unnoticed. The CSP was the cheap guard in the reference setup, and the adaptation dropped it without a recorded reason (memlog 114 lists what was not taken and doesn't mention CSP).
- **Fix:** Add a static `Content-Security-Policy` header (`default-src 'self'`, `connect-src 'self'`, `font-src 'self'`, `img-src 'self' data:`, script and style as Next.js needs) in `next.config.ts`, so it applies under Vercel and compose alike. Add one Playwright assertion that no request leaves the origin.

**M13 — The frontend's boundaries aren't checked in CI**
- **Location:** Design Paradigm ("Frontend imports go one way: `app` → `components` → `api`. Only `api` calls `fetch`"); AD-18; Lint and format row.
- **Problem:** On the backend, every boundary is enforced by import-linter or ruff (AD-1). The frontend's two boundary rules have no check, though AD-18's "Prevents" depends on them.
- **Fix:** Add ESLint rules to the Lint and format row: `no-restricted-globals`/`no-restricted-syntax` for `fetch` outside `src/api/`, `import/no-restricted-paths` (or eslint-plugin-boundaries) for the import direction and for `backend/`.

**M14 — NFR-10's frontend half has no owner**
- **Location:** Capability map row "Responsiveness (NFR-10) | backend, infra | AD-5, AD-14, performance convention"; EXPERIENCE State "Server waking".
- **Problem:** NFR-10 has three client-side targets: "first screen usable within 3 seconds", "a loading message within 1 second" and "usable within 10 seconds". All game screens are client components that wait for `GET /api/game`, and AD-12 forbids server-side prefetching. The loading state and the bundle size are therefore frontend decisions, but the map gives NFR-10 only to the backend.
- **Fix:** Add `frontend/src/app` and AD-17/AD-18 to the NFR-10 row. Add one sentence to AD-17: the layout renders a static loading state («Laster …») before the first envelope arrives, with no blocking fetch.

### Low

**L1 — Surfaces mapped only implicitly; AD-17's binds are incomplete**
- **Location:** AD-17 Binds and Rule.
- **Problem:**
  - The card warning (20, FR-31) is only implied by "the month's event".
  - The toast (09) and offline (28) are not mentioned in AD-17. Offline appears only in AD-18.
  - The binds leave out FR-15 (year end), FR-31, FR-40 (`/om-tallene`), FR-44 and FR-5 (`/meny`) and FR-54 (`/mobil`).
- **Fix:** In AD-17, add "the card warning is the month's event" and "the toast and the offline bar are page states, not routes". Add FR-5, FR-15, FR-31, FR-40, FR-44 and FR-54 to the binds.

**L2 — `/meny` as a route contradicts EXPERIENCE, and EXPERIENCE still points at hash routes**
- **Location:** AD-17 (`/meny`); EXPERIENCE Navigation ("Sheets (interest, add an activity below 1100 px, menu) stack one level deep"); EXPERIENCE Foundation ("UI system: none is named … architecture AD-12/AD-13"); IA column "Route (round 3)".
- **Problem:** Making the menu a route is the better call, because its nickname and password sheets then stay one level deep. But it differs from EXPERIENCE, and EXPERIENCE doesn't yet point to AD-17 to AD-19.
- **Fix:** Note in AD-17 that the menu is a route so that its sheets stay one level deep. Ask the UX owner to update EXPERIENCE's Navigation and Foundation lines and to mark the hash-route column as mockup-only.

**L3 — The token naming rule is incomplete**
- **Location:** AD-19 ("under the token's own name (`--color-money-in`, `--radius-lg`, `--space-4`; scene colours as `--sc-*`)").
- **Problem:**
  - DESIGN's groups are `colors`, `rounded`, `spacing`, `typography` and `components`, so the mapping isn't literally "own name". `rounded` becomes `radius`, and the rule for typography composites and `components` references isn't given.
  - The `scene-*` colours sit inside `colors`, so they could be emitted both as `--color-scene-wall` and as `--sc-wall`. That gives two names for one token, which AD-19 itself forbids.
  - DESIGN's shadows (28 % ink) and the 50 % scrim need alpha colours, which stylelint's hex/`rgb()` ban blocks.
- **Fix:** Give the generator's prefix rule per group, emit `scene-*` only as `--sc-*`, and either add shadow and scrim tokens or allow `color-mix()` on token variables.

**L4 — `next/font/local` versus the font family in the tokens**
- **Location:** AD-19.
- **Problem:** `next/font/local` assigns a generated family name. A token that reads `font-family: Bricolage Grotesque`, taken from DESIGN's typography, won't match the self-hosted file unless the font is exposed through a CSS variable.
- **Fix:** Load both fonts with `variable: '--font-bricolage'` and `'--font-kalam'` on `<html>`, and have the generator emit the typography tokens as `var(--font-…)`.

**L5 — The colour rule doesn't reach SVG**
- **Location:** AD-19 (stylelint refuses hex elsewhere; "the scenes are inline SVG … with `--sc-*` colours").
- **Problem:** Inline SVG lives in TSX, so stylelint never sees a `fill="#C7D5C0"` ported from the mockups.
- **Fix:** Add an ESLint rule or a CI grep that fails on hex or `rgb()` literals in `.tsx` and `.svg` files under `src/`.

**L6 — Gaps in AD-20's test scope**
- **Location:** AD-20.
- **Problem:**
  - The widths 320/390/1280 skip the 768-1099 rail layout.
  - No browser engine is named, though NFR-1's main device is Safari on iPhone.
  - "Written to a file in the repo" has no path.
  - jsdom's `<dialog>` support is partial, so focus moves around sheets belong in Playwright, not Vitest.
  - Specs that continue a seeded user's game change shared state and must not run in parallel.
- **Fix:** Add a 900 px width and a WebKit project. Name the manual results path (for example `docs/tests/manual/`). Move sheet focus checks to Playwright. State that specs which change a seeded user's game run serially or start from a fresh seed.

**L7 — The generated files and their sources aren't pinned**
- **Location:** AD-18 and AD-19 staleness checks; Structural Seed `frontend/scripts/`.
- **Problem:** The spine doesn't say whether the generated API types and `tokens.css` are committed. Vercel and the compose image build from `frontend/` and can't see `openapi.json` or `DESIGN.md` outside it. The generator's input is a dated planning folder (`.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/DESIGN.md`), which moves when the UX folder is renewed.
- **Fix:** State that both generated files are committed and never regenerated in Vercel or Docker builds. Name the `DESIGN.md` path that the script reads.

**L8 — The playtest copy for «Glemt passord» can't vary (Adversarial 9d)**
- **Location:** Frontend code row ("No `NEXT_PUBLIC_*` variables"); NFR-11 (no email in the playtest); EXPERIENCE 04.
- **Problem:** In the playtest, surface 04 needs "Ta kontakt med teamet for ny lenke". The spine gives the frontend no environment signal.
- **Fix:** Let a server component read one non-secret build variable (not `NEXT_PUBLIC_*`), or let the backend expose an `email_enabled` flag, and name the choice in the Frontend code row.

**L9 — The player information page still has three sources (Adversarial 21)**
- **Location:** AD-12 Player information ("names the processors and the log notes in AD-14"); Deferred row 1.
- **Problem:** The fix to make NFR-3 the single list of required contents (including a contact point and the audience) and point AD-12 at it didn't land. The frontend now owns the page.
- **Fix:** Change AD-12's sentence to "its contents are NFR-3's list; processors and log notes as AD-14".

**L10 — `GET /api/game/quote` isn't placed in the client**
- **Location:** AD-18; AD-13 Quotes.
- **Problem:** The quote response is `{quote, server_time}` with no `state`. AD-18's single store ("every response replaces it whole") doesn't say that this call bypasses the store, or whether it is debounced per input.
- **Fix:** Add to AD-18: quotes are plain typed reads made on the player's input, debounced, kept in the loan sheet's own state, and never written to the envelope store.

**L11 — Leftover "backend" labels and unowned CI jobs**
- **Location:** Frontmatter `name` and the H1 title ("LifeMode MVP backend"); Capability map row "Saving and devices (FR-6 to FR-8, FR-16) | persistence, api | AD-4, AD-5, AD-13"; `ci.yml` (Adversarial 8: "Give `ci.yml` jobs a named owner per side").
- **Problem:** The spine now covers the frontend, but its name and the FR-6/FR-8/FR-16 row don't. No CI job has an owner.
- **Fix:** Rename the spine to "LifeMode MVP". Add `frontend/src/api`, `frontend/src/app`, AD-17 and AD-18 to the Saving and devices row. Name an owner per CI job group in the Tests row.

**L12 — The Review convention isn't set up yet**
- **Location:** Review row ("Branch protection on `main` …").
- **Problem:** The repo is public, so branch protection is available. `gh api …/branches/main/protection` answered 404 (not set, or not visible to this account), and `rulesets` is empty. The rule depends on an admin doing it.
- **Fix:** Name who enables the `main` ruleset (required CI checks, one approval, no self-merge) and when, for example before the first story PR.

**L13 — DESIGN.md calls itself both draft and final**
- **Location:** DESIGN.md frontmatter `status: final` versus the body ("**Draft, 2026-11-23.** … The spine stays a draft until it is finalized"; Colors "No dark mode in this draft").
- **Problem:** AD-19 makes DESIGN the generator's source of truth, and the spine's preamble calls the UX final.
- **Fix:** Ask the UX owner to update DESIGN's body note to final, so `tokens.css` isn't generated from a file that calls itself a draft.

## 3. Quiet requirements checked and found consistent

- AD-18's "no timers, no fetch on focus" with AD-10's 30-minute idle limit and FR-5. The fetch triggers match FR-8's list (opened, reloaded, login, tab return, connection back, 5 min idle), as long as M1 and M2 are fixed.
- AD-18's transport-failure classes match AD-13's Errors exactly (`unavailable`, `internal_error` at most once, no JSON `code`). Account, session and disclosure calls are never retried automatically (AD-2).
- AD-2's "continue anyway is client-side only" matches EXPERIENCE's confirm sheet (FR-49).
- AD-19's "no component library, native `<dialog>`" matches EXPERIENCE's Sheet pattern, and "light mode only" matches both UX files.
- AD-20 covers NFR-2's two verification parts (automated, with serious or critical findings failing; manual keyboard and phone screen reader before each playtest) and NFR-9's CI requirement. The manual NFR-1 device check is a Deferred row.
- The Review row satisfies Adversarial 20 (an approval from another member, written review, also for AI code). The Lint and format row covers ruff check and format, ESLint, Prettier, stylelint and `tsc`.
- With AD-12, AD-17 keeps `/nytt-passord` (token in the fragment) and `/personvern` outside the game. The hash-route clash in Adversarial 8 is gone.
