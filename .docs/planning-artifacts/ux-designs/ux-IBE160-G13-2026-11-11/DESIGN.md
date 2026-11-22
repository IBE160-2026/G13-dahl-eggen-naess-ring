---
name: LifeMode
description: Ringer's layout in Speilet's world. A mirror selfie is home; phone, bank and job read like real apps; money always carries a sign, a word and one of three colours, and wellbeing has its own status colours.
title: LifeMode DESIGN
status: draft
created: 2026-11-11
updated: 2026-11-22
sources:
  - PRODUCT.md
  - .docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md
  - .docs/planning-artifacts/ux-designs/decisions.md
  - .docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-17/konsepter/speilet/DESIGN.md
mockups:
  - .working/round3/index.html
colors:
  canvas: '#DCE6D2'
  wall: '#C7D5C0'
  paper: '#F6F3EC'
  surface: '#FFFFFF'
  ink: '#1A1C2A'
  ink-muted: '#454656'
  hairline: '#DDD8CC'
  hairline-soft: '#E8E4DA'
  coral: '#FF6F59'
  coral-soft: '#FFE3DD'
  cobalt: '#2B4CC4'
  cobalt-soft: '#E6EBFA'
  money-in: '#1E8A6E'
  money-out: '#C2552D'
  money-rate: '#2B4CC4'
  money-in-soft: '#E3F2EC'
  money-out-soft: '#F8E7DF'
  status-good: '#1F7A4D'
  status-warn: '#D99A00'
  status-bad: '#C2261E'
  status-good-soft: '#E3F1E8'
  status-warn-soft: '#FBEFD2'
  status-bad-soft: '#FBE2DF'
  tag-invite-text: '#7A2416'
  tag-offer-text: '#0E5A46'
  locked: '#FFE27A'
  danger: '#A3122A'
  device: '#121318'
  scrim: '#14161F'
  sender-emma: '#94601A'
  sender-job: '#2E7D6B'
  sender-family: '#7154A8'
  sender-friend: '#25292E'
  scene-wall: '#C7D5C0'
  scene-wall-lit: '#DCE6D2'
  scene-wall-mirror: '#A9BBA3'
  scene-sky: '#DCEBF2'
  scene-frame: '#1C1C20'
  scene-hoodie: '#2B4CC4'
  scene-hoodie-shade: '#243A96'
  scene-skin: '#E6B796'
  scene-skin-shade: '#C49B83'
  scene-hair: '#3A2A20'
  scene-pants: '#E4D6BC'
typography:
  display: { fontFamily: Bricolage Grotesque, fontSize: 60px, fontWeight: 800, lineHeight: 1.02, letterSpacing: -0.03em }
  h1: { fontFamily: Bricolage Grotesque, fontSize: 28px, fontWeight: 800, lineHeight: 1.15, letterSpacing: -0.015em }
  h2: { fontFamily: Bricolage Grotesque, fontSize: 19px, fontWeight: 800, lineHeight: 1.15 }
  h3: { fontFamily: Bricolage Grotesque, fontSize: 16px, fontWeight: 800, lineHeight: 1.2 }
  body: { fontFamily: Bricolage Grotesque, fontSize: 15px, fontWeight: 500, lineHeight: 1.45 }
  meta: { fontFamily: Bricolage Grotesque, fontSize: 13px, fontWeight: 600, lineHeight: 1.4 }
  amount-large: { fontFamily: Bricolage Grotesque, fontSize: 32px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.02em }
  amount: { fontFamily: Bricolage Grotesque, fontSize: 26px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.02em }
  timeline-month: { fontFamily: Bricolage Grotesque, fontSize: 22px, fontWeight: 800, letterSpacing: -0.02em }
  timeline-label: { fontFamily: Bricolage Grotesque, fontSize: 11.5px, fontWeight: 600 }
  chip: { fontFamily: Bricolage Grotesque, fontSize: 14px, fontWeight: 600 }
  button: { fontFamily: Bricolage Grotesque, fontSize: 16px, fontWeight: 800 }
  tab-label: { fontFamily: Bricolage Grotesque, fontSize: 12px, fontWeight: 700 }
  marker: { fontFamily: Kalam, fontSize: 22px, fontWeight: 700, lineHeight: 1 }
  marker-small: { fontFamily: Kalam, fontSize: 15px, fontWeight: 700 }
