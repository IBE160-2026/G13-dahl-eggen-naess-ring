---
title: 'Adversarial review: frontend pairs that still collide (AD-17 to AD-20)'
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (status final, updated 2026-11-23, with AD-17 to AD-20 and the Frontend code, Lint and format and Review conventions)
consulted: ../.memlog.md (2026-11-23 frontend entries), ../../../ux-designs/ux-IBE160-G13-2026-11-11/EXPERIENCE.md (final), ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (FR-5, FR-6, FR-8, FR-11, FR-13, FR-15, FR-16, FR-31, FR-32, FR-40, FR-41, FR-43, FR-49)
lens: two frontend units one level down (stories built by different people or AI agents) that each obey every AD to the letter and still build incompatibly
excludes: backend seams already covered by review-2026-11-23-adversarial.md and the earlier reviews
---

# Adversarial review: frontend pairs that still collide

**Verdict:** the frontend ADs pick the right shape: one gate function, one game client, one token source and tests against the real stack. But they leave the shared client state without owners. These were written for a stateless projection, and the UX has five pieces of state that only live in the page: the result gate, the recap and year-end dismissals, the unread marks, the disclosure just dismissed, and a pending or offline action. AD-18 also builds the protocol fields from "the store" at send time. That quietly undoes the stale-device protection that `month`, `playthrough_id` and `plan_version` exist for. And AD-17's crisis gate locks the player out of the bank that FR-32b needs during a crisis. Three findings are critical. All of them close with AD sentences, and none needs a new unit.

| Severity | Count |
| --- | --- |
| Critical | 3 |
| High | 10 |
| Medium | 11 |
| Low | 8 |

Each finding names Unit A and Unit B, how each obeys the ADs, the divergence, and a fix as a sentence for the spine.

---

## Critical

### C1. `sendAction` takes the protocol fields from the latest store, not from the view the player acted on

- **Unit A, the game client story (AD-18):** `sendAction(action)` "builds `{request_id, playthrough_id, month, action}` (`plan_version` on continue) from the store". AD-18 also calls `GET /api/game` "on the player's next input after 5 minutes idle or a return to the tab". The client therefore fetches first and then sends the input that triggered the fetch, with fields read from the store, which now holds the new view.
- **Unit B, the hub CTA and the plan screen (AD-17, EXPERIENCE "Confirm before continuing"):** the confirm sheet shows the trigger status the player saw («Krise i desember hvis du fortsetter nå») and calls `sendAction({type: 'continue'})` on «Fortsett likevel».
- **Divergence:**
  - On a school PC left on month 5's hub, the phone has moved to month 7. Markus taps «Fortsett». The idle trigger fetches month 7, and `sendAction` stamps `month: 7` and month 7's `plan_version`. The server accepts, and a month he never saw is closed. FR-8 ("before it accepts the next choice") and FR-49 (the plan version "the device showed") both fail without any backend check firing.
  - The same happens on desktop with no other device. The confirm sheet is open in the centre while Markus removes an activity in the pane, so `plan_version` rises in the store. «Fortsett likevel» then sends the new version, and he has confirmed a trigger status that no longer holds.
  - A third builder reads "next input" as "swallow the input", so the tap does nothing and nothing is shown. Two builders make three behaviours.
- **Fix (AD-18):** *"An input that triggers an FR-8 fetch is consumed by that fetch and is never sent. If the fetched view's `playthrough_id` + `state_version` differ from the shown one, the page shows «Spillet ble oppdatert på en annen enhet.» through the live region; otherwise the player taps again. `sendAction(action, shown)` takes the `playthrough_id`, `state_version`, `month` and `plan_version` of the view the control was rendered from, and it sends nothing and treats the action as refused when the store's `state_version` is newer."*

### C2. The crisis gate locks out the bank and the plan that FR-32b keeps open during a crisis

