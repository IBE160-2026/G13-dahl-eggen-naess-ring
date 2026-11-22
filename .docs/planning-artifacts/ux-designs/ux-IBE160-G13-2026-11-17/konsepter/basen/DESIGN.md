---
name: LifeMode – Basen
description: Candidate visual system. A mountain base camp in a glossy mobile-game style; the camp is your base, the trail has one camp per year, the summit is your life goal.
status: candidate
created: 2026-11-18
updated: 2026-11-18
sketches: ../../.working/basen/oversikt.html
colors:
  hud: '#1B2340'
  hud-raised: '#26315A'
  hud-line: '#3A4778'
  panel-line: '#4A5890'
  outline-dark: '#0B1020'
  ink: '#151A2E'
  ink-muted: '#454B66'
  white: '#FFFFFF'
  text-muted-on-dark: '#C9D2F2'
  track-coming-text: '#AEB8DE'
  line-on-dark: '#8592C4'
  gold: '#FFC83D'
  gold-light: '#FFE27A'
  gold-deep: '#E59A12'
  gold-outline: '#8A5A00'
  gold-ink: '#5A3A00'
  action-primary: '#1C8441'
  action-primary-base: '#12562A'
  action-primary-deep: '#0F5A2A'
  progress-light: '#7FE08F'
  press: '#C7353A'
  press-light: '#FF8A8E'
  press-outline: '#7A1E22'
  job: '#2E7D6B'
  accent-blue: '#3557D6'
  disabled: '#6A7090'
  card-surface: '#FFFFFF'
  card-surface-low: '#EEF1FA'
  button-white-low: '#E6EAF6'
  card-base: '#A9B2D6'
  tint-coral: '#FCE7DD'
  tint-blue: '#DDE4FC'
  tint-mint: '#DDF3EA'
  tint-butter: '#FFF3D1'
  phone-frame: '#0B0E1A'
  phone-surface: '#F6F7FB'
  phone-muted: '#4A5068'
  phone-bubble: '#E7E9F2'
  banner-surface: '#FBFBFD'
  sender-emma: '#94601A'
  sender-butikken: '#1F6B58'
  sender-mamma: '#7154A8'
  sender-banken: '#2F4BC0'
  mountain-light: '#8E86C6'
  mountain-dark: '#5F5A9C'
  trail-pole: '#2A2F50'
  camp-locked: '#3A3F66'
  summit-track: '#E2E4F0'
  portrait-top: '#8CC3CF'
  portrait-bottom: '#6FA9B8'
  storm-cloud: '#3A4060'
  storm-rain: '#CFE0F5'
  winter-sky-top: '#26306A'
  winter-sky-bottom: '#7E8CC8'
  winter-ground-far: '#F4F7FB'
  winter-ground-near: '#C6D3E6'
  spring-sky-top: '#6E77C8'
  spring-sky-bottom: '#F3B18E'
  spring-ground-far: '#E9F1E6'
  spring-ground-near: '#8DB27E'
  summer-sky-top: '#4FA6E6'
  summer-sky-bottom: '#CDEBFA'
  summer-ground-far: '#C4E6A6'
  summer-ground-near: '#69A84E'
  autumn-sky-top: '#4A4F8C'
  autumn-sky-bottom: '#F09A5A'
  autumn-ground-far: '#E2C48E'
  autumn-ground-near: '#9C7038'
typography:
  display: { fontFamily: 'Lilita One', fontSize: 50px, fontWeight: 400 }
  amount: { fontFamily: 'Lilita One', fontSize: 34px, fontWeight: 400 }
  button-primary: { fontFamily: 'Lilita One', fontSize: 26px, fontWeight: 400 }
  level: { fontFamily: 'Lilita One', fontSize: 24px, fontWeight: 400 }
  panel-title: { fontFamily: 'Lilita One', fontSize: 21px, fontWeight: 400 }
  hud-name: { fontFamily: 'Lilita One', fontSize: 20px, fontWeight: 400 }
  hud-value: { fontFamily: 'Lilita One', fontSize: 18px, fontWeight: 400 }
  value: { fontFamily: 'Lilita One', fontSize: 17px, fontWeight: 400 }
  month-label: { fontFamily: 'Lilita One', fontSize: 15px, fontWeight: 400 }
  card-title: { fontFamily: Onest, fontSize: 16px, fontWeight: 800 }
  body-strong: { fontFamily: Onest, fontSize: 15px, fontWeight: 800 }
  body: { fontFamily: Onest, fontSize: 14px, fontWeight: 700, lineHeight: 20px }
  caption: { fontFamily: Onest, fontSize: 13px, fontWeight: 700 }
  label: { fontFamily: Onest, fontSize: 12px, fontWeight: 800 }
  micro: { fontFamily: Onest, fontSize: 11.5px, fontWeight: 800 }
  field-value: { fontFamily: Onest, fontSize: 15.5px, fontWeight: 600 }
  phone-title: { fontFamily: Onest, fontSize: 26px, fontWeight: 800 }
  phone-body: { fontFamily: Onest, fontSize: 14.5px, fontWeight: 500 }
