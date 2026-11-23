# Accessibility Review — IBE160-G13

Scope: `DESIGN.md`, `EXPERIENCE.md` (the spines, i.e. the contract), `mockups/index.html` (the round 3 prototype), checked against PRD NFR-2 and FR-51 and WCAG 2.2 AA. Date: 2026-11-23.

Method:
- I read all three files in full.
- I recomputed every colour pair in `DESIGN.md` with the WCAG relative-luminance formula, plus the pairs the prototype actually uses.
- I rendered 19 routes in headless Chrome inside a 320 × 640 iframe. On each route I checked `scrollWidth`, then focused every control in `#main` in order and tested with `elementFromPoint` whether any part of the control was still visible.
- Line numbers refer to `mockups/index.html` unless a spine section is named.

## Verdict

**Not yet a complete WCAG 2.2 AA contract, but the foundation is strong.** The colour rules are correct and the measured ratios hold. "Nothing by colour alone" is designed in properly, and the hard WCAG 2.2 criteria are handled well: 2.5.7 dragging, 3.3.7 redundant entry, 3.3.8 accessible authentication, and no timing.

The gaps are behavioural, and they sit exactly where a builder will copy the prototype:
- **The mirror scene's structure.** `role="img"` with live links inside it.
- **Focus.** The fixed CTA and tab bar cover focused controls (2.4.11), and the spines have no rule for where focus goes after an in-place change or on desktop pane routes.
- **The toast and disabled controls.** Neither is specified tightly enough.

Fix the 3 high spine gaps and the critical prototype bug before stories are written. Everything else can be fixed during the build.

Counts: **critical 1 · high 6 · medium 13 · low 10** (spines: 0/3/5/5, prototype: 1/3/8/5).

## Findings

### Spines (the contract)

- **[high]** The mirror scene is specified as one `role="img"` that also contains links (EXPERIENCE → Component Patterns "Mirror scene": "`role="img"` … Stickers on it are real links"; DESIGN → Components "Scene", "Menu button": a 44px button "at the bottom left of the hub scene, below 768px only"). `img` has presentational children: Chromium removes the descendants of `role="img"` from the accessibility tree, and VoiceOver flattens them. Read literally, the contract produces stickers and a menu button that screen readers can't reach. Below 768 px that menu button is the *only* way into Meny, which holds log out, change password and delete user (FR-4, FR-44). (1.1.1, 1.3.1, 4.1.2, 2.1.1.) *Fix:* State that `role="img"` and the text alternative belong to the artwork layer only. The stickers and the menu button are siblings positioned over it, never descendants. Add a second mobile route to Meny that isn't on the scene, such as an avatar button in a header or a "Meg" entry, so the menu doesn't depend on being on Hjem.

- **[high]** There is no rule for focus being obscured by the fixed and sticky layers (2.4.11 Focus Not Obscured (Minimum)). The spines require a fixed CTA above a fixed tab bar on mobile (DESIGN → Layout table; EXPERIENCE → Responsive), a sticky app bar and notch in the desktop phone pane (DESIGN "Phone, bank and job"), and a fixed toast at the top. None of them says that focused content must stay clear of them. Browsers count a control that sits in the viewport but under a fixed bar as "visible" and don't scroll it, so it stays completely hidden (verified in the prototype, see below). *Fix:* Add to the Accessibility Floor:
  - `scroll-padding-bottom` equal to the tab bar + CTA + gap (about 140 px) on the scrolling root below 768 px
  - `scroll-padding-top` equal to the notch + app bar inside the pane `.screen`
  - the toast never covers a focused element
  - acceptance check: tab through every surface at 320 × 640 and confirm no focused control is fully covered.

