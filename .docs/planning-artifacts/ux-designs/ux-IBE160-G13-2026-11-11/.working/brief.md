# Shared brief — LifeMode, 8 SVG design concepts

You are one of 8 designers working in parallel. Each of you owns ONE radically different design concept for the same product. Breadth of creative variation across the 8 is the point — commit fully to your concept's world; do not drift toward a safe, generic app look.

## Product (source of truth: `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/prd.md` — read §1, §2.3, §3 Glossary, §5.3–5.15, NFR-1, NFR-2, NFR-8)

LifeMode is a life-and-money game for 15–20-year-olds in Norway. The player lives 60 in-game months (age 15 → 20th birthday), one in-game year per session (10–15 min on a phone, often on the bus). Every choice carries forward and the game always shows WHY. It must feel like a game a 15-year-old prefers to scrolling — not schoolwork, not a quiz, not a banking app.

**Core loop per month (the game dynamic — the most important thing to design):**
1. Month opens → engine runs income/tax/costs; new messages land in the phone; either a **highlight event** (active month, 4 per year) or a **quiet-month summary**.
2. Explore: summary, phone, month plan, job, money.
3. Plan & act: place activities in **activity slots** (1–4 slots; more work hours = fewer slots; school & work shown as fixed blocks; tap to place, never drag), money actions, take offers, set hours, make the event's real choice.
4. **Continue** → activities applied, wellbeing calculated, crisis check → next month. A quiet month can be done in ONE tap.
Consequences: kroner and wellbeing deltas, **echo badges** (this effect comes from an earlier choice), **"Hvorfor?"** button explaining causes, room changes (room is built of up to 6 belonging layers, e.g. moped appears), "what this opened/closed", card warning, crisis month (up to 3 linked choices), session-end teaser ("Neste år kan du ta mopedlappen"), recap on return, four endings (ekte seier, hul seier, mål ikke nådd, tap), top-3 choices that mattered.

**Wellbeing** = 0–100 from stress, fritid (free time), sosialt liv; threshold 50 for a real win. Always show as text/number too, never colour alone.

## Screens

### KEY SCREENS — high fidelity, mobile 390×844 SVG each (the user cares most about these)
1. `01-landing.svg` — Landing / first screen. Pitch for a 15-year-old + **Logg inn** and **Opprett bruker** + "Glemt passord?". This is what makes a sceptical teen (Markus, told by his mum to try it) stay.
2. `02-lifemode-hub.svg` — The game page "LifeMode": the main month hub. Age/month (e.g. "16 år · Mars · måned 15 av 60"), room/avatar, balance, wellbeing (+3 parts), entry points to Telefon / Månedsplan / Jobb / Penger, the Continue action, new-message indicator. This is the heart of the game.
3. `03-event-scheduling.svg` — Event scheduling & month plan: show the year as a timeline (12 months, 4 active/highlight months marked, quiet months, crisis/card warning possibility, upcoming age unlock like mopedlappen in month 13) AND the month plan with activity slots (e.g. 3 slots this month because of extra shifts; school + work blocks; activities with cost and stress/social effects; "Samme som forrige måned"; missing-amount state). You may split this into `03a-year-timeline.svg` and `03b-month-plan.svg` if your concept needs it.
4. `04-highlight-event.svg` — An active month's highlight event: situation, sender, 2–3 options each stating kroner + wellbeing effect, one free option; ideally also the result moment (deltas, echo badge, Hvorfor?, what opened/closed). Split into `04a`/`04b` if needed.
5. `05-phone-messages.svg` — Phone / messages inbox: senders friends/family/employer/bank; kinds info / invitasjon / tilbud; new this month marked; an expired offer; the event copy. Ideally also one opened message (e.g. Emma invites to a concert → "Legg i månedsplan").
6. `06-money-view.svg` — Money view / accounts: brukskonto, sparekonto, BSU, kredittkort (from 18), money actions (flytt penger, BSU-innskudd, forbruksnivå lav/normal/høy, kortbruk på/av), savings target progress (e.g. pinned "Mopedlappen" 72%), upcoming costs next month, activity spend this year by kind, open options (e.g. moped licence with missing amount).

