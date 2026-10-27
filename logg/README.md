# Promptlogg (avsluttet prototype)

> **Status: avsluttet 2026-10-27.** Dette var en prototype-logger gruppen laget før Bård kom med sin løsning, `sesjonslogg`-skillen (se `.claude/skills/sesjonslogg/SKILL.md` og `CLAUDE.md`). Nye økter dokumenteres nå i `.logs/<bruker>/`. Promptene som ble logget her fra 2026-10-08 til 2026-10-27 er beholdt uendret som dokumentasjon av prosessen.

Mappen inneholder prompts gruppen sendte til Claude Code i dette repoet mens loggeren var i bruk. Loggen ble skrevet automatisk.

## Hvor finner jeg hva?

- `prompts/<navn>.md`: én fil per gruppemedlem, med navn fra `git config user.name`. Nyeste prompt ligger nederst.

Hver person hadde sin egen fil, slik at loggene ikke ga merge-konflikter når flere jobbet samtidig.

## Format

Hver prompt ble logget som én oppføring:

````markdown
## 2026-10-08 14:32:05

| Felt | Verdi |
|---|---|
| Dato | 2026-10-08 |
| Klokkeslett | 14:32:05 (UTC+02:00) |
| Person | Myggsaa |
| Branch | `main` |
| Økt-ID | `3f9a1c2e` |
| Verktøy | Claude Code |

```text
Selve prompten, ordrett.
```
````

| Felt | Betydning |
|---|---|
| Dato / Klokkeslett | Når prompten ble sendt, i lokal tid med tidssone |
| Person | Git-navnet til den som skrev prompten |
| Branch | Git-branchen personen sto på |
| Økt-ID | De første 8 tegnene av Claude Code-øktens ID. Prompts med samme ID hører til samme samtale. |
| Verktøy | Hvilket AI-verktøy prompten ble sendt til |

## Slik fungerte det

En `UserPromptSubmit`-hook i `.claude/settings.json` kjørte `.claude/hooks/log_prompt.py` hver gang noen sendte en prompt i Claude Code i dette repoet. Skriptet la til en oppføring i personens loggfil, og maskerte passord, API-nøkler, tokens, fødselsnumre, kortnumre og e-postadresser med `********` før de ble skrevet.

Hooken er fjernet fra `.claude/settings.json`, så ingen nye prompts blir logget. Skriptet ligger igjen i `.claude/hooks/` som en del av prototypen.

## Regel: sensitiv informasjon

Regelen gjelder fortsatt for de eksisterende loggfilene: blir det funnet passord eller annen sensitiv informasjon i dem, byttes den ut med `********`. Har en hemmelighet allerede blitt pushet, må den regnes som lekket og byttes ut (ny nøkkel eller nytt passord).
