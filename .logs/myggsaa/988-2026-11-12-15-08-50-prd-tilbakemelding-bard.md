# PRD-tilbakemelding fra Bård

## 2026-11-12 kl. 15:08 — Myggsaa

### Oppgave
Sjekke BMAD-status, hente siste endringer, og gå gjennom Bårds formative tilbakemelding på PRD-en (`tilbakemelding-prd.md`, 2026-11-12) med `bmad-prd` i oppdateringsmodus, punkt for punkt. Underveis ble det bedt om subagenter som skulle finne realistiske tall med kilder for verdier som manglet.

### Plan
- `git pull`. Den gamle grenen `docs/prd-endringer` var merget (#58) og slettet, så økten byttet til `main`, hentet, og opprettet grenen `docs/prd-tilbakemelding`.
- Gikk gjennom tilbakemeldingens punkt 4.1–4.5 og de mekaniske funnene, og viste konflikter med tidligere beslutninger før noe ble lagt inn.
- Tre subagenter fant tall: moped og bil, aktiviteter og forbruk, og opplevelse, lån og hosting.
- Alle beslutninger og endringer er logget i `prds/prd-IBE160-G13-2026-10-22/.memlog.md` (oppføring 145–158).

### Resultat
Commit `47b463a` på `docs/prd-tilbakemelding` er pushet.
- **4.1 Nivåer:** venter på teamet. Datoene er foreløpige: playtest 1.12., frys av utvidelser ca. 19.–20.11., og kjernen spillbar ca. 24.–26.11.
- **Playtest:** testperioden og retur-vinduet er kortet ned fra 7 til 3 dager (NFR-11, §7.1, OQ-14).
- **4.2 Hosting og innlogging:** teamet følger Bårds referanseoppsett (`architecture/technology.md`). NFR-5 er endret til «lav kostnad». NFR-6 krever nå én kommando og mock-fallback, med automatisk test som reservevei for e-post. NFR-3 nevner ikke lenger en tredjeparts innloggingstjeneste. Addendumet har merknader om at Supabase Auth er erstattet. Herdingen av innloggingen står fortsatt som punkt 11 på kuttlisten. OQ-14 venter på teamet.
- **4.3:** FR-oversikt øverst i §5. FR-9, FR-32 og FR-46 er delt i a–c. Ny §3.1 «Rule Set v1 in brief» med én setning per regel. Jeg valgte én tabell fremfor ~80 innskutte setninger.
- **4.4:** statuslinja sier «final for UX and architecture; content figures provisional». Frontmatter står som `draft` mens revisjonen pågår. Parametertabellen i Rule Set v1 har fått kolonnene Status, Eier og Frist.
- **4.5:** suksessmål SM-1 til SM-12 med en Validates-kolonne, og motmål CM-1 til CM-5. SM-1, SM-3 og SM-4 måles med skriftlig forklaring som teamet vurderer etter et skjema.
- **UJ-rekkefølgen** står, med begrunnelsen fra 11.11.
- **Research** ligger i `research/prices-oq3-oq17-2026-11-12/`: brukt moped 11 645 kr (regel 14 og eksempel 19 er regnet om), stor opplevelse 60 000 kr, drivstoff, SIFO 2026, aktivitetskatalog, og kilder for forbrukslån, mobil og skjerm. Hosting koster ca. 50–80 kr/mnd. OQ-3 og OQ-17 er krympet.
- Kommentarer om fremdrift er lagt i #29, #30, #43, #46, #47, #48 og #57.

### Åpne punkter
- Teamet bestemmer nivåene kjerne, utvidelse og kan kuttes, og bekrefter datoene (#66, #46).
- Hosting og OQ-14 må avklares med referanseoppsettet og Railway (#47).
- Når 4.1 og hosting er avklart, fullføres PRD-oppdateringen: review, polering, status final og PR mot main (#67).
- Arkitekturloggen fra 9.11. motsier referanseoppsettet: GoTrue, Koyeb og 7 dager. Den må revideres i neste arkitektur-økt (#68). Arkitekturmappa er fortsatt ukommittert.
- Regneeksempel 22 og 23 må regnes om med den nye mopedprisen, og eksempel 20 må sjekkes for mål 3 med 60 000 kr (#48).
- Mopedforsikring trenger et reelt tilbud fra en forsikringskalkulator (#29).
- Aktivitetskatalogen må godkjennes, og seks anslåtte priser trenger kilde (#57).
- Vurderingsskjemaet for de skriftlige forklaringene må skrives før playtesten (#69).
- Teamet bør svare selv på refleksjonsspørsmålene i Bårds tilbakemelding (#70).
