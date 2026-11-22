---
name: LifeMode · Blokka
description: Your life as an isometric 3D apartment block seen as a dollhouse. Five floors are År 1–5, your floor stands open, daylight and the Fjord palette.
status: candidate
created: 2026-11-17
updated: 2026-11-18
sketches: ../../.working/blokka/oversikt.html
colors:
  fog: '#DCEAE5'
  fog-light: '#F3F7F5'
  surface: '#FFFFFF'
  panel: '#E4ECE9'
  line: '#C3D2CD'
  steel: '#AFC0BA'
  ink: '#18262B'
  ink-soft: '#4D5F63'
  action: '#1E5A6B'
  action-deep: '#143E4A'
  action-tint: '#D5E6E2'
  on-action-muted: '#C9D4FF'
  press: '#B3364F'
  year-1-cloudberry: '#F0A24A'
  year-2-birch: '#E6D7B0'
  year-3-moss: '#8DAA7B'
  year-4-fjord: '#6E9BC4'
  year-5-lingonberry: '#C25B6E'
  year-5-tab: '#D98A98'
  lit: '#FFD45C'
  window-dark: '#5C6F8C'
  control-border: '#7C8F8A'
  stepper-border: '#5F7470'
  elevator-label: '#9FB0C8'
  note-blue: '#BFE3F5'
  note-pink: '#F7C5C0'
  wellbeing-leisure: '#4A7AA8'
  wellbeing-social: '#5E7E4E'
  sender-emma: '#24705E'
  sender-mamma: '#A9475A'
  room-wall: '#FBF3E6'
  room-floor: '#D8A97E'
  roof: '#6E7F95'
  street-front: '#EEF1F5'
  grass: '#8FC59A'
  phone-grey: '#6C6C70'
  phone-blue: '#0066CC'
  phone-banner: '#F4F3F8'
  phone-banner-label: '#5E5E66'
typography:
  wordmark: { fontFamily: Schibsted Grotesk, fontSize: 44px, fontWeight: 900, letterSpacing: -1.5px }
  result-amount: { fontFamily: Schibsted Grotesk, fontSize: 40px, fontWeight: 900, letterSpacing: -1px }
  month-title: { fontFamily: Schibsted Grotesk, fontSize: 30px, fontWeight: 900, letterSpacing: -0.8px }
  page-title: { fontFamily: Schibsted Grotesk, fontSize: 26px, fontWeight: 900, letterSpacing: -0.5px }
  event-title: { fontFamily: Schibsted Grotesk, fontSize: 24px, fontWeight: 900, letterSpacing: -0.5px }
  section-title: { fontFamily: Schibsted Grotesk, fontSize: 18px, fontWeight: 900 }
  floor-number: { fontFamily: Schibsted Grotesk, fontSize: 26px, fontWeight: 800 }
  button: { fontFamily: Schibsted Grotesk, fontSize: 17px, fontWeight: 800 }
  option-label: { fontFamily: Schibsted Grotesk, fontSize: 16px, fontWeight: 700 }
  option-amount: { fontFamily: Schibsted Grotesk, fontSize: 16px, fontWeight: 800 }
  label-strong: { fontFamily: Schibsted Grotesk, fontSize: 14.5px, fontWeight: 800 }
  body: { fontFamily: Schibsted Grotesk, fontSize: 14px, fontWeight: 500 }
  caption: { fontFamily: Schibsted Grotesk, fontSize: 12.5px, fontWeight: 500 }
  tag: { fontFamily: Schibsted Grotesk, fontSize: 11px, fontWeight: 800 }
  month-cell: { fontFamily: Schibsted Grotesk, fontSize: 9.5px, fontWeight: 800 }
  phone-system: { fontFamily: "-apple-system, 'Segoe UI', system-ui, sans-serif", fontSize: 15px, fontWeight: 400 }
rounded:
  xs: 2px
  sm: 6px
  md: 8px
  lg: 10px
  xl: 12px
  dialog: 16px
  sheet: 20px
  full: 9999px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
  '5': 20px
  '6': 24px
  margin-mobile: 20px
  option-gap: 10px
