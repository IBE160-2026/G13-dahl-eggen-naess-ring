---
name: LifeMode – Basen
status: superseded
superseded_by: .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/ (final; direction chosen in issue #95)
created: 2026-11-18
updated: 2026-11-18
sources:
  - ../../../../prds/prd-IBE160-G13-2026-10-22/prd.md
  - ../../PRODUCT.md
  - ../../EXPERIENCE.md
  - ../../.memlog.md
sketches: ../../.working/basen/oversikt.html
---

# Basen — Experience Delta

## Foundation

Basen inherits the shared spine in full: surfaces, voice, states, primitives, accessibility floor and journeys (shared rules: [`../../EXPERIENCE.md`](../../EXPERIENCE.md)). This file holds only what is specific to the base camp. Visuals live in [`DESIGN.md`](DESIGN.md). The PRD wins over both.

The metaphor: your camp in the mountains is your base. The trail has one camp per year (År 1–5), the summit is your life goal, and your level is your age. Stations in the camp are the game areas. Events, accounts and areas open as game panels with a ribbon title over the dimmed camp. PRD adaptations kept from the memlog: belongings stand in the camp (FR-34, at most 6 layers), unlocks follow age only (FR-18), no new rooms or areas (Later), no real-time waiting, no chance rewards, no typed avatar name (FR-10).

## Metaphor Map

| # | Surface | Where it lives in the camp |
|---|---|---|
| 01 | First screen | Summer mountain with an empty camp; "LifeMode" over the peak, «Fem år. Én leir per år. Toppen er målet ditt.» |
| 02–04 | Create user, log in, forgot password | Gold-ribbon panels over the dimmed summer mountain |
| 05 | Life goal | Panel "Velg toppen din": the goal is the summit you climb toward |
| 06 | Avatar | Panel "Hvem er du?": six round portraits, the chosen one large with a gold ring; no name field |
| 07 | Pengegave | Panel "Pengegave!" with envelope and coins; amount shown as a fact, then three option cards |
| 08 | Month hub | The camp: HUD on top, scene with stations, bottom bar with next unlock and "NESTE MÅNED" |
| 09 | Notification | SMS banner slides over the camp |
| 10–11 | Phone | The phone from the radio mast, held over the dimmed camp |
| 12 | Story event | Red-ribbon panel; the sender (e.g. Emma) stands in the camp beside it |
| 13 | Result | Panel over the camp; the figure reacts, HUD pills show the new values, a memory card for what was added |
| 14 | "Hvorfor?" | Panel with step boxes joined by gold arrows |
| 15 | Month plan | "Kveldene i april": four slots around the campfire |
| 16 | Job view | Teal "Butikken" panel from the kiosk |
| 17 | Money view | "Lageret" panel from the depot: total, accounts, locked card, goal progress |
| 18 | Room and wellbeing | "Slik har du det" from the tent: three meters and the belongings in the camp |
| 19 | Year line | "Turen din": the whole mountain, one band per year with twelve month dots |
| 20 | Card warning | Camp at 18 with the car; bank banner; bottom bar swaps to "BETAL HELE" and "Betal minstebeløp" |
| 21 | Crisis month | Storm over the camp, fire out, figure tired; red panel "Storm i oktober" with steps and ways out |
| 22 | Driving minigame | Teal "Øvingskjøring" panel, crossing seen from above, three white answer buttons |
| 23 | Year end | Green panel "Leir 3 nådd!"; the trail reaches the next camp |
| 24 | Welcome back | Panel "Velkommen tilbake!" over the camp with a three-line recap |
| 25 | Ending | Winter summit, the whole trail gold, you by the flag; panel "Toppen er nådd!" |
| 26–27 | Menu, about the numbers | Panels over the dimmed camp |
| 28 | Offline | Camp stays visible; red ribbon "Ingen nett", grey next-month button |

## Component Patterns

Delta on the shared patterns.

| Component | Basen behavior |
|---|---|
| Area entry points | Each station is one control: bubble, building and ground tag share one target. Radio mast → 10, tent ("Hjem") → 18, campfire ("Kveldene") → 15, depot ("Penger") → 17, kiosk ("Jobb") → 16. |
| Wage at the kiosk | The engine has already paid the wage. The gold "+4 290 kr" chip is a reveal: one tap shows the figure and the money pill shows the engine's new total. It changes no value and never blocks next month. [ASSUMPTION] An untapped wage chip simply clears when the month ends. |
| Hub status | The level shield shows the age; "Nivå 16" always pairs with "16 år". Money and wellbeing pills update in place while a panel is open. |
| Year progress | HUD year track for the current year; the full five-year view (19) is the mountain. [ASSUMPTION] 19 opens from the trail or summit card on 08. |
| Locked item | A locked camp (dark flag, padlock, "År N") and the bottom bar teaser «Leir 4 åpner på nivå 18» with what opens. Never tappable as an option. |
| Panel | One at a time, over the dimmed scene; ribbon color tells the kind (gold neutral, red event or storm, teal job, green year end). Closing returns to 08. |
| Option | White card with icon and kroner value; caption «Trivselen ser du etter at du har valgt.» [ASSUMPTION] Unaffordable cards dim and show the missing amount; not sketched. |
| Result | The scene behind reacts: figure mood, belongings appear or vanish (the moped is sold, the car arrives at 18), a memory card names what was added. |
| Belongings | Stand next to the tent, one layer per belonging (FR-34), drawn from flags so every device shows the same camp. |
| Next month | Green gloss button. Advances the year-track chip; the season recolors sky and ground; in December the year-end panel moves you to the next camp. |
| Menu | [ASSUMPTION] Not drawn on 08. Needs an entry in the HUD (e.g. on the level shield or a small menu button) before build. |

## Interaction Primitives

- Tap a station to open its area; no hotspot hunting, every station has a visible ground tag.
- Hours in the job panel use − and + gloss buttons, never a slider or drag.
- Evenings: tap an activity card to fill the next free slot, tap a filled slot to empty it.
- The driving game is three white answer buttons per step, «Ingen klokke. Ta den tiden du trenger.»
- No base-builder mechanics: stations never upgrade, nothing is built or collected on a timer, no energy, no chests.
- Motion is decorative only (fire, rain, flag, figure cheering) and stops with reduced motion. [ASSUMPTION] Motion is not sketched; frames are static.

## State Patterns

| State | Basen rendering |
|---|---|
| Quiet month | Bottom bar hint «Neste måned venter. Ingen ting må gjøres først.» |
| Active month | The event panel opens over the camp when the month opens; next month follows the shared rule. [ASSUMPTION] The hint text changes to say a choice is waiting. |
| Offline | Scene dims slightly, station bubbles hide but tags stay, red ribbon «Ingen nett» / «Du kan se deg rundt. Valgene venter.», grey "NESTE MÅNED", hint «Valgene venter til du er på nett igjen.» |
| Crisis | Storm: cloud band, rain, lightning, fire out, tired figure. Panel "Storm i oktober" with «Steg 1 av 3. Det finnes alltid en vei ut.» The storm clears when the crisis ends. [ASSUMPTION] Clearing is not sketched. |
| Locked by age | Dark camp flag with padlock on the trail; padlock rows in panels («åpner på nivå 18»). |
| Year end | Green ribbon "Leir N nådd!", year summary rows, "TIL ÅR N". Sketch copy: «År 2 er ferdig. Hele årsbanen er fylt.» |
| Ending | Summit flag at 20 in winter. Only the real win is sketched. [ASSUMPTION] Other endings keep the summit scene and summit card with the true goal percent; "Målet ble ikke nådd denne gangen" is never framed as a fall or failure. |
| Saving | [ASSUMPTION] The chosen card stays pressed and the others dim until the server confirms; not sketched. |

## Accessibility

Shared floor applies. Metaphor-specific:

- **Scene text:** the camp region has one text summary, as in each sketch's description: season, current camp, stations with counts, belongings, goal percent.
- **Camps and trail:** each camp is text: «År 1, fullført», «År 2, du er her», «År 4, låst, åpner på nivå 18». The trail itself is decorative.
- **Stations:** accessible name = tag + state, e.g. «Mobil, 2 nye meldinger», «Kveldene, 2 ledige», «Jobb, lønn å hente». The whole station is the target, at least 44 × 44 px, since tags are only 22 px high.
- **Year track:** each chip reads as month + state, e.g. «April, nå, hendelse». Event dots are never the only signal.
- **Game text:** Lilita labels are live text with a CSS outline, never baked into images; in forced-colors mode the outline may drop, so the fill must stay system text color.
- **Figure, season and storm:** decorative. Mood, weather and season always have a text equivalent (wellbeing value, crisis panel text, month name).

## Key Flows

Shared flows: [`../../EXPERIENCE.md#key-flows`](../../EXPERIENCE.md#key-flows). Basen climaxes:

- **Flow 1 — First session (UJ-1):** the climax 13 shows the result panel while Markus cheers in the camp and the pills move to the new money and wellbeing. The year ends in 23 with the trail reaching the next camp and the bottom bar naming what opens next.
- **Flow 4 — November with extra shifts (UJ-6):** at the campfire (15) he sees three slots instead of four; the kiosk panel (16) shows hours and kroner side by side, so time and money sit in one camp.
- **Flow 6 — Turning 20 (UJ-5):** the trail turns gold to the summit and the flag stands at 20 (25); "SE HISTORIEN DIN" leads to the three choices that mattered, "Start et nytt liv" starts a new climb.

## Inspiration & Anti-patterns

- **Wanted:** the feel of a real mobile game: glossy 3D buttons, outlined chunky type, a level shield, a HUD with currency pills, ribbon panels. The user asked for it explicitly.
- **Rejected — the room seen from the front:** the first Basen draft was a room with one wall removed. It worked as a game look but resembled Speilet and Blokka too much, so the base became a camp in the mountains.
- **Rejected — base-builder loops:** collect timers, energy bars, speed-ups, loot boxes, upgrade levels on stations. Nothing in Basen waits in real time or pays out by chance (shared primitives).
- **Rejected — childish:** no mascots, no cartoon gags, no baby colors; the figures are teens with natural proportions.
