# «Basen» (basecamp): byggeklosser for alle skjermene. Blankt mobilspill-uttrykk.
# Leiren er basen din, toppen er livsmålet, stien har én leir per år. Nivå = alder.
# PRD: stasjonene er spillområdene, opplåsing bare etter alder (FR-18), eiendeler i leiren (FR-34),
# ingen venting i sanntid, ingen lotteri, ikke noe skrevet navn (FR-10), motoren bestemmer alle tall.
import math
import basen as B
from basen import C, T, G, mix, grad, gloss, coin, heart, ICON_PLAN, ICON_MSG

MONTHS = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]
ACTIVE = {0, 3, 6, 9}
SEASON = {
    "vinter": dict(sky=("#26306A", "#7E8CC8"), g1=("#F4F7FB", "#D8E1EE"), g2=("#E4EBF5", "#C6D3E6"), sun="#F4F1DA", stars=True),
    "vår": dict(sky=("#6E77C8", "#F3B18E"), g1=("#E9F1E6", "#BFD6B4"), g2=("#A9C79A", "#8DB27E"), sun="#FFE6B8"),
    "sommer": dict(sky=("#4FA6E6", "#CDEBFA"), g1=("#C4E6A6", "#9ED17E"), g2=("#86C266", "#69A84E"), sun="#FFF2B0"),
    "høst": dict(sky=("#4A4F8C", "#F09A5A"), g1=("#E2C48E", "#C99E5E"), g2=("#B98A4E", "#9C7038"), sun="#FFD9A0"),
}
CAMPS = [(196, 520), (170, 466), (214, 368), (262, 318), (236, 262)]
LOOKS = {
    "markus": dict(skin="#E9B892", hair="#3A2A20", hood="#3557D6", style="kort"),
    "amina": dict(skin="#8A5A3F", hair="#1B1412", hood="#E09A2B", style="fletter"),
    "jonas": dict(skin="#F0CFB6", hair="#C9A060", hood="#2E8A6E", style="bolget"),
    "sara": dict(skin="#EEC3A4", hair="#7A3A22", hood="#8E6CC9", style="lang"),
    "ali": dict(skin="#B07A56", hair="#16110F", hood="#2A2F45", style="krus"),
    "linh": dict(skin="#E2BC96", hair="#14100E", hood="#C8453A", style="knute"),
}


def season_of(m):
    return "vinter" if m in (0, 1, 10, 11) else "vår" if m in (2, 3, 4) else "sommer" if m in (5, 6, 7) else "høst"


def status():
    return T(26, 31, "9:41", 15, "#FFFFFF", 700) + '<rect x="330" y="20" width="24" height="12" rx="3.5" fill="none" stroke="#FFFFFF" stroke-width="1.4"/><rect x="332.5" y="22.5" width="17" height="7" rx="1.5" fill="#FFFFFF"/>'


def home():
    return '<rect x="140" y="831" width="110" height="5" rx="2.5" fill="#FFFFFF" opacity=".85"/>'


def lock_icon(x, y, col=None, s=1):
    col = col or C["gold"]
    return f'<g transform="translate({x} {y}) scale({s})"><rect x="0" y="9" width="18" height="15" rx="3" fill="{col}"/><path d="M4 9 V6 a5 5 0 0 1 10 0 V9" fill="none" stroke="{col}" stroke-width="2.6"/></g>'


# ------------------------------------------------------------------ toppfeltet
def pill(x, y, w, icon, text):
    return f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="17" fill="{C["hud2"]}" stroke="#3A4778" stroke-width="2"/>' + icon + G(x + w - 12, y + 24, text, 18, "#FFFFFF", "end", "#0B1020")


def shield(cx, cy, age, s=1):
    p = "M0 -27 L24 -21 V1 C24 15 12 23 0 27 C-12 23 -24 15 -24 1 V-21 Z"
    return (f'<g transform="translate({cx} {cy}) scale({s})"><path d="{p}" fill="{mix(C["gold2"], "#000000", .3)}" transform="translate(0 3)"/>'
            f'<path d="{p}" fill="{grad("#FFE27A", C["gold"])}" stroke="#8A5A00" stroke-width="2"/>' + G(0, 9, str(age), 24, "#FFFFFF", "middle", "#8A5A00") + '</g>')


