# «Veien»: alle skjermene i appen. Kjør: python alle.py [nummer ...]
# Tallene er eksempeldata fra PRD-ens brukerreiser (UJ-1 til UJ-6), ikke motorberegninger.
import os, sys
import veien2
from veien2 import *

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "skjermer")
os.makedirs(OUT, exist_ok=True)
SCREENS = {}
HUB_SEGS = veien2.SEGS
EV_SEGS = [((170, 600), (60, 520), (330, 440), (220, 390)), ((220, 390), (150, 340), (270, 300), (212, 262))]
EMMA = dict(top=C2["jacket"], top2="#B9AEE6", hair="#5A1E8C", style="long", pants="#3A2A6E", face=-1, rim="#FFD36E")
FIELD_EDGE, TRACK_EDGE = "#7E68D8", "#6B57C9"
INK, SOFT, LIME, PRESS, PANEL, P2, LINE = C["ink"], C["soft"], C["lime"], C["press"], C["panel"], "#24125E", "#5B44B8"
MONTHS = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]


def screen(name, title):
    def deco(fn):
        SCREENS[name] = (title, fn)
        return fn
    return deco


def at(t):
    x, y = road_pt(t)
    return x, y, road_scale(t)


# ------------------------------------------------------------------ felles deler
def band(h=190, sun=True):
    """Smal himmelstripe øverst på undersider, så verden er med overalt."""
    o = [f'<rect width="390" height="{h}" fill="url(#sky)"/>']
    for i, (x, y) in enumerate([(30, 50), (140, 40), (250, 34), (320, 70), (200, 90), (80, 100)]):
        if y < h - 60:
            o.append(f'<circle cx="{x}" cy="{y}" r="1.8" fill="#fff" opacity=".8"/>')
    if sun:
        o.append(f'<circle cx="310" cy="{h-28}" r="40" fill="{C["sun"]}" opacity=".35" filter="url(#glow)"/><circle cx="310" cy="{h-26}" r="30" fill="{C["sun"]}"/>')
    o.append(f'<path d="M0 {h-30} C80 {h-58} 150 {h-34} 220 {h-50} S330 {h-60} 390 {h-40} V{h+40} H0Z" fill="{C["far"]}"/>')
    o.append(f'<path d="M0 {h-12} C90 {h-30} 200 {h-8} 390 {h-24} V{h+40} H0Z" fill="{C["mid"]}"/>')
    return "".join(o)


def sheet(y):
    return f'<path d="M0 {y+26} Q0 {y} 26 {y} H364 Q390 {y} 390 {y+26} V844 H0Z" fill="{PANEL}"/>'


def topnav(title, back=True, y=62, right=None):
    o = []
    if back:
        o.append(f'<g filter="url(#sh)"><circle cx="40" cy="{y+2}" r="20" fill="#12053A" opacity=".6"/></g><path d="M44 {y-6}l-8 8 8 8" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>')
    o.append(T(72 if back else 24, y + 10, title, 26, "#fff", 900))
    if right:
        o.append(right)
    return "".join(o)


def menu_btn(x=326, y=62):
    return (f'<g transform="translate({x} {y})"><rect width="44" height="44" rx="14" fill="#12053A" opacity=".55"/>'
            '<path d="M13 15h18M13 22h18M13 29h12" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/></g>')


def field(y, label, value, masked=False, placeholder=False, error=None, x=24, w=342):
    o = [T(x, y, label, 13, SOFT, 600)]
    o.append(f'<rect x="{x}" y="{y+8}" width="{w}" height="52" rx="14" fill="{P2}" stroke="{PRESS if error else FIELD_EDGE}" stroke-width="2"/>')
    if masked:
        o.append("".join(f'<circle cx="{x+22+i*14}" cy="{y+34}" r="4.5" fill="#fff"/>' for i in range(value)))
    else:
        o.append(T(x + 16, y + 40, value, 16, SOFT if placeholder else "#fff", 500))
    if error:
        o.append(f'<circle cx="{x+8}" cy="{y+78}" r="7" fill="{PRESS}"/>' + T(x + 8, y + 82, "!", 11, INK, 900, "middle") + T(x + 22, y + 82, error, 13, "#FFB3C9", 600))
    return "".join(o)


def checkbox(y, label, checked=False, x=24):
    o = f'<rect x="{x}" y="{y}" width="26" height="26" rx="8" fill="{LIME if checked else "none"}" stroke="{LIME if checked else SOFT}" stroke-width="2"/>'
    if checked:
        o += f'<path d="M{x+7} {y+13}l5 5 8-10" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    return o + T(x + 38, y + 18, label, 14.5, "#fff", 500)


def primary(y, label, x=24, w=342, arrow=True, h=56):
    o = (f'<rect x="{x}" y="{y+5}" width="{w}" height="{h}" rx="18" fill="{C["lime2"]}"/>'
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{LIME}"/>'
         f'<rect x="{x+16}" y="{y+8}" width="{w*0.28:.0f}" height="4" rx="2" fill="#fff" opacity=".5"/>'
         + T(x + w / 2 - (10 if arrow else 0), y + h / 2 + 7, label, 17, INK, 900, "middle", 'letter-spacing=".8"'))
    if arrow:
        o += f'<path d="M{x+w-44} {y+h/2}h18m-7-7 7 7-7 7" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    return o


def secondary(y, label, x=24, w=342, h=52, col="#fff"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="none" stroke="{col}" stroke-width="2"/>' + T(x + w / 2, y + h / 2 + 6, label, 16, col, 700, "middle")


def card(x, y, w, h, stroke=None, fill=None):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill or P2}" stroke="{stroke or LINE}" stroke-width="1.5"/>'


def row(y, left, right=None, sub=None, x=24, w=342, rc="#fff", chevron=False):
    o = T(x, y, left, 15.5, "#fff", 700)
    if sub:
        o += T(x, y + 19, sub, 12.5, SOFT, 400)
    if right:
        o += T(x + w - (18 if chevron else 0), y, right, 15.5, rc, 800, "end")
    if chevron:
        o += f'<path d="M{x+w-6} {y-11}l6 6-6 6" fill="none" stroke="{SOFT}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    return o


def divider(y, x=24, w=342):
    return f'<path d="M{x} {y}H{x+w}" stroke="#3A2580"/>'


def seg_bar(x, y, w, val, color=None, h=8, thr=None, mark=None):
    color = color or LIME
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#3A2580" stroke="{TRACK_EDGE}" stroke-width="1.5"/>',
         f'<rect x="{x}" y="{y}" width="{w*val/100:.0f}" height="{h}" rx="{h/2}" fill="{color}"/>']
    if thr is not None:
        o.append(f'<path d="M{x+w*thr/100:.0f} {y-5}v{h+10}" stroke="#fff" stroke-width="2"/>')
    return "".join(o)


def year_line_compact(x, y, w, current, done):
    """Kort årslinje i HUD: tolv punkter med forbokstav under."""
    letters = "JFMAMJJASOND"
    o = []
    step = w / 11
    o.append(f'<path d="M{x} {y}H{x+w}" stroke="#fff" stroke-width="2" opacity=".35"/>')
    o.append(f'<path d="M{x} {y}H{x+step*min(current,11):.1f}" stroke="#fff" stroke-width="2.4"/>')
    for i, L in enumerate(letters):
        cx = x + i * step
        active = i in (0, 3, 6, 9)
        if i == current:
            o.append(f'<circle cx="{cx:.1f}" cy="{y}" r="6.5" fill="{LIME}" stroke="#12053A" stroke-width="2"/>')
        elif i < done:
            o.append(f'<circle cx="{cx:.1f}" cy="{y}" r="{4 if active else 3}" fill="#fff"/>')
        else:
            o.append(f'<circle cx="{cx:.1f}" cy="{y}" r="{4 if active else 3}" fill="#12053A" stroke="#fff" stroke-width="1.5" opacity=".8"/>')
        o.append(T(f"{cx:.1f}", y + 17, L, 9.5, LIME if i == current else "#E9E2FF", 800 if i == current else 600, "middle"))
    return "".join(o)


