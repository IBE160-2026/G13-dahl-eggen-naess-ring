---
name: LifeMode — Speilet
status: candidate
created: 2026-11-17
updated: 2026-11-18
sources:
  - ../../../../prds/prd-IBE160-G13-2026-10-22/prd.md
  - ../../PRODUCT.md
  - ../../EXPERIENCE.md
  - ../../.memlog.md
sketches: ../../.working/speilet/oversikt.html
---

# Speilet — Experience Delta

## Foundation

This file inherits everything in the shared spine (`../../EXPERIENCE.md`): the 28 surfaces, voice, states, interaction primitives, accessibility floor and key flows. It only records how Speilet differs. Visual tokens and component specs are in `DESIGN.md`. The PRD wins on conflict.

Core idea: the whole screen is one scene, a mirror selfie in the player's own room. Choices live inside the scene as things to tap, not as boxes with buttons. The scene must feel alive: light follows the season, the reflection's mood reacts to choices, played months get photos and the room fills as the life goal grows.

PRD adaptations (memlog): the reflection shows the player's **current** age, never a projected 20-year-old; things unlock by age only (FR-18); the look is one of six preset avatars, with no typed name (FR-10). A home and avatar that evolve beyond belongings are "Later" in the PRD and are not part of this concept.

## Metaphor Map

| # | Surface | Where it lives in Speilet |
|---|---|---|
| 01 | First screen | Empty mirror in an empty room, twelve blank cards on the garland; "LifeMode" and marker "Fem år. Dine valg." on the glass; coral "Opprett bruker", white "Logg inn" |
| 02–04 | Create user, log in, forgot password | Paper sheet slides up over the dimmed empty scene |
| 05 | Choose life goal | Three glowing objects on the reflected floor: moving boxes ("Noe stort"), packed backpack ("Opplevelse"), small safe ("Buffer"); tap the object |
| 06 | Choose avatar | Six photos taped to the top of the glass; the chosen one is ringed and the reflection becomes that look; coral "Dette er meg"; "Utseendet påvirker ikke tallene." |
| 07 | Pengegave | Reflection holds an open envelope; marker callout with the amount; three white option stickers with sublines |
| 08 | Month hub | Mirror selfie; garland with the current month; "Du, 16 år" on the glass; locked post-its; stickers on the frame; work shirt; light switch |
| 09 | Notification | SMS banner slides down over the hub |
| 10–11 | Phone | The phone is held in the player's hands over the dimmed scene; invitation card with coral "Legg i planen" |
| 12 | Story event | Glass dims; only the choosable objects glow (headphones on the frame, work shirt, backpack on the floor), each with a marker callout and its kroner effect |
| 13 | Result | Reflection changes mood; the current garland card gets the event photo; changes written in marker beside the stickers |
| 14 | "Hvorfor?" | Glass dims further; the cause chain is drawn in white marker with arrows |
| 15 | Month plan | Four evenings drawn as dashed boxes on dimmed glass; activities are stickers below |
| 16 | Job view | "Vakter" app on the phone in hands |
| 17 | Money view | "Banken" app on the phone in hands; credit card row locked with a padlock until 18 |
| 18 | Room and wellbeing | Marker "Slik har du det" with three five-dot scales; callouts on room items (helmet, goal boxes) |
| 19 | Year line | Five garlands under each other on the wall, År 1–5, marker "her er du" on the current one |
| 20 | Card warning | Bank banner over the hub at 18; two option stickers |
| 21 | Crisis month | Dimmed glass, tired reflection, white marker "Oktober går ikke opp" and "Steg 1 av 3"; three way-out stickers |
| 22 | Driving minigame | "Øvingskjøring" on the phone in hands; crossing seen from above; three choices, "Ingen klokke." |
| 23 | Year end | All twelve cards have photos; marker "År 2 er ferdig!"; summary stickers; coral "Til År 3" |
| 24 | Welcome back | Dimmed glass with a short recap in white marker; coral "Fortsett" |
| 25 | Ending | Reflection at 20; boxes gone, keys on the hook; marker "Målet er nådd!"; "Se historien din", "Start et nytt liv" |
| 26–27 | Menu, about the numbers | Paper sheet over the hub |
| 28 | Offline | A yellow post-it "Ingen nett" on the glass; stickers and switch faded |

Life goal progress is a thing in the room: moving boxes in the reflection with the goal word and percent written on them (FR-9). Belongings appear as objects in the reflected room (FR-34), such as the moped helmet.

## Component Patterns

Delta only. Shared rules: `../../EXPERIENCE.md` → Component Patterns.

