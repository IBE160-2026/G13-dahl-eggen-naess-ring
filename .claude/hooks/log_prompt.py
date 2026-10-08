"""Claude Code UserPromptSubmit-hook: logger hver prompt til logg/prompts/<person>.md.

Leser hook-data (JSON) fra stdin og legger til én oppføring i et fast format.
Feiler stille, slik at en loggfeil aldri stopper selve prompten.
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime


def git(args, cwd):
    try:
        out = subprocess.run(
            ["git", *args], cwd=cwd, capture_output=True, text=True, timeout=5
        )
        return out.stdout.strip()
    except Exception:
        return ""


def fence_for(text):
    # Bruk en kodeblokk-gjerde som er lengre enn alle backtick-rekker i prompten.
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


def main():
    sys.stdin.reconfigure(encoding="utf-8")
    data = json.load(sys.stdin)
    prompt = data.get("prompt", "")
    if not prompt.strip():
        return

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    person = (
        git(["config", "user.name"], project_dir)
        or os.environ.get("USERNAME")
        or os.environ.get("USER")
        or "ukjent"
    )
    branch = git(["rev-parse", "--abbrev-ref", "HEAD"], project_dir) or "-"
    session = (data.get("session_id") or "-")[:8]

    now = datetime.now().astimezone()
    dato = now.strftime("%Y-%m-%d")
    klokke = now.strftime("%H:%M:%S")
    sone = now.strftime("%z")
    sone = f"{sone[:3]}:{sone[3:]}" if sone else ""

    log_dir = os.path.join(project_dir, "logg", "prompts")
    os.makedirs(log_dir, exist_ok=True)
    filename = re.sub(r"[^A-Za-z0-9._-]+", "-", person).strip("-") or "ukjent"
    path = os.path.join(log_dir, f"{filename}.md")

    entry = []
    if not os.path.exists(path):
        entry.append(f"# Promptlogg – {person}\n\n")
        entry.append(
            "Automatisk generert av `.claude/hooks/log_prompt.py`. "
            "Se `logg/README.md` for format.\n\n"
        )
    fence = fence_for(prompt)
    entry.append(f"## {dato} {klokke}\n\n")
    entry.append("| Felt | Verdi |\n|---|---|\n")
    entry.append(f"| Dato | {dato} |\n")
    entry.append(f"| Klokkeslett | {klokke} (UTC{sone}) |\n")
    entry.append(f"| Person | {person} |\n")
    entry.append(f"| Branch | `{branch}` |\n")
    entry.append(f"| Økt-ID | `{session}` |\n")
    entry.append("| Verktøy | Claude Code |\n\n")
    entry.append(f"{fence}text\n{prompt.rstrip()}\n{fence}\n\n---\n\n")

    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write("".join(entry))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