- **[high]** Focus management covers only route changes and sheets. It is silent on in-place changes, a removed opener, and pane routes (EXPERIENCE → Accessibility Floor "On route change, focus moves to the screen's heading"; Sheet "focus moves in and returns"). The core loop removes or replaces the focused control all the time: × on a slot, + in the add sheet (the sheet closes and its opener is gone), Ja takk / Nei takk, Spør om flere timer, Slutt med ekstravaktene, «Samme som i oktober», selling the moped, Lagre kallenavn, picking an avatar, and «Lagrer …» locking the chosen option. On desktop, Mobil, Melding, Penger and Jobb open in the pane while the centre stays on Hjem, and "the screen's heading" is ambiguous there. (2.4.3 Focus Order, 2.1.1, 3.2.2.) *Fix:* Add a focus table:
  - remove → focus moves to that evening's "Legg til" (or to the list heading from 1100 px)
  - place → focus moves to the filled slot row
  - offer answered → focus moves to the answer text «Du sa ja.» (`tabindex="-1"`)
  - ask sent → focus moves to the confirmation line
  - a radio change never re-renders the focused group
  - saving → focus stays on the chosen option (see the aria-disabled finding below)
  - sheet closed after its opener was removed → focus moves to the nearest stable heading
  - pane routes on desktop → focus moves to the pane's `h1`.

- **[medium]** Disabled controls are specified as `disabled` plus a nearby sentence, so keyboard and screen-reader users never meet the reason (EXPERIENCE → State Patterns "Offer open", "No free evening", "Offline"; Component "Ask for hours"; DESIGN "Ask for hours", "Buttons … Disabled buttons are at 50% opacity" vs "Offline bar … never see-through"). A natively disabled button leaves the tab order, and the reason line isn't tied to it. Disabling the focused option during «Lagrer …» also drops focus to `<body>`. DESIGN contradicts itself on how disabled controls look. (1.3.1, 2.4.3, 4.1.2.) *Fix:* Use `aria-disabled="true"`, keep the control focusable, suppress activation in script, and point `aria-describedby` at the reason («Svar på tilbudet først.», «Alle de frie kveldene er brukt.», the offline bar). Pick one visual: the hairline-soft fill with a muted border and muted text, for every locked state.

- **[medium]** The toast "goes away by itself" with no duration, no pause rule and no focus rule (EXPERIENCE → Component Patterns "Notification"). This also contradicts Interaction Primitives "No timers". The toast holds an actionable link («open the conversation»). Removing it on a timer is a time limit on that action (2.2.1 Timing Adjustable), and if it disappears while focused or hovered, focus is lost (2.4.3). The inbox and tab badge provide the same function, which lowers the impact but doesn't remove the focus-loss problem. *Fix:* Specify all four rules:
  - the toast stays until the player dismisses it or leaves Hjem (preferred), or for at least 20 s, and pauses while hovered or focused
  - it never takes focus and never removes itself while focus is inside it
  - Esc closes it while focus is inside it
  - it is placed so it never covers the timeline link when that link has focus.

- **[medium]** There is no focus-indicator spec, and the coral dots fail non-text contrast where they are the only cue (DESIGN has no "focus" entry anywhere; DESIGN → Colors "coral … unread dots"; EXPERIENCE "Something new in an area: A bare coral dot on Plan … and Jobb"). Coral is 2.47:1 on paper and 2.74:1 on white. The ink-border rule is written for coral *controls*, so the dots are left out. The bare dot on Plan and Jobb is the only visual sign of «noe nytt» (1.4.11 Non-text Contrast). *Fix:*
  - Add a focus token. The prototype's 3px ink outline, 2px offset and 6px coral halo is good (ink on canvas is 13.1:1). State that it is never removed and must sit outside ink-filled controls.
  - Require a 1.5–2px ink ring on every coral dot that carries meaning, or pair it with a glyph or text.

