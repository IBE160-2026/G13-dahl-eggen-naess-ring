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
  - mockups/index.html
---

# LifeMode — Experience Spine

> **Draft, 2026-11-22.** This describes how round 3 works (`mockups/index.html`, Ringer's layout in Speilet's style), built from the team's revisions in `../decisions.md`. It builds on saegg1205's shared spine (`ux-IBE160-G13-2026-11-17/EXPERIENCE.md`): the same 28 surfaces, states and journeys, with round 3's decisions on top. The group chose round 3 as the direction on 2026-11-22 (#95), took its job and shift rules into the PRD (#105), and decided that stress costs nothing extra during play (#106). The spine stays a draft until it is finalized. The PRD wins on product rules. This spine wins over the mockup.
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
- Hjem is home. Året, Hendelse, Resultat, the card warning, crisis and year end are reached from Hjem and count as Hjem in the navigation. Log in, sign-up, the gift, the recap and the ending have no tabs or rail.
- Sheets (interest, add an activity below 1100 px, menu) stack one level deep and never on top of each other.

| # | Surface | Route (round 3) | Reached from | Purpose (PRD) | Mocked |
|---|---|---|---|---|---|
| 01 | First screen | `#landing` | App open, logged out | Lag bruker / Logg inn (UJ-1) | yes |
| 02 | Create user | `#opprett` | 01 | Email once (shown back for checking), password, **nickname** with a live preview, stay logged in (FR-1, NFR-3) | yes |
| 03 | Log in | `#logginn` | 01 | Email, password, stay logged in (unticked), forgot password (FR-2, FR-5) | yes |
| 04 | Forgot password | `#glemt` | 03 | The same answer whether or not the email exists (FR-3) | yes |
| 05 | Life goal | `#start` | 02 | One of three goals (FR-9) | yes |
| 06 | Avatar | `#start` | 05 | Six preset looks; the choice recolours the mirror figure (FR-10) | yes |
| 07 | Pengegave and first choice | `#gave` | 06 | Random gift, first real choice (FR-11) | yes |
| 08 | Month hub and room | `#hjem` | Every month | Timeline, mirror with room layers and entries, this month's money, accounts, wellbeing, next month (FR-14, FR-34, FR-49) | yes |
| 09 | Message notification | toast on 08 | Over 08, below 1100 px | A new message slides in like an SMS | yes |
| 10 | Phone: messages | `#telefon` | Tab, sticker "2 nye", pane | Read-only inbox (FR-54) | yes |
| 11 | Phone: conversation | `#melding` | 10 | One thread; an invitation can go in the plan (FR-55) | yes |
| 12 | Event | `#hendelse` | Active months | Dimmed mirror, options as actions with kroner (FR-13) | yes |
| 13 | Result | `#resultat` | 12 | Chips, "Tidligere valg", "Hvorfor?", what changed | yes |
| 14 | "Hvorfor?" | inline on 13 | 13, money | Cause behind a change (FR-36, FR-38) | yes (inline) |
| 15 | Month plan | `#plan` | Tab, sticker "ledige kvelder" | Free evenings by tapping: activities and one-off shifts (FR-47, FR-52, FR-53) | yes |
| 16 | Job | `#jobb` | Tab, sticker "Jobb 14 t", pane | Job, wage, hours, offers, ask for more or fewer hours, one-off shifts, end extra shifts, quit (FR-47, FR-56) | yes |
| 17 | Money (bank) | `#penger` | Tab, accounts tile, pane | Accounts, interest, BSU, card, savings target and life goal, what comes next, buy and sell, spending, transactions (FR-9c, FR-22, FR-23, FR-26, FR-29, FR-45, FR-48, FR-57) | yes |
| 18 | Wellbeing | tile on 08 | 08 | Score with a status, three parts with a status, their consequences (FR-33) | yes (tile) |
| 19 | Year | `#aar` | The timeline, "Året ›" | Life bar, money per month, what unlocks | yes |
| 20 | Card warning | `#kort` | Age 18+, first month with card interest | Card debt in kroner, no scolding (FR-31) | yes |
| 21 | Crisis month | `#krise` | A trigger at month end | Up to three choices, always a way out (FR-32) | yes |
| 22 | Driving minigame | — | Licence purchase | Turn-based, no timing (FR-51). Waits for #51 | spine-only |
| 23 | Year end | `#aarsslutt` | December | Summary and teaser (FR-15) | yes |
| 24 | Welcome back | `#velkommen` | Login, or an hour away | Quick recap (FR-16, UJ-2) | yes |
| 25 | Ending | `#slutt`, `#slutt-hul`, `#slutt-ikke`, `#slutt-tap` | 20th birthday | Four endings, three choices that mattered (FR-41, FR-42, FR-43) | yes |
| 26 | Menu | `#meny` | Rail avatar, menu button on the scene | Nickname, password, information, new life, log out, delete user (FR-4, FR-5, FR-43, FR-44) | yes |
| 27 | About the numbers | `#tallene` | 26 | Disclosed simplifications (FR-40) | yes |
| 28 | Offline | `#offline` (state) | Any | Readable, options locked (FR-8) | yes |

