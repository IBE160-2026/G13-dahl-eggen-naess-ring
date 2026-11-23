# Spine Pair Review — IBE160-G13

Reviewed 2026-11-23 against `DESIGN.md` (300 lines), `EXPERIENCE.md` (293 lines), `mockups/index.html`, `mockups/oversikt.html`, the PRD (final), `decisions.md`, the shared spine `ux-IBE160-G13-2026-11-17/EXPERIENCE.md`, `.memlog.md` and `.working/round3/concept.md`. Line numbers refer to the files as of this review.

## Overall verdict

The pair is a usable contract with a sound structure. Both files follow the canonical shape, all 178 `{token}` references (61 unique) resolve, every PRD FR is accounted for, and the contrast figures I re-computed match the stated ratios. Before story-dev starts, one targeted pass is needed. Several states the PRD requires are missing (email already in use, a planned activity dropped at continue, the focus ring, logged out on another device). Several load-bearing bank components have behaviour rules but no visual spec. Component names drift between the two files. Two flows (UJ-3, UJ-4) don't deliver their PRD climax as written. Overall: **adequate**.

## 1. Flow coverage — adequate

Checked: UJ-1…UJ-6 (PRD §2.3) and FR-1…FR-58 (PRD §5) against EXPERIENCE.md Key Flows, IA and Coverage. Every UJ has a flow, and every flow has a named protagonist (Markus / «Mak»), numbered steps and a bolded climax. Six of the seven flows have an Edge line. Every FR is referenced at least once (FR-7 through the range «FR-6–FR-8», L26). FRs that aren't UX surfaces are listed in Coverage (L283).

