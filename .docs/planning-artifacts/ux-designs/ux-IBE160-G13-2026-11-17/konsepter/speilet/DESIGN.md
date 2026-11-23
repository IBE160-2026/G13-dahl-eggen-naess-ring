---
name: LifeMode — Speilet
description: A mirror selfie in your own room. The whole screen is one illustrated scene; the year hangs as a photo garland above a tall mirror, and choices are things in the scene.
status: superseded
superseded_by: .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/ (final; direction chosen in issue #95)
created: 2026-11-17
updated: 2026-11-18
sketches: ../../.working/speilet/oversikt.html
colors:
  wall: '#C7D5C0'
  wall-lit: '#DCE6D2'
  wall-mirror: '#A9BBA3'
  sky: '#DCEBF2'
  wall-winter: '#B8C4BC'
  wall-lit-winter: '#C8D2CA'
  wall-mirror-winter: '#97A69D'
  sky-winter: '#8EA3C9'
  wall-summer: '#CFDDBE'
  wall-lit-summer: '#E6EED8'
  wall-mirror-summer: '#B3C59F'
  sky-summer: '#9FD3F2'
  wall-autumn: '#C9CDB4'
  wall-lit-autumn: '#D9DCC6'
  wall-mirror-autumn: '#ACB295'
  sky-autumn: '#E8B27A'
  floor: '#C99A6B'
  floor-mirror: '#AD8459'
  baseboard: '#EEF0E8'
  mirror-frame: '#1C1C20'
  ink: '#1A1C2A'
  ink-muted: '#454656'
  note-yellow: '#FFE27A'
  paper: '#F6F3EC'
  white: '#FFFFFF'
  coral: '#FF6F59'
  cobalt: '#2B4CC4'
  money-green: '#2E7D6B'
  press: '#A3122A'
  goal-box: '#C4935F'
  clip: '#B8865A'
  tape: '#F4EEDC'
  dim: '#14161F'
  phone-body: '#121318'
  phone-muted: '#5A5E6B'
  phone-hairline: '#E2E2E8'
  phone-bubble: '#ECECF1'
  phone-card-job: '#E7F2EE'
  phone-card-offer: '#FFF5DA'
  phone-card-goal: '#F1EBDD'
  banner-surface: '#FBFBFD'
  sheet-hairline: '#DDD8CC'
  sender-emma: '#94601A'
  sender-mamma: '#7154A8'
typography:
  wordmark: { fontFamily: Bricolage Grotesque, fontSize: 40px, fontWeight: 800 }
  sheet-title: { fontFamily: Bricolage Grotesque, fontSize: 26px, fontWeight: 800 }
  age: { fontFamily: Bricolage Grotesque, fontSize: 26px, fontWeight: 800 }
  money-total: { fontFamily: Bricolage Grotesque, fontSize: 34px, fontWeight: 800 }
  year-label: { fontFamily: Bricolage Grotesque, fontSize: 15px, fontWeight: 800 }
  month-current: { fontFamily: Bricolage Grotesque, fontSize: 15px, fontWeight: 800 }
  month-initial: { fontFamily: Bricolage Grotesque, fontSize: 12px, fontWeight: 600 }
  value: { fontFamily: Bricolage Grotesque, fontSize: 14px, fontWeight: 800 }
  sticker-label: { fontFamily: Bricolage Grotesque, fontSize: 14px, fontWeight: 800 }
  sticker-sub: { fontFamily: Bricolage Grotesque, fontSize: 12px, fontWeight: 650 }
  button: { fontFamily: Bricolage Grotesque, fontSize: 16px, fontWeight: 800 }
  body: { fontFamily: Bricolage Grotesque, fontSize: 14.5px, fontWeight: 600 }
  field: { fontFamily: Bricolage Grotesque, fontSize: 15.5px, fontWeight: 500 }
  meta: { fontFamily: Bricolage Grotesque, fontSize: 13px, fontWeight: 600 }
  marker-heading: { fontFamily: Kalam, fontSize: 24px, fontWeight: 700 }
  marker: { fontFamily: Kalam, fontSize: 15px, fontWeight: 700 }
  marker-note: { fontFamily: Kalam, fontSize: 13.5px, fontWeight: 700 }
rounded:
  none: 0px
  sm: 6px
  md: 10px
  lg: 16px
  xl: 20px
  sheet: 24px
  device: 44px
  full: 9999px
spacing:
  scene-width: 390px
  banner-inset: 12px
  sheet-inset: 24px
  sticker-gap: 8px
  mirror-frame: 9px
  garland-pitch: 30.7px
  target-min: 44px
components:
  hub-status: { yearFont: '{typography.year-label}', ageWordFont: '{typography.marker}', ageFont: '{typography.age}', color: '{colors.ink}' }
  photo-garland: { string: '{colors.ink-muted}', clip: '{colors.clip}', card: '{colors.white}', blankCard: '{colors.paper}', cardSize: 22x28px, currentSize: 36x46px, ring: '{colors.coral}', ringOutline: '{colors.ink}', star: '{colors.note-yellow}', rounded: '{rounded.none}' }
  sticker: { background: '{colors.white}', border: '{colors.ink-muted}', borderWidth: 1.5px, height: 40px, heightWithSub: 48px, rounded: '{rounded.full}', label: '{typography.sticker-label}', sub: '{typography.sticker-sub}' }
  sticker-primary: { background: '{colors.coral}', border: '{colors.ink}', borderWidth: 2px, textColor: '{colors.ink}', rounded: '{rounded.full}' }
  locked-note: { background: '{colors.note-yellow}', border: '{colors.ink-muted}', size: 84x84px, rounded: '{rounded.none}', title: '{typography.marker-note}', tape: '{colors.tape}' }
  light-switch: { plate: '{colors.baseboard}', size: 38x56px, rounded: '{rounded.sm}', halo: '{colors.note-yellow}' }
  work-shirt: { fill: '{colors.money-green}', hook: '{colors.ink-muted}' }
  callout: { word: '{typography.marker}', value: '{typography.value}', arrowWidth: 2px, color: '{colors.ink}' }
  activity-slot: { border: '{colors.white}', borderWidth: 2.4px, dash: 7 5, size: 104x84px, rounded: '{rounded.md}' }
  sheet: { background: '{colors.paper}', scrim: '{colors.dim}', rounded: '{rounded.sheet}', title: '{typography.sheet-title}', inset: '{spacing.sheet-inset}' }
  field: { background: '{colors.white}', border: '{colors.ink-muted}', errorBorder: '{colors.press}', height: 50px, rounded: '{rounded.md}' }
  pill-button: { background: '{colors.coral}', border: '{colors.ink}', height: 52px, rounded: '{rounded.full}', font: '{typography.button}' }
  phone: { body: '{colors.phone-body}', screen: '{colors.white}', rounded: '{rounded.device}', muted: '{colors.phone-muted}', hairline: '{colors.phone-hairline}' }
  notification-banner: { background: '{colors.banner-surface}', size: 366x84px, rounded: '{rounded.xl}', inset: '{spacing.banner-inset}' }
  mirror: { frame: '{colors.mirror-frame}', frameWidth: '{spacing.mirror-frame}', glassEdge: '{colors.white}' }
---

## Brand & Style

Speilet is a mirror selfie in the player's own room. A tall mirror leans against the wall; the reflection holds a coral phone up to the glass and the flash sparkles. Everything the player needs lives inside that one picture: the year hangs as a photo garland of twelve clips above the mirror, locked things are yellow post-its on the glass, status is stickers on the frame, and the next month is the light switch on the wall. There are no tabs, card stacks or button rows.

The style is graphic illustration after three rounds (semi-realistic and over-the-shoulder were rejected): flat shapes, one shade tone per surface, a light grain over the whole screen, and handwriting in marker on glass and wall. It reads like a teenager's room photographed on a phone, grown-up rather than cartoonish. The scene is alive: the light follows the season, the reflection's mood changes with choices, played months get photos, and things arrive in the room as the life goal grows.

## Colors

- **Wall, wall-lit, wall-mirror, sky** are the room and its reflection. The reflected wall is darker than the real wall so the glass reads as glass. Each has a season variant (winter Jan, Feb, Nov, Dec with snow in the window; spring = base Mar–May; summer Jun–Aug; autumn Sep–Oct). Light is the only thing seasons change; layout never moves.
- **Floor, floor-mirror, baseboard** ground the scene. Baseboard (`#EEF0E8`) also paints the switch plate and window frame.
- **Mirror-frame** (`#1C1C20`) is the black frame that makes "this is a mirror" unmistakable. Never used for text.
- **Ink** (`#1A1C2A`) is all text, marker and arrows on light surfaces and the border of primary stickers. **Ink-muted** (`#454656`) is secondary text, sticker and note borders, the garland string and coming-month letters.
- **Note-yellow** (`#FFE27A`) as paper means **locked, and only locked**. The same yellow is reused as a soft halo behind tappable scene objects (switch, event and goal objects) and fills the star of a played story month. Never a yellow card for status, tips or news.
- **Coral** (`#FF6F59`) is the phone case, the primary-action sticker, the ring around the current month and the unread dot. Never for loss or warnings. Coral against the wall is only 1.79:1, so a coral control always carries a 2 px ink border.
- **Cobalt, money-green** are icon and object colors: cobalt for the messages icon, Markus's hoodie and Banken; money-green for the penger icon, the work shirt and Butikken. They are not state colors.
- **Press** (`#A3122A`) is for "Slett bruker" and field errors on the sheet only. Money loss is shown with "−" and a word, never with red.
- **Paper, white, dim** are the sheet, stickers and photo cards, and the dark scrim (`#14161F`, 45–62 %) used for overlays and dimmed glass. On dimmed glass the marker turns white.
- **Phone and sender tokens** are used only inside the phone held in the hands.

Measured with `.working/speilet/kontrast.py` against WCAG 2.2 AA: **49 pairs, 0 below the requirement** (lowest text pair 4.61:1, white marker over the spring window; lowest graphic pair 3.65:1, note border on winter glass). Nothing is shown by color alone: current month = larger card + full name + ring; played vs coming = photo vs dashed blank card; story month = star shape; locked = post-it + padlock + "fra 18 år"; money = sign and word. Faded offline stickers (55 % opacity) measure about 4.3–4.8:1 and are not in `kontrast.py`; they are inactive controls and the post-it carries the message.

## Typography

Two families. **Bricolage Grotesque** (400–800) is the system voice: every number, kroner amount, age, sticker label, sheet and phone text. **Kalam** (400, 700) is the marker: words written on glass and wall ("Du", "Kveldene i april", "Slå av lyset", "Hva gjør du i påsken?"). Rule: Kalam writes the word, Bricolage writes the value. A callout is a Kalam word with the Bricolage value underneath ("Jobb" / "8 t/uke"). Kalam is never below 13 px and always weight 700.

Ramp: `wordmark` 40 for "LifeMode" on screen 01; `age` 26 for "16 år"; `marker-heading` 21–26 for questions and screen headings on glass; `sheet-title` 26; `year-label` 15 for "År 2 av 5"; `sticker-label` 14 / `sticker-sub` 12; `month-initial` 12 for the single-letter months, `month-current` 15 for the full current month name.

## Layout & Spacing

Designed at 390 × 844. The first viewport is fixed by the direction contract: garland across the top (y ≈ 54–130) with "År N av 5" above it; the mirror fills the left two thirds (x 44–300, y 150–772, narrower at the top because it leans); marker age on the glass with an arrow to the reflection; locked post-its top right of the glass; three status stickers stacked on the lower right frame (`sticker-gap` 8 px); work shirt and light switch on the wall to the right of the mirror; floor across the bottom.

Overlays: notification banner inset 12 px; sheets inset 24 px and start between y 110 and 330 so the scene stays visible above; the phone fills the screen inside the player's hands. Below 390 px the window, floor and room behind the reflection crop first; the garland keeps all twelve clips by shrinking `garland-pitch`; stickers, switch and post-its keep their size [ASSUMPTION: 320 px layout not sketched].

## Elevation & Depth

Depth is physical, never decorative. Three levels: the scene itself (flat shapes, one darker shade tone per form, grain at 18 % multiply over everything); things stuck to it (post-its and stickers with a small drop shadow, 2.5 px down, 28 % ink, slightly rotated −4° to 4°); and things held over it (sheet, phone, banner with a lift shadow upward, 25 % ink, over the `dim` scrim). Glass is marked by two faint white sheen bands and a white 1.5 px inner edge at 50 %. Dimming the glass (not the whole screen) is how events, "Hvorfor?", the month plan and crisis focus attention.

## Shapes

Paper is square (`rounded.none`): post-its, photo cards, taped portraits. Stickers are full pills (`rounded.full`). Controls on the sheet: fields and slots `rounded.md`, checkbox and switch plate `rounded.sm`, phone cards `rounded.lg`, banner `rounded.xl`, sheet top corners `rounded.sheet`, phone body `rounded.device`. Slight rotation is part of the shape language for anything stuck on by hand; nothing on a sheet or phone is rotated.

## Components

- **Mirror** — black trapezoid frame (`mirror-frame`, 9 px), clipped glass showing the reflected room: window with seasonal sky, lamp, bed, goal boxes. A soft floor shadow at the foot. Optional dim layer inside the glass only.
- **Reflection figure** — flat graphic person, one of six preset looks (skin, hair style, hoodie, trousers; hoodie colors `#2B4CC4`, `#D99A2B`, `#2E7D6B`, `#8E6CC9`, `#25292E`, `#C8453A`). *Selfie pose* (hub): coral phone held in front of the face, camera toward the glass, one eye visible. *Standing pose* (events, results, wellbeing, ending): face visible with mood smil, glad, nøytral, tenker or sliten; phone or envelope in hand. Shows the current age only.
- **Flash** — white burst at the phone camera (core 5 px, halo 14 px at 40 %, eight rays). Selfie pose only; hidden when the glass is dimmed.
- **Marker text and callouts** — Kalam word + Bricolage value + a 2 px hand-drawn arrow to the object it names. Ink on light glass and wall; white on dimmed glass.
- **Hub status** — "År 2 av 5" (`year-label`) above the garland; month = the garland's current card; "Du" / "16 år" on the glass with an arrow to the reflection; money and wellbeing as stickers. No month name next to the age in a header.
- **Photo garland** — a sagging string with twelve wooden clips. Played months: white photo card with a month-tinted photo (twelve tints, winter blue to autumn rust) or the real event photo. Current month: 36 × 46 card, full name below, coral ring with a thin ink outline. Coming months: dashed blank paper card, letter in `ink-muted`. Story months (Jan, Apr, Jul, Oct): star at the clip, yellow when reached, paper when ahead.
- **Area entry points** — status stickers on the frame: messages icon + "2 nye" (coral dot when unread), heart + "Trivsel 64", note icon + "18 450 kr". Work shirt on a hook with callout "Jobb / 8 t/uke". Marker callout "Kveldene i april / 2 av 4 ledige" with an arrow to the current month.
- **Next month (light switch)** — switch plate 38 × 56 on the wall with a soft yellow halo; callout "Slå av lyset / Neste måned".
- **Locked post-it** — 84 × 84 yellow note, taped, rotated; dashed outline icon of the thing, Kalam title, "fra 18 år", padlock top right.
- **Option** — an object in the scene that glows (event) with a callout naming the action and its kroner effect ("Bli med på hytta / −1 200 kr"); when no object fits, a white sticker with a subline ("Halvparten i BSU" / "9 000 kr, resten fritt").
- **Primary action** — coral sticker with arrow icon and ink border ("Fortsett", "Ferdig", "Til År 3"); on sheets and in the phone, a full-width coral pill.
- **Result** — reflection in standing pose with the new mood; the current garland card gains the event photo; changes written in marker next to the stickers they changed; stickers show new values; white "Hvorfor?" sticker (circled ?) above coral "Fortsett".
- **"Hvorfor?"** — glass dimmed to 62 %; the cause chain drawn in white marker with arrows from the taped photo to each changed value ("Trivsel: 64 → 70"); coral "Lukk".
- **Activity slot** — dashed white rectangle drawn on dimmed glass; empty shows "+" and "ledig"; filled holds a white sticker with name and cost.
- **Phone and messages** — dark phone body in the player's hands over a 50 % scrim; white screen, app title, message rows with round sender initials, grey bubbles, invitation card with a coral pill.
- **Notification banner** — near-white rounded card at the top with sender icon, name, "nå" and two lines; lift shadow.
- **Sheet** — paper sheet with grab handle sliding over the dimmed scene; title, fields (50 px, error border `press`), checkbox, underlined links, coral pill; menu rows with chevrons, "Slett bruker" in `press`.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Use yellow post-it paper only for locked things | Use yellow notes for tips, news or status |
| Put every choice inside the scene as an object or sticker with a visible label | Add button rows, tabs or card stacks over the room |
| Keep the frame black and the reflected room darker than the real wall | Let the mirror read as a window or a poster |
| Write words in Kalam and values in Bricolage | Write kroner amounts or ages in handwriting |
| Change light with the season; keep positions fixed | Move the switch, stickers or garland between months |
| Show money changes as "−1 200 kr" with sign and word (sketch 13 omits "kr"; add it) | Color a loss red or a gain green |
| Turn marker white whenever the glass is dimmed | Put ink marker on dimmed glass |
| Keep the reflection at the player's current age | Show a projected future self |