→ Composition reference: `mockups/index.html` (open `#hjem`, `#plan`, `#aar`, `#penger`, `#jobb`). `mockups/oversikt.html` shows every surface and its states on one page. The spine wins on conflict.

**Room.** The PRD's room (FR-34) is the mirror scene. There is no separate room screen.

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
| «Snittet ditt er 61. Trivselsmålet er 50.» | «Du trenger 50», «Kravet var minst 50», «For å vinne …» |
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
| Room layers | One layer per belonging, set from flags, so the mirror looks the same after a reload and on every device. Three in version one: moped (none / owned), licence (none / moped / car) and phone (whole / cracked / used); the team may add up to three (FR-34, configuration). A layer changes in the same view as the choice that changed it: the result, or the hub when something is sold in the bank. The scene's text alternative names every belonging («Mopeden står utenfor vinduet, og hjelmen ligger på esken.»), and the change is announced and listed in the outcome list. |
| Next month (CTA) | One primary action per screen. A quiet month can be finished in one tap from 08 (principle 5). |
| Savings target | One option with a price, pinned in the bank (FR-57): progress from current account plus savings, the price, when it opens, and what's missing. «Bytt sparemål» opens a sheet; pinning moves no money. The life goal's progress is shown below it (FR-9c). Cleared with a note when the option is taken or given. |
| What comes next | Two closed rows in the bank: next month's known costs, and activity spend this year by kind (FR-57). In month 60 the first is empty. |
| Open options | In the bank, «Kan kjøpes eller selges» (FR-48): each open option with its price, «Mangler … kr» when short, the reason when blocked, or a lock with the age. Selling shows today's value and asks once in a sheet with what it changes (FR-29). |
| Credit card | From 18, in the bank (FR-26): balance, limit, how the bill is paid (whole, minimum or fixed), card use on/off, this month's interest in kroner and the cost of paying only the minimum. A consumer loan shows its monthly payment and total before it's taken (FR-25). `[NOTE FOR UX]` the 18+ bank isn't drawn; it reuses the account rows, radio cards and facts card. |
| Card warning | An event (FR-31): the facts first (debt, interest this month, time and cost at the minimum, and whether the player couldn't pay or chose to pay less), then the options that are possible. Shown before the next interest charge. |
| Crisis | Up to three linked choices (FR-32). Each step shows «Valg n av inntil 3», what is owed, and only options that are possible, each saying when it lands. Asking family and doing nothing are always offered, except that the family can't be asked twice in one crisis. It ends when no trigger is true, after the third step, or when the player ignores it. |
| Recap | After login or an hour away (FR-16): where they are, the current account, new messages this month, how much is planned, and a teaser with a price against what they have. One button continues. |
| Year end | The year's money, what changed, the average wellbeing, and a teaser for the next unlock (FR-15). Two buttons: continue, or «Ferdig for nå». Nothing locks the player out. |
| Ending | The outcome as a heading, one sentence, three facts (goal, average wellbeing with a status, debt), and up to three choices ranked by size in kroner (FR-42). Each opens to the «hvis du hadde valgt annerledes» line and a tip (FR-39). A hollow win includes the choice that hurt wellbeing most. One button: «Spill på nytt». After the ending, login lands here (FR-43). |
| Notification | Below 1100 px, a toast on Hjem when the month opens with a new message. It opens the conversation, closes with ×, and goes away by itself; the message stays in the inbox. A polite status message. On desktop the pane shows the inbox instead. |
| Menu | Nickname and password in sheets. Log out on all devices, start a new life and delete user ask for confirmation; delete asks for the password (FR-44). |
| Player information | On sign-up before the user is created, and in the menu (NFR-3): what is stored, why, how long, how to delete it, and which services handle it. The same text in both. |
| Money chip | Read-only, except an interest chip, which is a button that opens the interest sheet. |
| Interest (i) | Every interest amount (hub chip, savings account, transaction) opens the same sheet: what interest is, balance × rate = this month, and the BSU rate. The text comes from the engine. |
| Same as last month | «Samme som i oktober» in the plan places last month's activities on free evenings, each checked as a normal placement (FR-52). Hidden when there is nothing to place. |
| Wellbeing tile | The PRD's threshold is called «trivselsmål» to the player, next to «sparemål» and «livsmål»; the number comes from the engine, and exactly the number counts as reached. Shows the score, three parts, and at least one consequence the player can act on (evenings from free time; the average so far against the threshold once month 19 is calculated, FR-33). The score and each part also show how it is going, in a word with a status colour (good, warn, bad). The word is always there. The bands follow the wellbeing threshold in the PRD (50 by default, configuration): under it is bad, from it to 9 above is ok, 10 above and up is good. Stress is mirrored (100 − stress). The server sends the band with the figure. Stress and Sosialt show the month's value including the plan, with «Vanligvis n» under the bar when the two differ (FR-33). |
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
| Phone message | Read-only. An offer can carry a short tip (FR-19), as one sentence under the offer. An invitation has one action, "Legg i planen", plus "Nei takk". Grouped as «Nye i <måned>» and «Tidligere», so this month's messages stay marked as new all month (FR-54). The dot and the badge clear when a message is opened, in the open page only: nothing about reading is stored, and a reload shows them again (#112). |
| Sheet | Native `<dialog>`: focus moves in and returns, Esc closes, a scrim click closes. One level deep. |

## State Patterns

| State | Surface | Treatment |
|---|---|---|
| Saving | Any choice | Every option locks, the chosen one reads «Lagrer …», and it is announced. No result until the server confirms (FR-6). |
| Still trying | Any choice > 5 s | «Prøver fortsatt …», retries on reconnect, never applies a choice twice. It replaces «Lagrer …» in the same place. |
| Updated on another device | Any | The screen reloads with «Spillet ble oppdatert på en annen enhet.» (FR-8) |
| Server waking | First load | A loading message within 1 s, usable within 10 s (NFR-10). |
| Login failed | 03 | «Feil e-post eller passord.» for either, focus on the email. After repeated failures: «Prøv igjen om en stund, eller lag nytt passord.» (FR-2) |
| Reset link used or expired | 04 | Says so and offers a new one (FR-3). |
| Confirm before continuing | 08 | If the plan would set off a crisis trigger, continuing asks first (FR-49). |
| Minigame unfinished | 08, 22 | The player can't continue to the next month; the CTA names the game (FR-49, FR-51). |
| After the ending | 25 | The ending is read-only until a new life starts (FR-43). |
| Offline | Any | The screen stays readable, options and next month are locked, and a bar says «Ingen nett. Valgene venter til du er på nett igjen.» (FR-8). Announced. |
| Quiet month | 08 | The heading is "Denne måneden", the chips show wage, spending and interest. No event text. |
| Unread | 08, tabs, 10 | A coral dot on the sticker, a count badge on the Mobil tab/rail, bold rows in the inbox. "1 ny" / "2 nye". |
| Something new in an area | Tabs/rail | A bare coral dot on Plan (free evenings left) and Jobb (an unanswered offer). Screen-reader text: ", noe nytt". |
| Wellbeing status | 08 | Good, warn or bad, as a word plus a colour on the score and on each part. Score: «Det går bra» / «Helt ok» / «Tungt nå». Fritid and Sosialt: «bra» (60 and up) / «ok» (50–59) / «lite» (under 50). Stress: «lavt» (up to 40) / «middels» (41–50) / «høyt» (over 50). The score uses the same limits as Fritid. Under 50 matches the rules: a score under 50 heads for a hollow win (FR-41), free time under 50 raises stress and lowers social life (rule 12), and everyday stress stops rising at 50, so higher means a crisis or an event. |
| Offer open | 16 | The two ask buttons are disabled, with «Svar på tilbudet først.» |
| Hours request sent | 16 | The two buttons give way to «Du har spurt om flere timer. Line svarer i desember.» |
| Email check | 02 | After a valid form: «Sjekk at e-posten er riktig», the address, «Lag bruker» / «Endre e-post». Going back keeps what was typed. |
| Password too short | 02 | «Passordet må ha minst 8 tegn.», shown with the other errors at once; focus on the first. |
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

Version one has light mode only. Dark mode would need a night scene.

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
4. 07: gets 18 500 kr and chooses «Sett alt på sparekontoen». It reads «Lagrer …» until the server confirms.
5. **Climax:** 13 shows the money with a sign and a word, wellbeing revealed, and the mirror reflecting his mood, because of his own choice.
6. 08: months pass. Line at Butikken messages him (09–11), and he takes the job she offers (16).

Edge: the bus arrives mid-choice → the confirmed choice is kept (FR-6).

### Flow 2 — Back on a school PC (Markus, 15, four days later, bored in class) · UJ-2

1. 03: he logs in with email and password and leaves «Forbli innlogget» unticked.
2. 24: «Hei igjen, Mak. Alt er som da du gikk.» The recap shows the month, the current account, new messages and the plan.
3. **Climax:** the teaser names the licence and its price next to what he has. He sees how far it is.
4. 08: he continues in the same month.

Edge: he forgot the password → 04, same answer whether or not the email exists. He logs in on his phone later → the progress is there (FR-8). He forgets to log out → «Logg ut på alle enheter» (26).

### Flow 3 — November with extra shifts (Markus, 17, evening) · UJ-6

1. 08: November opens. The timeline marks November, «Denne måneden» shows +8 457 kr lønn, −6 593 kr brukt, +56 kr rente. The sticker says «2 nye».
2. 10–11: Emma invites him to a concert. He taps «Legg i planen», and it lands on Kveld 2.
3. 15: «3 frie kvelder · 1 ledig». The note says: «Du sa ja til ekstravakter i september. Derfor har du 3 frie kvelder i stedet for 4.» He adds «Hvilekveld» to Kveld 3.
4. 16: «Fra desember får du 4 frie kvelder i stedet for 3, men sitter igjen med 604 kr mindre i måneden.» He keeps the shifts, since they end after December.
5. **Climax:** he sees time and money traded in one sentence, and chooses.
6. 08: «Fortsett til desember».

Edge: he can't afford the concert → it shows the missing amount and can't be placed. He does nothing → the invitation runs out at the end of the month.

### Flow 4 — Interest grew (Markus, mid-game) · UJ-3

1. 10: Banken: «Tre fjerdedeler! Du har 79,8 % av Lappen.»
2. 17: he taps «+56 kr rente (i)» on the savings account.
3. **Climax:** the sheet shows 23 500 kr × 2,87 % = 56 kr this month, and «Jo mer du har der, og jo lenger, jo mer får du.»
4. 19: on Året, the blue interest strip shows it month by month.

Edge: he has nothing in savings → the hub shows no interest chip, and no bank message comes.

### Flow 5 — The phone breaks (Markus, 16, November event)

1. 08: «Fortsett» → 12: the mirror dims, the phone in his hand is cracked, and «Mobilen gikk i bakken» is written on the glass.
2. He picks «Reparer skjermen −2 500 kr».
3. **Climax:** 13: «Tidligere valg: I januar i fjor satte du pengegaven på sparekontoen. Den dekket de 136 kr du manglet.»
4. «Hvorfor?» splits the 2 500 kr into 2 364 kr from the current account and 136 kr from savings. The outcome list shows «Mobilen er hel igjen.» and «Sparemålet Lappen: 79,8 % → 72,1 %».

### Flow 6 — Asking for more hours (Markus, 18, paying down a card) · UJ-4

1. 20: card warning in kroner, no scolding.
2. 17: he moves from «Mye» down to «Vanlig» under «Hvor mye bruker du i måneden?». It shows that the change applies from next month.
3. 16: he taps «Spør om flere timer». Nothing changes yet.
4. 10–11, the next month: Line answers with 2 hours more a week. The offer says what it leaves after spending and how many free evenings he gets. He says Ja takk, and it applies from the month after.
5. 08: the wellbeing tile moves as his free time drops.
6. **Climax:** six months later the card is paid. He had fewer evenings with friends, and the wellbeing tile showed why.

Edge: missing the minimum twice starts a crisis month (21). «Spør mamma om hjelp» covers 500 of 700 kr, and the next choice is a payment plan or selling the moped, which then leaves the mirror.

### Flow 7 — Turning 20 (Markus) · UJ-5

1. 25: «Du klarte målet.» The mirror shows his room as it ended up, with the three facts and the three choices that mattered. He opens «Du brukte 15 000 kr av pengegaven»: «Hadde du valgt å spare alt, ville du hatt 17 270 kr mer da du fylte 20.» (FR-39)
2. **Climax:** he understands which choices shaped the ending.
3. «Spill på nytt» → 05: a new goal and a new pengegave (FR-43).

Edge: hollow win (goal reached, average under 50), goal not reached (never framed as failure) and loss (a trigger still true after month 60) each have their own heading and sentence.

## Coverage

- **Not UX surfaces:** FR-12, FR-17, FR-20, FR-21, FR-24, FR-46, FR-50 and FR-58 are engine, content or test rules. They reach the player through the surfaces above.
- **Spine-only:** 22 Driving minigame. It follows the event layout: one traffic situation, two to four answers, no timing, and the result on 13. It waits for #51.
- **FR-28 and FR-30 (licences):** bought as open options in the bank; the gift arrives as a message. Both change the licence layer.
- **FR-35 (what a choice opened or closed):** an extension in the PRD. Not drawn, after the team dropped «Åpnet/Stengt». The outcome list shows what changed.
- **FR-27 (family help):** appears as an option in events and crises, never as advice on its own.

## Open Questions

- **Unread marks (#112):** built as proposed; the group can still choose otherwise.
- **Player information:** the wording follows the architecture (AD-14). The frontend team owns the final text, and the 12-month deletion is named only if that job is built (NFR-3).
- **Unverified:** whether the stickers on the mirror read well at 320 px; test with players.