### Findings
- **high** Flow 4 (UJ-3) swaps the UJ's «Hvorfor?» path for the (i) interest sheet. That drops the PRD climax: the growth tied to *his own earlier choice* (FR-36/FR-38). It also omits UJ step 4, the pointer to other ways of earning (EXPERIENCE Key Flows › Flow 4, L246–253; PRD UJ-3 path 2–4). *Fix:* add a step where the bank message or the savings row offers «Hvorfor?» linking the interest to the pengegave choice, or state that the interest sheet carries that cause link. Add the earning pointer, or record that it was dropped.
- **medium** Flow 6 (UJ-4) leaves out two PRD path steps: turning card use off (FR-26) and checking what the moped would sell for (FR-29, UJ-4 step 5). It also moves the climax to the PRD's resolution beat («six months later the card is paid», L269). Steps 1–2 rest on the 18+ bank, which is flagged as undrawn (L112 `[NOTE FOR UX]`). *Fix:* add both steps, restore the climax as the realisation that he must work more and spend less for six months, and resolve the NOTE FOR UX before story-dev.
- **medium** Flow 1 (UJ-1) stops at «months pass» (L222). The UJ resolution (the session ends after one in-game year with a teaser, FR-15) is in no flow, so surface 23 Year end is exercised by no flow at all. *Fix:* add a final step «23: December, year end with teaser, Ferdig for nå».
- **medium** Flow 3 (UJ-6) is missing two of the PRD's UJ-6 edge cases: «spends the money before he continues → the activity is dropped with a note» (FR-53) and «switches to the PC → it reloads before he can continue» (FR-49) (L244). *Fix:* add both to the Edge line and back them with state rows (see §4).
- **low** Flow 5 (phone breaks) has no UJ, which is fine, but it is the only flow with no Edge line (e.g. he can't afford the repair, or he goes offline mid-choice), and it names none of the FRs it exercises (FR-13, FR-34, FR-36, FR-38) (L255–260). *Fix:* add an Edge line and an FR tag in the heading.

## 2. Token completeness — adequate

Checked: all 52 colour tokens, 15 typography, 12 rounded and 13 spacing tokens, and 30 component token objects against design-md-spec.md type rules. All colour values are valid hex. Every prose and component `{path}` reference resolves (0 unresolved). Light-only is an explicit, reasoned decision (L186), so missing dark pairs are not a defect. I re-computed the stated contrast figures and all match (e.g. ink-muted/canvas 7.2, ink/coral 6.17, cobalt/paper 6.46, money-in/white 4.27, status-warn/white 2.45). Mockup CSS: every UI-chrome colour in the `:root` block and rules maps to a token.

### Findings
- **medium** The avatar presets (FR-10; IA row 06 «Six preset looks») have no tokens. The mockup holds them in `LOOKS` and `LOOK_SHADE` (index.html L640–641: #D99A2B, #2E7D6B, #8E6CC9, #25292E, #C8453A plus shades #B07A1C, #22604F, #6E4FA6, #15181C, #A3352C). Only the default pair exists, as `scene-hoodie` / `scene-hoodie-shade`. *Fix:* add `avatar-1…6` and `avatar-1…6-shade` tokens, or one list token, and point DESIGN Colors › Scene tokens to it.
- **medium** The scene palette doesn't match the claim that the art can change «without editing paths» (DESIGN Colors › Scene tokens, L185). The mockup defines `--sc-hoodie-line` #1E2B71, `--sc-hair-hi` #6B5C52, `--sc-pants-shade` #C7B9A6 and `--sc-beam` (index.html CSS `:root`, second block) with no tokens. About 25 more fills are hard-coded in the SVG, e.g. #A8805D ×16, #896850, #EEF0E8, #D4D4D0, #FAFAF7, #F2EEE4 (index.html L469–477). The phone-layer shades #B85147 / #3E434E are also hard-coded (L559). *Fix:* tokenise the missing `--sc-*` variables, and either tokenise the props or state in DESIGN that furniture and props are fixed art outside the token set.
- **medium** No caption size exists. DESIGN specifies «Vanligvis 50» «in 12px meta» (Components › Wellbeing tile, L256), but `{typography.meta}` is 13px and L200 calls 13px the floor for running text. The mockup also uses 12px for sticker sublines, message times, day separators, the life bar and chart labels (index.html CSS L118, 201, 294, 300, 356, 377, 381), and 10px for badge counts (L63). *Fix:* add a `caption` (12px) token and a `badge` size with the uses they're allowed for, or raise these to 13px.
- **medium** No contrast is stated for text on the illustration: the white Kalam marker on the 55%-dimmed scene (Components › Scene, L243) and the ink marker on the glass (`scene-wall-mirror`). These are load-bearing reads (event title, outcome). *Fix:* measure and state both, or add a backing plate rule.
- **low** Some passing pairs are never stated: paper on ink (offline bar, selected tab and segment; 15.2:1), `danger` text on white (7.8:1), `tag-worse-text` on `money-out-soft` (7.9:1), ink on `locked` (13.2:1). *Fix:* one line in Colors.
- **low** Three colour tokens are never referenced or described: `bubble`, `option-selected`, `tag-worse-text` (DESIGN L65–67). Others are never referenced: rounded `key`, `bar`, `sm`, `md`, `tile-icon`, `bubble`, `screen`; spacing `target-min` and `target-floor`; typography `marker`. *Fix:* wire them into component objects or describe them in prose. Delete any that are unused.
- **low** Some tokens share a value under different names: `canvas` = `scene-wall-lit`, `wall` = `scene-wall`, `cobalt` = `money-rate` = `scene-hoodie`, `coral` = `scene-phone`. The mockup also uses different variable names (`--wall-lit`, `--white`, `--press`, `--dim`, `--in`, `--out`, `--hair-2`). *Fix:* add one sentence saying the duplicates are intentional decoupling, and add a token → CSS-variable map, or rename the CSS variables.
- **low** The lift shadow for sheets and the CTA has no values. DESIGN says only «a shadow pointing up or down» (Elevation & Depth, L226), while the mockup has `--shadow-lift: 0 -4px 16px rgba(26,28,42,.18)`. *Fix:* state the values next to the card and sticker shadows.

## 3. Component coverage — thin

Checked: I collected component names from both spines (DESIGN frontmatter `components` = 30 keys, DESIGN Components body = 37 entries, EXPERIENCE Component Patterns = 34 rows) and matched each against the other spine. Matching depends on guessing between different names (see §7). Where rows exist, the rules are substantive, not one-word descriptions.

### Findings
- **high** The bank components carry FR rules but have no visual spec. These are Savings target with its progress bar (the mockup has `.progress`), What comes next (two closed rows), Open options («Kan kjøpes eller selges» rows with «Mangler … kr» or a lock), Credit card, and the «account rows» that EXPERIENCE says the 18+ bank reuses (Component Patterns L109–112). None appears in DESIGN Components or in the frontmatter (FR-57, FR-48, FR-26, FR-45). *Fix:* add DESIGN entries and tokens for `progress`, `account-row`, `transaction-row` and `option-row`, and the card panel.
- **medium** The Outcome list visual names tints that aren't tokens: «check on green tint», «arrow on rust tint» (DESIGN Components L277). It has no frontmatter object, and its only behaviour lives inside the Result and Room layers rows. *Fix:* map it to `{colors.money-in-soft}` / `{colors.money-out-soft}` (or the status tints) and `tag-worse-text`, and add a Component Patterns row (order, announcement, glyph meaning).
- **medium** Several EXPERIENCE components have no visual counterpart: Same as last month (which button variant?), Add list (beyond `segmented`), Recap, Year end, Result layout. *Fix:* add short DESIGN entries, or point each to the existing component it reuses.
- **low** Some DESIGN components have no behavioural row: Card / tile (link hover is the only affordance named, L253), Menu button, Facts card, Email check (it exists only as a state row), One-off shift row (only inside Ask for hours), Offline bar (only as a state). *Fix:* add one-line rows or explicit pointers.
- **low** The frontmatter and body don't match. Some objects have no body entry: `tab-bar`, `rail`, `device-frame` (only referenced), `status-pill` (only inside Wellbeing tile). Some body entries have no token object: Menu button, Message groups, Ask for hours, One-off shift row, Email check, Facts card, Outcome list, Saving. *Fix:* add the missing objects and entries.
- **low** The (i) size disagrees: `info-button.size: 20px` (L130) against «18–20px» in prose (L260). *Fix:* pick one.

## 4. State coverage — adequate

Checked: I walked IA surfaces 01–28 for empty, cold-load, focus, error, offline and permission states. Global coverage is strong: saving, still trying, updated on another device, server waking (cold load), offline, unread and form errors are all present. Permission-denied doesn't apply on the client (PRD FR-2: «A player can reach only their own game» is enforced by the server).

### Findings
- **high** Email already in use at sign-up is missing. FR-1 requires the screen to say the address is in use and point to Log in and the forgotten-password link, and this is the only place the game shows that an address has a user. It is absent from State Patterns (L138–168) and from the mockup. *Fix:* add a row for surface 02 with the copy and focus target.
- **high** A planned activity dropped at continue is missing. FR-53, NFR-7 (PRD L1424) and the UJ-6 edge case all require it to be «dropped with a note», but no state, surface or copy is defined for that note. *Fix:* add a row naming where the note appears (hub or next month's result) and how it is announced.
- **high** The focus state has no visual spec. DESIGN.md never mentions focus (0 hits). EXPERIENCE covers only where focus moves (L136, L187). The mockup uses a 3px ink outline plus a 6px coral ring (index.html CSS `:focus-visible`). Every component builder needs this for WCAG 2.4.7 / 2.4.11. *Fix:* add a focus-ring spec to DESIGN (tokens plus the rule for scene stickers and dark surfaces such as the offline bar and selected tabs).
- **medium** Logged out on another device or session expired is missing. FR-5 says the next action shows the login screen, and FR-3, FR-4 and FR-44 log out other devices. «Updated on another device» (L144) is a different case. *Fix:* add a row.
- **medium** The Job view (16) has no state for before the player has a job. In UJ-1 the job arrives in month 3, but the Jobb tab is always there (IA L36). The Add list's Jobb tab is likewise only «needs a job» (L126): disabled, hidden or explained? *Fix:* define the no-job state for both.
- **medium** Several account form errors are missing. Menu: wrong current password, and a new password that is too short (FR-4); wrong password on delete (FR-44); nickname-change validation. Sign-up: a nickname over 16 characters or with characters that aren't allowed (FR-1); only «under 2» is covered (L166). The sign-up rate-limit message (FR-1) is also missing. *Fix:* add rows. Most can share one pattern with Email invalid.
- **low** Some empty and zero states are undefined: the inbox in month 1, the «Nye i <måned>» group when nothing is new, no savings target pinned yet, the year chart in January, and the wellbeing tile before month 19 (L124 implies no average then but doesn't say what shows). *Fix:* add a single «Empty» row per surface.
- **low** The crisis end screens are drawn (`krise~loest`, `krise~ikke`; oversikt.html L31) but EXPERIENCE only says *when* a crisis ends (L114), not what each end shows. *Fix:* add one line per outcome.

## 5. Visual reference coverage — adequate

Checked: `mockups/` holds `index.html` and `oversikt.html`. There are no `wireframes/` or `imports/` folders. EXPERIENCE IA gives every surface a route (L42–71), which is strong inline linking, and points to oversikt.html (L73). Neither file in `mockups/` is orphaned. The `.working/` artifacts aren't referenced and needn't be.

### Findings
- **medium** `oversikt.html` is not in either frontmatter `mockups:` list (DESIGN L13–14, EXPERIENCE L12–13) and isn't mentioned anywhere in DESIGN, though it is the only page showing every state. *Fix:* add it to both lists and mention it in DESIGN's intro.
- **medium** DESIGN cites the mockup only once, in the intro (L145). No Components entry names the route or state that illustrates it (e.g. Wellbeing tile → `#hjem`, Year chart → `#aar`, Offer card → `#jobb~svart`, Sheet → `#plan~velg` / `#hjem~rente`, Room layers → `#penger~solgt`). EXPERIENCE Component and State Patterns don't link states either (e.g. Email check → `#opprett~sjekk`, Offline → `#offline`). *Fix:* add `→ #route~state` pointers.
- **low** «Spine wins over mockup» appears three times (DESIGN L145, EXPERIENCE L18 and L73). *Fix:* keep one per file.
- **low** The mockup has known drift a developer could copy. A grain overlay on the whole page (`body::before`, opacity .04, z-index 100) contradicts «the canvas and the scene … no grain» (DESIGN L222, L297). The savings progress is computed on the client (`net()/GOAL_PRICE`), against «The frontend never calculates» (EXPERIENCE L27). *Fix:* remove the overlay, or list both under «spine wins» as known prototype shortcuts.

## 6. Bloat & overspecification — adequate

### Findings
- **medium** The wellbeing bands are stated three times, in two forms. DESIGN Colors (L180) and EXPERIENCE State Patterns › Wellbeing status (L155) hard-code 50/60 and 40/50. EXPERIENCE Component Patterns › Wellbeing tile (L124) says the threshold is configuration and «the server sends the band». A developer may hard-code the thresholds. *Fix:* keep the canonical rule in the Wellbeing tile row (server-sent band) and have the other two point to it with an example only.
- **medium** Responsive behaviour is duplicated, with different details: DESIGN Layout (L209–217: centre max 720/760) and EXPERIENCE Responsive & Platform (L194–198: scene capped at 480 px, pane routing). *Fix:* DESIGN keeps dimensions, EXPERIENCE keeps behaviour, and each points to the other.
- **low** Pixel literals appear where tokens exist: «16px padding» (L253 = `{spacing.4}`), menu button «44px» (L249 = `{spacing.target-min}`), email address «19px/800» (L266 = `{typography.h2}`). `status-pill` uses fontSize 15px / fontWeight 800 (L128), which matches no typography token. *Fix:* replace them with references, or add a `pill` type token.
- **low** Component Patterns restates engine rules that the frontend can't act on, e.g. «Extra shifts are never offered while extra shifts run» (L130), the family-ask limit (L114), consumer loan terms (L112). *Fix:* cut these to an FR pointer where the UI has no branch.
- **low** Process history and lineage add nothing for a consumer: the intro blocks with issue numbers (DESIGN L145, EXPERIENCE L18) and the «Lifted from…» list (L204–208). The «Rejected» line (L209) earns its place. The flow headings also restate persona mood from the PRD. *Fix:* trim.

## 7. Inheritance discipline — adequate

Checked: the sources resolve. All four EXPERIENCE sources and all four DESIGN sources exist, including `konsepter/speilet/DESIGN.md`. EXPERIENCE `design: DESIGN.md` resolves. The overrides of the shared spine are explicit (time format, «Ekko», surface 23 now FR-15).

### Findings
- **medium** Component names drift between the files, so a consumer can't extract by name:
  - DESIGN «Scene (the mirror)» / EXP «Mirror scene»
  - «Past-choice note» / «Past choice note»
  - «Info / interest button» + `info-button` / «Interest (i)»
  - «Locked post-it» + `locked-note` / «Locked post-it»
  - «Option radio card» + `option-radio` / «Spending choice»
  - «Toast» / «Notification»
  - «Message groups» / «Phone message»
  - «Segmented tabs» + `segmented` / «Add list» tabs
  - «Buttons» + `button-cta` / «Next month (CTA)»
  - «Crisis steps» / «Crisis»
  - «Menu row» / «Menu»
  - «Info box» / «Player information»
  - «Offer card» / «Offer»

  *Fix:* use one name per component, equal to its frontmatter key, in both files.
- **low** The flow headings paraphrase the UJ names instead of quoting them (e.g. «November with extra shifts» for UJ-6 «Markus fits a concert into a November with extra shifts»). The IDs are present, so the flows stay traceable. *Fix:* quote the PRD title after the ID.
- **low** The Past choice note row cites «FR-37 cause links» (L127). In the PRD, FR-37 is Echo badges and cause links are FR-36. *Fix:* «FR-36, FR-37».
- **low** No term map links PRD glossary terms to player-facing terms. Activity slot → «fri kveld / Kveld n», Threshold → «trivselsmål», Echo badge → «Tidligere valg», Spending level → Lite/Vanlig/Mye, and Money view → Penger/Banken are scattered across L84, L88, L124 and L127. *Fix:* add a short table in Foundation.
- **low** EXPERIENCE contains no `{token}` references. Colour roles are named in prose only («coral dot», «cobalt back link», «status colour»). *Fix:* use `{colors.coral}` and the like where a behaviour depends on a colour role.
- **low** Markus's age disagrees. Flow 3 has him at 17 in November, while the timeline sample (L30) and Flow 5 («16, November event») show 16, as does the mockup (concept.md acknowledges this). *Fix:* align with UJ-6 (17) or state the sample age.

## 8. Shape fit — strong

DESIGN has all eight body sections in canonical order (Brand & Style → Colors → Typography → Layout & Spacing → Elevation & Depth → Shapes → Components → Do's and Don'ts). EXPERIENCE has all eight required defaults. Responsive & Platform is present and triggered (multi-width web), and Inspiration & Anti-patterns is present. The invented Coverage and Open Questions sections earn their place: they map FRs that aren't surfaces and name undecided items.

### Findings
- **low** The EXPERIENCE frontmatter has no `name` key (both examples carry one). *Fix:* add `name: LifeMode`.

## Mechanical notes

- **Token resolution:** 178 `{…}` references (61 unique) in DESIGN; 0 unresolved. EXPERIENCE has none.
- **Frontmatter:**
  - DESIGN has name, description, status, dates, sources and mockups, all present.
  - EXPERIENCE has no `name`.
  - Neither `mockups:` list includes `oversikt.html`.
  - Both are `status: draft` while the intro says round 3 was chosen (#95). That is consistent, but downstream should treat the pair as pre-final.
- **Broken or loose references:**
  - «FR-37 cause links» (EXPERIENCE L127) should be FR-36.
  - DESIGN prose names `sender-*` and `scene-*` tokens bare (L184–185) instead of as `{colors.…}` references.
  - The Coverage section doesn't map NFR-4 (correct, explainable figures) or NFR-7 (robust input), though both shape UI states.
- **Name inconsistencies:** see §7. The status words are consistent across DESIGN L256, EXPERIENCE L124 and L155 («bra / ok / lite», «lavt / middels / høyt», «Det går bra / Helt ok / Tungt nå»). DESIGN's sample «25 lavt» is a stress value. That is correct but could confuse readers.
- **Mockup ↔ token check:** all UI-chrome CSS colours map to tokens. The untokenised colours are confined to illustration fills, avatar presets and three `--sc-*` variables (see §2).
- **Contrast spot-check:** 30 pairs re-computed; every stated ratio matches to ±0.05.