rounded:
  sm: 11px
  md: 14px
  DEFAULT: 16px
  lg: 18px
  xl: 22px
  phone: 46px
  full: 9999px
spacing:
  margin-mobile: 14px
  panel-inset: 16px
  panel-text-inset: 22px
  card-gap: 16px
  row-gap: 12px
  hud-height: 156px
  bottom-bar-height: 194px
  touch-min: 44px
components:
  hud: { backgroundColor: '{colors.hud}', height: '{spacing.hud-height}' }
  level-shield: { backgroundColor: '{colors.gold}', borderColor: '{colors.gold-outline}', textColor: '{colors.white}', typography: '{typography.level}', width: 48px }
  hud-pill: { backgroundColor: '{colors.hud-raised}', borderColor: '{colors.hud-line}', textColor: '{colors.white}', typography: '{typography.hud-value}', height: 34px, rounded: '{rounded.full}' }
  year-track: { backgroundColor: '{colors.hud-raised}', borderColor: '{colors.hud-line}', height: 28px, rounded: '{rounded.md}' }
  month-played: { backgroundColor: '{colors.gold}', textColor: '{colors.gold-ink}', width: 26px, height: 18px, rounded: '{rounded.full}' }
  month-current: { backgroundColor: '{colors.white}', borderColor: '{colors.gold}', textColor: '{colors.ink}', width: 30px, height: 26px, rounded: '{rounded.full}' }
  month-coming: { borderColor: '{colors.line-on-dark}', textColor: '{colors.track-coming-text}', width: 26px, height: 18px }
  station-bubble: { backgroundColor: '{colors.white}', badgeColor: '{colors.press}', size: 44px }
  ground-tag: { backgroundColor: '{colors.hud}', textColor: '{colors.white}', typography: '{typography.label}', height: 22px, rounded: '{rounded.sm}' }
  wage-chip: { backgroundColor: '{colors.hud}', textColor: '{colors.gold}', height: 22px, rounded: '{rounded.sm}' }
  button-primary: { backgroundColor: '{colors.action-primary}', depthColor: '{colors.action-primary-base}', textColor: '{colors.white}', outlineColor: '{colors.action-primary-deep}', typography: '{typography.button-primary}', height: 70px, depth: 7px, rounded: '{rounded.xl}' }
  button-primary-disabled: { backgroundColor: '{colors.disabled}', textColor: '{colors.white}' }
  button-white: { backgroundColor: '{colors.card-surface}', depthColor: '{colors.card-base}', textColor: '{colors.ink}', height: 56px, depth: 5px, rounded: '{rounded.lg}' }
  unlock-bar: { backgroundColor: '{colors.hud-raised}', borderColor: '{colors.hud-line}', iconColor: '{colors.gold}', height: 48px, rounded: '{rounded.md}' }
  panel: { backgroundColor: '{colors.hud-raised}', borderColor: '{colors.panel-line}', textColor: '{colors.white}', padding: '{spacing.panel-inset}', rounded: '{rounded.xl}' }
  panel-ribbon: { backgroundColor: '{colors.gold}', textColor: '{colors.white}', typography: '{typography.panel-title}', height: 44px }
  option-card: { backgroundColor: '{colors.card-surface}', depthColor: '{colors.card-base}', textColor: '{colors.ink}', typography: '{typography.card-title}', height: 74px, rounded: '{rounded.lg}' }
  result-row: { textColor: '{colors.white}', valueColor: '{colors.gold}', height: 60px, rounded: '{rounded.DEFAULT}' }
  why-step: { backgroundColor: '{colors.white}', connectorColor: '{colors.gold}', height: 50px, rounded: '{rounded.md}' }
  activity-slot: { backgroundColor: '{colors.card-surface}', emptyBorderColor: '{colors.white}', width: 100px, height: 66px, rounded: '{rounded.DEFAULT}' }
  wellbeing-meter: { fillColor: '{colors.gold}', borderColor: '{colors.gold}', segments: 5, height: 18px }
  phone: { frameColor: '{colors.phone-frame}', backgroundColor: '{colors.phone-surface}', textColor: '{colors.ink}', rounded: '{rounded.phone}' }
  banner: { backgroundColor: '{colors.banner-surface}', textColor: '{colors.ink}', height: 86px, rounded: 20px }
  field: { backgroundColor: '{colors.white}', borderColor: '{colors.line-on-dark}', textColor: '{colors.ink}', typography: '{typography.field-value}', height: 50px, rounded: '{rounded.md}' }
  offline-ribbon: { backgroundColor: '{colors.press}', borderColor: '{colors.white}', outlineColor: '{colors.press-outline}', height: 64px, rounded: '{rounded.lg}' }
  camp-flag: { doneColor: '{colors.gold}', nextColor: '{colors.white}', lockedColor: '{colors.camp-locked}', poleColor: '{colors.trail-pole}' }
  summit-card: { backgroundColor: '{colors.white}', textColor: '{colors.ink}', progressColor: '{colors.action-primary}', trackColor: '{colors.summit-track}', rounded: 12px }