components:
  hub-status: { textColor: '{colors.ink}', typography: '{typography.label-strong}', coinColor: '{colors.lit}', heartColor: '{colors.press}', flagColor: '{colors.action}' }
  month-strip: { backgroundColor: '{colors.surface}', borderColor: '{colors.line}', rounded: '{rounded.lg}', height: 52px, cellRounded: '{rounded.sm}', cellHeight: 38px, typography: '{typography.month-cell}' }
  month-cell-current: { backgroundColor: '{colors.action}', textColor: '{colors.surface}' }
  month-cell-played: { backgroundColor: '{colors.action-tint}', borderColor: '{colors.control-border}', textColor: '{colors.action-deep}' }
  month-cell-coming: { backgroundColor: transparent, borderColor: '{colors.control-border}', textColor: '{colors.ink-soft}' }
  doorbell-panel: { backgroundColor: '{colors.panel}', borderColor: '{colors.steel}' }
  doorbell-plate: { backgroundColor: '{colors.surface}', borderColor: '{colors.steel}', rounded: '{rounded.md}', width: 175px, height: 46px, gap: '{spacing.2}', buttonActive: '{colors.action}', noteColor: '{colors.action}' }
  button-primary: { backgroundColor: '{colors.action}', textColor: '{colors.surface}', subTextColor: '{colors.on-action-muted}', typography: '{typography.button}', rounded: '{rounded.lg}', height: 54px }
  button-secondary: { backgroundColor: '{colors.surface}', borderColor: '{colors.action}', textColor: '{colors.action}', rounded: '{rounded.lg}', height: 50px }
  option: { backgroundColor: '{colors.surface}', borderColor: '{colors.action}', borderWidth: 2px, rounded: '{rounded.md}', height: 50px, labelType: '{typography.option-label}', amountType: '{typography.option-amount}', amountColor: '{colors.action}', disabledOpacity: 0.45 }
  locked-floor: { opacity: 0.42, connector: 'dashed 3 4, {colors.ink-soft}' }
  result-note: { yellow: '{colors.lit}', blue: '{colors.note-blue}', pink: '{colors.note-pink}', textColor: '{colors.ink}' }
  why-link: { textColor: '{colors.action}', typography: '{typography.label-strong}', decoration: underline }
  why-card: { backgroundColor: '{colors.surface}', borderColor: '{colors.line}', rounded: '{rounded.lg}', stripeWidth: 8px }
  activity-slot: { rounded: '{rounded.lg}', height: 70px, emptyBorder: 'dashed 6 5, {colors.action}', workFill: '{colors.panel}' }
  window-meter: { cells: 20, cellHeight: 16px, rounded: '{rounded.xs}', on: '{colors.lit}', off: '{colors.window-dark}', newestBorder: '{colors.action}' }
  sms-banner: { backgroundColor: '{colors.phone-banner}', rounded: 22px, height: 76px, labelColor: '{colors.phone-banner-label}' }
  sheet: { backgroundColor: '{colors.fog-light}', rounded: '{rounded.sheet}', scrim: '{colors.ink}', scrimOpacity: 0.45 }
  dialog: { backgroundColor: '{colors.surface}', rounded: '{rounded.dialog}', scrimOpacity: 0.5 }
  floor-display: { backgroundColor: '{colors.ink}', numberColor: '{colors.lit}', labelColor: '{colors.elevator-label}', rounded: '{rounded.md}', width: 72px, height: 44px }
  year-tag: { width: 40px, height: 22px, rounded: 5px, current: '{colors.ink}', other: '{colors.surface}', typography: '{typography.tag}' }
---

## Brand & Style

Blokka turns five years of life into one apartment block. The camera is a fixed isometric 3D view of a dollhouse: the street level holds «BUTIKKEN» and «BANKEN», five floors above are År 1–5, the life goal is a flag on the roof, and a lift tower on the right side shows where you live now. Your floor stands open like a dollhouse room; floors you have lived in are closed with lit windows; floors above are lifted and see-through, waiting.

The posture is daylight, calm and grown-up: soft Nordic colors (the Fjord palette), flat shading with three tones per box, and slim, rounded avatars with natural proportions. It is a game you look into, not a dashboard and not a bank. Life happens on the floor and in the stairwell: the doorbell rings, notes go up on the wall, a photo appears after a trip.

