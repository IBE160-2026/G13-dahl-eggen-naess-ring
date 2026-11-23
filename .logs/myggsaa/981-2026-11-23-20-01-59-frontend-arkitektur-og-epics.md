# Frontend-arkitektur og epics

## 2026-11-23 kl. 20:01 — Myggsaa

### Oppgave
Brukeren startet `bmad-create-epics-and-stories`. Under steg 1 så brukeren at arkitekturen manglet frontend, selv om `technology.md` har den med. Siden gruppa nå selv er frontend-teamet, ble arkitekturspinen utvidet med frontend (#122), før epics-løpet fortsetter. Brukeren ba om en PR. Senere samme kveld ba brukeren om en siste sjekk av at spinen og PRD-en stemmer, før epics-løpet fortsatte med steg 2 og 3. Til slutt ba brukeren om push og PR, med beskjed om at det må gjøres review.

### Plan
- Epics steg 1: kravinventaret (FR, NFR, AD-er, UX-DR1 til UX-DR45, åpne punkter fra klarhetsgjennomgangen) ble skrevet til `.docs/planning-artifacts/epics.md`, og arbeidet ble satt på pause ved menyen [C].
- `bmad-architecture` (Update, Coaching): beslutningene ble tatt med brukeren (rutere og porter A, klientdatalag A, styling B, tester og standardpakke som anbefalt), og leveransen ble både spinen og `SOLUTION-DESIGN.md`.
- Reviewer gate med fire gjennomganger (adversarial, rubrikk, versjoner, avstemming mot UX og PRD) i `reviews/review-2026-11-23-frontend-*.md`. Rettelsene ble lagt inn samlet.
- UX-filene ble rettet etter funnene, og `epics.md` fikk frontend-kravene.
- Sjekk av spinen mot PRD-en med `bmad-review` (linsene adversarial og edge-case). Brukeren godtok anbefalingene for de fire PRD-punktene.
- Epics steg 2: 10 epics. Brukeren delte Epic 2 i to og beholdt Epic 9 og 10 som egne epics. Steg 3: storyer for hver epic, godkjent én epic om gangen.

### Resultat
Gren `docs/epics-and-stories`:
- Commit `95e4c4f`:
  - **Spinen:** omdøpt til «LifeMode MVP».
    - AD-17: `gateFor(envelope, session)`, med fullskjermporter (start, oppsett, oppsummering, slutt) og Hjem-porter (resultat, årsslutt, hendelse, krise) i fast rekkefølge.
    - AD-18: én spillklient med en sideøkt-record, single-flight, samme `request_id` ved nye forsøk etter 2, 5 og 10 s, og faste henteutløsere.
    - AD-19: `tokens.css` generert fra DESIGN.md, CSS Modules og `components/ui/`.
    - AD-20: Vitest, Playwright mot compose-stacken i Chromium og WebKit, og axe i CI.
    - Tillegg i AD-10, AD-12, AD-13 og AD-14, nye konvensjoner og nye versjoner (Next.js 16.4.x ≥ 16.4.5, Vitest 5, TS 5.9, `engines.node` 24.x).
  - **`SOLUTION-DESIGN.md`:** del 9 er skrevet om for frontend.
  - **`DESIGN.md`:** seks avatarutseender som `scene-look-1-*` til `scene-look-6-*` (fargene er hentet fra mockupen), og teksten er markert final.
  - **`EXPERIENCE.md`:** viser til AD-17 for ruter, `#`-kolonnen gjelder bare mockupen, og menyen er `/meny`.
  - **Memloggen:** oppføringene 100-115, inkludert «spine finalized».
- Commit `9d9d0c5`: `epics.md` med kravinventaret (steg 1) og frontend-kravene. Steg 2 (design av epics) er ikke startet.
- Lint av spinen gir bare den kjente falske treffen `{client_ip}`.
- PR #129 er opprettet fra grenen. #122 lukkes ved merge.
- Commit `bf44e3e`: rettelser fra sjekken av spinen mot PRD-en (30 funn i `reviews/review-2026-11-23-spine-vs-prd.json`).
  - **AD-17:** `recapDue` og `year_end`, og årsslutten kommer etter desembers hendelse og krise.
  - **AD-18:** løpenummer og epoker, en tapt utlogging regnes ikke som gjort, tidsavbrudd og nye forsøk hvert 30. s, og en liste over `announce()`.
  - **AD-13:** `year_end`, `continue_warning`, `crisis_skipped` og `client_times`.
  - **AD-12 og AD-20:** personverninfo på `/ny-bruker`, Firefox og `wcag22aa`.
  - **PRD:** FR-5 (nettleserøkt), FR-25 og NFR-7 (steg på 1 000 kr), NFR-1 (Firefox i den automatiske kjøringen). Addendumet, `EXPERIENCE.md` og `SOLUTION-DESIGN.md` sier det samme.
- Commit `009aaf5`: `epics.md` med epic-liste, FR-dekningskart og 64 storyer i 10 epics. Alle FR-er og UX-DR-er er dekket av minst én story. `stepsCompleted: [1, 2]`.
- Pushet til `docs/epics-and-stories`, og PR #129 er oppdatert med beskjed om at det må gjøres review.

### Åpne punkter
- Epics steg 4: sjekk avhengighetene mellom storyene før sprint-planlegging, som brukeren ba om (#130).
- Spørsmålet om hvordan frontend vet at e-post er av i playtesten hører til #125.
