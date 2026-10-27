# Forarbeid PRD: research

## 2026-10-27 kl. 11:34 — Myggsaa

### Oppgave
Etter konkurranseanalysen ville brukeren ha forslag til research- og brainstormingstema som bør sjekkes før PRD-en lages. Deretter ba brukeren om tre av dem: deep recon på KI-leverandørvilkår for mindreårige (punkt 4), en subagent på norske finansregler (punkt 6) og en subagent på LK20-kobling (punkt 7). Resten skal diskuteres med teamet.

### Plan
- `bmad-help`: status. Brief er final, PRD er et tomt utkast, neste påkrevde steg er PRD.
- `git pull`: grenen `sesjonslogg/github-issues` har ingen upstream. Fetch viste at den er 6 commits foran og 0 bak `origin/main`, så ingenting å hente.
- Ti forslag til tema, gruppert i brainstorm og research. Bruker valgte 4, 6 og 7.
- Punkt 4: `bmad-deep-recon` (technical, select shape, standard preset), godkjent plan. 3 assistenter i runde 1 og 2 i runde 2 (verifisering og hull).
- Punkt 6 og 7: hver sin bakgrunnsagent som kjørte `bmad-deep-recon` headless (domain).

### Resultat
Tre nye research-mapper under `.docs/planning-artifacts/research/` (ikke committet):
- `technical-free-tier-llm-provider-terms-for-minors-2026-10-27/`:
  - Gemini er utelukket. Vilkårene forbyr tjenester brukt av personer under 18 på alle nivåer, og EØS krever betalt nivå.
  - Hugging Face (ingen gratiskreditter), GitHub Models (lagt ned 2026-07-30) og Cerebras (bare en 30-dagers prøvekreditt) er også ute.
  - Valg: Groq (405/500), med Cloudflare Workers AI som reserve (370). Mistral (285) krever samtykke fra foreldre. OpenRouter (205) gir bare 50 kall per dag.
  - 18 påstander verifisert, 4 uverifisert, 1 omstridt. Sitatsjekken er ok.
- `domain-norwegian-youth-finance-rules-2026-10-27/`:
  - Regelen om 50 % over frikortgrensen er tilbakevist. Det er forskuddstrekk, og reell skatt på 110 000 kr er ca. 2 588 kr.
  - BSU-fradraget er 0 kr uten skatt.
  - Arbeidstiden for elever i grunnskolen er maks 2 timer per dag og 12 timer per uke.
  - Kreditt først fra 18 år og utlånsforskriften er bekreftet.
  - 13 påstander verifisert, 2 uverifisert.
- `domain-lk20-personal-finance-curriculum-2026-10-27/`:
  - Nye fagkoder fra 01.08.2026: SAF01-05 og MAT01-06.
  - Best faglig treff er MAT01-06 (10. trinn) og 1P-Y (VG1 yrkesfag).
  - Rapporten har fem forslag til quiz-spørsmål.
  - 8 påstander verifisert, 5 uverifisert.

Steg som ble hoppet over for å holde kjøringene lette: den semantiske sitatsjekken, HTML-briefingen og doc_standards-polering (bmad-review). Begge domenekjøringene ble gjort uten underagenter.

### Åpne punkter
- Rett skatteregelen (regel 3, eksempel 5, F8) og andre finansregler i addendum og brief (#16)
- Fjern Gemini fra arkitekturen. Bruk Groq med Cloudflare som reserve, og sjekk Groqs gratiskvoter og Cloudflares AUP (#17)
- Bruk nye LK20-koder i PRD-en og få quiz-forslagene vurdert av en lærer (#18)
- Teamdiskusjon før PRD: sluttspill, konsekvensforklaring, hendelsesbibliotek, personvern og brukerundersøkelser (#19). Koll på cashen og norske kilder følges allerede i #13 og #14.
