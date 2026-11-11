# Impeccable-installasjon

## 2026-11-11 kl. 14:25 — sarahnaess

### Oppgave
Brukeren kjørte `bmad help` for å se hvor prosjektet står i BMad-løpet. Før UX-arbeidet starter, skulle design-skillen Impeccable installeres for Claude Code. Den skal brukes i UX- og frontendarbeidet.

### Plan
- `bmad-help`: leste katalogen og konfigurasjonen, og sjekket planleggingsartefaktene i `.docs/`.
- Søkte på nett etter Impeccable og leste den offisielle README-en (`pbakaus/impeccable`, Apache-2.0) for riktig installasjonskommando.
- Brukeren valgte installasjon for prosjektet, med design-hooken.

### Resultat
- **BMad-status:** PRD-en er final (2026-11-11). Neste steg er UX (`bmad-ux`, anbefalt) og deretter Architecture (`bmad-architecture`, påkrevd). `architecture/architecture_technical_design.md` er et støttedokument fra brief-fasen og ikke output fra `bmad-architecture`.
- **Installert:** kjørte `npx impeccable@latest install --providers=claude --scope=project -y`.
  - Skill: `.claude/skills/impeccable/`, med motor v0.1.21 for darwin-arm64 i `scripts/bin/` (18 MB)
  - Subagenter: `.claude/agents/impeccable-{asset-producer,documenter,finish-reviewer,manual-edit-applier}.md`
  - Hooks (SessionStart, PostToolUse på Edit/Write, Stop): `.claude/settings.local.json`, som er gitignorert
- Installasjonsfilene er ikke committet, i påvente av beslutningen i #61.

### Åpne punkter
- Bestemme hvordan Impeccable deles i gruppa: om 18 MB-binæren skal gitignores, og om hooken skal flyttes til `settings.json` (#61).
