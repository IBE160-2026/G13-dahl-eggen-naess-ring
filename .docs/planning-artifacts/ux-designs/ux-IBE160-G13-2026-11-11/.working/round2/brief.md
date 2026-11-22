# Round 2 brief: LifeMode, 4 responsive HTML design directions

You are one of 4 designers working in parallel. Each of you owns ONE design direction (your card is at the bottom of the prompt that sent you here). All four directions share the same product decisions, screens and game dynamics below. What differs is the **visual world**: type, palette, density and one signature move. Commit fully to your direction. The four together must span the range the team is split on, from fresh and modern to muted and calm.

Paths below are relative to the repo root `/Users/saranaess/Documents/IBE160/G13-dahl-eggen-naess-ring`. `W` = `.docs/planning-artifacts/ux-designs/ux-IBE160-G13-2026-11-11/.working`.

## 1. Read before you design

1. `PRODUCT.md` (repo root): product truth, users, constraints, accessibility.
2. `.docs/planning-artifacts/ux-designs/decisions.md`: the team's round 2 decisions. They are binding. They are summarised in §2 below.
3. Round 1 work you inherit from. Open each SVG with the Read tool to see it:
   - `W/concepts/c6/` **Rommet**: `concept.md`, `02-lifemode-hub.svg`, `03b-month-plan.svg`, `04a-highlight-event.svg`, `04b-event-result.svg`. This is the base idea and game dynamic. Its visual identity (warm cream/oat, pine, rust, ochre lamplight, Fraunces serif) is **rejected**. Do not reuse it.
   - `W/concepts/c1/` **Månedsfeed**: `concept.md`, `05a-phone-inbox.svg`, `05b-phone-message.svg`, `06-money-view.svg`. The team wants these three screens' structure and realism carried forward.
   - `W/concepts/c5/03a-year-timeline.svg` (the top overview strip only) and `W/concepts/c3/03a-year-timeline.svg` (the detailed year view). These are the reference for the new timeline (§2.3).
   - `W/concepts/c4/concept.md` and `W/concepts/c4/02-lifemode-hub.svg` **Mobilen (Ly)**: part of the team liked its calm, muted feel.
4. Inspiration you may draw from: `.docs/design/design-thinking-2026-10-16.md` (especially "Top Concepts" and "Round 1 result: concept 2 sketched"), and the hand sketches `.docs/design/mobile-sketches/k2-01-03.pdf` and `k2-04-06.pdf` (read them with the Read tool, pages "1-3"). The sketches' bottom bar Hjem / Plan / Jobb / Økonomi, the tap-to-pick month plan, and the "For the digital round" notes are good material.
5. Real figures: `.docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/addendum.md` (Rule Set v1: parameter table and worked examples, especially 25, 26 and 26a, which are the UJ-6 November scenario). Use these figures, not invented ones.
6. PRD for anything unclear: `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md`. Use §3 Glossary and §5.3-5.14 (FR-9 to FR-57). Don't read all of it; grep for what you need.
7. Impeccable craft rules. Read these files before you write any UI: `.claude/skills/impeccable/reference/craft-floor.md`, `.claude/skills/impeccable/reference/mode-operate.md` (the game screens are Operate surfaces) and `.claude/skills/impeccable/reference/mode-persuade.md` (only the landing screen is Persuade).

## 2. Binding decisions (from the team)

### 2.1 Base: Rommet's idea and game dynamics
The player's own room is the hub. Objects in the room open the systems: the phone opens messages, the calendar/planner opens the month plan and year, money opens the bank, and the work item opens the job. The room reacts to the month: new messages light up the phone, and belongings collect over five years (up to 6 layers, e.g. a moped outside from 16). Stress makes the room visibly messier, but wellbeing is always written as text and numbers too. Every room object has a permanent text label, and a standard navigation route always exists as well (bottom bar on phones, rail or panes on larger screens), so nobody has to hunt for hotspots.

### 2.2 A more modern visual identity
It must look more modern, and **must not look like Claude's own look**: no warm cream or ivory ground, no terracotta/rust/clay accent, no serif display with italic accents, no lamplight warmth as a default. The team is split: one member likes Månedsfeed's crisp, fresh look; others like Ly/Rommet's calmer, muted colours. Your card says where on that range you sit.

### 2.3 Time: no "måned X av 60"
Never show "måned 15 av 60" or any month count out of 60.
- **Timeline bar:** a compact bar showing the current in-game year as 12 **named months** (jan-des; a session is January to December), with the current month marked, past months filled, plus the player's **age** (e.g. "16 år") and the year. No events on it, just months, year and age. The reference is the top strip of c5 `03a-year-timeline.svg`. It is reused on several screens (hub, month plan, money view, etc.), always in the same place and form.
- **Year view:** tapping the timeline bar opens a detailed year view, like c3 `03a-year-timeline.svg`. It shows the months of this year as blocks with what happened in past months (the events and choices already made, quiet months), the current month, and upcoming **age unlocks** (e.g. "mopedlappen fra 16 år"). It must **not** reveal future events (the PRD hides them on purpose). It also shows the five years from 15 to 20 as an age rail, so the player sees how far into the life they are without any "X of 60".

