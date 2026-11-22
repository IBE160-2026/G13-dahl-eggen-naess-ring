---
title: LifeMode EXPERIENCE
status: draft
created: 2026-11-11
updated: 2026-11-22
sources:
  - .docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md
  - PRODUCT.md
  - .docs/planning-artifacts/ux-designs/decisions.md
  - .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-17/EXPERIENCE.md
design: DESIGN.md
mockups:
  - .working/round3/index.html
---

# LifeMode — Experience Spine

> **Draft, 2026-11-22.** This describes how round 3 works (`.working/round3/index.html`, Ringer's layout in Speilet's style), built from the team's revisions in `../decisions.md`. It builds on saegg1205's shared spine (`ux-IBE160-G13-2026-11-17/EXPERIENCE.md`): the same 28 surfaces, states and journeys, with round 3's decisions on top. The group chose round 3 as the direction on 2026-11-22 (#95), took its job and shift rules into the PRD (#105), and decided that stress costs nothing extra during play (#106). The spine stays a draft until it is finalized. The PRD wins on product rules. This spine wins over the mockup.
>
> Tags: `[ASSUMPTION]` is a choice made without a team decision. `[NOTE FOR UX]` marks something the PRD asks for that isn't drawn yet.

## Foundation

- **Form factor:** a web app, mobile-first at 390 × 844, working from 320 CSS px up to tablet and desktop with no horizontal scroll (NFR-1). It is not a PWA and has no offline mode.
- **UI system:** none is named. The framework is the frontend team's choice (architecture AD-12/AD-13). `DESIGN.md` is the visual identity.
- **The server decides everything (FR-6–FR-8):**
  - The frontend never calculates or formats an amount.
  - Every figure and game sentence comes finished from the engine in Norwegian bokmål.
  - The frontend owns only UI text (labels, buttons, empty states).
- **Time:** shown as a month name, age and year ("November · 16 år · 2027"), never "måned X av 60" or "År N av 5".
- **The player's name:** the player picks a nickname at sign-up (PRD FR-1, PR #100). Game text uses it ("Hei Mak!"). Only the player sees it.

## Information Architecture

**Navigation.**
- Mobile: a tab bar with **Hjem · Plan · Mobil · Jobb · Penger**.
- Tablet and desktop: the same five items in a rail on the left.
- Desktop: a phone pane on the right that always shows Meldinger unless the player opened Melding, Penger or Jobb there.
- Hjem is home. Året, Hendelse and Resultat are reached from Hjem and count as Hjem in the navigation.
- Sheets (interest, add an activity below 1100 px, menu) stack one level deep and never on top of each other.

