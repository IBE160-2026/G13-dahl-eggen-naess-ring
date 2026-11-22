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
- **Hub:** the mirror selfie replaces the room. Both scenes are cut from Speilet's screens 08 and 13 and inlined in `index.html` as SVG (`#sc-selfie` and `#sc-glad`). The garland, post-its, status bar, goal-box labels and grain are removed.

## What changed, by the team's points
| Point | Change |
|---|---|
| Ringer + Speilet | Ringer's layout, Speilet's style. The mirror is the hub, and the phone and bank look like real apps (a phone frame on desktop, full-screen apps on mobile). |
| Drop the photos at the top | The photo garland is gone. The timeline is 12 named months with the current month in coral, plus "November · 16 år · 2027" and "Året ›". It is reused on Hjem, Plan, Hendelse and Resultat. |
| Forbruksnivå | It stays, but no screen says "forbruksnivå". The bank asks "Hvor mye bruker du i måneden?", and each of the three choices shows kroner, examples ("Matpakke, sjelden nye klær") and what it means ("Du sparer mer"). |
| Rente | Every interest amount is a button with an (i) icon (hub chip, savings account, transaction). It opens a sheet with what interest is and the calculation behind this month's amount. |
| "Ekko fra …" | Now "Tidligere valg", followed by a plain sentence: "Du sa ja til ekstravakter i september. Derfor har du én kveld mindre." |
| Trivsel | The parts are shown with their consequences: "Fritid 72 gir deg 3 kvelder. Snitt så langt 61, du trenger 50." See open questions. |
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

Wellbeing has its own status palette, used only on the wellbeing tile: good `#1F7A4D`, warn `#D99A00`, bad `#C2261E`. It passes the validator (CVD ΔE 17.2, normal-vision ΔE 25.0). The warn colour is only 2.45:1 on white, so every bar always has a word next to it ("ok") and the dot has an ink ring. A plain red/amber/green set (`#2E8540`, `#B26B00`, `#B3261E`) failed: protan ΔE 3.9.

## Diverges from the PRD (needs team decision)
- **FR-47 / UJ-5:** hours come as offers, and the player can ask for more. Today the player sets hours freely, and UJ-5 step 4 raises them from 10 to 12.
- **FR-52:** a one-off shift in the plan takes an evening slot. Today work never goes in slots.
- **FR-23:** the spending level is unchanged as a rule. Only the wording and the examples are new.

## Open questions
- **Trivsel in play:** per the PRD, the felt effects are fewer evenings (free time), the end score (hollow win), and the room or mirror. High stress has no effect during play beyond these. Should high stress also cost something now, such as an evening or a darker mirror and a tired face?
- **Dark mode:** not drawn. The Speilet scene is a lit room, so dark mode would need its own scene.
- **The mirror at 320 px:** the stickers overlap the reflection. That is the Speilet idea, but it should be tested.

## Invented figures (not in Rule Set v1)
- **Year chart, month by month:** income, spending and interest. The November figures follow UJ-6.
- **Spending examples and effects:** the example texts and "Du sparer mer". The amounts (60/75/95 % of 8 457 kr) follow rule 16.
- **Offers:** the extra-shift offer for January–March (ca. 2 414 kr) and "2 timer til" (ca. 1 207 kr).
- **One-off shifts:** fredag 558 kr (4 h) and varetelling 697 kr (5 h).
- **Wellbeing thresholds:** Fritid and Sosialt: ≥60 "bra", 40–59 "ok", <40 "lite". Stress: ≤35 "lavt" (good), 36–60 "middels", >60 "høyt". The score: ≥60 "Det går bra", 40–59 "Helt ok", <40 "Tungt nå". The engine should own these.
- **Phone event:** as in round 2 (2 500 / 1 800 / 0 kr).
- **Age:** UJ-6 is at 17, and it's shown at 16 as in round 2.

## Verified
Rendered at 320, 390 and 1280 px in headless Chrome. The Impeccable detector reported no findings.
