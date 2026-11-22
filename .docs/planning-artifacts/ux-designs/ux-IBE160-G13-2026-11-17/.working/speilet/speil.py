# «Speilet»: byggeklosser for alle skjermene (grafisk illustrasjon, speilselfie).
# Et høyt speil står lent mot veggen på rommet ditt. Året henger som en fotosnor over speilet.
# Bare gule post-it-lapper (det som er låst). Mobil, trivsel og penger er klistremerker på speilrammen.
# Hovedhandlinger er korallfargede klistremerker. Kontoskjermer er et ark som legger seg over scenen.
# Tallene er eksempeldata fra PRD-ens brukerreiser, ikke motorberegninger.
import math
from folk_farger import mix, dark, light

FONTS = "family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&amp;family=Kalam:wght@400;700"
SANS = "'Bricolage Grotesque', sans-serif"
HAND = "'Kalam', cursive"

BASE = {"wall": "#C7D5C0", "wall_lit": "#DCE6D2", "wall_mir": "#A9BBA3", "sky": "#DCEBF2", "floor": "#C99A6B", "floor_mir": "#AD8459",
        "frame": "#1C1C20", "base": "#EEF0E8", "ink": "#1A1C2A", "ink2": "#454656", "note": "#FFE27A", "paper": "#F6F3EC",
        "skin": "#E6B796", "case": "#FF6F59", "shoe": "#FAFAF7", "box": "#C4935F", "press": "#A3122A", "plus": "#1E6B45"}
C = dict(BASE)

# lyset følger årstiden: vegg, gjenskinn, vindu
SEASONS = {
    "vinter": dict(wall="#B8C4BC", wall_lit="#C8D2CA", wall_mir="#97A69D", sky="#8EA3C9", snow=True),
    "vår": dict(),
    "sommer": dict(wall="#CFDDBE", wall_lit="#E6EED8", wall_mir="#B3C59F", sky="#9FD3F2"),
    "høst": dict(wall="#C9CDB4", wall_lit="#D9DCC6", wall_mir="#ACB295", sky="#E8B27A"),
}
MONTHS = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]
ACTIVE = {0, 3, 6, 9}
PHOTO = ["#DCE6F2", "#C9D6E6", "#B9CBB0", "#9DBF8A", "#B6D77A", "#7FC0E0", "#62AEE0", "#E9C46A", "#D9A05B", "#C9783F", "#8D8FA6", "#AFC3DD"]


def season_of(m):
    return "vinter" if m in (0, 1, 10, 11) else "vår" if m in (2, 3, 4) else "sommer" if m in (5, 6, 7) else "høst"


def set_month(m):
    C.clear()
    C.update(BASE)
    C.update({k: v for k, v in SEASONS[season_of(m)].items()})
    C["month"] = m


LOOKS = {
    "markus": dict(skin="#E6B796", hair="#3A2A20", style="kort", hood="#2B4CC4", pants="#E4D6BC", build="m"),
    "amina": dict(skin="#8A5A3F", hair="#1B1412", style="fletter", hood="#D99A2B", pants="#2B2F45", build="f"),
    "jonas": dict(skin="#F0CFB6", hair="#C9A060", style="bolget", hood="#2E7D6B", pants="#E4D6BC", build="m"),
    "sara": dict(skin="#EEC3A4", hair="#7A3A22", style="lang", hood="#8E6CC9", pants="#3E5C8A", build="f"),
    "ali": dict(skin="#B07A56", hair="#16110F", style="krus", hood="#25292E", pants="#C9B79A", build="m"),
    "linh": dict(skin="#E2BC96", hair="#14100E", style="knute", hood="#C8453A", pants="#2B2F45", build="f"),
}

# speilet: lent mot veggen, litt smalere i toppen
ML, MR, MT, MB = 44, 300, 150, 772
TL, TR = 54, 290
F = 9


def T(x, y, s, size, fill=None, w=600, anchor="start", font="s", extra=""):
    fam = SANS if font == "s" else HAND
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{w}" fill="{fill or C["ink"]}" text-anchor="{anchor}" {extra}>{s}</text>'


def glass_poly():
    return f"{TL+F},{MT+F} {TR-F},{MT+F} {MR-F},{MB-F} {ML+F},{MB-F}"


