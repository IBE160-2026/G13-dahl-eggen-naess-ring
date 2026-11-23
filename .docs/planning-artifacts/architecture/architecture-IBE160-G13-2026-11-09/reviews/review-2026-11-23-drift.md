---
title: Drift review — ARCHITECTURE-SPINE.md against the current PRD and the final UX
created: 2026-11-23
spine: ../ARCHITECTURE-SPINE.md (updated 2026-11-23)
inputs:
  - ../../../prds/prd-IBE160-G13-2026-10-22/prd.md (working copy 2026-11-23)
  - ../../../prds/prd-IBE160-G13-2026-10-22/addendum.md
  - ../../../prds/prd-IBE160-G13-2026-10-22/.memlog.md (entries 2026-11-16 to 2026-11-23)
  - ../../../briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md (Rule Set v1)
  - ../../../ux-designs/ux-IBE160-G13-2026-11-11/EXPERIENCE.md (final 2026-11-23)
  - ../../../ux-designs/ux-IBE160-G13-2026-11-11/DESIGN.md (final 2026-11-23)
baseline: reviews/reconcile-prd-2026-11-15.md (last full reconcile)
method: independent read; spine not edited
---

# Drift review: spine vs current PRD and final UX

**Verdict:** the spine still holds structurally. The #111 and #116 changes (bands, start year, month totals) and the nickname, OQ-12 and Vercel changes are in. The #105 job-and-shift change was only partly carried over: the spine handles one-off shift *pay* in AD-9, but not one-off shifts as content, not the hours-offer flow, and not the new inputs and refusals. The UX also needs two things from the view that AD-13 doesn't provide: a quote for a loan the player configures, and field-level form errors. One UX element breaks an AD-13 rule (the nickname preview at sign-up).

**Count:** 0 critical · 2 high · 6 medium · 9 low (17 findings). 11 need a spine sentence, 6 need a PRD, Rule Set or UX change (2 need both).

Line numbers refer to the files as they stand on 2026-11-23. "Spine" means `ARCHITECTURE-SPINE.md`.

---

## High

### H1. One-off shifts and hours answers have no content home, no schema and no owner in the selection step

- **Source:**
  - prd.md:939 (FR-47): «a player with a job sees the employer's one-off shifts for this month in the job view and in the month plan's activity picker. Each has a name (flavour) and its hours, from the content library.»
  - prd.md:846 (FR-55): «when the player has asked for more or fewer hours (FR-47), the employer's answer arrives as a triggered offer the next month»
  - prd.md:827 (FR-54) still lists only three offer targets: «points to an open option (FR-48), to extra shifts (FR-47), or to a one-time gift»
  - addendum.md:139-163: schemas exist for events, activities and messages only. The message `links to` row (addendum.md:160) has no hours-answer target, and there is no one-off shift schema. FR-53 (prd.md:811) says «no activity pays money», so a shift can't be an activity.