- **Unit A, the gate story (AD-17):** `gateFor` returns "a crisis step" while one is pending, and "a gate renders in place of the area content whatever the URL". `/penger` and `/plan` show the crisis step.
- **Unit B, the bank and plan stories (FR-32b, FR-49, EXPERIENCE Crisis check):** "money actions and open options stay available, use no crisis step, and the triggers are checked again after them". A money action can end the crisis (FR-32c: it ends "when no trigger is true"). Activities "can be planned in a crisis month as in any month".
- **Divergence:**
  - Built to AD-17, the only way out of a crisis is the crisis options. A transfer from savings that would clear a negative balance can't be made, so the player spends a step on «Spør mamma om hjelp» instead.
  - A bank builder who follows FR-32b adds a «Til banken» link on the crisis step. That link lands on `/penger`, which the gate turns back into the crisis step: a loop.
  - A third builder exempts `/penger` from the gate in a crisis month, so the bank and the crisis step disagree about what is pending.
- **Fix (AD-17):** *"A crisis step is a Hjem-area screen, not a gate. `/hjem` shows it while a step is pending, and every other area stays reachable; continuing is refused (`cannot_continue`) until the crisis ends. After a money action that ends the crisis, the hub shows the crisis end. Only setup steps, the month's event (the card warning included), the recap, the year end, the result and the ending are gates."* The alternative is to say that FR-32b's money actions are not offered while a step is pending. That is a PRD change and needs the team's decision.

### C3. Gates that the player dismisses have no dismissal owner, and `gateFor(view)` can't express one

- **Unit A, the gate story (AD-17):** `gateFor(view)` is a function of the view. The recap comes from `server_time − last_action_at` against `recap_threshold`, and the year end is shown in December. Neither changes until the player's next game action. «Fortsett» on the recap, «Fortsett» on the year end and «Spill på nytt» on the ending make no request, because the protocol has no "seen" action.
- **Unit B, the recap, year-end and ending screens (EXPERIENCE: "One button continues", "Two buttons: continue, or «Ferdig for nå»", "One button: «Spill på nytt»"):** each holds a `dismissed` flag in its own `useState`.
- **Divergence:**
  - Built literally, the recap and the year end can never be left. The same view gives the same gate on the next render.
  - With component state, the flag dies when the gate unmounts. The AD-17 result gate (also "held only in the page session") has the same problem: the event component holds the result reference, and it unmounts the moment the response turns `gateFor` to "none". The result is never shown.
  - A third builder adds a backend `acknowledge` action, which no AD allows and which would raise `state_version` and close the recap window on other devices.
  - Reload behaviour differs by owner. The result disappears after a reload (AD-17); nothing says whether the year end and recap come back.
  - "After a login" (FR-16) can't be read from the view at all, so a recap after a 10-minute re-login is shown by one builder and skipped by another.
  - `gateFor(view)` doesn't receive `server_time` or `recap_threshold`, which sit in the envelope, not the view. One builder passes the envelope, another passes the view and reads `Date.now()`, against AD-13.
- **Fix (AD-17):** *"`gateFor(envelope, session)` is pure over the latest envelope and one page-session record owned by the game client: `{justLoggedIn, dismissed: Set<(playthrough_id, gate kind, month)>, shownResult: result_id | null, playAgain: boolean}`. Only `frontend/src/api/` writes it. «Fortsett» on the recap and the year end adds to `dismissed`; a login sets `justLoggedIn` until the recap is dismissed; an event, crisis or pengegave response with a non-null `result` sets `shownResult`; «Spill på nytt» sets `playAgain`. The record is cleared on reload, on logout and when `playthrough_id` changes, so after a reload the recap and year end show again and the result does not."*

---

## High

### H1. Whether a setup step or a choice is pending is derived by the frontend