def hud(age=16, year=2, month=3, money="18 450 kr", trivsel="64", track=True):
    o = [f'<rect x="0" y="0" width="390" height="156" fill="{C["hud"]}"/>', status(), shield(38, 77, age)]
    o.append(G(72, 72, f"Du, {age} år", 20, "#FFFFFF", "start", "#0B1020") + T(72, 94, f"Nivå {age} · År {year} av 5", 13, "#C9D2F2", 700))
    o.append(pill(234, 52, 140, coin(254, 69), money))
    o.append(pill(282, 92, 92, heart(302, 109, .95), trivsel))
    if track:
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
            if i in ACTIVE:
                o.append(f'<circle cx="{x+23}" cy="121" r="4" fill="{C["red"] if i >= month else C["gold2"]}" stroke="{C["hud"]}" stroke-width="1.5"/>')
        if 0 <= month < 12:
            xm = 20 + month * 29.6 + 13
            o.append(f'<path d="M{xm} 150 l-6 7 h12 z" fill="#FFFFFF"/>' + G(min(max(xm, 40), 350), 172, MONTHS[month], 15, "#FFFFFF", "middle", "#0B1020"))
    return "".join(o)


# ------------------------------------------------------------------ fjellet og leiren
def sky_and_mountain(season):
    S = SEASON[season]
    o = [f'<rect x="0" y="156" width="390" height="494" fill="{grad(*S["sky"])}"/>', f'<circle cx="86" cy="250" r="22" fill="{S["sun"]}" opacity=".9"/>']
    if S.get("stars"):
        o.append("".join(f'<circle cx="{(i*53) % 380 + 6}" cy="{190 + (i*37) % 150}" r="1.4" fill="#FFFFFF" opacity=".8"/>' for i in range(22)))
    o.append(f'<path d="M-20 470 L60 360 L120 420 L170 350 L220 470 Z" fill="#9C93CF"/><path d="M60 360 L120 420 L90 470 Z" fill="#8A81BE"/>')
    o.append(f'<path d="M70 560 L250 196 L420 560 Z" fill="{grad("#8E86C6", "#5F5A9C")}"/><path d="M250 196 L420 560 H330 Z" fill="#4E4A88" opacity=".55"/>')
    o.append('<path d="M250 196 L292 282 L272 272 L258 290 L240 270 L222 284 L214 268 Z" fill="#FFFFFF"/><path d="M250 196 L292 282 L272 272 Z" fill="#DCD8F2"/>')
    return "".join(o)