| # | Surface | Route (round 3) | Reached from | Purpose (PRD) | Mocked |
|---|---|---|---|---|---|
| 01 | First screen | `#landing` | App open, logged out | Lag bruker / Logg inn (UJ-1) | yes |
| 02 | Create user | `#opprett` | 01 | Email once (shown back for checking), password, **nickname** with a live preview, stay logged in (FR-1, NFR-3) | yes |
| 03 | Log in | — | 01 | Email, password, stay logged in, forgot password (FR-2) | spine-only |
| 04 | Forgot password | — | 03 | The same answer whether or not the email exists (FR-3) | spine-only |
| 05 | Life goal | `#start` | 02 | One of three goals (FR-9) | yes |
| 06 | Avatar | `#start` | 05 | Six preset looks; the choice recolours the mirror figure (FR-10) | yes |
| 07 | Pengegave and first choice | — | 06 | Random gift, first real choice (FR-11) | spine-only |
| 08 | Month hub | `#hjem` | Every month | Timeline, mirror with entries, this month's money, accounts, wellbeing, next month | yes |
| 09 | Message notification | — | Over 08 | A new message slides in like an SMS | spine-only |
| 10 | Phone: messages | `#telefon` | Tab, sticker "2 nye", pane | Read-only inbox (FR-54) | yes |
| 11 | Phone: conversation | `#melding` | 10 | One thread; an invitation can go in the plan (FR-55) | yes |
| 12 | Event | `#hendelse` | Active months | Dimmed mirror, options as actions with kroner | yes |
| 13 | Result | `#resultat` | 12 | Chips, "Tidligere valg", "Hvorfor?", what changed | yes |
| 14 | "Hvorfor?" | inline on 13 | 13, money | Cause behind a change (FR-36, FR-38) | yes (inline) |
| 15 | Month plan | `#plan` | Tab, sticker "ledige kvelder" | Free evenings by tapping: activities and one-off shifts (FR-47, FR-52, FR-53) | yes |
| 16 | Job | `#jobb` | Tab, sticker "Jobb 14 t", pane | Job, wage, hours, offers, ask for more or fewer hours, one-off shifts, end extra shifts, quit (FR-47, FR-56) | yes |
| 17 | Money (bank) | `#penger` | Tab, accounts tile, pane | Accounts, interest, BSU, card, goal, spending, transactions | yes |
| 18 | Wellbeing | tile on 08 | 08 | Score with a status, three parts with a status, their consequences (FR-33) | yes (tile) |
| 19 | Year | `#aar` | The timeline, "Året ›" | Life bar, money per month, what unlocks | yes |
| 20 | Card warning | — | Age 18+ | Card debt in kroner, no scolding (5.11) | spine-only |
| 21 | Crisis month | — | Unpaid bills | Up to three steps, always a way out (FR-32) | spine-only |
| 22 | Driving minigame | — | Licence purchase | Turn-based, no timing (FR-51) | spine-only |
| 23 | Year end | — | December | Summary and teaser (FR-14) | spine-only |
| 24 | Welcome back | — | Login after a break | Quick recap (UJ-2) | spine-only |
| 25 | Ending | — | 20th birthday | Four endings, three choices that mattered (FR-41, FR-42) | spine-only |
| 26 | Menu | — | Rail or avatar | Account, nickname, information, privacy, new life, log out, delete user (FR-43, FR-44) | spine-only |
| 27 | About the numbers | — | 26 | Disclosed simplifications (FR-40) | spine-only |
| 28 | Offline | — | Any | Readable, options locked (FR-8) | spine-only |

→ Composition reference: `.working/round3/index.html` (open `#hjem`, `#plan`, `#aar`, `#penger`, `#jobb`). The spine wins on conflict.

## Voice and Tone

UI microcopy. The brand voice is in `DESIGN.md` → Brand & Style. The team's rule is **no unnecessary text**: one sentence beats a paragraph, and a label beats a sentence.

| Do | Don't |
|---|---|
| «Denne måneden» | «Stille måned» |
| «Kveld 1», «3 frie kvelder · 2 ledige» | «Plass 1», «slots», «tar en kveld» |
| «Fra desember får du 4 frie kvelder i stedet for 3, men sitter igjen med 604 kr mindre i måneden.» | «4 plasser fra desember» |
| «Tidligere valg: Du sa ja til ekstravakter i september.» | «Ekko fra september» |
| «+56 kr rente (i)» → a sheet explains | A paragraph about interest on the screen |
| «Hvor mye bruker du i måneden?» Lite / Vanlig / Mye with kroner and examples | «Forbruksnivå: lav / normal / høy» |
| «68/100 · Det går bra», «25 lavt», «55 ok» | A colour with no word, or «Dårlig trivsel!» |
| «Velg i lista →» beside an always-visible list | A «Legg til» button that does nothing new |
| «Mobilen er hel igjen.» «Sparemålet Lappen: 79,8 % → 72,1 %» | «Åpnet» / «Stengt» |
| «−2 500 kr betalt» (sign and word) | A red number alone |
| «Legg til aktivitet» | «Trykk for å legge i en ledig plass» |
| «Du svarer med det du gjør, ikke med tekst.» | Explaining why messages can't be answered |

