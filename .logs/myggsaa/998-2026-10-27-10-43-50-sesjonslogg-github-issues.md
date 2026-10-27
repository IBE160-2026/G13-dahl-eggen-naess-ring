# Sesjonslogg-github-issues

## 2026-10-27 kl. 10:43 — Myggsaa

### Oppgave
Ta i bruk GitHub Issues for åpne punkter fra sesjonsloggene, slik at de lagres som issues i repoet og ikke i en lokal `issues.md`. (Økten startet med `bmad-help`. Neste BMAD-steg, å fullføre PRD-en, er utsatt til senere.)

### Plan
- Ny gren `sesjonslogg/github-issues`, stablet på `logg/avslutt-promptlogg` (PR #9), fordi `.logs/` ikke finnes på `main` ennå.
- Skrive om `issues.md`-delen av `sesjonslogg`-skillen til en GitHub Issues-rutine med `gh`, og oppdatere `CLAUDE.md`.
- Flytte de eksisterende åpne punktene til issues og fjerne `issues.md`.

### Resultat
- `.claude/skills/sesjonslogg/SKILL.md`: åpne punkter blir issues med label `sesjonslogg` og `--assignee @me`. Skillen sjekker først for duplikater med `gh issue list`, skriver issuenummeret i loggen og lukker issues med `gh issue close --comment` eller `Closes #N` i en PR. Uten `gh` eller remote skal den si fra, ikke falle tilbake til en lokal liste. Loggcommiten inneholder nå bare loggfila.
- `CLAUDE.md`: instruksen peker til GitHub Issues.
- Labelen `sesjonslogg` er opprettet i repoet.
- Issue #10 (godkjenning av at promptlogg-hooken fjernes) og #11 (kravet om lagrede prompts i sensorveiledningen) er opprettet fra den gamle `issues.md`. Fila er slettet, og den gamle loggen har fått issuenumrene.
- Commit eaf1e6a på `sesjonslogg/github-issues`. Etter at PR #9 ble merget, ble grenen pushet og PR #15 opprettet mot `main`. Bare de to commitene fra denne økten er med. Den lokale grenen har i tillegg loggcommiten `7a0546f` fra en annen økt (konkurrentanalyse-deep-recon), og den ble holdt utenfor.
- #10 er lukket, siden PR #9 er merget og hook-fjerningen dermed godkjent. Lenkene i #10 og #11 peker nå til `main`.

### Åpne punkter
Ingen.