def hud2(month, age, year_no, current, done, stats=True, sub=None):
    o = [status(), level_badge(42, 86, age), T(76, 80, month, 27, "#fff", 900, extra='letter-spacing="-.5"')]
    o.append(T(76, 99, sub or f"År {year_no} av 5", 12.5, "#E9E2FF", 700))
    o.append(menu_btn())
    if not sub:
        o.append(f'<g filter="url(#sh)"><rect x="20" y="118" width="350" height="44" rx="16" fill="#12053A" opacity=".6"/></g>')
        o.append(year_line_compact(38, 133, 314, current, done))
    if stats:
        o.append(f'<g filter="url(#sh)"><rect x="20" y="172" width="128" height="36" rx="18" fill="#12053A" opacity=".72"/></g>' + coin(40, 190, 10) + T(58, 196, "3 120 kr", 16, "#fff", 900))
        o.append(f'<g filter="url(#sh)"><rect x="156" y="172" width="112" height="36" rx="18" fill="#12053A" opacity=".72"/></g>' + heart(176, 189, 1.05) + T(192, 196, "64", 16, "#fff", 900) + T(216, 196, "trivsel", 11.5, SOFT, 600))
    return "".join(o)


def portrait(cx, cy, r, **kw):
    cid = f"pt{cx}{cy}{r}"
    return (f'<clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#2A1470"/><g clip-path="url(#{cid})">{person(cx, cy + r * 2.9, r / 30, **kw)}</g>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LIME}" stroke-width="2.5"/>')


def dialog(y0, h, who=None, sub=None, stroke=None, accent=None):
    accent = accent or LIME
    o = [f'<rect x="0" y="{y0-50}" width="390" height="{844-y0+50}" fill="url(#fade)"/>',
         f'<g filter="url(#sh)"><rect x="12" y="{y0}" width="366" height="{h}" rx="24" fill="{PANEL}" stroke="{stroke or LINE}" stroke-width="2"/></g>',
         f'<rect x="40" y="{y0-2}" width="310" height="5" rx="2.5" fill="{accent}"/>']
    if who:
        o.append(who)
    return "".join(o)


def home_ind(col="#fff"):
    return f'<rect x="140" y="828" width="110" height="4" rx="2" fill="{col}" opacity=".5"/>'