- **[medium]** The 24 × 24 target rule exists, but the year chart can't meet it on small phones, and the spines give no fallback (EXPERIENCE → Interaction Primitives "Targets are at least 24 × 24"; Component "Year chart: Each month is a button"; DESIGN "Year chart … 14px bars"). Twelve month buttons in a card on a 320 px screen are 19.5 px wide with 2 px gaps. At 360 px they are 22.8 px. They reach 24 px only from about 375 px, so many Android phones (360 wide) fail 2.5.8 too. The spacing exception doesn't apply, because the centres are under 24 px apart. *Fix:* Below 375 px, either:
  - draw the chart as two rows of six months, or
  - keep the bars `aria-hidden` and select the month with a month stepper (‹ november ›) or a native `<select>` that meets 24 px, with the table view remaining the full alternative.

- **[medium]** Reflow and zoom are specified for width only. Short viewports, 200–400 % zoom and text spacing aren't covered (EXPERIENCE → Foundation, Accessibility Floor "At 320 px the hub keeps …"). At 400 % zoom on a 1280 × 1024 desktop, or on a phone in landscape, the viewport is about 256–360 CSS px tall. The fixed tab bar (56 px) plus the CTA (56 px plus a 20 px gap) then cover 40–50 % of it (1.4.10 Reflow, 1.4.4 Resize Text). Text spacing (1.4.12) isn't mentioned. Fixed-height chips, the badge dot (`line-height:1`) and the ellipsised toast line are the places at risk. *Fix:*
  - When the viewport height is below about 480 px, the CTA becomes static at the end of the content and the tab bar may stay.
  - Add "1.4.12 text-spacing override on Hjem, Plan and Penger loses no content" to the manual test list.
  - Avoid fixed heights on text containers.

- **[low]** The spines name "tabs" for the add list and "Segmented tabs" for Fritid | Jobb, but no interaction pattern (EXPERIENCE "Add list"; DESIGN "Segmented tabs"). Builders will produce a half-tablist, as the prototype did. (4.1.2, 2.1.1.) *Fix:* Prefer two toggle buttons (`aria-pressed`), since the control filters one list. If the team keeps tabs, require the full APG pattern: roving `tabindex`, arrow keys, `tabpanel` and `aria-controls`.

- **[low]** Status messages are well covered but miss a few cases (EXPERIENCE → State Patterns, Accessibility Floor; PRD NFR-2 bullet 3):
  - «Spillet ble oppdatert på en annen enhet.» needs focus or an announcement after the reload.
  - The login error needs `aria-describedby` on both fields (FR-2 forbids saying which one was wrong).
  - The spine should say that live regions exist in the page from load. A region injected together with its text often isn't read out, and the prototype does exactly that.

  (4.1.3, 3.3.1.) *Fix:* Add these three lines to the State Patterns.

- **[low]** Two AA basics are not in the contract: a document title per screen (2.4.2) and `autocomplete` tokens on the account fields (1.3.5). The prototype has the right tokens, but nothing obliges the build to keep them. *Fix:* Add "title: «<Skjerm> · LifeMode»" and the tokens `email` / `username`, `current-password` / `new-password` and `nickname` to the Accessibility Floor.

- **[low]** Session expiry isn't addressed (2.2.1). UJ-2 is a school PC with «Forbli innlogget» unticked. If a session can expire mid-play in less than 20 h, the player needs a warning or a silent refresh. FR-6 means no choice is lost, but the spine should say so. *Fix:* Add one line: "A session never ends during play without a warning; after re-login the player lands where they were."

- **[low]** The avatar looks and some text alternatives lack content (EXPERIENCE "06 Avatar: Six preset looks"; Mirror scene "text alternative that matches the scene state"):
  - The looks have no names.
  - The scene's alt text isn't required to include the Kalam marker («Mobilen gikk i bakken», «Hel igjen»).

  (1.1.1.) *Fix:* Each look has a spoken name («Blå genser»). The scene's text alternative includes the marker text, or the marker is real text outside the `img`.

### Prototype (bugs a builder would copy)