## Colors

Fjord palette from `skjermer.py` (`PALETTES["fjord"]`). Measured with `kontrast.py` against WCAG 2.2 AA: **71 pairs, 0 below the requirement** (lowest: control borders `#7C8F8A` on fog-light at 3.16:1, graphics need 3:1; small text lowest is phone search at 4.56:1). Rule: **nothing by color alone**. Money carries a sign and a word, months differ by fill and outline, floors carry «År N» tags, windows are also counted in text.

- **Fog / fog-light** (`#DCEAE5` → `#F3F7F5`) is the sky gradient behind the scene and the lower sheet. Not for cards (cards are `surface`).
- **Year colors** are floor facades only: cloudberry År 1, birch År 2, moss År 3, fjord blue År 4, lingonberry År 5. They identify a year, never a state or a value. Ink text is allowed on years 1–4 (5.29–10.89:1); on År 5 use `year-5-tab` (`#D98A98`, 5.95:1), never ink on lingonberry.
- **Action** (`#1E5A6B`, deep fjord green) is the only interactive color: primary button, option borders and amounts, links, doorbell buttons, the current month. `action-deep` and `action-tint` render played months. `on-action-muted` is only the secondary word in the primary button («desember»).
- **Press** (`#B3364F`) is reserved for what pushes on you: card debt, crisis, «Si opp jobben», «Slett kontoen», stress, negative totals at the ending. Not for decoration and never as a scolding signal. [ASSUMPTION] The sketches also use press for the wellbeing heart icon, the moped helmet, the gift box and the «BUTIKKEN» sign; the group should decide whether those stay.
- **Lit** (`#FFD45C`) is light: lit windows (played months, wellbeing), the floor number in the lift display, the yellow note, the coin. `window-dark` is an unlit window.
- **Notes** (lit, `note-blue`, `note-pink`) are result notes on the wall; ink text on all (10.1–11.5:1).
- **Phone colors** (`phone-*`, system font) belong only to surfaces 09–11, which deliberately look like a real phone.

Light only. [ASSUMPTION] No dark-mode tokens exist in the sketches; the daylight look is part of the concept.

## Typography

Schibsted Grotesk (Google Fonts, weights 400–900) everywhere except the phone, which uses the system stack so SMS feels real. Heavy weights carry the game: month name at `month-title`, money results at `result-amount`, titles at 900. Body text is `body` 14px/500, secondary lines `caption` in `ink-soft`. The month strip uses 9.5px/800 capitals («JAN» … «DES»), which is the floor of the ramp. Time is always the month name plus «17 år · År 3 av 5», never a month number. [ASSUMPTION] Line heights are not set in the SVG sketches; use about 1.2 for titles and 1.45 for body.

## Layout & Spacing

Designed at 390 × 844. Side margin `spacing.margin-mobile` (20px); the doorbell panel and primary button sit at 16px. Options stack with `option-gap` (10px, 50px tall on a 60px rhythm); doorbell plates sit 2 × 2 with an 8px gap.

Hub layout from top: status, month name and age line with the lift display at top right, a status row (money, wellbeing, life goal), the month strip, the scene (clipped to your floor and the ones below), then the doorbell panel and «Neste måned». Event, result and pressure screens split at about y 452: scene on top, a light sheet below with text and options. Sub-pages (02–06, 15, 19, 26, 27) use a fog header with a mini block icon and a sheet with 20px top corners. At 320px the scene crops first; the strip, doorbells and primary button stay.

## Elevation & Depth

Depth comes from the isometric box itself: every box has three faces, top at full tone, left at 88 %, right at 74 % (`iso.py`). Floors above yours are lifted with dashed corner lines and drawn at 42 % opacity. UI elevation is a single soft drop shadow (`dy 6, blur 8, #14213D at 16 %`) on floating pills, the speech bubble, the SMS banner, dialogs and sheets. Scrims are ink at 45–50 % (12 % behind the SMS banner).

## Shapes