# ------------------------------------------------------------------ 01-04 innlogging
@screen("01-velkommen", "Første skjerm: Logg inn eller Opprett bruker")
def s01():
    veien2.SEGS = HUB_SEGS
    b = [landscape(), status()]
    x, y, k = at(.36)
    b.append(person(x - 34, y + 8, 1.0, face=1))
    b.append(person(x + 34, y + 2, .92, wave=True, **EMMA))
    b.append(f'<rect x="0" y="0" width="390" height="250" fill="#12053A" opacity=".0"/>')
    b.append(T(195, 132, "LifeMode", 50, "#fff", 900, "middle", 'letter-spacing="-1.5"'))
    b.append(T(195, 166, "Fem år av livet. Hvert valg teller.", 16, "#E9E2FF", 600, "middle"))
    b.append('<rect x="0" y="560" width="390" height="284" fill="url(#fade)"/>')
    b.append(primary(632, "OPPRETT BRUKER"))
    b.append(secondary(704, "Logg inn"))
    b.append(T(195, 794, "Glemt passord?", 14.5, "#E9E2FF", 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


@screen("02-opprett-bruker", "Opprett bruker med spillerinformasjon")
def s02():
    b = [band(170), status(), topnav("Opprett bruker"), sheet(150)]
    b.append(field(196, "E-post", "markus@eksempel.no"))
    b.append(field(278, "Skriv e-posten en gang til", "markus@eksempel.no"))
    b.append(field(360, "Passord (minst 8 tegn)", 9, masked=True))
    b.append(checkbox(446, "Hold meg innlogget på denne enheten"))
    b.append(card(24, 494, 342, 168))
    b.append(T(42, 524, "Dette lagrer vi", 15, "#fff", 800))
    for i, l in enumerate(["E-posten din, bare for innlogging og nytt passord.", "Spillet ditt, så du kan fortsette på andre enheter.", "Alt slettes etter 12 måneder uten spill.", "Du kan slette kontoen når du vil."]):
        b.append(f'<circle cx="46" cy="{550+i*24}" r="3" fill="{LIME}"/>' + T(58, 554 + i * 24, l, 12.5, SOFT, 400))
    b.append(T(42, 650, "Les hele spillerinformasjonen", 12.5, LIME, 700, extra='text-decoration="underline"'))
    b.append(primary(690, "OPPRETT BRUKER"))
    b.append(T(195, 790, "Har du bruker? Logg inn", 14, "#E9E2FF", 600, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


@screen("03-logg-inn", "Logg inn")
def s03():
    b = [band(240), status(), topnav("Logg inn"), sheet(220)]
    b.append(field(274, "E-post", "markus@eksempel.no"))
    b.append(field(356, "Passord", 10, masked=True))
    b.append(checkbox(444, "Hold meg innlogget på denne enheten"))
    b.append(T(24, 512, "Delt PC, for eksempel på skolen? La boksen stå tom.", 12.5, SOFT, 400))
    b.append(primary(546, "LOGG INN"))
    b.append(T(195, 640, "Glemt passord?", 14.5, LIME, 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


@screen("04-glemt-passord", "Glemt passord: samme svar uansett")
def s04():
    b = [band(240), status(), topnav("Glemt passord"), sheet(220)]
    b.append(T(24, 270, "Skriv e-posten din, så sender vi en lenke.", 14.5, SOFT, 400))
    b.append(field(300, "E-post", "markus@eksempel.no"))
    b.append(card(24, 392, 342, 116, stroke=LIME))
    b.append(f'<circle cx="52" cy="424" r="14" fill="{LIME}"/><path d="M45 424l5 5 9-10" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(T(78, 429, "Sjekk e-posten din", 16, "#fff", 800))
    b.append(T(42, 462, "Hvis adressen har en bruker, får du en lenke.", 13, SOFT, 400))
    b.append(T(42, 484, "Lenken virker én gang, i 60 minutter.", 13, SOFT, 400))
    b.append(primary(540, "SEND NY LENKE", arrow=False))
    b.append(T(195, 634, "Tilbake til innlogging", 14.5, "#E9E2FF", 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 05-07 start på livet
GOALS = [("Spar til noe stort", "Ha minst 100 000 kr spart når du fyller 20.", "For eksempel en start på egen leilighet."),
         ("Gjeldfri med buffer", "Ingen gjeld, og minst 30 000 kr tilgjengelig", "hver måned det siste året."),
         ("Råd til en stor opplevelse", "Kjøp åtte uker Interrail for 60 000 kr", "uten lån, innen august det siste året.")]


@screen("05-livsmal", "Velg livsmål")
def s05():
    b = [band(200), status(), topnav("Velg livsmålet ditt", back=False), sheet(176)]
    b.append(T(24, 214, "Målet sjekkes når du fyller 20. Du kan ikke bytte underveis.", 13, SOFT, 400))
    icons = ['<path d="M-12 8 L0 -10 L12 8Z M-4 8v-8h8v8"/>', '<path d="M-11 -9h22v18h-22z M-11 -3h22"/>', '<path d="M-12 6h24 M-8 6 l4 -14 h8 l4 14 M-2 -8 v-4"/>']
    for i, (t, l1, l2) in enumerate(GOALS):
        y = 234 + i * 132
        sel = i == 0
        b.append(f'<rect x="24" y="{y}" width="342" height="118" rx="20" fill="{P2}" stroke="{LIME if sel else LINE}" stroke-width="{3 if sel else 1.5}"/>')
        b.append(f'<circle cx="62" cy="{y+40}" r="22" fill="{LIME if sel else "#3A2580"}"/><g transform="translate(62 {y+40})" fill="none" stroke="{INK if sel else "#fff"}" stroke-width="2.4" stroke-linejoin="round">{icons[i]}</g>')
        b.append(T(98, y + 36, t, 18, "#fff", 900) + T(42, y + 80, l1, 13.5, SOFT, 400) + T(42, y + 100, l2, 13.5, SOFT, 400))
        if sel:
            b.append(f'<circle cx="340" cy="{y+30}" r="12" fill="{LIME}"/><path d="M334 {y+30}l4 4 8-8" fill="none" stroke="{INK}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(primary(650, "VELG MÅL"))
    b.append(T(195, 750, "Trivselen din teller også: et rikt, men slitsomt liv gir en hul seier.", 12, SOFT, 400, "middle"))
    b.append(home_ind())
    return b


LOOKS = [dict(top="#FF7A59", top2="#D85536", hair="#2A1A12"),
         dict(top="#7A4BD6", top2="#5A33A8", hair="#C27A3A"),
         dict(top="#2FB7A8", top2="#1E8075", hair="#111"),
         dict(top=C2["jacket"], top2="#B9AEE6", hair="#5A1E8C", style="long"),
         dict(top="#FFC24A", top2="#D39522", hair="#3A2014", style="long"),
         dict(top="#3A6FE0", top2="#2851A8", hair="#E8C07A", style="long")]


@screen("06-avatar", "Velg avatar blant faste utseender")
def s06():
    b = [band(200), status(), topnav("Velg hvordan du ser ut", back=True), sheet(176)]
    b.append(T(24, 214, "Du er 15 år og står ved starten av veien.", 13.5, SOFT, 400))
    for i, lk in enumerate(LOOKS):
        cx = 24 + (i % 3) * 116
        cy = 234 + (i // 3) * 198
        sel = i == 0
        b.append(f'<rect x="{cx}" y="{cy}" width="106" height="184" rx="20" fill="{P2}" stroke="{LIME if sel else LINE}" stroke-width="{3 if sel else 1.5}"/>')
        kw = dict(lk)
        b.append(person(cx + 53, cy + 160, .95, face=1, **kw))
        if sel:
            b.append(f'<circle cx="{cx+90}" cy="{cy+18}" r="11" fill="{LIME}"/><path d="M{cx+85} {cy+18}l3.5 3.5 7-7" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(primary(660, "START LIVET"))
    b.append(T(195, 760, "Du får en pengegave med en gang du starter.", 12.5, SOFT, 400, "middle"))
    b.append(home_ind())
    return b


@screen("07-pengegave", "Første valg: hva gjør du med pengegaven?")
def s07():
    veien2.SEGS = EV_SEGS
    b = [landscape()]
    x, y, k = at(.24)
    b.append(person(x - 20, y + 6, .95, face=1))
    gx, gy = x + 46, y - 10
    b.append(f'<circle cx="{gx}" cy="{gy-30}" r="46" fill="{C["sun"]}" opacity=".35" filter="url(#glow)"/>')
    b.append(f'<rect x="{gx-24}" y="{gy-36}" width="48" height="38" rx="5" fill="{PRESS}"/><rect x="{gx-28}" y="{gy-48}" width="56" height="14" rx="4" fill="#FF86A8"/><rect x="{gx-4}" y="{gy-48}" width="8" height="50" fill="{LIME}"/>')
    b.append(burst(gx, gy - 40, 40, 54, C["sun"], 10))
    b.append(float_tag(gx + 20, gy - 110, "+18 400 kr", C["sun"]))
    b.append(hud2("Januar", 15, 1, 0, 0, stats=False, sub="År 1 av 5 · du fyller 15"))
    y0 = 520
    b.append(dialog(y0, 304, who=portrait(48, y0 + 2, 24, top="#FFC24A", top2="#D39522", hair="#5A3A2A", style="long", face=1)))
    b.append(T(82, y0 + 28, "Mamma", 15, "#fff", 900) + T(144, y0 + 28, "gratulerer med dagen!", 12, SOFT, 500))
    b.append(T(28, y0 + 62, "Du har fått 18 400 kr", 22, "#fff", 900))
    b.append(T(28, y0 + 84, "Pengegaven er din. Hva gjør du med den?", 13.5, SOFT, 400))
    for i, (l, p) in enumerate([("Spar alt på sparekonto", "0 kr brukt"), ("Spar halvparten", "9 200 kr"), ("Ny mobil og spill", "18 400 kr")]):
        b.append(chunky(28, y0 + 104 + i * 58, 334, 48, l, p))
    b.append(T(195, y0 + 290, "Det du velger nå, kan dukke opp igjen senere.", 11.5, SOFT, 500, "middle"))
    veien2.SEGS = HUB_SEGS
    return b


# ------------------------------------------------------------------ 08-11 måned og mobil
def hub_scene(month_idx=10):
    veien2.SEGS = HUB_SEGS
    b = [landscape()]
    b.append(milestone(.27, "OKT", "past", -1))
    b.append(milestone(.53, "DES", "future", -1))
    gx, gy, gk = at(.64)
    b.append(age_gate(.64, 18, None))
    b.append(flag(gx + 70, gy + 30, "Førerkort", "75 % spart", .8))
    x, y, k = at(.38)
    b.append(person(x - 4, y + 10, 1.1, face=1))
    return b


@screen("08-maned", "Månedsnavet: veien er hovedmotivet")
def s08():
    b = hub_scene()
    b.append(hud2("November", 17, 3, 10, 10))
    b.append(dock(badges={"Plan": "3", "Mobil": "2"}))
    return b


def sms_banner(y, sender, text, when="nå"):
    """Ser ut som et ekte varsel fra telefonen, ikke som en spillboks."""
    return (f'<g filter="url(#sh)"><rect x="10" y="{y}" width="370" height="76" rx="22" fill="#F4F3F8" opacity=".97"/></g>'
            f'<rect x="24" y="{y+16}" width="38" height="38" rx="10" fill="#34C759"/>'
            f'<path d="M33 {y+31} q0 -8 10 -8 q10 0 10 8 q0 8 -10 8 l-6 4 1 -5 q-5 -2 -5 -7z" fill="#fff"/>'
            + T(74, y + 27, "MELDINGER", 11.5, "#6B6B76", 600, extra='letter-spacing=".5"') + T(366, y + 27, when, 12, "#6B6B76", 500, "end")
            + T(74, y + 46, sender, 15, "#111", 700) + T(74, y + 65, text, 14.5, "#222", 400))


@screen("09-sms-varsel", "En SMS kommer inn som et ekte varsel på telefonen")
def s09():
    b = hub_scene()
    b.append(hud2("November", 17, 3, 10, 10))
    b.append(dock(badges={"Plan": "3", "Mobil": "2"}))
    b.append(f'<rect width="390" height="844" fill="#000" opacity=".12"/>')
    b.append(sms_banner(12, "Emma", "Konsert på fredag, blir du med? 400 kr"))
    return b


def phone_status():
    return (T(30, 30, "9:41", 15, "#111", 600) +
            '<g fill="#111"><rect x="331" y="19" width="23" height="11" rx="3" fill="none" stroke="#111" stroke-width="1.4"/><rect x="333.5" y="21.5" width="16" height="6" rx="1.2"/></g>')


@screen("10-mobil-meldinger", "Mobil: ser ut som en ekte meldingsapp")
def s10():
    F = "-apple-system, 'Segoe UI', system-ui, sans-serif"
    def t(x, y, s, size, fill="#111", w=400, a="start"):
        return f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
    b = ['<rect width="390" height="844" fill="#FFFFFF"/>', phone_status()]
    b.append(t(20, 74, "‹ Spill", 17, "#0066CC", 400) + t(366, 74, "Rediger", 17, "#0066CC", 400, "end"))
    b.append(t(20, 124, "Meldinger", 34, "#111", 700))
    b.append('<rect x="16" y="140" width="358" height="38" rx="11" fill="#EFEFF4"/>' + t(44, 165, "Søk", 16, "#6C6C70"))
    b.append('<circle cx="32" cy="159" r="6" fill="none" stroke="#6C6C70" stroke-width="2"/>')
    rows = [("Emma", "Konsert på fredag, blir du med?", "nå", True, "#FF9BC2", "E"),
            ("Banken", "Du har passert 3/4 av sparemålet ditt.", "nå", True, "#2FE3D2", "B"),
            ("Butikken – Sjefen", "Kan du ta ekstravakter ut desember?", "sep.", False, "#FFC24A", "S"),
            ("Mamma", "Forsikringen på mopeden går i januar.", "aug.", False, "#B4E86E", "M"),
            ("Jonas", "Gaming i kveld?", "jul.", False, "#7A4BD6", "J")]
    for i, (n, msg, when, new, col, L) in enumerate(rows):
        y = 194 + i * 84
        if new:
            b.append(f'<circle cx="12" cy="{y+34}" r="5.5" fill="#0066CC"/>')
        b.append(f'<circle cx="52" cy="{y+34}" r="26" fill="{col}"/>' + t(52, y + 42, L, 22, "#170A40", 700, "middle"))
        b.append(t(92, y + 26, n, 17, "#111", 700) + t(366, y + 26, when, 15, "#6C6C70", 400, "end"))
        b.append(t(92, y + 48, msg, 15, "#6C6C70"))
        b.append(f'<path d="M92 {y+80}H390" stroke="#E5E5EA"/>')
    b.append('<rect x="0" y="780" width="390" height="64" fill="#F7F7F9"/><path d="M0 780H390" stroke="#E5E5EA"/>')
    b.append(t(195, 806, "Meldinger fra denne måneden er merket med blå prikk.", 12.5, "#6C6C70", 400, "middle"))
    b.append('<rect x="140" y="828" width="110" height="4" rx="2" fill="#111"/>')
    return b, "#FFFFFF"


@screen("11-mobil-samtale", "Mobil: samtalen med Emma, invitasjonen legges i planen")
def s11():
    F = "-apple-system, 'Segoe UI', system-ui, sans-serif"
    def t(x, y, s, size, fill="#111", w=400, a="start"):
        return f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'
    b = ['<rect width="390" height="844" fill="#FFFFFF"/>', phone_status()]
    b.append('<rect x="0" y="44" width="390" height="96" fill="#F7F7F9"/><path d="M0 140H390" stroke="#E5E5EA"/>')
    b.append(t(20, 78, "‹", 30, "#0066CC", 400))
    b.append('<circle cx="195" cy="80" r="24" fill="#FF9BC2"/>' + t(195, 88, "E", 20, "#170A40", 700, "middle") + t(195, 126, "Emma ›", 13, "#111", 500, "middle"))
    b.append(t(195, 172, "Oktober", 12, "#6C6C70", 500, "middle"))
    b.append('<rect x="16" y="184" width="250" height="40" rx="20" fill="#E9E9EB"/>' + t(32, 209, "Gjengen leier hytte i høstferien!", 15.5))
    b.append('<path d="M290 236 h84 v40 h-84 a20 20 0 0 1 0 -40z" fill="#0066CC" opacity="0"/>')
    b.append(t(195, 262, "I dag", 12, "#6C6C70", 500, "middle"))
    b.append('<rect x="16" y="274" width="276" height="62" rx="20" fill="#E9E9EB"/>' + t(32, 299, "Konsert på fredag, blir du med?", 15.5) + t(32, 321, "Billetten er 400 kr", 15.5))
    # invitasjonen som et spillkort festet til meldingen
    b.append('<g filter="url(#sh)"><rect x="16" y="350" width="300" height="150" rx="22" fill="#170A40"/></g>')
    b.append(f'<rect x="16" y="350" width="300" height="6" rx="3" fill="{LIME}"/>')
    b.append(f'<g transform="translate(46 392)" fill="none" stroke="{LIME}" stroke-width="2.6" stroke-linecap="round"><path d="M-6 8V-10l14-4v18"/><circle cx="-10" cy="8" r="4.5"/><circle cx="4" cy="4" r="4.5"/></g>')
    b.append(T(74, 388, "Invitasjon: Konsert", 16, "#fff", 900) + T(74, 408, "1 kveld · 400 kr · bare i november", 12.5, SOFT, 500))
    b.append(primary(428, "LEGG I PLANEN", x=30, w=272, h=50))
    b.append(t(195, 528, "Levert", 11.5, "#6C6C70", 500, "middle"))
    b.append('<rect x="0" y="752" width="390" height="92" fill="#F7F7F9"/><path d="M0 752H390" stroke="#E5E5EA"/>')
    b.append('<rect x="16" y="766" width="358" height="38" rx="19" fill="#fff" stroke="#D1D1D6"/>' + t(34, 791, "Du kan ikke svare i spillet", 15, "#6C6C70"))
    b.append('<rect x="140" y="828" width="110" height="4" rx="2" fill="#111"/>')
    return b, "#FFFFFF"


# ------------------------------------------------------------------ 12-14 hendelse
def event_scene():
    veien2.SEGS = EV_SEGS
    b = [landscape()]
    cx, cy, ck = at(.55)
    b.append(cabin(cx + 46, cy - 64, False))
    x, y, k = at(.22)
    b.append(person(x - 34, y + 4, .95, face=1))
    ex, ey, ek = at(.34)
    b.append(person(ex + 22, ey + 8, .88, wave=True, **EMMA))
    b.append(bubble(ex - 96, ey - 176, ["Blir du med", "på hyttetur?"], "right"))
    veien2.SEGS = HUB_SEGS
    return b


def event_dialog(disabled=False):
    y0 = 528
    b = [dialog(y0, 300, who=portrait(48, y0 + 2, 24, **EMMA))]
    b.append(T(82, y0 + 28, "Emma", 15, "#fff", 900) + T(132, y0 + 28, "til deg og gjengen", 12, SOFT, 500))
    b.append(T(28, y0 + 62, "Hyttetur i høstferien", 22, "#fff", 900))
    b.append(T(28, y0 + 84, "Tre dager på hytta. 1 800 kr per person med mat.", 13, SOFT, 400))
    b.append(T(28, y0 + 104, "Brukskonto 4 220 kr · Sparing 18 750 kr · Gjeld 0 kr", 12.5, "#fff", 600))
    for i, (l, p) in enumerate([("Bli med og betal alt", "1 800 kr"), ("Bli med, ta med egen mat", "1 100 kr"), ("Stå over denne gangen", "0 kr")]):
        b.append(f'<g opacity="{.4 if disabled else 1}">{chunky(28, y0 + 118 + i * 56, 334, 46, l, p)}</g>')
    b.append(T(195, y0 + 292, "Trivselseffekten ser du etter at du har valgt.", 11.5, SOFT, 500, "middle"))
    return b


@screen("12-hendelse", "Hendelse som dialogboks på veien")
def s12():
    b = event_scene()
    b.append(hud2("Oktober", 17, 3, 9, 9, stats=False, sub="År 3 av 5 · noen venter på veien"))
    b += event_dialog()
    return b


@screen("13-resultat", "Resultat: tallene svever over figurene")
def s13():
    veien2.SEGS = EV_SEGS
    b = [landscape()]
    sx, sy, sk = at(.3)
    path = f"M{sx:.0f} {sy:.0f} C{sx+60:.0f} {sy-10:.0f} {sx+90:.0f} {sy-50:.0f} {sx+120:.0f} {sy-74:.0f}"
    b.append(f'<path d="{path}" stroke="{LIME}" stroke-width="22" fill="none" stroke-linecap="round" opacity=".35" filter="url(#glow)"/><path d="{path}" stroke="{LIME}" stroke-width="12" fill="none" stroke-linecap="round"/>')
    b.append(cabin(sx + 96, sy - 136, True))
    b.append(burst(sx + 60, sy - 110, 74, 90, LIME, 14))
    b.append(person(sx + 40, sy - 52, .82, face=1, wave=True))
    b.append(person(sx + 74, sy - 56, .8, **EMMA))
    b.append(float_tag(sx + 10, sy - 196, "+6 sosialt", LIME))
    b.append(float_tag(sx - 30, sy - 154, "−3 stress", C["road"]))
    b.append(float_tag(sx + 118, sy - 230, "−1 100 kr", C["sun"]))
    veien2.SEGS = HUB_SEGS
    b.append(hud2("Oktober", 17, 3, 9, 9, stats=False, sub="Hyttetur · du tok med egen mat"))
    y0 = 500
    b.append(dialog(y0, 324, stroke=LIME))
    b.append(T(28, y0 + 48, "−1 100 kr", 38, "#fff", 900) + T(362, y0 + 46, "igjen 3 120 kr", 13, SOFT, 600, "end"))
    b.append(heart(36, y0 + 82, 1.1) + T(54, y0 + 88, "Trivsel", 15, "#fff", 800) + T(362, y0 + 88, "61 → 64", 16, LIME, 900, "end"))
    b.append(wellbeing_bar(28, y0 + 100, 334, 64, new=1))
    ey = y0 + 122
    b.append(f'<rect x="28" y="{ey}" width="334" height="66" rx="14" fill="#2A1470"/>')
    b.append(f'<g fill="{LIME}"><ellipse cx="50" cy="{ey+24}" rx="5" ry="7.5" transform="rotate(-12 50 {ey+24})"/><ellipse cx="63" cy="{ey+44}" rx="5" ry="7.5" transform="rotate(-12 63 {ey+44})"/></g>')
    b.append(T(84, ey + 28, "Spor fra da du var 15", 14, LIME, 800) + T(84, ey + 48, "Du sparte pengegaven. Derfor hadde du råd.", 12.5, "#fff", 500))
    b.append(T(28, ey + 90, "Hvorfor?", 15, "#fff", 800, extra='text-decoration="underline"') + T(362, ey + 90, "Nytt på rommet: bilde fra hytta", 12, SOFT, 500, "end"))
    b.append(primary(ey + 108, "GÅ VIDERE", x=28, w=334, h=54))
    return b


@screen("14-hvorfor", "Hvorfor? forklarer endringen og peker på valget bak")
def s14():
    b = s13()
    b.append('<rect width="390" height="844" fill="#0B0426" opacity=".6"/>')
    y0 = 300
    b.append(f'<g filter="url(#sh)"><path d="M0 {y0+26} Q0 {y0} 26 {y0} H364 Q390 {y0} 390 {y0+26} V844 H0Z" fill="{PANEL}"/></g>')
    b.append(f'<rect x="170" y="{y0+10}" width="50" height="5" rx="2.5" fill="{LINE}"/>')
    b.append(T(24, y0 + 56, "Hvorfor?", 26, "#fff", 900))
    items = [("−1 100 kr", "Hytteturen, valget ditt i oktober.", "Egen mat gjorde turen 700 kr billigere."),
             ("Sosialt liv +6", "Tre dager med gjengen.", "Gjelder denne måneden."),
             ("Stress −3", "Fri fra jobben i høstferien.", "Gjelder denne måneden."),
             ("Ekko", "Du hadde råd fordi du sparte pengegaven", "i januar da du var 15.")]
    for i, (h, a, c) in enumerate(items):
        y = y0 + 96 + i * 82
        b.append(card(24, y, 342, 70))
        b.append(T(42, y + 28, h, 16, LIME if i < 3 else C["sun"], 900) + T(42, y + 48, a, 13.5, "#fff", 500) + T(42, y + 64, c, 12, SOFT, 400))
    b.append(f'<circle cx="34" cy="{y0+446}" r="10" fill="none" stroke="{SOFT}" stroke-width="2"/>' + T(34, y0 + 451, "i", 13, SOFT, 900, "middle") + T(52, y0 + 451, "Om tallene: hvordan spillet forenkler", 13, SOFT, 600, extra='text-decoration="underline"'))
    b.append(primary(y0 + 474, "LUKK", arrow=False))
    return b


# ------------------------------------------------------------------ 15-19 områdene
def sub_page(title, h=170):
    return [band(h), status(), topnav(title), sheet(h - 20)]


def slot(x, y, w, h, state, label=None, price=None, col=None):
    if state == "empty":
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="none" stroke="{LIME}" stroke-width="2" stroke-dasharray="6 5"/>'
                + T(x + w / 2, y + h / 2 + 6, "+ ledig", 14, LIME, 800, "middle"))
    if state == "work":
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#3A2580"/>'
                + T(x + w / 2, y + h / 2 - 2, "Ekstravakt", 13.5, SOFT, 800, "middle") + T(x + w / 2, y + h / 2 + 16, "ut desember", 11.5, SOFT, 500, "middle"))
    return (f'<rect x="{x}" y="{y+4}" width="{w}" height="{h}" rx="16" fill="#0B0426"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{col}"/>'
            + T(x + 14, y + 28, label, 14.5, INK, 900) + T(x + 14, y + 48, price, 13, INK, 700))


@screen("15-manedsplan", "Månedsplanen: fyll ledige kvelder ved å trykke, ikke dra")
def s15():
    b = sub_page("Kveldene i november")
    b.append(T(24, 194, "Skole og jobb (14 t/uke) tar resten av tiden.", 13.5, SOFT, 400))
    b.append(f'<rect x="24" y="210" width="210" height="34" rx="10" fill="#3A2580"/>' + T(129, 232, "Skole", 13.5, SOFT, 800, "middle"))
    b.append(f'<rect x="240" y="210" width="126" height="34" rx="10" fill="#3A2580"/>' + T(303, 232, "Jobb 14 t", 13.5, SOFT, 800, "middle"))
    b.append(T(24, 280, "3 ledige kvelder", 17, "#fff", 900) + T(366, 280, "Planlagt: 650 kr", 14, LIME, 800, "end"))
    b.append(slot(24, 296, 162, 70, "full", "Konsert", "400 kr · fra Emma", C["sun"]))
    b.append(slot(204, 296, 162, 70, "full", "Vennekveld", "250 kr", "#FF9BC2"))
    b.append(slot(24, 380, 162, 70, "empty"))
    b.append(slot(204, 380, 162, 70, "work"))
    b.append(divider(474))
    b.append(T(24, 504, "Trykk for å legge til", 14, SOFT, 600))
    acts = [("Hvilekveld", "0 kr", "stress ned"), ("Gaming", "0 kr", "kos hjemme"), ("Trening", "0 kr", "stress ned"), ("Kino", "150 kr", "med venner")]
    for i, (n, p, e) in enumerate(acts):
        y = 520 + i * 58
        b.append(card(24, y, 342, 48))
        b.append(T(42, y + 30, n, 15.5, "#fff", 700) + T(160, y + 30, e, 12.5, SOFT, 400) + T(320, y + 30, p, 14.5, LIME, 800, "end"))
        b.append(f'<circle cx="344" cy="{y+24}" r="11" fill="{LIME}"/><path d="M339 {y+24}h10M344 {y+19}v10" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>')
    b.append(secondary(756, "Samme som forrige måned", h=48))
    b.append(home_ind())
    return b


@screen("16-jobb", "Jobb: timer, lønn og ekstravakter")
def s16():
    b = sub_page("Jobben")
    b.append(card(24, 176, 342, 108))
    b.append(f'<circle cx="62" cy="216" r="22" fill="{C["sun"]}"/><g transform="translate(62 216)" fill="none" stroke="{INK}" stroke-width="2.4"><path d="M-10 -4h20v12h-20z M-4 -4v-4h8v4"/></g>')
    b.append(T(96, 210, "Butikkmedarbeider", 17, "#fff", 900) + T(96, 230, "Butikken i sentrum", 13, SOFT, 400))
    b.append(T(42, 266, "Lønn i november", 13.5, SOFT, 500) + T(348, 266, "7 242 kr", 18, LIME, 900, "end"))
    b.append(T(24, 322, "Timer per uke", 15, "#fff", 800))
    b.append(f'<rect x="24" y="334" width="342" height="64" rx="18" fill="{P2}" stroke="{LINE}" stroke-width="1.5"/>')
    b.append(f'<circle cx="60" cy="366" r="20" fill="#3A2580"/><path d="M52 366h16" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
    b.append(T(195, 374, "10 t", 26, "#fff", 900, "middle"))
    b.append(f'<circle cx="330" cy="366" r="20" fill="#3A2580"/><path d="M322 366h16M330 358v16" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
    b.append(T(24, 420, "Gjelder fra neste måned. Grensen er 40 t i uka.", 12.5, SOFT, 400))
    b.append(T(24, 462, "Ekstravakter (+4 t/uke ut desember)", 15, "#fff", 800))
    b.append(f'<rect x="24" y="476" width="342" height="104" rx="18" fill="{P2}" stroke="{LIME}" stroke-width="2.5"/>')
    b.append(f'<circle cx="50" cy="502" r="10" fill="{LIME}"/><circle cx="50" cy="502" r="4" fill="{INK}"/>' + T(70, 507, "Behold ekstravaktene", 15.5, "#fff", 800))
    b.append(T(70, 532, "+604 kr i måneden etter forbruk", 13, LIME, 700) + T(70, 554, "3 ledige kvelder i desember", 13, SOFT, 500))
    b.append(f'<rect x="24" y="592" width="342" height="80" rx="18" fill="{P2}" stroke="{LINE}" stroke-width="1.5"/>')
    b.append(f'<circle cx="50" cy="618" r="10" fill="none" stroke="{SOFT}" stroke-width="2"/>' + T(70, 623, "Avslutt fra desember", 15.5, "#fff", 700) + T(70, 648, "4 ledige kvelder i desember", 13, SOFT, 500))
    b.append(primary(700, "LAGRE"))
    b.append(T(195, 790, "Si opp jobben", 13.5, "#FFB3C9", 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


@screen("17-penger", "Penger: kontoer, sparemål og kommende kostnader")
def s17():
    b = sub_page("Pengene dine")
    accts = [("Brukskonto", "3 120 kr"), ("Sparekonto", "18 750 kr"), ("BSU", "0 kr")]
    for i, (n, v) in enumerate(accts):
        x = 24 + i * 116
        b.append(card(x, 176, 106, 78))
        b.append(T(x + 14, 202, n, 12.5, SOFT, 600) + T(x + 14, 232, v, 16, "#fff", 900))
    b.append(card(24, 268, 342, 120, stroke=LIME))
    b.append(f'<path d="M48 290v28" stroke="#fff" stroke-width="2.5"/><path d="M48 290h18l-5 6 5 6h-18z" fill="{LIME}"/>')
    b.append(T(78, 304, "Sparemål: Førerkort", 16, "#fff", 900) + T(348, 304, "75 %", 16, LIME, 900, "end"))
    b.append(seg_bar(42, 322, 306, 75, h=10))
    b.append(T(42, 360, "18 750 av 25 000 kr · åpner i januar", 13, SOFT, 500) + T(348, 378, "Bytt mål", 12.5, LIME, 700, "end", 'text-decoration="underline"'))
    b.append(T(24, 424, "Livsmål: spar til noe stort", 15, "#fff", 800) + T(366, 424, "19 %", 15, LIME, 900, "end"))
    b.append(seg_bar(24, 436, 342, 19, h=8))
    b.append(T(24, 466, "18 750 av 100 000 kr", 12.5, SOFT, 500))
    b.append(divider(486))
    b.append(T(24, 516, "Gjør noe med pengene", 15, "#fff", 800))
    acts = [("Flytt til sparekonto", "›"), ("Sett inn på BSU", "›"), ("Forbruk: normalt", "Endre ›")]
    for i, (n, r) in enumerate(acts):
        y = 530 + i * 54
        b.append(card(24, y, 342, 44))
        b.append(T(42, y + 28, n, 15, "#fff", 600) + T(348, y + 28, r, 14, LIME, 800, "end"))
    b.append(divider(704))
    b.append(T(24, 732, "Neste måned", 15, "#fff", 800) + T(366, 732, "1 340 kr faste kostnader", 13.5, SOFT, 600, "end"))
    b.append(T(24, 760, "Brukt på aktiviteter i år", 13.5, SOFT, 500) + T(366, 760, "4 850 kr", 13.5, "#fff", 800, "end"))
    b.append(home_ind())
    return b


def room(x0, y0, w, h):
    o = [f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="22" fill="#2A1470"/>',
         f'<rect x="{x0}" y="{y0+h*0.72}" width="{w}" height="{h*0.28}" rx="0" fill="#20105A"/>',
         f'<rect x="{x0+w-120}" y="{y0+28}" width="90" height="100" rx="8" fill="url(#sky)"/><path d="M{x0+w-75} {y0+28}v100M{x0+w-120} {y0+78}h90" stroke="#2A1470" stroke-width="5"/>',
         f'<rect x="{x0+24}" y="{y0+40}" width="70" height="52" rx="4" fill="#fff"/><rect x="{x0+29}" y="{y0+45}" width="60" height="42" fill="url(#sky)"/>',
         f'<path d="M{x0+29} {y0+87} l18 -14 12 8 14 -10 16 16z" fill="{C["near"]}"/><rect x="{x0+60}" y="{y0+70}" width="12" height="10" fill="{C["front"]}"/><rect x="{x0+63}" y="{y0+73}" width="4" height="4" fill="{C["sun"]}"/>',
         f'<rect x="{x0+20}" y="{y0+h*0.6}" width="150" height="46" rx="12" fill="#5B44B8"/><rect x="{x0+20}" y="{y0+h*0.6-18}" width="46" height="24" rx="8" fill="#E9E2FF"/>',
         f'<rect x="{x0+w-150}" y="{y0+h*0.6}" width="120" height="10" rx="3" fill="#5B44B8"/><rect x="{x0+w-140}" y="{y0+h*0.6+10}" width="7" height="44" fill="#5B44B8"/><rect x="{x0+w-46}" y="{y0+h*0.6+10}" width="7" height="44" fill="#5B44B8"/>',
         f'<rect x="{x0+w-118}" y="{y0+h*0.6-34}" width="46" height="32" rx="4" fill="#12053A"/><rect x="{x0+w-114}" y="{y0+h*0.6-30}" width="38" height="24" rx="2" fill="{C["road"]}" opacity=".7"/>',
         f'<ellipse cx="{x0+w-62}" cy="{y0+h*0.6-12}" rx="16" ry="12" fill="{PRESS}"/><rect x="{x0+w-76}" y="{y0+h*0.6-14}" width="28" height="5" fill="#12053A" opacity=".5"/>']
    return "".join(o)


@screen("18-rommet-trivsel", "Rommet ditt og trivselen: alt som bilde finnes også som tekst")
def s18():
    b = sub_page("Rommet ditt")
    b.append(room(24, 172, 342, 230))
    b.append(T(24, 428, "Nytt: bilde fra hytteturen og hjelmen til mopeden.", 12.5, SOFT, 400))
    b.append(heart(32, 470, 1.2) + T(52, 476, "Trivsel", 18, "#fff", 900) + T(366, 476, "64", 22, LIME, 900, "end"))
    b.append(seg_bar(24, 490, 342, 64, h=12, thr=50))
    b.append(T(24, 522, "Grensen for ekte seier er 50. Snittet ditt så langt: 58.", 12.5, SOFT, 400))
    parts = [("Stress", 38, "lavere er bedre", PRESS), ("Fritid", 72, "følger skole og jobb", C["road"]), ("Sosialt liv", 58, "vanlig 52 · +6 denne måneden", LIME)]
    for i, (n, v, s, col) in enumerate(parts):
        y = 560 + i * 66
        b.append(T(24, y, n, 15, "#fff", 800) + T(366, y, str(v), 15, "#fff", 900, "end"))
        b.append(seg_bar(24, y + 12, 342, v, color=col, h=8))
        b.append(T(24, y + 40, s, 12, SOFT, 400))
    b.append(home_ind())
    return b


@screen("19-arslinje", "Årslinjen: januar til desember, år 1 til 5")
def s19():
    b = sub_page("Året ditt", h=150)
    for i in range(5):
        x = 24 + i * 70
        sel = i == 2
        done = i < 2
        b.append(f'<rect x="{x}" y="160" width="62" height="54" rx="14" fill="{LIME if sel else P2}" stroke="{LIME if sel else LINE}" stroke-width="1.5" opacity="{1 if (sel or done) else .55}"/>')
        b.append(T(x + 31, 182, f"År {i+1}", 13, INK if sel else "#fff", 900, "middle") + T(x + 31, 202, f"{15+i} år", 11.5, INK if sel else SOFT, 600, "middle"))
    events = {0: "Ny mobil? Du ventet", 3: "Bursdag: 1 000 kr fra bestemor", 5: "Tilbud om sommerjobb", 6: "Sommerjobb i butikken",
              8: "Sjefen: ekstravakter", 9: "Hyttetur med gjengen", 10: "Du er her", 11: "Siste måned med ekstravakter"}
    y0, step = 248, 44
    b.append(f'<path d="M48 {y0} V{y0+step*11}" stroke="#3A2580" stroke-width="6" stroke-linecap="round"/>')
    b.append(f'<path d="M48 {y0} V{y0+step*10}" stroke="{C["road"]}" stroke-width="6" stroke-linecap="round"/>')
    for i, m in enumerate(MONTHS):
        y = y0 + i * step
        active = i in (0, 3, 6, 9)
        if i == 10:
            b.append(f'<circle cx="48" cy="{y}" r="13" fill="{LIME}" stroke="#12053A" stroke-width="3"/>')
            b.append(f'<rect x="76" y="{y-17}" width="290" height="34" rx="12" fill="{P2}" stroke="{LIME}" stroke-width="2"/>')
        elif i < 10:
            b.append(f'<circle cx="48" cy="{y}" r="{9 if active else 6}" fill="{C["road"] if not active else "#fff"}" stroke="#12053A" stroke-width="2"/>')
        else:
            b.append(f'<circle cx="48" cy="{y}" r="{9 if active else 6}" fill="#12053A" stroke="#5B44B8" stroke-width="2"/>')
        b.append(T(88, y + 5, m, 14.5, "#fff" if i <= 10 else SOFT, 800 if i == 10 else 600))
        if i in events:
            b.append(T(184, y + 5, events[i], 12.5, LIME if i == 10 else SOFT, 700 if i == 10 else 400))
    b.append(f'<circle cx="34" cy="{y0+step*11+40}" r="7" fill="#fff"/>' + T(48, y0 + step * 11 + 45, "= måned med hendelse", 12, SOFT, 500))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 20-22 varsler, krise, kjørespill
def dark_scene(segs=None, tint=PRESS):
    veien2.SEGS = segs or EV_SEGS
    b = [landscape(sun=False)]
    b.append(f'<rect width="390" height="844" fill="{tint}" opacity=".10"/>')
    veien2.SEGS = HUB_SEGS
    return b


@screen("20-kortvarsel", "Kortvarsel: konsekvensen i kroner, uten kjeft")
def s20():
    b = dark_scene()
    veien2.SEGS = EV_SEGS
    x, y, k = at(.5)
    y -= 4
    b.append(person(x - 10, y + 6, .95, face=1, top="#3A6FE0", top2="#2851A8"))
    b.append(f'<g transform="translate({x+40} {y-120})"><rect x="-34" y="-22" width="68" height="44" rx="8" fill="{PRESS}"/><rect x="-34" y="-12" width="68" height="8" fill="#12053A" opacity=".5"/><rect x="-26" y="6" width="22" height="6" rx="2" fill="#fff" opacity=".7"/></g>')
    b.append(float_tag(x + 40, y - 170, "10 000 kr gjeld", PRESS))
    veien2.SEGS = HUB_SEGS
    b.append(hud2("Mars", 18, 4, 2, 2, stats=False, sub="År 4 av 5 · kortet ditt"))
    y0 = 400
    b.append(dialog(y0, 424, stroke=PRESS, accent=PRESS))
    b.append(T(28, y0 + 44, "Renta på kortet har startet", 21, "#fff", 900))
    b.append(T(28, y0 + 68, "Kortet er fullt, og du fikk ikke betalt hele regningen.", 13, SOFT, 400))
    rows = [("Rente i år", "22,6 %"), ("Renter denne måneden", "188 kr"), ("Betaler du bare minstebeløpet", "51 måneder"), ("Renter totalt da", "5 508 kr")]
    for i, (l, r) in enumerate(rows):
        yy = y0 + 104 + i * 30
        b.append(T(28, yy, l, 14, "#fff", 500) + T(362, yy, r, 15, "#FFB3C9" if i else "#fff", 900, "end"))
    b.append(divider(y0 + 206, 28, 334))
    for i, (l, p) in enumerate([("Slå av kortbruk", "0 kr"), ("Ta ekstravakter", "+ timer"), ("Snakk med familien", "kanskje hjelp")]):
        b.append(chunky(28, y0 + 222 + i * 56, 334, 46, l, p))
    b.append(T(195, y0 + 408, "Ingenting skjer før du velger. Du kan også la det være.", 11.5, SOFT, 500, "middle"))
    return b


@screen("21-krisemaned", "Krisemåned: opptil tre steg, alltid en vei ut")
def s21():
    b = dark_scene()
    veien2.SEGS = EV_SEGS
    x, y, k = at(.5)
    b.append(f'<path d="M40 250 L120 220 L110 260 L190 240" stroke="{PRESS}" stroke-width="5" fill="none" opacity=".7"/>')
    b.append(person(x + 10, y + 2, .95, face=1, top="#3A6FE0", top2="#2851A8"))
    veien2.SEGS = HUB_SEGS
    b.append(hud2("Mai", 18, 4, 4, 4, stats=False, sub="År 4 av 5 · krisemåned"))
    b.append(f'<g filter="url(#sh)"><rect x="20" y="124" width="200" height="34" rx="17" fill="{PRESS}"/></g>' + T(120, 146, "STEG 1 AV 3", 13, INK, 900, "middle", 'letter-spacing="1.5"'))
    y0 = 400
    b.append(dialog(y0, 424, stroke=PRESS, accent=PRESS))
    b.append(T(28, y0 + 44, "Brukskontoen er under 0 kr", 21, "#fff", 900))
    b.append(T(28, y0 + 68, "Du mangler 1 640 kr. Hva gjør du først?", 13.5, SOFT, 400))
    opts = [("Selg mopeden", "+8 152 kr", "neste måned: buss igjen"), ("Ta ekstravakter", "neste mnd", None),
            ("Senk forbruket", "neste mnd", None), ("Spør familien", "kanskje hjelp", None), ("Ignorer krisen", "gjelda vokser", None)]
    for i, (l, p, s) in enumerate(opts):
        b.append(chunky(28, y0 + 88 + i * 56, 334, 46, l, p))
    b.append(T(195, y0 + 404, "Krisen tar slutt når kontoen er over 0, eller etter tre steg.", 11.5, SOFT, 500, "middle"))
    return b


@screen("22-kjorespill", "Kjørespill for mopedførerkort: turbasert, ingen tidspress")
def s22():
    b = [band(150), status(), topnav("Kjøretimen", back=False), sheet(130)]
    b.append(T(24, 172, "Situasjon 3 av 6", 13.5, LIME, 800) + T(366, 172, "Moped · 16 år", 13, SOFT, 600, "end"))
    for i in range(6):
        b.append(f'<rect x="{24+i*58}" y="182" width="52" height="6" rx="3" fill="{LIME if i < 2 else ("#fff" if i == 2 else "#3A2580")}"/>')
    # kryss sett ovenfra
    X0, Y0 = 24, 204
    b.append(f'<rect x="{X0}" y="{Y0}" width="342" height="300" rx="22" fill="#2E7D4F"/>')
    b.append(f'<rect x="{X0+126}" y="{Y0}" width="90" height="300" fill="#1F2230"/><rect x="{X0}" y="{Y0+105}" width="342" height="90" fill="#1F2230"/>')
    b.append(f'<path d="M{X0+171} {Y0}v100 M{X0+171} {Y0+200}v100 M{X0} {Y0+150}h120 M{X0+222} {Y0+150}h120" stroke="#fff" stroke-width="3" stroke-dasharray="12 10"/>')
    b.append(f'<g transform="translate({X0+192} {Y0+252})"><rect x="-9" y="-20" width="18" height="40" rx="8" fill="{C["road"]}"/><circle cy="-6" r="6" fill="{LIME}"/></g>')
    b.append(f'<path d="M{X0+192} {Y0+222} C{X0+192} {Y0+170} {X0+170} {Y0+150} {X0+120} {Y0+140}" stroke="{LIME}" stroke-width="4" fill="none" stroke-dasharray="6 6"/><path d="M{X0+128} {Y0+132}l-10 8 12 4" fill="none" stroke="{LIME}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(f'<g transform="translate({X0+150} {Y0+50})"><rect x="-13" y="-24" width="26" height="48" rx="8" fill="{C["sun"]}"/><rect x="-9" y="-14" width="18" height="10" rx="3" fill="#12053A" opacity=".6"/></g>')
    b.append(f'<path d="M{X0+150} {Y0+80}v20" stroke="{C["sun"]}" stroke-width="3" stroke-dasharray="4 4"/>')
    b.append(T(24, 538, "Du skal svinge til venstre.", 18, "#fff", 900))
    b.append(T(24, 562, "En bil kommer mot deg og skal rett frem.", 14, SOFT, 400))
    for i, l in enumerate(["Kjør først, du er raskest", "Vent til bilen har kjørt forbi", "Tut og sving"]):
        b.append(chunky(24, 584 + i * 60, 342, 50, l, ""))
    b.append(T(195, 784, "Ingen klokke. Ta den tiden du trenger.", 12.5, SOFT, 500, "middle"))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 23-25 år, retur, slutt
@screen("23-arsslutt", "Året er ferdig: årslinjen fylt, teaser for neste år")
def s23():
    veien2.SEGS = HUB_SEGS
    b = [landscape()]
    gx, gy, gk = at(.42)
    b.append(age_gate(.42, 18, None))
    x, y, k = at(.24)
    b.append(person(x, y + 6, 1.05, face=1, wave=True))
    b.append(burst(gx, gy - 90, 70, 86, LIME, 16))
    b.append(status())
    b.append(T(195, 100, "År 3 er ferdig!", 32, "#fff", 900, "middle"))
    b.append(T(195, 128, "Du er 17, og snart kommer nivå 18.", 15, "#E9E2FF", 600, "middle"))
    y0 = 470
    b.append(dialog(y0, 354, stroke=LIME))
    b.append(year_line_compact(44, y0 + 40, 302, 12, 12))
    b.append(T(28, y0 + 96, "Spart i år", 13.5, SOFT, 500) + T(362, y0 + 96, "+9 400 kr", 16, LIME, 900, "end"))
    b.append(T(28, y0 + 124, "Trivsel i snitt", 13.5, SOFT, 500) + T(362, y0 + 124, "61", 16, "#fff", 900, "end"))
    b.append(divider(y0 + 144, 28, 334))
    b.append(T(28, y0 + 174, "Neste år", 15, C["sun"], 900))
    b.append(T(28, y0 + 198, "Du fyller 18. Bilførerkort og kredittkort åpner.", 13.5, "#fff", 500))
    b.append(T(28, y0 + 220, "Et valg du tok i fjor kan også komme tilbake …", 13.5, SOFT, 400))
    b.append(primary(y0 + 244, "START ÅR 4", x=28, w=334, h=54))
    b.append(T(195, y0 + 336, "Alt er lagret. Du kan ta pause nå.", 12.5, SOFT, 500, "middle"))
    return b


@screen("24-velkommen-tilbake", "Velkommen tilbake: kort oppsummering etter pause")
def s24():
    b = hub_scene()
    b.append(f'<rect width="390" height="844" fill="#0B0426" opacity=".55"/>')
    b.append(status())
    y0 = 180
    b.append(f'<g filter="url(#sh)"><rect x="20" y="{y0}" width="350" height="470" rx="26" fill="{PANEL}" stroke="{LIME}" stroke-width="2"/></g>')
    b.append(portrait(195, y0, 34, face=1))
    b.append(T(195, y0 + 66, "Velkommen tilbake!", 24, "#fff", 900, "middle"))
    b.append(T(195, y0 + 92, "Du er i november. 17 år, år 3 av 5.", 14, SOFT, 500, "middle"))
    b.append(year_line_compact(52, y0 + 128, 286, 10, 10))
    b.append(card(40, y0 + 168, 310, 110))
    b.append(coin(64, y0 + 198, 10) + T(82, y0 + 204, "3 120 kr på brukskontoen", 14.5, "#fff", 700))
    b.append(f'<rect x="56" y="{y0+222}" width="16" height="22" rx="4" fill="none" stroke="#fff" stroke-width="2"/>' + T(82, y0 + 238, "2 meldinger kom denne måneden", 14.5, "#fff", 700))
    b.append(T(64, y0 + 266, "Planlagt: konsert og vennekveld", 13, SOFT, 500))
    b.append(T(195, y0 + 314, "Neste år kan du ta bilførerkort.", 14, C["sun"], 800, "middle"))
    b.append(T(195, y0 + 336, "Det koster rundt 25 000 kr.", 13, SOFT, 500, "middle"))
    b.append(primary(y0 + 374, "FORTSETT", x=40, w=310, h=54))
    return b


@screen("25-slutt", "Slutten: hvordan livet gikk, og de tre valgene som betydde mest")
def s25():
    b = [band(250), status()]
    b.append(burst(195, 150, 64, 82, LIME, 18))
    b.append(f'<g transform="translate(195 150)"><path d="M-30 -40h60v26a30 30 0 0 1 -60 0z" fill="{C["sun"]}"/><path d="M-30 -32h-14a14 14 0 0 0 14 22 M30 -32h14a14 14 0 0 1 -14 22" fill="none" stroke="{C["sun"]}" stroke-width="5"/><rect x="-6" y="14" width="12" height="16" fill="{C["sun"]}"/><rect x="-20" y="30" width="40" height="8" rx="3" fill="{C["sun"]}"/></g>')
    b.append(sheet(226))
    b.append(T(195, 276, "Ekte seier!", 32, "#fff", 900, "middle"))
    b.append(T(195, 302, "Du fylte 20, nådde målet og hadde det bra underveis.", 13.5, SOFT, 500, "middle"))
    b.append(card(24, 322, 166, 76) + T(40, 348, "Spart", 12.5, SOFT, 600) + T(40, 380, "104 300 kr", 19, LIME, 900))
    b.append(card(200, 322, 166, 76) + T(216, 348, "Trivsel i snitt", 12.5, SOFT, 600) + T(216, 380, "58 av 100", 19, "#fff", 900))
    b.append(T(24, 432, "Valgene som betydde mest", 16, "#fff", 900))
    top3 = [("Sparte pengegaven", "15 år · januar", "+17 270 kr"), ("Kortet som debetkort", "18 år", "−5 508 kr"), ("Konserter", "5 år samlet", "−2 600 kr")]
    for i, (n, w, v) in enumerate(top3):
        y = 446 + i * 74
        b.append(card(24, y, 342, 64))
        b.append(f'<circle cx="50" cy="{y+32}" r="15" fill="{LIME if i == 0 else "#3A2580"}"/>' + T(50, y + 37, str(i + 1), 14, INK if i == 0 else "#fff", 900, "middle"))
        b.append(T(76, y + 28, n, 15, "#fff", 800) + T(76, y + 48, w, 12.5, SOFT, 500) + T(330, y + 37, v, 15, LIME if v.startswith("+") else "#FFB3C9", 900, "end"))
        b.append(f'<path d="M344 {y+26}l6 6-6 6" fill="none" stroke="{SOFT}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(primary(686, "SPILL IGJEN FRA 15"))
    b.append(T(195, 786, "Nytt mål, ny pengegave, nytt liv.", 12.5, SOFT, 500, "middle"))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 26-28 meny, om tallene, frakoblet
@screen("26-meny", "Meny: konto, personvern og nytt liv")
def s26():
    b = sub_page("Meny")
    groups = [("Spillet", [("Året ditt", "›"), ("Rommet ditt", "›"), ("Om tallene", "›"), ("Start et nytt liv", "›")]),
              ("Kontoen", [("Bytt passord", "›"), ("Spillerinformasjon", "›"), ("Logg ut", "›"), ("Logg ut på alle enheter", "›")])]
    y = 186
    for g, items in groups:
        b.append(T(24, y, g, 13, SOFT, 800, extra='letter-spacing="1"'))
        y += 12
        b.append(card(24, y, 342, 52 * len(items)))
        for i, (n, r) in enumerate(items):
            yy = y + 33 + i * 52
            b.append(T(42, yy, n, 15.5, "#fff", 600) + T(348, yy, r, 18, SOFT, 600, "end"))
            if i < len(items) - 1:
                b.append(divider(y + 52 * (i + 1), 42, 324))
        y += 52 * len(items) + 34
    b.append(secondary(y - 6, "Slett kontoen", col="#FFB3C9"))
    b.append(T(195, y + 70, "Sletting krever passordet og kan ikke angres.", 12, SOFT, 500, "middle"))
    b.append(home_ind())
    return b


@screen("27-om-tallene", "Om tallene: hvor spillet forenkler virkeligheten")
def s27():
    b = sub_page("Om tallene")
    b.append(T(24, 190, "Spillet bruker ekte norske tall fra 2026, men", 13.5, SOFT, 400))
    b.append(T(24, 210, "forenkler noen ting. Her står alt samlet.", 13.5, SOFT, 400))
    items = [("Lønn", "Alle jobber gir samme timelønn for alderen."),
             ("Skatt", "Skatt regnes på årslønna, uten andre fradrag."),
             ("Renter", "Renter regnes én gang i måneden, i hele kroner."),
             ("Kveldene", "Måneden har ledige kvelder, ikke dager."),
             ("Mopeden", "Verdien faller litt hver måned, uansett kjøring.")]
    for i, (h, t) in enumerate(items):
        y = 232 + i * 88
        b.append(card(24, y, 342, 76))
        b.append(f'<circle cx="48" cy="{y+28}" r="11" fill="none" stroke="{LIME}" stroke-width="2"/>' + T(48, y + 33, "i", 13, LIME, 900, "middle"))
        b.append(T(70, y + 33, h, 15.5, "#fff", 800) + T(42, y + 58, t, 12.5, SOFT, 400))
    b.append(T(195, 692, "Første gang en forenkling dukker opp i spillet,", 12.5, SOFT, 500, "middle"))
    b.append(T(195, 710, "vises den bak et i-symbol.", 12.5, SOFT, 500, "middle"))
    b.append(home_ind())
    return b


@screen("28-frakoblet", "Frakoblet: skjermen kan leses, valgene er låst")
def s28():
    b = event_scene()
    b.append(hud2("Oktober", 17, 3, 9, 9, stats=False, sub="År 3 av 5 · noen venter på veien"))
    b += event_dialog(disabled=True)
    b.append(f'<g filter="url(#sh)"><rect x="20" y="460" width="350" height="52" rx="16" fill="#FFFFFF"/></g>')
    b.append(f'<g transform="translate(46 486)" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"><path d="M-12 -2a17 17 0 0 1 24 0M-7 3a10 10 0 0 1 14 0"/><circle cx="0" cy="8" r="2" fill="{INK}"/><path d="M-13 -11L13 13" stroke="{PRESS}"/></g>')
    b.append(T(72, 482, "Du er frakoblet", 15, INK, 900) + T(72, 500, "Valgene låses opp når nettet er tilbake.", 12.5, "#4A3D7A", 500))
    return b


# ------------------------------------------------------------------ skriv filer
def render(name):
    title, fn = SCREENS[name]
    res = fn()
    bg = None
    if isinstance(res, tuple):
        res, bg = res
    svg = page(f"Veien: {title}", "\n".join(res))
    if bg:
        svg = svg.replace('<rect width="390" height="844" fill="#12053A"/>', f'<rect width="390" height="844" fill="{bg}"/>', 1)
    with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
        f.write(svg)


if __name__ == "__main__":
    only = sys.argv[1:]
    for name in SCREENS:
        if only and not any(name.startswith(o) for o in only):
            continue
        render(name)
        print(name)