### ALL OTHER PAGES — sketch level, on ONE overview sheet `07-all-pages.svg`
A sitemap/contact sheet with small lo-fi phone thumbnails (in your concept's visual language, but simpler) for: Opprett bruker · Logg inn · Glemt passord · Velg livsmål (3 goals) · Lag avatar · Pengegave-valget (month 1) · Hendelse-resultat + Hvorfor? · Jobb-visning · Kortvarsel (card warning) · Krisemåned · Stille måned-oppsummering · Recap ved retur · Årsslutt-teaser · Kjøreprøve-minispill (turn-based) · Slutt-skjerm (ending + top 3 choices) · Om tallene / meny / innstillinger. Show navigation arrows between them so the sheet reads as the app's information architecture.

## Content rules
- All on-screen copy in **Norwegian bokmål**, written the way a Norwegian 16-year-old would find natural — not childish, not corporate. Use real figures from the PRD (e.g. timelønn 136,41 kr; 3 000 kr gir 84 kr i rente på et år; kredittkort 22,6 %, grense 10 000 kr; pengegave 10 000–30 000 kr; mopedlappen; BSU; frikort). Protagonist: Markus (or let the player avatar be unnamed); friends like Emma.
- Money changes always have sign + word, not just red/green. No alcohol/tobacco. No real brands or logos. Not a quiz — options read as actions.
- Accessibility (NFR-2): ≥ 4.5:1 text contrast, touch targets ≥ 44px for option buttons, nothing by colour alone, no drag needed.

## Craft rules (impeccable)
Read `.claude/skills/impeccable/SKILL.md`, `.claude/skills/impeccable/reference/new-work.md` and `.claude/skills/impeccable/reference/craft-floor.md` before drawing, and apply them: a clear point of view, committed visual world, no generic AI-template look, no default purple gradients, no emoji-as-icons laziness, real hierarchy. Landing = Persuade mode (full commitment). Hub/plan/phone/money = Operate-in-a-game: precise and scannable, but still unmistakably your world. Do NOT run `impeccable init`, do not create PRODUCT.md/DESIGN.md, and do not ask the user anything.

## SVG technical rules
- Standalone valid SVG 1.1/2: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 390 844" width="390" height="844">` for key screens; the overview sheet can be any size (e.g. 1600×1100).
- Vector only: no embedded raster images, no external hrefs, no `<foreignObject>`, no scripts. Gradients, patterns, filters, clipPaths are fine. Draw illustrations (room, avatar, icons) yourself with paths/shapes.
- Fonts: use Google Fonts families by name with a generic fallback, e.g. `font-family="'Space Grotesk', system-ui, sans-serif"`. List the exact families you use in `concept.json` so the gallery can load them. Max 2–3 families.
- Each SVG preferably < 80 KB. Keep text as real `<text>` (not outlined).
- Validate every file with `xmllint --noout file.svg`. Then render to look at it: `qlmanage -t -s 900 -o <your folder>/_preview <file.svg>` and Read the resulting PNG to check overlaps, clipped text, contrast. Fix what you see (one batch of fixes, then re-check). Delete the `_preview` folder when done.

## Deliverables — write ONLY inside your concept folder
- The SVGs above.
- `concept.json`:
  ```json
  {"id":"c1","name":"<short evocative name>","tagline":"<one line, Norwegian or English>",
   "fonts":["Family One","Family Two"],
   "palette":[{"name":"...","hex":"#..."}],
   "files":["01-landing.svg", "..."]}
  ```
- `concept.md` (English, ≤ 400 words): the idea in one paragraph; **game dynamics** — how the monthly loop, consequences, echo badges, Hvorfor? and the room feel like play in this concept (most important section); visual language (palette, type, shape, motion intent); why it works for 15–20-year-olds; risks/trade-offs; what you'd prototype first.

Your final reply to the orchestrator: 3–5 lines — concept name, files produced, the single strongest idea, and any problem.
