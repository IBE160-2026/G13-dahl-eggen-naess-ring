# Validation Report — IBE160-G13

- **DESIGN.md:** `/Users/saranaess/Documents/IBE160/G13-dahl-eggen-naess-ring/.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/DESIGN.md`
- **EXPERIENCE.md:** `/Users/saranaess/Documents/IBE160/G13-dahl-eggen-naess-ring/.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/EXPERIENCE.md`
- **Run at:** 2026-11-23T11:06:29

## Overall verdict

The pair is a usable contract with a sound structure. Both files follow the canonical shape, all 178 `{token}` references (61 unique) resolve, every PRD FR is accounted for, and the contrast figures I re-computed match the stated ratios. Before story-dev starts, one targeted pass is needed. Several states the PRD requires are missing (email already in use, a planned activity dropped at continue, the focus ring, logged out on another device). Several load-bearing bank components have behaviour rules but no visual spec. Component names drift between the two files. Two flows (UJ-3, UJ-4) don't deliver their PRD climax as written. Overall: **adequate**.

The three extra reviewers sharpen that picture without changing it. Accessibility found one critical prototype bug: the hub scene's `role="img"` swallows the sticker links and the only mobile route to the menu. It also found three spine gaps, all about focus (obscured by the fixed bars, lost after in-place changes, wrong target on desktop pane routes). PRD consistency found four high issues: Flow 5 opens an event inside a quiet month, the crisis hides «Spør mamma» after one ask, the interest equation misses ÷ 12, and the event screen drops the balances FR-13 requires. The money core matches Rule Set v1 exactly.

Plain language found ten high issues, mostly money jargon on the 18+ screens and one concept with several words (frie/ledige kvelder, Lappen/Billappen, ekstravakter/enkeltvakter). It also caught one untrue sentence: «604 kr mindre i måneden» for extra shifts that end anyway. In total: 1 critical, 25 high, 72 medium and 72 low. None blocks the direction. The critical item and the high items should be fixed in one Update pass before the spines are set to final and stories are written.

## Category verdicts
- Flow coverage — adequate
- Token completeness — adequate
- Component coverage — thin
- State coverage — adequate
- Visual reference coverage — adequate
- Bloat & overspecification — adequate
- Inheritance discipline — adequate
- Shape fit — strong

**Extra reviewers:** Accessibility review: 1 critical, 6 high, 13 medium, 10 low; PRD consistency review: 4 high, 15 medium, 13 low; Plain-language review: 10 high, 27 medium, 28 low

## Findings by severity

### Critical (1)

**[Accessibility]** — The hub scene's `role="img"` wraps the menu link and all three sticker links (lines 581–590 (§ lines 581–590: `.scene-menu` and `.scene-stk` are inside `<div class="scene room" role="img">`)
`.scene-menu` and `.scene-stk` are inside `<div class="scene room" role="img">`). In Chromium these links are pruned from the accessibility tree, and VoiceOver on iOS treats the scene as one image. Below 768 px the rail, and with it `#rail-menu` (line 515), is `display:none` (lines 55, 72). The scene button is then the only route to Meny, so a screen-reader player on a phone can't log out, change password or delete their user. (4.1.2, 2.1.1, 1.3.1.)
Fix: Close the `role="img"` element after `.scene-in`. Render `.scene-menu` and `.scene-stk` as siblings inside a plain positioned wrapper, and give the sticker link "2 nye" the hidden text "meldinger".

### High (25)

**[Rubric · Flow coverage]** — Flow 4 (UJ-3) swaps the UJ's «Hvorfor?» path for the (i) interest sheet. (§ FR-36/FR-38)
That drops the PRD climax: the growth tied to *his own earlier choice* (FR-36/FR-38). It also omits UJ step 4, the pointer to other ways of earning (EXPERIENCE Key Flows › Flow 4, L246–253; PRD UJ-3 path 2–4).
Fix: add a step where the bank message or the savings row offers «Hvorfor?» linking the interest to the pengegave choice, or state that the interest sheet carries that cause link. Add the earning pointer, or record that it was dropped.

**[Rubric · Component coverage]** — The bank components carry FR rules but have no visual spec. (§ Component Patterns L109–112)
These are Savings target with its progress bar (the mockup has `.progress`), What comes next (two closed rows), Open options («Kan kjøpes eller selges» rows with «Mangler … kr» or a lock), Credit card, and the «account rows» that EXPERIENCE says the 18+ bank reuses (Component Patterns L109–112). None appears in DESIGN Components or in the frontmatter (FR-57, FR-48, FR-26, FR-45).
Fix: add DESIGN entries and tokens for `progress`, `account-row`, `transaction-row` and `option-row`, and the card panel.

**[Rubric · State coverage]** — Email already in use at sign-up is missing. (§ L138–168)
FR-1 requires the screen to say the address is in use and point to Log in and the forgotten-password link, and this is the only place the game shows that an address has a user. It is absent from State Patterns (L138–168) and from the mockup.
Fix: add a row for surface 02 with the copy and focus target.

