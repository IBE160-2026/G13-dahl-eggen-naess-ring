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
- Commit `ca6119d`: diagram 05 (`diagrams/05-hvilken-skjerm.svg`, laget i en annen økt) viste årsslutten før hendelsen. Nå kommer den etter hendelse og krise, som i AD-17.
- Pushet til `docs/epics-and-stories`, og PR #129 er oppdatert med ny tittel og beskrivelse, og en kommentar om at det må gjøres review.

### Åpne punkter
- Epics steg 4: sjekk avhengighetene mellom storyene før sprint-planlegging, som brukeren ba om (#130).
- Spørsmålet om hvordan frontend vet at e-post er av i playtesten hører til #125.

## 2026-11-25 kl. 19:06 — Myggsaa

### Oppgave
Brukeren spurte hva neste BMad-steg var, hentet det nyeste fra GitHub (#131 og #129 var merget) og ba om steg 4 i `bmad-create-epics-and-stories`: sluttsjekken av dekning og avhengigheter mellom storyene (#130). Etterpå ba brukeren om commit, push og PR, og om å oppdatere #130 og #133.

### Plan
- `git pull` på `docs/epics-and-stories` (fast-forward til `7ec2b0e`), så bytte til `main` og pull (`34de3f2`). Ny gren `docs/epics-steg-4`.
- Steg 4: hele `epics.md` lest (72 storyer). Dekningen ble sjekket med skript, og alle henvisninger til senere storyer ble listet og vurdert. Saras log (`../saegg1205/991-2026-11-24-20-12-40-review-pr-129.md`) og kommentaren i #130 ble sjekket mot teksten.
- 8 funn ble lagt fram. Brukeren valgte å rette alle unntatt funn 2 (1.4 og 10.4), som venter på Sara. Rettelsen av funn 1 og 4 ga nye henvisninger framover, og brukeren valgte å bytte numre.

### Resultat
- **Sjekket og i orden:** alle FR (unntatt FR-35 og FR-51), alle 45 UX-DR, alle NFR og AD-1 til AD-20 er nevnt i storyene. Ingen startmal, og tabellene lages når de trengs. Alle punktene i kommentaren i #130 er løst i teksten.
- Commit `7e10ae6` på `docs/epics-steg-4` (`epics.md`):
  - **2.3 ↔ 2.4:** pengegaven (kjerne) er 2.3 og bygger speilet (UX-DR7) og tidslinja (UX-DR6). Avataren (utvidelse) er 2.4.
  - **4.1 ↔ 4.2:** årsslutten (kjerne) er 4.1 og legger tabellen over aldersvalg (FR-18) i config. «Året» er 4.2.
  - 4.3 (linja om slutten fjernet), 6.1 (krisemåneder testes i 7.7), 8.1 (forberedte flagg), 9.1 (nivålinje), Epic 10 og dekningskartet (daglig sjekk og NFR-11 i 1.9), og en merknad om at 8.11 kan bygges før 8.6.
  - Nivåtabellen, lenkeregelen og henvisningene i 2.5, 5.3 og 5.5 bruker de nye numrene. Ingen andre filer bruker numrene.
- Pushet, og PR #134 er opprettet mot `main`.
- #133 fikk ny tittel (story 4.2) og en kommentar om at tabellen ikke lenger avhenger av den. #130 fikk en kommentar med funnene.
- `stepsCompleted` er fortsatt `[1, 2, 3]`. Brukeren vil vente på at gruppa godkjenner.

### Åpne punkter
- Gruppa godkjenner storyene i #134. Så settes `stepsCompleted` til `[1, 2, 3, 4]`, og #130 lukkes (#130).
- Sara avgjør om testen av innlogget på forsiden kjøres i 1.4 eller 10.4 (#135).
- Velg nivå for 4.2 «Året» (#133).
- Sett opp låsen på `main` før første story, som brukeren vil ta neste (#132).

## 2026-11-26 kl. 13:32 — Myggsaa

### Oppgave
Brukeren spurte hva neste BMad-steg var, hentet det nyeste fra GitHub, ba om å pushe loggen fra forrige økt og tok opp #130. Etterpå ba brukeren om en SVG-visualisering av epics og storyer (laget av en underagent), om å se alle epics og storyer på en side i Claude, og om min mening om hva som står på «kan kuttes». Brukeren ba meg ikke kutte noe jeg mener ikke må kuttes, og ba om det jeg anbefalte for å gjøre det lettere å bygge inn AI som spillmotor senere.

### Plan
- `bmad-help`: planleggingen er ferdig fram til sprint-planlegging, som venter på at gruppa godkjenner storyene (#130).
- `git pull`: #134 var merget (`85b8b35`, av sarahnaess) og grenen `docs/epics-steg-4` slettet på GitHub. Byttet til `main` og pullet.
- Loggcommiten `519254b` var bare lokal. Den ble kopiert til `main` med cherry-pick og pushet, slik tidligere logger er pushet rett til `main` (`main` har ikke lås ennå, #132).
- #130: #134 er merget uten formell review. Brukeren vil ikke regne mergen som godkjenning og vil vente.
- Kan kuttes: gikk gjennom 8.4, 8.5 og 9.4 mot PRD §4.4, FR-9a og SM-9. Bare «Hva kommer neste måned» bør ikke kuttes. BSU-sammenligningen kan kuttes, fordi BSU læres i 3.2, ved årsslutten i 4.1 og i skattefradraget.
- AI i V2: sjekket «Ready for V2: AI as game master» i addendumet og AD-1, AD-7 og AD-8 i spinen. Det meste er alt på plass. Tre billige skjøter ble lagt til, uten nye funksjoner.

### Resultat
- `main` er à jour med `origin/main`, og loggen fra 2026-11-25 er pushet (`12734a3`).
- #130 har fått en kommentar som ber gruppa godkjenne storyene i `main`. Kommentaren sier 72 storyer. Etter delingen av 9.4 er det 73.
- Ny gren `docs/fr57-kommende-kostnader` (ikke pushet):
  - `0db05cf`: FR-57 er kjerne for kostnadene som kommer, og sparemålet og aktivitetsforbruket står fortsatt først på kuttlista. PRD §4.4, FR-oversikten, FR-57, memloggen og addendumet er oppdatert. I `epics.md` er 9.4 «See what's coming next month» (kjerne) og 9.5 «Pin a savings target and see this year's activity spend» (kan kuttes).
  - `1c9e765`: AD-7 har én funksjon som sjekker ett element mot et lastet bibliotek. AD-8 har egne funksjoner for å foreslå og å sjekke, og `source: library` på lagrede elementer. Story 2.1 og 2.6 og AD-linjene i `epics.md` er oppdatert, og memloggen for arkitekturen har fått en oppføring. Lint av spinen gir bare den kjente falske treffen `{client_ip}`.
  - `dbb7df5`: `.docs/planning-artifacts/epics-diagrams/01-oversikt.svg` og `02-avhengigheter.svg`, laget av en underagent og sjekket som gyldig XML.
- Artifact (lenkedelt): https://claude.ai/artifact/HwGTeDrrAmcJUvaRK4EoqJ, med alle 73 storyene, søk, filter på nivå og begge diagrammene.
- Underagenten fant noe uklart i `epics.md`: 4.6 viser til 9.3, som kommer i en senere epic og er utvidelse. Det er ikke rettet.
- PR #137 ble opprettet med de tre commitene og loggene. Den er merget (`0913cee`).
- En egen side med alle de åtte diagrammene (seks for arkitekturen, to for epics), med en kort forklaring til hvert: https://claude.ai/artifact/7izxJ6RzyPtmgtVitxyCL9 (privat til den deles). Brukeren valgte bort de 201 UX-skissene i `.working`.
- Logger som bare lå lokalt, er pushet til `main`: `e189f72` og `c58961a` (fr48-familielan fra 2026-11-23).
- Utdaterte grener er slettet, lokalt og på GitHub, etter en sjekk av at PR-en er merget og at alt på grenen ligger i `main`: `docs/epics-and-stories`, `docs/epics-steg-4`, `docs/fr48-familielan`, `docs/fr57-kommende-kostnader`, `docs/arkitektur-116`, `docs/klarhet-for-epics`, `docs/sara-review-129` og `docs/issue-opprydding`.
- `docs/issue-opprydding` hadde en commit som aldri kom inn i `main` (`babe2a8`, reviewer-gate 2026-11-22, #93). Brukeren valgte å ta den med. Den er kopiert til `docs/arkitektur-gate-2026-11-22` (`cc3cbd4`, med konflikten i memloggen løst til én ny linje), og PR #138 er opprettet.
- 4.2 «See my year» er utvidelse etter brukerens valg (`4ee670f`), og oversiktsdiagrammet er oppdatert av underagenten (`6edb4e9`). Begge sidene i Claude er oppdatert. PR #139 lukker #133 ved merge. Nå har alle 73 storyer et nivå.

### Åpne punkter
- Gruppa godkjenner storyene, nå med 9.4/9.5 og AI-skjøtene. Så settes `stepsCompleted` til `[1, 2, 3, 4]`, og #130 lukkes (#130).
- Avgjør om testen av innlogget på forsiden kjøres i 1.4 eller 10.4 (#135).
- Sett opp låsen på `main` før første story (#132).
- Avgjør hva 4.6 tar vare på om 9.3 kuttes, siden 4.6 viser framover til 9.3 (#136).
