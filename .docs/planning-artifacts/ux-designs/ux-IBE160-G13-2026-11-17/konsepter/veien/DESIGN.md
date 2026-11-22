---
name: LifeMode · Veien
description: Five years of life as a level map in perspective. Dusk-violet world, turquoise road, one toned-down lime for action, pink only for pressure.
status: candidate
created: 2026-11-17
updated: 2026-11-18
sketches: ../../.working/veien/oversikt.html
colors:
  surface-sky-top: '#24107A'
  surface-sky-mid: '#6A22E0'
  surface-sky-dusk: '#FF6FA8'
  sun: '#FFD36E'
  hill-far: '#9A55FF'
  hill-mid: '#6A25D9'
  hill-near: '#3D1499'
  hill-front: '#2A0D73'
  ground-top: '#3A1690'
  ground-bottom: '#1C0858'
  road: '#2FE3D2'
  road-near: '#5CF2E4'
  road-far: '#B8FFF7'
  road-edge: '#0FA394'
  action-primary: '#B4E86E'
  action-primary-depth: '#7FAE45'
  press: '#FF5D8F'
  press-text: '#FFB3C9'
  press-soft: '#FF9BC2'
  surface-panel: '#170A40'
  surface-card: '#24125E'
  surface-option: '#2A1470'
  surface-track: '#3A2580'
  surface-deep: '#12053A'
  shadow: '#0B0426'
  border-card: '#5B44B8'
  border-field: '#7E68D8'
  border-track: '#6B57C9'
  lamp-off: '#6C5AB0'
  ink: '#170A40'
  ink-on-dark: '#FFFFFF'
  ink-lavender: '#E9E2FF'
  ink-soft: '#C9BEF2'
  ink-soft-on-light: '#4A3D7A'
  skin: '#FFD2B8'
  skin-shade: '#B87452'
  phone-surface: '#FFFFFF'
  phone-bar: '#F7F7F9'
  phone-banner: '#F4F3F8'
  phone-search: '#EFEFF4'
  phone-bubble: '#E9E9EB'
  phone-divider: '#E5E5EA'
  phone-ink: '#111111'
  phone-ink-secondary: '#6C6C70'
  phone-link: '#0066CC'
  phone-app-icon: '#34C759'
  drive-grass: '#2E7D4F'
  drive-asphalt: '#1F2230'
typography:
  display: { fontFamily: Rubik, fontSize: 50px, fontWeight: 900, letterSpacing: -1.5px }
  amount-xl: { fontFamily: Rubik, fontSize: 38px, fontWeight: 900 }
  headline: { fontFamily: Rubik, fontSize: 32px, fontWeight: 900 }
  hud-month: { fontFamily: Rubik, fontSize: 27px, fontWeight: 900, letterSpacing: -0.5px }
  title-page: { fontFamily: Rubik, fontSize: 26px, fontWeight: 900 }
  title-dialog: { fontFamily: Rubik, fontSize: 22px, fontWeight: 900 }
  label-go: { fontFamily: Rubik, fontSize: 22px, fontWeight: 900, letterSpacing: 1px }
  button: { fontFamily: Rubik, fontSize: 17px, fontWeight: 900, letterSpacing: 0.8px }
  option: { fontFamily: Rubik, fontSize: 16px, fontWeight: 700 }
  option-value: { fontFamily: Rubik, fontSize: 16px, fontWeight: 900 }
  row: { fontFamily: Rubik, fontSize: 15.5px, fontWeight: 700 }
  body: { fontFamily: Rubik, fontSize: 13.5px, fontWeight: 400 }
  meta: { fontFamily: Rubik, fontSize: 12.5px, fontWeight: 500 }
  sign: { fontFamily: Rubik, fontSize: 12px, fontWeight: 800 }
  label: { fontFamily: Rubik, fontSize: 11.5px, fontWeight: 700 }
  micro: { fontFamily: Rubik, fontSize: 9.5px, fontWeight: 800, letterSpacing: 1.5px }
  phone-title: { fontFamily: "-apple-system, 'Segoe UI', system-ui, sans-serif", fontSize: 34px, fontWeight: 700 }
  phone-name: { fontFamily: "-apple-system, 'Segoe UI', system-ui, sans-serif", fontSize: 17px, fontWeight: 700 }
  phone-body: { fontFamily: "-apple-system, 'Segoe UI', system-ui, sans-serif", fontSize: 15px, fontWeight: 400 }
  phone-meta: { fontFamily: "-apple-system, 'Segoe UI', system-ui, sans-serif", fontSize: 12px, fontWeight: 500 }
