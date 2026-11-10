# PRD-revisjon: mer spill, mindre quiz

## 2026-11-10 kl. 14:45 — Myggsaa

### Oppgave
Finne ut hvor prosjektet står i BMad og hva som er neste steg. Teamet har bestemt at PRD-en skal endres, slik at LifeMode blir mer et livssimuleringsspill med fire områder: kalender, jobb, mobil og økonomi. Første steg var et revisjonsforslag til PRD-en, ikke ferdige endringer. KI skal kunne fungere som spillmotor i V2, ikke i V1.

### Plan
- Kjørte `bmad-help`. PRD-en er final på main. Arkitekturen er i gang (beslutningslogg, men `ARCHITECTURE-SPINE.md` er fortsatt malen). UX-dokumenter mangler.
- Vurderte UX-konseptskissene (kalender med aktivitetsplasser, jobb, mobilinnboks, økonomi) mot PRD-en. Fant avvik: plasser per måned i stedet for timer per uke, og flere handlinger per måned.
- Byttet til `main`, laget ny gren `docs/prd-endringer` og startet `bmad-prd` i oppdateringsmodus.
- Leste hele PRD-en, PRD-tillegget, regelsettet Rule Set v1 og beslutningsloggen. Skrev deretter et revisjonsforslag i stedet for å endre PRD-en direkte, slik teamet ba om.
- Plandokument: `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/revision-proposal-2026-11-10-game-loop.md`

### Resultat
- **Nytt:** `revision-proposal-2026-11-10-game-loop.md` (ikke committet). Forslaget inneholder:
  - Ny månedsløkke innenfor den todelte måneden i FR-49. Rekkefølgen i regel 1 er uendret.
  - Tabell over hva som kan gjenbrukes, per område.
  - Forslag P1–P8 med anbefalinger. Antall aktivitetsplasser regnes ut fra fritiden i regel 12, så timer forblir eneste kilde til lønn og fritid. Aktiviteter trekkes når spilleren går videre. Ekstravakter gjelder fortsatt fra neste måned. Faste tilbud kommer som meldinger, med 4 hendelsesmåneder i året. Aktiviteter gir trivselseffekt innenfor et månedstak, og sluttoppsummeringen slår dem sammen per type. Et eget avsnitt beskriver hvordan V2-KI kan kobles på.
  - Konflikttabell mot regel 1, 7, 10, 12 og 16 og FR-9/13/14/17/18/23/42/46/48/49, NFR-2/7/8 og UX-skissene.
  - Fordeling mellom MVP og V2.
  - Forslag til PRD-tekst: nye FR-52 til FR-57, ny brukerreise UJ-6 (utkast), endringer i eksisterende krav, OQ-17 til OQ-22, nye worked examples 24–26 og omregning av 17a/17b/21/23.
- Overlappsberegning for FR-43 med P4: 51 % med 40 hendelser og 42 % med 50, mot 64 % i dag.
- `prd.md`, PRD-tillegget og Rule Set v1 er ikke endret. Ingen beslutninger er registrert som godkjent. Beslutningsloggen har fått én hendelseslinje om at oppdateringen er startet.
- Arkitekturmappen `architecture-IBE160-G13-2026-11-09/` ligger fortsatt ucommittet i arbeidskopien.

### Åpne punkter
- Teamet må avgjøre P1–P8 og OQ-17–22 i revisjonsforslaget. Deretter kjøres `bmad-prd` update, og arkitekturen fullføres mot den oppdaterte PRD-en (#54)
