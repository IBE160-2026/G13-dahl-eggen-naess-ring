#!/usr/bin/env python3
"""Assemble the 8 LifeMode concepts into one self-contained gallery page."""
import html, json, re, sys
from pathlib import Path

W = Path(sys.argv[1])            # ux workspace
OUT = Path(sys.argv[2])          # output html
CON = W / ".working" / "concepts"

LABELS = {
    "01": "Landingsside", "02": "LifeMode-hub", "03": "Hendelser og månedsplan",
    "03a": "Årstidslinje", "03b": "Månedsplan", "04": "Hendelse", "04a": "Hendelse",
    "04b": "Resultat", "05": "Telefon og meldinger", "06": "Pengevisning", "07": "Alle sider",
}


def md(text: str) -> str:
    """Tiny markdown → HTML: headings, lists, bold/italic/code, paragraphs."""
    out, para, lst = [], [], []

    def inline(s):
        s = html.escape(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        return s

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para.clear()
        if lst:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in lst) + "</ul>"); lst.clear()

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush(); continue
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            flush()
            lvl = min(len(m.group(1)) + 2, 6)
            if len(m.group(1)) == 1:
                continue  # concept title is shown by the page itself
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); continue
        m = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)", line)
        if m:
            if para: flush()
            lst.append(m.group(1)); continue
        if lst and raw.startswith("  "):
            lst[-1] += " " + line.strip(); continue
        if lst: flush()
        para.append(line.strip())
    flush()
    return "\n".join(out)


def svg_size(svg: str):
    m = re.search(r'viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)', svg)
    return (float(m.group(1)), float(m.group(2))) if m else (390.0, 844.0)


def fonts_link(fonts):
    """One link per family: a 400+700 request, plus a plain one that still loads
    if the family has no 700 weight (Google returns 400 for unknown weights)."""
    links = []
    for f in fonts:
        fam = f.replace(" ", "+")
        links.append(f"https://fonts.googleapis.com/css2?family={fam}:wght@400;700&display=swap")
        links.append(f"https://fonts.googleapis.com/css2?family={fam}&display=swap")
    return links


def frame_doc(svg, flink):
    head = "".join(f'<link rel="stylesheet" href="{u}">' for u in flink)
    return (f"<!doctype html><html><head><meta charset='utf-8'>{head}"
            "<style>html,body{margin:0;padding:0;background:transparent;overflow:hidden}"
            "svg{display:block;width:100%;height:auto}</style></head><body>"
            f"{svg}</body></html>")


concepts = []
for d in sorted(CON.glob("c*")):
    meta_p = d / "concept.json"
    if not meta_p.exists():
        continue
    meta = json.loads(meta_p.read_text())
    files = meta.get("files") or sorted(p.name for p in d.glob("*.svg"))
    files = [f for f in files if (d / f).exists()]
    extra = sorted(p.name for p in d.glob("*.svg") if p.name not in files)
    files += extra
    flink = fonts_link(meta.get("fonts", []))
    screens = []
    for f in files:
        svg = (d / f).read_text()
        svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
        svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg)
        w, h = svg_size(svg)
        key = f.split("-")[0]
        label = LABELS.get(key, f.rsplit(".", 1)[0])
        screens.append({"file": f, "w": w, "h": h, "label": label,
                        "doc": frame_doc(svg, flink), "sheet": w > 700})
    md_p = d / "concept.md"
    concepts.append({"id": meta.get("id", d.name), "name": meta.get("name", d.name),
                     "tagline": meta.get("tagline", ""), "fonts": meta.get("fonts", []),
                     "palette": meta.get("palette", [])[:7], "screens": screens,
                     "body": md(md_p.read_text()) if md_p.exists() else ""})

e = html.escape
nav = "".join(
    f'<a class="idx" href="#{c["id"]}"><span class="idx-n">{i+1}</span>'
    f'<span class="idx-sw">' + "".join(f'<i style="background:{e(p["hex"])}"></i>' for p in c["palette"][:5]) +
    f'</span><span class="idx-name">{e(c["name"])}</span></a>'
    for i, c in enumerate(concepts))

