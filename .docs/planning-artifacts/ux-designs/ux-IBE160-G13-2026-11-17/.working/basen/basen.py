# «Basen»: byggeklosser i blankt mobilspill-uttrykk (første utkast var rommet sett forfra; erstattet av basecamp i leir.py og alle.py).
# PRD: rommet viser eiendelene dine (FR-34, maks 6 lag), nivået er alderen, opplåsing bare etter alder (FR-18),
# ingen venting i sanntid, ingen nye rom, ingen lotteri. Stasjonene er spillområdene: kveldene (månedsplan),
# mobil, jobb og penger, pluss livsmålet. Tallene er eksempeldata, ikke motorberegninger. Kjør: python basen.py
import os, math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "skjermer")
os.makedirs(OUT, exist_ok=True)
FONTS = "family=Lilita+One&amp;family=Onest:wght@500;600;700;800"
GAME = "'Lilita One', sans-serif"
SANS = "'Onest', sans-serif"
C = {"hud": "#1B2340", "hud2": "#26315A", "ink": "#151A2E", "white": "#FFFFFF", "gold": "#FFC83D", "gold2": "#E59A12",
     "green": "#1C8441", "green2": "#0F5A2A", "red": "#C7353A", "wall": "#8CC3CF", "wall2": "#6FA9B8", "floor": "#D49A62", "floor2": "#B57A45",
     "frame": "#4A3426", "teal": "#2E7D6B", "hood": "#3557D6", "skin": "#E9B892", "hair": "#3A2A20"}


def _rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def mix(a, b, t):
    a, b = _rgb(a), _rgb(b)
    return "#" + "".join(f"{int(round(a[i] + (b[i] - a[i]) * t)):02X}" for i in range(3))


def T(x, y, s, size, fill, w=700, anchor="start", font="s", extra=""):
    fam = SANS if font == "s" else GAME
    return f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'


def G(x, y, s, size, fill="#FFFFFF", anchor="start", stroke=None):
    """Spilltekst med mørk kant, som i mobilspill."""
    st = f'stroke="{stroke}" stroke-width="{size*.16:.1f}" paint-order="stroke" stroke-linejoin="round"' if stroke else ""
    return T(x, y, s, size, fill, 400, anchor, "g", st)


_gid = [0]


def grad(c1, c2, vertical=True):
    _gid[0] += 1
    gid = f"g{_gid[0]}"
    d = 'x1="0" y1="0" x2="0" y2="1"' if vertical else 'x1="0" y1="0" x2="1" y2="0"'
    DEFS.append(f'<linearGradient id="{gid}" {d}><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')
    return f"url(#{gid})"


DEFS = []


def gloss(x, y, w, h, r, col, depth=5, stroke=None):
    """Blank knapp/flate: mørkere bunn (3D), lysere topp og et høylys."""
    return (f'<rect x="{x}" y="{y+depth}" width="{w}" height="{h}" rx="{r}" fill="{mix(col, "#000000", .35)}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{grad(mix(col, "#FFFFFF", .22), col)}"' + (f' stroke="{stroke}" stroke-width="2"' if stroke else "") + '/>'
            f'<rect x="{x+6}" y="{y+4}" width="{w-12}" height="{max(4, h*.32):.0f}" rx="{max(2, r-4)}" fill="#FFFFFF" opacity=".28"/>')


