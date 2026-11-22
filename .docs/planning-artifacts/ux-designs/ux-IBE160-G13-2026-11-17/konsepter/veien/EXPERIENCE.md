---
name: LifeMode · Veien — Experience delta
status: candidate
created: 2026-11-17
updated: 2026-11-18
sources:
  - .docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md
  - ../../PRODUCT.md
  - ../../EXPERIENCE.md
  - ../../.memlog.md
sketches: ../../.working/veien/oversikt.html
---

# Veien — Experience Delta

## Foundation

Veien inherits everything in the shared spine (`../../EXPERIENCE.md`): the 28 surfaces, voice, states, interaction primitives, accessibility floor and key flows. This file holds only what Veien does differently: the world is a level map in perspective where the player walks a road through the year, months are milestones, the age is the level, New Year is a gate, and savings goals are flags. Visual specs live in `DESIGN.md`. Shared rules: `../../EXPERIENCE.md`. The PRD wins over both.

## Metaphor Map

| # | Surface | Where it lives in Veien |
|---|---|---|
| 01 | First screen | Full road scene; the player and Emma stand on the road under the "LifeMode" logo |
| 02–04 | Create user, log in, forgot password | Sky band on top, dark sheet below; the world stays visible |
| 05 | Life goal | Three goal cards on the sheet; the chosen goal later appears as a flag/line in 17 |
| 06 | Avatar | Six full-body preset looks; "Du er 15 år og står ved starten av veien." |
| 07 | Pengegave | First dialog on the road: Mamma's portrait, a gift box with a burst, a floating "+18 400 kr" |
| 08 | Month hub | The road: past milestone behind, coming milestone ahead, gate and flag further up, player in the middle, HUD on top, game dock with GÅ at the bottom |
| 09 | Notification | Real SMS banner slides over the hub |
| 10–11 | Phone | Leaves the world entirely for a real messaging app; "‹ Spill" returns |
| 12 | Story event | The sender waits on the road with a speech bubble; the event is a dialog box sliding up from the bottom |
| 13 | Result | A lime side path branches off to the destination (lit cabin); numbers float over the figures; result dialog below |
| 14 | "Hvorfor?" | Sheet over the dimmed result |
| 15–17 | Plan, job, money | Dock destinations; sky band + sheet |
| 18 | Room and wellbeing | Illustrated room on the sheet; reached from the menu |
| 19 | Year line | The road drawn straight and vertical, one stop per month; year tabs År 1–5 (15–19 år) |
| 20–21 | Card warning, crisis | The road at night: no sun, pink tint, pink-bordered dialog |
| 22 | Driving minigame | Top-down crossing; the moped in road turquoise |
| 23 | Year end | The camera reaches the gate; lime burst; "START ÅR N" crosses it |
| 24 | Welcome back | Card over the dimmed hub with a portrait and the year strip |
| 25 | Ending | Trophy in the sky band; no road (the journey is over) |
| 26–27 | Menu, about the numbers | Sky band + sheet, opened from the HUD menu button |
| 28 | Offline | White banner over the current scene; options greyed |

## Component Patterns

Behavioral delta only.

| Component | Veien behavior |
|---|---|
| Hub status | Age is shown as a level badge, not as text alone; the accessible name still reads "17 år". |
| Year progress | Two forms: the compact HUD strip (current year) and the full year line (19). The road only shows the previous and next milestone; the full year is never squeezed onto the road. |
| Area entry points | Dock order is fixed: Plan, Jobb, GÅ, Mobil, Penger. Badges show numbers only ("3", "2"); the accessible name carries the text ("3 ledige kvelder", "2 nye meldinger"). Room and year line live in the menu. [ASSUMPTION] Tapping the wellbeing chip also opens 18 and tapping the year strip opens 19. |
| Next month | GÅ always names its target ("til desember"). In December the caption names the gate. [ASSUMPTION] exact December caption. |
| Locked item | The gate announces the next level and what opens there; individual locked things follow the shared rule. |
| Option | Options never sit in the scene; they are always in a dialog. |
| Result | Floating tags in the scene repeat the dialog values; the dialog is the source of truth. |
| Phone message | The phone is deliberately non-game styled so the SMS feels real; only the invitation card inside a thread uses game styling. |
| Scene objects | Road, milestones, gate, flag and figures are display, not controls. [ASSUMPTION] Tapping the flag may open 17; not drawn. |