---

## Brand & Style

Basen is LifeMode as a real mobile game: a base camp in the mountains, drawn in the glossy, chunky style of popular phone games. Your camp is your base, the trail up the mountain has one camp per year (År 1–5), and the summit is your life goal. Your level is your age. A dark navy HUD frames a living scene whose sky and ground change with the season, and every action is a fat, pressable 3D button. The posture is confident and playful but never childish: no mascots, no cartoon jokes, no timers or treasure chests.

## Colors

- **HUD navy (`#1B2340` / raised `#26315A`)** is the game chrome: top HUD, bottom bar, panels, tags. Not used inside the scene except as tag and chip backgrounds.
- **Gold (`#FFC83D`, light `#FFE27A`, deep `#E59A12`)** means progress and money: level shield, played months, coins, walked trail, done camps, amounts. Gold amounts carry both plus and minus values; the sign and the word carry the meaning, never the hue. Not for buttons.
- **Action green (`#1C8441`)** is the one primary action ("NESTE MÅNED", "FORTSETT", "LEGG I PLANEN") and goal progress. Not for decoration or "good" states.
- **Press red (`#C7353A`)** is for attention: unread badges, event dots on the year track, the current-camp marker, the event and storm ribbons, the offline ribbon. Light red `#FF8A8E` is only for destructive text ("Slett bruker") and the heart gradient. Not a money-loss color.
- **Job teal (`#2E7D6B`)** belongs to the kiosk and job panels (and the driving game). **Accent blue (`#3557D6`)** is for the message icon, moped and small illustrations.
- **Cards** are white to `#EEF1FA` on a `#A9B2D6` base; icon circles use four soft tints (coral, blue, mint, butter) per option type. **Phone** colors (`#F6F7FB`, `#4A5068`, sender colors) only appear inside the phone and the SMS banner.
- **Seasons** recolor sky and ground only (winter Dec–Feb, spring Mar–May, summer Jun–Aug, autumn Sep–Nov); winter adds stars. UI chrome never changes with the season.

Contrast: `kontrast.py` measures 33 pairs against WCAG 2.2 AA, 0 below the bar. The tight ones are large-text or graphic passes: "NESTE MÅNED" white on the lightest green 3.23:1, the grey offline button 3.19:1, coming-month and field borders 4.14:1. Lilita text on gold ribbons and the level shield (white on gold ≈ 1.4–1.6:1) is readable only because of its dark outline (≈ 3.5–4.6:1); never drop the outline there. The 9.5 px "BUTIKKEN" sign on the kiosk (≈ 4.4:1) is decorative; the "Jobb" ground tag carries the label. Nothing is shown by color alone: month states differ by fill, outline and size; camps by flag, "År N" chip and lock icon; money by sign and word.

## Typography

Two families. **Lilita One** (400 only) is the game voice: numbers, button labels, panel titles, the level, amounts. It always has a dark outline (stroke ≈ 16 % of the font size, painted under the fill) when it sits on color or the scene. **Onest** (500–800) is the reading voice: body text, card titles, tags, captions and the phone. Big buttons use upper case ("NESTE MÅNED", "FORTSETT"); everything else is sentence case. Button labels never go below 19 px, so white on green stays large text.

## Layout & Spacing

Portrait 390 × 844 in three bands: the HUD (0–156 px), the scene (156–650 px) and the bottom bar (650–844 px). Chrome uses a 14 px side margin (362 px wide bars and buttons); panels sit at the same margin with 16 px inner inset for cards and 22 px for text. Option cards stack with 16 px gaps, result rows with 12 px. Panels open in the scene band and may cover the bottom bar; the HUD stays visible so money and wellbeing update in place. At 320 px the mountain and side stations crop first; HUD, tags and the primary button keep their order.

## Elevation & Depth

Depth is physical, as in mobile games: buttons and cards are a lighter top face over a darker base offset 5–7 px down, plus a white highlight at 28 % opacity across the top third. Panels have a navy shadow 6 px down at 50 %. Station bubbles and the summit card get a soft drop shadow (`#0B1020`, 35 %). When a panel or phone opens, the scene dims with `#0B1020` at 45–60 %. Pressed state: the top face moves down onto its base [ASSUMPTION: press animation not sketched].