rounded:
  sm: 6px
  md: 10px
  lg: 16px
  xl: 20px
  sheet: 24px
  device: 44px
  full: 9999px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
  '5': 24px
  '6': 32px
  '7': 48px
  gutter-mobile: 16px
  rail-width: 220px
  pane-width: 400px
  target-min: 44px
  target-floor: 24px
components:
  timeline: { monthFont: '{typography.timeline-month}', labelFont: '{typography.timeline-label}', past: '{colors.ink}', current: '{colors.coral}', currentBorder: '{colors.ink}', future: '{colors.paper}', futureBorder: '{colors.ink-muted}', segmentHeight: 8px, currentHeight: 12px, rounded: '{rounded.full}' }
  scene: { background: '{colors.scene-wall}', rounded: '{rounded.xl}', aspect: 362/470, maxHeightMobile: 480px, heightDesktop: 430px }
  sticker: { background: '{colors.surface}', border: '{colors.ink-muted}', borderWidth: 1.5px, height: 40px, rounded: '{rounded.full}', font: '{typography.chip}', newDot: '{colors.coral}' }
  money-chip: { background: '{colors.surface}', border: '{colors.hairline}', height: 36px, rounded: '{rounded.full}', font: '{typography.chip}', keyIn: '{colors.money-in}', keyOut: '{colors.money-out}', keyRate: '{colors.money-rate}' }
  button-primary: { background: '{colors.coral}', textColor: '{colors.ink}', border: '{colors.ink}', borderWidth: 2px, height: 48px, rounded: '{rounded.full}', font: '{typography.button}' }
  button-secondary: { background: '{colors.surface}', textColor: '{colors.ink}', border: '{colors.ink}', borderWidth: 2px, height: 48px, rounded: '{rounded.full}' }
  button-cta: { background: '{colors.coral}', border: '{colors.ink}', height: 56px, rounded: '{rounded.full}' }
  card: { background: '{colors.surface}', rounded: '{rounded.lg}', padding: '{spacing.4}' }
  slot-row: { background: '{colors.surface}', emptyBorder: '{colors.ink-muted}', emptyDash: 2px dashed, height: 68px, rounded: '{rounded.lg}', label: '{typography.marker-small}', hintDesktop: '{colors.ink-muted}' }
  wellbeing-tile: { background: '{colors.surface}', rounded: '{rounded.lg}', scoreFont: '{typography.amount}', barHeight: 6px, barTrack: '{colors.hairline-soft}', barGood: '{colors.status-good}', barWarn: '{colors.status-warn}', barBad: '{colors.status-bad}', dotSize: 8px, valueColor: '{colors.ink}', wordColor: '{colors.ink-muted}' }
  status-pill: { good: '{colors.status-good-soft}', warn: '{colors.status-warn-soft}', bad: '{colors.status-bad-soft}', textColor: '{colors.ink-muted}', fontSize: 15px, fontWeight: 800, rounded: '{rounded.full}', padding: 3px 10px 3px 8px, dotSize: 8px }
  past-choice-note: { background: '{colors.paper}', icon: '{colors.cobalt}', labelColor: '{colors.cobalt}', rounded: '{rounded.lg}' }
  info-button: { background: '{colors.cobalt}', textColor: '{colors.surface}', size: 20px, rounded: '{rounded.full}', underline: '{colors.money-rate}' }
  offer-card: { background: '{colors.surface}', border: '{colors.ink}', borderWidth: 2px, rounded: '{rounded.lg}' }
  option-radio: { border: '{colors.hairline}', selectedBorder: '{colors.ink}', dot: '{colors.coral}', rounded: '{rounded.lg}' }
  event-option: { background: '{colors.surface}', border: '{colors.ink}', borderWidth: 2px, height: 64px, rounded: '{rounded.lg}' }
  locked-note: { background: '{colors.locked}', border: '{colors.ink-muted}', font: '{typography.marker-small}', rounded: 0px }
  year-chart: { in: '{colors.money-in}', out: '{colors.money-out}', rate: '{colors.money-rate}', baseline: '{colors.ink}', barWidth: 14px, selected: '{colors.paper}' }
  segmented: { track: '{colors.hairline-soft}', selected: '{colors.ink}', selectedText: '{colors.paper}', height: 40px, rounded: '{rounded.full}' }
  sheet: { background: '{colors.paper}', scrim: '{colors.scrim}', rounded: '{rounded.sheet}' }
  tab-bar: { background: '{colors.paper}', active: '{colors.ink}', activeText: '{colors.paper}', label: '{typography.tab-label}', badge: '{colors.coral}' }
  rail: { background: '{colors.paper}', width: '{spacing.rail-width}', active: '{colors.ink}' }
  device-frame: { body: '{colors.device}', screen: '{colors.surface}', rounded: '{rounded.device}', width: '{spacing.pane-width}' }