- **Unit A, the engine view story (AD-13; "Other fields of … the player view" deferred to engine stories):** it exposes `avatar: null` until it is chosen and `pengegave: {amount, placed: false}`, and it lists the event under `event` with `chosen_option_id: null`.
- **Unit B, the gate story (AD-17):** it builds `gateFor` on a field it expects, `setup_step: 'avatar' | 'gift'`. Once that doesn't exist in the generated types, it infers the step from `avatar === null`.
- **Divergence:** the order and completeness rules of FR-11's "the next login continues at the first step not done yet" end up written twice: in the engine, which refuses with `cannot_continue` or `already_chosen`, and in `gateFor`. When a pengegave action is split into a transfer plus a choice, the two disagree on whether a half-placed gift is "done". AD-13 already says the frontend never derives a status, and this is one.
- **Fix (AD-13, Other statuses):** *"The view carries `pending`: one of `none`, `setup_avatar`, `setup_gift`, `event`, `crisis_step`, computed by the engine function that also decides `cannot_continue`. `gateFor` reads it and never infers a step from other fields."*

### H2. No precedence among gates

- **Unit A, the year-end screen:** it is shown "when December opens".
- **Unit B, the event screen:** it "opens an active month, before its hub".
- **Divergence:** a December with an event has both, and AD-17 gives no order. Nor does it order these pairs:
  - the recap against a pending setup step, event or crisis
  - the result gate against the next crisis step after a step's result
  - the recap against the ending (FR-16 says FR-43 applies "instead")
  - the year end in month 60, against month 60's summary and the ending
  - the "crisis skipped" note (FR-32a: skipped at open, "with a short note", event chosen again)

  Two `gateFor` implementations, each a chain of `if`s in a different order, both pass their own Vitest fixtures.
- **Fix (AD-17):** *"`gateFor` checks in this fixed order and returns the first match: start screens (`status` `none` or `ended`, or `playAgain`), ending (`completed`), recap (`justLoggedIn` or the gap at or above the threshold, not dismissed), setup step, result (`shownResult`), year end (December, not dismissed), event, crisis end note; the crisis-skipped note is a line in the month summary, not a gate. One Vitest table test covers every pair."*

### H3. Refusals with `state: null`, and refusals with no `server_time`

- **Unit A, the game client story (AD-18):** it "treats every other code as a refusal whose `state` replaces the store". A `401 not_logged_in` and a `422 invalid_input` carry `state: null` (AD-13).
- **Unit B, the hub story:** it reads `store.state.month` and the rest of the view on every render.
- **Divergence:**
  - A literal Unit A writes `null` into the store, and the next render throws before AD-17's redirect to `/logg-inn` runs. A second builder keeps the old state. A third merges the refusal's `state` into the old envelope.
  - The refusal envelope (`code`, `message`, `state`) has no `server_time` or `recap_threshold`. Replacing the envelope "whole" therefore drops the inputs to the recap check (`NaN`, so the recap never or always shows). Keeping the old `server_time` against a newer `last_action_at` from another device gives a negative gap.
  - AD-13 says to fetch `GET /api/game` after a 422 on the action endpoint, but that is not one of AD-18's four fetch triggers.
  - Which refusals show «Spillet ble oppdatert på en annen enhet.» (EXPERIENCE, FR-8) is unstated: `game_changed`, `plan_changed`, `wrong_month`, `already_chosen`? Each screen picks its own.
- **Fix (AD-18; AD-13 Errors):** *"Every game refusal with a non-null `state` also carries `server_time` and `recap_threshold`, and the store replaces its envelope with them. A refusal with `state: null` never touches the store: `401` clears it and goes to `/logg-inn` (H7), and `422 invalid_input` on the action endpoint triggers one `GET /api/game`, the fifth allowed fetch trigger. `wrong_month`, `plan_changed`, `game_changed` and `already_chosen` show «Spillet ble oppdatert på en annen enhet.» once through the live region; other refusals show their `message` next to the control."*

### H4. Concurrent game requests and out-of-order responses

