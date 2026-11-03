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


MASK = "********"

# Ord som betyr at verdien etter er hemmelig, f.eks. «passord: abc123» eller «API_KEY=...».
SECRET_WORDS = (
    r"passord(?:et)?|password|passwd|pwd|pass|passphrase|pin(?:-?kode)?"
    r"|hemmelighet|secret|client[_-]?secret|token|access[_-]?token|refresh[_-]?token"
    r"|api[_-]?n(?:ø|o)kkel(?:en)?|api[_-]?key|apikey|access[_-]?key|private[_-]?key"
    r"|service[_-]?role[_-]?key|anon[_-]?key|auth(?:orization)?"
)

# Mønstre der hele treffet er sensitivt.
SECRET_PATTERNS = [
    # Private nøkler (PEM-blokker)
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----",
    # Kjente formater for API-nøkler og tokens
    r"\bsk-(?:ant-)?[A-Za-z0-9_-]{16,}",  # Anthropic / OpenAI
    r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}",  # GitHub
    r"\bgithub_pat_[A-Za-z0-9_]{20,}",
    r"\bgsk_[A-Za-z0-9]{20,}",  # Groq
    r"\bAIza[0-9A-Za-z_-]{30,}",  # Google / Gemini
    r"\bAKIA[0-9A-Z]{16}\b",  # AWS
    r"\bxox[abprs]-[A-Za-z0-9-]{10,}",  # Slack
    r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}",  # JWT (bl.a. Supabase)
    r"\bsb_(?:secret|publishable)_[A-Za-z0-9_-]{16,}",  # Supabase
    # Norsk fødselsnummer (11 siffer, evt. med mellomrom etter fødselsdato)
    r"\b[0-7]\d[01]\d\d{2}\s?\d{5}\b",
    # Betalingskortnummer (13–19 siffer, evt. gruppert)
    r"\b(?:\d{4}[ -]?){3}\d{1,7}\b",
    # E-postadresser
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
]


def redact(text):
    """Bytter ut passord, nøkler og annen sensitiv informasjon med ********."""
    # Brukernavn:passord i URL-er, f.eks. postgres://bruker:hemmelig@vert
    text = re.sub(r"(\b[a-z][a-z0-9+.-]*://[^\s:/@]+:)[^\s@/]+(@)", rf"\1{MASK}\2", text, flags=re.I)
    # «Authorization: Bearer <token>»
    text = re.sub(r"(\bBearer\s+)[A-Za-z0-9._~+/=-]+", rf"\1{MASK}", text, flags=re.I)
    # «passord: x», «API_KEY=x», «passordet mitt er x», «"token": "x"»
    text = re.sub(
        rf"((?:[A-Za-z0-9]+_)*\b(?:{SECRET_WORDS})\b(?:_[A-Za-z0-9]+)*[\"']?"
        r"(?:\s+(?:mitt|min|vårt|v[åa]r|til\s+\S+))?"
        r"\s*(?::|=|\bis\b|\ber\b)\s*[\"']?)"
        r"(?!\*{8})[^\s\"',;]+",
        rf"\1{MASK}",
        text,
        flags=re.I,
    )
    for pattern in SECRET_PATTERNS:
        text = re.sub(pattern, MASK, text, flags=re.S)
    return text


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
    # Regel: sensitiv informasjon skal aldri skrives til loggen.
    prompt = redact(prompt)

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