- **[critical]** The hub scene's `role="img"` wraps the menu link and all three sticker links (lines 581–590: `.scene-menu` and `.scene-stk` are inside `<div class="scene room" role="img">`). In Chromium these links are pruned from the accessibility tree, and VoiceOver on iOS treats the scene as one image. Below 768 px the rail, and with it `#rail-menu` (line 515), is `display:none` (lines 55, 72). The scene button is then the only route to Meny, so a screen-reader player on a phone can't log out, change password or delete their user. (4.1.2, 2.1.1, 1.3.1.) *Fix:* Close the `role="img"` element after `.scene-in`. Render `.scene-menu` and `.scene-stk` as siblings inside a plain positioned wrapper, and give the sticker link "2 nye" the hidden text "meldinger".

- **[high]** The fixed CTA and tab bar fully cover focused controls. There is no `scroll-padding` anywhere in the file (lines 58, 130). Measured at 320 × 640, these controls were completely hidden after focus:
  - «Reparer skjermen −2 500 kr» on `#hendelse`, the month's real choice
  - «Ja takk» / «Nei takk» and «Slutt med ekstravaktene» on `#jobb`
  - «Slett bruker» on `#meny`
  - «Aktiviteter i år», a spending radio and «Rente, sparekonto» on `#penger`

  At 500 × 553 the hub's «Meny», «2 nye» and «Jobb 14 t» also landed under the tab bar or CTA. (2.4.11.) *Fix:* Add `html{scroll-padding-bottom:144px}` below 768 px, and `.screen{scroll-padding-top:96px}` for the sticky notch and app bar in the pane.

- **[high]** Full re-renders destroy the focused control, so focus falls to `<body>`. `render(false)` replaces `#main.innerHTML` (line 1023) after:
  - a spending change (line 1123). This breaks arrow-key navigation in the radiogroup: after one step, focus is gone.
  - × remove (line 1092), and place from the sheet (lines 1083–1084: the sheet closes, focus returns to the opener, then the opener is destroyed)
  - Ja takk / Nei takk (line 1111), ask (line 1112), «Samme som i oktober» (line 1113), end extra shifts (line 1115)
  - selling the moped (line 1105), saving the nickname (line 1107), picking an avatar (line 1119)

  Only the year chart (line 1110) and the tabs (line 1093) restore focus. (2.4.3, 2.1.1.) *Fix:* Patch in place instead of re-rendering, or restore focus to a stable target according to the spine's focus table. Never re-render a radiogroup in response to its own `change`.

- **[high]** On desktop, the pane routes put focus in the wrong place. With a width of 1100 px or more, `#telefon`, `#melding`, `#penger` and `#jobb` render Hjem in `#main` (line 1021), and `render` focuses `#main h1, #main h2[tabindex]` (line 1029), which is the hub's «Denne måneden». The content the player just opened, in `#pane`, gets no focus, and opening a message from the pane also throws focus back to the centre. (2.4.3, 3.2.1.) *Fix:* On pane routes, focus `#pane h1` (with `tabindex="-1"`).

- **[medium]** The heading structure is broken on the main screen. Hjem has no `h1` (lines 658–678), so the first heading is the `h2` «Denne måneden», although DESIGN says "one `h1` per screen". Plan jumps from `h1` to `h3` in its slot rows (lines 696–698, 721). On desktop, the pane's `h1.app-title` (line 907) gives two `h1` elements. (1.3.1, 2.4.6.) *Fix:* Give Hjem a visually hidden `h1` («November, 16 år»), or make the timeline month the `h1`. Add `h2` «Dine kvelder» to the plan, and make the pane title an `h2` while the pane is secondary.

- **[medium]** The tablist is incomplete (lines 703–705, 1093). It has `role="tab"` buttons but no `tabpanel`, no `aria-controls`, no arrow-key handling and no roving `tabindex`, so both tabs sit in the tab order. (4.1.2, 2.1.1.) *Fix:* Follow the spine decision above. The simplest fix is two buttons with `aria-pressed`.