- **Unit A, the bank in the desktop pane:** it sends a transfer.
- **Unit B, the hub CTA in the centre:** it sends continue while the transfer is in flight. Both use `sendAction`, and AD-18 never makes it single-flight.
- **Divergence:**
  - The server serializes the two by lock. If continue wins, the transfer is refused with `wrong_month`. Its refusal state (month M+1, from before or after the continue response depending on network order) and continue's success response both "replace the store whole", in whatever order they arrive. An older view can overwrite a newer one, so the hub shows month M after M+1 opened.
  - A double tap on the life goal makes two starts with two `request_id`s. The second carries `playthrough_id: null` after a row exists and gets `409 game_changed`, shown as "updated on another device" on a brand-new account.
  - EXPERIENCE's "every option is locked" is per screen. Nothing locks the other pane.
- **Fix (AD-18):** *"`sendAction` is single-flight across the page: while a game request is pending, every game control everywhere is locked (`aria-disabled`, described by the saving text) and a second call is refused without sending. The store accepts an envelope only if its `playthrough_id` differs from the stored one or its `state_version` is not lower."*

### H5. Retrying a transport failure without a timer can deadlock, and the offline state has no exit rule

- **Unit A, the game client (AD-18):** it "retries transport failures … with the same `request_id`" and "there are no timers". AD-10 adds that "no request is made without a player input, a page load, a login or the connection coming back". So it retries only on the `online` event.
- **Unit B, the offline bar (AD-18, EXPERIENCE Offline):** offline is "`navigator.onLine` false or a transport failure", and the store "marks options locked".
- **Divergence:**
  - A Caddy `503 unavailable` during a backend restart happens while `navigator.onLine` stays true. No `online` event ever fires, options are locked so the player can't give an input, and the page stays at «Prøver fortsatt …» until a reload.
  - A second builder retries on `setTimeout` with backoff, which breaks AD-10's no-timer rule and slides the idle session.
  - After `internal_error` twice, "at most once" ends the retries, but nothing says what is then shown: a refusal, offline, or an error.
  - When `online` fires while an action is pending, AD-18 both refetches `GET /api/game` and retries the action. The GET may land first, showing the choice applied with no result (FR-6 fails), or showing the event still open while the retry is in flight.
- **Fix (AD-18; AD-10 amended):** *"A pending action is retried at 2, 5 and 10 s after a transport failure. These retries continue the player's input and are the only timer-driven requests allowed (AD-10). After them, the bar shows «Prøver fortsatt …» with a «Prøv igjen» button, and `online` retries too. While an action is pending, `online` retries the action and does not fetch `GET /api/game`. A second `internal_error` ends the action with the fixed chrome text «Noe gikk galt. Prøv igjen.» and one `GET /api/game`. The offline state clears on the next response with a JSON `code` or success."*

### H6. The result gate's source after a retry, a replay or a refusal

- **Unit A, the result screen (AD-17):** "it shows the result the action's response refers to".
- **Unit B, a second builder of the same screen:** it shows the open month's latest result entry, because after a reload or a replay the response's `result` may be `null` (AD-13: "`result: null, replayed: true`").
- **Divergence:**
  - Two devices answer the same event. The phone's choice is refused with `already_chosen`, and its refusal `state` holds the PC's result as the latest entry. Unit B shows the PC's choice as if it were the player's own result on this device; Unit A shows nothing.
  - On a replayed retry with a non-null reference (the lost-response case of FR-6), one builder hides the result because `replayed` is true. FR-6 says the result is shown when the connection comes back.
- **Fix (AD-17):** *"The result gate shows only the entry named by a success response's `result.result_id`, whether `replayed` is true or false; a refusal, a `null` result or a reload never shows it."*

### H7. Logout, account deletion, a revoked session and a new login leave the game store behind

