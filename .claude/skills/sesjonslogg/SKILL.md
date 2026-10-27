---
name: sesjonslogg
description: Dokumenterer arbeidssesjonen i `.logs/` i prosjektroten (Oppgave + Plan + Resultat + åpne punkter) og vedlikeholder åpne punkter som GitHub Issues (label `sesjonslogg`), slik at sluttoppsummeringer og «husk at»-punkter ikke forsvinner i chat-scrollback. Bruk denne ved slutten av ENHVER arbeidsøkt eller fullført oppgave som endret tilstand — også små mekaniske økter som en commit, push, publisering eller konfig-endring — alltid før du skriver sluttoppsummeringen til brukeren, og særlig når oppsummeringen inneholder «åpne punkter», «gjenstår», «husk at», «legg merke til», «neste steg», «ikke gjort» eller lignende. Bruk den også når brukeren sier «logg sesjonen», «logg dette», «oppdater loggen», «skriv sesjonslogg», og når du trenger å vite hva som ble gjort i en tidligere sesjon (les da `.logs/` og åpne issues med `gh issue list --label sesjonslogg` i stedet for å gjette).
---

# Sesjonslogg

Formål: brukeren leser ikke alltid sluttoppsummeringen i terminalen, og den forsvinner uansett når vinduet lukkes. Hva som ble gjort og bevisst *ikke* ble gjort skal overleve som Markdown i `.logs/`; hvert reelt «husk at …» / «gjenstår …»-punkt skal i tillegg overleve som et GitHub Issue i prosjektets repo. Loggen er brukerens sesjonshukommelse, mens issuene med label `sesjonslogg` er gruppens samlede liste over det som gjenstår.

## Hvor og når

- Finn prosjektroten med `git rev-parse --show-toplevel` (i et git-worktree: worktreets egen rot). Loggmappen er `<rot>/.logs/<bruker-slug>/` — én mappe per bruker, slik at hver bruker ser sine egne økter adskilt. Slugen er kebab-case av `git config user.name` (f.eks. `bard-pettersen`; mangler navnet, bruk local-part av `user.email`). Opprett mappen hvis den mangler.
- Skriv loggen når en oppgave/økt avsluttes, **før** du skriver sluttoppsummeringen til brukeren — da er alt ferskt, og oppsummeringen kan gjenbruke teksten. I lange økter: oppdater gjerne loggen underveis ved milepæler.
- Rene småspørsmål-økter (ett faktasvar, ingenting endret, ingenting å huske) trenger ikke logg. Alt annet logges.
- Testen for «trenger ikke logg» er **om økten endret tilstand** — ikke hvor liten oppgaven føltes. En commit, push, publisering, migrasjon, seeding eller konfig-endring er tilstandsendring og skal logges selv om den bare tok to kommandoer: det er nettopp de små mekaniske øktene som glemmes først, og loggen er eneste sted et fremtidig «når ble dette pushet, og hva lå i det?» kan besvares. To følgeregler:
  - En økt som *starter* som et spørsmål («er X à jour?») men *ender* i en handling («commit og push det») er ikke lenger en spørsmålsøkt.
  - Inneholder sluttoppsummeringen din et «merk at …»/«husk …»/«gjenstår …»-punkt, har du allerede bevist at økten har noe å miste i scrollback — da logges den, uansett størrelse.

## Ny fil eller fortsettelse?

List filene i **din egen** brukermappe (`.logs/<bruker-slug>/`) først.

- Finnes det en fil der som dokumenterer **samme arbeid/feature** som denne økten fortsetter på? → Gjenbruk den fila: legg en ny dato-seksjon nederst. Filnavnet (med det opprinnelige nummeret og tidsstempelet) beholdes. Ble samme arbeid sist logget av en *annen* bruker (fila ligger i deres mappe), lag i stedet en ny fil i din egen mappe og lenk til deres fil i Plan-seksjonen (`../per-kristian-rekdal/NNN-….md`) — skriv aldri i en annen brukers mappe.
- Nytt arbeid → ny fil: `NNN-yyyy-mm-dd-HH-MM-SS-<tittel>.md` — et **tresifret nedtellende løpenummer** først, deretter dagens dato og klokkeslettet (24-timers, med bindestreker: `14-31-07`). NNN starter på `999` i en tom mappe; neste fil får laveste eksisterende nummer i mappen − 1 (`998`, `997`, …). Nedtellingen gjør at nyeste fil alltid ligger øverst ved vanlig stigende sortering — også på tvers av dager. Klokkeslettet står i tillegg i dato-overskriften inne i fila (se malen). Tittelen er kebab-case og beskrivende — helst feature-navnet: `999-2026-08-08-14-31-07-kurstab-redesign.md`, aldri noe generisk som `…-sesjon.md`.
- Har du allerede logget denne økten i dag (samme fil har en seksjon med dagens dato for samme arbeid)? → Oppdater dagens seksjon i stedet for å legge til en dublett.