- **[medium]** Disabled controls hide their reason, and saving drops focus:
  - The ask buttons use `disabled` with an unlinked «Svar på tilbudet først.» (lines 982–983).
  - «Legg i planen» is disabled with an unlinked reason (lines 925–926).
  - The add buttons are disabled with no reason at all (line 710).
  - Offline sets `disabled` on every option (line 1033), and `.btn[disabled]` / `.ev-opt[disabled]` use 50 % opacity (lines 129, 169), against DESIGN's "never see-through".
  - Saving disables the focused option (line 1096).

  (1.3.1, 2.4.3.) *Fix:* Use `aria-disabled` plus `aria-describedby`. The offline CTA already does this correctly (line 1034).

- **[medium]** Some live regions are injected together with their text, so they aren't reliably announced:
  - The offline bar `<div class="net" role="status">` is inserted with its message (line 1032), although the PRD requires "offline" to be read out (NFR-2).
  - The year detail `role="status"` (line 756) is recreated on every month click by `render(false)` (line 1110). The month button's own label covers this.
  - The result chips' `role="status"` (line 800) is rendered with the route.

  (4.1.3.) *Fix:* Send these through the persistent `#live` region (line 521), as `place()` already does, or keep the status node and update only its text.

- **[medium]** The toast removes itself after 8 s even while focused or hovered (line 1039). It comes after the tab bar in DOM order (line 522), so keyboard users reach it last. It sits fixed over the top of the screen, where the timeline link is. (2.2.1, 2.4.3.) *Fix:* Apply the spine fix above: no auto-dismiss, or at least 20 s with a pause on hover and focus, and never remove it while focus is inside.

- **[medium]** The rail badges have no text for screen readers, and the bare dots are too faint (line 1046).
  - The count renders as `<span class="cnt">2</span>`, so the link reads "Mobil2".
  - The bare dot uses `aria-label="noe nytt"` on a generic `<span>`, which is not allowed in ARIA 1.2 and is ignored.
  - The tab bar does this correctly (line 1045).
  - The bare dots (lines 64, 79) are coral on paper at 2.47:1 and are the only visual cue.

  (1.3.1, 1.4.11.) *Fix:* Reuse the tab bar's `.sr` text («, 2 nye», «, noe nytt») and add a 1.5px ink ring to `.dot.bare` and `.cnt.bare`.

- **[medium]** The year chart's month buttons are too small on narrow phones (lines 362–363): 19.5 px wide at 320 and 22.8 px at 360, with 2 px gaps. (2.5.8.) *Fix:* Apply the spine fallback (two rows of six, or a stepper or select below 375 px).

- **[medium]** The nickname and password sheets don't explain errors. On invalid input, «Lagre» sets `aria-invalid` and moves focus, but shows no visible or programmatic message (line 1107). The hints «2–16 tegn» and «Minst 8 tegn» in the sheets aren't linked to their fields (lines 1067–1068). The sign-up form does all of this correctly (lines 1134–1139). (3.3.1, 1.3.1.) *Fix:* Reuse the `fail()` pattern from sign-up in the sheets.

- **[low]** The future-month labels in the year chart use `opacity:.7` (line 374): muted at 70 % on white is #7D7E89, which measures 4.02:1 at 11.5px. (1.4.3.) *Fix:* Drop the opacity. The months already differ by having no bars.

- **[low]** The rail menu link's accessible name doesn't contain its visible label. `aria-label="Meny, Mak"` (line 1047) overrides the visible «Mak · 16 år», so a voice-control user who says "Mak 16 år" gets no match. (2.5.3 Label in Name.) *Fix:* Use «Mak · 16 år, meny», or drop the `aria-label` and add hidden text "meny".

- **[low]** Some names are missing or swallowed:
  - The look buttons are named «Genser 1» to «Genser 6» (line 652).
  - The offer's avatar «L» isn't hidden (line 975).
  - The landing scene's teaser stickers («Første jobb», «Konsert lørdag?», «Kredittkort fra 18») are swallowed by `role="img"`, whose label omits them (lines 604–610).
  - The result scene's label leaves out the marker outcome (line 798).

  (1.1.1, 2.4.6.) *Fix:* Name the colours, add `aria-hidden` to the avatar, put the stickers outside the `img`, and add the marker text to the label.