- **Unit A, the menu and account forms:** logout, «Logg ut overalt» and deletion are "plain typed calls" (AD-18). After success they `router.push('/')`.
- **Unit B, the game client:** its store lives in a module, so it survives client-side navigation.
- **Divergence:**
  - On a shared school PC, after Markus logs out, the back button or the next player's login renders Markus's envelope (balances, nickname, messages) until the post-login `GET` returns. NFR-3 and FR-5 ("can't be reached on that device") fail.
  - AD-17 sends a 401 to `/logg-inn`, but nothing clears a pending `sendAction`, the page-session record (C3) or the offline lock.
  - The login page builder fetches `GET /api/game` after login (an AD-18 trigger). The game layout builder fetches on mount. Done both ways you get two requests; done neither way, an empty store.
  - «Du ble logget ut. Logg inn igjen for å spille videre.» is shown after a revoked session, but not after the 30-minute idle expiry? EXPERIENCE ties it to logout elsewhere; nothing says how `/logg-inn` learns the reason. One builder uses `?grunn=`, another `sessionStorage`.
- **Fix (AD-18):** *"The game client exports `reset()`, which drops the envelope, the pending action and the page-session record. Logout, logging out everywhere, account deletion and every `401` call it before navigating, and only the login and sign-up success handlers call `GET /api/game`, after `reset()`. A `401` from a request made with a store holding a view navigates to `/logg-inn?utlogget=1`, which shows the logged-out text; a `401` on page load shows the plain login screen."*

### H8. Focus and the one polite live region have no owner across gate swaps

- **Unit A, the event screen (EXPERIENCE "Saving a choice → stays on the chosen option"):** it keeps focus on «Lagrer …».
- **Unit B, the result screen:** it moves focus to its `h1` on mount. A third unit, the toast, adds `aria-live` for «Ny melding fra Emma.», and the offline bar uses `role="status"`.
- **Divergence:**
  - A gate swap changes no URL, so EXPERIENCE's "a route change → the screen's `h1`" doesn't fire. When the response replaces the event with the result, the focused option unmounts and focus falls to `body`, unless the result builder happened to add a mount effect. «Fortsett» on the result has the same problem.
  - Each feature that needs an announcement mounts its own region. That breaks EXPERIENCE's "one polite region exists from page load". A region rendered inside a gate or page is unmounted with it, so announcements made during a swap (saving, the result, offline) are lost.
  - `frontend/src/api/` may not import `components`, so "`sendAction` … shows «Prøver fortsatt …» after 5 s" (AD-18) can't be done by `api` itself, and builders invent different hooks.
- **Fix (AD-17, AD-18):** *"The root layout mounts the one polite live region and exposes `announce(text)` from `components/`; no other element carries `aria-live`, `role="status"` or `role="alert"`. One focus manager in the gate shell moves focus to the new screen's `h1` whenever `gateFor`'s result or the pathname changes, except for the in-place moves in EXPERIENCE's focus table. The game client exposes `pending` (`{action, since, slow}`) in the store; components render «Lagrer …» and «Prøver fortsatt …» from it and announce it once."*

### H9. The end-to-end suite and the seed script disagree on who owns test state, and CI's single network hits the sign-up limit

- **Unit A, the Playwright suite (AD-20):** it runs the main flow at 320, 390 and 1280 px, "logged in as the NFR-6 seeded users". Each run continues months, picks the card option and plays the crisis.
- **Unit B, the seed story (AD-14):** it seeds each user once (`cli seed --if-empty` in local; CI "runs the seed script and asserts each target state").
- **Divergence:**
  - The 320 px run consumes the seeded crisis and the 390 px run finds a hub. Parallel Playwright workers race on one playthrough and get `409 already_chosen`. Tests pass in isolation and fail together.
  - "Sign-up" at three widths, plus retries, comes from one fixed placeholder network in `ci` (AD-10), so the per-network sign-up limit and the failed-login limits trip with `429`.
  - Nothing says whether Playwright may call the CLI to reset a user.
- **Fix (AD-20; AD-14):** *"Each Playwright test that changes state starts from its own seeded copy: CI runs `cli seed --user <name> --fresh` (allowed only in `local`/`ci`) per test file, and the main flow's sign-up uses a unique address per run. The `ci` compose environment raises the sign-up and login limits in settings, except in the limit tests, which set `X-Client-IP` explicitly. Read-only screens (axe checks) may share one seeded user."*

### H10. A gate on desktop: does it cover the pane and the tabs?