def page(title, desc, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="390" height="844" viewBox="0 0 390 844" role="img" aria-labelledby="t d">
  <title id="t">Basen: {title}</title>
  <desc id="d">{desc}</desc>
  <defs>
    <style>@import url('https://fonts.googleapis.com/css2?{FONTS}&amp;display=block');</style>
    <filter id="sh" x="-30%" y="-30%" width="160%" height="180%"><feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0B1020" flood-opacity=".35"/></filter>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="8"/></filter>
    {"".join(DEFS)}
  </defs>
  <rect width="390" height="844" fill="{C['hud']}"/>
{body}
</svg>"""


# ------------------------------------------------------------------ toppfeltet: nivå, penger, trivsel og året
def coin(cx, cy, r=13):
    return (f'<circle cx="{cx}" cy="{cy+2}" r="{r}" fill="{C["gold2"]}"/><circle cx="{cx}" cy="{cy}" r="{r}" fill="{grad("#FFE27A", C["gold"])}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*.62:.1f}" fill="none" stroke="{C["gold2"]}" stroke-width="2"/>' + T(cx, cy + 4.5, "kr", r * .62, "#8A5A00", 800, "middle"))


def heart(cx, cy, s=1):
    return (f'<path transform="translate({cx} {cy}) scale({s})" d="M0 11 C-14 2 -15 -9 -7 -11 C-3 -12 -1 -9 0 -6 C1 -9 3 -12 7 -11 C15 -9 14 2 0 11 Z" fill="{grad("#FF8A8E", C["red"])}"/>'
            f'<ellipse cx="{cx-5*s}" cy="{cy-5*s}" rx="{3*s}" ry="{2*s}" fill="#FFFFFF" opacity=".55"/>')


def pill(x, y, w, icon, text):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="17" fill="{C["hud2"]}" stroke="#3A4778" stroke-width="2"/>' + icon + G(x + w - 12, y + 24, text, 18, "#FFFFFF", "end", "#0B1020"))


def hud(age=16, year=2, month=3, money="18 450 kr", trivsel="64"):
    o = [f'<rect x="0" y="0" width="390" height="156" fill="{C["hud"]}"/>',
         T(26, 31, "9:41", 15, "#FFFFFF", 700) + '<rect x="330" y="20" width="24" height="12" rx="3.5" fill="none" stroke="#FFFFFF" stroke-width="1.4"/><rect x="332.5" y="22.5" width="17" height="7" rx="1.5" fill="#FFFFFF"/>']
    # nivåskjold = alder
    o.append(f'<path d="M38 50 L62 56 V78 C62 92 50 100 38 104 C26 100 14 92 14 78 V56 Z" fill="{mix(C["gold2"], "#000000", .3)}" transform="translate(0 3)"/>'
             f'<path d="M38 50 L62 56 V78 C62 92 50 100 38 104 C26 100 14 92 14 78 V56 Z" fill="{grad("#FFE27A", C["gold"])}" stroke="#8A5A00" stroke-width="2"/>'
             + G(38, 86, str(age), 24, "#FFFFFF", "middle", "#8A5A00"))
    o.append(G(72, 72, f"Du, {age} år", 20, "#FFFFFF", "start", "#0B1020") + T(72, 94, f"Nivå {age} · År {year} av 5", 13, "#C9D2F2", 700))
    o.append(pill(234, 52, 140, coin(254, 69), money))
    o.append(pill(282, 92, 92, heart(302, 109, .95), trivsel))
    # årsbanen: tolv måneder
    MON = "JFMAMJJASOND"
    o.append(f'<rect x="14" y="118" width="362" height="28" rx="14" fill="{C["hud2"]}" stroke="#3A4778" stroke-width="2"/>')
    for i in range(12):
        x = 20 + i * 29.6
        if i < month:
            o.append(f'<rect x="{x}" y="123" width="26" height="18" rx="9" fill="{grad("#FFE27A", C["gold"])}"/>' + T(x + 13, 136, MON[i], 11, "#5A3A00", 800, "middle"))
        elif i == month:
            o.append(f'<rect x="{x-2}" y="119" width="30" height="26" rx="13" fill="#FFFFFF" stroke="{C["gold"]}" stroke-width="3"/>' + T(x + 13, 137, MON[i], 13, C["ink"], 800, "middle"))
        else:
            o.append(f'<rect x="{x}" y="123" width="26" height="18" rx="9" fill="none" stroke="#8592C4" stroke-width="1.5"/>' + T(x + 13, 136, MON[i], 11, "#AEB8DE", 700, "middle"))
        if i in (0, 3, 6, 9):
            o.append(f'<circle cx="{x+23}" cy="121" r="4" fill="{C["red"] if i >= month else C["gold2"]}" stroke="{C["hud"]}" stroke-width="1.5"/>')
    o.append(f'<path d="M{20 + month*29.6 + 13} 150 l-6 7 h12 z" fill="#FFFFFF"/>' + G(20 + month * 29.6 + 13, 172, "April", 15, "#FFFFFF", "middle", "#0B1020"))
    return "".join(o)


# ------------------------------------------------------------------ rommet (basen)
RX0, RX1, RY0, RY1 = 14, 376, 180, 640      # utsnittet av rommet


def room_shell():
    o = [f'<rect x="{RX0}" y="{RY0}" width="{RX1-RX0}" height="{RY1-RY0}" rx="18" fill="{C["frame"]}"/>',
         f'<rect x="{RX0+10}" y="{RY0+10}" width="{RX1-RX0-20}" height="{RY1-RY0-20}" rx="10" fill="{grad(C["wall"], C["wall2"])}"/>']
    # gulvet i perspektiv
    o.append(f'<path d="M{RX0+10} {RY1-10} L{RX0+40} 530 H{RX1-40} L{RX1-10} {RY1-10} Z" fill="{grad(C["floor2"], C["floor"])}"/>')
    for i in range(1, 9):
        xb = RX0 + 40 + i * (RX1 - RX0 - 80) / 9
        xf = RX0 + 10 + i * (RX1 - RX0 - 20) / 9
        o.append(f'<path d="M{xb:.0f} 530 L{xf:.0f} {RY1-10}" stroke="{C["floor2"]}" stroke-width="1.5" opacity=".7"/>')
    o.append(f'<path d="M{RX0+10} {RY0+10} L{RX0+40} {RY0+30} V530 L{RX0+10} {RY1-10} Z" fill="{mix(C["wall2"], "#000000", .12)}"/>')
    o.append(f'<path d="M{RX1-10} {RY0+10} L{RX1-40} {RY0+30} V530 L{RX1-10} {RY1-10} Z" fill="{mix(C["wall2"], "#000000", .2)}"/>')
    o.append(f'<rect x="{RX0+40}" y="522" width="{RX1-RX0-80}" height="8" fill="#F4EFE6" opacity=".8"/>')
    return "".join(o)


def window():
    sky = grad("#5D6BB8", "#F2A58A")
    return '<g transform="translate(-22 0) scale(.92 1)">' + (f'<rect x="70" y="222" width="110" height="96" rx="6" fill="{sky}"/>'
            f'<path d="M70 300 L70 282 L92 272 L110 284 L130 268 L152 280 L180 274 V318 H70 Z" fill="#3B4478" opacity=".8"/>'
            + "".join(f'<rect x="{x}" y="{y}" width="5" height="6" fill="#FFD37A"/>' for x, y in [(84, 290), (120, 284), (140, 296), (162, 288)]) +
            f'<rect x="66" y="218" width="118" height="104" rx="8" fill="none" stroke="#F4EFE6" stroke-width="7"/><path d="M125 220 V320 M68 270 H182" stroke="#F4EFE6" stroke-width="5"/>'
            f'<rect x="60" y="322" width="130" height="10" rx="4" fill="#F4EFE6"/>') + '</g>'


def bed():
    return (f'<ellipse cx="110" cy="548" rx="92" ry="12" fill="#0B1020" opacity=".2"/>'
            f'<rect x="30" y="404" width="22" height="140" rx="8" fill="{grad("#8A5A3C", "#6B4128")}"/>'
            f'<rect x="38" y="470" width="160" height="56" rx="14" fill="{grad("#F4EFE6", "#D9D2C6")}"/>'
            f'<rect x="40" y="488" width="158" height="52" rx="14" fill="{grad("#6F7FD9", "#4A5AB8")}"/><rect x="48" y="492" width="140" height="10" rx="5" fill="#FFFFFF" opacity=".25"/>'
            f'<rect x="50" y="456" width="56" height="26" rx="12" fill="{grad("#FFFFFF", "#E2DCD2")}"/>'
            f'<rect x="36" y="538" width="166" height="10" rx="4" fill="#6B4128"/>')


def nightstand_phone():
    return (f'<rect x="206" y="482" width="44" height="58" rx="6" fill="{grad("#B07A4E", "#8A5A3C")}"/><rect x="210" y="500" width="36" height="4" rx="2" fill="#6B4128"/>'
            f'<ellipse cx="228" cy="470" rx="26" ry="14" fill="#9FB4FF" opacity=".45" filter="url(#blur)"/>'
            f'<g transform="rotate(-12 228 470)"><rect x="216" y="452" width="24" height="40" rx="5" fill="#151A2E"/><rect x="219" y="456" width="18" height="32" rx="3" fill="{grad("#8FA6FF", "#4A5AB8")}"/></g>')


def desk():
    return (f'<ellipse cx="300" cy="548" rx="70" ry="10" fill="#0B1020" opacity=".2"/>'
            f'<rect x="246" y="430" width="112" height="14" rx="5" fill="{grad("#C9925E", "#A8723F")}"/>'
            f'<rect x="254" y="444" width="10" height="96" rx="4" fill="#8A5A3C"/><rect x="340" y="444" width="10" height="96" rx="4" fill="#8A5A3C"/>'
            f'<rect x="268" y="398" width="58" height="34" rx="4" fill="#151A2E"/><rect x="272" y="402" width="50" height="26" rx="2" fill="{grad("#BFE9DF", "#7CC9B8")}"/>'
            + "".join(f'<rect x="{276 + (i%4)*11}" y="{406 + (i//4)*9}" width="8" height="6" rx="1.5" fill="{"#FFFFFF" if i in (0,1,4) else "#3E8E7E"}"/>' for i in range(8)) +
            f'<path d="M262 432 H332 L340 438 H254 Z" fill="#2A3150"/>')


def job_stand():
    return (f'<rect x="338" y="300" width="6" height="234" rx="3" fill="#6B4128"/><ellipse cx="341" cy="536" rx="20" ry="5" fill="#6B4128"/>'
            f'<path d="M318 330 L341 318 L364 330 L370 360 L362 364 L362 430 L320 430 L320 364 L312 360 Z" fill="{grad("#3A9C82", C["teal"])}"/>'
            f'<rect x="346" y="346" width="13" height="16" rx="2" fill="#FFFFFF"/><rect x="348" y="349" width="9" height="5" fill="{C["teal"]}"/>')


def safe():
    return (f'<ellipse cx="74" cy="612" rx="44" ry="8" fill="#0B1020" opacity=".25"/>'
            f'<rect x="36" y="556" width="76" height="56" rx="8" fill="#3B4258"/><rect x="36" y="552" width="76" height="56" rx="8" fill="{grad("#7D879E", "#5A6378")}"/>'
            f'<rect x="44" y="560" width="60" height="40" rx="5" fill="none" stroke="#C9D0DE" stroke-width="2"/>'
            f'<circle cx="74" cy="580" r="11" fill="{grad("#E9EDF4", "#AEB6C6")}"/><path d="M74 580 L80 574" stroke="#3B4258" stroke-width="2.5" stroke-linecap="round"/>'
            + coin(104, 552, 9) + coin(92, 548, 9))


def goal_frame(pct=31):
    w = 84
    return '<g transform="translate(-34 -4)">' + (f'<rect x="232" y="226" width="110" height="120" rx="8" fill="{grad("#FFF8EA", "#EFE4CF")}" stroke="#8A5A3C" stroke-width="5"/>'
            f'<path d="M262 284 V262 L287 244 L312 262 V284 Z" fill="#C2674F"/><rect x="281" y="266" width="12" height="18" fill="#6B4128"/>'
            + T(287, 302, "Egen leilighet", 12, C["ink"], 800, "middle") +
            f'<rect x="245" y="312" width="{w}" height="14" rx="7" fill="#E2D8C4" stroke="#8A5A3C" stroke-width="1.5"/><rect x="245" y="312" width="{w*pct/100:.0f}" height="14" rx="7" fill="{grad("#7FE08F", C["green"])}"/>'
            + T(287, 340, f"{pct} % spart", 11.5, C["ink"], 800, "middle")) + '</g>'


def locked_slot(x, y, age, text):
    return (f'<rect x="{x}" y="{y}" width="58" height="58" rx="10" fill="#FFFFFF" opacity=".22" stroke="#FFFFFF" stroke-width="2" stroke-dasharray="6 5"/>'
            f'<g transform="translate({x+20} {y+10})"><rect x="0" y="9" width="18" height="15" rx="3" fill="#FFFFFF"/><path d="M4 9 V6 a5 5 0 0 1 10 0 V9" fill="none" stroke="#FFFFFF" stroke-width="2.6"/></g>'
            + G(x + 29, y + 50, f"Nivå {age}", 12.5, "#FFFFFF", "middle", "#1B2340") + T(x + 29, y + 74, text, 11.5, C["ink"], 800, "middle"))


def avatar(cx, feet, h=176):
    s = h / 176
    sk, hd = C["skin"], C["hood"]
    o = [f'<g transform="translate({cx} {feet}) scale({s})">', '<ellipse cx="0" cy="0" rx="40" ry="8" fill="#0B1020" opacity=".25"/>',
         f'<rect x="-22" y="-80" width="20" height="78" rx="9" fill="{grad("#4A5A7A", "#36435E")}"/><rect x="2" y="-80" width="20" height="78" rx="9" fill="{grad("#41506E", "#2E3A52")}"/>',
         '<rect x="-26" y="-10" width="26" height="12" rx="6" fill="#FFFFFF"/><rect x="0" y="-10" width="26" height="12" rx="6" fill="#F0F0F0"/>',
         f'<path d="M-30 -136 Q-34 -84 -28 -76 H28 Q34 -84 30 -136 Q0 -148 -30 -136 Z" fill="{grad(mix(hd, "#FFFFFF", .2), hd)}"/>',
         f'<path d="M-30 -132 Q-44 -110 -40 -84" stroke="{mix(hd, "#000000", .15)}" stroke-width="13" stroke-linecap="round" fill="none"/>',
         f'<path d="M30 -132 Q46 -116 40 -96 L26 -88" stroke="{mix(hd, "#000000", .25)}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" fill="none"/>',
         f'<circle cx="-40" cy="-80" r="7" fill="{sk}"/><circle cx="24" cy="-88" r="7" fill="{sk}"/>',
         f'<rect x="-14" y="-104" width="28" height="18" rx="5" fill="{mix(hd, "#000000", .2)}"/>',
         f'<path d="M-14 -142 Q0 -132 14 -142" stroke="#F4EFE6" stroke-width="3" fill="none"/><path d="M-6 -138 V-118 M6 -138 V-118" stroke="#F4EFE6" stroke-width="2.4"/>',
         f'<rect x="-7" y="-152" width="14" height="14" fill="{mix(sk, "#000000", .12)}"/>',
         f'<ellipse cx="0" cy="-172" rx="21" ry="24" fill="{grad(mix(sk, "#FFFFFF", .15), sk)}"/>',
         f'<path d="M-22 -174 Q-24 -200 0 -200 Q24 -200 22 -174 Q16 -188 2 -186 Q-12 -190 -22 -174 Z" fill="{C["hair"]}"/><path d="M-12 -194 Q0 -199 12 -194" stroke="#6B4A36" stroke-width="3" fill="none"/>',
         f'<ellipse cx="-8" cy="-171" rx="2.6" ry="3.4" fill="#151A2E"/><ellipse cx="8" cy="-171" rx="2.6" ry="3.4" fill="#151A2E"/>',
         f'<circle cx="-7" cy="-172" r=".9" fill="#FFFFFF"/><circle cx="9" cy="-172" r=".9" fill="#FFFFFF"/>',
         f'<path d="M-6 -160 Q0 -155 6 -160" stroke="#8A3B3B" stroke-width="2.2" fill="none" stroke-linecap="round"/>',
         f'<ellipse cx="-14" cy="-163" rx="4" ry="2.4" fill="#E5484D" opacity=".18"/><ellipse cx="14" cy="-163" rx="4" ry="2.4" fill="#E5484D" opacity=".18"/>', '</g>']
    return "".join(o)


# ------------------------------------------------------------------ stasjonsmerker
def bubble(cx, cy, inner, badge=None, r=22):
    o = [f'<g filter="url(#sh)"><path d="M{cx-r} {cy} a{r} {r} 0 1 1 {2*r} 0 a{r} {r} 0 0 1 {-r*.55:.1f} {r*.84:.1f} l{-r*.45:.1f} {r*.42:.1f} l{-r*.18:.1f} {-r*.5:.1f} a{r} {r} 0 0 1 {-r*.82:.1f} {-r*.76:.1f} z" fill="#FFFFFF"/></g>', inner]
    if badge:
        o.append(f'<circle cx="{cx+r-2}" cy="{cy-r+4}" r="11" fill="{C["red"]}" stroke="#FFFFFF" stroke-width="2.5"/>' + G(cx + r - 2, cy - r + 9.5, badge, 14, "#FFFFFF", "middle"))
    return "".join(o)


def tag(cx, y, text, sub=None):
    w = max(len(text), len(sub or "")) * 7.6 + 22
    h = 38 if sub else 24
    return (f'<rect x="{cx-w/2:.0f}" y="{y}" width="{w:.0f}" height="{h}" rx="{min(12, h/2)}" fill="{C["hud"]}" opacity=".92"/>' + T(cx, y + 17, text, 13, "#FFFFFF", 800, "middle") +
            (T(cx, y + 32, sub, 12, "#C9D2F2", 700, "middle") if sub else ""))


ICON_PLAN = lambda cx, cy: (f'<rect x="{cx-11}" y="{cy-10}" width="22" height="20" rx="4" fill="none" stroke="{C["ink"]}" stroke-width="2.6"/>'
                            f'<path d="M{cx-11} {cy-3} H{cx+11} M{cx-5} {cy-14} V{cy-7} M{cx+5} {cy-14} V{cy-7}" stroke="{C["ink"]}" stroke-width="2.6" stroke-linecap="round"/>')
ICON_MSG = lambda cx, cy: f'<path d="M{cx-12} {cy-9} H{cx+12} a3 3 0 0 1 3 3 V{cy+5} a3 3 0 0 1 -3 3 H{cx-3} L{cx-9} {cy+14} V{cy+8} H{cx-12} a3 3 0 0 1 -3 -3 V{cy-6} a3 3 0 0 1 3 -3 Z" fill="{C["hood"]}"/>'


# ------------------------------------------------------------------ skjermen
def s_maned():
    o = [hud()]
    o.append(room_shell() + window() + goal_frame() + bed() + nightstand_phone() + desk() + job_stand() + safe())
    o.append(f'<circle cx="200" cy="350" r="0"/>')
    o.append(avatar(176, 604, 176))
    # merker over stasjonene
    o.append(bubble(228, 420, ICON_MSG(228, 418), "2") + tag(222, 554, "Mobil", "2 nye"))
    o.append(bubble(298, 362, ICON_PLAN(298, 364), "2") + tag(306, 556, "Kveldene", "2 ledige"))
    o.append(bubble(341, 262, coin(341, 260, 12)) + f'<rect x="306" y="292" width="70" height="24" rx="12" fill="{C["hud"]}"/>' + G(341, 310, "+4 290 kr", 13, C["gold"], "middle") + tag(341, 440, "Jobb", "hent lønn"))
    o.append(tag(74, 616, "Penger"))
    o.append(tag(122, 354, "Livsmål") if False else "")
    # bunnfeltet: neste opplåsing og neste måned
    o.append(f'<rect x="0" y="650" width="390" height="194" fill="{C["hud"]}"/>')
    o.append(f'<rect x="14" y="662" width="362" height="48" rx="14" fill="{C["hud2"]}" stroke="#3A4778" stroke-width="2"/>'
             f'<g transform="translate(28 673)"><rect x="0" y="9" width="18" height="15" rx="3" fill="{C["gold"]}"/><path d="M4 9 V6 a5 5 0 0 1 10 0 V9" fill="none" stroke="{C["gold"]}" stroke-width="2.6"/></g>'
             + T(58, 682, "Neste opplåsing: nivå 18", 13.5, "#FFFFFF", 800) + T(58, 700, "kredittkort, bil-lappen og forbrukslån", 12.5, "#C9D2F2", 700))
    o.append(gloss(14, 724, 362, 70, 22, C["green"], 7) + G(176, 768, "NESTE MÅNED", 26, "#FFFFFF", "middle", C["green2"]) +
             f'<path d="M296 748 l18 12 -18 12 z" fill="#FFFFFF" stroke="{C["green2"]}" stroke-width="3" stroke-linejoin="round"/>')
    o.append(T(195, 822, "Mai venter. Ingen ting må gjøres først.", 12.5, "#C9D2F2", 700, "middle"))
    o.append('<rect x="140" y="831" width="110" height="5" rx="2.5" fill="#FFFFFF" opacity=".85"/>')
    return o


SCREENS = {"08-maned": ("Månedsnavet: april, 16 år",
                        "Rommet ditt som base i et mobilspill, sett forfra. Øverst nivåskjoldet 16, penger 18 450 kr, trivsel 64 og årsbanen med april markert. "
                        "I rommet: senga, nattbordet med mobilen (2 nye), pulten med kveldene (2 ledige), jobbjakka med lønn å hente (+4 290 kr), safen med pengene, "
                        "livsmålet egen leilighet 31 prosent på veggen og en låst plass for kredittkort på nivå 18. Nederst knappen Neste måned.", s_maned)}

if __name__ == "__main__":
    print("basen.py har bare byggeklosser (toppfelt, knapper, ikoner). Skjermene lages av alle.py.")