def page(title, desc, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="390" height="844" viewBox="0 0 390 844" role="img" aria-labelledby="t d">
  <title id="t">Speilet: {title}</title>
  <desc id="d">{desc}</desc>
  <defs>
    <style>@import url('https://fonts.googleapis.com/css2?{FONTS}&amp;display=block');</style>
    <clipPath id="glass"><polygon points="{glass_poly()}"/></clipPath>
    <filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="4"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0"/></filter>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="2.5" stdDeviation="2" flood-color="#1A1C2A" flood-opacity=".28"/></filter>
    <filter id="lift" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="-4" stdDeviation="8" flood-color="#1A1C2A" flood-opacity=".25"/></filter>
    <filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="10"/></filter>
  </defs>
  <rect width="390" height="844" fill="{C['wall']}"/>
{body}
  <rect width="390" height="844" filter="url(#grain)" opacity=".18" style="mix-blend-mode:multiply" pointer-events="none"/>
</svg>"""


def status(fill=None):
    c = fill or C["ink"]
    return (T(26, 31, "9:41", 15, c, 700) +
            f'<rect x="330" y="20" width="24" height="12" rx="3.5" fill="none" stroke="{c}" stroke-width="1.4"/><rect x="332.5" y="22.5" width="17" height="7" rx="1.5" fill="{c}"/>')


def home_ind(fill=None):
    return f'<rect x="140" y="831" width="110" height="5" rx="2.5" fill="{fill or C["ink"]}" opacity=".8"/>'


# ------------------------------------------------------------------ rommet du står i
def your_room():
    o = [f'<polygon points="0,150 150,108 150,520 0,600" fill="{C["wall_lit"]}"/>',
         f'<rect x="0" y="742" width="390" height="10" fill="{C["base"]}"/>',
         f'<rect x="0" y="752" width="390" height="92" fill="{C["floor"]}"/>']
    for x in range(-40, 420, 64):
        o.append(f'<path d="M{x} 752 L{x-30} 844" stroke="{dark(C["floor"], .18)}" stroke-width="1.5"/>')
    o.append(f'<polygon points="0,790 120,770 160,844 0,844" fill="{light(C["floor"], .25)}" opacity=".6"/>')
    return "".join(o)


# ------------------------------------------------------------------ rommet bak deg, sett i speilet
def goal_boxes(n, label="31 %", word="LEILIGHET"):
    stack = [(62, 560, 64, 52), (68, 514, 52, 46), (74, 476, 40, 38)]
    o = []
    for x, y, w, h in stack[:n]:
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C["box"]}"/><rect x="{x+w-10}" y="{y}" width="10" height="{h}" fill="{dark(C["box"], .18)}"/>'
                 f'<rect x="{x+w/2-5}" y="{y}" width="10" height="12" fill="{light(C["box"], .45)}"/><path d="M{x} {y+12} H{x+w}" stroke="{dark(C["box"], .3)}" stroke-width="1.5"/>')
    if n and label:
        x, y, w, h = stack[0]
        o.append(T(x + 6, y + 30, word, 9.5, C["ink"], 800, extra='letter-spacing=".5"') + T(x + 6, y + 46, label, 14, C["ink"], 800))
    return "".join(o)


def mirror_room(boxes=2, goal="31 %", helmet=False, extra=""):
    sky = C["sky"]
    o = [f'<rect x="0" y="0" width="390" height="844" fill="{C["wall_mir"]}"/>',
         f'<rect x="96" y="196" width="56" height="96" fill="{sky}"/>']
    if C.get("snow"):
        o.append("".join(f'<circle cx="{98 + (i*23) % 54}" cy="{200 + (i*37) % 88}" r="1.6" fill="#FFFFFF"/>' for i in range(14)))
        o.append(f'<path d="M96 292 V280 Q124 270 152 280 V292 Z" fill="#FFFFFF"/>')
    o.append(f'<path d="M124 196 V292 M96 244 H152" stroke="{C["base"]}" stroke-width="5"/><rect x="92" y="192" width="64" height="104" fill="none" stroke="{C["base"]}" stroke-width="6"/>')
    o.append(f'<polygon points="96,330 156,322 176,560 116,575" fill="{light(C["wall_mir"], .2)}"/>')
    o.append(f'<rect x="232" y="352" width="44" height="60" fill="#F2EEE4"/><circle cx="254" cy="374" r="12" fill="{C["case"]}"/><rect x="240" y="394" width="28" height="4" fill="{C["ink"]}"/>')
    if helmet:
        o.append(f'<circle cx="254" cy="428" r="2.5" fill="{C["ink2"]}"/><path d="M236 452 C236 430 272 430 272 452 V462 H236 Z" fill="#1C1C20"/><rect x="240" y="448" width="28" height="9" fill="#3E7BB6"/>')
    o.append(f'<rect x="0" y="612" width="390" height="240" fill="{C["floor_mir"]}"/><rect x="0" y="606" width="390" height="8" fill="{dark(C["base"], .12)}"/>')
    o.append(f'<polygon points="116,575 176,560 196,700 126,720" fill="{light(C["floor_mir"], .18)}"/>')
    o.append(f'<path d="M232 560 H300 V640 H232 Z" fill="#E9E4F2"/><path d="M232 560 C250 552 280 552 300 560 V574 H232 Z" fill="#CFC6E0"/><rect x="226" y="640" width="80" height="12" fill="{dark("#E9E4F2", .25)}"/>')
    o.append(goal_boxes(boxes, goal))
    o.append(extra)
    return "".join(o)


def mirror(inner, dim=0):
    gp = glass_poly()
    o = [f'<polygon points="{ML-6},{MB+6} {MR+16},{MB+6} {MR+4},{MB-4} {ML+2},{MB-4}" fill="{dark(C["floor"], .35)}" opacity=".5"/>',
         f'<polygon points="{TL},{MT} {TR},{MT} {MR},{MB} {ML},{MB}" fill="{C["frame"]}"/>',
         f'<g clip-path="url(#glass)">{inner}' + (f'<rect width="390" height="844" fill="#14161F" opacity="{dim}"/>' if dim else '') +
         f'<polygon points="{TL+F},{MT+F} {TL+80},{MT+F} {ML+F+10},{MB-F-200} {ML+F},{MB-F-160}" fill="#FFFFFF" opacity=".10"/>'
         f'<polygon points="{TL+110},{MT+F} {TL+130},{MT+F} {ML+F+40},{MB-F-120} {ML+F+30},{MB-F-110}" fill="#FFFFFF" opacity=".08"/></g>',
         f'<polygon points="{gp}" fill="none" stroke="#FFFFFF" stroke-width="1.5" opacity=".5"/>']
    return "".join(o)


# ------------------------------------------------------------------ personen i speilet (grafisk)
def _hair_back(L):
    st, c = L["style"], L["hair"]
    if st in ("lang", "fletter"):
        d = "M-52 60 C-64 150 -66 230 -58 290 L64 290 C70 230 68 150 58 60 Z"
        o = f'<path d="{d}" fill="{c}"/>'
        if st == "fletter":
            o += "".join(f'<path d="M{x} 120 V286" stroke="{light(c, .22)}" stroke-width="2" stroke-dasharray="6 5"/>' for x in range(-50, 60, 11))
        return o
    if st == "bolget":
        return f'<path d="M-54 60 C-62 110 -60 150 -50 176 L56 176 C64 150 64 110 56 60 Z" fill="{c}"/>'
    return ""


def _hair_front(L):
    st, c = L["style"], L["hair"]
    hi = light(c, .25)
    if st == "kort":
        return (f'<path d="M-48 70 C-56 18 -26 -12 6 -10 C42 -8 60 22 52 72 C48 52 42 40 32 34 C16 44 -12 32 -28 42 C-38 48 -44 58 -48 70 Z" fill="{c}"/>'
                f'<path d="M-30 4 C-14 -6 12 -8 28 0 C12 2 -6 6 -22 16 Z" fill="{hi}"/>')
    if st in ("lang", "fletter"):
        return (f'<path d="M-50 84 C-56 20 -24 -12 4 -10 C34 -10 58 18 54 84 C50 56 40 36 20 26 C10 34 -8 30 -22 32 C-36 42 -46 60 -50 84 Z" fill="{c}"/>'
                f'<path d="M4 -10 C0 4 2 18 8 28" stroke="{dark(c, .3)}" stroke-width="3" fill="none"/>')
    if st == "bolget":
        return (f'<path d="M-52 96 C-60 30 -30 -14 6 -12 C44 -12 64 28 56 96 C52 70 50 50 38 40 C26 50 8 36 -6 44 C-22 38 -38 50 -44 64 Z" fill="{c}"/>'
                f'<path d="M-30 8 C-20 0 -10 10 0 4 C10 -2 20 8 30 4" stroke="{hi}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    if st == "krus":
        pts = [(-42, 36), (-34, 10), (-18, -6), (2, -12), (22, -6), (38, 10), (46, 34), (-26, 14), (-6, 0), (14, 2), (30, 18), (-44, 56), (50, 56)]
        return "".join(f'<circle cx="{x}" cy="{y}" r="17" fill="{c if i % 2 else dark(c, .15)}"/>' for i, (x, y) in enumerate(pts))
    if st == "knute":
        return (f'<circle cx="4" cy="-22" r="22" fill="{c}"/><path d="M-48 70 C-54 18 -24 -10 4 -10 C34 -10 58 18 52 70 C48 44 32 28 4 26 C-24 28 -42 44 -48 70 Z" fill="{c}"/>'
                f'<path d="M-6 -30 C2 -38 12 -36 18 -28" stroke="{hi}" stroke-width="3" fill="none"/>')
    return ""


def figure(cx, feet, h, look="markus", mood="smil", pose="selfie", age=16, item=None):
    """Speilbildet. pose: selfie (mobilen foran ansiktet) eller stand (ansiktet synes, mobilen i hånda)."""
    L = LOOKS[look] if isinstance(look, str) else look
    s = h / 1000
    sk, sh = L["skin"], dark(L["skin"], .16)
    hd, hd2 = L["hood"], dark(L["hood"], .28)
    pa, pa2 = L["pants"], dark(L["pants"], .14)
    fx = .9 if L["build"] == "f" else 1.0
    o = [f'<g transform="translate({cx} {feet - 1000*s}) scale({s:.4f})">',
         f'<ellipse cx="6" cy="1000" rx="150" ry="16" fill="{dark(C["floor_mir"], .3)}" opacity=".5"/>',
         f'<g transform="scale({fx} 1)">']
    o.append(f'<path d="M-86 470 L-4 470 L-12 968 L-92 968 C-98 800 -100 640 -86 470 Z" fill="{pa}"/><path d="M4 470 L88 470 C100 640 100 800 94 968 L14 968 Z" fill="{pa}"/>')
    o.append(f'<path d="M40 470 L88 470 C100 640 100 800 94 968 L56 968 C62 800 58 620 40 470 Z" fill="{pa2}"/>')
    o.append(f'<path d="M-4 480 L-10 700" stroke="{pa2}" stroke-width="4"/><path d="M-60 900 C-40 910 -26 908 -14 900" stroke="{pa2}" stroke-width="4" fill="none"/>')
    for x0, x1 in ((-98, -6), (10, 100)):
        o.append(f'<path d="M{x0} 954 C{x0-6} 972 {x0-4} 990 {x0+8} 996 L{x1+4} 996 C{x1+12} 990 {x1+12} 970 {x1+2} 954 Z" fill="{C["shoe"]}"/>'
                 f'<rect x="{x0-4}" y="986" width="{x1-x0+16}" height="12" rx="5" fill="{dark(C["shoe"], .2)}"/>')
    o.append(f'<path d="M-90 168 C-66 148 -28 144 0 148 C28 144 66 148 90 168 C106 210 110 320 104 440 C104 466 100 482 92 494 L-92 494 C-100 482 -104 466 -104 440 C-110 320 -106 210 -90 168 Z" fill="{hd}"/>')
    o.append(f'<path d="M30 150 C60 150 80 156 90 168 C106 210 110 320 104 440 C104 466 100 482 92 494 L44 494 C64 420 62 260 30 150 Z" fill="{hd2}"/>')
    o.append(f'<rect x="-94" y="470" width="190" height="26" rx="6" fill="{hd2}"/><path d="M-52 372 L52 372 L60 452 L-60 452 Z" fill="{hd2}" opacity=".55"/>')
    o.append(f'<path d="M-44 150 C-40 196 40 196 44 150 C30 134 -30 134 -44 150 Z" fill="{hd2}"/>')
    o.append('</g>')
    hg = '<g transform="translate(0 140) scale(1.2) translate(0 -140)">'
    o.append(hg + _hair_back(L) + '</g>')
    o.append(hg)
    o.append(f'<rect x="-17" y="118" width="34" height="44" fill="{sh}"/><ellipse cx="2" cy="76" rx="46" ry="60" fill="{sk}"/>')
    o.append(f'<path d="M24 24 C48 40 52 90 40 118 C30 130 18 136 4 136 C30 110 36 60 24 24 Z" fill="{sh}"/>')
    if L["style"] not in ("lang", "fletter"):
        o.append(f'<ellipse cx="47" cy="84" rx="8" ry="13" fill="{sh}"/>')
    if age >= 19 and L["build"] == "m":
        o.append(f'<path d="M-30 100 C-24 132 28 132 34 100 C30 124 -24 124 -30 100 Z" fill="{L["hair"]}" opacity=".35"/>')
    o.append(_hair_front(L))
    mouths = {"smil": "M-8 108 C0 118 14 118 22 108", "noytral": "M-6 112 C2 114 12 114 20 112", "sliten": "M-6 116 C2 109 12 109 20 116", "tenker": "M-2 112 C6 110 14 112 20 109"}
    if pose == "selfie":
        o.append(f'<ellipse cx="26" cy="72" rx="4" ry="5" fill="{C["ink"]}"/><path d="M18 58 C24 54 32 55 38 59" stroke="{L["hair"]}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    else:
        lid = 2 if mood == "sliten" else 0
        for ex in (-18, 22):
            o.append(f'<ellipse cx="{ex}" cy="{72+lid/2}" rx="4.5" ry="{5.5-lid}" fill="{C["ink"]}"/>')
            tilt = {"tenker": 4 if ex < 0 else -2, "sliten": 3}.get(mood, 0)
            o.append(f'<path d="M{ex-10} {58+tilt} C{ex-4} {54+tilt} {ex+4} {54} {ex+10} {58}" stroke="{L["hair"]}" stroke-width="4" fill="none" stroke-linecap="round"/>')
        o.append(f'<path d="M4 76 C2 86 0 92 6 94" stroke="{sh}" stroke-width="3" fill="none" stroke-linecap="round"/>')
        if mood == "glad":
            o.append(f'<path d="M-12 104 C-4 126 18 126 26 104 Z" fill="{C["ink"]}"/><path d="M-8 106 C0 112 14 112 22 106 L20 110 C12 114 2 114 -6 110 Z" fill="#FFFFFF"/>')
        else:
            o.append(f'<path d="{mouths[mood]}" stroke="{C["ink"]}" stroke-width="4" fill="none" stroke-linecap="round"/>')
        o.append(f'<ellipse cx="-26" cy="96" rx="9" ry="5" fill="{C["case"]}" opacity=".18"/><ellipse cx="32" cy="96" rx="9" ry="5" fill="{C["case"]}" opacity=".18"/>')
    o.append('</g>')
    if pose == "selfie":
        o.append(f'<path d="M-90 170 C-112 210 -124 270 -122 320 C-120 344 -108 356 -88 352 C-60 300 -36 200 -24 126 L-60 112 C-70 160 -86 220 -96 270 C-96 240 -92 200 -78 180 Z" fill="{hd}" stroke="{dark(hd, .5)}" stroke-width="3.5" stroke-linejoin="round"/>')
        o.append(f'<path d="M-122 320 C-120 344 -108 356 -88 352 C-84 344 -80 336 -78 328 C-96 330 -112 326 -122 320 Z" fill="{hd2}"/>')
        o.append(hg + f'<g transform="rotate(-6 -30 76)"><rect x="-62" y="18" width="60" height="112" rx="12" fill="{C["case"]}"/>'
                 f'<rect x="-56" y="24" width="28" height="31" rx="8" fill="{dark(C["case"], .3)}"/>'
                 f'<circle cx="-48" cy="32" r="5" fill="{C["ink"]}"/><circle cx="-36" cy="32" r="5" fill="{C["ink"]}"/><circle cx="-48" cy="46" r="5" fill="{C["ink"]}"/><circle cx="-36" cy="46" r="2.4" fill="#FFF6D6"/>'
                 + "".join(f'<rect x="-70" y="{y}" width="30" height="13" rx="6.5" fill="{sk}"/><path d="M-48 {y+2} v9" stroke="{sh}" stroke-width="2"/>' for y in (78, 93, 108))
                 + f'<path d="M-66 120 C-70 134 -64 148 -50 150 C-36 150 -28 140 -30 128 Z" fill="{sk}"/></g></g>')
        o.append(f'<path d="M86 168 C110 200 122 260 120 320 C118 360 98 400 64 430 L44 410 C70 380 86 352 88 320 C90 280 84 230 76 200 Z" fill="{hd2}"/>')
        o.append(f'<path d="M64 430 L44 410 C38 418 36 428 42 436 Z" fill="{dark(hd, .45)}"/>')
    else:
        for sg in (-1, 1):
            x = 90 * sg * fx
            col = hd if sg < 0 else hd2
            o.append(f'<path d="M{x} 168 C{x+sg*22} 210 {x+sg*28} 300 {x+sg*24} 400 C{x+sg*22} 430 {x+sg*18} 450 {x+sg*14} 466 L{x-sg*8} 462 C{x-sg*6} 430 {x-sg*4} 400 {x-sg*4} 360 C{x-sg*4} 300 {x-sg*6} 240 {x-sg*12} 200 Z" fill="{col}" stroke="{dark(hd, .5)}" stroke-width="3" stroke-linejoin="round"/>')
            o.append(f'<ellipse cx="{x+sg*4}" cy="478" rx="15" ry="19" fill="{sk}"/>')
        if item == "konvolutt":
            o.append(f'<g transform="rotate(-10 104 470)"><rect x="80" y="440" width="64" height="44" rx="3" fill="#FFFFFF" stroke="{C["ink2"]}" stroke-width="2"/><path d="M80 442 L112 466 L144 442" stroke="{C["ink2"]}" stroke-width="2" fill="none"/><rect x="92" y="424" width="40" height="24" fill="#B7D4A8" stroke="{C["ink2"]}" stroke-width="1.5"/></g>')
        else:
            o.append(f'<rect x="{94*fx}" y="452" width="22" height="40" rx="5" fill="{C["case"]}" transform="rotate(8 {104*fx} 470)"/>')
    o.append('</g>')
    return "".join(o)


def flash(x, y):
    rays = "".join(f'<path d="M{x} {y} L{x + (22 if i % 2 else 14)*math.cos(a):.1f} {y + (22 if i % 2 else 14)*math.sin(a):.1f}" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" opacity=".85"/>'
                   for i, a in enumerate([k * 0.785 for k in range(8)]))
    return f'<circle cx="{x}" cy="{y}" r="14" fill="#FFFFFF" opacity=".4"/><circle cx="{x}" cy="{y}" r="5" fill="#FFFFFF"/>' + rays


# ------------------------------------------------------------------ tidslinja: fotosnor
def star(x, y, r, fill, stroke=None):
    pts = " ".join(f"{x + (r if k % 2 == 0 else r*.45) * math.cos(-math.pi/2 + k*math.pi/5):.1f},{y + (r if k % 2 == 0 else r*.45) * math.sin(-math.pi/2 + k*math.pi/5):.1f}" for k in range(10))
    return f'<polygon points="{pts}" fill="{fill}"' + (f' stroke="{stroke}" stroke-width="1.2"' if stroke else '') + '/>'


def trip_photo(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#C9D6E8"/><path d="M{x} {y+h} V{y+h*.65} Q{x+w/2} {y+h*.5} {x+w} {y+h*.62} V{y+h} Z" fill="#FFFFFF"/>'
            f'<path d="M{x+w*.15} {y+h*.7} V{y+h*.42} L{x+w*.4} {y+h*.25} L{x+w*.65} {y+h*.42} V{y+h*.7} Z" fill="#8C4A3A"/>'
            + "".join(f'<circle cx="{x+w*(.72+i*.08):.1f}" cy="{y+h*.62:.1f}" r="{w*.04:.1f}" fill="{c}"/>' for i, c in enumerate(["#2B4CC4", "#D99A2B", "#2E7D6B"])))


def timeline(cur, year, photos_upto=None, special=None, y0=66, label=True, compact=False):
    """Fotosnor januar-desember. photos_upto: siste måned med bilde (standard cur-1). special: {måned: 'trip'}."""
    special = special or {}
    upto = cur - 1 if photos_upto is None else photos_upto
    o = [T(14, y0 - 12, f"År {year} av 5", 15, C["ink"], 800)] if label else []
    y_at = lambda x: y0 + 16 * (1 - ((x - 195) / 190) ** 2)
    o.append(f'<path d="M4 {y0} Q195 {y0+32} 386 {y0}" stroke="{C["ink2"]}" stroke-width="1.6" fill="none"/>')
    for i in range(12):
        x = 26 + i * 30.7
        y = y_at(x)
        big = i == cur
        w, h = (36, 46) if big else (22, 28)
        rot = (-5, 3, -2, 4, -3, 2)[i % 6] if not big else 0
        g = [f'<g transform="rotate({rot} {x} {y})">']
        if i <= upto or big:
            g.append(f'<rect x="{x-w/2}" y="{y+4}" width="{w}" height="{h}" fill="#FFFFFF" stroke="{C["ink2"]}" stroke-width="1"/>')
            if special.get(i) == "trip":
                g.append(trip_photo(x - w/2 + 2.5, y + 6.5, w - 5, h - 9))
            else:
                g.append(f'<rect x="{x-w/2+2.5}" y="{y+6.5}" width="{w-5}" height="{h-9}" fill="{PHOTO[i]}"/>')
                g.append(f'<path d="M{x-w/2+2.5} {y+h-2.5} L{x-w/2+2.5} {y+h-9} Q{x} {y+h-15} {x+w/2-2.5} {y+h-8} V{y+h-2.5} Z" fill="{dark(PHOTO[i], .25)}"/>')
                if big and i > upto:
                    g.append(f'<rect x="{x-5}" y="{y+16}" width="10" height="16" rx="3" fill="#2B4CC4"/><circle cx="{x}" cy="{y+14}" r="4" fill="#E6B796"/>')
        else:
            g.append(f'<rect x="{x-w/2}" y="{y+4}" width="{w}" height="{h}" fill="{C["paper"]}" stroke="{C["ink2"]}" stroke-width="1" stroke-dasharray="3 2"/>')
        g.append(f'<rect x="{x-2.5}" y="{y-3}" width="5" height="11" rx="1" fill="#B8865A"/>')
        if i in ACTIVE:
            g.append(star(x + w/2 - 3, y + 8, 5.5, C["note"] if i <= max(cur, upto) else C["paper"], C["ink2"]))
        g.append('</g>')
        o.append("".join(g))
        if not compact:
            anc, lx = ("start", 4) if big and i == 0 else (("end", 386) if big and i == 11 else ("middle", x))
            o.append(T(lx, y + h + (19 if big else 18), MONTHS[i] if big else MONTHS[i][0], 12 if not big else 15, C["ink"] if i <= max(cur, upto) else C["ink2"], 800 if big else 600, anc))
    if 0 <= cur < 12:
        xc = 26 + cur * 30.7
        o.append(f'<ellipse cx="{xc}" cy="{y_at(xc)+27}" rx="26" ry="29" fill="none" stroke="{C["case"]}" stroke-width="3" transform="rotate(-6 {xc} {y_at(xc)+27})"/>')
        o.append(f'<ellipse cx="{xc}" cy="{y_at(xc)+27}" rx="27.5" ry="30.5" fill="none" stroke="{C["ink"]}" stroke-width="1" opacity=".6" transform="rotate(-6 {xc} {y_at(xc)+27})"/>')
    return "".join(o)


# ------------------------------------------------------------------ lapper, merknader, klistremerker
def tape(x, y, rot=0, w=30):
    return f'<rect x="{x-w/2}" y="{y-6}" width="{w}" height="12" fill="#F4EEDC" opacity=".85" transform="rotate({rot} {x} {y})"/>'


def note(x, y, w, h, rot, inner, label=None):
    return (f'<g transform="translate({x} {y}) rotate({rot} {w/2} {h/2})" filter="url(#soft)"' + (f' aria-label="{label}"' if label else '') + '>'
            f'<rect width="{w}" height="{h}" fill="{C["note"]}" stroke="{C["ink2"]}" stroke-width="1.5"/>{inner}</g>' + tape(x + w / 2, y + 1, rot, min(30, w * .45)))


LOCK = '<rect x="0" y="6" width="12" height="10" rx="2"/><path d="M2.5 6 V3.5 a3.5 3.5 0 0 1 7 0 V6" fill="none" stroke-width="1.8"/>'
CAR = '<path d="M2 34 L6 24 Q8 17 16 17 H34 Q41 17 44 24 L48 34 Z"/><circle cx="13" cy="36" r="4.5"/><circle cx="38" cy="36" r="4.5"/>'
CARD = '<rect x="2" y="12" width="46" height="30" rx="4"/><path d="M2 21 H48"/><path d="M8 34 H22"/>'
MOPED = '<circle cx="9" cy="36" r="6.5"/><circle cx="42" cy="36" r="6.5"/><path d="M9 36 L20 21 H31 L42 36 M28 21 L33 10 H40"/>'
JOBB = '<rect x="6" y="14" width="38" height="28" rx="3"/><path d="M18 14 V8 H32 V14 M6 26 H44"/>'


def locked(x, y, rot, title, age, icon):
    inner = (f'<g transform="translate(9 2)" fill="none" stroke="{C["ink2"]}" stroke-width="2" stroke-dasharray="4 3" stroke-linecap="round">{icon}</g>'
             + T(8, 60, title, 13.5, C["ink"], 700, font="k") + T(8, 76, f"fra {age} år", 13, C["ink2"], 700, font="k")
             + f'<g transform="translate(66 6)" fill="{C["ink2"]}" stroke="{C["ink2"]}">{LOCK}</g>')
    return note(x, y, 84, 84, rot, inner, label=f"{title}: låst, åpnes når du blir {age} år")


def callout(x, y, word, value, arrow="", size=15, anchor="start", strong=False, fill=None):
    c = fill or C["ink"]
    o = [f'<path d="{arrow}" stroke="{c}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' if arrow else "",
         T(x, y, word, size + (3 if strong else 0), c, 700, anchor, font="k")]
    if value:
        o.append(T(x, y + size + 3, value, size - 1 + (2 if strong else 0), c, 800, anchor))
    return "".join(o)


def marker(x, y, s, size, w=700, anchor="start", fill=None):
    return T(x, y, s, size, fill or C["ink"], w, anchor, font="k")


ICONS = {
    "mobil": lambda: f'<path d="M10 8 H30 a4 4 0 0 1 4 4 V24 a4 4 0 0 1 -4 4 H18 L12 33 V28 H10 a4 4 0 0 1 -4 -4 V12 a4 4 0 0 1 4 -4 Z" fill="#2B4CC4"/><circle cx="32" cy="9" r="6" fill="{C["case"]}" stroke="#FFFFFF" stroke-width="1.5"/>',
    "mobil0": lambda: f'<path d="M10 8 H30 a4 4 0 0 1 4 4 V24 a4 4 0 0 1 -4 4 H18 L12 33 V28 H10 a4 4 0 0 1 -4 -4 V12 a4 4 0 0 1 4 -4 Z" fill="#2B4CC4"/>',
    "trivsel": lambda: f'<path d="M20 31 C8 23 4 16 7 11 C10 6 17 6 20 12 C23 6 30 6 33 11 C36 16 32 23 20 31 Z" fill="{C["case"]}"/>',
    "penger": lambda: '<rect x="5" y="10" width="30" height="19" rx="3" fill="#2E7D6B"/><circle cx="20" cy="19.5" r="5.5" fill="none" stroke="#FFFFFF" stroke-width="1.6"/>',
    "pil": lambda: f'<path d="M8 20 H30 M22 12 L30 20 L22 28" stroke="{C["ink"]}" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>',
    "pluss": lambda: f'<path d="M20 9 V31 M9 20 H31" stroke="{C["ink"]}" stroke-width="3.2" stroke-linecap="round"/>',
    "lås": lambda: f'<g transform="translate(13 9)" fill="{C["ink2"]}" stroke="{C["ink2"]}">{LOCK}</g>',
    "hvorfor": lambda: f'<circle cx="20" cy="20" r="12" fill="none" stroke="{C["ink"]}" stroke-width="2.6"/>' + T(20, 26, "?", 17, C["ink"], 800, "middle"),
    "kalender": lambda: f'<rect x="8" y="10" width="26" height="22" rx="3" fill="none" stroke="{C["ink"]}" stroke-width="2.4"/><path d="M8 17 H34 M14 7 V13 M28 7 V13" stroke="{C["ink"]}" stroke-width="2.4"/>',
}


def sticker(x, y, w, kind, text, rot=0, label=None, primary=False, sub=None, faded=False):
    """Klistremerke. primary=True gir korall hovedhandling. kind=None gir merke uten ikon."""
    fill = C["case"] if primary else "#FFFFFF"
    hgt = 48 if sub else 40
    icon = f'<g transform="translate(4 {(hgt-40)/2})">{ICONS[kind]()}</g>' if kind else ""
    tx = 46 if kind else 16
    o = (f'<g transform="translate({x} {y}) rotate({rot} {w/2} {hgt/2})" filter="url(#soft)"' + (f' aria-label="{label}"' if label else '') +
         (' opacity=".55"' if faded else '') + '>'
         f'<rect width="{w}" height="{hgt}" rx="{hgt/2}" fill="{fill}" stroke="{C["ink"] if primary else C["ink2"]}" stroke-width="{2 if primary else 1.5}"/>{icon}')
    if sub:
        o += T(tx, 21, text, 14, C["ink"], 800) + T(tx, 38, sub, 12, C["ink"] if primary else C["ink2"], 650)
    else:
        o += T(tx, 26, text, 14.5 if primary else 14, C["ink"], 800)
    return o + '</g>'


def stat_stickers(msgs="2 nye", trivsel="Trivsel 64", penger="18 450 kr", faded=False, y=600):
    return (sticker(248, y, 126, "mobil" if msgs and msgs[0] != "0" else "mobil0", msgs or "Ingen nye", -3, f"Mobil: {msgs}", faded=faded) +
            sticker(246, y + 48, 128, "trivsel", trivsel, 2, trivsel, faded=faded) +
            sticker(248, y + 96, 126, "penger", penger, -2, f"Penger: {penger}", faded=faded))


# ------------------------------------------------------------------ tingene i rommet ditt
def switch(x=328, y=404, glow=True):
    o = f'<circle cx="{x+19}" cy="{y+28}" r="34" fill="{C["note"]}" opacity=".55"/>' if glow else ""
    return o + (f'<rect x="{x}" y="{y}" width="38" height="56" rx="6" fill="{C["base"]}" filter="url(#soft)"/>'
                f'<rect x="{x+11}" y="{y+12}" width="16" height="32" rx="4" fill="#FFFFFF" stroke="{dark(C["base"], .3)}" stroke-width="1.5"/>'
                f'<rect x="{x+13}" y="{y+14}" width="12" height="13" rx="3" fill="{dark(C["base"], .12)}"/>')


def work_shirt(x=346, y=156):
    return (f'<circle cx="{x}" cy="{y}" r="4" fill="{C["ink2"]}"/><path d="M{x} {y+2} q0 10 -2 12" stroke="{C["ink2"]}" stroke-width="2" fill="none"/>'
            f'<path d="M{x-26} {y+22} L{x} {y+12} L{x+26} {y+22}" stroke="{C["ink2"]}" stroke-width="2.5" fill="none"/>'
            f'<path d="M{x-26} {y+22} L{x-38} {y+46} L{x-26} {y+52} L{x-24} {y+128} L{x+24} {y+128} L{x+26} {y+52} L{x+38} {y+46} L{x+26} {y+22} L{x+12} {y+18} Q{x} {y+30} {x-12} {y+18} Z" fill="#2E7D6B"/>'
            f'<rect x="{x+4}" y="{y+40}" width="16" height="10" rx="1.5" fill="#FFFFFF"/>')


def right_wall(job=True, switch_on=True, job_text="8 t/uke"):
    o = []
    if job:
        o.append(work_shirt())
        o.append(callout(346, 316, "Jobb", job_text, "M346 298 V290", 15, "middle"))
    if switch_on:
        o.append(switch())
        o.append(callout(344, 490, "Slå av lyset", "Neste måned", "M344 474 V468", 14, "middle"))
    return "".join(o)


# ------------------------------------------------------------------ hele månedsscenen
def scene(month=3, age=16, year=2, look="markus", mood="smil", pose="selfie", boxes=2, goal="31 %", locks=(("Bil-lappen", 18, CAR), ("Kredittkort", 18, CARD)),
          kveldene="2 av 4 ledige", show_age=True, stats=("2 nye", "Trivsel 64", "18 450 kr"), job=True, switch_on=True, dim=0, special=None,
          photos_upto=None, mirror_extra="", helmet=False, item=None):
    set_month(month)
    o = [your_room(), timeline(month, year, photos_upto, special)]
    inner = mirror_room(boxes, goal, helmet) + mirror_extra + figure(206, 742, 410, look, mood, pose, age, item)
    o.append(mirror(inner, dim))
    if pose == "selfie" and not dim:
        o.append(flash(167, 352))
    pos = [(194, 162, 4), (196, 250, -3)]
    for (title, a, icon), (x, y, r) in zip(locks, pos):
        o.append(locked(x, y, r, title, a, icon))
    if kveldene:
        o.append(callout(68, 190, f"Kveldene i {MONTHS[month].lower()}", kveldene, "M100 172 C104 166 110 162 114 156 M108 159 L114 156 L117 163" if month == 3 else
                         f"M100 172 L{min(max(26 + month * 30.7, 60), 330):.0f} 158", 14))
    if show_age:
        o.append(T(68, 290, "Du", 22, C["ink"], 700, font="k") + T(68, 318, f"{age} år", 26, C["ink"], 800))
        o.append(f'<path d="M104 300 C130 300 158 312 176 334 M166 330 L176 334 L174 323" stroke="{C["ink"]}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    if stats:
        o.append(stat_stickers(*stats))
    o.append(right_wall(job, switch_on))
    return o


# ------------------------------------------------------------------ ark over scenen (konto, meny) og mobilen i hendene
def dim_all(op=.45):
    return f'<rect width="390" height="844" fill="#14161F" opacity="{op}"/>'


def sheet(top, title, sub=None):
    o = [dim_all(), f'<path d="M0 {top+24} Q0 {top} 24 {top} H366 Q390 {top} 390 {top+24} V844 H0 Z" fill="{C["paper"]}" filter="url(#lift)"/>',
         f'<rect x="171" y="{top+10}" width="48" height="5" rx="2.5" fill="{C["ink2"]}" opacity=".5"/>', T(24, top + 56, title, 26, C["ink"], 800)]
    if sub:
        for i, line in enumerate(sub if isinstance(sub, list) else [sub]):
            o.append(T(24, top + 84 + i * 20, line, 14.5, C["ink2"], 600))
    return "".join(o)


def field(x, y, w, label, value="", masked=False, error=None):
    o = [T(x, y, label, 13.5, C["ink"], 700),
         f'<rect x="{x}" y="{y+8}" width="{w}" height="50" rx="10" fill="#FFFFFF" stroke="{C["press"] if error else C["ink2"]}" stroke-width="{2 if error else 1.5}"/>']
    if masked:
        o.append("".join(f'<circle cx="{x+20+i*14}" cy="{y+33}" r="4.5" fill="{C["ink"]}"/>' for i in range(value)))
    elif value:
        o.append(T(x + 16, y + 39, value, 15.5, C["ink"], 500))
    if error:
        o.append(T(x, y + 78, error, 13, C["press"], 700))
    return "".join(o)


def pill(x, y, w, text, primary=True, h=52):
    fill = C["case"] if primary else "#FFFFFF"
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}" stroke="{C["ink"]}" stroke-width="2"/>'
            + T(x + w / 2, y + h / 2 + 6, text, 16, C["ink"], 800, "middle"))


def link(x, y, text, anchor="start"):
    return T(x, y, text, 14.5, C["ink"], 700, anchor, extra='text-decoration="underline"')


def checkbox(x, y, text, checked=False):
    o = f'<rect x="{x}" y="{y}" width="24" height="24" rx="6" fill="{C["case"] if checked else "#FFFFFF"}" stroke="{C["ink"]}" stroke-width="2"/>'
    if checked:
        o += f'<path d="M{x+6} {y+12} l4 4 8 -9" stroke="{C["ink"]}" stroke-width="2.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    return o + text


def phone(app_title, body, back=None, dark_mode=False):
    """Mobilen holdt i hendene, over scenen."""
    scr = "#FFFFFF"
    o = [dim_all(.5),
         f'<rect x="34" y="62" width="322" height="760" rx="44" fill="#121318" filter="url(#lift)"/>',
         f'<rect x="44" y="72" width="302" height="740" rx="36" fill="{scr}"/>',
         f'<rect x="160" y="82" width="70" height="20" rx="10" fill="#121318"/>',
         T(64, 98, "9:41", 13, C["ink"], 700),
         f'<path d="M44 160 H346" stroke="#E2E2E8"/>']
    if back:
        o.append(f'<path d="M68 128 l-8 8 8 8" stroke="{C["ink"]}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' + T(78, 141, back, 15, C["ink"], 600))
        o.append(T(195, 141, app_title, 17, C["ink"], 800, "middle"))
    else:
        o.append(T(64, 146, app_title, 26, C["ink"], 800))
    o.append(body)
    o.append(f'<rect x="140" y="796" width="110" height="5" rx="2.5" fill="{C["ink"]}"/>')
    # hendene som holder mobilen
    sk = "#E6B796"
    o.append(f'<path d="M0 700 C22 690 40 700 46 720 C52 744 44 790 30 844 H0 Z" fill="{sk}"/><path d="M36 712 C50 704 60 712 58 728 C56 744 46 752 36 752 Z" fill="{dark(sk, .12)}"/>')
    o.append(f'<path d="M390 690 C368 680 350 690 344 712 C338 740 346 790 360 844 H390 Z" fill="{sk}"/><path d="M352 704 C340 698 330 708 332 724 C334 740 344 746 352 746 Z" fill="{dark(sk, .12)}"/>')
    o.append('<path d="M0 760 C20 770 30 800 26 844 H0 Z" fill="#2B4CC4"/><path d="M390 750 C370 762 360 800 364 844 H390 Z" fill="#2B4CC4"/>')
    return "".join(o)


def banner(sender, text, icon_col="#2E7D6B", y=54, initial=None):
    return (f'<g filter="url(#lift)"><rect x="12" y="{y}" width="366" height="84" rx="20" fill="#FBFBFD"/></g>'
            f'<rect x="26" y="{y+16}" width="36" height="36" rx="9" fill="{icon_col}"/>' + T(44, y + 41, initial or sender[0], 18, "#FFFFFF", 800, "middle") +
            T(74, y + 32, sender, 15, C["ink"], 800) + T(364, y + 32, "nå", 13, "#5A5E6B", 600, "end") +
            T(74, y + 54, text[0], 14, C["ink"], 500) + (T(74, y + 72, text[1], 14, C["ink"], 500) if len(text) > 1 else ""))
