---
title: LifeMode EXPERIENCE
status: candidate
created: 2026-11-17
updated: 2026-11-18
sources:
  - .docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md
  - PRODUCT.md
concepts:
  - konsepter/veien/EXPERIENCE.md
  - konsepter/blokka/EXPERIENCE.md
  - konsepter/speilet/EXPERIENCE.md
  - konsepter/basen/EXPERIENCE.md
---

# LifeMode — Shared Experience Spine

This spine holds everything the four candidate concepts (Veien, Blokka, Speilet and Basen) have in common: the same PRD, the same 28 surfaces, the same states, tone, accessibility floor and journeys. Each concept adds only its own delta in `konsepter/<concept>/EXPERIENCE.md` and its visual identity in `konsepter/<concept>/DESIGN.md`. The group picks one concept in issue #95; until then every file here has status `candidate`.

The PRD (`prd-IBE160-G13-2026-10-22/prd.md`, status final) is the fixed basis. Where this spine and the PRD disagree, the PRD wins. Where a concept spine and this shared spine disagree on something concept-specific (metaphor, layout, component behavior), the concept spine wins. On product rules, this spine wins.

## Foundation

- **Form factor:** web app in the browser, mobile-first, designed at 390 × 844 and adapting down to 320 CSS px wide and up to tablet and desktop (NFR-1). Not a PWA, no offline mode.
- **UI system:** none named. The frontend team picks the framework (architecture spine AD-12/AD-13). Each concept's `DESIGN.md` is its own visual system.
- **Server-authoritative:** every result is decided and saved by the server (FR-6 to FR-8). The frontend never calculates money and only renders finished Norwegian strings from the engine, plus UI chrome text.
- **Player-facing language:** Norwegian, plain enough for a 15-year-old (NFR-8). This spine is written in English; quoted UI strings are Norwegian.
- **Time:** shown as month name, age and "År N av 5". Never a running month number such as "måned 36".

## Information Architecture

The same 28 surfaces exist in all four concepts. The concept decides where on screen a surface lives and what it looks like, not whether it exists.

| # | Surface | Reached from | Purpose (PRD) |
|---|---|---|---|
| 01 | First screen | App open, logged out | Two choices: Logg inn / Opprett bruker (UJ-1) |
| 02 | Create user | 01 | Email, password, player information consent (FR-1, NFR-3) |
| 03 | Log in | 01 | Email, password, stay logged in, forgot password (FR-2) |
| 04 | Forgot password | 03 | Same answer whether or not the email exists (FR-3) |
| 05 | Choose life goal | After account creation | One of three goals (FR-9) |
| 06 | Choose avatar | 05 | Preset looks, no typed name (FR-10) |
| 07 | Pengegave and first choice | 06 | Random gift 10–30k, first real choice (FR-11) |
| 08 | Month hub | Every month | Month, age, money, wellbeing, the four areas, next month (5.4) |
| 09 | Message notification | Over 08 | New message arrives like a real SMS (5.6) |
| 10 | Phone: messages | 08 / 09 | Inbox, read-only (FR-54) |
| 11 | Phone: conversation | 10 | One thread; an invitation can be put in the plan (FR-55) |
| 12 | Story event | Active months (Jan, Apr, Jul, Oct) | Pre-written options as actions (5.4) |
| 13 | Result | After an option | What changed, now including wellbeing (FR-35, 5.12) |
| 14 | "Hvorfor?" | 13, money view, messages | Cause link behind a change (FR-36, FR-38) |
| 15 | Month plan | 08 | Activity slots by tapping, never dragging (5.5, FR-52, FR-53) |
| 16 | Job view | 08 | Job, wage, weekly hours, extra shifts (5.7, FR-47) |
| 17 | Money view | 08 | Accounts, BSU, card, goal progress, move money (5.8) |
| 18 | Room and wellbeing | 08 | Belongings (FR-34) and the three wellbeing parts (5.12) |
| 19 | Year line | 08 | År 1–5 and the months of each year |
| 20 | Card warning | Age 18+ | Card debt warning in kroner, no scolding (5.11) |
| 21 | Crisis month | Unpaid bills | Up to three steps, always a way out (FR-32) |
| 22 | Driving minigame | Licence purchase | Turn-based, no timing (FR-51) |
| 23 | Year end | December | Year summary and teaser for the next age unlock (FR-14) |
| 24 | Welcome back | Login after a break | Quick recap (UJ-2) |
| 25 | Ending | 20th birthday | Four endings, three choices that mattered (FR-41, FR-42) |
| 26 | Menu | From 08 | Account, player information, about the numbers, privacy, new life, log out, delete user (FR-43, FR-44) |
| 27 | About the numbers | 26 | Disclosed simplifications (FR-40) |
| 28 | Offline | Any surface | Readable, options locked (FR-8) |

