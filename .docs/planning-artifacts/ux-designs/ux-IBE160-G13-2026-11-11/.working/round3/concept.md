# Round 3: Ringer i Speilet-stil

Built 2026-11-22 from the team's round 3 revisions in `../../../../decisions.md` ("Nye revisjoner"). It's one improved draft, not a set of alternatives.

## Base
- **Layout and flow:** r2-b Ringer (round 2), including:
  - a rail, centre and right pane on desktop
  - a tab bar on mobile
  - the phone as its own pane
  - the same 12 routes
- **Visual style:** Speilet (saegg1205, `ux-IBE160-G13-2026-11-17/konsepter/speilet/DESIGN.md`):
  - sage wall, paper, ink, coral primary with an ink border
  - Bricolage Grotesque plus Kalam marker
  - stuck-on stickers, grain, and yellow post-its that mean locked only
- **Hub:** the mirror selfie replaces the room. Both scenes are cut from Speilet's screens 08 and 13 and inlined in `../../mockups/index.html` as SVG (`#sc-selfie` and `#sc-glad`). The garland, post-its, status bar, goal-box labels and grain are removed.

## What changed, by the team's points
| Point | Change |
|---|---|
| Ringer + Speilet | Ringer's layout, Speilet's style. The mirror is the hub, and the phone and bank look like real apps (a phone frame on desktop, full-screen apps on mobile). |
| Drop the photos at the top | The photo garland is gone. The timeline is 12 named months with the current month in coral, plus "November · 16 år · 2027" and "Året ›". It is reused on Hjem, Plan, Hendelse and Resultat. |
| Forbruksnivå | It stays, but no screen says "forbruksnivå". The bank asks "Hvor mye bruker du i måneden?", and each of the three choices shows kroner, examples ("Matpakke, sjelden nye klær") and what it means ("Du sparer mer"). |
| Rente | Every interest amount is a button with an (i) icon (hub chip, savings account, transaction). It opens a sheet with what interest is and the calculation behind this month's amount. |
| "Ekko fra …" | Now "Tidligere valg", followed by a plain sentence: "Du sa ja til ekstravakter i september. Derfor har du én kveld mindre." |
| Trivsel | The parts are shown with their consequences: "Fritid 72 gir deg 3 kvelder. Snitt så langt 61, du trenger 50." The wording is now "Snittet ditt er 61. Trivselsmålet er 50." |
| Less text | The "Stille måned" explanation, the CTA subline, the plan help text, the event footnote and the inbox filters are gone. |
| Plan, left pane | Same style as the right pane: one row per evening ("Kveld 1 · Kveld med venner · −200 kr", "Kveld 2 · Ledig [+ Legg til]"). School and work are one locked line, not hatched blocks. |
| "Plass 1/2/3" | Now "Kveld 1/2/3", and "3 ledige kvelder" on the hub. |
| "Trykk for å legge inn …" | Now "Legg til aktivitet", with Fritid and Jobb tabs. Jobb lists one-off shifts from the employer. On mobile it's a sheet. |
| Året | "Året så langt" is now "Pengene dine i år": a chart with income above the line (green) and spending below it (rust), each month tappable, and interest in its own strip (blue, its own scale). It also shows totals, a table view, and "Låses opp etter hvert" as post-its. |
| Jobb, "plasser" | "4 kvelder fra desember". |
| Jobb, free hours | The hours are fixed and can't be changed directly. There's an offer from the boss with Ja takk / Nei takk, and "Spør om flere timer", which gets an answer as a new offer. Ending the extra shifts and quitting stay. |

## Finpuss (2026-11-22)
| Point | Change |
|---|---|
| "4 kvelder fra desember" made little sense | Job texts are now whole sentences: "Fra desember får du én fri kveld mer i måneden, men 604 kr mindre i lønn." The offers say "Du tjener ca. 2 414 kr mer i måneden, men får én fri kveld mindre." The plan says "3 frie kvelder i stedet for 4". |
| Åpnet/Stengt | Removed. The result lists what changed, with an icon for better, worse or unchanged: "Mobilen er hel igjen.", "Sparemålet Lappen: 79,8 % → 72,1 %". |
| "Stille måned" | The heading is now "Denne måneden". |
| Mobil, jobb and bank looked different | On mobile they use the same canvas, white cards, round back button and chips as the rest. On desktop the phone frame stays (the team liked it there), and inside it the app looks like a real one. |
| The mirror selfie | It is now inline vector (SVG), not an image. Every colour is a CSS variable (`--sc-hoodie`, `--sc-skin`, `--sc-hair`, `--sc-wall` and so on), the figure and the reflection are named groups (`sc-selfie-figur`, `sc-selfie-speilbilde`), and the grain is removed, so it looks sharp. The scene is always shown whole (`meet`), not cropped by the screen. On tablet and desktop the mirror stands in the middle of a wide wall, with the stickers on the wall to the right. The jumper colour in "Hvordan ser du ut?" really changes the illustration. The original source is `speil.py` (saegg1205), which generates the shapes. |