sections = []
for i, c in enumerate(concepts):
    phones = [s for s in c["screens"] if not s["sheet"]]
    sheets = [s for s in c["screens"] if s["sheet"]]

    def fig(s, cls):
        return (f'<figure class="{cls}"><div class="frame" style="aspect-ratio:{s["w"]:.0f}/{s["h"]:.0f}">'
                f'<iframe title="{e(c["name"])}: {e(s["label"])}" loading="lazy" tabindex="-1" '
                f'srcdoc="{e(s["doc"], quote=True)}"></iframe>'
                f'<button class="zoom" type="button" aria-label="Forstørr {e(s["label"])}" '
                f'data-w="{s["w"]:.0f}" data-h="{s["h"]:.0f}"></button></div>'
                f'<figcaption><span>{e(s["label"])}</span><code>{e(s["file"])}</code></figcaption></figure>')

    pal = "".join(f'<li><i style="background:{e(p["hex"])}"></i><span>{e(p.get("name",""))}</span>'
                  f'<code>{e(p["hex"])}</code></li>' for p in c["palette"])
    sections.append(f"""
<section class="concept" id="{e(c['id'])}">
  <header class="c-head">
    <p class="c-num">Konsept {i+1} av {len(concepts)}</p>
    <h2>{e(c['name'])}</h2>
    <p class="c-tag">{e(c['tagline'])}</p>
  </header>
  <div class="strip" role="list">{''.join(fig(s, 'phone') for s in phones)}</div>
  <div class="c-body">
    <div class="c-text">{c['body']}</div>
    <aside class="c-meta">
      <h4>Palett</h4><ul class="pal">{pal}</ul>
      <h4>Typografi</h4><p class="fonts">{e(' · '.join(c['fonts']))}</p>
    </aside>
  </div>
  {''.join(fig(s, 'sheet') for s in sheets)}
</section>""")