Navigation rule: the month hub (08) is home. Every area surface returns to 08. Overlays (events, results, "Hvorfor?", phone) stack one level deep over the hub and never on top of each other.

## Voice and Tone

Microcopy. Brand voice lives in each concept's `DESIGN.md`.

| Do | Don't |
|---|---|
| «Kortregning 4 200 kr forfaller 20. mars.» (consequence in kroner) | «Du har brukt for mye!» (scolding) |
| «−1 200 kr · brukt på turen» (sign and word) | A red number with no sign or word |
| «Bli med på hytta» (an action) | «Riktig svar: spar pengene» (quiz framing) |
| «Hvile teller for trivselen.» | «Bortkastet tid» about free time |
| «Målet ble ikke nådd denne gangen.» | «Du tapte» for goal not reached |
| «Det finnes alltid en vei ut.» (crisis) | Panic language or countdowns |
| «Ingen nett. Valgene venter.» | «Error: network failure» |

Senders in the phone sound like the people sending them (Emma, Mamma, Butikken, Banken). Family can advise, never give personal financial advice. No alcohol or tobacco anywhere (NFR-8).

## Component Patterns

Behavioral, concept-neutral names. Each concept maps them to its own metaphor and visual spec.

| Component | Behavioral rules |
|---|---|
| Hub status | Always shows month, age, "År N av 5", money and wellbeing. Values come from the engine. |
| Year progress | Twelve months of the current year; played, current and coming months are distinguishable without color; months with a story event are marked. |
| Area entry points | One entry per game area (phone, month plan, job, money) plus room/wellbeing. Each shows its count or state as text ("2 nye", "2 ledige"). |
| Next month | One clear primary action. A quiet month can be finished in one tap (product principle 4). |
| Locked item | Shows what it is and the age it opens at ("fra 18 år"); never tappable as an option before it unlocks (FR-18). |
| Option | Reads as an action, shows its kroner effect with sign. Wellbeing effect is hidden until after the pick (5.12). Disabled with a reason when unaffordable. |
| Result | Money change with sign and word, wellbeing change now revealed, belongings/room change, a "Hvorfor?" entry and one primary continue. |
| "Hvorfor?" | Links the change to the choice behind it, using engine text only. |
| Activity slot | Empty or filled, state available as text; filled by tapping an activity, removed by tapping again. |
| Phone message | Read-only. An invitation carries one action: put it in the plan. |
| Notification | Slides in at the top like a real SMS; dismisses itself; announced politely to screen readers. |
| Sheet / dialog | Account and menu tasks; one level deep; closable. |

## State Patterns

| State | Surface | Treatment |
|---|---|---|
| Saving | Any choice | Options locked, a short saving state, no result until the server confirms (FR-6). |
| Still trying | Any choice > 5 s | «Prøver fortsatt …», retries on reconnect, never applies a choice twice. |
| Offline | Any | Screen stays readable, options and next month locked, text explains why (FR-8). Announced to screen readers. |
| Updated on another device | Any | Reloads latest progress with a short message (FR-8). |
| Server waking | First load | Loading message within 1 s, usable within 10 s (NFR-10). |
| Quiet month | 08 | Nothing to do is a valid state; next month is one tap. |
| Unaffordable option | 12, 15 | Shows the missing amount and stays unselectable (FR-53). |
| No free slot | 15 | Remove an activity first. |
| Locked by age | 08, 16, 17 | Locked item with the opening age; teaser names the next unlock. |
| Crisis | 21 | Up to three steps, each with a way out; never a dead end. |
| Ending | 25 | Real win, hollow win, goal not reached (never framed as failure), loss. |