- **[low]** The document title is static, «LifeMode runde 3» (line 6), on every route. (2.4.2.) *Fix:* Set `document.title` in `render()`.

- **[low]** The scrim-click handler (line 1075) closes the sheet when `e.target===sheet`. That is also true for taps on the sheet's own padding, not just the backdrop, so an imprecise tap inside a sheet can dismiss it. *Fix:* Compare the click coordinates with the dialog's bounding rectangle, or wrap the content in an inner element that fills the dialog.

## What is already solid

- **The contrast figures in DESIGN.md are correct.** Recomputed:
  - ink-muted is 7.20 / 9.28 / 8.37:1 on canvas, white and paper
  - ink on coral is 6.17:1, and coral on canvas is 2.12:1, which is why the ink-border rule exists
  - cobalt is 6.46:1 on paper, and white on cobalt is 7.16:1
  - money-in is 4.27:1 on white, which is why it is correctly kept out of text
  - the tag texts are 8.26:1 and 7.07:1
  - the status pills are at least 7.53:1
  - status-warn is 2.45:1 on white and 1.93:1 on the track, which is why the word and the ink ring are required
  - the sender initials are at least 4.93:1
  - danger is 7.84:1 on white and 6.09:1 on canvas

  Every claimed number holds.
- **Nothing is shown by colour alone, and the rule is applied consistently.** Amounts carry a sign, a word and a shaped key. Wellbeing has a mandatory status word, and the spine says why (deutan ΔE 7.6). Timeline states differ by fill, outline and height, outcome icons by glyph, and locked items by a lock icon and text. Because the same information is in text, the faint bar fills don't fail 1.4.11.
- **2.5.7, 2.2.1 and FR-51 are designed in, not bolted on.** The plan is tap-to-place, nothing anywhere is dragged, there are no timers, and the minigame is turn-based with no timing, motion or gestures.
- **3.3.7 and 3.3.8 are handled correctly:**
  - The email is typed once and shown back, instead of being asked for twice.
  - «Endre e-post» keeps the input and refocuses the field (line 1118).
  - Paste and password managers work.
  - There is no CAPTCHA.
  - The prototype's `autocomplete` tokens are all correct (lines 618–620, 826–827, 1063–1064).
- **The sign-up form's error handling is a model to copy.** All errors appear at once, each with `aria-invalid` and `aria-describedby`, merged with the hint id, and focus goes to the first invalid field (lines 1134–1139).
- **Sheets use native `<dialog>` with `showModal()`.** Focus moves in, Esc works, the sheet is named by `aria-labelledby`, and openers carry `aria-haspopup="dialog"`.
- **Route changes move focus to the `h1` with `preventScroll`.** Tabs use `aria-current="page"`, the tab-bar badges have screen-reader text, «Hvorfor?» uses `aria-expanded` and `aria-controls`, and the ending and «Om tallene» rows use native `details` and `summary`.
- **The year chart has a full text alternative.** Each month button's label carries its three figures, and a table view lists the same data.
- **Reflow at 320 px holds.** No horizontal scroll on any of the 19 routes rendered at 320 CSS px, with every `details` element opened. Targets elsewhere are generous: round buttons are 44 px, buttons 48 or 56 px, tabs 56 px and stickers 40 px.
- **The scene is accessible as an image.** It is SVG with `aria-hidden` and `focusable="false"` on the art and no text inside the SVG. Its text alternative is built from the same room flags as the drawing (`roomText()`, line 564), so the alt text can't drift from the picture.
- **Motion and announcements are handled.** `prefers-reduced-motion` switches off all animation, there is a persistent polite `#live` region, saving is announced («Lagrer valget.»), and the offline CTA correctly uses `aria-disabled` on a focusable link.
