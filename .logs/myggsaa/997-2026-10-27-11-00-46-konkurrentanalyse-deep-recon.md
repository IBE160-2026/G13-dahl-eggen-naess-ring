# Konkurrentanalyse (deep recon)

## 2026-10-27 kl. 11:00 — Myggsaa

### Oppgave
Brukeren spurte hvor prosjektet står i BMad, og deretter om konkurrentundersøkelsene er gode nok. Etter en vurdering av hullene i `market-research.md` ble det kjørt en avgrenset `bmad-deep-recon` (competitive) her i Claude Code, med eksplisitt norsk og nordisk søk etter brukerens ønske.

### Plan
- `bmad-help`: statusvurdering. Briefen er final, PRD-en er stoppet etter discovery (8 linjer, journeys UJ-1–UJ-5 bekreftet i memlog). Neste påkrevde steg er `bmad-prd`.
- Vurdering av eksisterende konkurrentanalyse: mangler kategorien pengesimuleringsspill for skolen, KI-spill fra 2025–2026 er ikke sjekket, kildene er bare domenenavn, og det finnes ingen sammenligningstabell.
- Plan for deep recon (godkjent av brukeren): D1 internasjonale skolespill, D1b norske og nordiske spill, D2 KI-drevne finansspill 2025–2026, D3 sammenligningstabell. Tre parallelle forskningsagenter i runde 1, og en kort runde 2 kjørt av hovedagenten for det norske hullet og Life Finance.
- Planen er loggført i run-mappas `.memlog.md`.

### Resultat
- Ny mappe (ukommittert): `.docs/planning-artifacts/briefs/brief-Ibe160-prosjektmappe-2026-09-17/research/competitive-youth-finance-sim-games-gap-fill-2026-10-27/` med `research.md`, `digests/` (4 filer) og `.memlog.md`.
- `research.md`: status complete, 20 kilder med URL og tilgangsdato, mekanisk kildekontroll ok (20/20), 5 verifiserte og 2 uverifiserte påstander, sammenligningstabell med 12 produkter og LifeMode til kontrast, samt foreldelseskart.
- Hovedfunn: posisjoneringen holder bare i smal form. Ingen live produkt for unge kombinerer en deterministisk finansmotor med KI-fortelling, men arkitekturen finnes allerede (Life Finance, hackathon-prosjekt, uverifisert). Nærmeste reelle konkurrent er svenske *Koll på cashen* (Finansinspektionen og Riksbanken, 2025), som mangler i market-research.md. Ingen norsk digital privatøkonomi-simulering for 15–20 ble funnet, og ingen skolespill bruker KI.
- Hoppet over: semantisk kildesjekk med egen agent, HTML-briefing og doc_standards-gjennomgang (struktur og prosa).

### Åpne punkter
- Snevre inn differensieringspåstanden i brief/PRD og legg Koll på cashen og PersonalFinanceLab inn i market-research.md (#12)
- Spill Koll på cashen og prøv PersonalFinanceLab før UX-reisene i PRD-en (#13)
- Åpne spørsmål: Life Finance, Taloussankari, norske kilder som ikke er søkt, tilgjengelighet i norsk App Store (#14)