def trail(year=2, lock_camp=4, goal=31, summit_label=True, done_all=False):
    pts = [(130, 572), (196, 520), (170, 466), (240, 420), (214, 368), (262, 318), (236, 262), (250, 204)]
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    o = [f'<path d="{d}" stroke="#FFFFFF" stroke-width="4" fill="none" stroke-dasharray="2 9" stroke-linecap="round" opacity=".9"/>']
    idx = {1: 2, 2: 3, 3: 5, 4: 6, 5: 7}
    upto = len(pts) if done_all else idx.get(year, 2)
    o.append(f'<path d="M' + " L".join(f"{x} {y}" for x, y in pts[:upto]) + f'" stroke="{C["gold"]}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
    for n, (x, y) in enumerate(CAMPS, 1):
        if n == year and not done_all:
            continue
        st = "done" if (n < year or done_all) else ("lock" if n == lock_camp else "next")
        fill = C["gold"] if st == "done" else ("#FFFFFF" if st == "next" else "#3A3F66")
        o.append(f'<path d="M{x} {y} V{y-26}" stroke="#2A2F50" stroke-width="2.5"/><path d="M{x} {y-26} L{x+20} {y-20} L{x} {y-14} Z" fill="{fill}" stroke="#2A2F50" stroke-width="1.5"/>')
        o.append(f'<rect x="{x-24}" y="{y+4}" width="48" height="20" rx="10" fill="{C["hud"]}" opacity=".9"/>' + T(x, y + 18, f"År {n}", 11.5, "#FFFFFF", 800, "middle"))
        if st == "lock":
            o.append(lock_icon(x + 24, y - 34, s=.8))
    if not done_all:
        x, y = CAMPS[year - 1]
        o.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{C["red"]}" stroke="#FFFFFF" stroke-width="3"/>')
        lx = x - 50 if x > 190 else x - 50
        o.append(f'<rect x="{lx-48}" y="{y-46}" width="96" height="22" rx="11" fill="#FFFFFF"/>' + T(lx, y - 30, f"År {year} · du er her", 11.5, C["ink"], 800, "middle"))
    o.append(f'<path d="M250 204 V160" stroke="#2A2F50" stroke-width="3"/><path d="M250 160 L284 168 L250 178 Z" fill="{C["green"]}" stroke="#2A2F50" stroke-width="1.5"/>')
    if summit_label:
        o.append(f'<g filter="url(#sh)"><rect x="282" y="176" width="100" height="76" rx="12" fill="#FFFFFF"/></g>'
                 + T(332, 196, "Toppen: 20 år", 11.5, C["ink"], 800, "middle") + T(332, 212, "Egen leilighet", 12, C["ink"], 800, "middle")
                 + f'<rect x="292" y="219" width="80" height="9" rx="4.5" fill="#E2E4F0"/><rect x="292" y="219" width="{max(4, 80*goal/100):.0f}" height="9" rx="4.5" fill="{C["green"]}"/>'
                 + T(332, 244, f"{goal} % spart", 12, C["ink"], 800, "middle"))
    return "".join(o)


def ground(season):
    S = SEASON[season]
    return (f'<path d="M0 560 Q120 536 230 548 Q320 556 390 540 V650 H0 Z" fill="{grad(*S["g1"])}"/>'
            f'<path d="M0 600 Q140 586 260 598 Q340 604 390 594 V650 H0 Z" fill="{grad(*S["g2"])}"/>')


def tent():
    return ('<ellipse cx="96" cy="604" rx="70" ry="10" fill="#0B1020" opacity=".2"/>'
            f'<path d="M30 602 L96 504 L162 602 Z" fill="{grad("#FF9E5E", "#E5652F")}"/><path d="M96 504 L162 602 H120 Z" fill="#C4511F"/>'
            '<path d="M96 540 L80 602 H112 Z" fill="#7A2E12"/><path d="M96 504 L96 492" stroke="#4A3426" stroke-width="3"/><path d="M40 586 L96 512" stroke="#FFFFFF" stroke-width="3" opacity=".35"/>')


def moped():
    return ('<ellipse cx="22" cy="620" rx="26" ry="6" fill="#0B1020" opacity=".2"/><circle cx="6" cy="610" r="10" fill="#2A2F50"/><circle cx="40" cy="610" r="10" fill="#2A2F50"/>'
            f'<path d="M6 610 L16 588 H34 L40 610" fill="none" stroke="{C["hood"]}" stroke-width="6" stroke-linejoin="round"/><path d="M30 588 L36 574 H44" stroke="#2A2F50" stroke-width="4" fill="none"/>')


def campfire(lit=True):
    o = '<path d="M188 604 L226 592 M190 592 L228 604" stroke="#6B4128" stroke-width="7" stroke-linecap="round"/>'
    if lit:
        o = (f'<ellipse cx="208" cy="590" rx="44" ry="20" fill="#FFB35C" opacity=".45" filter="url(#blur)"/>' + o +
             f'<path d="M196 596 C194 580 206 574 204 560 C214 570 222 580 218 596 Z" fill="{grad("#FFD27A", "#FF7A3D")}"/>')
    return o


def radio_mast():
    return ('<path d="M30 460 L44 560 M58 460 L44 560 M36 500 H52 M33 480 H55" stroke="#4A4F6E" stroke-width="3" fill="none"/>'
            f'<path d="M44 460 V438" stroke="#4A4F6E" stroke-width="3"/><circle cx="44" cy="436" r="4" fill="{C["red"]}"/>'
            '<path d="M30 428 a18 18 0 0 1 28 0 M24 420 a26 26 0 0 1 40 0" stroke="#FFFFFF" stroke-width="2.4" fill="none" opacity=".8"/>')


def kiosk():
    return ('<ellipse cx="340" cy="612" rx="48" ry="8" fill="#0B1020" opacity=".2"/>'
            f'<rect x="300" y="540" width="80" height="68" rx="6" fill="{grad("#3A9C82", C["teal"])}"/>'
            f'<path d="M292 540 L388 540 L380 520 H300 Z" fill="#FFFFFF"/><path d="M300 520 h16 l-4 20 h-16 Z M332 520 h16 l-4 20 h-16 Z M364 520 h16 l-4 20 h-16 Z" fill="{C["red"]}"/>'
            f'<rect x="312" y="556" width="56" height="26" rx="4" fill="#E8F6F1"/>' + T(340, 574, "BUTIKKEN", 9.5, C["teal"], 800, "middle"))


def depot():
    return ('<ellipse cx="268" cy="626" rx="34" ry="6" fill="#0B1020" opacity=".2"/>'
            f'<rect x="240" y="596" width="40" height="30" rx="4" fill="{grad("#C9925E", "#A8723F")}"/><path d="M240 606 H280 M260 596 V626" stroke="#7A4E2A" stroke-width="2"/>'
            f'<rect x="270" y="604" width="28" height="22" rx="3" fill="{grad("#7D879E", "#5A6378")}"/><circle cx="284" cy="615" r="5" fill="none" stroke="#E9EDF4" stroke-width="2"/>'
            + coin(252, 590, 8) + coin(266, 586, 8))


def car():
    """Eiendel fra 18 år: bil ved leiren (FR-34)."""
    return ('<ellipse cx="34" cy="622" rx="40" ry="6" fill="#0B1020" opacity=".2"/>'
            f'<path d="M-6 616 V598 Q-4 590 6 588 L20 572 H52 L68 588 Q78 590 78 598 V616 Z" fill="{grad("#FF6F59", "#D9483A")}"/>'
            '<path d="M24 576 H50 L60 588 H16 Z" fill="#CFE6F5"/><circle cx="12" cy="616" r="9" fill="#2A2F50"/><circle cx="60" cy="616" r="9" fill="#2A2F50"/>')


def storm():
    o = ['<rect x="0" y="156" width="390" height="494" fill="#1B2340" opacity=".45"/>',
         '<path d="M-10 230 Q60 200 130 226 Q190 196 260 222 Q330 194 400 220 V170 H-10 Z" fill="#3A4060"/>']
    o.append("".join(f'<path d="M{(i*41) % 400} {180 + (i*67) % 440} l-10 26" stroke="#CFE0F5" stroke-width="2" opacity=".7"/>' for i in range(46)))
    o.append('<path d="M300 200 L284 246 H298 L286 290" stroke="#FFE27A" stroke-width="4" fill="none" stroke-linejoin="round"/>')
    return "".join(o)


# ------------------------------------------------------------------ figurer
def figure(cx, feet, h=118, look="markus", mood="smil", hold=None):
    L = LOOKS[look] if isinstance(look, str) else look
    s = h / 176
    sk, hd, hr = L["skin"], L["hood"], L["hair"]
    o = [f'<g transform="translate({cx} {feet}) scale({s:.3f})">', '<ellipse cx="0" cy="0" rx="40" ry="8" fill="#0B1020" opacity=".25"/>',
         f'<rect x="-22" y="-80" width="20" height="78" rx="9" fill="{grad("#4A5A7A", "#36435E")}"/><rect x="2" y="-80" width="20" height="78" rx="9" fill="{grad("#41506E", "#2E3A52")}"/>',
         '<rect x="-26" y="-10" width="26" height="12" rx="6" fill="#FFFFFF"/><rect x="0" y="-10" width="26" height="12" rx="6" fill="#F0F0F0"/>']
    if L["style"] in ("lang", "fletter"):
        o.append(f'<path d="M-24 -176 C-30 -140 -30 -120 -26 -104 H26 C30 -120 30 -140 24 -176 Z" fill="{hr}"/>')
    o.append(f'<path d="M-30 -136 Q-34 -84 -28 -76 H28 Q34 -84 30 -136 Q0 -148 -30 -136 Z" fill="{grad(mix(hd, "#FFFFFF", .2), hd)}"/>')
    arm_up = mood == "glad"
    if arm_up:
        o.append(f'<path d="M-30 -132 Q-48 -160 -44 -190" stroke="{mix(hd, "#000000", .15)}" stroke-width="13" stroke-linecap="round" fill="none"/><circle cx="-44" cy="-194" r="7" fill="{sk}"/>')
    else:
        o.append(f'<path d="M-30 -132 Q-44 -110 -40 -84" stroke="{mix(hd, "#000000", .15)}" stroke-width="13" stroke-linecap="round" fill="none"/><circle cx="-40" cy="-80" r="7" fill="{sk}"/>')
    o.append(f'<path d="M30 -132 Q46 -116 40 -96 L26 -88" stroke="{mix(hd, "#000000", .25)}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="24" cy="-88" r="7" fill="{sk}"/>')
    o.append(f'<rect x="-14" y="-104" width="28" height="18" rx="5" fill="{mix(hd, "#000000", .2)}"/>')
    o.append(f'<path d="M-14 -142 Q0 -132 14 -142" stroke="#F4EFE6" stroke-width="3" fill="none"/><path d="M-6 -138 V-118 M6 -138 V-118" stroke="#F4EFE6" stroke-width="2.4"/>')
    o.append(f'<rect x="-7" y="-152" width="14" height="14" fill="{mix(sk, "#000000", .12)}"/><ellipse cx="0" cy="-172" rx="21" ry="24" fill="{grad(mix(sk, "#FFFFFF", .15), sk)}"/>')
    st = L["style"]
    if st == "kort":
        o.append(f'<path d="M-22 -174 Q-24 -200 0 -200 Q24 -200 22 -174 Q16 -188 2 -186 Q-12 -190 -22 -174 Z" fill="{hr}"/>')
    elif st in ("lang", "fletter"):
        o.append(f'<path d="M-24 -168 Q-26 -202 0 -202 Q26 -202 24 -168 Q16 -192 0 -190 Q-16 -192 -24 -168 Z" fill="{hr}"/>')
        if st == "fletter":
            o.append("".join(f'<path d="M{x} -150 V-108" stroke="{mix(hr, "#FFFFFF", .25)}" stroke-width="2" stroke-dasharray="4 4"/>' for x in (-22, -16, 16, 22)))
    elif st == "bolget":
        o.append(f'<path d="M-24 -160 Q-30 -204 2 -202 Q30 -200 24 -160 Q20 -186 8 -188 Q-6 -182 -16 -190 Q-22 -180 -24 -160 Z" fill="{hr}"/>')
    elif st == "krus":
        o.append("".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{hr}"/>' for x, y in [(-18, -186), (-8, -196), (6, -197), (17, -188), (-22, -176), (22, -176), (0, -190)]))
    elif st == "knute":
        o.append(f'<circle cx="0" cy="-204" r="9" fill="{hr}"/><path d="M-22 -172 Q-24 -198 0 -198 Q24 -198 22 -172 Q12 -186 0 -186 Q-12 -186 -22 -172 Z" fill="{hr}"/>')
    lid = 1.5 if mood == "sliten" else 3.4
    o.append(f'<ellipse cx="-8" cy="-171" rx="2.6" ry="{lid}" fill="#151A2E"/><ellipse cx="8" cy="-171" rx="2.6" ry="{lid}" fill="#151A2E"/>')
    mouth = {"smil": "M-6 -160 Q0 -155 6 -160", "glad": "M-8 -161 Q0 -150 8 -161 Z", "sliten": "M-6 -157 Q0 -161 6 -157", "tenker": "M-5 -159 H5"}[mood]
    o.append(f'<path d="{mouth}" stroke="#8A3B3B" stroke-width="2.2" fill="{"#8A3B3B" if mood == "glad" else "none"}" stroke-linecap="round"/>')
    o.append('<ellipse cx="-14" cy="-163" rx="4" ry="2.4" fill="#E5484D" opacity=".18"/><ellipse cx="14" cy="-163" rx="4" ry="2.4" fill="#E5484D" opacity=".18"/></g>')
    return "".join(o)


def portrait(cx, cy, r, look):
    """Rundt profilbilde til utvalget av utseender."""
    L = LOOKS[look]
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{grad("#8CC3CF", "#6FA9B8")}"/>'
            f'<clipPath id="pc{look}"><circle cx="{cx}" cy="{cy}" r="{r-2}"/></clipPath><g clip-path="url(#pc{look})">{figure(cx, cy + r*3.3, r*3.6, look)}</g>')


# ------------------------------------------------------------------ merker og knapper
def bubble(cx, cy, inner, badge=None, r=22):
    return B.bubble(cx, cy, inner, badge, r)


def ground_tags(items):
    o = []
    for cx, t in items:
        w = len(t) * 8 + 18
        o.append(f'<rect x="{cx-w/2:.0f}" y="626" width="{w:.0f}" height="22" rx="11" fill="{C["hud"]}"/>' + T(cx, 641, t, 12, "#FFFFFF", 800, "middle"))
    return "".join(o)


def big_button(y, text, col=None, w=362, x=14, h=70, size=26, arrow=True):
    col = col or C["green"]
    dark = mix(col, "#000000", .45)
    o = gloss(x, y, w, h, 22, col, 7) + G(x + w / 2 - (14 if arrow else 0), y + h / 2 + size * .35, text, size, "#FFFFFF", "middle", dark)
    if arrow:
        ax = x + w / 2 + len(text) * size * .27 + 8
        o += f'<path d="M{ax} {y+h/2-12} l18 12 -18 12 z" fill="#FFFFFF" stroke="{dark}" stroke-width="3" stroke-linejoin="round"/>'
    return o


def white_button(x, y, w, text, h=56, size=18):
    return (f'<rect x="{x}" y="{y+5}" width="{w}" height="{h}" rx="18" fill="#A9B2D6"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{grad("#FFFFFF", "#E6EAF6")}"/>'
            + G(x + w / 2, y + h / 2 + size * .35, text, size, C["ink"], "middle"))


def bottom_bar(lock=("Leir 4 åpner på nivå 18", "kredittkort, bil-lappen og forbrukslån"), button="NESTE MÅNED", hint="Neste måned venter. Ingen ting må gjøres først.", disabled=False):
    o = [f'<rect x="0" y="650" width="390" height="194" fill="{C["hud"]}"/>']
    if lock:
        o.append(f'<rect x="14" y="662" width="362" height="48" rx="14" fill="{C["hud2"]}" stroke="#3A4778" stroke-width="2"/>' + lock_icon(28, 673) +
                 T(58, 682, lock[0], 13.5, "#FFFFFF", 800) + T(58, 700, lock[1], 12.5, "#C9D2F2", 700))
    o.append(big_button(724, button, "#6A7090" if disabled else None))
    o.append(T(195, 822, hint, 12.5, "#C9D2F2", 700, "middle"))
    return "".join(o)


def camp(month=3, age=16, year=2, money="18 450 kr", trivsel="64", goal=31, mood="smil", look="markus", msgs="2", plan="2", wage="+4 290 kr",
         lock_camp=4, belongings=("moped",), dim=0, stations=True, weather=None, lit=True, tags=True):
    """Leiren uten toppfelt og bunnfelt."""
    season = season_of(month)
    o = [sky_and_mountain(season), trail(year, lock_camp, goal), ground(season)]
    if weather == "storm":
        o.append(storm())
    o.append(radio_mast() + tent() + campfire(lit) + kiosk() + depot())
    if "moped" in belongings:
        o.append(moped())
    if "bil" in belongings:
        o.append(car())
    o.append(figure(150, 636, 118, look, mood))
    if stations:
        if msgs:
            o.append(bubble(44, 392, ICON_MSG(44, 390), msgs))
        if plan:
            o.append(bubble(222, 520, ICON_PLAN(222, 522), plan))
        if wage:
            o.append(bubble(340, 470, coin(340, 468, 12)) + f'<rect x="300" y="584" width="80" height="22" rx="11" fill="{C["hud"]}"/>' + G(340, 600, wage, 13, C["gold"], "middle"))
    if tags:
        o.append(ground_tags([(44, "Mobil"), (96, "Hjem"), (208, "Kveldene"), (268, "Penger"), (340, "Jobb")]))
    if dim:
        o.append(f'<rect x="0" y="156" width="390" height="494" fill="#0B1020" opacity="{dim}"/>')
    return "".join(o)


# ------------------------------------------------------------------ paneler (sprettvinduer i spillstil)
def panel(x, y, w, h, title=None, ribbon=None):
    o = [f'<rect x="{x}" y="{y+6}" width="{w}" height="{h}" rx="22" fill="#0B1020" opacity=".5"/>',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{grad(C["hud2"], C["hud"])}" stroke="#4A5890" stroke-width="3"/>']
    if title:
        rc = ribbon or C["gold"]
        o.append(f'<path d="M{x+30} {y-18} H{x+w-30} l12 22 -12 22 H{x+30} l-12 -22 Z" fill="{mix(rc, "#000000", .3)}" transform="translate(0 4)"/>'
                 f'<path d="M{x+30} {y-18} H{x+w-30} l12 22 -12 22 H{x+30} l-12 -22 Z" fill="{grad(mix(rc, "#FFFFFF", .25), rc)}"/>'
                 + G(x + w / 2, y + 12, title, 21, "#FFFFFF", "middle", mix(rc, "#000000", .45)))
    return "".join(o)


def field(x, y, w, label, value="", masked=False):
    o = [T(x, y, label, 13.5, "#FFFFFF", 700), f'<rect x="{x}" y="{y+8}" width="{w}" height="50" rx="14" fill="#FFFFFF" stroke="#8592C4" stroke-width="2"/>']
    if masked:
        o.append("".join(f'<circle cx="{x+20+i*14}" cy="{y+33}" r="4.5" fill="{C["ink"]}"/>' for i in range(value)))
    elif value:
        o.append(T(x + 16, y + 39, value, 15.5, C["ink"], 600))
    return "".join(o)


def link(x, y, text, anchor="start", col="#FFFFFF"):
    return T(x, y, text, 14.5, col, 700, anchor, 'text-decoration="underline"')


def option_card(x, y, w, icon, title, sub, value, h=74, col="#FFFFFF"):
    return (f'<rect x="{x}" y="{y+5}" width="{w}" height="{h}" rx="18" fill="#A9B2D6"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{grad("#FFFFFF", "#EEF1FA")}"/>'
            f'<circle cx="{x+36}" cy="{y+h/2}" r="24" fill="{col}"/>' + icon(x + 36, y + h / 2) +
            T(x + 72, y + 30, title, 16, C["ink"], 800) + T(x + 72, y + 52, sub, 13, "#454B66", 700) +
            G(x + w - 16, y + h / 2 + 6, value, 17, C["ink"], "end"))


def dim_all(op=.55):
    return f'<rect width="390" height="844" fill="#0B1020" opacity="{op}"/>'


def phone(app, body, back=None):
    o = [dim_all(.6), f'<rect x="30" y="56" width="330" height="770" rx="46" fill="#0B0E1A" stroke="#4A5890" stroke-width="3"/>',
         f'<rect x="42" y="68" width="306" height="746" rx="36" fill="#F6F7FB"/><rect x="160" y="80" width="70" height="20" rx="10" fill="#0B0E1A"/>',
         T(64, 96, "9:41", 13, C["ink"], 700), '<path d="M42 160 H348" stroke="#E2E4EE"/>']
    if back:
        o.append(f'<path d="M68 128 l-8 8 8 8" stroke="{C["ink"]}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' + T(78, 141, back, 15, C["ink"], 600) + T(195, 141, app, 17, C["ink"], 800, "middle"))
    else:
        o.append(T(62, 146, app, 26, C["ink"], 800))
    o.append(body + f'<rect x="140" y="798" width="110" height="5" rx="2.5" fill="{C["ink"]}"/>')
    return "".join(o)


def banner(sender, lines, col, initial=None, y=50):
    return (f'<g filter="url(#sh)"><rect x="12" y="{y}" width="366" height="86" rx="20" fill="#FBFBFD"/></g>'
            f'<rect x="26" y="{y+16}" width="36" height="36" rx="9" fill="{col}"/>' + T(44, y + 41, initial or sender[0], 18, "#FFFFFF", 800, "middle") +
            T(74, y + 32, sender, 15, C["ink"], 800) + T(364, y + 32, "nå", 13, "#4A5068", 600, "end") +
            "".join(T(74, y + 54 + i * 18, l, 14, C["ink"], 500) for i, l in enumerate(lines)))