Senders sound like themselves (Emma, Mamma, Line at Butikken, Banken). There is no advice that reads as personal financial advice, and no alcohol or tobacco (NFR-8).

## Component Patterns

Behavioral. Visual specs are in `DESIGN.md` → Components.

| Component | Behavioral rules |
|---|---|
| Timeline | Shown at the top of 08, 12, 13 and 15. It is one link to Året. Past, current and coming months differ by fill and outline, not only colour. Its accessible name reads "November 2027, du er 16 år. Åpne året." |
| Mirror scene | `role="img"` with a text alternative that matches the scene state. Stickers on it are real links, each with count or state as text ("2 nye", "2 ledige kvelder", "Jobb 14 t"). The marker shows the nickname on the hub and the outcome on the result. |
| Next month (CTA) | One primary action per screen. A quiet month can be finished in one tap from 08 (principle 5). |
| Money chip | Read-only, except an interest chip, which is a button that opens the interest sheet. |
| Interest (i) | Every interest amount (hub chip, savings account, transaction) opens the same sheet: what interest is, balance × rate = this month, and the BSU rate. The text comes from the engine. |
| Wellbeing tile | Shows the score, three parts, and at least one consequence the player can act on (evenings from free time; the average so far against the threshold once month 19 is calculated, FR-33). The score and each part also show how it is going, in a word with a status colour (good, warn, bad). The word is always there. The bands follow the wellbeing threshold in the PRD (50 by default, configuration): under it is bad, from it to 9 above is ok, 10 above and up is good. Stress is mirrored (100 − stress). The server sends the band with the figure. |
| Slot row | Empty, below 1100 px → "+ Legg til" opens the add list for that evening. Empty, from 1100 px → no button; the row says «Velg i lista →» as plain text, since the list is already beside it. Filled → a × removes it, free, while the month is open (FR-53). School and work are one locked line. An empty evening has no effect (FR-52). |
| Add list | Fritid / Jobb tabs. Fritid lists activities with cost and effect. Jobb lists this month's one-off shifts with name, hours and pay, and needs a job (FR-47). A shift takes one evening, has no wellbeing effect of its own, and has no day or date (FR-52). A placed item shows a check. When there are no free evenings, the add buttons are disabled. From 1100 px: the right column, always visible, and a + places the item on the first free evening. Below 1100 px: a sheet titled with the evening, and a + places the item on that evening. The plan's total covers activity costs only, never wages (FR-52). |
| Past choice note | Shown when an earlier choice explains something now. One sentence naming the month and the choice. Replaces "Ekko" (FR-37 cause links). |
| Event option | An action plus signed kroner. The wellbeing effect is hidden until after the pick (5.12). The player picks by a tap or Enter. |
| Result | Chips (money, wellbeing), an optional past choice note, "Hvorfor?" (expands in place, `aria-expanded`), an outcome list, and one Fortsett. |
| Offer | From the employer in the phone and the job view: extra shifts, or the answer to an hours request. A question, one sentence of consequence, Ja takk / Nei takk. The sentence says what it leaves after spending each month and how many free evenings the new hours give next month (FR-47). It also warns when it would take free time below 50. It can be answered only in the month it arrives, then it shows as expired (FR-54, FR-55). Extra shifts are never offered while extra shifts run (FR-47). |
| Ask for hours | In the job view, for more or fewer hours, one request at a time (FR-47). The employer answers by message the next month: an offer of 2 h a week more or fewer, or a no with the reason at the limit or the floor. The player can't set hours directly. The job view also lists this month's one-off shifts; «Til planen» opens Plan with the Jobb tab chosen, and they are placed there (FR-56). |
| Spending choice | Three radio cards with kroner and examples. The current level is marked "Dette bruker du nå". A change shows "Gjelder fra desember" (FR-23). |
| Year chart | Each month is a button. The selection updates a three-figure detail (`role="status"`). The table view lists the same data. Coming months are inert. |
| Locked post-it | Shows what it is and when it opens; never tappable as an option before it unlocks (FR-18). |
| Phone message | Read-only. An invitation has one action, "Legg i planen", plus "Nei takk". Reading the message clears its unread dot and badge. |
| Sheet | Native `<dialog>`: focus moves in and returns, Esc closes, a scrim click closes. One level deep. |

