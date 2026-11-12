# PRD-tilbakemelding og gammel gren

## 2026-11-12 kl. 15:09 — saegg1205

### Oppgave
Finne ut om den gamle grenen `docs/prd-sara-endringer` fortsatt trengs. Grunnlaget var lærerens PRD-tilbakemelding (`tilbakemelding-prd.md` på main), sammenlignet med PRD-en på grenen og med det som allerede var tatt inn på main. Etter enighet i gruppa skulle grenen slettes hvis den var overflødig.

### Plan
- Bytte fra `ux/sara-design-thinking` til `main` og hente de nyeste endringene med `git pull origin main`.
- Lese `tilbakemelding-prd.md` og gå gjennom hvert punkt mot `prd.md` på `docs/prd-sara-endringer`.
- Finne commit-ene som bare lå på grenen, og sjekke om innholdet deres finnes på main.
- Slette grenen lokalt og på GitHub hvis ingenting gikk tapt. Analysen gjorde ingen endringer i filer.

### Resultat
- **Pull:** main ble spolt fram fra `2e0981e` til `73d4b74`. Med kom `.docs/planning-artifacts/architecture/technology.md` og `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/tilbakemelding-prd.md`.
- **Lærerens tilbakemelding gjelder main, ikke grenen:** læreren vurderte `prd.md` på main (commit `755b3b7`, status final). PRD-en på grenen var en eldre utgave (status draft) uten review-rettelsene fra 2026-11-11.
- **Lærerens punkter mot PRD-en på grenen:**
  - *Dekket:* tese, testbarhet og ærlig avgrensning (det læreren roser). UJ-ene står i kronologisk rekkefølge, fordi grenen nummererte brukerreisene etter alder.
  - *Delvis dekket:* omfang og kutt (4.1: kuttliste og «These always stay», men ingen nivåer, datoer eller kuttpunkter), drift og lokal kjøring (4.2: seedede testbrukere i NFR-6, men ingen reservevei, og OQ-14 er åpen), «final» og plassholdere (4.4: status draft, men ingen parametertabell), antakelser i PRD-en (F5-flyttingen står i §7.3) og refleksjonsspørsmål 1 (kildene til revisjonen 2026-11-10).
  - *Mangler:* oversikt over FR-ene, oppdeling av FR-9, FR-32 og FR-46, og regler skrevet ut i FR-ene (4.3). Videre ID-er på suksessmålene (4.5), avklaring av OQ-6, innsnevring av livsløp og innlogging, og tallene «42, 46 og 37» (refleksjonsspørsmål 2). Main mangler det samme, bortsett fra tallene.
- **Det som bare lå på grenen er allerede håndtert på main:** commit `755b3b7` (sarahnaess, 2026-11-11) tok for hånd inn kildene til revisjonen 2026-11-10, OQ-19 (aktiviteter teller bare i sin egen måned), at ekstravakter kan avsluttes fra neste måned, og sesjonsloggen `998-2026-11-11-01-55-31-prd-kilder-uj4-oq19.md`. Konsertreisen i måned 15 og omnummereringen av brukerreisene ble bevisst valgt bort. Begrunnelsen står i main `prd-IBE160-G13-2026-10-22/addendum.md` under «Not taken from that branch».
- **Grenen er slettet:** først lokalt med `git branch -d` (den pekte på `da2ec45`), så på GitHub med `git push origin --delete`. Det skjedde etter enighet i gruppa. Commit-ene finnes fortsatt i Git-historikken.
- Ingen PRD eller andre dokumenter ble endret i økten.

### Åpne punkter
Ingen nye. Oppfølgingen av lærerens tilbakemelding følges allerede i #66 (nivåer kjerne/utvidelse/kan kuttes), #67 (fullføre PRD-oppdateringen), #70 (refleksjonsspørsmålene), #46 (datoer) og #47 (vertskap). Kronologisk UJ-nummerering, som læreren foreslo og som grenen hadde, hører inn under #67 hvis gruppa vil gjøre det på main.