## Palette check
The money colours are the same everywhere (chips, transactions, year chart): in `#1E8A6E`, out `#C2552D`, interest `#2B4CC4`. They pass the dataviz validator on white: CVD ΔE 10.0, normal-vision ΔE 23.2, contrast ≥ 3:1. They always come with a sign and a word, never colour alone.

Wellbeing has its own status palette, used only on the wellbeing tile: good `#1F7A4D`, warn `#D99A00`, bad `#C2261E`. Measured across all pairs on white: normal-vision ΔE 25.0, and green against red ΔE 7.6 for colour-blind players (deutan). That is just below the target of 8, so the word is required. (An earlier note said 17.2, which covered neighbouring colours only.) The warn colour is only 2.45:1 on white, so every bar always has a word next to it ("ok") and the dot has an ink ring. A plain red/amber/green set (`#2E8540`, `#B26B00`, `#B3261E`) failed: protan ΔE 3.9.

## Aligned with the PRD (2026-11-22)
#105 was decided and the PRD now has the rules, so the mockup was brought in line:
- **Wellbeing bands** follow the threshold of 50 (rule 12): under 50 bad, 50–59 ok, 60 and up good, stress mirrored.
- **Hours (FR-47):** the offer is the employer's answer to last month's request. It shows what is left after spending (302 kr) and free evenings as a number. The player can ask for more or fewer, one request at a time, answered next month. The old offer of new extra shifts is gone: they can't be offered while extra shifts run.
- **Extra shifts:** ending them shows 4 evenings instead of 3 and 604 kr less left, as in UJ-6.
- **One-off shifts (FR-47, FR-52):** no dates, no stress effect, not counted in the plan's total, and listed in the job view.
- **Sign-up (FR-1, #109):** one email field, shown back before the user is created.

## Completed (2026-11-22)
- **The mirror is the room (FR-34, per sarahnaess):** moped, licence and phone are layers in the scene. Selling the moped in the bank removes it. Try `#penger` on desktop.
- **Drawn:** 03, 04, 07, 09, 20, 21, 23, 24, 25 (four endings), 26, 27 and 28. 22 waits for #51.
- **Added:** savings target, life goal, next month's costs, activity spend and buy/sell in the bank; «Samme som i oktober»; «Vanligvis n» under stress and social; «Lagrer …»; the player information; password length; «Forbli innlogget» unticked by default (FR-5).
- **Corrected against the PRD:** the 250 kr in November is moped insurance, not activities; the unlock notes follow FR-18 (Øvelseskjøring and «BSU når du har inntekt» weren't in it).

## Open questions
- **Trivsel in play:** per the PRD, the felt effects are fewer evenings (free time), the end score (hollow win), and the room or mirror. High stress has no effect during play beyond these. The group decided on 2026-11-22 that it stays that way (#106).
- **Dark mode:** not drawn. The Speilet scene is a lit room, so dark mode would need its own scene.
- **The mirror at 320 px:** the stickers overlap the reflection. That is the Speilet idea, but it should be tested.

## Invented figures (not in Rule Set v1)
- **Year chart, month by month:** income, spending and interest. The November figures follow UJ-6.
- **Spending examples and effects:** the example texts and "Du sparer mer". The amounts (60/75/95 % of 8 457 kr) follow rule 16.
- **One-off shifts:** the names Kveldsvakt and Varetelling and their hours (4 and 5). The pay is hours × 139,40 kr.
- **Phone event:** as in round 2 (2 500 / 1 800 / 0 kr).
- **Gift:** 18 500 kr and the three choices. **Crisis:** 700 kr overdue, mother lends 500 kr, 939 kr a month for the payment plan (10 000 kr, 22,6 %, 12 months). **Endings:** all amounts except 17 270, 16 728 and 5 508. **Activity spend:** 3 150 kr. The moped's value follows rule 14 (11 645 kr, six months).
- **Age:** UJ-6 is at 17, and it's shown at 16 as in round 2.

## Verified
Rendered at 320, 390 and 1280 px in headless Chrome, with the job, plan and sign-up flows clicked through.