### 2.4 Phone and bank feel real
Carry forward Månedsfeed's phone inbox, opened message and money view. The phone should feel like a real messaging app: threads by sender (friends, family, employer, bank), unread markers, invitation and offer messages with actions ("Legg i månedsplanen"), an expired offer. Never show clock times; messages belong to a month (FR-52). The money view should feel like a real Norwegian banking app: brukskonto, sparekonto, BSU, kredittkort (only from 18; show it locked or absent at 16), money actions (flytt penger, BSU-innskudd, forbruksnivå lav/normal/høy), a savings target with a progress bar ("Lappen" / car licence, e.g. 79.8%), "Neste måned" bills, and «Småtteri» (activity spend this year by kind). Do not copy any real bank's or app's branding.

### 2.5 Nickname
At sign-up, the player picks a **kallenavn** (nickname). It is not a real name, and no one else sees it. Messages and texts address the player by it ("Hei Mak! Konsert lørdag?"). Show this on the create-user screen with a short helper text saying it is only for you and need not be your real name. (Note: this conflicts with the current PRD, which allows no free text beyond the email address. The team knows, and the design should show it anyway.)

### 2.6 Web app: mobile-first, scales to tablet and desktop
LifeMode is a web app in the browser (NFR-1): mobile-first, from 320 px up to tablet, laptop and desktop, with no horizontal scrolling. The larger layouts must be **designed**, not a stretched phone column. Use the width: for example the room in the centre with the phone docked as a side pane and money or the plan as another pane, or a rail with panes. Each direction should make its own call. A centred 390 px column on a desktop fails the brief.

## 3. Screens: one responsive HTML prototype

