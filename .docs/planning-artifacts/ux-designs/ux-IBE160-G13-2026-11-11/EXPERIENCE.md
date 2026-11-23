---
title: LifeMode EXPERIENCE
status: final
created: 2026-11-11
updated: 2026-11-23
name: LifeMode
sources:
  - .docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md
  - PRODUCT.md
  - .docs/planning-artifacts/ux-designs/decisions.md
  - .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-17/EXPERIENCE.md
design: DESIGN.md
mockups:
  - mockups/index.html
  - mockups/oversikt.html
---

# LifeMode — Experience Spine

> **Final, 2026-11-23.** This describes how round 3 works (`mockups/index.html`, Ringer's layout in Speilet's style), built from the team's revisions in `../decisions.md`. It builds on saegg1205's shared spine (`ux-IBE160-G13-2026-11-17/EXPERIENCE.md`): the same 28 surfaces, states and journeys, with round 3's decisions on top. The group chose round 3 as the direction on 2026-11-22 (#95), took its job and shift rules into the PRD (#105), and decided that stress costs nothing extra during play (#106). On 2026-11-23 the group approved the last open UX decisions: the wellbeing bands (#111), unread marks (#112), one-off shift pay with next month's wage (#114) and FR-35 left out (#115). The spine is final. The PRD wins on product rules. This spine wins over the mockup.
>
> Every choice here is a team decision or a PRD rule. What waits on the PRD, architecture or rule set is listed under Open Questions.

## Foundation

- **Form factor:** a web app, mobile-first at 390 × 844, working from 320 CSS px up to tablet and desktop with no horizontal scroll (NFR-1). It is not a PWA and has no offline mode.
- **UI system:** none is named. The framework is the frontend team's choice (architecture AD-12/AD-13). `DESIGN.md` is the visual identity.
- **The server decides everything (FR-6–FR-8):**
  - The frontend never calculates or formats an amount.
  - Every figure and game sentence comes finished from the engine in Norwegian bokmål.
  - The frontend owns only UI text (labels, buttons, empty states).
- **Time:** shown as a month name, age and year ("November · 16 år · 2027"), never "måned X av 60" or "År N av 5".
- **The player's name:** the player picks a nickname at sign-up (PRD FR-1, PR #100). Game text uses it ("Hei Mak!"). Only the player sees it.
- **Words the player sees.** One word per concept, in every surface and in the engine's texts:

  | PRD term | Player sees |
  |---|---|
  | Activity slot | «fri kveld» (unit), «Kveld 1», state «planlagt» / «Tom» |
  | Activity / one-off shift | «aktivitet» / «vakt» |
  | Extra shifts | «ekstravakter» |
  | Echo badge | «Tidligere valg» |
  | Spending level low/normal/high | «Hvor mye bruker du i måneden?» Lite / Vanlig / Mye |
  | Threshold | «trivselsmålet» (never bare «målet») |
  | Life goal / savings target | «livsmålet» / «sparemålet» |
  | Car licence / moped licence | «Billappen» / «Mopedlappen» |
  | Money view | «Penger» (tab), «Banken» (screen title) |
  | Minimum payment | «det minste» with an (i) |
  | Payment plan | «Del opp hele kortgjelden» |
  | Disclosure | «Forenklet», then an (i) |
  | Rule 8 trigger status | «Ingen krise på vei» / «Krise i <måned> hvis du fortsetter nå» |
  | Card use on/off | «Bruk kortet» |
  | Device | «mobil eller PC», «overalt» |

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
| 08 | Month hub and room | `#hjem` | Every month, after its event if it has one | Timeline, mirror with room layers and entries, this month's money, accounts, wellbeing, next month (FR-14, FR-34, FR-49) | yes |
| 09 | Message notification | toast at the top of 08 | 08, below 1100 px | A new message, like an SMS | yes |
| 10 | Phone: messages | `#telefon` | Tab, sticker "2 nye", pane | Read-only inbox (FR-54) | yes |
| 11 | Phone: conversation | `#melding` | 10 | One thread; an invitation can go in the plan (FR-55) | yes |
| 12 | Event | `#hendelse` | Opens an active month, before its hub | Dimmed mirror, what the player has (current account, savings, debt, fixed costs), options as actions with kroner (FR-13) | yes |
| 13 | Result | `#resultat` | 12 | Chips, "Tidligere valg", "Hvorfor?", what changed | yes |
| 14 | "Hvorfor?" | inline on 13 | 13, money | Cause behind a change (FR-36, FR-38) | yes (inline) |
| 15 | Month plan | `#plan` | Tab, sticker «Planlegg n kvelder» | Free evenings by tapping: activities and one-off shifts (FR-47, FR-52, FR-53) | yes |
| 16 | Job | `#jobb` | Tab, sticker «Jobb 14 t i uka», pane | Job, wage, hours, the weekly limit, offers, ask for more or fewer hours, one-off shifts, end extra shifts, quit (FR-47, FR-56) | yes |
| 17 | Money (bank) | `#penger` | Tab, accounts tile, pane | Accounts, interest, BSU, card, savings target and life goal, what comes next, buy and sell, spending, transactions, the crisis check before continuing; from 18 the card, its payment and the consumer loan (`#penger~18`) (FR-9c, FR-22, FR-23, FR-25, FR-26, FR-29, FR-45, FR-48, FR-49, FR-57) | yes |
| 18 | Wellbeing | tile on 08 | 08 | Score with a status, three parts with a status, their consequences (FR-33) | yes (tile) |
| 19 | Year | `#aar` | The timeline, "Året ›" | Life bar, money per month, what unlocks | yes |
| 20 | Card warning | `#kort` | Age 18+, first month with card interest | Card debt in kroner, no scolding (FR-31) | yes |
| 21 | Crisis month | `#krise` | A trigger at month end | Up to three choices, always a way out (FR-32) | yes |
| 22 | Driving minigame | — | Licence purchase | Turn-based, no timing (FR-51). Waits for #51 | spine-only |
| 23 | December and year end | `#aarsslutt` | December opens | The year's money, the year's tax, what changed, notes for anything dropped, teaser (FR-15, FR-21, FR-49) | yes |
| 24 | Welcome back | `#velkommen` | Login, or an hour away | Quick recap (FR-16, UJ-2) | yes |
| 25 | Ending | `#slutt`, `#slutt-hul`, `#slutt-ikke`, `#slutt-tap` | 20th birthday | Four endings, three choices that mattered (FR-41, FR-42, FR-43) | yes |
| 26 | Menu | `#meny` | Avatar in the timeline (below 768 px), rail avatar | Nickname, password, information, new life, log out, delete user (FR-4, FR-5, FR-43, FR-44) | yes |
| 27 | About the numbers | `#tallene` | 26 | All 26 disclosed simplifications, grouped by theme (FR-40) | yes |
| 28 | Offline | `#offline` (state) | Any | Readable, options locked (FR-8) | yes |

→ Composition reference: `mockups/index.html` (open `#hjem`, `#plan`, `#aar`, `#penger`, `#jobb`). `mockups/oversikt.html` shows every surface and its states on one page. The spine wins on conflict.

**Room.** The PRD's room (FR-34) is the mirror scene. There is no separate room screen.

## Voice and Tone

UI microcopy. The brand voice is in `DESIGN.md` → Brand & Style. The team's rule is **no unnecessary text**: one sentence beats a paragraph, and a label beats a sentence.

| Do | Don't |
|---|---|
| «Denne måneden» | «Stille måned» |
| «Kveld 1», «3 frie kvelder · 1 planlagt», «Planlegg 2 kvelder» | «Plass 1», «slots», «tar en kveld», «2 ledige» (fri and ledig mean the same) |
| «I desember får du 4 frie kvelder i stedet for 3, og 604 kr mindre. Ekstravaktene slutter uansett etter desember.» | «4 plasser fra desember», or a monthly loss for something that lasts one month |
| «Tidligere valg: Du sa ja til ekstravakter i september.» | «Ekko fra september» |
| «+56 kr rente (i)» → a sheet explains | A paragraph about interest on the screen |
| «Hvor mye bruker du i måneden?» Lite / Vanlig / Mye with kroner and examples | «Forbruksnivå: lav / normal / høy» |
| «68/100 · Det går bra», «25 lavt», «55 ok» | A colour with no word, or «Dårlig trivsel!» |
| «Snittet ditt er 61. Trivselsmålet er 50.» | «Du trenger 50», «Kravet var minst 50», «For å vinne …» |
| «Velg i lista →» beside an always-visible list | A «Legg til» button that does nothing new |
| «Mobilen er hel igjen.» «Sparemålet Billappen: 79,8 % → 72,1 %» | «Åpnet» / «Stengt» |
| «Betaler du bare det minste (i)», «Del opp hele kortgjelden» | «Minstebeløp», «betalingsavtale» |
| «Ingen nett. Du kan se, men ikke velge, før du er på nett igjen.» | «Valgene venter» (sounds as if choices are queued) |
| «−2 500 kr betalt» (sign and word) | A red number alone |
| «Legg til aktivitet» | «Trykk for å legge i en ledig plass» |
| «Du svarer med det du gjør, ikke med tekst.» | Explaining why messages can't be answered |

Senders sound like themselves (Emma, Mamma, Line at Butikken, Banken). There is no advice that reads as personal financial advice, and no alcohol or tobacco (NFR-8).

## Component Patterns

Behavioral. Visual specs are in `DESIGN.md` → Components.

| Component | Behavioral rules |
|---|---|
| Timeline | Shown at the top of every in-game screen. «Året ›» and the month bar link to Året; the bar is a duplicate target, hidden from screen readers. «Året ›» is named «Året, november 2027, du er 16 år». Below 768 px it ends with the player's avatar, a link to the menu («Meny, Mak»), so the menu is reachable from every screen. Past, current and coming months differ by fill and outline, not only colour. |
| Scene | Only the artwork layer is `role="img"`, with a text alternative that matches the scene state and includes the marker text. Stickers are real links placed over it as siblings, never inside the image, each with count or state as text («2 nye», «Planlegg 2 kvelder», «Jobb 14 t i uka»; the first is named «2 nye meldinger»). The marker shows the nickname on the hub and the outcome on the result. |
| Room layers | One layer per belonging, set from flags, so the mirror looks the same after a reload and on every device. Three in version one: moped (none / owned), licence (none / moped / car) and phone (whole / cracked / used); the team may add up to three (FR-34, configuration). A layer changes in the same view as the choice that changed it: the result, or the hub when something is sold in the bank. The scene's text alternative names every belonging («Mopeden står utenfor vinduet, og hjelmen ligger på esken.»), and the change is announced and listed in the outcome list. |
| CTA button | One primary action per screen. A quiet month can be finished in one tap from 08 (principle 5). Continuing opens the next month: its event first if it is an active month, otherwise its hub (FR-49). |
| Event facts | Four small facts above the options: current account, savings, debt and fixed costs per month, engine figures (FR-13). |
| Outcome list | On results and crisis ends: one line per change, better (check), worse (arrow down) or unchanged (dash), in the order the engine sends them. Announced with the result. |
| Savings target | One option with a price, pinned in the bank (FR-57): progress from current account plus savings, the price, when it opens, and what's missing. Before continuing, progress counts the planned activities' payments and says so: «Etter planlagte aktiviteter», with the planned amount and the figure before the plan (FR-49, FR-57). The hub tile and the life goal are marked the same way. «Bytt sparemål» opens a sheet; pinning moves no money. The life goal's progress is shown below it (FR-9c). Cleared with a note when the option is taken or given. |
| What comes next | Two closed rows in the bank: next month's known costs, and activity spend this year by kind (FR-57). In month 60 the first is empty. |
| Open options | In the bank, «Kan kjøpes eller selges» (FR-48): each open option with its price, «Mangler … kr» when short, the reason when blocked, or a lock with the age. Selling shows today's value and asks once in a sheet with what it changes (FR-29). |
| Credit card | From 18, in the bank (FR-26, `#penger~18`): a card row in the account list, then a card section with what is used against the limit, the yearly rate and this month's interest in kroner. An overdue amount adds «Ikke betalt» and a «Betal … nå» button. «Bruk kortet» is a switch (`role="switch"`) that says where purchases go. «Slik betaler du kortregningen» is three radio cards: the whole bill (no interest), «det minste» (with how long and how much interest if only that is paid) and a fixed amount, which opens a stepper in 100 kr steps from the minimum up to the balance. A change applies from the next bill. The bills taken over at 18 (mobile, then the moped or the bus) show under What comes next (FR-23). |
| Consumer loan | In the bank from 18 (FR-25): what the player can borrow, and «Se hva et lån koster» opens a sheet. The term is three toggle buttons (12, 24, 36 months); the sheet shows the amount, the rate, the monthly payment, the last payment, the total and what the loan costs, all engine figures, before the loan is taken. In months 59–60 the row is locked with the reason (rule 6). |
| Crisis check | At the top of the bank before continuing (FR-49, rule 8): a status row with a dot and words, «Ingen krise på vei» or what would start a crisis month. When a trigger is true, the hub repeats the row above the CTA, and the CTA opens a confirm sheet with «Til banken» first and «Fortsett likevel» second. Month 59: a crisis in December is the last chance before the ending. Month 60: continuing with the trigger still true ends the game with debt (FR-41). Paying what is overdue turns the row to «Kortet er betalt». |
| Month summary | On 08 under the chips, «Hva gikk pengene til?», closed by default: everyday spending with example purchases that have no amounts of their own (FR-23, NFR-4), fixed costs, each automatic transfer from savings (FR-45), last month's evenings with their cost (FR-53), and when the player takes over the bills at 18 (FR-23, D23). |
| Disclosure (first time) | The first time a mechanism appears, a note card labelled «Forenklet» with the D-text and «Skjønner» sits under the screen's heading (FR-40), for example D26 on the first plan. After «Skjønner» it is gone on every device and playthrough (the engine stores it once per account), and focus moves to the (i) beside the heading, where the same text stays. «Om tallene» lists all 26, grouped by theme. |
| Card warning | An event (FR-31): the facts first (debt, the yearly rate, interest this month, time and cost if only «det minste» is paid, with an (i), and whether the player couldn't pay or chose to pay less), then the options that are possible. Shown before the next interest charge. |
| Crisis | Up to three linked choices (FR-32). Each step shows «Valg n av maks 3», what is owed, and only options that are possible, each saying when it lands. Asking family and doing nothing are always offered on every step (FR-32b). Asking family again in the same crisis shows the stored answer («Hun har allerede lånt deg 500 kr»), moves no money and uses no step (FR-27). It ends when no trigger is true, after the third step, or when the player ignores it; the end screen lists what changed. |
| Recap | After login or an hour away (FR-16): where they are, the current account, new messages this month, how much is planned, and a teaser with a price against what they have. One button continues. |
| Year end | December's summary: the year's money, the year's tax (or «0 kr» with why), the expected BSU deduction when there is a BSU, what changed, the average wellbeing against the trivselsmål, notes for planned activities that were dropped, and a teaser for the next unlock with its price (FR-15, FR-21, FR-49). Two buttons: continue, or «Ferdig for nå». Nothing locks the player out. |
| Ending | The outcome as a heading, one sentence, three facts (saved against the livsmål, average wellbeing against the trivselsmål with a status, debt), and up to three choices ranked by size in kroner (FR-42). Each opens to the «hvis du hadde valgt annerledes» line and a tip (FR-39). A hollow win includes the choice that hurt wellbeing most. Wages have a system cause and are never ranked (FR-36). One button: «Spill på nytt». After the ending, login lands here (FR-43). |
| Toast | Below 1100 px, a card at the top of Hjem, first in reading order, when the month opens with a new message. It opens the conversation and closes with × or Esc; focus then goes to «Denne måneden». It never closes by itself and never takes focus. Its arrival is announced once («Ny melding fra Emma.»). The message stays in the inbox. On desktop the pane shows the inbox instead. |
| Menu | Nickname and password in sheets. Log out on all devices, start a new life and delete user ask for confirmation; delete asks for the password (FR-44). |
| Info box (player information) | On sign-up before the user is created, and in the menu (NFR-3): what is stored, why, how long, how to delete it, and which services handle it. The same text in both. |
| Money chip | Read-only, except an interest chip, which is a button that opens the interest sheet. |
| Info button | A 24 px (i) next to a word or amount that needs a sentence: interest, the trivselsmål, «det minste», BSU. It opens a sheet. The interest sheet shows what interest is, then balance × yearly rate ÷ 12 = this month («23 500 kr × 2,87 % ÷ 12 = 56 kr»), a pointer to earning more (more hours, a summer job) and the BSU rate. The texts come from the engine. |
| Same as last month | «Samme kvelder som i oktober» in the plan places last month's activities on free evenings, each checked as a normal placement (FR-52). Hidden when there is nothing to place. |
| Wellbeing tile | The PRD's threshold is called «trivselsmål» to the player, next to «sparemål» and «livsmål»; the number comes from the engine, and exactly the number counts as reached. Shows the score, three parts, and at least one consequence the player can act on (evenings from free time; the average so far against the threshold once month 19 is calculated, FR-33). An (i) explains the trivselsmål. The score and each part also show how it is going, in a word with a status colour (good, warn, bad). The word is always there. This row is the canonical band rule: under the trivselsmål (50 by default, configuration) is bad, from it to 9 above is ok, 10 above and up is good; stress is mirrored (100 − stress). The band comes with the figure from the engine (#111, decided 2026-11-23). Stress and Sosialt show the month's value including the plan, with «Vanligvis n» under the bar when the two differ (FR-33). |
| Slot row | Empty rows read «Tom». Below 1100 px → "+ Legg til" opens the add list for that evening. Empty, from 1100 px → no button; the row says «Velg i lista →» as plain text, since the list is already beside it. Filled → a × removes it, free, while the month is open (FR-53). School and work are one locked line. An empty evening has no effect (FR-52). |
| Add list | Fritid / Jobb as two toggle buttons (`aria-pressed`) that filter one list. Fritid lists activities with cost and effect. Jobb lists this month's one-off shifts with name, hours and pay («558 kr lønn i desember»), and needs a job (FR-47). The pay comes with next month's wage, at its income step (#114, rule 1). A shift takes one evening, has no wellbeing effect of its own, and has no day or date (FR-52). A placed item shows a check. When there are no free evenings, the add buttons are locked and say why: «Alle de frie kveldene er fylt opp. Fjern en aktivitet først.» From 1100 px: the right column, always visible, and a + places the item on the first free evening. Below 1100 px: a sheet titled with the evening, and a + places the item on that evening. The plan's total («Aktivitetene koster») covers activity costs only, never wages (FR-52). |
| Past-choice note | Shown only when the engine has a cause link from an effect now to an earlier choice (FR-36, FR-37 echo badges), for example the extra shifts behind fewer evenings. One sentence naming the month and the choice. A payment topped up from savings is not a cause link; «Hvorfor?» explains it from the payment order instead (FR-45). |
| Event option | An action plus signed kroner. The wellbeing effect is hidden until after the pick (5.12). The player picks by a tap or Enter. |
| Result | Chips (money, wellbeing), an optional past-choice note, "Hvorfor?" (expands in place, `aria-expanded`), an outcome list, and one Fortsett. |
| Offer card | From the employer in the phone and the job view: extra shifts, or the answer to an hours request. A question, one sentence of consequence, Ja takk / Nei takk. The sentence says what it leaves after spending each month and how many free evenings the new hours give next month (FR-47). It also warns when it would take free time below 50. It can be answered only in the month it arrives, then it shows as expired (FR-54, FR-55). Extra shifts are never offered while extra shifts run (FR-47). |
| Ask for hours | In the job view, for more or fewer hours, one request at a time (FR-47). The employer answers by message the next month: an offer of 2 h a week more or fewer, or a no with the reason at the limit or the floor. The player can't set hours directly. The job view also lists this month's one-off shifts; «Til planen» opens Plan with the Jobb tab chosen, and they are placed there (FR-56). |
| Option radio card | Spending and life goal. Spending: three cards with kroner and examples. The current level is marked «Dette bruker du nå»; a change shows «Gjelder fra desember» and is announced (FR-23). Changing the radio never re-renders the group, so arrow keys keep working. |
| Year chart | Each month is a button. Under the chart, ‹ month › arrow buttons (44 px) step through the months; on narrow phones the month bars are under 24 px wide, and the arrows are the equivalent control (WCAG 2.5.8). The selection updates a three-figure detail (`role="status"`). The table view lists the same data. Coming months are inert. |
| Locked post-it | Shows what it is and when it opens; never tappable as an option before it unlocks (FR-18). |
| Message | Read-only. An offer can carry a short tip (FR-19), as one sentence under the offer. An invitation has one action, "Legg i planen", plus "Nei takk". Grouped as «Nye i <måned>» and «Tidligere», so this month's messages stay marked as new all month (FR-54). The dot (with an ink ring) and the badge clear when a message is opened, in the open page only: nothing about reading is stored, and a reload shows them again (#112, decided 2026-11-23). An invitation's «Nei takk» only closes it; nothing is sent. |
| Sheet | Native `<dialog>`: focus moves in and returns, Esc closes, a scrim click closes. One level deep. |

## State Patterns

| State | Surface | Treatment |
|---|---|---|
| Saving | Any choice | The chosen option reads «Lagrer …» and keeps focus; every option is locked (`aria-disabled`), and it is announced. No result until the server confirms (FR-6). |
| Still trying | Any choice > 5 s | «Prøver fortsatt …», retries on reconnect, never applies a choice twice. It replaces «Lagrer …» in the same place. |
| Updated on another device | Any | The screen reloads with «Spillet ble oppdatert på en annen enhet.» (FR-8) |
| Server waking | First load | A loading message within 1 s, usable within 10 s (NFR-10). |
| Login failed | 03 | «Feil e-post eller passord.» for either, focus on the email. After repeated failures: «Prøv igjen om en stund, eller lag nytt passord.» (FR-2) |
| Reset link used or expired | 04 | Says so and offers a new one (FR-3). |
| Confirm before continuing | 08, 17 | If a crisis trigger is true, the crisis check shows on the hub and in the bank, and the CTA asks first (FR-49). Month 59: «Krise i desember hvis du fortsetter nå … Desember er siste sjanse før slutten.» Month 60: «Spillet slutter med gjeld hvis du fortsetter nå», and «Fortsett likevel» leads to the loss ending. |
| Months 59–60 | 17 | The consumer loan is locked with the reason (rule 6). In month 60 next month's previews are empty (FR-49). |
| Minigame unfinished | 08, 22 | The player can't continue to the next month; the CTA names the game (FR-49, FR-51). |
| After the ending | 25 | The ending is read-only until a new life starts (FR-43). |
| Offline | Any | The screen stays readable, options and next month are locked (`aria-disabled`, described by the bar), and a bar says «Ingen nett. Du kan se, men ikke velge, før du er på nett igjen.» (FR-8). Announced once through the page's live region. |
| Logged out elsewhere | Any | After «Logg ut overalt», a password change or a reset elsewhere, the next action shows Log in with «Du ble logget ut. Logg inn igjen for å spille videre.» The game is unchanged (FR-5). |
| Quiet month | 08 | The heading is "Denne måneden", the chips show wage, spending and interest, and «Hva gikk pengene til?» opens the month summary. No event text. |
| Automatic transfer | 08 | The month summary has a line «Flyttet fra sparekontoen» with the amount and «Brukskontoen hadde ikke nok» (FR-45). |
| Unread | 08, tabs, 10 | A coral dot with an ink ring on the sticker, a count badge on the Mobil tab/rail, bold rows in the inbox. "1 ny" / "2 nye". |
| Something new in an area | Tabs/rail | A bare coral dot with an ink ring on Plan (free evenings left) and Jobb (an unanswered offer). Screen-reader text: ", noe nytt". |
| Wellbeing status | 08, 25 | The words, with the band rule in Component Patterns → Wellbeing tile. Score: «Det går bra» / «Helt ok» / «Tungt nå» (on the ending in past tense: «Det gikk bra» / «Helt ok» / «Tungt»). Fritid and Sosialt: «bra» / «ok» / «lite». Stress: «lavt» / «middels» / «høyt». Example at the default trivselsmål of 50: 60 and up is good, 50–59 ok, under 50 bad; stress up to 40 good. |
| Offer open | 16 | The two ask buttons stay focusable but locked (`aria-disabled`), described by «Svar på tilbudet først.» |
| Hours request sent | 16 | The two buttons give way to «Du har spurt om flere timer. Line svarer i desember.» |
| Email check | 02 | After a valid form: «Sjekk at e-posten er riktig», the address, «Lag bruker» / «Endre e-post». Going back keeps what was typed. |
| Password too short | 02 | «Passordet må ha minst 8 tegn.», shown with the other errors at once; focus on the first. |
| Email in use | 02 | After «Lag bruker», the form comes back with the email field marked: «Det finnes allerede en bruker med denne e-posten. Logg inn eller lag nytt passord.» with both as links; focus on the field (FR-1). |
| Email invalid | 02 | A red border, «Skriv en hel e-postadresse, som navn@eksempel.no.», focus on the field, `aria-invalid`. |
| No free evening | 15, 11 | Add buttons and «Legg i planen» are locked and described by «Alle de frie kveldene er fylt opp.» Remove an activity first. |
| Activity dropped | 23 or the next month's hub | A planned activity the engine drops when the month closes (no money, no longer eligible) gets a note card on the next month's opening: «Konserten med Emma ble ikke noe av. Du hadde ikke nok penger da november var over.» It is part of the summary, not an alert (FR-53, NFR-7). |
| Can't afford | 12, 15 | Activities are paid from the current account, then savings (FR-45), so "Mangler … kr" appears only when both are short. It shows the missing amount and stays unselectable (FR-53). |
| Offer answered | 16 | The card keeps the question and shows «Du sa ja.» / «Du sa nei takk.» An offer left unanswered lapses at the end of the month and shows as expired (FR-47, FR-54). |
| Extra shifts ended | 16 | The button is locked, reading «Avsluttet», and keeps focus. The job row says «Slutter etter november». |
| No job | 16, 15 | The job view shows the open job offers or when the next one opens (FR-56). The plan's Jobb filter says «Du har ingen jobb ennå.» |
| Locked by age | 17, 19 | Post-it or lock row with the age. The year end teaser names the next unlock. |
| Nickname invalid | 02, 26 | Under 2 characters → «Kallenavnet må ha minst 2 tegn.» Other characters than letters, digits, spaces and hyphens → «Bruk bare bokstaver, tall, mellomrom og bindestrek.» A red border, focus to the field, `aria-invalid`, the message linked. The same in the menu's sheet. |
| Password wrong | 26 | Change password and delete user: «Feil passord.» on the current-password field, focus there (FR-4, FR-44). |
| Crisis | 21 | Up to three steps, each with a way out, never a dead end. |
| Ending | 25 | Real win, hollow win, goal not reached (never framed as failure), loss. |

## Interaction Primitives

- Tap or select to act. Everything works with a keyboard (NFR-2).
- No dragging anywhere. The plan is tap-to-place (WCAG 2.2, 2.5.7).
- No timers, countdowns or real-time waiting, and nothing on screen disappears by itself. Minigames have no timing or gestures (FR-51).
- No chance-based rewards. Random draws are stated as a fact.
- Targets are at least 24 × 24 CSS px, and 44 × 44 for options, round buttons and tabs.
- Motion: one authored moment (chips pop in on the result, the sheet slides up) and stickers straighten on hover. All motion is off under reduced motion.
- No core function depends on hover.

## Accessibility Floor

Behavioral. Contrast is measured in `DESIGN.md` → Colors.

- WCAG 2.2 AA on every surface (NFR-2).
- Every picture also exists as text: the mirror scene (state and mood), stickers, post-its, the year chart (labels per month plus the table) and wellbeing parts, including their status word (the coloured dot is hidden from screen readers).
- Nothing by colour alone: amounts have a sign and a word, wellbeing status has a word (green and red are close for some colour-blind players), timeline states differ by shape, outcome icons differ by glyph, locked has a lock icon and text.
- **Scene structure:** only the artwork is an image; every link sits outside it (see Component Patterns → Scene).
- **Focus moves:**

  | After | Focus goes to |
  |---|---|
  | A route change | The screen's `h1`. On desktop pane routes, the pane's `h1`. Hjem has a visually hidden `h1` («Hjem, november»). |
  | Removing an activity | That evening's «Legg til», or the list's heading from 1100 px |
  | Placing an activity | The filled evening row |
  | Answering an offer | The answer («Du sa ja.») |
  | Asking for hours | The confirmation line |
  | Saving a choice | Stays on the chosen option |
  | Selling in the bank | The section heading |
  | Closing a sheet whose opener is gone | The nearest stable heading |
  | Closing the toast | «Denne måneden» |
  | «Skjønner» on a disclosure | The (i) beside the heading |
  | Paying what is overdue on the card | The crisis check row |
  | The card switch, the payment radios, the stepper, Året's arrows | Stay on the control |

  Nothing re-renders the control that has focus without restoring it.
- **Focus not obscured (2.4.11):** below 768 px the page scrolls focused content clear of the fixed CTA and tab bar (scroll padding of at least 150 px at the bottom); in the desktop pane, clear of the sticky app bar. Check by tabbing through every surface at 320 × 640.
- **Locked controls:** `aria-disabled="true"`, still focusable, with `aria-describedby` pointing at the reason. Never a bare `disabled` on something the player might try.
- **Live region:** one polite region exists from page load; status text is sent there, never injected together with a new region.
- **Document title:** «<screen> · LifeMode» on every route.
- **Account fields:** `autocomplete` email/username, current-password/new-password and nickname.
- Status changes (an activity placed or removed, an offer answered, the spending changed) are announced through the live region.
- Badges include screen-reader text ("Mobil, 2 nye").
- Login works with password managers and paste. Email is typed once and shown back for checking before the user is created (FR-1, WCAG 3.3.7, #50).
- At 320 px the hub keeps the timeline, the scene stickers, this month and the CTA. Timeline labels drop to 11 px, and the scene shrinks; the stickers don't.
- Coral dots that carry meaning have an ink ring (coral alone is 2.5:1).

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
7. 23: December opens with the year's money and a teaser for what opens next. He taps «Ferdig for nå».

Edge: the bus arrives mid-choice → the confirmed choice is kept (FR-6). The email is already in use → the form says so and links to Log in.

### Flow 2 — Back on a school PC (Markus, 15, four days later, bored in class) · UJ-2

1. 03: he logs in with email and password and leaves «Forbli innlogget» unticked.
2. 24: «Hei igjen, Mak. Alt er som da du gikk.» The recap shows the month, the current account, new messages and the plan.
3. **Climax:** the teaser names the licence and its price next to what he has. He sees how far it is.
4. 08: he continues in the same month.

Edge: he forgot the password → 04, same answer whether or not the email exists. He logs in on his phone later → the progress is there (FR-8). He forgets to log out → «Logg ut på alle enheter» (26).

### Flow 3 — November with extra shifts (Markus, 17, evening) · UJ-6

1. 08: November opens. The timeline marks November, «Denne måneden» shows +8 457 kr lønn, −6 593 kr brukt, +56 kr rente. The sticker says «2 nye».
2. 10–11: Emma invites him to a concert. He taps «Legg i planen», and it lands on Kveld 2.
3. 15: «3 frie kvelder · 2 planlagt». The note says: «Du sa ja til ekstravakter i september. Derfor har du 3 frie kvelder i stedet for 4.» He adds «Hvilekveld» to Kveld 3.
4. 16: «I desember får du 4 frie kvelder i stedet for 3, og 604 kr mindre. Ekstravaktene slutter uansett etter desember.» He keeps them.
5. **Climax:** he sees time and money traded in one sentence, and chooses.
6. 08: «Fortsett til desember» → 23 December opens.

Edge: he can't afford the concert → it shows the missing amount and can't be placed. He spends the money before continuing → the concert is dropped, and December opens with a note. He switches to the PC → it reloads before he can continue (FR-49). He does nothing → the invitation runs out at the end of the month.

### Flow 4 — Interest grew (Markus, mid-game) · UJ-3

1. 10: Banken: «Sparepengene dine har tjent over 50 kr i rente.» (FR-55)
2. 17: he taps «Hvorfor?» on the interest line.
3. **Climax:** it links the interest to his own choice: «I januar i fjor satte du pengegaven på sparekontoen.» The interest sheet shows 23 500 kr × 2,87 % ÷ 12 = 56 kr this month.
4. The sheet points on: «Vil du ha mer? Spar mer, eller tjen mer med flere timer eller sommerjobb.»
5. 19: on Året, the blue interest strip shows it month by month.

Edge: he has nothing in savings → the hub shows no interest chip, and no bank message comes.

### Flow 5 — The phone breaks (Markus, 16, October event) · FR-13, FR-34, FR-38

1. October opens with an event, before the hub. 12: the mirror dims, the phone in his hand is cracked, «Mobilen gikk i bakken» is written on the glass, and the facts show what he has.
2. He picks «Reparer skjermen −2 500 kr». It reads «Lagrer …».
3. 13: the phone in the mirror is whole again.
4. **Climax:** «Hvorfor?» splits the 2 500 kr: 2 364 kr from the current account, and the rest from the savings he built up. The outcome list shows «Mobilen er hel igjen.» and «Sparemålet Billappen: 79,8 % → 72,1 %».
5. «Fortsett» → October's hub.

Edge: he can't afford any paid option → the free one («Lev med sprekkene 0 kr») is always there (FR-45). He goes offline mid-choice → «Prøver fortsatt …», and the choice is applied once.

### Flow 6 — Asking for more hours (Markus, 18, paying down a card) · UJ-4

1. 20: card warning in kroner, no scolding: 10 000 kr, 22,6 % a year, and 51 months if he pays only «det minste».
2. He picks «Skru av kortet».
3. 17: he moves from «Mye» down to «Vanlig» under «Hvor mye bruker du i måneden?». It shows that the change applies from next month.
4. 16: he taps «Spør om flere timer». Nothing changes yet.
5. 17: under «Kan kjøpes eller selges» he sees what the moped is worth now. It wouldn't cover the debt, so he keeps it.
6. 10–11, the next month: Line answers with 2 hours more a week. The offer says what it leaves after spending and how many free evenings he gets. He says Ja takk, and it applies from the month after.
7. 08: the wellbeing tile moves as his free time drops.
8. **Climax:** he realises he must work more and spend less for the next six months, and sees it cost him evenings with friends.
9. Six months later the card is paid.

Edge: missing the minimum twice starts a crisis month (21). «Spør mamma om hjelp» covers 500 of 700 kr, and the next choice is «Del opp hele kortgjelden» or selling the moped, which then leaves the mirror.

### Flow 7 — Turning 20 (Markus) · UJ-5

1. 25: «Du klarte målet.» The mirror shows his room as it ended up, with the three facts and the three choices that mattered. He opens «Konserter og arrangementer»: «Hadde du droppet dem, ville du hatt 10 210 kr mer da du fylte 20. De ga deg også mer sosialt liv.» (FR-39)
2. **Climax:** he understands which choices shaped the ending.
3. «Spill på nytt» → 05: a new goal and a new pengegave (FR-43).

Edge: hollow win (goal reached, average under 50), goal not reached (never framed as failure) and loss (a trigger still true after month 60) each have their own heading and sentence.

## Coverage

- **Not UX surfaces:** FR-12, FR-17, FR-20, FR-21, FR-24, FR-46, FR-50 and FR-58 are engine, content or test rules. They reach the player through the surfaces above.
- **Spine-only:** 22 Driving minigame. It follows the event layout: one traffic situation, two to four answers, no timing, and the result on 13. It waits for #51.
- **FR-28 and FR-30 (licences):** bought as open options in the bank; the gift arrives as a message. Both change the licence layer.
- **FR-35 (what a choice opened or closed):** left out of the MVP by the team on 2026-11-23 (#115), under its «If left out» clause. Flags still drive follow-ups, unlocks and the room; the outcome list shows what changed.
- **FR-27 (family help):** appears as an option in events and crises, never as advice on its own.
- **FR-24 vs the phone event:** the broken phone in Flow 5 is a story event (FR-17). An FR-24 unexpected expense arrives as a deduction with a «Hvorfor?» system cause, not as an event.

## Open Questions

- **Decided 2026-11-23:** the wellbeing bands as built (#111), unread marks as built (#112), one-off shift pay with next month's wage (#114), and FR-35 left out (#115).
- **For the PRD, architecture and rule set (they don't change the screens):**
  - The PRD texts for #111, #114 and #115 (FR-33, FR-47, FR-35).
  - A start year for «2027» in the timeline, the year's monthly totals for Året, and the wellbeing band are not in the player view yet (#116, AD-13).
  - D12, D25 and D26 still say the player sets hours, «forbruksnivå» and «plasser» (#117). The prototype shows the proposed wording on «Om tallene» and in the first-plan disclosure.
- **Driving minigame (#51):** surface 22 is spine-only until the team decides.
- **Player information:** the wording follows the architecture (AD-14). The frontend team owns the final text, and the 12-month deletion is named only if that job is built (NFR-3).
- **Unverified:** whether the stickers on the mirror read well at 320 px; test with players.