## Interaction Primitives

- Tap or select to act. Every action also works with a keyboard (NFR-2).
- No dragging anywhere; the month plan is tap-to-place (WCAG 2.2, 2.5.7).
- No timing, motion or gestures required in minigames (FR-51).
- No real-time waiting, no timers, no countdowns.
- No chance-based rewards; random draws (the pengegave) are shown as a fact, not a prize.
- Touch targets at least 24 × 24 CSS px, options 44 × 44 where possible.
- Motion is decorative only and respects reduced motion.

## Accessibility Floor

Behavioral. Visual contrast lives in each concept's `DESIGN.md`; every concept's sketches are measured against WCAG 2.2 AA with its own `kontrast.py`.

- WCAG 2.2 AA across all surfaces (NFR-2).
- Every picture also exists as text: room states, belongings, the moped, echo badges, wellbeing parts, the year progress and the concept's metaphor objects.
- Nothing by color alone: money changes carry a sign and a word; locked, current and played states differ by shape or text too.
- Status messages ("saved", "offline", card warning) are announced; new messages are announced without interrupting.
- Login works with password managers and paste.
- The whole main flow, minigames included, is playable by keyboard alone; focus order follows reading order.
- Layout holds at 320 CSS px with no horizontal scrolling.

## Responsive & Platform

Mobile-first at 390 × 844. Down to 320 px the hub keeps status, year progress, area entries and next month visible; decorative scene parts shrink or crop first. On tablet and desktop the scene stays centered at phone proportions or widens its scene without moving controls away from their thumb-reachable order. No core function depends on hover.

## Key Flows

Journeys follow the PRD's protagonist, Markus. Concept spines describe how each step looks in their world.

### Flow 1 — First session (Markus, 15, on the bus, slightly irritated) · UJ-1

1. 01 → 02: creates a user with email and password.
2. 05: picks saving for something big (a flat of his own).
3. 06: picks a preset look.
4. 07: gets a pengegave and makes his first real choice.
5. **Climax:** 13 shows how money, wellbeing and belongings changed because of his own choice.
6. 08: months pass; a message from the shop (09–11) leads to a job (16).
7. 23: the year ends with a teaser for what opens at 16.

Edge: the bus arrives mid-choice → the confirmed choice is kept (FR-6).

### Flow 2 — Back on a school PC (Markus, four days later) · UJ-2

1. 03: logs in without "stay logged in".
2. 24: quick recap and a teaser naming the moped licence and its cost.
3. **Climax:** 08 / 17 shows what the licence costs compared with what he has.

### Flow 3 — Interest grew (Markus, mid-game) · UJ-3

1. 09–10: the bank says his savings grew.
2. **Climax:** 14 "Hvorfor?" links the growth to his earlier choice to save.

### Flow 4 — November with extra shifts (Markus, 17) · UJ-6

1. 08: November opens, two new messages, three slots instead of four.
2. 15: places the concert and friends, then a rest night.
3. 16: sees what the extra shifts cost in slots and give in kroner.
4. **Climax:** he feels that time is as scarce as money.

### Flow 5 — First credit card (Markus, 18) · UJ-4

1. 20: card warning in kroner, interest explained without scolding.
2. 17: moves spending down, raises hours in 16.
3. **Climax:** six months later the card is paid in full.

Edge: missing the minimum twice starts a crisis month (21).

### Flow 6 — Turning 20 (Markus) · UJ-5

1. 25: summary of the life, the three choices that mattered and their "if you had chosen differently" lines (FR-39).
2. **Climax:** he understands which choices shaped his ending.
3. 26: starts a new life with a new goal and pengegave (FR-43).
