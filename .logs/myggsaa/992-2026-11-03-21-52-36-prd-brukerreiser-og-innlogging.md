# PRD: brukerreiser og innlogging

## 2026-11-03 kl. 21:52 — Myggsaa

### Oppgave
Fortsette PRD-en for LifeMode med `bmad-prd` (journey-ledet coaching): hente inn kildene, skrive brukerreisene og avklare det de reiser av spørsmål. Til slutt pushe arbeidet til GitHub for merge og fortsette i morgen.

### Plan
- Gjenoppta PRD-kjøringen i `.docs/planning-artifacts/prds/prd-IBE160-G13-2026-10-22/`, og flette inn `origin/main`.
- Hente ut kildene med tre delagenter til `extract-*.md`, og la `.memlog.md` gjelde der eldre dokumenter sier noe annet.
- Fange én brukerreise om gangen med Markus, 15 år, og skrive krav der teamet ba om det.

### Resultat
Arbeidet ligger i commit 500a961.

**PRD-en (`prd.md`):**
- UJ-1 (første økt), UJ-2 (fortsetter på skole-PC) og UJ-3 (sparing gir renter) er bekreftet.
- FR-1 til FR-5 dekker konto og innlogging, og FR-6 til FR-8 dekker lagring og synkronisering.

**Beslutninger (`.memlog.md` og PRD-ens `addendum.md`):**
- **Innlogging:** e-post og passord, med glemt passord på e-post og bytte av passord i spillet. Dette erstatter brukernavn uten e-post og uten tilbakestilling. Ingen e-postbekreftelse før spillet starter, men e-postadressen skrives to ganger.
- **Start:** pengegave på tilfeldig 10 000-30 000 kr, og det første reelle valget er hva spilleren gjør med pengene.
- **Med i MVP-en:** teaser ved slutten av økten, ett rom med noen få tilstander, enkel visning av framtidige muligheter, og det som låses opp etter alder i spillet. Én økt er ett år i spillet, og spilleren låses aldri ute i sanntid.
- **Senere:** utvikling av avatar og hjem, opplåsing etter måloppnåelse, nye områder og fond. Renter under lange pauser er tatt ut av MVP-en.
- **Mopedlappen:** spilleren betaler for kjøretimer, obligatoriske timer og lappen, etter reelle priser.
- **Annet:** ekte rentetall vises selv om de er små, og noen hendelser får korte, generelle tips.

**Andre dokumenter:** brief, briefens addendum, arkitektur og møteforberedelsen er oppdatert til e-postinnlogging. Speltestnotatene er oppdatert med hele teamets vurdering.

**Issues:** #12 og #13 er lukket. #24 har fått ny kommentar og ny tittel om e-post.

**Ikke gjort:**
- Endringene etter `/usage` er foreslått, men ikke gjennomført: Sonnet som standardmodell for delagenter, og 15 ubrukte skills slått av. De venter på svar fra Myggsaa, og innstillingene er ikke endret.
- Statuslinjen ble ikke satt opp, fordi det ikke finnes noen PS1-innstilling å bygge på.

### Åpne punkter
- UJ-4, UJ-5, resten av PRD-seksjonene og finaliseringen gjenstår. UJ-4 er stilt med et eksempel, men ikke besvart (#28).
- Reelle priser for mopedlappen er ikke funnet (#29).
- Sending av e-post for glemt passord må virke med null løpende kostnad og når sensor kjører lokalt (#30).
- Innlogging på delte skole-PC-er er utsatt av teamet (#31).
- Brief og arkitektur beskriver fortsatt KI som en del av første versjon (#32).
- Personvern for e-postadresser må sjekkes før lansering (#24).