- **Spine:**
  - AD-7, line 140: «`content/library/vN/` holds `events/`, `activities/`, `messages/`, `room/`, `options/` … `expenses/`, `texts/` … and `lists.yaml`». There is no folder for one-off shifts.
  - AD-8, line 150: «One engine unit decides what arrives when a month opens: the event, and the messages.» It doesn't say which unit picks this month's one-off shifts, or whether they are drawn (which would bring in AD-6's draw-owner rule).
  - Deferred, line 412: «Content schemas in detail … The addendum's schemas apply». No such schema exists.
- **Why it matters:** this is the exact failure AD-7 says it prevents («content kinds placed differently by authors and engine builders»). Content authors may put shifts under `activities/` with a pay field, which breaks FR-53. Engine builders may draw shifts outside the selection step. The hours answer has no `links to` value that the content check can validate.
- **Fix (both sides):**
  - **PRD addendum should change:** add a one-off shift schema (id, version, name text, hours as a quoted Decimal, age range, required and blocking flags, how many per month or a chance, and the source for the hours). Add «an hours answer (FR-47)» to the message `links to` row and to FR-54's offer kinds, or state that the hours answer is a system message with no library item.
  - **Spine AD-7, layout:** add «`shifts/` (one-off shifts, FR-47; never an activity, since they pay)».
  - **Spine AD-8:** «… the event, the messages (including the triggered answer to an hours request, FR-55) and the month's one-off shifts (FR-47). A shift that is drawn has its draw key built in `draws.py` like any other draw.»

### H2. The UX shows a loan quote for terms the player picks, and the spine has no read path for it

- **Source:**
  - EXPERIENCE.md:138: «"Se hva et lån koster" opens a sheet. The term is three toggle buttons (12, 24, 36 months); the sheet shows the amount, the rate, the monthly payment, the last payment, the total and what the loan costs, all engine figures, before the loan is taken.»
  - prd.md:997-998 (FR-25): the amount runs from NOK 5,000 up to a cap in steps of NOK 1,000, and the term is 12, 24, 36, 48 or 60 months.
- **Spine:**
  - AD-4, line 89: «`GET /api/game` returns the player view. Account, session and disclosure endpoints are separate.»
  - AD-13, line 210: «the view carries every figure the UI shows as a status, a date or a sum, computed in the engine; the frontend never derives one.»
  - AD-13, line 207: «No endpoint serves library or config files or their parsed form»
- **Why it matters:** an annuity schedule for an amount and term the player picks is neither in the view nor reachable through any endpoint. The frontend can't compute it either, because AD-13 forbids that. Under deadline pressure, the likely result is the frontend computing rule 4 itself, which breaks NFR-4. The same pattern (a preview of an input the player hasn't committed yet) is close for the card's fixed-amount stepper if the UX later shows its payoff time.
- **Fix (spine, AD-13, new bullet):** «**Quotes:** where the UI previews an action whose figures depend on a parameter the player picks before confirming (the consumer loan's amount and term, FR-25), the view carries the engine's quote for every allowed term at the amount shown. If the player may change the amount, `GET /api/game/quote?kind=loan&amount=&term=` returns the engine's quote. It is read-only, writes nothing, and goes through the same view formatting. The frontend never computes one.» Also add FR-25 to AD-13's binds.

---

## Medium

### M1. AD-2 limits requests to NFR-7's input list, which doesn't name the parameters the new actions need

- **Source:**
  - prd.md:1391 (NFR-7): «the option, money action, or activity they picked, plus changes to the month plan, a savings-target pin, a disclosure they've seen, ending a life early or starting a new one, an amount where one is asked for, or an answer in a minigame. The server ignores anything else.»
  - New inputs:
    - the loan term (prd.md:998; EXPERIENCE.md:138)
    - the card payment mode, which is whole, minimum or fixed (prd.md:1010; EXPERIENCE.md:137)
    - asking for *more* or *fewer* hours (prd.md:938; EXPERIENCE.md:160)
    - yes or no on an hours offer, and «Nei takk» on an extra-shift offer, which persists as «Du sa nei takk.» (EXPERIENCE.md:159, :197)
- **Spine:** AD-2, line 76: «Requests carry the player's inputs listed in NFR-7, the protocol fields in AD-4, and the account and start inputs … Following NFR-7, unknown fields are ignored».
- **Why it matters:** NFR-7's categories do cover the actions themselves. Ask for and answer hours, the card switch and the payment mode are FR-45 money actions (prd.md:900, :903), and placing a one-off shift is a month-plan change. But a term, a mode, a direction and a yes/no aren't «an amount». Read literally, AD-2 together with «unknown fields are ignored» lets a server drop `term`. Declining an extra-shift offer isn't a listed money action at all (FR-45 lists only «answer an hours offer»).
- **Fix:**
  - **Spine AD-2:** «… the player's inputs listed in NFR-7, each with the parameters its FR names (an amount, a loan term, a card payment mode, more or fewer hours, yes or no on an offer) …».
  - **PRD should change:** NFR-7's input sentence adds «the parameters an action asks for, such as a loan term or a yes or no to an offer», and FR-45 or FR-47 says whether declining an extra-shift offer is stored (the UX assumes it is).
- Checked: «mark messages read» is correctly *not* an input (FR-54 prd.md:834, #112). Disclosure seen and nickname change are covered (AD-2, AD-4, AD-5).

### M2. NFR-7's refusal list wasn't updated for #105, and AD-13 and the test convention key off it

- **Source:**
  - prd.md:1404: «more working hours than rule 10 allows for the month they apply from, including extra shifts (FR-47)». The player no longer sends hours, so the case can only arise through accepting an offer or placing a one-off shift.
  - prd.md:1413 covers activities only («an activity with no empty slot left …»).
  - These cases have no refusal:
    - placing a one-off shift with no job, in month 60, one not offered this month, the same shift twice, or one over rule 10 or the 173 h cap (prd.md:939)
    - a second hours request while one is pending, or asking while an offer is open (prd.md:938; EXPERIENCE.md:188-189)
    - answering an hours offer when none is open
- **Spine:**
  - AD-13 table, line 223: «`invalid_input` and the other NFR-7 input refusals»
  - Tests convention, line 289: «One automated test per NFR-7 refusal case»
- **Why it matters:** the spine's refusal tests and error codes follow NFR-7. Cases missing there get no test and no code, and one listed case can no longer be written as a test.
- **Fix:**
  - **PRD should change:** NFR-7's work bullet becomes «accepting an hours offer, or placing a one-off shift, that would go above rule 10 or the 173 h cap (FR-47)». Add to the month-plan bullet «a one-off shift with no job, not offered this month, placed twice, or in month 60». Add «an hours request while one is pending or an offer is open, or an answer to an hours offer that isn't open».
  - **Spine:** no new rule is needed. Optionally list `request_pending` under 409 in the AD-13 table, since it is a turn refusal.

### M3. One-off shift pay: the rounding point, the rate's age and the stored figure aren't fixed

- **Source:**
  - prd.md:939: «Its pay is its hours × the hourly rate for the player's age, paid with next month's wage at its income step (… #114), taxed as wage income in the month it's paid … The shift shows when the pay comes.»
  - EXPERIENCE.md:155: «"558 kr lønn i desember"» is shown when the shift is placed.
  - The player's birthday is in January (rule 11), so a December shift is worked at age n and paid at age n+1.
- **Spine:**
  - AD-6, line 132: «A `Decimal` result becomes `int` again through the one rule 2 rounding function, at the points Rule Set v1 names: … each job's pay on its own (rule 10). The only other roundings are the ones Rule Set v1 and the PRD name».
  - AD-9, line 168: «A one-off shift's pay therefore belongs to the month it is paid (FR-47).»
- **Why it matters:** the figure shown at placement and the figure paid next month must be the same integer. With no named rounding point, two units can round differently: per shift or summed with the wage, and at the placement month's rate or the payment month's rate. The month totals then disagree with the plan's preview.
- **Fix:**
  - **Spine AD-6, money:** add «each one-off shift's pay, rounded on its own when the shift is placed, at the rate for the player's age in the month it is worked; the engine stores that integer with the shift, the view shows it, and the next income step pays exactly that».
  - **PRD should confirm the age:** add one clause to FR-47: «at the rate for the month the shift is worked».

### M4. The single error shape can't carry the UX's field-level form errors

- **Source:**
  - EXPERIENCE.md:191: «"Passordet må ha minst 8 tegn.", shown with the other errors at once; focus on the first.»
  - EXPERIENCE.md:193: email invalid, with «focus on the field, `aria-invalid`».
  - EXPERIENCE.md:201: nickname invalid has two different messages (too short, or wrong characters), «the same in the menu's sheet».
  - EXPERIENCE.md:192: email in use, with the email field marked.
- **Spine:**
  - AD-13, line 214: «the handlers for it, for `RequestValidationError` and for Starlette's `HTTPException` all emit one shape: `{code, message, state}`»
  - Table line 223: `422 | invalid_input …`
- **Why it matters:** a 422 for sign-up, the nickname change or a password change gives one code and one message. It names no field and can't report several fields at once, so the UI can't mark the field or move focus. Mirroring FR-1's rules in the client is fine for live feedback, but the server's answer is what decides, and the frontend can't tell which field failed.
- **Fix (spine, AD-13 errors):** «For an input refusal on an account form, the shape also carries `fields: [{field, code}]`, with `field` the request field name and `code` a stable string (`too_short`, `invalid_chars`, `invalid_email`, `email_in_use`, `wrong_password`). The frontend maps each code to its own text. The frontend may check FR-1's rules as the player types, but the server's refusal decides.»

### M5. The UX's live nickname preview at sign-up breaks AD-13's «frontend never inserts it into game text»

- **Source:**
  - EXPERIENCE.md:66: «**nickname** with a live preview»
  - EXPERIENCE.md:279: «"Hva skal vi kalle deg?" → "Mak". Emma's preview bubble updates as he types.»
  - prd.md:420 (FR-1): «The server fills it in, the same way it fills in figures».
- **Spine:** AD-13, line 209: «The player's nickname (FR-1) is a placeholder that the same formatting function fills in when the view is built. … the frontend never inserts it into game text. The frontend owns only UI chrome text».
- **Why it matters:** before sign-up there is no account and no view, so the backend can't render Emma's bubble. The frontend must build a message-like sentence containing the nickname, which is exactly what AD-13 forbids. Without a decision, someone may add a content message to the frontend bundle, or an unauthenticated rendering endpoint.
- **Fix (spine, AD-13, game text):** add «The sign-up preview (UX surface 02) is UI chrome: one fixed sentence owned by the frontend, not taken from the content library, with the typed nickname inserted. It is the only place the frontend inserts the nickname into a sentence.» The alternative is that the UX changes the preview to show the nickname alone.

### M6. Rule Set v1 still says the player sets weekly hours, and the spine treats Rule Set v1 as deciding *what*

- **Source:**
  - Brief addendum line 79 (rule 10): «In the game, the player sets weekly hours.»
  - D12, line 291: «Forenklet: Du velger hvor mange timer du jobber i uka …»
  - PRD addendum line 482 (P3): «Extra shifts are never placed in a slot», and line 517: «In the PRD, shifts are never placed in a slot».
  - All of these contradict FR-47 (prd.md:930: «The player can't set them freely: hours change only when the player says yes to an offer») and FR-52 (prd.md:782, one-off shifts take a slot).
  - EXPERIENCE.md:365 notes the D12, D25 and D26 wording as open (#117), but not rule 10 itself.
- **Spine:**
  - Line 26: «The PRD … and Rule Set v1 (brief addendum) decide *what* the game does.»
  - AD-6, line 132 cites rule 10 for the hour-cap and per-job rounding.
  - No spine sentence itself assumes hours are set directly (checked AD-1 to AD-16, the conventions and the map).
- **Why it matters:** an engine builder who reads rule 10 through AD-6 meets «the player sets weekly hours» and may build a `set_hours` action.
- **Fix (Rule Set v1 / PRD should change):**
  - Rule 10: «Weekly hours come from the job and change only through an hours offer (PRD FR-47).»
  - #117 should also cover rule 10 and addendum P3 and line 517 (one-off shifts are the stated exception).
  - Spine: no change needed. Optionally add to AD-6 «rule 10 as amended by FR-47».

---

## Low

### L1. FR-35 is still bound, though it is left out

- **Source:** prd.md:1166: «**Decision (2026-11-23, #115):** left out of the MVP». EXPERIENCE.md:355.
- **Spine:** frontmatter `binds`, line 11 includes `FR-35`. The capability map row at line 396 covers «FR-31 to FR-43».
- **Fix:** keep FR-35 in `binds` but mark it in the map: «Warnings, wellbeing, room, causes, endings (FR-31 to FR-34, FR-36 to FR-43; FR-35 left out, #115; the event schema keeps its texts)». Or drop it from `binds`. Either way, say so in the memlog.

### L2. The binds lists and the capability map don't follow #105's spread of FR-47, or the UX's preview needs

- **Spine:**
  - Map line 394: «Money (FR-20 to FR-27, FR-45, FR-47, FR-57) | `engine` | AD-6, AD-9».
  - AD-13 binds, line 203: «FR-8, FR-12, FR-13, FR-15, rule 11, FR-16, FR-21, FR-33, FR-34, FR-37 to FR-40, FR-42, FR-51, FR-54 …».
  - AD-8 binds, line 148 has no FR-47.
- **Source:** FR-47 now runs through the month plan (prd.md:939, plan_version under AD-4), triggered messages (prd.md:846, AD-8) and view previews (prd.md:938, :860). The view also has to carry the nickname (FR-1), the loan and card figures (FR-25, FR-26: prd.md:1018), the rule 8 status and month 60 previews (FR-49: prd.md:617, :620), job previews (FR-56) and goal progress after the plan (FR-57).
- **Fix:**
  - Map, Money row: «AD-4, AD-6, AD-8, AD-9, AD-13».
  - AD-8 binds: add FR-47.
  - AD-13 binds: add FR-1, FR-25, FR-26, FR-47, FR-49, FR-56, FR-57.

### L3. AD-13's derived-figures list doesn't name several statuses the UX shows

- **Source:**
  - crisis check row «Ingen krise på vei» / «Krise i <måned> hvis du fortsetter nå» (EXPERIENCE.md:139; prd.md:617)
  - offer and job-action previews: kroner left after spending, next month's free evenings, the warning below 50 free time (EXPERIENCE.md:159; prd.md:860, :938)
  - «Gjelder fra desember» (EXPERIENCE.md:161)
  - the month a one-off shift's pay comes (EXPERIENCE.md:155)
  - Plan dot «free evenings left» and Jobb dot «an unanswered offer» (EXPERIENCE.md:186)
  - messages grouped «Nye i <måned>» (EXPERIENCE.md:164)
- **Spine:** AD-13, line 210 has the general rule «every figure the UI shows as a status, a date or a sum», and then lists only bands, calendar and money per month (lines 211-213).
- **Why it matters:** the general rule technically covers these. But «free evenings left» invites the frontend to subtract planned from slots, and «new» invites a date comparison.
- **Fix (AD-13, after «Money per month»):** «**Other statuses:** the rule 8 trigger status with its month (FR-49); each offer and job action's preview (kroner left after spending, next month's slots, the free-time warning; FR-47, FR-56); the month a change or a shift's pay applies; free slots left; whether an offer is open; and each message's arrival month with a `new` flag. Reading a message is never stored (#112).»

### L4. The nickname view field is described as being for the settings only

- **Source:**
  - EXPERIENCE.md:129: «The marker shows the nickname on the hub»
  - EXPERIENCE.md:128: the menu link is named «Meny, Mak»
- **Spine:** AD-13, line 209: «The view also carries the nickname as its own field so the settings can show it».
- **Fix:** «… as its own field, which the UI may show on its own (settings, the hub marker, the menu link's name), never inside a sentence».

### L5. The month summary's line items and dropped-activity notes aren't named as state

- **Source:**
  - EXPERIENCE.md:140: «each automatic transfer from savings (FR-45), last month's evenings with their cost (FR-53)»
  - EXPERIENCE.md:195: a dropped activity «gets a note card on the next month's opening»
  - EXPERIENCE.md:145: year-end notes for dropped activities
  - prd.md:607 (FR-12): everything processed is saved
- **Spine:** AD-9, line 168 stores month totals by class and part only. AD-5, line 124 has `action_log` store «the result part». Deferred, line 411 leaves the other state fields to engine stories.
- **Why it matters:** if these lines exist only in the continue response, a second device or a reload loses the dropped note and the transfer lines.
- **Fix (AD-13 or the Deferred row):** «The month summary's lines (automatic transfers, applied and dropped activities with their notes) are stored in the state when the month closes, and the view reads them from there, never from the action result.»

### L6. The spine's baseline date for the PRD is stale

- **Spine:** line 26: «The PRD (final, as it stands on 2026-11-15)». The frontmatter `updated` is 2026-11-23.
- **Source:** PRD memlog entries from 2026-11-16 to 2026-11-23 (nickname, OQ-12, #105, OQ-11, #111, #114, #115, #116).
- **Fix:** «The PRD (final, as it stands on 2026-11-23, after #105, #111, #114, #115 and #116)». Note in the memlog which of these the spine has absorbed (after this review's fixes).

### L7. «Future schedule data» vs the teasers, locked post-its and Året's «what unlocks»

- **Source:**
  - EXPERIENCE.md:83 (Året: «what unlocks»)
  - EXPERIENCE.md:163 (locked post-it shows «when it opens»)
  - EXPERIENCE.md:145 (teaser with price)
  - prd.md:648 (FR-15: «hints at an open boomerang pair»)
- **Spine:** AD-13, line 207: «It leaves out the seed, future schedule data, minigame solutions …».
- **Fix:** «Future schedule data means drawn or scheduled events, messages and draws not yet revealed. FR-18 unlock ages and prices, and FR-15's teaser text, are not schedule data and may be shown.»

### L8. UX loan terms differ from the PRD (UX or PRD should change)

- **Source:** EXPERIENCE.md:138: «three toggle buttons (12, 24, 36 months)». prd.md:998: «The term is 12, 24, 36, 48, or 60 months.»
- **Spine:** not affected, as long as the term is a validated parameter (M1).
- **Fix:** the UX adds 48 and 60, or the PRD narrows FR-25 to 12, 24 and 36. The content check and the NFR-7 refusals follow whichever is chosen.

### L9. Small source-side wording drift (PRD and UX should change, no spine change)

- prd.md:1357 (NFR-3) names only «the database host and any email relay» as processors. Spine AD-14 (line 235) and NFR-11 name Vercel and Railway. NFR-3 should say «the hosts (frontend and proxy, backend, database) and any email relay».
- EXPERIENCE.md:141: «the engine stores it once per account». Under AD-5 (line 124), the seen-disclosures record is a per-account table written outside the game pipeline, not engine state. The behaviour is the same, but the UX wording should say «the server stores it».

---

## Checked and consistent (no finding)

- **Unread marks (#112):** not stored, cleared in the open page only (EXPERIENCE.md:164). This matches FR-54 (prd.md:834) and addendum.md:23 («Nothing about reading messages is stored»). No AD-5 table or view state is needed. L3 only asks the view to carry the arrival month.
- **First-time disclosure «Forenklet» (D26 on the first plan):** tracked by the per-account `seen_disclosures` table (AD-5, line 124; ER diagram, line 335) and passed to `view(…, seen_disclosure_ids, …)` (AD-13, line 207). «Om tallene» with all 26 texts is the one content served outside the view (line 207). Survives a new life (FR-43, prd.md:1271).
- **New error states:**
  - password wrong → `403 wrong_password`
  - email in use → `409 email_in_use`
  - logged out elsewhere → `401 not_logged_in`
  - repeated failed logins → `401 login_failed` / `429 rate_limited`
  - reset link used → `410 reset_link_invalid`
  - updated on another device → `409 game_changed` / `plan_changed` / `wrong_month` / `already_chosen`
  
  All are in the AD-13 table (lines 216-224). Only the field-level 422 is missing (M4).
- **#111 bands:** AD-13, line 211 matches FR-33 (prd.md:1138), EXPERIENCE.md:153 and DESIGN.md:194: bad below the threshold, good from threshold + 10, stress mirrored, the usual stress and social life unbanded.
- **#116 calendar and money per month:** AD-13, lines 212-213 cover the timeline «November · 16 år · 2027», «i fjor», Året's twelve months with later months null, and the year end's expected BSU deduction.
- **#114:** AD-9, line 162 (`wage` includes one-off shifts) and line 168 (pay belongs to the month paid). Month 60 offers no shifts, which is an engine rule and needs no spine text. The rounding gap is M3.
- **Nickname (FR-1):** account field, one validation function, placeholder filled in by the view and never stored in state or the log (conventions line 283, AD-13 line 209, AD-15 line 264). The exceptions are M5 and L4.
- **OQ-12:** nothing in the spine assumes a confirm-email field. The email check is client-side.
- **Vercel:** AD-12 and AD-14 are amended (lines 189-199, 235).
- **Month plan protocol:** placing or removing a one-off shift is a month-plan change, so it raises `plan_version` (AD-4, line 90). Hours offers and quitting apply from the next month and don't touch the open plan.
- **Card switch, payment radios, ask for and answer hours, sell, spending level:** these are FR-45 money actions (prd.md:897-904), so they fall under NFR-7's «money action» category. Only their parameters are unnamed (M1).
- **Capability map coverage:** every FR-1 to FR-58 and NFR-3 to NFR-11 still has a row. NFR-1 and NFR-2 stay with the frontend (Deferred).