## State Patterns

| State | Surface | Treatment |
|---|---|---|
| Saving | Any choice | Options locked and a short saving state. No result until the server confirms (FR-6). |
| Still trying | Any choice > 5 s | «Prøver fortsatt …», retries on reconnect, never applies a choice twice. `[NOTE FOR UX]` not drawn |
| Offline | Any | The screen stays readable, options and next month are locked, and the text says why (FR-8). Announced. `[NOTE FOR UX]` not drawn |
| Quiet month | 08 | The heading is "Denne måneden", the chips show wage, spending and interest. No event text. |
| Unread | 08, tabs, 10 | A coral dot on the sticker, a count badge on the Mobil tab/rail, bold rows in the inbox. "1 ny" / "2 nye". |
| Something new in an area | Tabs/rail | A bare coral dot on Plan (free evenings left) and Jobb (an unanswered offer). Screen-reader text: ", noe nytt". |
| Wellbeing status | 08 | Good, warn or bad, as a word plus a colour on the score and on each part. Score: «Det går bra» / «Helt ok» / «Tungt nå». Fritid and Sosialt: «bra» (60 and up) / «ok» (50–59) / «lite» (under 50). Stress: «lavt» (up to 40) / «middels» (41–50) / «høyt» (over 50). The score uses the same limits as Fritid. Under 50 matches the rules: a score under 50 heads for a hollow win (FR-41), free time under 50 raises stress and lowers social life (rule 12), and everyday stress stops rising at 50, so higher means a crisis or an event. |
| Offer open | 16 | The two ask buttons are disabled, with «Svar på tilbudet først.» |
| Hours request sent | 16 | The two buttons give way to «Du har spurt om flere timer. Line svarer i desember.» |
| Email check | 02 | After a valid form: «Sjekk at e-posten er riktig», the address, «Lag bruker» / «Endre e-post». Going back keeps what was typed. |
| Email invalid | 02 | A red border, «Skriv en hel e-postadresse, som navn@eksempel.no.», focus on the field, `aria-invalid`. |
| No free evening | 15, 11 | Add buttons disabled; the invitation says «Alle de frie kveldene er brukt.» Remove an activity first. |
| Can't afford | 12, 15 | Activities are paid from the current account, then savings (FR-45), so "Mangler … kr" appears only when both are short. It shows the missing amount and stays unselectable (FR-53). |
| Offer answered | 16 | The card keeps the question and shows «Du sa ja.» / «Du sa nei takk.» An offer left unanswered lapses at the end of the month and shows as expired (FR-47, FR-54). |
| Extra shifts ended | 16 | The button is disabled, reading "Avsluttet", and the job row says "Slutter nå". |
| Locked by age | 17, 19 | Post-it or lock row with the age. The year end teaser names the next unlock. |
| Nickname invalid | 02 | Under 2 characters → a red border, «Kallenavnet må ha minst 2 tegn.», focus returns to the field, `aria-invalid`. |
| Crisis | 21 | Up to three steps, each with a way out, never a dead end. |
| Ending | 25 | Real win, hollow win, goal not reached (never framed as failure), loss. |

## Interaction Primitives