---

# LifeMode — Design Spine

> **Draft, 2026-11-22.** Distilled from UX round 3 (`.working/round3/index.html`), which the team built from its own revisions in `../decisions.md`. The group chose round 3 as the direction on 2026-11-22 (#95). The spine stays a draft until it is finalized. `EXPERIENCE.md` covers how it works. When this spine and the mockup disagree, the spine wins.

## Brand & Style

LifeMode looks like a teenager's own room photographed on a phone: grown-up, warm and a little handmade, never a banking app or a school worksheet. Two sources shape it:
- **Layout from Ringer (round 2):** a tab bar on mobile, a rail and a phone pane on desktop, and apps that feel real.
- **The world from Speilet (saegg1205):**
  - sage walls and paper surfaces
  - a mirror selfie as home
  - stuck-on stickers
  - handwriting on glass
  - yellow post-its that only ever mean *locked*

The game sits in the mirror. Everything else (money, messages, plans) is clean, legible UI on white cards, so the scene carries the feeling and the cards carry the numbers.

The style is restrained in operation and committed in identity. The rules are:
- one accent (coral) for actions and "now"
- three fixed money colours
- a separate status palette that only wellbeing uses
- one display family
- one handwriting face used sparingly

## Colors

- **canvas, wall, paper, surface.** `{colors.canvas}` is the app background, a lit sage wall. `{colors.wall}` is the scene's own wall. `{colors.paper}` is the rail, the tab bar, sheets and quiet notes. `{colors.surface}` (white) is every card, sticker and chip.
- **ink, ink-muted.**
  - `{colors.ink}` is all primary text, the borders of primary controls, past months on the timeline and the selected tab.
  - `{colors.ink-muted}` is secondary text and sticker borders. It measures 7.2:1 on canvas, 9.3:1 on white and 8.4:1 on paper.
- **coral.** `{colors.coral}` is the only accent: the primary button, the current month, unread dots and the chosen radio. It is 2.1:1 on canvas, so a coral control always has a 2px `{colors.ink}` border, and ink on coral is 6.2:1. Coral never means loss or warning.
- **cobalt.** `{colors.cobalt}` is for information: the "Tidligere valg" icon and label (6.5:1 on paper) and the (i) on interest. White on cobalt is 7.2:1.
- **Money colours.** `{colors.money-in}`, `{colors.money-out}` and `{colors.money-rate}` are the same everywhere: the chip dots, the transaction keys and the year chart. They passed the dataviz validator on white, with adjacent CVD ΔE 10.0 and normal-vision ΔE 23.2. They are marks, never text colours (`money-in` is only 4.3:1 on white). Every amount also has a sign and a word ("+8 457 kr lønn").
- **Soft tints.** `{colors.money-in-soft}`, `{colors.money-out-soft}`, `{colors.coral-soft}` and `{colors.cobalt-soft}` are backgrounds for tags, outcome icons and hover states. The `status-*-soft` tints belong to the wellbeing pill and nothing else. Tag text uses `{colors.tag-invite-text}` (8.3:1) and `{colors.tag-offer-text}` (7.1:1).
- **locked.** `{colors.locked}` yellow paper means locked, and only locked. Never use it for tips or news.
- **Wellbeing status.** `{colors.status-good}`, `{colors.status-warn}` and `{colors.status-bad}` are used only for wellbeing: bar fills, an 8px dot before each value, and the score pill on `{colors.status-good-soft}` / `{colors.status-warn-soft}` / `{colors.status-bad-soft}` with `{colors.ink-muted}` text (at least 7.5:1).
  - **Measured on white, all pairs:** normal-vision ΔE 25.0 at worst. For colour-blind players green and red are the weakest pair, at ΔE 7.6 (deutan), which is below the target of 8. That is allowed only with a second cue, so the word next to the value ("25 lavt", "72 bra", "55 ok") is required, never optional.
  - **Bands follow the PRD threshold (50, rule 12):** under 50 is bad, 50–59 is ok, 60 and up is good. Stress is mirrored (100 − stress): up to 40 is good, 41–50 is medium, over 50 is bad.
  - **`status-warn` is weak:** 2.45:1 on white and 1.9:1 on the bar track. The number and word carry the value, and its dot has a thin ink ring.
  - They are never text colours, and money never uses them.
- **danger.** `{colors.danger}` is used only for "Si opp jobben", "Slett bruker" and form errors. A money loss is never red. `{colors.status-bad}` is a different red with a different job, so don't swap them.
- **Senders.** These colours fill the round initials in the phone: `sender-emma`, `sender-job`, `sender-family`, `sender-friend`, plus cobalt for the bank. White letters measure at least 4.9:1.
- **Scene tokens.** The `scene-*` colours are the illustration's palette, exposed as CSS variables (`--sc-*`), so the hoodie, skin, hair, walls and frame can change without editing paths. The avatar picker sets `scene-hoodie`.
- **No dark mode in this draft.** The scene is a lit room, so dark mode would need its own night scene. This is an open question.

## Typography

**Bricolage Grotesque** (400–800, self-hosted per NFR-3) sets every number, label, heading and sentence, with tabular figures on all amounts. **Kalam** (700) is the marker, and its use is strict:
- It appears only on the scene ("Mak", "Hel igjen", "Mobilen gikk i bakken"), on the evening labels in the plan ("Kveld 1") and on post-its.
- Kalam writes words, and Bricolage writes values. A kroner amount is never handwritten.

The ramp:
- `{typography.display}`: the landing headline only.
- `{typography.h1}`: one per screen.
- `{typography.h2}`: section headings.
- `{typography.h3}`: card and row titles.
- `{typography.body}`: 15px body text at 1.45.
- `{typography.meta}`: secondary lines at 13px. This is the floor for running text.
- `{typography.timeline-label}` (11.5px) and `{typography.tab-label}` (12px): only for single short words. They drop to 11px under 360px wide.

Amounts use `{typography.amount-large}` for a bank total, `{typography.amount}` for tiles, and weight 800 inline.

## Layout & Spacing

The grid is 4px, using the `{spacing.1}`–`{spacing.7}` scale. The gutter is `{spacing.gutter-mobile}`.

| Width | Layout |
|---|---|
| 320–767 | One column. A tab bar at the bottom (Hjem, Plan, Mobil, Jobb, Penger). The primary CTA is fixed above the tab bar. Phone, bank and job open as full screens in the shared design. |
| 768–1099 | A `{spacing.rail-width}` rail on the left, one centred column (max 720), and a sticky CTA at the end of the content. |
| ≥ 1100 | Rail, centre (max 760) and a `{spacing.pane-width}` right pane that holds the phone in a device frame. Hjem, Plan, Året, Hendelse and Resultat take the centre. Mobil, Melding, Penger and Jobb open in the pane while the centre stays on Hjem. |

- **The scene:** on mobile it fills the column at 362:470. From tablet up, the mirror stands centred on a wide wall (`{components.scene.heightDesktop}`), with the stickers on the wall to the right.
- **The timeline** sits at the top of Hjem, Plan, Hendelse and Resultat, always in the same place.
- **The plan:** from 1100 px there are two columns (your evenings | add an activity), and the add list is always visible, so empty evenings have no button. Below 1100 px it is one column, and "Legg til" opens the add list in a sheet.

## Elevation & Depth

There are three levels:
1. **Flat:** the canvas and the scene. The scene has flat shapes, one shade per form and no grain.
2. **Resting:** cards and tiles, with a soft two-layer shadow (1px/2px at 6%, 6px/18px at 6%). There are no borders on cards.
3. **Stuck on:** stickers and post-its, with a small offset shadow (2.5px down, 4px blur, 28% ink) and a slight rotation of −4° to 4°.

Sheets and the CTA lift on a shadow pointing up or down. Dimming applies to the scene's glass only (events). The device frame on desktop has a 20px/40px shadow at 25%. A shadow never has zero offset.

## Shapes

- **Square:** paper is square, meaning post-its (`rounded: 0`).
- **Full pills:** controls you press: buttons, stickers, chips, tabs and segmented tabs (`{rounded.full}`).
- **Large:** cards, rows, offers and radio options use `{rounded.lg}`. The scene uses `{rounded.xl}`. Sheets use `{rounded.sheet}` at the top. The device uses `{rounded.device}`.
- **Rotation:** only things stuck on by hand are rotated. Nothing on a card, sheet or phone is.

## Components

- **Timeline.** The heading row reads "November · 16 år · 2027" plus an "Året ›" pill. Below it are 12 segments with month names:
  - past months are solid ink
  - the current month is coral with an ink border and taller
  - coming months are paper with a muted outline

  The whole thing is one link to Året. There are no events, no photos and no "måned X av 60".
- **Scene (the mirror).** The inline SVG scenes `#sc-selfie` (hub, event) and `#sc-glad` (result) have the named groups `-figur` and `-speilbilde`. A Kalam marker sits on the glass: the nickname with an arrow on the hub, or the outcome on the result. On events the glass dims to 55%, and the marker turns white. Stickers on the scene are links: "2 nye" (with a coral dot when unread), "2 ledige kvelder" and "Jobb 14 t".
- **Sticker.** A white pill with a 1.5px `{colors.ink-muted}` border, a 28px round icon and an 800-weight label. It is rotated slightly and straightens on hover.
- **Money chip.** A white pill with a 10px colour key (square for in and out, round for interest), a bold signed amount and a plain word. A chip with an (i) is a button that opens the interest sheet.
- **Buttons.** Primary and secondary buttons both have a 2px ink border. The primary is coral, and the CTA is 56px tall with a lift shadow. Ghost buttons are underlined text. Disabled buttons are at 50% opacity with no movement.
- **Card / tile.** White, `{rounded.lg}` and 16px padding. A tile that links outlines in ink on hover.
- **Wellbeing tile.** From top to bottom:
  - the score out of 100 with a status pill next to it ("Det går bra" / "Helt ok" / "Tungt nå"). The pill wraps below the score when the tile is narrow
  - three labelled 6px bars (Stress, Fritid, Sosialt) filled by status. On the right of each label: an 8px dot, the value and a word ("25 lavt", "72 bra", "55 ok"). Stress is inverted, so low is good
  - a footer that states a consequence ("Fritid 72 gir deg 3 frie kvelder. Snitt så langt 61, du trenger 50.").
- **Slot row.** It has a Kalam label ("Kveld 1"), a title, and cost · effect. A filled row is a white card with a round × button. An empty row has a 2px dashed muted border. Below 1100 px it holds a coral "+ Legg til" button. From 1100 px it holds the quiet text "Velg i lista →" in `{colors.ink-muted}`, which is not a control. School and work are one quiet locked line with a lock icon.
- **Past-choice note ("Tidligere valg").** A paper card with a round cobalt history icon, a cobalt label and one plain sentence. This replaces "Ekko".
- **Info / interest button.** An underlined amount (2px `{colors.money-rate}` underline) with a 18–20px cobalt (i). It opens a sheet with the explanation and a three-line calculation.
- **Segmented tabs.** Fritid | Jobb, with ink as the selected state.
- **Offer card.** A white card with a 2px ink border, showing the sender and time, a question, the consequence (kroner left after spending, and free evenings as a number), and Ja takk (primary) / Nei takk (secondary). Once answered, the border drops and the answer is shown.
- **Ask for hours.** Two full-width secondary buttons ("Spør om flere timer" / "Spør om færre timer"), disabled with one meta line ("Svar på tilbudet først.") while an offer is open. Once asked, they become one line with a check icon: "Du har spurt om flere timer. Line svarer i desember."
- **One-off shift row.** In the job view: name, hours · signed pay, and a small secondary "Til planen". Once placed, a chip reads "I planen". It has no date.
- **Email check.** On sign-up, the form gives way to a heading ("Sjekk at e-posten er riktig"), the address at 19px/800, which may break after @ and dots, a coral "Lag bruker" and a secondary "Endre e-post".
- **Option radio card.** Used for spending and goals. The title and the amount sit on one line, with examples and the meaning below. When selected, the border is 2px ink and the dot is coral inside an ink ring.
- **Event option.** A 64px white button with a 2px ink border, the action on the left and the signed kroner on the right.
- **Outcome list.** A 26px round icon (check on green tint for better, arrow on rust tint for worse, dash for unchanged) and a sentence. This replaces Åpnet/Stengt.
- **Year chart.** A diverging bar for each month, with income up and spending down, 14px bars, 4px rounded ends at the data end and an ink baseline. Interest is a separate small strip on its own scale (never a second axis). The selected month gets a paper background and an ink outline, with a three-figure detail below and a table view.
- **Locked post-it.** Yellow, square, rotated, with a lock icon, a Kalam title and an age ("fra 18 år"). When open it turns white with an open lock in `money-in`.
- **Phone, bank and job.**
  - Mobile: the shared design, with a round back button, white cards and chips.
  - Desktop: inside `{components.device-frame}` with a notch, a sticky app bar, a cobalt back link and flat rows on white, so it reads like a real phone app.
- **Sheet.** Paper, sliding up on mobile and centred on desktop, with a grab handle, a title, a round × and the scrim at 50%.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Give every amount a sign, a word and a money colour key | Colour a number red or green, or use colour alone |
| Use coral only for the action and "now", always with an ink border | Use coral for warnings or as a large fill behind text |
| Give every wellbeing status a word next to its colour | Show wellbeing as a coloured bar alone, or use status colours for money |
| Use yellow only for locked things | Use yellow for tips, news or highlights |
| Write words in Kalam and values in Bricolage | Handwrite amounts, ages or body text |
| Say what the player is left with after spending ("302 kr mer i måneden") | Show only the extra wage in an offer |
| Say "fri kveld / frie kvelder i måneden" | Say "plass", "slot" or "tar en kveld" |
| Keep the scene as editable SVG with `--sc-*` colours | Ship the illustration as a raster image or with baked-in grain |
| Show interest as a tappable amount with (i) | Explain interest in a paragraph on the screen |
| Keep the timeline in the same place on every month screen | Show "måned X av 60" or "År N av 5" |
| Use one primary button per screen | Stack several coral buttons |