page = f"""<title>LifeMode designkonsepter</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
/* Layout: a quiet studio wall — index of 8, then one long section per concept with a scrollable phone strip and the full-width sitemap sheet. The concepts carry the colour; the wall stays neutral. */
:root {{
  --bg: #eeede8; --panel: #f7f6f2; --ink: #17181a; --muted: #5b5d63; --line: #d3d1c9; --accent: #2f4cdd;
  --display: 'Bricolage Grotesque', 'Helvetica Neue', Arial, sans-serif;
  --body: 'Instrument Sans', system-ui, sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #141517; --panel: #1c1d20; --ink: #ecebe6; --muted: #a2a3a8; --line: #33343a; --accent: #8fa2ff; color-scheme: dark; }} }}
:root[data-theme="dark"] {{ --bg: #141517; --panel: #1c1d20; --ink: #ecebe6; --muted: #a2a3a8; --line: #33343a; --accent: #8fa2ff; color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ background: var(--bg); color: var(--ink); font: 400 16px/1.55 var(--body);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 0 64px; }}
.wrap {{ max-width: 1280px; margin: 0 auto; }}
.top {{ padding-block: 48px 28px; border-bottom: 1px solid var(--line); }}
.eyebrow {{ font: 500 12px/1 var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 0 0 14px; }}
h1 {{ font: 800 clamp(40px, 7vw, 88px)/.95 var(--display); letter-spacing: -.03em; margin: 0; text-wrap: balance; }}
.lede {{ max-width: 62ch; color: var(--muted); font-size: 17px; margin: 18px 0 0; }}
.index {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; padding-block: 24px; }}
.idx {{ display: grid; grid-template-columns: auto 1fr; grid-template-rows: auto auto; gap: 6px 12px; align-items: center;
  padding: 12px 14px; border: 1px solid var(--line); border-radius: 10px; background: var(--panel); color: inherit; text-decoration: none; }}
.idx:hover, .idx:focus-visible {{ border-color: var(--ink); outline: none; }}
.idx-n {{ grid-row: 1 / 3; font: 800 28px/1 var(--display); width: 1.4em; color: var(--muted); }}
.idx-name {{ font-weight: 600; }}
.idx-sw {{ display: flex; gap: 3px; }}
.idx-sw i {{ width: 18px; height: 10px; border-radius: 2px; box-shadow: inset 0 0 0 1px rgba(0,0,0,.12); }}
.concept {{ padding-block: 56px 24px; border-top: 1px solid var(--line); scroll-margin-top: 12px; }}
.c-num {{ font: 500 12px/1 var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--accent); margin: 0 0 10px; }}
h2 {{ font: 800 clamp(34px, 5vw, 60px)/1 var(--display); letter-spacing: -.025em; margin: 0; }}
.c-tag {{ font-size: 19px; color: var(--muted); margin: 10px 0 0; max-width: 60ch; }}
.c-body {{ display: grid; grid-template-columns: minmax(0, 1fr) 260px; gap: 40px; margin-top: 28px; }}
.c-text {{ min-width: 0; max-width: 72ch; }}
.c-text h3, .c-text h4 {{ font: 700 15px/1.3 var(--body); letter-spacing: .02em; text-transform: uppercase; margin: 22px 0 6px; }}
.c-text p, .c-text ul {{ margin: 0 0 10px; }}
.c-text ul {{ padding-left: 1.1em; }}
.c-text code {{ font: 13px var(--mono); }}
.c-meta h4 {{ font: 500 11px/1 var(--mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); margin: 0 0 10px; }}
.pal {{ list-style: none; padding: 0; margin: 0 0 22px; display: grid; gap: 6px; }}
.pal li {{ display: grid; grid-template-columns: 22px 1fr auto; gap: 8px; align-items: center; font-size: 13px; }}
.pal i {{ width: 22px; height: 22px; border-radius: 4px; box-shadow: inset 0 0 0 1px rgba(0,0,0,.15); }}
.pal code, .fonts {{ font: 12px var(--mono); color: var(--muted); }}
.strip {{ display: flex; gap: 22px; overflow-x: auto; padding: 24px 2px 14px; scroll-snap-type: x proximity; }}
.phone {{ flex: 0 0 min(300px, 78vw); margin: 0; scroll-snap-align: start; }}
.sheet {{ margin: 18px 0 0; }}
.frame {{ position: relative; width: 100%; border-radius: 22px; overflow: hidden; background: var(--panel);
  box-shadow: 0 0 0 1px var(--line), 0 18px 40px -24px rgba(0,0,0,.45); }}
.sheet .frame {{ border-radius: 10px; }}
.frame iframe {{ position: absolute; inset: 0; width: 100%; height: 100%; border: 0; pointer-events: none; }}
.zoom {{ position: absolute; inset: 0; width: 100%; height: 100%; background: transparent; border: 0; cursor: zoom-in; }}
.zoom:focus-visible {{ outline: 3px solid var(--accent); outline-offset: -3px; border-radius: inherit; }}
figcaption {{ display: flex; justify-content: space-between; gap: 8px; margin-top: 10px; font-size: 14px; font-weight: 600; }}
figcaption code {{ font: 11px var(--mono); color: var(--muted); font-weight: 400; align-self: center; }}
dialog {{ border: 0; padding: 0; background: transparent; max-width: 96vw; max-height: 96vh; }}
dialog::backdrop {{ background: rgba(10,10,12,.82); }}
.lb {{ position: relative; }}
.lb iframe {{ display: block; border: 0; border-radius: 14px; background: #fff; }}
.lb-close {{ position: absolute; top: 10px; right: 10px; font: 600 14px var(--body); padding: 10px 14px; min-height: 44px;
  border-radius: 999px; border: 0; background: var(--ink); color: var(--bg); cursor: pointer; }}
.foot {{ margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--line); color: var(--muted); font-size: 14px; }}
@media (max-width: 820px) {{ .c-body {{ grid-template-columns: 1fr; gap: 18px; }} .index {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} }}
</style>
<div class="wrap">
  <header class="top">
    <p class="eyebrow">LifeMode · UX · 11. november 2026</p>
    <h1>Åtte måter å leve fem år på</h1>
    <p class="lede">Åtte designkonsepter for LifeMode, tegnet i parallell fra samme PRD og samme brief. Hvert konsept viser landingsside, spillhuben, hendelser og månedsplan, en hendelse, telefonen og pengevisningen, pluss et oversiktsark over alle de andre sidene. Trykk på en skjerm for å se den større.</p>
  </header>
  <nav class="index" aria-label="Konsepter">{nav}</nav>
  {''.join(sections)}
  <p class="foot">Kilder: PRD «LifeMode» (final, 2026-11-11) og felles brief i <code>.working/brief.md</code>. Skissene er retningsvalg, ikke spesifikasjon — DESIGN.md og EXPERIENCE.md skrives når et konsept er valgt.</p>
</div>
<dialog id="lb" aria-label="Forstørret skjerm"><div class="lb"><iframe id="lbf" title="Forstørret skjerm"></iframe>
<button class="lb-close" type="button" id="lbc">Lukk</button></div></dialog>
<script>
(() => {{
  const dlg = document.getElementById('lb'), f = document.getElementById('lbf');
  document.querySelectorAll('.zoom').forEach(b => b.addEventListener('click', () => {{
    const src = b.previousElementSibling, w = +b.dataset.w, h = +b.dataset.h;
    const s = Math.min((innerWidth * .94) / w, (innerHeight * .92) / h, w > 700 ? 1.6 : 1.25);
    f.style.width = Math.round(w * s) + 'px'; f.style.height = Math.round(h * s) + 'px';
    f.srcdoc = src.getAttribute('srcdoc'); f.title = src.title;
    dlg.showModal();
  }}));
  document.getElementById('lbc').addEventListener('click', () => dlg.close());
  dlg.addEventListener('click', e => {{ if (e.target === dlg) dlg.close(); }});
}})();
</script>
"""
OUT.write_text(page)
print(f"{len(concepts)} concepts, {sum(len(c['screens']) for c in concepts)} screens, {OUT.stat().st_size/1e6:.2f} MB → {OUT}")