Build **one self-contained `index.html`** that holds all screens, navigable with hash routes (`#hjem`, `#plan`, etc.) and real links/buttons between them. Use vanilla JS for routing and small state (e.g. tapping an activity into a slot, opening "Hvorfor?", switching event → result), and no frameworks. Follow the UJ-6 November scenario where it fits (16 år, November, 14 h work a week = 3 slots, Emma's concert invitation NOK 450, evening with friends NOK 200, wage NOK 8,457, car licence savings target 79.8%). Use the player's nickname, e.g. "Mak".

| Route | Screen | Must show |
|---|---|---|
| `#landing` | Landing (Persuade) | A pitch a sceptical 15-year-old stays for; **Opprett bruker**, **Logg inn**, "Glemt passord?" |
| `#opprett` | Create user | Email twice, password (min 8), **kallenavn** with helper text, "Forbli innlogget", a link to the short player information |
| `#start` | Life goal + avatar | 3 life goals (see FR-9a), a small set of preset avatar looks, continue |
| `#hjem` | **The room (hub), the heart of the game** | Timeline bar; the room with labelled objects (phone with unread count, planner, money, work); balance; wellbeing as a number out of 100 plus its 3 parts (stress, fritid, sosialt) in text; this month's state (quiet or highlight event waiting); the primary action **Fortsett til desember** (a quiet month is one tap); navigation |
| `#aar` | Year view | As §2.3 |
| `#plan` | Month plan | School and work as fixed blocks; 3 of 4 free slots this month because of extra shifts; activity cards with price, stress and social effects written with sign and word; tap to place, never drag; one card that can't be afforded ("Mangler … kr"); "Samme som forrige måned" |
| `#hendelse` | Highlight event | Sender, situation, 2-3 options as actions with kroner (wellbeing effects are hidden before the pick, per the architecture), one free option |
| `#resultat` | Event result | Kroner and wellbeing deltas with sign and word, an **echo badge** naming the earlier choice an effect came from, a **"Hvorfor?"** that expands in place, "Åpnet / Stengt" (what this opened or closed), and the change shown in the room |
| `#telefon` | Phone inbox | As §2.4 |
| `#melding` | Opened message | Emma invites Mak to the concert → "Legg i månedsplanen" |
| `#penger` | Money view | As §2.4 |
| `#jobb` | Job view | Hours control (10 + 4 extra = 14 h), hourly rate, expected pay, hours limit, and the preview "ending the extra shifts gives 4 slots from December, and NOK 604 less a month" |

Add a small prototype-only screen index (e.g. a discreet "Skjermer" button or a footer) so a reviewer can jump to every route. Keep it visually apart from the product UI.

**State worth showing:** after "Fortsett", changed figures and new messages stay highlighted until the player has seen them (see the shared raise in §5).

## 4. Rules

**Content**
- All on-screen copy in Norwegian bokmål that a Norwegian 16-year-old finds natural: not childish, not corporate. Options read as actions, never as quiz answers.
- Real figures from Rule Set v1 and the worked examples. If a figure doesn't exist there, mark it in `concept.md` as invented.
- Money changes always carry a sign and a word ("+604 kr inn", "−450 kr"), never colour alone. No alcohol or tobacco. No real brands or logos.

**Accessibility (NFR-2, WCAG 2.2 AA)**
- Text contrast ≥ 4.5:1 (≥ 3:1 for large text and UI components).
- Touch targets ≥ 24 px, and option buttons and primary actions ≥ 44 px.
- Visible focus states, and keyboard-operable: every control is a real `<button>` or `<a>`.
- Every picture has a text equivalent: the room objects, room state and echo badges have labels or `aria-label`.
- Respect `prefers-reduced-motion`.

**Craft (impeccable)**
- Apply craft-floor.md and the mode rules. The world lends **type, palette, density and one signature move**; the navigation and controls stay standard web controls.
- Banned as display or brand faces unless your card names them: Fraunces, Playfair Display, Cormorant, Lora, Crimson, Newsreader, Syne, Space Grotesk, Space Mono, IBM Plex, Inter-as-display, DM Sans, DM Serif, Outfit, Plus Jakarta Sans, Instrument Sans. Use at most 2-3 families from Google Fonts. In production they will be self-hosted (no third-party loads, NFR-3); note this in concept.md.
- No default purple gradients, no glassmorphism by reflex, no emoji as icons, no generic icon-tile grids. Draw the room and icons yourself as inline SVG. The room is the hero illustration and deserves real craft at every size.
- Avoid the four AI-default looks: cream ground with serif display and terracotta accent; near-black with one neon accent and glow; broadsheet hairlines with italic serif and tracked mono labels; flat saturated ink with black boxes and hard offset shadows.

**Technical**
- One file, `index.html`, with inline CSS and JS. External loads only from fonts.googleapis.com / fonts.gstatic.com. No raster images, no external scripts.
- Use CSS custom properties for your tokens (colours, type scale, spacing, radii) at `:root`, so they can later be lifted into DESIGN.md.
- Must work at 320, 390, 768, 1024 and 1440 px wide with no horizontal scroll.
- Keep it under ~300 KB.

## 5. Shared raises (from the impeccable direction roll)

Every direction carries these. Each was taken from a challenger world as a *discipline*, not as a look:
- **Held change** (from the airport gate board): when a month opens, changed values (balance, wellbeing parts, a new message, an echo) stay marked until the player has looked at them. Don't flash them and drop them.
- **Density on big screens** (from Japanese high-density web): tablet and desktop layouts use the width for real panes with real content. No inflated whitespace around a lone phone column.
- **Extent at a glance** (from the stepped tab rail of a reference manual): the age rail in the year view shows the five years with the current position, so the player feels how much of the life is lived and left.

## 6. Verify by looking

Render with headless Chrome and look at the screenshots:

```sh
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --screenshot=OUT.png --window-size=390,844 "file://ABS_PATH/index.html#hjem"
```

Screenshot at least `#hjem`, `#plan`, `#resultat`, `#telefon` and `#penger` at 390×844, plus `#hjem` at 820×1180 and 1440×900. Read the PNGs, then fix overlaps, clipped text, contrast and broken layouts in one batch, and check once more. Put working screenshots in `_preview/` and delete that folder when done, **except** keep these three final thumbnails for the gallery in your folder: `shot-mobile.png` (`#hjem` 390×844), `shot-tablet.png` (`#hjem` 820×1180) and `shot-desktop.png` (`#hjem` 1440×900).

## 7. Deliverables (write ONLY inside your own folder `W/round2/<your-id>/`)

- `index.html`
- `shot-mobile.png`, `shot-tablet.png`, `shot-desktop.png`
- `concept.json`: `{"id":"r2-a","name":"…","tagline":"… (Norwegian)","position":"<where on the fresh↔muted range>","fonts":["…"],"palette":[{"name":"…","hex":"#…"}],"routes":["#landing","…"]}`
- `concept.md` (English, ≤ 450 words) with these sections:
  - **The idea** (one paragraph)
  - **Signature move**
  - **Game dynamics:** how the month loop, room, held change, echo badge and "Hvorfor?" feel like play here
  - **Visual language:** palette, type, shape, motion
  - **Desktop and tablet:** the layout decision
  - **Where it sits** between Månedsfeed and Ly/Rommet
  - **Risks**
  - **Invented figures**, if any

Don't ask the user anything. Don't run `impeccable init`, and don't write PRODUCT.md or DESIGN.md.

Your final reply to the orchestrator: 3-5 lines with the name, the files produced, the strongest idea, and any problem.