rounded:
  sm: 8px
  md: 14px
  option: 16px
  lg: 18px
  xl: 22px
  dialog: 24px
  sheet: 26px
  full: 9999px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
  '5': 20px
  '6': 24px
  gutter: 24px
  hud-inset: 20px
  dialog-inset: 12px
  option-gap: 10px
components:
  hub-status: { month: '{typography.hud-month}', year: '{typography.meta}', textColor: '{colors.ink-on-dark}', chipFill: '{colors.surface-deep}', chipOpacity: 0.72, chipHeight: 36px, chipRadius: '{rounded.full}' }
  level-badge: { shape: hexagon 38x44px, fill: '{colors.action-primary}', number: '{typography.title-dialog}', numberColor: '{colors.ink}', caption: '{typography.micro}' }
  year-strip: { height: 44px, fill: '{colors.surface-deep}', opacity: 0.6, radius: '{rounded.md}', current: '{colors.action-primary}', past: '{colors.ink-on-dark}', letters: '{typography.micro}' }
  dock-button: { size: 52px, fill: '{colors.surface-option}', border: '{colors.border-card}', label: '{typography.label}', labelColor: '{colors.ink-lavender}' }
  dock-badge: { size: 20px, fill: '{colors.action-primary}', textColor: '{colors.ink}' }
  go-button: { size: 88px, fill: '{colors.action-primary}', depth: '{colors.action-primary-depth}', depthOffset: 6px, label: '{typography.label-go}', labelColor: '{colors.ink}', caption: '{typography.label}' }
  button-primary: { height: 56px, fill: '{colors.action-primary}', depth: '{colors.action-primary-depth}', depthOffset: 5px, radius: '{rounded.lg}', label: '{typography.button}', textColor: '{colors.ink}' }
  button-secondary: { height: 52px, border: '{colors.ink-on-dark}', radius: '{rounded.option}', label: '{typography.option}' }
  option: { height: 46px, fill: '{colors.surface-option}', border: '{colors.border-card}', depth: '{colors.shadow}', radius: '{rounded.option}', label: '{typography.option}', value: '{typography.option-value}', valueColor: '{colors.action-primary}' }
  option-picked: { fill: '{colors.action-primary}', textColor: '{colors.ink}' }
  dialog: { inset: '{spacing.dialog-inset}', fill: '{colors.surface-panel}', border: '{colors.border-card}', radius: '{rounded.dialog}', accentBar: '{colors.action-primary}', title: '{typography.title-dialog}' }
  dialog-press: { border: '{colors.press}', accentBar: '{colors.press}' }
  sheet: { fill: '{colors.surface-panel}', radius: '{rounded.sheet}', handle: '{colors.border-card}', scrim: '{colors.shadow}', scrimOpacity: 0.6 }
  activity-slot: { size: 162x70px, radius: '{rounded.option}', emptyBorder: '{colors.action-primary}', blockedFill: '{colors.surface-track}', filledText: '{colors.ink}' }
  road: { fill: '{colors.road-near}', fillFar: '{colors.road-far}', edge: '{colors.road-edge}', glow: '{colors.road}' }
  milestone: { pastLamp: '{colors.action-primary}', futureLamp: '{colors.lamp-off}', pastPlate: '{colors.ink-on-dark}', futurePlate: '{colors.surface-option}', label: '{typography.sign}' }
  gate: { posts: '{colors.action-primary}', banner: '{colors.action-primary}', label: '{typography.sign}', textColor: '{colors.ink}' }
  goal-flag: { flag: '{colors.action-primary}', plate: '{colors.surface-panel}', radius: 10px }
  float-tag: { height: 30px, radius: '{rounded.full}', textColor: '{colors.ink}', label: '{typography.option-value}' }
  sms-banner: { height: 76px, fill: '{colors.phone-banner}', radius: '{rounded.xl}', icon: '{colors.phone-app-icon}', textColor: '{colors.phone-ink}' }
  phone-screen: { fill: '{colors.phone-surface}', title: '{typography.phone-title}', link: '{colors.phone-link}', bubble: '{colors.phone-bubble}' }
  field: { height: 52px, fill: '{colors.surface-card}', border: '{colors.border-field}', radius: '{rounded.md}' }
---

## Brand & Style