**[Rubric · State coverage]** — A planned activity dropped at continue is missing. (§ PRD L1424)
FR-53, NFR-7 (PRD L1424) and the UJ-6 edge case all require it to be «dropped with a note», but no state, surface or copy is defined for that note.
Fix: add a row naming where the note appears (hub or next month's result) and how it is announced.

**[Rubric · State coverage]** — The focus state has no visual spec. (§ L136, L187)
DESIGN.md never mentions focus (0 hits). EXPERIENCE covers only where focus moves (L136, L187). The mockup uses a 3px ink outline plus a 6px coral ring (index.html CSS `:focus-visible`). Every component builder needs this for WCAG 2.4.7 / 2.4.11.
Fix: add a focus-ring spec to DESIGN (tokens plus the rule for scene stickers and dark surfaces such as the offline bar and selected tabs).

**[Accessibility]** — The mirror scene is specified as one `role="img"` that also contains links (EXPERIENCE → Component Patterns "Mirror scene"
"`role="img"` … Stickers on it are real links"; DESIGN → Components "Scene", "Menu button": a 44px button "at the bottom left of the hub scene, below 768px only"). `img` has presentational children: Chromium removes the descendants of `role="img"` from the accessibility tree, and VoiceOver flattens them. Read literally, the contract produces stickers and a menu button that screen readers can't reach. Below 768 px that menu button is the *only* way into Meny, which holds log out, change password and delete user (FR-4, FR-44). (1.1.1, 1.3.1, 4.1.2, 2.1.1.)
Fix: State that `role="img"` and the text alternative belong to the artwork layer only. The stickers and the menu button are siblings positioned over it, never descendants. Add a second mobile route to Meny that isn't on the scene, such as an avatar button in a header or a "Meg" entry, so the menu doesn't depend on being on Hjem.

**[Accessibility]** — There is no rule for focus being obscured by the fixed and sticky layers (2.4.11 Focus Not Obscured (Minimum)). (§ DESIGN → Layout table; EXPERIENCE → Responsive)
The spines require a fixed CTA above a fixed tab bar on mobile (DESIGN → Layout table; EXPERIENCE → Responsive), a sticky app bar and notch in the desktop phone pane (DESIGN "Phone, bank and job"), and a fixed toast at the top. None of them says that focused content must stay clear of them. Browsers count a control that sits in the viewport but under a fixed bar as "visible" and don't scroll it, so it stays completely hidden (verified in the prototype, see below).
Fix: Add to the Accessibility Floor: - `scroll-padding-bottom` equal to the tab bar + CTA + gap (about 140 px) on the scrolling root below 768 px - `scroll-padding-top` equal to the notch + app bar inside the pane `.screen` - the toast never covers a focused element - acceptance check: tab through every surface at 320 × 640 and confirm no focused control is fully covered.

**[Accessibility]** — Focus management covers only route changes and sheets. (§ EXPERIENCE → Accessibility Floor "On route change, focus moves to the screen's heading"; Sheet "focus moves in and returns")
It is silent on in-place changes, a removed opener, and pane routes (EXPERIENCE → Accessibility Floor "On route change, focus moves to the screen's heading"; Sheet "focus moves in and returns"). The core loop removes or replaces the focused control all the time: × on a slot, + in the add sheet (the sheet closes and its opener is gone), Ja takk / Nei takk, Spør om flere timer, Slutt med ekstravaktene, «Samme som i oktober», selling the moped, Lagre kallenavn, picking an avatar, and «Lagrer …» locking the chosen option. On desktop, Mobil, Melding, Penger and Jobb open in the pane while the centre stays on Hjem, and "the screen's heading" is ambiguous there. (2.4.3 Focus Order, 2.1.1, 3.2.2.)
Fix: Add a focus table: - remove → focus moves to that evening's "Legg til" (or to the list heading from 1100 px) - place → focus moves to the filled slot row - offer answered → focus moves to the answer text «Du sa ja.» (`tabindex="-1"`) - ask sent → focus moves to the confirmation line - a radio change never re-renders the focused group - saving → focus stays on the chosen option (see the aria-disabled finding below) - sheet closed after its opener was removed → focus moves to the nearest stable heading - pane routes on desktop → focus moves to the pane's `h1`.

**[Accessibility]** — The fixed CTA and tab bar fully cover focused controls. (§ lines 58, 130)
There is no `scroll-padding` anywhere in the file (lines 58, 130). Measured at 320 × 640, these controls were completely hidden after focus: - «Reparer skjermen −2 500 kr» on `#hendelse`, the month's real choice - «Ja takk» / «Nei takk» and «Slutt med ekstravaktene» on `#jobb` - «Slett bruker» on `#meny` - «Aktiviteter i år», a spending radio and «Rente, sparekonto» on `#penger` At 500 × 553 the hub's «Meny», «2 nye» and «Jobb 14 t» also landed under the tab bar or CTA. (2.4.11.)
Fix: Add `html{scroll-padding-bottom:144px}` below 768 px, and `.screen{scroll-padding-top:96px}` for the sticky notch and app bar in the pane.

**[Accessibility]** — Full re-renders destroy the focused control, so focus falls to `<body>`. (§ line 1023)
`render(false)` replaces `#main.innerHTML` (line 1023) after: - a spending change (line 1123). This breaks arrow-key navigation in the radiogroup: after one step, focus is gone. - × remove (line 1092), and place from the sheet (lines 1083–1084: the sheet closes, focus returns to the opener, then the opener is destroyed) - Ja takk / Nei takk (line 1111), ask (line 1112), «Samme som i oktober» (line 1113), end extra shifts (line 1115) - selling the moped (line 1105), saving the nickname (line 1107), picking an avatar (line 1119) Only the year chart (line 1110) and the tabs (line 1093) restore focus. (2.4.3, 2.1.1.)
Fix: Patch in place instead of re-rendering, or restore focus to a stable target according to the spine's focus table. Never re-render a radiogroup in response to its own `change`.

**[Accessibility]** — On desktop, the pane routes put focus in the wrong place. (§ line 1021)
With a width of 1100 px or more, `#telefon`, `#melding`, `#penger` and `#jobb` render Hjem in `#main` (line 1021), and `render` focuses `#main h1, #main h2[tabindex]` (line 1029), which is the hub's «Denne måneden». The content the player just opened, in `#pane`, gets no focus, and opening a message from the pane also throws focus back to the centre. (2.4.3, 3.2.1.)
Fix: On pane routes, focus `#pane h1` (with `tabindex="-1"`).

**[PRD consistency]** — Flow 5 opens an event *after* the quiet-month hub, in the same month, in a month that isn't active. (§ EXP:255–257)
UX says: "08: «Fortsett» → 12: the mirror dims, the phone in his hand is cracked … (Markus, 16, November event)" (EXP:255–257). The hub CTA "Fortsett til desember" links to `#hendelse` (HTML:678), and the event and result use November's balances ("Brukskontoen hadde 2 364 kr", HTML:787). The result's Fortsett then returns to November's hub. PRD says: "When it opens, the engine runs rule 1 up to interest on savings … and the player sees the highlight event or the quiet-month summary. When the player continues, the engine applies the planned activities …, works out wellbeing, checks rule 8, and opens the next month" (FR-49, PRD:611). "The highlight event is always shown when the month opens" (FR-49, PRD:615). "By default they are months 1, 4, 7, and 10 of each in-game year" (FR-46a, PRD:706). UJ-6 calls November "a quiet month" (PRD:114). A developer could wire Continue so that it opens an event inside the current month.
Fix: re-stage Flow 5 so that the event opens a month (for example October, an active month): the event comes first, then the result, then that month's hub. Point the November hub CTA at the next month's opening. Keep the November figures for Flow 3 only.

**[PRD consistency]** — The crisis hides "ask family" after the first ask. (§ EXP:114)
The PRD says it is always offered. UX says: "Asking family and doing nothing are always offered, except that the family can't be asked twice in one crisis" (EXP:114). The prototype drops the option once `k.asked` is set (HTML:862). PRD says: "Asking family and ignoring the crisis are always offered" (FR-32b, PRD:1109). "Asking again in the same event or crisis month shows the same answer, moves no money, and doesn't use up a crisis step" (FR-27, PRD:1025). This states a rule in the spine that contradicts two Core FRs.
Fix: keep "Spør mamma" on every step. After the first ask, it shows the stored answer again ("Mamma har allerede lånt deg 500 kr"), with no money and no step used.

**[PRD consistency]** — The interest explanation states a false equation. (§ Flow 4 climax, EXP:250)
UX says: "the sheet shows 23 500 kr × 2,87 % = 56 kr this month" (Flow 4 climax, EXP:250). The interest component row says "balance × rate = this month" (EXP:122). DESIGN calls it "a three-line calculation" (DES:260). PRD/Rule Set says: "Monthly interest is `balance × annual rate / 12`" (rule 2, RS:69). 23 500 × 2.87 % is 674 kr, a year's interest. NFR-4 requires figures that are "correct, explainable". This is the climax of UJ-3, the game's main lesson about interest. A content or engine developer who follows the spine would render an equation that doesn't hold. (The prototype sheet lists balance, yearly rate and this month as rows, HTML:1057, without stating the equation.)
Fix: change both spine lines to "balance × yearly rate ÷ 12 = this month" (for example «23 500 kr × 2,87 % ÷ 12 = 56 kr»), and add the ÷ 12 row to the sheet.

**[PRD consistency]** — The event screen drops the balances that FR-13 requires. (§ FR-13)
UX says: "12 | Event | … | Dimmed mirror, options as actions with kroner (FR-13)" (EXP:55). The event shows only the scene, a sentence and three options (HTML:771–782). PRD says: "In a month with a highlight event, the player sees the situation together with their balance, savings, debt, and fixed costs, and picks one of a few options" (FR-13, PRD:625). The "Can't afford" state (EXP:162) depends on the player seeing what they have.
Fix: add a compact facts row to surface 12 in the spine (current account, savings, debt and fixed costs, engine figures) and draw it.

**[Plain-language]** — 20 `#kort` (and `k_nei`) — «Bare minstebeløpet · 51 måneder, 5 508 kr i rente» → «Betaler du bare det minste (i) · 51 måneder · −5 508 kr i rente».
«Minstebeløp» is bank jargon a 15–18-year-old won't know, and the line is a label without a verb. You can't avoid the idea, so add an (i) sheet: «Minstebeløpet er det minste banken lar deg betale hver måned. Resten blir stående, og du betaler rente av det.» Use the same (i) in `k_nei`.

**[Plain-language]** — 21 `#krise` — «Be om betalingsavtale · 939 kr i mnd · I 12 måneder fra september.
Kortet sperres.» → «Del opp hele kortgjelden · −939 kr i måneden · 12 måneder fra september. Kortet blir sperret.» «Betalingsavtale» is jargon. The real trap is that the screen just said «Du skylder 700 kr nå», and 939 kr a month looks like a mistake unless it says the *whole* debt is split up. «mnd» is an abbreviation, and the amount has no sign. Also fix the log line «939 kr i måneden, og kortet er sperret.» → «−939 kr i måneden i 12 måneder. Kortet er sperret.»

**[Plain-language]** — 05 `#start` — «Gjeldfri med buffer · 30 000 kr tilgjengelig hver måned det siste året» → «Ingen gjeld og en buffer (i) · 30 000 kr på konto hele det siste året».
«Tilgjengelig hver måned» sounds like 30 000 kr a month in income. «Buffer» is adult finance talk, so explain it: «Penger du har liggende i tilfelle noe skjer.» Or drop the word: «Ingen gjeld, 30 000 kr i reserve».

**[Plain-language]** — 08 `#hjem` sticker, 15 `#plan` — «2 ledige kvelder» (sticker), «3 frie kvelder · 2 ledige» (plan), «Ledig» (empty row) → sticker «Planlegg 2 kvelder», plan «3 frie kvelder · 1 planlagt», empty row «Tom».
*Fri* and *ledig* are synonyms in everyday speech. The difference (free from school and work vs not yet planned) is invisible, so «3 frie, 2 ledige» reads like 5 evenings or a contradiction. Count what is done, not what is left.

**[Plain-language]** — 16 `#jobb` — «Slutte med ekstravaktene? Fra desember får du 4 frie kvelder i stedet for 3, men sitter igjen med 604 kr mindre i måneden.» → «Slutte med ekstravaktene? I desember får du 4 frie kvelder i stedet for 3, og 604 kr mindre.
Ekstravaktene slutter uansett etter desember.» The card above says the extra shifts run «ut desember», and Flow 3 says they end after December. So «fra desember … i måneden» falsely implies a lasting loss. The same sentence is quoted as a «Do» in EXPERIENCE.md → Voice and Tone, so update it there too. The row text «Slutter nå» after the button contradicts «fra desember»: → «Slutter etter november».

**[Plain-language]** — 08, 13, 17, 19, 23, 24, INBOX — «Sparemål
Lappen», «Lappen (bil)», «Mopedlappen», «Du har 79,8 % av Lappen» → «Sparemål: Billappen», «Billappen», «Mopedlappen». The player already has the moped licence («Mopedlappen henger på speilet»). A savings target called just «Lappen» reads as that one, and the result screen then says «Sparemålet Lappen: 79,8 % → 72,1 %». «Billappen» is the word teenagers use.

**[Plain-language]** — 17 `#penger` — «+1 920 kr i november» (chip under the total) → «+1 920 kr mer enn du brukte i november», or as a label
«Igjen etter november: +1 920 kr». It's the month's net, but nothing says so. A teenager will guess it's wage, interest or a deposit.

**[Plain-language]** — 17 `#penger`, 08 rente sheet — «BSU · Ikke åpnet · [Åpne]», «Til BSU», «BSU gir 5,61 % rente, men pengene er låst til bolig.» → «BSU (i) · Du har ingen ennå · [Start BSU]», and in the sheet «BSU er sparing til egen bolig.
Den gir 5,61 % rente, men pengene kan bare brukes til å kjøpe bolig.» The acronym is never spelled out. «Ikke åpnet / Åpne» brings back the «Åpnet» word the team rejected, and «Åpne» can mean "open this view". «Til BSU» is offered when no BSU exists: disable or hide it until there is one.

**[Plain-language]** — 16 `#jobb`, 15 `#plan` — «Ekstravakter +4 t/uke ut desember» next to «Enkeltvakter i november» → keep «Ekstravakter», rename the second section «Vakter du kan ta i november».
The two words differ by a few letters and mean different deals (recurring hours vs single evenings). The plan's Jobb tab and hint («Vaktene kommer fra Butikken») already say «vakter», so the section heading is the odd one out.

**[Plain-language]** — 08 `#hjem`, 23 `#aarsslutt`, 25 endings, 27 `#tallene` — «Trivselsmålet er 50.» (hub), «Trivselen din var 61 i snitt.
Målet er 50.» (year end), «Trivsel i snitt · Målet var 50» right under «Spart · Målet var 100 000 kr» (ending) → «Trivselsmålet er 50.» everywhere, «Livsmålet: 100 000 kr» / «Trivselsmålet: 50» on the ending, and an (i) on the hub tile: «Trivselsmålet: Har du minst 50 i snitt når du fyller 20, har du klart deg både med penger og med livet.» This is text that sounds like a rule but isn't explained anywhere. The (i) under Om tallene → Trivsel doesn't mention it either. Bare «Målet» next to the life goal is ambiguous.

### Medium (72)

**[Rubric · Flow coverage]** — Flow 6 (UJ-4) leaves out two PRD path steps (§ FR-26)
turning card use off (FR-26) and checking what the moped would sell for (FR-29, UJ-4 step 5). It also moves the climax to the PRD's resolution beat («six months later the card is paid», L269). Steps 1–2 rest on the 18+ bank, which is flagged as undrawn (L112 `[NOTE FOR UX]`).
Fix: add both steps, restore the climax as the realisation that he must work more and spend less for six months, and resolve the NOTE FOR UX before story-dev.

**[Rubric · Flow coverage]** — Flow 1 (UJ-1) stops at «months pass» (L222). (§ L222)
The UJ resolution (the session ends after one in-game year with a teaser, FR-15) is in no flow, so surface 23 Year end is exercised by no flow at all.
Fix: add a final step «23: December, year end with teaser, Ferdig for nå».

**[Rubric · Flow coverage]** — Flow 3 (UJ-6) is missing two of the PRD's UJ-6 edge cases (§ FR-53)
«spends the money before he continues → the activity is dropped with a note» (FR-53) and «switches to the PC → it reloads before he can continue» (FR-49) (L244).
Fix: add both to the Edge line and back them with state rows (see §4).

**[Rubric · Token completeness]** — The avatar presets (FR-10; IA row 06 «Six preset looks») have no tokens. (§ FR-10; IA row 06 «Six preset looks»)
The mockup holds them in `LOOKS` and `LOOK_SHADE` (index.html L640–641: #D99A2B, #2E7D6B, #8E6CC9, #25292E, #C8453A plus shades #B07A1C, #22604F, #6E4FA6, #15181C, #A3352C). Only the default pair exists, as `scene-hoodie` / `scene-hoodie-shade`.
Fix: add `avatar-1…6` and `avatar-1…6-shade` tokens, or one list token, and point DESIGN Colors › Scene tokens to it.

**[Rubric · Token completeness]** — The scene palette doesn't match the claim that the art can change «without editing paths» (DESIGN Colors › Scene tokens, L185). (§ DESIGN Colors › Scene tokens, L185)
The mockup defines `--sc-hoodie-line` #1E2B71, `--sc-hair-hi` #6B5C52, `--sc-pants-shade` #C7B9A6 and `--sc-beam` (index.html CSS `:root`, second block) with no tokens. About 25 more fills are hard-coded in the SVG, e.g. #A8805D ×16, #896850, #EEF0E8, #D4D4D0, #FAFAF7, #F2EEE4 (index.html L469–477). The phone-layer shades #B85147 / #3E434E are also hard-coded (L559).
Fix: tokenise the missing `--sc-*` variables, and either tokenise the props or state in DESIGN that furniture and props are fixed art outside the token set.

**[Rubric · Token completeness]** — No caption size exists. (§ Components › Wellbeing tile, L256)
DESIGN specifies «Vanligvis 50» «in 12px meta» (Components › Wellbeing tile, L256), but `{typography.meta}` is 13px and L200 calls 13px the floor for running text. The mockup also uses 12px for sticker sublines, message times, day separators, the life bar and chart labels (index.html CSS L118, 201, 294, 300, 356, 377, 381), and 10px for badge counts (L63).
Fix: add a `caption` (12px) token and a `badge` size with the uses they're allowed for, or raise these to 13px.

**[Rubric · Token completeness]** — No contrast is stated for text on the illustration (§ Components › Scene, L243)
the white Kalam marker on the 55%-dimmed scene (Components › Scene, L243) and the ink marker on the glass (`scene-wall-mirror`). These are load-bearing reads (event title, outcome).
Fix: measure and state both, or add a backing plate rule.

**[Rubric · Component coverage]** — The Outcome list visual names tints that aren't tokens (§ DESIGN Components L277)
«check on green tint», «arrow on rust tint» (DESIGN Components L277). It has no frontmatter object, and its only behaviour lives inside the Result and Room layers rows.
Fix: map it to `{colors.money-in-soft}` / `{colors.money-out-soft}` (or the status tints) and `tag-worse-text`, and add a Component Patterns row (order, announcement, glyph meaning).

**[Rubric · Component coverage]** — Several EXPERIENCE components have no visual counterpart
Same as last month (which button variant?), Add list (beyond `segmented`), Recap, Year end, Result layout.
Fix: add short DESIGN entries, or point each to the existing component it reuses.

**[Rubric · State coverage]** — Logged out on another device or session expired is missing. (§ L144)
FR-5 says the next action shows the login screen, and FR-3, FR-4 and FR-44 log out other devices. «Updated on another device» (L144) is a different case.
Fix: add a row.

**[Rubric · State coverage]** — The Job view (16) has no state for before the player has a job. (§ IA L36)
In UJ-1 the job arrives in month 3, but the Jobb tab is always there (IA L36). The Add list's Jobb tab is likewise only «needs a job» (L126): disabled, hidden or explained?
Fix: define the no-job state for both.

**[Rubric · State coverage]** — Several account form errors are missing. (§ FR-4)
Menu: wrong current password, and a new password that is too short (FR-4); wrong password on delete (FR-44); nickname-change validation. Sign-up: a nickname over 16 characters or with characters that aren't allowed (FR-1); only «under 2» is covered (L166). The sign-up rate-limit message (FR-1) is also missing.
Fix: add rows. Most can share one pattern with Email invalid.

**[Rubric · Visual reference coverage]** — `oversikt.html` is not in either frontmatter `mockups:` list (DESIGN L13–14, EXPERIENCE L12–13) and isn't mentioned anywhere in DESIGN, though it is the only page showing every state. (§ DESIGN L13–14, EXPERIENCE L12–13)

Fix: add it to both lists and mention it in DESIGN's intro.

**[Rubric · Visual reference coverage]** — DESIGN cites the mockup only once, in the intro (L145). (§ L145)
No Components entry names the route or state that illustrates it (e.g. Wellbeing tile → `#hjem`, Year chart → `#aar`, Offer card → `#jobb~svart`, Sheet → `#plan~velg` / `#hjem~rente`, Room layers → `#penger~solgt`). EXPERIENCE Component and State Patterns don't link states either (e.g. Email check → `#opprett~sjekk`, Offline → `#offline`).
Fix: add `→ #route~state` pointers.

**[Rubric · Bloat & overspecification]** — The wellbeing bands are stated three times, in two forms. (§ L180)
DESIGN Colors (L180) and EXPERIENCE State Patterns › Wellbeing status (L155) hard-code 50/60 and 40/50. EXPERIENCE Component Patterns › Wellbeing tile (L124) says the threshold is configuration and «the server sends the band». A developer may hard-code the thresholds.
Fix: keep the canonical rule in the Wellbeing tile row (server-sent band) and have the other two point to it with an example only.

**[Rubric · Bloat & overspecification]** — Responsive behaviour is duplicated, with different details (§ L209–217: centre max 720/760)
DESIGN Layout (L209–217: centre max 720/760) and EXPERIENCE Responsive & Platform (L194–198: scene capped at 480 px, pane routing).
Fix: DESIGN keeps dimensions, EXPERIENCE keeps behaviour, and each points to the other.

**[Rubric · Inheritance discipline]** — Component names drift between the files, so a consumer can't extract by name
- DESIGN «Scene (the mirror)» / EXP «Mirror scene» - «Past-choice note» / «Past choice note» - «Info / interest button» + `info-button` / «Interest (i)» - «Locked post-it» + `locked-note` / «Locked post-it» - «Option radio card» + `option-radio` / «Spending choice» - «Toast» / «Notification» - «Message groups» / «Phone message» - «Segmented tabs» + `segmented` / «Add list» tabs - «Buttons» + `button-cta` / «Next month (CTA)» - «Crisis steps» / «Crisis» - «Menu row» / «Menu» - «Info box» / «Player information» - «Offer card» / «Offer»
Fix: use one name per component, equal to its frontmatter key, in both files.

**[Accessibility]** — Disabled controls are specified as `disabled` plus a nearby sentence, so keyboard and screen-reader users never meet the reason (EXPERIENCE → State Patterns "Offer open", "No free evening", "Offline"; Component "Ask for hours"; DESIGN "Ask for hours", "Buttons … Disabled buttons are at 50% opacity" vs "Offline bar … never see-through").
A natively disabled button leaves the tab order, and the reason line isn't tied to it. Disabling the focused option during «Lagrer …» also drops focus to `<body>`. DESIGN contradicts itself on how disabled controls look. (1.3.1, 2.4.3, 4.1.2.)
Fix: Use `aria-disabled="true"`, keep the control focusable, suppress activation in script, and point `aria-describedby` at the reason («Svar på tilbudet først.», «Alle de frie kveldene er brukt.», the offline bar). Pick one visual: the hairline-soft fill with a muted border and muted text, for every locked state.

**[Accessibility]** — The toast "goes away by itself" with no duration, no pause rule and no focus rule (EXPERIENCE → Component Patterns "Notification"). (§ EXPERIENCE → Component Patterns "Notification")
This also contradicts Interaction Primitives "No timers". The toast holds an actionable link («open the conversation»). Removing it on a timer is a time limit on that action (2.2.1 Timing Adjustable), and if it disappears while focused or hovered, focus is lost (2.4.3). The inbox and tab badge provide the same function, which lowers the impact but doesn't remove the focus-loss problem.
Fix: Specify all four rules: - the toast stays until the player dismisses it or leaves Hjem (preferred), or for at least 20 s, and pauses while hovered or focused - it never takes focus and never removes itself while focus is inside it - Esc closes it while focus is inside it - it is placed so it never covers the timeline link when that link has focus.

**[Accessibility]** — There is no focus-indicator spec, and the coral dots fail non-text contrast where they are the only cue (DESIGN has no "focus" entry anywhere; DESIGN → Colors "coral … unread dots"; EXPERIENCE "Something new in an area
A bare coral dot on Plan … and Jobb"). Coral is 2.47:1 on paper and 2.74:1 on white. The ink-border rule is written for coral *controls*, so the dots are left out. The bare dot on Plan and Jobb is the only visual sign of «noe nytt» (1.4.11 Non-text Contrast).
Fix: - Add a focus token. The prototype's 3px ink outline, 2px offset and 6px coral halo is good (ink on canvas is 13.1:1). State that it is never removed and must sit outside ink-filled controls. - Require a 1.5–2px ink ring on every coral dot that carries meaning, or pair it with a glyph or text.

**[Accessibility]** — The 24 × 24 target rule exists, but the year chart can't meet it on small phones, and the spines give no fallback (EXPERIENCE → Interaction Primitives "Targets are at least 24 × 24"; Component "Year chart
Each month is a button"; DESIGN "Year chart … 14px bars"). Twelve month buttons in a card on a 320 px screen are 19.5 px wide with 2 px gaps. At 360 px they are 22.8 px. They reach 24 px only from about 375 px, so many Android phones (360 wide) fail 2.5.8 too. The spacing exception doesn't apply, because the centres are under 24 px apart.
Fix: Below 375 px, either: - draw the chart as two rows of six months, or - keep the bars `aria-hidden` and select the month with a month stepper (‹ november ›) or a native `<select>` that meets 24 px, with the table view remaining the full alternative.

**[Accessibility]** — Reflow and zoom are specified for width only. (§ EXPERIENCE → Foundation, Accessibility Floor "At 320 px the hub keeps …")
Short viewports, 200–400 % zoom and text spacing aren't covered (EXPERIENCE → Foundation, Accessibility Floor "At 320 px the hub keeps …"). At 400 % zoom on a 1280 × 1024 desktop, or on a phone in landscape, the viewport is about 256–360 CSS px tall. The fixed tab bar (56 px) plus the CTA (56 px plus a 20 px gap) then cover 40–50 % of it (1.4.10 Reflow, 1.4.4 Resize Text). Text spacing (1.4.12) isn't mentioned. Fixed-height chips, the badge dot (`line-height:1`) and the ellipsised toast line are the places at risk.
Fix: - When the viewport height is below about 480 px, the CTA becomes static at the end of the content and the tab bar may stay. - Add "1.4.12 text-spacing override on Hjem, Plan and Penger loses no content" to the manual test list. - Avoid fixed heights on text containers.

**[Accessibility]** — The heading structure is broken on the main screen. (§ lines 658–678)
Hjem has no `h1` (lines 658–678), so the first heading is the `h2` «Denne måneden», although DESIGN says "one `h1` per screen". Plan jumps from `h1` to `h3` in its slot rows (lines 696–698, 721). On desktop, the pane's `h1.app-title` (line 907) gives two `h1` elements. (1.3.1, 2.4.6.)
Fix: Give Hjem a visually hidden `h1` («November, 16 år»), or make the timeline month the `h1`. Add `h2` «Dine kvelder» to the plan, and make the pane title an `h2` while the pane is secondary.

**[Accessibility]** — The tablist is incomplete (lines 703–705, 1093). (§ lines 703–705, 1093)
It has `role="tab"` buttons but no `tabpanel`, no `aria-controls`, no arrow-key handling and no roving `tabindex`, so both tabs sit in the tab order. (4.1.2, 2.1.1.)
Fix: Follow the spine decision above. The simplest fix is two buttons with `aria-pressed`.

**[Accessibility]** — Disabled controls hide their reason, and saving drops focus (§ lines 982–983)
- The ask buttons use `disabled` with an unlinked «Svar på tilbudet først.» (lines 982–983). - «Legg i planen» is disabled with an unlinked reason (lines 925–926). - The add buttons are disabled with no reason at all (line 710). - Offline sets `disabled` on every option (line 1033), and `.btn[disabled]` / `.ev-opt[disabled]` use 50 % opacity (lines 129, 169), against DESIGN's "never see-through". - Saving disables the focused option (line 1096). (1.3.1, 2.4.3.)
Fix: Use `aria-disabled` plus `aria-describedby`. The offline CTA already does this correctly (line 1034).

**[Accessibility]** — Some live regions are injected together with their text, so they aren't reliably announced (§ line 1032)
- The offline bar `<div class="net" role="status">` is inserted with its message (line 1032), although the PRD requires "offline" to be read out (NFR-2). - The year detail `role="status"` (line 756) is recreated on every month click by `render(false)` (line 1110). The month button's own label covers this. - The result chips' `role="status"` (line 800) is rendered with the route. (4.1.3.)
Fix: Send these through the persistent `#live` region (line 521), as `place()` already does, or keep the status node and update only its text.

**[Accessibility]** — The toast removes itself after 8 s even while focused or hovered (line 1039). (§ line 1039)
It comes after the tab bar in DOM order (line 522), so keyboard users reach it last. It sits fixed over the top of the screen, where the timeline link is. (2.2.1, 2.4.3.)
Fix: Apply the spine fix above: no auto-dismiss, or at least 20 s with a pause on hover and focus, and never remove it while focus is inside.

**[Accessibility]** — The rail badges have no text for screen readers, and the bare dots are too faint (line 1046). (§ line 1046)
- The count renders as `<span class="cnt">2</span>`, so the link reads "Mobil2". - The bare dot uses `aria-label="noe nytt"` on a generic `<span>`, which is not allowed in ARIA 1.2 and is ignored. - The tab bar does this correctly (line 1045). - The bare dots (lines 64, 79) are coral on paper at 2.47:1 and are the only visual cue. (1.3.1, 1.4.11.)
Fix: Reuse the tab bar's `.sr` text («, 2 nye», «, noe nytt») and add a 1.5px ink ring to `.dot.bare` and `.cnt.bare`.

**[Accessibility]** — The year chart's month buttons are too small on narrow phones (lines 362–363) (§ lines 362–363)
19.5 px wide at 320 and 22.8 px at 360, with 2 px gaps. (2.5.8.)
Fix: Apply the spine fallback (two rows of six, or a stepper or select below 375 px).

**[Accessibility]** — The nickname and password sheets don't explain errors. (§ line 1107)
On invalid input, «Lagre» sets `aria-invalid` and moves focus, but shows no visible or programmatic message (line 1107). The hints «2–16 tegn» and «Minst 8 tegn» in the sheets aren't linked to their fields (lines 1067–1068). The sign-up form does all of this correctly (lines 1134–1139). (3.3.1, 1.3.1.)
Fix: Reuse the `fail()` pattern from sign-up in the sheets.

**[PRD consistency]** — The quiet-month summary drops content that four FRs put there. (§ EXP:152)
UX says: "Quiet month | 08 | The heading is "Denne måneden", the chips show wage, spending and interest. No event text." (EXP:152). The hub shows three chips only (HTML:663–666). PRD says: "the month summary shows what was spent in total, with a few example purchases that fit the player's age and spending level" (FR-23, PRD:973). "The month summary lists each activity and its cost" (FR-53, PRD:807). "The month summary shows each transfer" (FR-45, PRD:893). "The month summary says when the player takes over the bills at 18" (FR-23, PRD:976).
Fix: add an expandable "Hva gikk pengene til?" row to surface 08 (example purchases, the activity lines, savings transfers, the note at 18). The chips can stay as they are.

**[PRD consistency]** — The year end has no tax or BSU deduction line, and the spine doesn't mention the December summary. (§ FR-15)
UX says: "Year end | The year's money, what changed, the average wellbeing, and a teaser for the next unlock (FR-15)" (EXP:116). The prototype's year end shows in/out/interest only (HTML:864–870). PRD says: "The December summary shows the year's tax and the expected BSU deduction, which is paid when the player continues" (FR-21, PRD:952). "The December summary marks the deduction as expected" (FR-49, PRD:618). FR-22 asks for a plain «BSU-fradrag: 0 kr …» when there is no tax (PRD:960).
Fix: add a "December" state to 08 or 23 with the year's tax and the expected BSU deduction, marked as expected, including the 0 kr wording.

**[PRD consistency]** — FR-35 (what a choice opened or closed) was dropped without a PRD change. (§ EXP:286)
UX says: "FR-35 … an extension in the PRD. Not drawn, after the team dropped «Åpnet/Stengt». The outcome list shows what changed." (EXP:286). PRD says: "After a choice, the game shows what the choice opened or closed" (FR-35, PRD:1160). The team aims to build every Extension (§4.4). UJ-1 step 4 says "future opportunities change" (PRD:81).
Fix: either show the FR-35 flag texts as lines in the outcome list (for example «Du kan nå kjøpe moped»), or ask the PM to record FR-35 as left out, using its "If left out" clause.

**[PRD consistency]** — FR-40 first-time disclosures have no pattern. (§ FR-40)
Only the "Om tallene" page exists. UX says: "27 | About the numbers | `#tallene` | 26 | Disclosed simplifications (FR-40)" (EXP:70). Nothing in the component or state patterns covers first-time display. The prototype page lists 5 of the 26 texts, and 2 of them are cut short (HTML:895). PRD says: "Each disclosure is shown the first time its mechanism or feature appears, behind an info icon or under "Hvorfor?" … Once per account" (FR-40, PRD:1219–1222).
Fix: add a "Disclosure" component: a one-time info chip on the first appearance (D3 on the interest sheet, D25 on the spending choice, D26 on the first plan, and so on) that is seen once per account. Use the full D-texts on "Om tallene".

**[PRD consistency]** — Progress before continuing isn't shown "after planned activities, marked as such". (§ EXP:109)
The trigger status and the month 59/60 warnings are missing. UX says: "Savings target | … progress from current account plus savings, the price, when it opens, and what's missing" (EXP:109). The prototype shows 79.8 % with "Kveld med venner −200 kr" planned (HTML:668, 939). PRD says: "Before the player continues, progress is shown after the planned activities' payments, marked as such" (FR-57, PRD:876; FR-9c, PRD:552). "Before the player continues, the money view shows the rule 8 trigger status … In month 59, the warning says … In month 60 …" (FR-49, PRD:617). Worked example 25 has 77.8 % after the activities (RS:235).
Fix: add the "etter planlagte aktiviteter" marking to the savings target and the life goal, a trigger-status row in 17, and month-59 and month-60 warning states.

**[PRD consistency]** — The money view leaves out FR-45 money actions. (§ EXP:60)
UX says: "17 | Money (bank) | … Accounts, interest, BSU, card, savings target and life goal, what comes next, buy and sell, spending, transactions" (EXP:60). The card row lists "balance, limit, how the bill is paid …, card use on/off" (EXP:112). PRD says the player can "deposit in BSU …, or withdraw the whole BSU", "pay extra on the card", "pay off a consumer loan, a family loan, or a payment plan early", "stop an everyday cost that has no binding period" (FR-45, PRD:897–904; FR-23, PRD:977).
Fix: list the missing actions in the 17 row and the Credit card row: withdraw BSU (whole, closes, deduction repaid), extra card payment, pay off early, and stop an everyday cost. The latter is shown with its binding period.

**[PRD consistency]** — The job view leaves out the rule 10 limit and the no-job state. (§ EXP:59)
UX says: "16 | Job | … Job, wage, hours, offers, ask for more or fewer hours, one-off shifts, end extra shifts, quit" (EXP:59). The prototype shows the wage, the fixed hours and the extra shifts but no limit (HTML:972–973). PRD says: "The job view shows … the rule 10 limit, the expected monthly pay" (FR-56, PRD:856). "With no job: the view shows the open job offers, or when the next one unlocks" (FR-56, PRD:862).
Fix: add a "Maks 40 t/uke" row (or 12 in grunnskole), pay that includes placed one-off shifts, and a no-job state.

**[PRD consistency]** — Wellbeing bands, and a server-sent band, go beyond the PRD and the architecture. (§ EXP:124)
UX says: "under it is bad, from it to 9 above is ok, 10 above and up is good. Stress is mirrored … The server sends the band with the figure." (EXP:124). It also says "Fritid and Sosialt: «bra» (60 and up) / «ok» (50–59) / «lite» (under 50)" (EXP:155), and "Bands follow the PRD threshold (50, rule 12)" (DES:180). PRD says the threshold is "The ending wellbeing needed for a real win, 50" (glossary, PRD:220). Rule 12 ties social life to 20, not 50: "If social life is then below 20, stress rises by 5" (RS:79). AD-13 sends "raw integers where the UI needs a number (… wellbeing …)" (ARCH:201), with no band. The 60 cut-off and the band on each part are new rules that the engine would have to own.
Fix: ask the PM to add the bands to FR-33 as configuration, and the architecture to add `band` to the player view. Alternatively, make them a frontend display rule over the threshold in the view. Revisit the Sosialt band, since its rule threshold is 20.

**[PRD consistency]** — The summer job is ranked as an ending choice, but its wages have a system cause. (§ HTML:877, 879)
UX says (prototype): «Sommerjobben i 2027 +16 728 kr … Uten sommerjobben ville du hatt 18 000 kr mindre.» This is ranked first in three of the four endings (HTML:877, 879). PRD says: "System causes: wages, tax, the mobile cost … have a system cause" (FR-36, PRD:1181). "Choices with no kroner effect aren't ranked" (FR-42, PRD:1256). FR-39 compares "with the option in the same event" (PRD:1209). Only one-off shift pay links to its choice (FR-47, PRD:939).
Fix: replace the entry with an event choice or an activity group. Optionally, add a sentence to the spine's Ending row that job wages are never ranked.

**[PRD consistency]** — The Flow 5 echo invents a cause link that FR-36 can't store, and the spine cites the wrong FR. (§ EXP:259, HTML:786)
UX says: «Tidligere valg: I januar i fjor satte du pengegaven på sparekontoen. Den dekket de 136 kr du manglet.» (EXP:259, HTML:786). It also says "Past choice note … Replaces "Ekko" (FR-37 cause links)" (EXP:127). PRD says: "An echo badge is shown only for effects that carry a cause link to an earlier choice" (FR-37, PRD:1190). Shared causes are proportional only for interest and debt (FR-36, PRD:1179). A savings top-up is a payment-order transfer (FR-45), so no earlier deposit "covered" the 136 kr. FR-37 is "Echo badges", and FR-36 is "Cause links".
Fix: use an echo the engine can derive (for example the extra-shifts note, HTML:726, or card interest linked to an earlier purchase). Correct the citation to "FR-37 echo badges, from FR-36 cause links".

**[PRD consistency]** — Flow 4 (UJ-3) uses a different message and drops two journey steps. (§ EXP:248–249)
UX says: "10: Banken: «Tre fjerdedeler! Du har 79,8 % av Lappen.» 17: he taps «+56 kr rente (i)»" (EXP:248–249). PRD says: "The bank sends a message: his savings have grown, because they have earned interest. He … presses "Hvorfor?" … It shows the real figure: NOK 3,000 earns NOK 84 in a year … The game points him to other ways of earning" (UJ-3, PRD:105–108). "One more bank message reports savings interest: the first month the interest earned so far passes NOK 50" (FR-55, PRD:843).
Fix: make the Flow 4 trigger the FR-55 interest message, which opens the interest sheet or "Hvorfor?". Add the earning pointer (hours, summer job) as a line on the sheet, or as a tip (FR-19).

**[PRD consistency]** — Days and times of day appear in a game with no days or times. (§ HTML:901, 923)
UX/prototype says: «Konsert lørdag?» and an invitation card reading "Lørdag · −450 kr · Sosialt +8" (HTML:901, 923). Message times are "14:02", "11:30" and "i går" (HTML:901–903), and the thread shows "I dag 14:02". PRD says: "No days or times: the plan has no days, times, or dates within the month (D26)" (FR-52, PRD:793). D26 says «Spillet følger ikke dager eller klokkeslett» (RS:303). The content model has no time or day field.
Fix: drop the weekday from the invitation card and the times from the inbox. Show "Ny" / month labels instead (the "Nye i november" grouping already does this).

**[PRD consistency]** — Missing account surfaces and states that the PRD and the architecture define. (§ EXP:46–47)
UX lists 03, log in, and 04, forgot password (EXP:46–47), and the states at EXP:146–166. None covers: - (a) The new-password page that the reset link opens. Architecture: "Reset link: `{PUBLIC_BASE_URL}/nytt-passord#token=<token>` … The page reads it … and posts the token and the new password" (AD-12, ARCH:190). FR-3: after a reset every device is logged out (PRD:448). - (b) Email already in use. "The game then says the address is in use and points to **Log in** and the forgotten-password link" (FR-1, PRD:425). - (c) Logged out from elsewhere. "Its next action shows the login screen" (FR-5, PRD:472). - (d) Nickname character rules. "letters, including æ, ø, and å, digits, spaces, and hyphens … The screen says the nickname … needn't be their real name" (FR-1, PRD:419). The hint reads only «2–16 tegn. Bare du ser det.» (HTML:619).
Fix: add surface "04b Nytt passord" (two states: set password, and link used or expired). Add the states "E-posten er i bruk", "Logget ut på en annen enhet" and "Ugyldige tegn i kallenavnet", and extend the nickname hint.

**[PRD consistency]** — One-off shift pay contradicts Rule Set rule 1. (§ EXP:126)
The UX doesn't say when the pay lands. UX says: "Jobb lists this month's one-off shifts with name, hours and pay" (EXP:126). The plan row reads "+558 kr lønn" (HTML:697), but the hub's wage chip stays at 8 457 kr (HTML:664). PRD says: "Its pay … paid with this month's wage" (FR-47, PRD:939), and also "no wage is paid outside the income step" (FR-47, PRD:942). Rule Set says: "Activities and the month plan never add hours or wages to the current month" (rule 1, RS:68). The income step runs when the month opens (FR-49).
Fix: this is a PRD and Rule Set conflict, not a UX error. Ask the PM to say when one-off pay is credited (on continuing, or next month's income step). Then add one line to the spine's Add list row, and update the hub chip or the bank list.

**[PRD consistency]** — The BSU line on the interest sheet states a rule the game doesn't have. (§ HTML:1059)
UX says (prototype): «BSU gir 5,61 % rente, men pengene er låst til bolig.» (HTML:1059). The spine wants "the BSU rate" on the sheet (EXP:122). PRD says: "The player can withdraw the whole BSU. It then closes for the rest of the playthrough, and any BSU deductions received are taken from the payout at once" (FR-22, PRD:963). D22 says «I spillet kan du bare ta ut hele BSU-en» (RS:299).
Fix: «BSU gir 5,61 % rente. Du kan bare ta ut alt på en gang, og da forsvinner fradraget.» The text comes from the engine (AD-13).

**[Plain-language]** — 12 `#hendelse` — «Den virker, men sprekkene går over halve skjermen.» → «Mobilen virker, men sprekkene går over halve skjermen.» «Den» points to a word that exists only in the handwriting on the mirror and in the hidden aria text.
Screen readers and anyone skimming lose the referent.

**[Plain-language]** — 13 `#resultat~repair` — «I januar i fjor satte du pengegaven på sparekontoen.
Den dekket de 136 kr du manglet.» → «I januar i fjor satte du pengegaven på sparekontoen. Derfor var det nok der til de 136 kr du manglet.» «Den» can be the gift or the account. It was the account.

**[Plain-language]** — 08 rente sheet vs 17 — «På sparekontoen 23 500 kr» while the bank and hub show «23 556 kr» → show the same figure, or label it «På sparekontoen 1.
november». A teenager checking the sum will think the game is wrong. Flow 4 in EXPERIENCE.md repeats 23 500.

**[Plain-language]** — 28 `#offline` — «Ingen nett.
Valgene venter til du er på nett igjen.» → «Ingen nett. Du kan se, men ikke velge, før du er på nett igjen.» «Valgene venter» suggests choices are queued and will be sent later. They are locked. The same text is in EXPERIENCE.md → State Patterns.

**[Plain-language]** — 17 `#penger` — «Hvor mye bruker du i måneden? · Av lønna di.
Aktiviteter kommer i tillegg.» → «Mat, klær og annet hverdagsliv. Aktivitetene i planen kommer i tillegg.» «Av lønna di.» is a fragment, and it reads as "a share of your wage" while the options show fixed kroner.

**[Plain-language]** — 17 `#penger` — heading «Fremover» over «Kommer i desember» and «Aktiviteter i år» → «Utgifter», or split it
«Kommer i desember» as its own row and «Brukt på aktiviteter i år». «Aktiviteter i år» is the past, not «fremover».

**[Plain-language]** — 08 sticker, 16 — «Jobb 14 t», «Fast 10 t/uke», «+4 t/uke ut desember» → «Jobb 14 t i uka», «Faste timer
10 i uka», «Ekstravakter: +4 t i uka til og med desember». «t» on its own doesn't say per what. «ut desember» can be read as "out in December".

**[Plain-language]** — 13 result chips — «Stress −2 lettere», «Stress +3 mer», «Stress ±0», «Sosialt +4 mer» → «Stress −2», «Stress +3», «Stress uendret», «Sosialt +4».
The "sign and a word" rule is for money. On a wellbeing chip the label is already the word, and «−2 lettere» / «+4 mer» say the same thing twice. «±» is a maths sign many 15-year-olds can't read.

**[Plain-language]** — 13 `k_nei` — «Betaler du bare minstebeløpet, tar det 51 måneder.
Av de første 350 kronene går 188 kr til rente.» → «Betaler du bare det minste, tar det 51 måneder å bli kvitt gjelden. Av de første 350 kr du betaler, går 188 kr til rente.» «Tar det 51 måneder» doesn't say to do what. Mixing «kronene» and «kr» in one sentence is uneven. The chip «188 kr rente denne måneden» needs a sign: «−188 kr rente denne måneden».

**[Plain-language]** — 27 `#tallene` Skatt — «Skatten regnes ut fra hele årsinntekten din med satsene for 2026.
I virkeligheten kan arbeidsgiveren trekke 50 % av lønna til du har skattekort, eller når frikortet er brukt opp.» → «I spillet regnes skatten av alt du tjener i løpet av året, med 2026-regler. I virkeligheten kan sjefen trekke halve lønna i skatt hvis du ikke har skattekort, eller når du har tjent mer enn frikortet dekker (i).» «Satsene», «årsinntekten» and «frikortet» are jargon, and «til du har … eller når …» breaks the parallel. «Skattekort» and «frikort» can't be avoided for a summer-job teenager, so link them to a one-line (i).

**[Plain-language]** — 27 `#tallene` Lønn and Alle satser — «Timelønna i spillet er minstesatsen i tariffavtalen for varehandelen (Virke/HK) fra 1.
april 2026. Norge har ingen lovbestemt minstelønn …» / «Alle satser og beløp er 2026-tall. De holdes faste …» → «Timelønna er det laveste butikker må betale etter avtalen mellom arbeidsgiverne og fagforeningen (2026). Norge har ingen lov om minstelønn, så ekte lønn kan bli høyere eller lavere.» / «Alle priser, renter og lønner er fra 2026. De endrer seg ikke, selv om du blir fem år eldre i spillet.» «Minstesatsen i tariffavtalen», «Virke/HK», «lovbestemt», «satser» and «holdes faste» read like a government page.

**[Plain-language]** — 27 `#tallene` — «Her er det spillet forenkler.» → «Dette gjør spillet enklere enn virkeligheten.» The word order invites the reading "here, it is the game that simplifies".


**[Plain-language]** — 08, 16 — «+8 457 kr lønn», «Lønn i november 8 457 kr» → «+8 457 kr lønn før skatt», or say in Om tallene → Skatt when tax is taken.
Om tallene says tax exists, but no screen shows it. A player with a real summer job knows pay arrives smaller.

**[Plain-language]** — 07 `#gave` — «Spar halvparten, bruk resten · −9 250 kr» → «Spar halvparten, bruk resten · −9 250 kr brukt».
A bare minus figure on a half-save option looks like the price of saving. The other options are clear: «18 500 kr spart», and «Kjøp gaming-PC −15 000 kr» (the verb carries it).

**[Plain-language]** — 10 INBOX Banken — «Tre fjerdedeler! Du har 79,8 % av Lappen.» → «Over tre fjerdedeler! Du har spart 79,8 % av det billappen koster.» «Du har 79,8 % av Lappen» is literally "you have 79,8 % of the licence".
Also 79,8 % is more than three quarters, so add «Over».

**[Plain-language]** — 02 `#opprett`, 26 info — «Serverne våre hos Railway lagrer logger med IP‑adresser i USA i 90 dager, og Vercel lagrer logger i 1 time.» / «Ellers slettes det etter 12 måneder uten spilling.» → «Railway i USA tar vare på IP-adressen din i 90 dager når du spiller, Vercel i 1 time.» / «Spiller du ikke på 12 måneder, slettes alt.» «Serverne» and «logger» are jargon («logger» also reads as the verb).
The word order puts the IP addresses "in the USA". «det» has no clear referent. EXPERIENCE says the 12-month line may only appear if that job is built.

**[Plain-language]** — 02, 03, 26, EXPERIENCE state — «Forbli innlogget på denne enheten», «Logg ut på alle enheter», «Andre enheter logges ut.», «Spillet ble oppdatert på en annen enhet.» → «Hold meg innlogget her», «Logg ut overalt» (the sheet button already says that), «Du blir logget ut på andre mobiler og PC-er.», «Du har spilt videre et annet sted.
Her er det nyeste.» «Enhet» is IT jargon, and «Forbli» is formal.

**[Plain-language]** — 10 `#telefon` aria — «Ikke åpnet» (unread dot) → «Ulest».
It's the standard word, and «åpnet» is the term the team dropped.

**[Plain-language]** — tab bar, rail, 17 — tab «Penger», screen «Banken», link «Åpne banken» → one word (see Terms).
Tapping «Penger» and landing on «Banken» makes the player wonder if they went to the right place.

**[Plain-language]** — 23 `#aarsslutt` — «Et valg du tok i år, kan få følger senere.» beside the post-it «Lappen (bil) fra 18 år» → «Billappen åpner når du fyller 18.
Den koster 32 500 kr.» The line is vague and slightly ominous, it doesn't relate to the post-it next to it, and the spec says the teaser names the next unlock.

**[Plain-language]** — 17 live message, bank list — «Vanlig forbruk valgt.» / «Hverdagsforbruk −6 343 kr» → «Du har valgt Vanlig
ca. 6 343 kr i måneden.» / «Mat, klær og annet (Vanlig) −6 343 kr». This brings back «forbruk», the word family the team rejected with «forbruksnivå». The bank row should match the choice the player made above it.

**[Plain-language]** — 20, 21, 19 — unsigned costs
«Rente denne måneden 188 kr», «939 kr i mnd», «Så langt i år: inn 46 714 kr, ut 50 343 kr, rente 652 kr» → «−188 kr», «−939 kr i måneden», «+46 714 kr inn, −50 343 kr ut, +652 kr rente». NFR-8 says money always has a sign and a word. These are the places it slips. Year end does this correctly.

**[Plain-language]** — 17 sell sheet — «Du får 10 772 kr på brukskontoen og slipper 250 kr i forsikring.» → «… og slipper 250 kr i forsikring hver måned.» Without «hver måned» it reads as a one-time saving.


**[Plain-language]** — 21 `#krise` — «Valg 1 av inntil 3» → «Valg 1 av maks 3».
«Inntil» is formal, and some read it as "until". DESIGN.md and EXPERIENCE.md quote it too.

**[Plain-language]** — 21 `#krise` ends — «Krisen er over», «Krisen er ikke løst», «Neste krise kan komme tidligst i november.» → «Kortet er betalt» / «Gjelden er ikke ordnet ennå», and «Gjelden vokser videre.
Du får en ny sjanse senere.» The player was never told this is a «krise» (the heading was «Kortet er ikke betalt på to måneder»). «Tidligst i november» sounds like a cooldown rule that is never explained. With the payment plan, «Krisen er over» while 12 months of payments remain also oversells.

**[Plain-language]** — 16 offer — «Du sitter igjen med 302 kr mer i måneden.
Du får 3 frie kvelder i desember, og fra januar 3 i stedet for 4.» (302 is what the formula gives; the text varies by state) → as labels: «+302 kr i måneden etter det du bruker · Desember: 3 frie kvelder · Fra januar: 3 frie kvelder (nå 4)». Two time frames and a bare «3 i stedet for 4» in one sentence make the reader do sums. Here the team's own rule says labels beat sentences.

**[Plain-language]** — 06 `#start` aria — «Genser 1» … «Genser 6» → «Blå genser», «Gul genser», «Grønn genser», «Lilla genser», «Svart genser», «Rød genser».
Numbered names give screen-reader users nothing to choose by.

### Low (72)

**[Rubric · Flow coverage]** — Flow 5 (phone breaks) has no UJ, which is fine, but it is the only flow with no Edge line (e.g. (§ e.g. he can't afford the repair, or he goes offline mid-choice)
he can't afford the repair, or he goes offline mid-choice), and it names none of the FRs it exercises (FR-13, FR-34, FR-36, FR-38) (L255–260).
Fix: add an Edge line and an FR tag in the heading.

**[Rubric · Token completeness]** — Some passing pairs are never stated (§ offline bar, selected tab and segment; 15.2:1)
paper on ink (offline bar, selected tab and segment; 15.2:1), `danger` text on white (7.8:1), `tag-worse-text` on `money-out-soft` (7.9:1), ink on `locked` (13.2:1).
Fix: one line in Colors.

**[Rubric · Token completeness]** — Three colour tokens are never referenced or described (§ DESIGN L65–67)
`bubble`, `option-selected`, `tag-worse-text` (DESIGN L65–67). Others are never referenced: rounded `key`, `bar`, `sm`, `md`, `tile-icon`, `bubble`, `screen`; spacing `target-min` and `target-floor`; typography `marker`.
Fix: wire them into component objects or describe them in prose. Delete any that are unused.

**[Rubric · Token completeness]** — Some tokens share a value under different names
`canvas` = `scene-wall-lit`, `wall` = `scene-wall`, `cobalt` = `money-rate` = `scene-hoodie`, `coral` = `scene-phone`. The mockup also uses different variable names (`--wall-lit`, `--white`, `--press`, `--dim`, `--in`, `--out`, `--hair-2`).
Fix: add one sentence saying the duplicates are intentional decoupling, and add a token → CSS-variable map, or rename the CSS variables.

**[Rubric · Token completeness]** — The lift shadow for sheets and the CTA has no values. (§ Elevation & Depth, L226)
DESIGN says only «a shadow pointing up or down» (Elevation & Depth, L226), while the mockup has `--shadow-lift: 0 -4px 16px rgba(26,28,42,.18)`.
Fix: state the values next to the card and sticker shadows.

**[Rubric · Component coverage]** — Some DESIGN components have no behavioural row (§ link hover is the only affordance named, L253)
Card / tile (link hover is the only affordance named, L253), Menu button, Facts card, Email check (it exists only as a state row), One-off shift row (only inside Ask for hours), Offline bar (only as a state).
Fix: add one-line rows or explicit pointers.

**[Rubric · Component coverage]** — The frontmatter and body don't match.
Some objects have no body entry: `tab-bar`, `rail`, `device-frame` (only referenced), `status-pill` (only inside Wellbeing tile). Some body entries have no token object: Menu button, Message groups, Ask for hours, One-off shift row, Email check, Facts card, Outcome list, Saving.
Fix: add the missing objects and entries.

**[Rubric · Component coverage]** — The (i) size disagrees (§ L130)
`info-button.size: 20px` (L130) against «18–20px» in prose (L260).
Fix: pick one.

**[Rubric · State coverage]** — Some empty and zero states are undefined (§ L124 implies no average then but doesn't say what shows)
the inbox in month 1, the «Nye i <måned>» group when nothing is new, no savings target pinned yet, the year chart in January, and the wellbeing tile before month 19 (L124 implies no average then but doesn't say what shows).
Fix: add a single «Empty» row per surface.

**[Rubric · State coverage]** — The crisis end screens are drawn (`krise~loest`, `krise~ikke`; oversikt.html L31) but EXPERIENCE only says *when* a crisis ends (L114), not what each end shows. (§ `krise~loest`, `krise~ikke`; oversikt.html L31)

Fix: add one line per outcome.

**[Rubric · Visual reference coverage]** — «Spine wins over mockup» appears three times (DESIGN L145, EXPERIENCE L18 and L73). (§ DESIGN L145, EXPERIENCE L18 and L73)

Fix: keep one per file.

**[Rubric · Visual reference coverage]** — The mockup has known drift a developer could copy. (§ DESIGN L222, L297)
A grain overlay on the whole page (`body::before`, opacity .04, z-index 100) contradicts «the canvas and the scene … no grain» (DESIGN L222, L297). The savings progress is computed on the client (`net()/GOAL_PRICE`), against «The frontend never calculates» (EXPERIENCE L27).
Fix: remove the overlay, or list both under «spine wins» as known prototype shortcuts.

**[Rubric · Bloat & overspecification]** — Pixel literals appear where tokens exist (§ L253 = `{spacing.4}`)
«16px padding» (L253 = `{spacing.4}`), menu button «44px» (L249 = `{spacing.target-min}`), email address «19px/800» (L266 = `{typography.h2}`). `status-pill` uses fontSize 15px / fontWeight 800 (L128), which matches no typography token.
Fix: replace them with references, or add a `pill` type token.

**[Rubric · Bloat & overspecification]** — Component Patterns restates engine rules that the frontend can't act on, e.g. (§ L130)
«Extra shifts are never offered while extra shifts run» (L130), the family-ask limit (L114), consumer loan terms (L112).
Fix: cut these to an FR pointer where the UI has no branch.

**[Rubric · Bloat & overspecification]** — Process history and lineage add nothing for a consumer (§ DESIGN L145, EXPERIENCE L18)
the intro blocks with issue numbers (DESIGN L145, EXPERIENCE L18) and the «Lifted from…» list (L204–208). The «Rejected» line (L209) earns its place. The flow headings also restate persona mood from the PRD.
Fix: trim.

**[Rubric · Inheritance discipline]** — The flow headings paraphrase the UJ names instead of quoting them (e.g.
«November with extra shifts» for UJ-6 «Markus fits a concert into a November with extra shifts»). The IDs are present, so the flows stay traceable.
Fix: quote the PRD title after the ID.

**[Rubric · Inheritance discipline]** — The Past choice note row cites «FR-37 cause links» (L127). (§ L127)
In the PRD, FR-37 is Echo badges and cause links are FR-36.
Fix: «FR-36, FR-37».

**[Rubric · Inheritance discipline]** — No term map links PRD glossary terms to player-facing terms.
Activity slot → «fri kveld / Kveld n», Threshold → «trivselsmål», Echo badge → «Tidligere valg», Spending level → Lite/Vanlig/Mye, and Money view → Penger/Banken are scattered across L84, L88, L124 and L127.
Fix: add a short table in Foundation.

**[Rubric · Inheritance discipline]** — EXPERIENCE contains no `{token}` references.
Colour roles are named in prose only («coral dot», «cobalt back link», «status colour»).
Fix: use `{colors.coral}` and the like where a behaviour depends on a colour role.

**[Rubric · Inheritance discipline]** — Markus's age disagrees. (§ L30)
Flow 3 has him at 17 in November, while the timeline sample (L30) and Flow 5 («16, November event») show 16, as does the mockup (concept.md acknowledges this).
Fix: align with UJ-6 (17) or state the sample age.

**[Rubric · Shape fit]** — The EXPERIENCE frontmatter has no `name` key (both examples carry one).

Fix: add `name: LifeMode`.

**[Accessibility]** — The spines name "tabs" for the add list and "Segmented tabs" for Fritid | Jobb, but no interaction pattern (EXPERIENCE "Add list"; DESIGN "Segmented tabs"). (§ EXPERIENCE "Add list"; DESIGN "Segmented tabs")
Builders will produce a half-tablist, as the prototype did. (4.1.2, 2.1.1.)
Fix: Prefer two toggle buttons (`aria-pressed`), since the control filters one list. If the team keeps tabs, require the full APG pattern: roving `tabindex`, arrow keys, `tabpanel` and `aria-controls`.

**[Accessibility]** — Status messages are well covered but miss a few cases (EXPERIENCE → State Patterns, Accessibility Floor; PRD NFR-2 bullet 3) (§ EXPERIENCE → State Patterns, Accessibility Floor; PRD NFR-2 bullet 3)
- «Spillet ble oppdatert på en annen enhet.» needs focus or an announcement after the reload. - The login error needs `aria-describedby` on both fields (FR-2 forbids saying which one was wrong). - The spine should say that live regions exist in the page from load. A region injected together with its text often isn't read out, and the prototype does exactly that. (4.1.3, 3.3.1.)
Fix: Add these three lines to the State Patterns.

**[Accessibility]** — Two AA basics are not in the contract
a document title per screen (2.4.2) and `autocomplete` tokens on the account fields (1.3.5). The prototype has the right tokens, but nothing obliges the build to keep them.
Fix: Add "title: «<Skjerm> · LifeMode»" and the tokens `email` / `username`, `current-password` / `new-password` and `nickname` to the Accessibility Floor.

**[Accessibility]** — Session expiry isn't addressed (2.2.1).
UJ-2 is a school PC with «Forbli innlogget» unticked. If a session can expire mid-play in less than 20 h, the player needs a warning or a silent refresh. FR-6 means no choice is lost, but the spine should say so.
Fix: Add one line: "A session never ends during play without a warning; after re-login the player lands where they were."

**[Accessibility]** — The avatar looks and some text alternatives lack content (EXPERIENCE "06 Avatar (§ EXPERIENCE "06 Avatar: Six preset looks"; Mirror scene "text alternative that matches the scene state")
Six preset looks"; Mirror scene "text alternative that matches the scene state"): - The looks have no names. - The scene's alt text isn't required to include the Kalam marker («Mobilen gikk i bakken», «Hel igjen»). (1.1.1.)
Fix: Each look has a spoken name («Blå genser»). The scene's text alternative includes the marker text, or the marker is real text outside the `img`.

**[Accessibility]** — The future-month labels in the year chart use `opacity:.7` (line 374) (§ line 374)
muted at 70 % on white is #7D7E89, which measures 4.02:1 at 11.5px. (1.4.3.)
Fix: Drop the opacity. The months already differ by having no bars.

**[Accessibility]** — The rail menu link's accessible name doesn't contain its visible label. (§ line 1047)
`aria-label="Meny, Mak"` (line 1047) overrides the visible «Mak · 16 år», so a voice-control user who says "Mak 16 år" gets no match. (2.5.3 Label in Name.)
Fix: Use «Mak · 16 år, meny», or drop the `aria-label` and add hidden text "meny".

**[Accessibility]** — Some names are missing or swallowed (§ line 652)
- The look buttons are named «Genser 1» to «Genser 6» (line 652). - The offer's avatar «L» isn't hidden (line 975). - The landing scene's teaser stickers («Første jobb», «Konsert lørdag?», «Kredittkort fra 18») are swallowed by `role="img"`, whose label omits them (lines 604–610). - The result scene's label leaves out the marker outcome (line 798). (1.1.1, 2.4.6.)
Fix: Name the colours, add `aria-hidden` to the avatar, put the stickers outside the `img`, and add the marker text to the label.

**[Accessibility]** — The document title is static, «LifeMode runde 3» (line 6), on every route. (§ line 6)
(2.4.2.)
Fix: Set `document.title` in `render()`.

**[Accessibility]** — The scrim-click handler (line 1075) closes the sheet when `e.target===sheet`. (§ line 1075)
That is also true for taps on the sheet's own padding, not just the backdrop, so an imprecise tap inside a sheet can dismiss it.
Fix: Compare the click coordinates with the dialog's bounding rectangle, or wrap the content in an inner element that fills the dialog.

**[PRD consistency]** — The phone event mirrors the Rule Set's unexpected expense, which the PRD says isn't an event. (§ EXP:257–258, HTML:779–781)
UX says: "Mobilen gikk i bakken … «Reparer skjermen −2 500 kr»" as an event with three options (EXP:257–258, HTML:779–781). PRD says: "Example unexpected expense NOK 2,500 (broken phone screen)" (RS:33). "An unexpected expense is a deduction, not an event, so it doesn't use an active month" (FR-24, PRD:988). The figures are declared (CON:71), so the severity is lowered.
Fix: add one line in Coverage: this is a story event (FR-17), and FR-24 broken-phone expenses arrive as a deduction with a "Hvorfor?" system cause.

**[PRD consistency]** — UX additions the PRD doesn't name (§ EXP:30)
absolute calendar years and the year chart's monthly history. UX says: "shown as a month name, age and year ("November · 16 år · 2027")" (EXP:30). Ending texts read «Sommerjobben i 2027» and «hytteturen i 2028» (HTML:877–878). The year chart totals are "Så langt i år: inn … ut … rente" (HTML:756). PRD says: "Month 1 is January of the year the player turns 15" (rule 11, PRD:246), with no start year. The frontend "never calculates" sums (NFR-4).
Fix: ask the PM or the architecture to fix a start-year setting, and add the year's monthly totals to the player view (AD-13 "other fields … engine stories", ARCH:399).

**[PRD consistency]** — The invitation "Nei takk" and the disabled ask buttons are rules or inputs the PRD doesn't have. (§ EXP:135)
UX says: "An invitation has one action, "Legg i planen", plus "Nei takk"" (EXP:135). It also says "Offer open | 16 | The two ask buttons are disabled, with «Svar på tilbudet først.»" (EXP:156). PRD says: "Ignoring a message only means missing what it offered" (FR-54, PRD:829). NFR-7's input list has no "decline invitation" (PRD:1388). FR-47 says only "one request at a time" (PRD:938).
Fix: state that "Nei takk" on an invitation is client-only (it just closes), or remove it. Mark the ask-lock as [ASSUMPTION] for the PM.

**[PRD consistency]** — Terms differ from the PRD glossary, and the D-texts still use the banned words. (§ PRD:180)
UX uses: - "Tidligere valg" / "Past choice note" for **Echo badge** (PRD:180) - "trivselsmål" for **Threshold** (PRD:220; EXP:124) - "Kveld" / "frie kvelder" / "Slot row" for **Activity slot** (PRD:164) - "Hvor mye bruker du i måneden?" / Lite–Vanlig–Mye for **Spending level** low/normal/high (PRD:216) - "Penger" / "Banken" for **Money view** (PRD:199) - "Welcome back" for **Recap** The UX rejects "forbruksnivå" and "plass" as jargon (EXP:209). D25, however, reads «I spillet velger du et forbruksnivå» (RS:302), and D26 reads «noen få ledige plasser» (RS:303). D12 and rule 10 say the player sets their hours («Du velger hvor mange timer du jobber i uka», RS:289, and "In the game, the player sets weekly hours", RS:77), which contradicts FR-47 (PRD:930).
Fix: add a glossary-mapping table to the spine. Ask the Rule Set owner to reword D12, D25, D26 and the rule 10 sentence.

**[PRD consistency]** — The crisis sale value doesn't follow rule 14 for the prototype's own timeline. (§ HTML:862, 1101)
UX says: «Selg mopeden +8 152 kr» in August 2029 (month 44) (HTML:862, 1101). The moped was bought in May 2027, month 17 (HTML:534; the bank's 6-month value of 10 772 kr confirms it). PRD/Rule Set says: resale = start × (1 − 15 % × months owned / 12). 27 months gives 11 645 × 0.6625 = **7 715 kr** (rule 14, RS:81; worked example 19 row "Gift … 27 months", RS:163). 8 152 kr is the figure for 24 months. This figure isn't declared.
Fix: use 7 715 kr.

**[PRD consistency]** — The year chart's 10 h wage is off by 5 kr. (§ "Fast jobb", HTML:533)
UX says: August and September income of 6 036 kr ("Fast jobb", HTML:533). Rule Set says: "with 10 h a week the wage would be NOK 6,041" (worked example 25, RS:234). The chart is declared (CON:68), but the figure is derivable.
Fix: 6 041 kr.

**[PRD consistency]** — The prototype's wellbeing start values differ from worked example 26. (§ HTML:682)
UX says: `USUAL={st:25,so:50}` (HTML:682), shown as "Vanligvis 50". Worked example 26 says: "stress 30 and social life 55 … stress falls by 5 to 25. Social life stays at 55" (RS:240). The hub's 68 then needs an activity (+5) instead of no activities.
Fix: use social 55, so that case "none" = 68 and case a = 74 match the answer key.

**[PRD consistency]** — The card warning and the payment plan leave out a figure each. (§ HTML:849)
UX shows the debt, this month's interest and the minimum-only cost (HTML:849), and the plan shows "939 kr i mnd" (HTML:862). PRD says: "The game shows the card's interest rate" (UJ-4 step 2, PRD:136). The plan "option shows the monthly instalment against what the player has left each month" (FR-32b, PRD:1110).
Fix: add «22,6 % rente i året» to the facts card and «Du har ca. … kr igjen i måneden» to the plan option.

**[PRD consistency]** — The age and story differ between flows (age declared, the rest not). (§ EXP:226, 230)
Flow 2 is "Markus, 15", and its climax is "the teaser names the licence" (EXP:226, 230). The recap shows the car licence (32 500 kr) at 16 (HTML:845), while UJ-2's teaser is the moped licence (PRD:92). Flow 3 is "Markus, 17" and Flow 5 is "Markus, 16" for the same November figures (EXP:235, 255). Flow 7 says «Du brukte 15 000 kr av pengegaven» (EXP:275), while Flow 5 and the prototype say the gift went to savings (EXP:259, HTML:786).
Fix: name the moped licence and 12 000 kr in Flow 2. Use one age for the November flows (16, as declared in CON:73). Make the Flow 7 story match.

**[PRD consistency]** — The sign-up preview puts the nickname and an amount into game text on the client. (§ EXP:45, 218)
UX says: "nickname with a live preview" and "Emma's preview bubble updates as he types" (EXP:45, 218). It renders «Hei Mak! Konsert lørdag? Billetten er 450 kr.» (HTML:635). The architecture says: "the frontend never inserts it into game text" (AD-13, ARCH:201). It "prevents … figures put into text outside the backend" (ARCH:196).
Fix: treat the bubble as UI chrome with no amount («Hei Mak!»), or drop it.

**[PRD consistency]** — The spine doesn't say which strings come from the engine. (§ EXP:157)
UX sets strings that carry game data as patterns: «Du har spurt om flere timer. Line svarer i desember.» (EXP:157). «Fritid 72 gir deg 3 frie kvelder. Snittet ditt er 61. Trivselsmålet er 50.» (DES:257). PRD/architecture says: "The frontend owns only UI chrome text" (AD-13, ARCH:201).
Fix: tag pattern strings as [engine] or [UI] in the Voice table.

**[PRD consistency]** — The player information text leaves out two NFR-3 items. (§ HTML:822)
UX says (prototype): «Spillet ligger hos Supabase i Tyskland. Serverne våre hos Railway lagrer logger …» (HTML:822). NFR-3 says: "the attempt limits briefly process network addresses, so … network addresses count as personal data" (PRD:1346), and the text must name "which services handle the data" (PRD:1354). The backend runs at Railway, EU West (ARCH:223). AD-12 makes it "a static page … reachable before any account exists" (ARCH:191), while UX shows it only inside sign-up and the menu (EXP:120).
Fix: add the network-address line and the server location, and link the page from the first screen and the login screen too.

**[PRD consistency]** — Smaller drops and wording issues (§ PRD:625, 828)
- FR-13/FR-54 event copy in the phone isn't mentioned (PRD:625, 828). - «Slutter nå» for extra shifts that end "from the next month" (HTML:973; FR-47, PRD:941). - The spending cards show money only, not the social −2/+2 (FR-23, PRD:972), and claim «Det de fleste velger» (HTML:928). - The savings-target sheet offers "Moped, ny" to a moped owner (HTML:1066; FR-29, PRD:1052). - The ending pill uses «lavt» while the hub uses «Tungt nå» (HTML:882, 692). - The goal card for goal 2 omits "no debt at 20", and the card for goal 3 omits the 60 000 kr price and the month-56 deadline (HTML:639; FR-9a, PRD:536–538). - The licence layer is exclusive (none/moped/car), so it can't show a moped and a car licence together (EXP:107).

**[Plain-language]** — 11 `#melding` — «Alle de frie kveldene er brukt.» → «Alle de frie kveldene er fylt opp.» «brukt» already means spent money and second-hand.


**[Plain-language]** — 13 `#resultat~used` marker — «Ny brukt» → «Brukt mobil».
"New used" reads as a joke or a typo.

**[Plain-language]** — 13 `g_bruk` — «Du kjøpte gaming-PC.» → «Du kjøpte en gaming-PC.» The article is missing.


**[Plain-language]** — 13 `g_spar` / `g_halv` — «Rommet er som før.» / «Sosialt gikk opp.» → drop the first (the player never sees a «rom», only the mirror), and «Sosialt +3» for the second (other screens use numbers).
The chip «+44 kr rente neste måned» vs the explanation «44 kr den første måneden» should use the same words: «neste måned».

**[Plain-language]** — 17 — «Moped, brukt», «Moped, ny», sheet «Moped, ny, 29 000 kr» → «Brukt moped», «Ny moped», «Ny moped · 29 000 kr».
Inventory word order, and two commas in a row in the sheet.

**[Plain-language]** — 19 `#aar` — post-it «Mopedlappen · Tatt» vs «fra 18 år» → «tatt».
Capitalisation is inconsistent across the post-its.

**[Plain-language]** — 19 `#aar` — «Full jobb · fra 19 år» → «Fulltidsjobb · fra 19 år».
«Full jobb» can mean a busy job.

**[Plain-language]** — 19 `#aar` — «Forbrukslån» as a gold unlock post-it → keep the unlock, but give it a neutral line, «Forbrukslån · mulig fra 18 år», so a loan doesn't read like a prize.


**[Plain-language]** — 19 `#aar` — «Rente · maks 100 kr» (strip label) → «Rente (0–100 kr)», or drop it.
«maks» reads as a cap on interest.

**[Plain-language]** — 19 `#aar` — «Hele livet i spillet» → «Fra 15 til 20 år».
«Hele livet» is grand for a five-segment bar.

**[Plain-language]** — 10 INBOX — tag «Utløpt» → «For sent».
It's bureaucratic, and Jonas is a friend.

**[Plain-language]** — 15 `#plan` — «Samme som i oktober» → «Samme kvelder som i oktober».
Same what?

**[Plain-language]** — 15 `#plan` — «Kveld 1 · Kveld med venner», aria «Fjern Kveld med venner fra kveld 1» → activity «Henge med venner».
«Kveld» twice in one row.

**[Plain-language]** — 15 `#plan` — «Gratis» in the add list, «0 kr» on the placed row for the same activity → «Gratis» in both.


**[Plain-language]** — 24 `#velkommen` — «Planen · 1 av 3 kvelder», «Du er her · November 2027, 16 år» → «Planlagt · 1 av 3 frie kvelder», «Du er her · November · 16 år · 2027» (the timeline's order). (§ the timeline's order)


**[Plain-language]** — 25 endings — the wellbeing pill reads «42 lavt» while the hub says «Tungt nå» and the bars say «lite» → «42 · Tungt», «61 · Det gikk bra».
Use one set of words.

**[Plain-language]** — 25 `#slutt-ikke` — «Du brukte penger på livet underveis, og det er lov.» → «Du brukte penger på livet underveis.» «Det er lov» sounds like an adult granting permission.
Teenagers hear that as talking down.

**[Plain-language]** — 25 CH — «Hadde du latt være, ville du hatt 10 210 kr mer …» → «Hadde du droppet dem, ville du hatt 10 210 kr mer …».
«latt være» has no object.

**[Plain-language]** — 25 CH headings — mixed forms
«Konserter og arrangementer», «Du brukte 15 000 kr av pengegaven», «Sommerjobben i 2027», «Du droppet hytteturen i 2028» → all nouns: «Konserter og arrangementer», «Pengegaven», «Sommerjobben i 2027», «Hytteturen i 2028». The amount column already shows the kroner.

**[Plain-language]** — 13 `k_mamma` — marker «Et råd» next to «Mamma … har ikke råd» → marker «Mamma svarer».
The pun on «råd» is confusing. Also, Mamma can't lend in May 2029 (`k_mamma`) but lends 500 kr in August 2029 (crisis): add a reason or make it consistent.

**[Plain-language]** — 16, 13 — «Tilbud fra sjefen», «Sjefen svarer neste måned» vs «Line svarer» → «Tilbud fra Line», «Line svarer neste måned».


**[Plain-language]** — rail — aria «Meny, Mak» on a link whose visible text is «Mak · 16 år» → «Mak · 16 år, meny».
Label-in-name (WCAG 2.5.3): the accessible name should start with the visible text.

**[Plain-language]** — 08 sticker — visible «2 nye», accessible name «2 nye» → aria «2 nye meldinger».
Out of context, «2 nye» says nothing.

**[Plain-language]** — all money strings — `kr()`/`plain()` use non-breaking spaces correctly.
But the hard-coded engine sentences («2 500 kr», «18 500 kr», «8 152 kr», «79,8 %», «2,87 %», «50 %») and `pct()` (`' %'`) use normal spaces, so «2 500 | kr» or «79,8 | %» can wrap at 320 px. Since the engine sends these sentences, put «NBSP between digit groups and before kr/%» into the engine's text contract.

**[Plain-language]** — 04 `#glemt~sendt` — «Finnes adressen hos oss, har vi sendt en lenke.» → «Har du bruker med denne e-posten, har vi sendt deg en lenke.» Still the same answer either way (FR-3), and less formal. (§ FR-3)


**[Plain-language]** — 17 `SPEND` — «Kantina av og til, klær iblant» → «Kantina av og til, nye klær noen ganger».
«Iblant» is written language.

**[Plain-language]** — 17 live message — «Sparemålet er valgt.» → «Sparemålet er nå Billappen.» Say which one.


**[Plain-language]** — 13, 21, 25 scene aria — «Speilbildet er alvorlig.» → «Speilbildet ser alvorlig ut.» A reflection can't be serious, it can only look it.


## Reviewer files
- `review-rubric.md`
- `review-accessibility.md`
- `review-prd.md`
- `review-language.md`