| Component | Speilet behavior |
|---|---|
| Hub status | Split across the scene: year above the garland, month on the garland, age in marker on the glass, money and wellbeing as stickers. Never the month name next to the age in a header. |
| Year progress | The photo garland. A month gets its photo when it is played; the event photo replaces the generic tint. |
| Area entry points | Messages sticker → 10, wellbeing sticker → 18, money sticker → 17, work shirt → 16, "Kveldene" callout → 15. The garland → 19 [ASSUMPTION: not marked in sketches]. |
| Next month | The light switch. Only one per hub; it is hidden while an event, result or overlay is open. |
| Locked item | Yellow post-it on the glass. At unlock the note comes off and the thing appears in the room [ASSUMPTION: carried from round 1, not drawn in round 3]. |
| Option | A glowing object in the scene when one fits; a white sticker otherwise. The chosen object, not a separate button, is the action. |
| Primary action | Coral sticker, one per screen. On 20 the sketch marks "Betal hele" as coral; whether a recommended option may be coral is open, since the shared spine forbids quiz framing. |
| Sheet | Account and menu tasks only; never game choices. |
| Menu entry | Not drawn on the hub [ASSUMPTION: needs a labeled object or sticker, placement open]. |

## Interaction Primitives

- Tap objects in the scene: stickers, post-its, the work shirt, the switch, glowing event objects, taped photos. Each has a visible handwritten or printed label; nothing is a hidden hotspot.
- Next month = tap the light switch ("Slå av lyset"). The room goes dark briefly and the next month starts in its season's light; with reduced motion this is an instant change.
- Overlays come from the scene: the phone is lifted into the hands, sheets slide up from the floor, and the glass dims for events, "Hvorfor?", the month plan and crisis. Closing returns to the same hub.
- The flash sparkle and seasonal light are decorative motion only.

## State Patterns

Only concept-specific renderings; the states themselves are shared.

| State | Speilet rendering |
|---|---|
| Offline | Yellow post-it "Ingen nett. Du kan se deg rundt. Valgene venter til du er på nett igjen."; status stickers at 55 % opacity; switch faded with callout "venter på nett". Yellow is right here because things are locked. |
| Focus moments (12, 14, 15, 21, 24) | Only the glass dims (50–62 %); marker turns white; the frame, garland and wall stay in normal light. |
| Seasons | Winter (Jan, Feb, Nov, Dec) cool wall and snow in the window; spring base; summer bright sky; autumn warm sky. Only color changes. |
| Saving / still trying | [ASSUMPTION] Not sketched; shown as marker text on the glass with options locked. |
| Ending variants | Only the real win is sketched (25); hollow win, goal not reached and loss [ASSUMPTION] use the same scene with a different reflection mood and room. |

## Accessibility Notes

- **Reflection:** text alternative names look, age, pose and mood, e.g. "Speilbildet ditt, 16 år, tar en speilselfie" or "… smiler". The look never changes the numbers.
- **Garland:** one text summary, e.g. "År 2 av 5. April, fire av tolv måneder. Historie i januar, april, juli og oktober." Single-letter month labels are not read one by one.
- **Stickers and post-its:** labels follow the sketches: "Mobil: 2 nye", "Penger: 18 450 kr", "Bil-lappen: låst, åpnes når du blir 18 år".
- **Marker text:** Kalam is only used for words, at 13 px or larger, weight 700; every value is in Bricolage. All marker pairs, including white marker on dimmed glass in all four seasons, pass AA (`DESIGN.md` → Colors).
- **Focus order** follows reading order: garland, age, post-its, stickers, work shirt, switch [ASSUMPTION: focus ring style not sketched].
- Rotated stickers are drawn 40 px tall; their touch area must reach at least 44 px.

## Key Flows

Flows and steps are the shared ones (`../../EXPERIENCE.md` → Key Flows). Speilet's visual climax:

- **Flow 1 — First session:** at 13 the reflection smiles, the April card on the garland gets the photo from the trip, and the money and wellbeing stickers change, with the changes written in marker beside them.
- **Flow 3 — Interest grew:** in 14 the glass dims and the cause chain is drawn in white marker, from the earlier choice to the new value.
- **Flow 4 — November with extra shifts:** in 15 three evenings, not four, are drawn on the dark winter glass, so time is visibly short.

## Inspiration & Anti-patterns

From the memlog (entries 27–43):

- **Rejected — not clearly a mirror** (rounds 1 and 2): solved by the selfie pose, the black frame, the flash and the darker reflected room.
- **Rejected — semi-realistic SVG people** and the over-the-shoulder view: replaced by flat graphic illustration.
- **Rejected — pink LED strip:** light with no function. Light now has jobs: season and the switch.
- **Rejected — white paper notes and too many elements:** only yellow post-its (locked) remain; status moved to stickers; stool and wallet removed.
- **Rejected — month name next to age in the header:** the month lives only on the garland.
- **Kept principle:** a static picture with hotspots felt wrong; the scene must react.
