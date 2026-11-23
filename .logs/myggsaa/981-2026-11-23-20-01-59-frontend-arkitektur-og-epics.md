# Frontend-arkitektur og epics steg 1

## 2026-11-23 kl. 20:01 — Myggsaa

### Oppgave
Brukeren startet `bmad-create-epics-and-stories`. Under steg 1 så brukeren at arkitekturen manglet frontend, selv om `technology.md` har den med. Siden gruppa nå selv er frontend-teamet, ble arkitekturspinen utvidet med frontend (#122), før epics-løpet fortsetter. Til slutt ba brukeren om en PR.

### Plan
- Epics steg 1: kravinventaret (FR, NFR, AD-er, UX-DR1 til UX-DR45, åpne punkter fra klarhetsgjennomgangen) ble skrevet til `.docs/planning-artifacts/epics.md`, og arbeidet ble satt på pause ved menyen [C].
- `bmad-architecture` (Update, Coaching): beslutningene ble tatt med brukeren (rutere og porter A, klientdatalag A, styling B, tester og standardpakke som anbefalt), og leveransen ble både spinen og `SOLUTION-DESIGN.md`.
- Reviewer gate med fire gjennomganger (adversarial, rubrikk, versjoner, avstemming mot UX og PRD) i `reviews/review-2026-11-23-frontend-*.md`. Rettelsene ble lagt inn samlet.
- UX-filene ble rettet etter funnene, og `epics.md` fikk frontend-kravene.

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
- PR er opprettet fra grenen. #122 lukkes ved merge.

### Åpne punkter
Ingen nye. Spørsmålet om hvordan frontend vet at e-post er av i playtesten hører til #125.
