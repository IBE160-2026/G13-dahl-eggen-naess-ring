# Merge av arkitektur-spine

## 2026-11-16 kl. 11:42 — sarahnaess

### Oppgave
Brukeren ba om `bmad help` for å se hvor prosjektet står i BMad-flyten, og spurte så om arkitektur-PR-en (#94) burde merges til `main`. Svaret var ja, og brukeren ba om godkjenning og merge.

### Plan
- Kjørte `bmad-help`: brief og PRD er final. Arkitekturen lå i PR #94. UX-dokumentene er tomme utkast, og ingen av de 8 konseptene er valgt (#65). Epics, stories og sprintplanlegging er ikke startet.
- Gikk gjennom PR #94: mergeable, ingen konflikter, `main` hadde ingen commits som manglet på grenen, ingen sjekker og ingen reviews.
- Kontrollerte hovedpåstanden i PR-en: regel 5 og regneeksempel 7 i Rule Set v1 på `main` sier allerede brukskonto og så sparekonto for kortregningen. Den rettede FR-45-tabellen stemmer altså med reglene.
- Pekte ut den reelle regelendringen: regel 4 (familielån-avdrag betales nå fra brukskonto og så sparekonto, aldri under 0 kr) og regneeksempel 8. I tillegg kommer engangslenke i stedet for e-post i playtesten (FR-3, NFR-11).

### Resultat
- PR #94 er godkjent av sarahnaess og merget til `main` (merge-commit `761e912`). Godkjenningen nevner endringen i regel 4 og engangslenken.
- Merge lukket #90 (gjennomgang av PRD-endringene fra arkitekturavstemmingen).
- Arkitekturen ligger nå på `main` i `.docs/planning-artifacts/architecture/architecture-IBE160-G13-2026-11-09/` (`ARCHITECTURE-SPINE.md`, `SOLUTION-DESIGN.md`, `reviews/`).
- Lokal `main` er oppdatert med fast-forward.
- Neste steg i BMad: UX (`bmad-ux`) etter at et konsept er valgt, deretter epics og stories (`bmad-create-epics-and-stories`) og sprintplanlegging.

### Åpne punkter
- Avgjør om reviewer-gaten skal kjøres på nytt på spinen. Anbefalingen er å lukke den, fordi avstemmingen mot PRD-en er nok (#93).
- Dahl kontrollerer betalingstabellen i FR-45 mot Rule Set v1. PR-en lenket ikke til issuet, så det er fortsatt åpent (#87).
- Avklar grensen mot frontend før stories (#91).
- Kjør hosting-spiken i sprint 1 (#92).
- Velg UX-konsept før DESIGN.md og EXPERIENCE.md skrives (#65).