- Tap or select to act. Everything works with a keyboard (NFR-2).
- No dragging anywhere. The plan is tap-to-place (WCAG 2.2, 2.5.7).
- No timers, countdowns or real-time waiting. Minigames have no timing or gestures (FR-51).
- No chance-based rewards. Random draws are stated as a fact.
- Targets are at least 24 × 24 CSS px, and 44 × 44 for options, round buttons and tabs.
- Motion: one authored moment (chips pop in on the result, the sheet slides up) and stickers straighten on hover. All motion is off under reduced motion.
- No core function depends on hover.

## Accessibility Floor

Behavioral. Contrast is measured in `DESIGN.md` → Colors.

- WCAG 2.2 AA on every surface (NFR-2).
- Every picture also exists as text: the mirror scene (state and mood), stickers, post-its, the year chart (labels per month plus the table) and wellbeing parts, including their status word (the coloured dot is hidden from screen readers).
- Nothing by colour alone: amounts have a sign and a word, wellbeing status has a word (green and red are close for some colour-blind players), timeline states differ by shape, outcome icons differ by glyph, locked has a lock icon and text.
- On route change, focus moves to the screen's heading. Status changes (an activity placed or removed, an offer answered, the spending changed) are announced through a polite live region.
- Badges include screen-reader text ("Mobil, 2 nye").
- Login works with password managers and paste. Email is typed once and shown back for checking before the user is created (FR-1, WCAG 3.3.7, #50).
- At 320 px the hub keeps the timeline, the scene stickers, this month and the CTA. Timeline labels drop to 11 px, and the scene shrinks; the stickers don't.

## Responsive & Platform

| Width | Behaviour |
|---|---|
| 320–767 | One column, a tab bar, a fixed CTA above the tab bar. The scene fills the width at 362:470. Phone, bank and job are full screens in the shared design with a round back button. "Legg til" opens a sheet. |
| 768–1099 | A rail plus one column. The scene is capped at 480 px tall, with the mirror centred on a wide wall. The CTA is sticky at the end. The plan is one column, and "Legg til" opens a sheet. |
| ≥ 1100 | Rail, centre and the phone pane in a device frame (real-app look: an app bar, a cobalt back link, flat rows). The mirror stands centred on a wide wall with the stickers to the right. The plan shows two columns with the add list always visible, and empty evenings have no button. Area routes open in the pane while the centre shows Hjem. |

There is no dark mode in this draft (`[ASSUMPTION]`: it needs a night scene).

## Inspiration & Anti-patterns

- **Lifted from Rommet (round 1, c6):** the room as the hub, held change on objects, and an event as a scene.
- **Lifted from Månedsfeed (round 1, c1):** a realistic phone inbox, message threads and bank view.
- **Lifted from Ringer (round 2):** the tab bar, rail and pane layout; stickers with counts; the result flow.
- **Lifted from Speilet (saegg1205):** the mirror selfie, stickers on the frame, handwriting on glass, yellow = locked.
- **Lifted from Riso-zine / Pixel-RPG (round 1):** a month bar across the top, with a detailed year view behind it.
- **Rejected:** a photo garland as the year (hard to read); "måned X av 60" (meaningless to the player); "Ekko", "plass", "forbruksnivå", "Åpnet/Stengt" (jargon); a phone frame on a phone (mobile).

## Key Flows

The protagonist is Markus, from the PRD. In the prototype his nickname is "Mak".

### Flow 1 — First session (Markus, 15, on the bus, slightly irritated) · UJ-1

1. 01: he taps «Lag bruker».
2. 02: email once (shown back for checking), password, and «Hva skal vi kalle deg?» → «Mak». Emma's preview bubble updates as he types.
3. 05–06: picks «Spare til noe stort» and a hoodie colour; the mirror figure changes colour.
4. 07: gets a pengegave and makes his first choice.
5. **Climax:** 13 shows the money with a sign and a word, wellbeing revealed, and the mirror reflecting his mood, because of his own choice.
6. 08: months pass. Line at Butikken messages him (09–11), and he takes the job she offers (16).

Edge: the bus arrives mid-choice → the confirmed choice is kept (FR-6).

### Flow 2 — November with extra shifts (Markus, 17, evening) · UJ-6

1. 08: November opens. The timeline marks November, «Denne måneden» shows +8 457 kr lønn, −6 593 kr brukt, +56 kr rente. The sticker says «2 nye».
2. 10–11: Emma invites him to a concert. He taps «Legg i planen», and it lands on Kveld 2.
3. 15: «3 frie kvelder · 1 ledig». The note says: «Du sa ja til ekstravakter i september. Derfor har du 3 frie kvelder i stedet for 4.» He adds «Hvilekveld» to Kveld 3.
4. 16: «Fra desember får du 4 frie kvelder i stedet for 3, men sitter igjen med 604 kr mindre i måneden.» He keeps the shifts, since they end after December.
5. **Climax:** he sees time and money traded in one sentence, and chooses.
6. 08: «Fortsett til desember».

### Flow 3 — Interest grew (Markus, mid-game) · UJ-3

1. 10: Banken: «Tre fjerdedeler! Du har 79,8 % av Lappen.»
2. 17: he taps «+56 kr rente (i)» on the savings account.
3. **Climax:** the sheet shows 23 500 kr × 2,87 % = 56 kr this month, and «Jo mer du har der, og jo lenger, jo mer får du.»
4. 19: on Året, the blue interest strip shows it month by month.

### Flow 4 — The phone breaks (Markus, 16, November event)

1. 08: «Fortsett» → 12: the mirror dims, and «Mobilen gikk i bakken» is written on the glass.
2. He picks «Reparer skjermen −2 500 kr».
3. **Climax:** 13: «Tidligere valg: I januar i fjor satte du pengegaven på sparekontoen. Den dekket de 136 kr du manglet.»
4. «Hvorfor?» splits the 2 500 kr into 2 364 kr from the current account and 136 kr from savings. The outcome list shows «Mobilen er hel igjen.» and «Sparemålet Lappen: 79,8 % → 72,1 %».

### Flow 5 — Asking for more hours (Markus, 18, paying down a card) · UJ-4

1. 20: card warning in kroner, no scolding.
2. 17: he moves from «Mye» down to «Vanlig» under «Hvor mye bruker du i måneden?». It shows that the change applies from next month.
3. 16: he taps «Spør om flere timer». Nothing changes yet.
4. 10–11, the next month: Line answers with 2 hours more a week. The offer says what it leaves after spending and how many free evenings he gets. He says Ja takk, and it applies from the month after.
5. 08: the wellbeing tile moves as his free time drops.
6. **Climax:** six months later the card is paid. He had fewer evenings with friends, and the wellbeing tile showed why.

Edge: missing the minimum twice starts a crisis month (21).

### Flow 6 — Turning 20 (Markus) · UJ-5

1. 25: a summary of his life, the three choices that mattered, and «if you had chosen differently» lines (FR-39).
2. **Climax:** he understands which choices shaped the ending.
3. 26: he starts a new life with a new goal and pengegave (FR-43).

## Open Questions

- **Usual and this month `[NOTE FOR UX]`:** FR-33 shows stress and social life both as the usual value and with this month's activities. The tile shows one value.
- **Same as last month `[NOTE FOR UX]`:** FR-52 has one action that places last month's activities again. It isn't drawn.
- **Unread marks:** FR-54 stores nothing about reading, and marks messages new only in the month they arrive. Proposal, waiting for the group: the dot and the badge clear when a message is opened, kept only in the open page and never stored, and they all clear when the month changes. A «Ny» tag stays on the month's messages. The mockup clears Emma's message this way. It has no «Ny» tag, and the bank's message doesn't clear.
- **Where the mockup is behind this spine:** the player information (NFR-3) isn't on the sign-up screen, and the password isn't checked for 8 characters.
- **Unverified:** whether the stickers on the mirror read well at 320 px; test with players.