## Shapes

Everything is round and chunky. `xl` 22 px for panels and the big button, `lg` 18 px for option cards, white buttons and the offline ribbon, `DEFAULT` 16 px for result rows and activity slots, `md` 14 px for fields, year track and the unlock bar, `sm` 11 px for ground tags. Pills (HUD values, month chips) are fully round. The level is a heraldic shield; ribbons have notched ends; station markers are speech bubbles.

## Components

- **HUD:** gold level shield with the age, "Du, 16 år" and "Nivå 16 · År 2 av 5" beside it; money pill with coin (140 px) and wellbeing pill with heart (92 px), right aligned. Below, the year track: twelve letter chips J–D; played = gold fill, current = larger white chip with gold ring and a pointer plus month name under it, coming = outline only. Event months carry a small dot (red ahead, deep gold when passed).
- **Station bubbles and ground tags:** a white speech bubble over a station shows its icon (message, calendar, coin) and a red count badge. Each station has a navy ground tag ("Mobil", "Hjem", "Kveldene", "Penger", "Jobb") on one baseline. Uncollected wage shows as a gold "+4 290 kr" chip by the kiosk.
- **Next-month button:** full-width glossy green, 70 px, Lilita 26 upper case with a white play triangle; a muted hint line below ("Neste måned venter. Ingen ting må gjøres først."). Disabled: same shape in `#6A7090`.
- **Next-unlock bar / locked item:** raised navy strip above the button with a gold padlock, "Leir 4 åpner på nivå 18" and what opens. Locked rows in panels use the padlock and "åpner på nivå 18" on a faint white row; a locked camp has a dark flag with a padlock.
- **Panel with ribbon:** navy gradient window, 3 px light border, notched ribbon title across the top edge. Ribbon color tells the kind: gold for neutral and rewards, red for events and storm, teal for job and driving, green for year end.
- **Option card:** white 3D card, tinted icon circle left, Onest title and subline, Lilita kroner value right ("−1 200 kr", "+1 090 kr", "0 kr"); "›" for non-money picks.
- **Result rows:** faint white rows with white icon circle, text and sub, gold outlined value ("−1 200 kr", "64 → 70", "opp"); a memory card for new belongings or memories; white "Hvorfor?" and green "FORTSETT" side by side.
- **"Hvorfor?" panel:** white step boxes joined by gold down arrows, cause to change ("Det kostet −1 200 kr" → "Penger nå 17 250 kr").
- **Activity slots:** four slots around a small campfire; filled = white card with name and price, empty = dashed white outline with "+" and "ledig"; activities below as white cards.
- **Wellbeing meter:** five pill segments per part (stress, fritid, sosialt), gold filled or gold outline, with a word ("lavt", "passe", "bra").
- **Phone and messages:** a dark phone over the dimmed scene with a light screen, round sender avatars with initials, unread red dot and bold line, chat bubbles in `#E7E9F2`, an invitation card with a small green gloss button.
- **Notification banner:** light rounded card at the top, sender square, name, "nå", two lines of text.
- **Form fields:** white label above a white 50 px field with `#8592C4` border; masked dots for passwords; green check box; underlined white links.
- **White secondary button:** white 3D button with Lilita ink label ("Logg inn", "Tilbake", "Hvorfor?", "Lukk").
- **Mountain, trail and camps:** a lilac mountain with snowcap and back range; a dotted white trail with the walked part in solid gold; five camp flags with "År N" chips (gold = done, white = next, dark + padlock = locked); a red dot and white label "År 2 · du er her" marks the current camp; a green flag on the summit.
- **Summit card:** white card by the peak: "Toppen: 20 år", the goal name, a green progress bar and "31 % spart".
- **Stations:** radio mast with red light and signal arcs (phone), orange tent (home and belongings), campfire with glow (evenings; unlit in storms), crate and safe with coins (money), teal kiosk with striped awning "BUTIKKEN" (job). Belongings stand by the tent: moped, car from 18.
- **Figure:** one of six preset looks (skin, hair style, hoodie color) with moods: smiling, cheering (arm up), tired, thinking. Shown in round portraits with a gold ring when selected.
- **Storm:** navy veil over the scene, dark cloud band, slanted rain and a yellow lightning bolt; fire out, figure tired.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Keep Lilita text outlined on color and scene | Set white Lilita on gold or green without its dark outline |
| One green gloss button per screen | Two green buttons of equal weight |
| Show unlocks as camps and padlocks with the age | Show prices, timers or "speed up" on locked things |
| Let the season change sky and ground | Recolor the HUD or buttons by season |
| Give every station a ground tag and every badge a count | Rely on an icon or red dot alone |
| Keep shapes chunky and round | Thin lines, sharp corners, flat bank-app rows |