## Format

Skriv på samme språk som brukeren. Mal — `# Tittel` kun øverst i en ny fil; hver økt får sin `## dato`-seksjon:

```markdown
# Kurstab-redesign

## 2026-08-08 kl. 14:31 — Bård Pettersen

### Oppgave
Hva brukeren ba om, med intensjonen bak — 1–3 setninger.

### Plan
- Punktliste over den faktiske fremgangsmåten (kort — dette er ikke plandokumentet).
- Finnes det et lagret plandokument (PLAN.md, .docs/plans/…, godkjent plan fra plan-modus
  skrevet til fil), lenk til det her — brukeren skal kunne spore nøyaktig hva planen var.

### Resultat
Hva som ble gjort: endrede filer/områder, commits (hash hvis committet), migrasjoner,
testresultater, hva som ble verifisert. Konkret nok til at en fremtidig sesjon kan
bygge videre uten å gjette.

### Åpne punkter
- Alt som gjenstår, ble bevisst utsatt, eller må huskes. Hvert punkt får et GitHub Issue (se under) — skriv issuenummeret bak punktet: `… (#12)`.
- Skriv «Ingen.» hvis det ikke er noen.
```

Dato-overskriften bærer klokkeslettet for når loggen skrives **og hvem som kjørte oppgaven**: `## yyyy-mm-dd kl. hh:mm — <utfører>` (24-timers; `date "+%F kl. %H:%M"` / `Get-Date -Format "yyyy-MM-dd 'kl.' HH:mm"`). Utføreren er git-brukeren: `git config user.name` (fall tilbake på `user.email`, eller utelat hvis begge mangler). Fortsettelser: legg `## <ny dato> kl. <tid> — <utfører>` **nederst** i den eksisterende fila, med de samme fire underseksjonene — slik ser man også hvem som kjørte hver økt.

## Commit loggfila (alltid)

Etter at loggfila er skrevet (ny fil, ny dato-seksjon eller oppdatert dagens seksjon), **skal** den committes umiddelbart, før sluttoppsummeringen. Ellers blir loggene glemt som ukommitterte filer og kommer ut av sync mellom brukere og maskiner. Dette er et krav, ikke et valg — ikke spør om lov, og hopp det ikke over fordi økten var liten.

**Commit kun loggfila — ingenting annet.** Andre endringer i arbeidskopien (kode, konfig, utracket filer, ting brukeren selv har staget) skal ikke bli med. Bruk en path-begrenset commit, slik at annet som allerede ligger i staging-området ikke dras med:

```sh
git add -- ".logs/<bruker-slug>/<fil>.md"
git commit -m "Logg: <tittel>" -- ".logs/<bruker-slug>/<fil>.md"
```

- Meldingen er `Logg: <tittel>` (tittelen er den samme som i fila, f.eks. `Logg: kurstab-redesign`), pluss eventuelle attribusjonslinjer harnessen krever for commits. Angir prosjektets `CLAUDE.md`/`AGENTS.md` en egen commit-meldingskonvensjon for logger, følg den i stedet.
- Kontroller etterpå med `git show --stat HEAD` at commiten inneholder nøyaktig loggfila. Inneholder den mer, angre med `git reset --soft HEAD~1`, unstage det som ikke hører til, og commit på nytt.
- **Ikke push** med mindre brukeren ber om det i økten. Skillen committer bare lokalt.
- Er `.logs/` git-ignorert, eller er prosjektet ikke et git-repo, hopp over commit og nevn det kort i sluttoppsummeringen.
- Hook-feil: løs årsaken og commit på nytt. Aldri `--no-verify`.
- Loggfila kan ikke selv inneholde hashen til sin egen commit. Under «Resultat» refererer du til commit-hasher for det *arbeidet* som ble gjort, ikke til loggcommiten.

## Hva er (ikke) et åpent punkt?

Et åpent punkt er noe som gjenstår i selve produktet eller prosjektet: en manglende test, en kjent bug, konfig som må settes ved deploy, en beslutning som venter, noe brukeren eksplisitt ba deg huske. Git- og prosesstatus er **ikke** åpne punkter — brukeren ser git-status selv, og slike punkter drukner de ekte. (I Resultat-seksjonen kan commit-hash eller «ukommittert» nevnes kort som faktum.) Eksempler på ting som IKKE skal inn i Åpne punkter eller bli issues:

- «Ingen av endringene er committet — husk å committe.» / «må pushes»
- Samordningsbeskjeder om repo-tilstand: «NN må `git pull` / re-synke klonene sine»
- Observasjoner om førtilstand: «fil X sto som endret/utracket før økten — avklar før commit»

Unntaket er når tilstanden er reelt kritisk — f.eks. en migrasjon er kjørt mot en delt database mens koden ikke er delt, slik at andre kan rammes.

## GitHub Issues

Åpne punkter føres som GitHub Issues i prosjektets repo, med label `sesjonslogg`. Der ser hele gruppa dem, og de kan tildeles, diskuteres og lukkes fra PR-er. Bruk `gh` (repoet utledes fra `origin`). Vedlikehold issuene hver gang du logger, **før** sesjonsfila skrives ferdig og committes, slik at issuenumrene kan stå i loggen:

1. **Les lista først**, så du ikke dupliserer et punkt som alt er åpent:
   ```sh
   gh issue list --label sesjonslogg --state open --limit 100
   ```
   Finnes det et åpent issue for samme sak, gjenbruk det (eventuelt med en kommentar) i stedet for å opprette et nytt.
2. **Opprett** ett issue per nytt åpent punkt. Tittelen er punktet, kort og konkret. Brødteksten forklarer konteksten og lenker til sesjonsfila via grenen den er committet på:
   ```sh
   gh issue create --label sesjonslogg --assignee @me \
     --title "E2e-test for tastaturnavigasjon gjenstår" \
     --body "Fra sesjonslogg [kurstab-redesign](https://github.com/<eier>/<repo>/blob/<gren>/.logs/<bruker-slug>/<fil>.md), 2026-08-08.

   <1–3 setninger om hvorfor dette gjenstår og hva som må til.>"
   ```
   Mangler labelen i repoet, opprett den først: `gh label create sesjonslogg --color 5319e7 --description "Åpent punkt fra en sesjonslogg"`. Ikke opprett noe for `Ingen.`. Skriv issuenummeret bak punktet i loggens Åpne punkter.
3. **Lukk** issues denne økten løste — også fra tidligere sesjoner — med en kommentar om hva som løste det: `gh issue close <nr> --comment "Løst i <commit/PR>, se sesjonslogg <tittel>."`. Løses punktet av en PR, skriv heller `Closes #<nr>` i PR-beskrivelsen, så lukkes det ved merge. Referer til lukkede issues i Resultat.

Er `gh` ikke installert eller ikke innlogget, eller mangler repoet en GitHub-remote: skriv punktene i loggens Åpne punkter som vanlig, og si tydelig i sluttoppsummeringen at issuene ikke ble opprettet og hvorfor. Ikke falle tilbake til en lokal liste.

Unntak: sier prosjektets rot-`CLAUDE.md`/`AGENTS.md` eksplisitt at åpne punkter skal føres et annet sted, følg den instruksen i stedet.

## Forankring i CLAUDE.md/AGENTS.md

Sjekk ved hver bruk om prosjektets rot-`CLAUDE.md` eller `AGENTS.md` refererer til denne skillen (`sesjonslogg`). Gjør ingen av dem det, **legg referansen inn** — det er den instruksen som sørger for at fremtidige økter i prosjektet faktisk logger; skill-beskrivelsen alene er ingen garanti for trigging.

- Legg regelen der prosjektets agent-instruksjoner faktisk bor: i `AGENTS.md` hvis den finnes (eller hvis `CLAUDE.md` bare er en `@AGENTS.md`-import), ellers i `CLAUDE.md`; finnes ingen av dem, opprett `CLAUDE.md` med regelen.
- Hold den kort og tilpass filens eksisterende struktur og språk, f.eks.:
  > **Logg sesjonen.** Når en oppgave/økt avsluttes — før sluttoppsummeringen — bruk `sesjonslogg`-skillen: den logger Oppgave + Plan + Resultat + åpne punkter per bruker i `.logs/<bruker>/`, fører åpne punkter som GitHub Issues og committer loggfila.
- Ikke dupliser: står referansen alt et sted i en av filene, er alt i orden.

## Ved oppstart av en fortsettelse

Når brukeren refererer til tidligere arbeid («fortsett med …», «hva gjorde vi sist med …»), les den relevante fila i `.logs/` (brukerens egen mappe først, deretter eventuelt andre brukeres) og de åpne issuene (`gh issue list --label sesjonslogg`) **før** du begynner — det er raskere og sikrere enn å rekonstruere fra koden eller hukommelsen.