Veien is a mobile game level map. The player is a teenager standing on a glowing road that runs from the bottom of the screen up into a dusk horizon. Months are lamp-post milestones along the road, the player's age is the level, New Year is a gate to the next level, and savings goals are flags planted beside the road. The road is the largest thing on the hub; everything else (HUD, game dock, dialogs) sits at the edges or slides over it.

Posture: youthful and game-like, never childish, school-like or bank-like. Chunky, pressable buttons with a visible "depth" layer, heavy Rubik, a big round "GÅ" button, numbers that float over figures after a choice. Detailed avatars (3/4 profile, hoodies, sneakers, rim light) replace the earlier simple figures. The phone is the one deliberate break in style: messages look like a real phone app so an SMS feels real.

## Colors

The rule from the sketch code: **the violet family is the world, turquoise is the road, lime is action, pink is pressure.**

- **Sky and hills** (`surface-sky-*`, `hill-*`, `ground-*`, `sun`): the dusk landscape behind every screen, also as a 150–250 px band on sub-pages so the world is always present. Never used for controls.
- **Road** (`road`, `road-near`, `road-far`, `road-edge`): the player's path, progress in the year line (19), the "Fritid" bar and the moped in 22. Not for buttons.
- **Action-primary** (`#B4E86E`, toned down from a louder green per user feedback) with `action-primary-depth` underneath: the one call to action per screen, the level badge, the gate, lit milestones, goal flags, the current month, selected states and positive values. Not decoration.
- **Press** (`#FF5D8F`, `press-text` on dark, `press-soft` for a soft card): debt, stress, crisis, card warnings and "Si opp"/"Slett kontoen". The dusk-pink in the sky is the only other pink. The wellbeing heart icon is drawn in press pink in the sketches.
- **Surfaces** (`surface-panel` → `surface-card` → `surface-option` → `surface-track`): dark violet layers for sheets, cards, options and empty tracks. `ink` (#170A40) is text on lime, sun, road and pink.
- **Text on dark**: `ink-on-dark` for primary, `ink-lavender` on the sky, `ink-soft` for secondary.
- **Phone** (`phone-*`): light system colors only inside 09–11.
- **Driving game** (`drive-*`): top-down grass and asphalt in 22.

Contrast: `kontrast.py` measures 75 text and graphic pairs against WCAG 2.2 AA; **0 fall below** after the fixes logged in the memlog (dark text on pink, field border #7E68D8, track border #6B57C9, phone grey #6C6C70 and blue #0066CC, asphalt #1F2230). The thinnest margins are the field border on a card (3.67:1), asphalt on grass (3.13:1), empty wellbeing segments (3.32:1) and the phone search text (4.56:1); do not lighten these. **Nothing by color alone:** money carries a sign and a word, the current month is also larger, played months are filled and coming months hollow, lit and unlit milestones differ in plate fill.

## Typography

One family, Rubik (Google Fonts, weights 400/500/700/800/900), set heavy. Headings and values use 900; labels 700–800; body 400–500. Button labels and gate/step labels are uppercase with letter-spacing ("OPPRETT BRUKER", "NIVÅ 18 · JANUAR", "STEG 1 AV 3"). Month names in the HUD are 27 px/900; milestone plates use three-letter month labels ("OKT", "DES"). The phone screens (09–11) switch to the system font stack so they read as the real phone. No running month numbers anywhere.

## Layout & Spacing

Designed at 390 × 844. Hub (08): HUD in the top 210 px (status bar, level badge, month, "År N av 5", menu button, year strip, money and wellbeing chips at a 20 px inset), the road scene in the middle, the game dock at the bottom over a dark fade. Sub-pages: sky band (150–240 px) with a 26 px title, then a dark sheet with a 24 px gutter. Dialogs inset 12 px from the screen edge with 16 px inner padding; options stack with a 10 px gap. At 320 px the scene crops first; HUD, dock and dialog content keep their order. [ASSUMPTION] Tablet and desktop keep the phone-proportioned column centered.

## Elevation & Depth

Depth is game-like, not material. A soft drop shadow (`shadow` at 45–50 %, 8 px down, 10 px blur) lifts chips, signs, dialogs and the dock. Pressable items carry a solid under-layer 4–6 px lower (`action-primary-depth` under lime, `shadow` under options and filled slots) so they look like physical buttons. Glow (6–7 px blur) is reserved for the sun, the road, lit lamps, the gate and the GÅ button. Overlays use a dark fade or a `shadow` scrim (55–60 %); the SMS banner uses a light 12 % black scrim.

## Shapes

Rounded and chunky. `sm` 8 px for signs and checkboxes, `md` 14 px for fields and HUD buttons, `option` 16 px for options and slots, `lg` 18 px for primary buttons and cards, `xl` 22 px for the SMS banner and invitation card, `dialog` 24 px, `sheet` 26 px top corners, `full` for chips, float tags, dock buttons and GÅ. The level badge is a hexagon; the goal flag is a notched pennant.

## Components

- **Hub status** — Hexagon level badge with the age and "ÅR"; month name; "År 3 av 5"; menu button (44 px); chips "3 120 kr" with a coin and "64 trivsel" with a heart.
- **Year progress** — HUD strip: twelve dots on a line with month initials; played filled white, current lime and larger with a dark ring, coming hollow; event months (January, April, July, October) have bigger dots. Full view (19): five year tabs "År 1"–"År 5" with ages 15–19, a vertical road line with one row per month, "Du er her" row outlined in lime, legend "= måned med hendelse".
- **Area entry points** — Game dock: four 52 px round buttons "Plan", "Jobb", "Mobil", "Penger" around the central GÅ, with lime count badges. Room (18) and year (19) are reached from the menu (26).
- **Next month** — GÅ button, 88 px lime circle with depth and glow, "GÅ" plus arrow, caption naming the target month ("til desember").
- **Locked item** — The gate is the level unlock. [ASSUMPTION] A locked option or area uses the coming-milestone style: `surface-option` plate, `lamp-off` outline, text such as "fra 18 år".
- **Option** — Chunky 46–50 px bar, action label left, kroner value right in lime; picked turns lime with ink text; locked shows at 40 % opacity. [ASSUMPTION] Unaffordable shows the missing amount in `meta` under the label.
- **Result** — Dialog with a lime border: amount in `amount-xl` with sign, "igjen …" balance, "Trivsel 61 → 64" with a 20-segment bar (new segments white, threshold line at 50), echo card with lime footprints ("Spor fra da du var 15"), underlined "Hvorfor?", room change line, "GÅ VIDERE". The scene shows floating tags over the figures.
- **"Hvorfor?"** — Bottom sheet over a 60 % scrim: one card per change (heading in lime, echo in `sun`), link to "Om tallene", "LUKK".
- **Activity slot** — 162 × 70 px. Empty: dashed lime border, "+ ledig". Filled: solid colored card (sun for invitations, `press-soft` for social) with ink text and depth. Blocked: `surface-track` with "Ekstravakt". Activity list rows end in a lime plus.
- **Phone / messages** — White iOS-like app: "‹ Spill" back link, large "Meldinger", search, round initial avatars, blue unread dot, reply field "Du kan ikke svare i spillet". An invitation is a dark game card with a lime top bar and "LEGG I PLANEN".
- **Notification** — `sms-banner` at the top: green app icon, "MELDINGER", "nå", sender and text.
- **Sheet / dialog** — Dialog: dark panel with a sender portrait (lime ring) overlapping the top edge, accent bar, title, context, account line, options, footnote. Pressure variant (20, 21) swaps border and accent to `press`. Sheets: rounded top with a grab handle.
- **Road** — Perspective road from bottom to horizon: edge, gradient, white center dashes, glow; pines shrink with distance.
- **Milestones** — Lamp posts with a month plate. Past: lit lime lamp and white plate. Coming: `lamp-off` lamp and dark outlined plate. The player figure marks the current month.
- **Gate** — Two lime posts and a banner across the road, "NIVÅ 18 · JANUAR", with a soft glow; shown at New Year and on year end (23).
- **Goal flag** — Lime pennant on a white pole with a dark plate: goal name and "75 % spart".
- **Avatar** — Six preset looks (three short, three long hair; hoodie colors in `alle.py` LOOKS), 3/4 profile, two-tone hoodie, jeans, white sneakers with a lime stripe, colored rim light, eye highlight. Portraits are circle crops with a lime ring.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Make the road the biggest element on the hub | Shrink the world into a small header picture |
| Keep one lime action per screen | Use lime for decoration or several equal buttons |
| Reserve pink for debt, stress and crisis | Use pink for warnings that are not pressure |
| Show months as names, initials or "OKT" plates | Show "måned 36" or other running numbers |
| Make SMS and messages look like the real phone | Draw the phone as another game box |
| Give every pressable thing a depth layer and 44 px target | Make flat text links the main action |
| Keep the measured contrast fixes | Lighten borders, phone grey or asphalt |
