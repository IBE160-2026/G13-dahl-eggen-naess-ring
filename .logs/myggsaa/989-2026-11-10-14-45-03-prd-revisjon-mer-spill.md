# PRD-revisjon: mer spill, mindre quiz

## 2026-11-10 kl. 14:45 — Myggsaa

### Oppgave
Finne ut hvor prosjektet står i BMad og hva som er neste steg. Teamet har bestemt at PRD-en skal endres, slik at LifeMode blir mer et livssimuleringsspill med fire områder: kalender, jobb, mobil og økonomi. Først skulle det lages et revisjonsforslag. Etter at teamet hadde diskutert det, ble alle anbefalingene lagt inn i PRD-en. KI skal kunne fungere som spillmotor i V2, ikke i V1.

### Plan
- Kjørte `bmad-help`. PRD-en er final på main. Arkitekturen er i gang (beslutningslogg, men `ARCHITECTURE-SPINE.md` er fortsatt malen). UX-dokumenter mangler.
- Vurderte UX-konseptskissene mot PRD-en. Laget grenen `docs/prd-endringer` og startet `bmad-prd` i oppdateringsmodus.
- Skrev revisjonsforslaget: `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/revision-proposal-2026-11-10-game-loop.md`. Det står nå som `accepted`.
- Teamet godtok P1–P8 som anbefalt. Dahl valgte også hele revisjonen med kuttliste, foreløpige tuningverdier og hurtigspor.
- Regnet på trivselsbalansen med et skript etter regel 12 før endringene ble skrevet inn. Skriptet ga samme tall som de dokumenterte resultatene i eksempel 17b (34 og 75).

### Resultat
- **Funn under innlegging:** varige aktivitetseffekter hoper seg opp og fjerner den hule seieren. Pengejageren i 17b gikk fra 34 til 65 med én gratis aktivitet i hver plass. P5 er derfor presisert: effekten teller bare i sin egen måned. Da ender pengejageren på 41/44/37 i verste fall (mål 1/2/3), og forsiktig spiller på 82–85. Dette er flagget som OQ-19.
- **`prd.md`** (status `draft`):
  - Visjon og omfang: «tid er like begrenset som penger», nye seksjoner 5.13–5.15 og ny kuttliste der FR-57 og gruppering står øverst og hendelsesminimum er 40.
  - Ordliste og brukerreiser: oppdatert ordliste, endringer i UJ-1/3/4/5 og ny UJ-6 (utkast).
  - Nye krav FR-52 til FR-57.
  - Endrede krav: FR-9, 12, 13, 14, 16, 17, 18, 23, 29, 30, 32, 33, 36, 39, 42, 45, 46 (4 hendelsesmåneder, ingen milepæler), 47, 48, 49, 50 og 51, samt NFR-2/4/7/8/9/10 og §7.
  - Åpne spørsmål: OQ-8 er utvidet, og OQ-17 til OQ-19 er nye.
- **Rule Set v1 (brief-tillegget):**
  - Nye parametere for aktiviteter og meldinger.
  - Regel 1, 7 og 12 er oppdatert.
  - Nye regneeksempler 24–26, regnet med Claudes skript og ennå ikke uavhengig kontrollert.
  - Ny forenkling D26 og oppdatert merknad i 17a.
- **PRD-tillegget:**
  - Arkitekturnotater og ny hendelsesplan (måned 1, 4, 7, 10; tilbudsmeldinger; overlapp 51 % ved 40 hendelser).
  - Skjemaer for aktiviteter og meldinger, og avsnittet «Ready for V2: AI as game master».
  - Beslutningshistorikk P1–P8.
- **Beslutningsloggen** har fått 4 beslutnings- og antakelseslinjer og 4 endringslinjer.
- **Issues:** #54 er lukket som avgjort, #48 har fått en kommentar med de nye tuningverdiene, og #55, #56 og #57 er opprettet.
- Ingenting av PRD-arbeidet er committet ennå. Grenen er ikke pushet. Arkitekturmappen ligger fortsatt ucommittet.

### Åpne punkter
- Regneeksempel 24–26 må regnes om uavhengig, og PRD-en trenger reviewer-pass, triage og polering før den settes final. Deretter kan arkitekturen fullføres (#55)
- Teamet må bekrefte at aktiviteter bare påvirker trivselen i sin egen måned (OQ-19) (#56)
- Aktivitetskatalogen trenger priser og kilder (OQ-17), og teamet må avgjøre om venner går igjen ved navn (OQ-18) (#57)