## Interaction Primitives

- GÅ is the one-tap way through a quiet month (shared principle 4), placed at the bottom center for the thumb.
- Every pressable thing has a visible depth layer; pressing flattens it. [ASSUMPTION] press animation, skipped under reduced motion.
- [ASSUMPTION] After GÅ the player figure walks to the next milestone (decorative only, skipped under reduced motion; the next month's content appears without waiting).
- Dialogs slide up over the scene and never cover the HUD.

## State Patterns

| State | Veien rendering |
|---|---|
| Offline (28) | White banner "Du er frakoblet" / "Valgene låses opp når nettet er tilbake." over the scene; options at 40 % opacity. The shared voice line «Ingen nett. Valgene venter.» stays the reference copy. |
| Locked by age | The gate ahead on the road ("NIVÅ 18 · JANUAR"); the year-end teaser names what opens. |
| Card warning / crisis | The sun is gone and the scene is tinted pink; crisis shows a "STEG 1 AV 3" pill. The road is still there: there is always a way on. |
| Event waiting | HUD subline "noen venter på veien". |
| Quiet month | Hub with no dialog; GÅ is the only lime element. |

## Accessibility Notes

- **Road:** decorative; the hub's text alternative is the HUD ("November · 17 år · År 3 av 5").
- **Milestones:** each plate is text ("OKT", "DES"); played vs coming also differs by plate fill and lamp. Screen readers get full month names. [ASSUMPTION] text alternative format, e.g. "Oktober, spilt".
- **Gate:** read as text, e.g. "Neste nivå: 18 år i januar".
- **Flag:** read as "Sparemål: Førerkort, 75 % spart".
- **Year strip:** read by month name, never by month number, e.g. "November, år 3 av 5. Januar til oktober spilt." Event months are marked by size, not color, and announced as "med hendelse".
- **Floating tags:** decorative duplicates of the result dialog; hidden from screen readers.
- **Avatars and portraits:** labeled by role ("Emma", "Mamma", "Du").
- **Phone screens:** the light phone palette is measured separately in `kontrast.py` (all pass).

## Key Flows

Flows follow the shared spine; only the visual climax is Veien-specific.

- **Flow 1 — First session (UJ-1).** Climax at 13: a lime path branches off the road to where the choice took the player, the destination lights up, and the money, wellbeing and room change float over the figures before the result dialog states them.
- **Flow 3 — Interest grew (UJ-3).** The bank SMS slides in as a real banner (09); in 14 the echo card in sun yellow ties the change back to the saving choice "da du var 15".
- **Flow 6 / year end (FR-14).** At 23 the camera reaches the gate, the year strip fills, and "START ÅR 4" walks the player through it to the next level.

## Inspiration & Anti-patterns

- **Lifted:** mobile game level maps (milestones, gates, flags); the K2 hand sketches' four areas (Plan, Jobb, Økonomi) as the dock; the real phone's messaging app for SMS.
- **Rejected — information overload and many elements** (round 1: Plakaten, Brettet, Linjen). Hence one main thing per screen and the newest thing clearest.
- **Rejected — ugly and dull colors**, and earlier sketches that all looked alike and monotone. Hence a strong dusk palette, but the green was toned down to #B4E86E when it was too loud.
- **Rejected — childish/cartoon, school or learning-tool feel, and a static picture you tap on.** Hence detailed avatars, a scene that reacts (lit cabin, side path, night for crisis) and choices in dialogs.
- **Rejected — bank-app feel as a whole.** Bank-like pieces (accounts in 17) are allowed only inside the game frame.
- **Rejected — simple avatars, a small road and a normal tab bar** (Veien v1/v2). The road became the biggest element and the tab bar became a game dock with a big GÅ.
- **Rejected — a game-styled phone.** The SMS must feel like a real SMS.