Rectangles with modest radii, like signage in a stairwell: `xs` window panes, `sm` month cells, `md` options, fields, doorbell plates and the lift display, `lg` buttons and cards, `xl` goal and avatar cards, `dialog` 16px, `sheet` 20px top corners. Pills (`full`) only for floating labels in the scene («+18 400 kr», «10 000 kr gjeld», «STEG 1 AV 3»). People are the only fully soft shapes.

## Components

- **Hub status** — Month name (`month-title`) and «17 år · År 3 av 5»; row with coin + «3 120 kr», heart + «Trivsel 64», flag + «Mål 19 %».
- **Year progress (month strip)** — White bar, 12 cells. Current: action fill, white text. Played: tint fill, border, deep text. Coming: outline only. A 2.4px dot under months with a story event (Jan, Apr, Jul, Oct).
- **Area entry points (doorbell panel)** — Panel in `panel` with a steel top rule; four nameplates «Plan», «Mobil», «Jobb», «Penger», each with a round bell. Bell filled with action plus a note in action («3 ledige kvelder», «2 nye meldinger») when something waits; white bell and empty second line when nothing does.
- **Next month** — `button-primary` full width, «Neste måned» left, «desember» in `on-action-muted`, arrow right.
- **Locked item** — Floors above yours at 42 % opacity with dark windows; teasers in text («I 4. etasje: Bilførerkort og kredittkort åpner.»). [ASSUMPTION] No explicit locked chip is sketched; use a note on the lifted floor with «fra 18 år».
- **Option** — White, 2px action border, label left in ink, kroner right in action. Disabled at 45 % opacity. A caption under the list says wellbeing comes after.
- **Result** — Notes taped to the wall of your open floor («+6 sosialt», «−3 stress», «−1 100 kr»), a new photo when belongings change, an ink pill «Nytt på veggen»; below, the amount in `result-amount`, «Trivsel 61 → 64», the window meter and an echo card «Et lys fra År 1».
- **"Hvorfor?"** — Underlined action link; opens a sheet of cards with an 8px color stripe matching the note behind each change, plus «Om tallene» link and «Lukk».
- **Activity slot** — 70px cards in a 2 × 2 grid. Empty: dashed action border, «+ ledig kveld». Filled: note color with name and price. Work: panel fill, soft text.
- **Phone / messages** — Leaves the Blokka look: real messaging app with system font, back label «‹ Blokka», sender circles in year colors or sender colors. Invitation card has an action top strip and «Legg i planen».
- **Notification** — `sms-banner` over the dimmed hub: green app icon, «MELDINGER», sender, text, «nå».
- **Sheet / dialog** — Sheet: fog-light, 20px top corners, grab handle. Dialog (24 Velkommen tilbake): white, 16px, avatar in a tint circle breaking the top edge.
- **Isometric floor** — Open: wood floor, two back walls, year-colored floor slab and trim, bed, desk, window, poster, belongings. Closed: year-colored box with six plus four windows, lit if played. Street level: shopfront and bank.
- **Lift / floor display** — Tower on the right; the lift car in action color stops at your floor. Display top right: ink plate, up arrow, «ETG», floor number in `lit`.
- **Year tag** — «År N» plate on the left corner of each floor; ink fill for your floor, white otherwise; on the hub «År 3 · din etasje».
- **Avatar** — Soft, slim, rounded figures with natural proportions (`folk.py`): open jacket over a T-shirt, darker back limbs, small face, four hair styles. Six presets. Never block or low-poly figures.
- **Window meter (wellbeing)** — 20 windows × 5 points, lit vs dark, newest windows with an action border, a threshold line at 50.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Keep one fixed isometric camera and three-tone boxes | Rotate, tilt or perspective-shift the block |
| Use year colors only for floors and year identity | Use year colors for status, money or warnings |
| Keep press for pressure only, with a sign and a word | Show a red number without «−» and a reason |
| Pair every lit/dark window with text («Tente vinduer = måneder du har spilt») | Let lit windows be the only signal |
| Use soft, natural-proportion avatars | Bring back block figures or cartoon mascots |
| Let the phone look like a real phone | Restyle SMS in the Blokka palette |
| Keep the scene changing: notes, photo, lit windows, lift | Freeze the hub into a static picture |