- **Unit A, the desktop layout (AD-17: "From 1100 px the layout opens `/mobil`, `/jobb` and `/penger` in the right pane while the centre shows Hjem"):** it renders the gate in the centre, because the gate replaces "the area content", and the pane keeps its route.
- **Unit B, the event gate builder:** it reads "whatever the URL" as covering the whole viewport, pane included. AD-17's "Prevents" names "the plan while an event waits".
- **Divergence:**
  - With Unit A, Markus sells the moped in the pane while October's event waits in the centre, or answers an offer in the thread. With Unit B he can't.
  - The tab bar highlights from the pathname. During a gate on `/plan`, it shows Plan as current over an event, while EXPERIENCE says the event "counts as Hjem". Below 768 px EXPERIENCE hides the tabs for some gates (gift, recap, ending) and not others.
- **Fix (AD-17):** *"A gate replaces the centre and the pane together, and the tab bar or rail marks Hjem as current during every gate. Setup steps, the recap and the ending hide the tab bar and rail; the event, result, year end and card warning keep them, and a tab tapped during a gate changes the URL but the gate stays."*

---

## Medium

### M1. Unread marks: three owners of "opened in this page"

- **Units:** the inbox (`/mobil`) clears bold rows and dots when a thread opens. The Mobil tab badge (layout) and the hub sticker «2 nye» count the view's `new` flags. The toast's ×.
- **Divergence:**
  - If the opened set lives in the inbox component, navigating away brings the dots back. EXPERIENCE says only a reload should.
  - The badge never drops, because `new` stays true all month (#112), while the inbox shows no dots.
  - Does opening the thread from the toast count as opened? Does × count?
  - The toast's trigger is "when the month opens with a new message". One builder shows it on every load with new messages, another only after a continue response, and a third shows it again each time Hjem mounts.
- **Fix (AD-18 or EXPERIENCE pointer):** *"The page-session record (C3) holds `openedMessageIds`. A message is unread when its view `new` flag is set and its id is not in that set, and the badge, the sticker, the inbox and the toast all use this one selector. Opening a thread from anywhere adds its id; the toast's × doesn't. The toast shows only after a continue response whose new month has an unread message, once per month per page session."*

### M2. A disclosure's "seen" state is stale after «Skjønner»

- **Unit A, the disclosure card:** it posts the seen id (a plain call, AD-18) and hides itself in local state.
- **Unit B, the plan screen:** it decides to show D26 from the view's seen list.
- **Divergence:**
  - The view still lists D26 as unseen until the next game response. Leaving and coming back to `/plan` shows the card again. A builder who refetches `GET /api/game` after the POST uses a trigger AD-18 doesn't allow.
  - Which disclosure belongs to which screen ("the first time a mechanism appears") is content knowledge. Hard-coding `D26` in the plan component breaks AD-13's "frontend owns only chrome" if ids move.
- **Fix (AD-13, AD-18):** *"The view carries, per screen area, the ids of disclosures due now, with their text. After a successful disclosure POST the game client adds the id to the page-session `seenDisclosureIds`, and the selector for due disclosures subtracts it. Nothing refetches."*

### M3. Account forms and the start have no double-submit rule

- **Units:** sign-up, password change, nickname change and deletion (plain calls, never retried), and the life-goal start (a game action).
- **Divergence:**
  - A double tap on «Lag bruker» sends two sign-ups. The second gets `409 email_in_use`, and the form shows "already exists" to a user who was just created and logged in.
  - A double password change makes the second request fail `403 wrong_password` (the current password has just changed), so «Feil passord.» shows after a success.
  - One builder locks the button; another doesn't.
- **Fix (AD-18):** *"Every account, session and disclosure form is single-flight: its submit is locked (`aria-disabled`, «Lagrer …») from send to response, and a lost response follows AD-2 (fetch `GET /api/game` or show login)."* H4 covers the start.

### M4. Account changes that alter view text leave the store stale

- **Units:** the nickname sheet in the menu, and the hub and messages that render "Hei Mak!" (AD-13 fills the nickname when the view is built).
- **Divergence:** after a nickname change, every game text and the menu link keep the old name until the next game action. One builder refetches (not an allowed trigger), another patches `view.nickname` in the store (a client-edited view), and a third leaves it.
- **Fix (AD-18):** *"A successful nickname change is followed by one `GET /api/game`; this, a login and a 422 on the action endpoint are the only fetch triggers beyond page load, `online`, idle and tab return."*

### M5. Error bodies are not typed per route in the generated contract

- **Units:** the backend router story (AD-13: errors through `AppError` handlers) and the game client (AD-18: "types are never written by hand").
- **Divergence:** FastAPI documents only `422` validation errors unless each route declares its error responses. openapi-fetch then types `error` as `unknown` for 401, 403, 409 and 410, and the client builder hand-writes `{code, message, state, fields}`. That is exactly what AD-18 forbids, and it drifts when `fields` changes.
- **Fix (AD-13, Contract):** *"Every route declares its non-2xx responses with the shared error envelope model, whose `code` is the enum of stable codes, so the generated types cover every error body; a contract test fails on a route without them."*

### M6. "The first free evening" is computed in the client

- **Units:** the desktop add list ("a + places the item on the first free evening") and the plan action model (AD-4, members deferred).
- **Divergence:** the backend builder makes `slot` required. The desktop builder then picks the first free slot from the view, which is a derived status, against AD-13. A mobile builder sends the evening the sheet was opened for. If the backend makes `slot` optional and picks the first free one itself, two clients behave differently on the same request.
- **Fix (AD-4 or AD-13):** *"The place action takes an optional `slot`; omitted, the engine places on the first free evening, and the desktop list always omits it."*

### M7. Echoing a typed amount needs a formatter the frontend is not allowed to have

- **Units:** the transfer, extra-payment and loan forms ("Flytt 5 000 kr til sparekontoen?") and AD-13 ("every money figure the UI shows as text … is a string from that function").
- **Divergence:** one builder writes `Intl.NumberFormat('nb-NO')`, which gives "5 000,00 kr" with a different minus sign and decimals. Another avoids echoing, so confirmation sheets differ between screens.
- **Fix (AD-13, Game text):** *"The only money text the frontend formats is the player's own typed input, through one `formatKroner(int)` in `components/` that follows AD-13's rules (U+00A0 groups, U+2212 minus, «kr» after) and is tested against the engine's output for the same integers."*

### M8. Vitest fixtures can be typed and still be impossible

- **Units:** the `gateFor` and component tests ("fixtures are player views typed by the generated API types") and the engine view story.
- **Divergence:** a hand-built fixture satisfies the types but not the semantics, for example an event pending in a `completed` view, or `band: 'good'` on a value under the threshold. `gateFor` passes on fixtures and fails on real views. The memlog said "never hand-shaped"; the spine dropped that.
- **Fix (AD-20):** *"Fixtures are player views captured from the seed run by a CI step into `frontend/src/test/fixtures/`, and a staleness check fails when they differ; hand edits are limited to removing fields."*

### M9. Two ways to start a new life from the menu, and «Spill på nytt» has no path

- **Unit A, the menu:** "start a new life" sends the end-early action (`status = ended`), and `gateFor` shows the start screens.
- **Unit B, a second builder of the same screen:** it navigates to the life-goal screen and sends the start directly with the active `playthrough_id`. AD-4 allows this ("names the playthrough the request acts on or replaces").
- **Divergence:** leaving halfway through the life-goal screen leaves the old life ended with Unit A and still active with Unit B. «Spill på nytt» on a `completed` life has no ended state to fall into, so it needs C3's `playAgain`.
- **Fix (AD-17):** *"Starting a new life from the menu sends the end-early action after the confirmation, and the start screens follow from `status: ended`; «Spill på nytt» sets `playAgain`. Only the life-goal screen sends the start."*

### M10. The pengegave choice and the crisis end are outside the result rule

- **Units:** the gift screen (Flow 1: "13 shows the money … because of his own choice") and AD-17 ("the result after an event or crisis choice").
- **Divergence:** one builder shows the result after the gift and another doesn't. One builder shows the crisis end ("the end screen lists what changed") as a result gate, which disappears after a reload. Another reads it from the view as a gate.
- **Fix (AD-17):** *"The result gate follows the pengegave choice, an event option and every crisis step; the crisis end is the last step's result."*

### M11. The desktop pane is built two ways

- **Units:** a layout builder using App Router parallel routes (`@pane`), and one rendering by a JS media query in a client layout.
- **Divergence:** the media-query build gets a hydration mismatch and renders Hjem plus the pane route at once, with two `h1`s and duplicate ids. Resizing across 1100 px changes which element is focused. The parallel-route build needs different file paths. Stories that add a pane screen don't know where to put the file.
- **Fix (AD-17):** *"The pane is an App Router parallel route (`@pane`) in the game layout. From 1100 px it holds `/mobil`, `/jobb` and `/penger` and the centre slot holds Hjem; below, the pane slot is not rendered. The breakpoint is decided by CSS on the layout, never by JS before hydration."*

---

## Low

### L1. «Ferdig for nå» has no defined effect

EXPERIENCE gives the year end two buttons, and nothing says whether «Ferdig for nå» logs out, goes to `/hjem` or closes nothing. **Fix (AD-17):** *"«Ferdig for nå» dismisses the year end like «Fortsett» and shows a short chrome line; it never logs out."*

### L2. The year chart's `role="status"` is a second live region

This contradicts "one polite region" in EXPERIENCE itself, and H8's fix forbids it. **Fix:** with H8, the chart's detail announces through `announce()`.

### L3. Cross-screen intents have no carrier

«Til planen» opens Plan "with the Jobb tab chosen", «Til banken» comes from the confirm sheet, and after a re-login the player may need to return to the screen they left. One builder uses search params and another uses store state. **Fix (AD-17):** *"Cross-screen intents are URL search params on the area route (`/plan?vis=jobb`), never store state."*

### L4. A logged-in player on `/`, `/logg-inn` or `/ny-bruker`

The cookie is `httpOnly`, so only `GET /api/game` can tell. One builder fetches on these pages; another shows the form to a logged-in player. **Fix:** *"The pages outside the game call `GET /api/game` on load and go to `/hjem` on `200`."*

### L5. The quote call has no classification

`GET /api/game/quote` is neither the game store nor an account call. Nothing says whether it retries, or whether a quote shown after another device acted is stale. **Fix (AD-18):** *"Quote calls are plain typed calls, never retried; the sheet drops its quote whenever the store's `state_version` changes."*

### L6. Gates are not deep-linkable, so "the main screens" for axe is undefined

The axe runs reach the event, result, crisis, year end and ending only by driving state. **Fix (AD-20):** *"The axe list is every surface in EXPERIENCE's table that the MVP builds, each reached from a seeded user at the matching state."*

### L7. The crisis-skipped note has no home

FR-32a's "short note" could be a gate or a summary line. H2's fix places it in the month summary. Recorded here so the engine view story carries it as a summary line.

### L8. The idle clock

"5 minutes idle" can be measured from the last input or the last request, and builders differ. **Fix (AD-18):** *"Idle is measured from the last player input handled by the page."*

---

## Where the fixes land

| AD | Findings |
| --- | --- |
| AD-17 | C2, C3, H2, H6, H8, H10, M9, M10, M11, L1, L3, L4 |
| AD-18 | C1, H3, H4, H5, H7, H8, M1, M2, M3, M4, L5, L8 |
| AD-13 | H1, H3, M2, M5, M6, M7 |
| AD-20 / AD-14 | H9, M8, L6 |
| AD-10 | H5 (timer-driven retries of a pending action) |

C2 is the one finding that may need the team rather than a sentence: either the crisis stops being a gate (the recommended fix), or the PRD changes FR-32b.
