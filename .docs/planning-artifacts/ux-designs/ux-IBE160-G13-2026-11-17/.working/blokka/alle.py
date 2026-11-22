# «Blokka» (Fjord): alle skjermene i appen. Kjør: python alle.py [nummer ...]
# Tallene er eksempeldata fra PRD-ens brukerreiser (UJ-1 til UJ-6), ikke motorberegninger.
import os, sys, math
import skjermer as S
from skjermer import (apply_palette, building, open_room, corridor, month_strip, wall_note, side_note,
                      bubble, ME, EMMA, W, D, WOOD, WALL, YEAR_COL, ground, shopfront, closed_floor)
from blokka import K, T, page, topbar, doorbells, option, window_meter, status, floor_display
from iso import Iso, shade
from folk import person

apply_palette("fjord")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "skjermer")
os.makedirs(OUT, exist_ok=True)
SCREENS = {}
MONTHS = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]
MAMMA = dict(skin="#EBC0A0", hair="#8A5A3C", top="#C25B6E", shirt="#F3F7F5", pants="#3B4A5C", shoes="#3B4A5C", style="long")
LOOKS = [ME,
         dict(skin="#C68E68", hair="#1D1B22", top="#6E9BC4", shirt="#F3F7F5", pants="#2C3E66", shoes="#FFFFFF", style="curly"),
         dict(skin="#F2CDB0", hair="#D9A55B", top="#8DAA7B", shirt="#FFFFFF", pants="#3D3456", shoes="#FFFFFF", style="short"),
         EMMA,
         dict(skin="#8D5B3E", hair="#1D1B22", top="#F0A24A", shirt="#FFFFFF", pants="#2C3E66", shoes="#FFFFFF", style="long"),
         dict(skin="#F5D3BA", hair="#B8572E", top="#1E5A6B", shirt="#E6D7B0", pants="#4A4A52", shoes="#FFFFFF", style="bun")]


def screen(name, title):
    def deco(fn):
        SCREENS[name] = (title, fn)
        return fn
    return deco


# ------------------------------------------------------------------ felles deler
def home_ind():
    return f'<rect x="140" y="832" width="110" height="4" rx="2" fill="{K["ink"]}" opacity=".5"/>'


def primary(y, label, x=20, w=350, h=54, arrow=True):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{K["cobalt"]}"/>' + T(x + 20, y + h / 2 + 6, label, 17, "#fff", 800)
    if arrow:
        o += f'<path d="M{x+w-34} {y+h/2}h16m-6-6 6 6-6 6" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>'
    return o


def secondary(y, label, x=20, w=350, h=50, col=None):
    col = col or K["cobalt"]
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" stroke="{col}" stroke-width="2"/>' + T(x + w / 2, y + h / 2 + 6, label, 16, col, 700, "middle")


def card(x, y, w, h, stroke=None, fill="#fff"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke or K["line"]}" stroke-width="1.5"/>'


def field(y, label, value, masked=False, error=None, x=20, w=350):
    o = [T(x, y, label, 13, K["soft"], 600)]
    o.append(f'<rect x="{x}" y="{y+8}" width="{w}" height="50" rx="8" fill="#fff" stroke="{K["press"] if error else "#7C8F8A"}" stroke-width="2"/>')
    if masked:
        o.append("".join(f'<circle cx="{x+20+i*14}" cy="{y+33}" r="4.5" fill="{K["ink"]}"/>' for i in range(value)))
    else:
        o.append(T(x + 16, y + 39, value, 16, K["ink"], 500))
    return "".join(o)


def checkbox(y, label, checked=False, x=20):
    o = f'<rect x="{x}" y="{y}" width="24" height="24" rx="5" fill="{K["cobalt"] if checked else "#fff"}" stroke="{K["cobalt"] if checked else "#7C8F8A"}" stroke-width="2"/>'
    if checked:
        o += f'<path d="M{x+6} {y+12}l4 4 8-9" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>'
    return o + T(x + 36, y + 17, label, 14.5, K["ink"], 500)


def divider(y, x=20, w=350):
    return f'<path d="M{x} {y}H{x+w}" stroke="{K["line"]}"/>'


def bar(x, y, w, val, col, h=8, thr=None):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#fff" stroke="#7C8F8A" stroke-width="1.2"/><rect x="{x}" y="{y}" width="{w*val/100:.0f}" height="{h}" rx="{h/2}" fill="{col}"/>'
    if thr is not None:
        o += f'<path d="M{x+w*thr/100:.0f} {y-5}v{h+10}" stroke="{K["ink"]}" stroke-width="2"/>'
    return o


def back_btn(y=62):
    return f'<circle cx="38" cy="{y}" r="19" fill="#fff" stroke="{K["line"]}" stroke-width="1.5"/><path d="M42 {y-7}l-7 7 7 7" fill="none" stroke="{K["ink"]}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'


def mini_block(x, y, k=.3, cur=3, lit_all=False):
    """Liten blokk som ikon, med etasjen din markert."""
    iso = Iso(x, y, k)
    o = [iso.box(0, 0, 0, W, D, 26, "#EEF1F5")]
    z = 26
    for yr in range(1, 6):
        col = YEAR_COL[yr]
        o.append(iso.box(0, 0, z, W, D, 22, col))
        lit = lit_all or yr < cur
        for i in range(5):
            o.append(iso.left(10 + i * 26, D, z + 6, 14, 10, "#FFD45C" if lit else "#5C6F8C"))
        if yr == cur and not lit_all:
            o.append(iso.left(0, D, z, W, 22, "none", f'stroke="{K["ink"]}" stroke-width="{8*k:.1f}"'))
        z += 22
    o.append(iso.box(-3, -3, z, W + 6, D + 6, 4, "#6E7F95"))
    return "".join(o)


def sub_page(title, back=True, h=150):
    """Undersider: lys himmel, en liten blokk i hjørnet, hvitt ark under."""
    o = [f'<rect width="390" height="{h+40}" fill="url(#sky)"/>', mini_block(332, 128, .24), status()]
    if back:
        o.append(back_btn())
    o.append(T(70 if back else 20, 72, title, 26, K["ink"], 900, extra='letter-spacing="-.5"'))
    o.append(f'<path d="M0 {h+14} Q0 {h-6} 20 {h-6} H370 Q390 {h-6} 390 {h+14} V844 H0Z" fill="{K["sky2"]}"/>')
    return "".join(o)


def dialog_card(y0, who_col, who_letter, who, sub, title, text):
    o = [f'<rect x="0" y="{y0-8}" width="390" height="{844-y0+8}" fill="{K["sky2"]}"/>',
         f'<rect x="20" y="{y0+6}" width="32" height="32" rx="6" fill="{who_col}"/>' + T(36, y0 + 28, who_letter, 15, "#fff", 800, "middle"),
         T(62, y0 + 19, who, 14.5, K["ink"], 800) + T(62, y0 + 35, sub, 12, K["soft"], 500),
         T(20, y0 + 76, title, 24, K["ink"], 900, extra='letter-spacing="-.5"'),
         T(20, y0 + 100, text, 14, K["soft"], 500)]
    return "".join(o)


def scene_clip(y0, y1, body):
    cid = f"sc{y0}{y1}"
    return f'<clipPath id="{cid}"><rect x="0" y="{y0}" width="390" height="{y1-y0}"/></clipPath><g clip-path="url(#{cid})">{body}</g>'


BELLS = [("Plan", "3 ledige kvelder"), ("Mobil", "2 nye meldinger"), ("Jobb", None), ("Penger", None)]


# ------------------------------------------------------------------ 01-04 innlogging
@screen("01-velkommen", "første skjerm: Logg inn eller Opprett bruker")
def s01():
    b = ['<rect width="390" height="844" fill="url(#sky)"/>', status()]
    iso = Iso(176, 520, .95)
    people = person(*iso.p(84, 52, 70), .95, ME, -1)
    b.append(building(iso, 3, people=people, goal="Livsmålet ditt"))
    b.append(person(*iso.p(60, D + 18, 0), 1.25, ME, -1, wave=True) + person(*iso.p(92, D + 14, 0), 1.25, EMMA, -1))
    b.append(T(20, 92, "LifeMode", 44, K["ink"], 900, extra='letter-spacing="-1.5"'))
    b.append(T(20, 122, "Fem år i blokka. Én etasje i året.", 16, K["soft"], 600))
    b.append(f'<rect x="0" y="626" width="390" height="218" fill="{K["sky2"]}"/>')
    b.append(primary(646, "Opprett bruker"))
    b.append(secondary(712, "Logg inn"))
    b.append(T(195, 796, "Glemt passord?", 14.5, K["cobalt"], 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


@screen("02-opprett-bruker", "opprett bruker med spillerinformasjon")
def s02():
    b = [sub_page("Opprett bruker")]
    b.append(field(186, "E-post", "markus@eksempel.no"))
    b.append(field(266, "Skriv e-posten en gang til", "markus@eksempel.no"))
    b.append(field(346, "Passord (minst 8 tegn)", 9, masked=True))
    b.append(checkbox(430, "Hold meg innlogget på denne enheten"))
    b.append(card(20, 474, 350, 168, fill=K["panel"]))
    b.append(T(38, 504, "Dette lagrer vi", 15, K["ink"], 800))
    for i, l in enumerate(["E-posten din, bare for innlogging og nytt passord.", "Spillet ditt, så du kan fortsette på andre enheter.", "Alt slettes etter 12 måneder uten spill.", "Du kan slette kontoen når du vil."]):
        b.append(f'<circle cx="42" cy="{530+i*24}" r="3" fill="{K["cobalt"]}"/>' + T(54, 534 + i * 24, l, 12.5, K["soft"], 500))
    b.append(T(38, 630, "Les hele spillerinformasjonen", 12.5, K["cobalt"], 700, extra='text-decoration="underline"'))
    b.append(primary(668, "Opprett bruker"))
    b.append(T(195, 768, "Har du bruker? Logg inn", 14, K["cobalt"], 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


@screen("03-logg-inn", "logg inn")
def s03():
    b = [sub_page("Logg inn")]
    b.append(field(196, "E-post", "markus@eksempel.no"))
    b.append(field(276, "Passord", 10, masked=True))
    b.append(checkbox(360, "Hold meg innlogget på denne enheten"))
    b.append(T(20, 414, "Delt PC, for eksempel på skolen? La boksen stå tom.", 12.5, K["soft"], 500))
    b.append(primary(444, "Logg inn"))
    b.append(T(195, 536, "Glemt passord?", 14.5, K["cobalt"], 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


@screen("04-glemt-passord", "glemt passord: samme svar uansett")
def s04():
    b = [sub_page("Glemt passord")]
    b.append(T(20, 190, "Skriv e-posten din, så sender vi en lenke.", 14.5, K["soft"], 500))
    b.append(field(216, "E-post", "markus@eksempel.no"))
    b.append(card(20, 304, 350, 110, stroke=K["cobalt"]))
    b.append(f'<circle cx="48" cy="336" r="13" fill="{K["cobalt"]}"/><path d="M42 336l4 4 8-9" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(T(72, 341, "Sjekk e-posten din", 16, K["ink"], 800))
    b.append(T(38, 374, "Hvis adressen har en bruker, får du en lenke.", 13, K["soft"], 500))
    b.append(T(38, 396, "Lenken virker én gang, i 60 minutter.", 13, K["soft"], 500))
    b.append(primary(440, "Send ny lenke", arrow=False))
    b.append(T(195, 532, "Tilbake til innlogging", 14.5, K["cobalt"], 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 05-07 start
GOALS = [("Spar til noe stort", "Minst 100 000 kr spart når du fyller 20.", "For eksempel en start på egen leilighet."),
         ("Gjeldfri med buffer", "Ingen gjeld, og minst 30 000 kr tilgjengelig", "hver måned det siste året."),
         ("Råd til en stor opplevelse", "Åtte uker Interrail for 60 000 kr, uten lån,", "innen august det siste året.")]


@screen("05-livsmal", "velg livsmålet som skal stå på taket")
def s05():
    b = [sub_page("Livsmålet ditt", back=False)]
    b.append(T(20, 186, "Målet står på taket av blokka og sjekkes når du fyller 20.", 13, K["soft"], 500))
    b.append(T(20, 204, "Du kan ikke bytte underveis.", 13, K["soft"], 500))
    for i, (t, l1, l2) in enumerate(GOALS):
        y = 224 + i * 128
        sel = i == 0
        b.append(f'<rect x="20" y="{y}" width="350" height="114" rx="12" fill="#fff" stroke="{K["cobalt"] if sel else K["line"]}" stroke-width="{3 if sel else 1.5}"/>')
        b.append(f'<path d="M44 {y+50}v-30" stroke="{K["ink"]}" stroke-width="2.2"/><path d="M44 {y+20}h20l-5 6 5 6h-20z" fill="{[K["cobalt"], YEAR_COL[4], YEAR_COL[5]][i]}"/>')
        b.append(T(78, y + 36, t, 18, K["ink"], 900) + T(38, y + 76, l1, 13.5, K["soft"], 500) + T(38, y + 96, l2, 13.5, K["soft"], 500))
        if sel:
            b.append(f'<circle cx="344" cy="{y+28}" r="12" fill="{K["cobalt"]}"/><path d="M338 {y+28}l4 4 8-8" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(primary(632, "Velg mål"))
    b.append(T(195, 718, "Trivselen teller også: et rikt, men slitsomt liv gir en hul seier.", 12, K["soft"], 500, "middle"))
    b.append(home_ind())
    return b


@screen("06-avatar", "velg hvordan du ser ut")
def s06():
    b = [sub_page("Hvem flytter inn?")]
    b.append(T(20, 186, "Du er 15 år og flytter inn i 1. etasje.", 13.5, K["soft"], 500))
    for i, lk in enumerate(LOOKS):
        cx = 20 + (i % 3) * 118
        cy = 204 + (i // 3) * 196
        sel = i == 0
        b.append(f'<rect x="{cx}" y="{cy}" width="108" height="184" rx="12" fill="#fff" stroke="{K["cobalt"] if sel else K["line"]}" stroke-width="{3 if sel else 1.5}"/>')
        b.append(f'<ellipse cx="{cx+54}" cy="{cy+166}" rx="34" ry="8" fill="{K["panel"]}"/>')
        b.append(person(cx + 54, cy + 166, 3.0, lk, -1))
        if sel:
            b.append(f'<circle cx="{cx+90}" cy="{cy+18}" r="11" fill="{K["cobalt"]}"/><path d="M{cx+85} {cy+18}l3.5 3.5 7-7" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(primary(612, "Flytt inn"))
    b.append(T(195, 700, "Du får en pengegave med en gang du flytter inn.", 12.5, K["soft"], 500, "middle"))
    b.append(home_ind())
    return b


@screen("07-pengegave", "første valg: pengegaven i 1. etasje")
def s07():
    b = ['<rect width="390" height="460" fill="url(#sky)"/>', topbar("Januar", 15, 1, sub="Du fyller 15 · År 1 av 5", stats=False)]
    iso = Iso(176, 300, 1.55)
    gift = iso.box(48, 66, 13, 18, 16, 12, K["press"]) + iso.box(46, 64, 25, 22, 20, 4, "#D9707F") + iso.box(55, 64, 13, 4, 20, 16.5, "#FFD45C")
    people = person(*iso.p(92, 54, 0), 1.5, ME, -1, wave=True)
    b.append(open_room(iso, 0, 60, 1, gift + people, phone=False))
    a, c = iso.p(57, 74, 34)
    b.append(f'<g filter="url(#sh)"><rect x="{a-50:.1f}" y="{c-30:.1f}" width="100" height="28" rx="14" fill="#FFD45C"/></g>' + T(f"{a:.1f}", f"{c-11:.1f}", "+18 400 kr", 14, K["ink"], 900, "middle"))
    y0 = 452
    b.append(dialog_card(y0, "#A9475A", "M", "Mamma", "gratulerer med dagen!", "Du har fått 18 400 kr", "Pengegaven er din. Hva gjør du med den?"))
    for i, (l, p) in enumerate([("Spar alt på sparekonto", "0 kr brukt"), ("Spar halvparten", "9 200 kr"), ("Ny mobil og spill", "18 400 kr")]):
        b.append(option(20, y0 + 120 + i * 60, 350, 50, l, p))
    b.append(T(195, y0 + 314, "Det du velger nå, kan dukke opp igjen senere.", 12.5, K["soft"], 500, "middle"))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 08-11 måned og mobil
def hub_scene():
    """Zoomet inn på etasjen din: bare etasjene under og din egen vises."""
    iso = Iso(165, 452, 1.75)
    people = person(*iso.p(90, 54, 70), 1.7, ME, -1)
    body = (ground(iso) + shopfront(iso, 0, 26) + closed_floor(iso, 26, 22, 1, 3) + closed_floor(iso, 48, 22, 2, 3)
            + open_room(iso, 70, 64, 3, people))
    o = ['<rect width="390" height="660" fill="url(#sky)"/>', scene_clip(204, 652, body)]
    a, c = iso.p(W, D, 70)
    o.append(f'<rect x="{a-140:.0f}" y="{c+8:.0f}" width="120" height="26" rx="6" fill="{K["ink"]}"/>' + T(f"{a-80:.0f}", f"{c+26:.0f}", "År 3 · din etasje", 12, "#fff", 800, "middle"))
    o.append(f'<rect x="296" y="214" width="80" height="96" rx="10" fill="#fff" opacity=".9" stroke="{K["line"]}"/>' + mini_block(334, 290, .2))
    return o


@screen("08-maned", "månedsnavet: zoomet inn på etasjen din")
def s08():
    b = hub_scene()
    b.append(topbar("November", 17, 3))
    b.append(T(260, 133, "Mål 19 %", 15, K["ink"], 800))
    b.append(f'<path d="M244 136v-15" stroke="{K["ink"]}" stroke-width="2"/><path d="M244 121h11l-3 3.5 3 3.5h-11z" fill="{K["cobalt"]}"/>')
    b.append(month_strip(146, 10, 10))
    b.append(doorbells(652, BELLS, "Neste måned", "desember"))
    return b


def sms_banner(y, sender, text, when="nå"):
    return (f'<g filter="url(#sh)"><rect x="10" y="{y}" width="370" height="76" rx="22" fill="#F4F3F8" opacity=".98"/></g>'
            f'<rect x="24" y="{y+16}" width="38" height="38" rx="10" fill="#34C759"/>'
            f'<path d="M33 {y+31} q0 -8 10 -8 q10 0 10 8 q0 8 -10 8 l-6 4 1 -5 q-5 -2 -5 -7z" fill="#fff"/>'
            + T(74, y + 27, "MELDINGER", 11.5, "#5E5E66", 600, extra='letter-spacing=".5"') + T(366, y + 27, when, 12, "#5E5E66", 500, "end")
            + T(74, y + 46, sender, 15, "#111", 700) + T(74, y + 65, text, 14.5, "#222", 400))


@screen("09-sms-varsel", "en SMS kommer inn som et ekte varsel")
def s09():
    b = s08()
    b.append('<rect width="390" height="844" fill="#000" opacity=".12"/>')
    b.append(sms_banner(12, "Emma", "Konsert på fredag, blir du med? 400 kr"))
    return b


F = "-apple-system, 'Segoe UI', system-ui, sans-serif"


def t(x, y, s, size, fill="#111", w=400, a="start"):
    return f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{s}</text>'


def phone_status():
    return (t(30, 30, "9:41", 15, "#111", 600) +
            '<g fill="#111"><rect x="331" y="19" width="23" height="11" rx="3" fill="none" stroke="#111" stroke-width="1.4"/><rect x="333.5" y="21.5" width="16" height="6" rx="1.2"/></g>')


GREY, BLUE = "#6C6C70", "#0066CC"


@screen("10-mobil-meldinger", "Mobil: ser ut som en ekte meldingsapp")
def s10():
    b = ['<rect width="390" height="844" fill="#FFFFFF"/>', phone_status()]
    b.append(t(20, 74, "‹ Blokka", 17, BLUE) + t(366, 74, "Rediger", 17, BLUE, 400, "end"))
    b.append(t(20, 124, "Meldinger", 34, "#111", 700))
    b.append('<rect x="16" y="140" width="358" height="38" rx="11" fill="#EFEFF4"/>' + t(44, 165, "Søk", 16, GREY))
    b.append(f'<circle cx="32" cy="159" r="6" fill="none" stroke="{GREY}" stroke-width="2"/>')
    rows = [("Emma", "Konsert på fredag, blir du med?", "nå", True, "#24705E", "E"),
            ("Banken", "Du har passert 3/4 av sparemålet ditt.", "nå", True, K["cobalt"], "B"),
            ("Butikken – Sjefen", "Kan du ta ekstravakter ut desember?", "sep.", False, YEAR_COL[1], "S"),
            ("Mamma", "Forsikringen på mopeden går i januar.", "aug.", False, "#A9475A", "M"),
            ("Jonas, 4. etasje", "Gaming i kveld?", "jul.", False, YEAR_COL[4], "J")]
    for i, (n, msg, when, new, col, L) in enumerate(rows):
        y = 194 + i * 84
        if new:
            b.append(f'<circle cx="12" cy="{y+34}" r="5.5" fill="{BLUE}"/>')
        lc = K["ink"] if col in (YEAR_COL[1], YEAR_COL[4]) else "#fff"
        b.append(f'<circle cx="52" cy="{y+34}" r="26" fill="{col}"/>' + t(52, y + 42, L, 22, lc, 700, "middle"))
        b.append(t(92, y + 26, n, 17, "#111", 700) + t(366, y + 26, when, 15, GREY, 400, "end"))
        b.append(t(92, y + 48, msg, 15, GREY))
        b.append(f'<path d="M92 {y+80}H390" stroke="#E5E5EA"/>')
    b.append('<rect x="0" y="780" width="390" height="64" fill="#F7F7F9"/><path d="M0 780H390" stroke="#E5E5EA"/>')
    b.append(t(195, 806, "Meldinger fra denne måneden er merket med blå prikk.", 12.5, GREY, 400, "middle"))
    b.append('<rect x="140" y="828" width="110" height="4" rx="2" fill="#111"/>')
    return b, "#FFFFFF"


@screen("11-mobil-samtale", "Mobil: invitasjonen legges i planen fra meldingen")
def s11():
    b = ['<rect width="390" height="844" fill="#FFFFFF"/>', phone_status()]
    b.append('<rect x="0" y="44" width="390" height="96" fill="#F7F7F9"/><path d="M0 140H390" stroke="#E5E5EA"/>')
    b.append(t(20, 78, "‹", 30, BLUE))
    b.append(f'<circle cx="195" cy="80" r="24" fill="#24705E"/>' + t(195, 88, "E", 20, "#fff", 700, "middle") + t(195, 126, "Emma ›", 13, "#111", 500, "middle"))
    b.append(t(195, 172, "Oktober", 12, GREY, 500, "middle"))
    b.append('<rect x="16" y="184" width="250" height="40" rx="20" fill="#E9E9EB"/>' + t(32, 209, "Gjengen leier hytte i høstferien!", 15.5))
    b.append(t(195, 262, "I dag", 12, GREY, 500, "middle"))
    b.append('<rect x="16" y="274" width="276" height="62" rx="20" fill="#E9E9EB"/>' + t(32, 299, "Konsert på fredag, blir du med?", 15.5) + t(32, 321, "Billetten er 400 kr", 15.5))
    b.append(f'<g filter="url(#sh)"><rect x="16" y="350" width="300" height="146" rx="14" fill="#fff" stroke="{K["line"]}"/></g>')
    b.append(f'<rect x="16" y="350" width="300" height="6" rx="3" fill="{K["cobalt"]}"/>')
    b.append(f'<g transform="translate(44 390)" fill="none" stroke="{K["cobalt"]}" stroke-width="2.6" stroke-linecap="round"><path d="M-6 8V-10l14-4v18"/><circle cx="-10" cy="8" r="4.5"/><circle cx="4" cy="4" r="4.5"/></g>')
    b.append(T(72, 386, "Invitasjon: Konsert", 16, K["ink"], 900) + T(72, 406, "1 kveld · 400 kr · bare i november", 12.5, K["soft"], 600))
    b.append(primary(426, "Legg i planen", x=30, w=272, h=50))
    b.append(t(195, 524, "Levert", 11.5, GREY, 500, "middle"))
    b.append('<rect x="0" y="752" width="390" height="92" fill="#F7F7F9"/><path d="M0 752H390" stroke="#E5E5EA"/>')
    b.append(f'<rect x="16" y="766" width="358" height="38" rx="19" fill="#fff" stroke="#D1D1D6"/>' + t(34, 791, "Du kan ikke svare i spillet", 15, GREY))
    b.append('<rect x="140" y="828" width="110" height="4" rx="2" fill="#111"/>')
    return b, "#FFFFFF"


# ------------------------------------------------------------------ 12-14, 28 hendelse
@screen("12-hendelse", "hendelsen: det ringer på døra i oktober")
def s12():
    return S.event()


@screen("13-resultat", "resultatet: lapper på veggen og et nytt bilde")
def s13():
    return S.result()


@screen("14-hvorfor", "Hvorfor? viser valget bak endringen")
def s14():
    b = S.result()
    b.append(f'<rect width="390" height="844" fill="{K["ink"]}" opacity=".45"/>')
    y0 = 292
    b.append(f'<g filter="url(#sh)"><path d="M0 {y0+20} Q0 {y0} 20 {y0} H370 Q390 {y0} 390 {y0+20} V844 H0Z" fill="{K["sky2"]}"/></g>')
    b.append(f'<rect x="170" y="{y0+10}" width="50" height="5" rx="2.5" fill="{K["line"]}"/>')
    b.append(T(20, y0 + 56, "Hvorfor?", 26, K["ink"], 900))
    items = [("−1 100 kr", "Hytteturen, valget ditt i oktober.", "Egen mat gjorde turen 700 kr billigere.", "#F7C5C0"),
             ("Sosialt liv +6", "Tre dager med gjengen.", "Gjelder denne måneden.", "#FFD45C"),
             ("Stress −3", "Fri fra jobben i høstferien.", "Gjelder denne måneden.", "#BFE3F5"),
             ("Lys fra År 1", "Du hadde råd fordi du sparte pengegaven", "i januar da du var 15.", YEAR_COL[1])]
    for i, (h, a, c, col) in enumerate(items):
        y = y0 + 80 + i * 82
        b.append(card(20, y, 350, 70) + f'<rect x="20" y="{y}" width="8" height="70" rx="4" fill="{col}"/>')
        b.append(T(40, y + 26, h, 16, K["ink"], 900) + T(40, y + 46, a, 13.5, K["ink"], 500) + T(40, y + 63, c, 12, K["soft"], 500))
    b.append(f'<circle cx="30" cy="{y0+426}" r="10" fill="none" stroke="{K["cobalt"]}" stroke-width="2"/>' + T(30, y0 + 431, "i", 13, K["cobalt"], 900, "middle") + T(48, y0 + 431, "Om tallene: hvordan spillet forenkler", 13, K["cobalt"], 700, extra='text-decoration="underline"'))
    b.append(primary(y0 + 456, "Lukk", arrow=False))
    return b


@screen("28-frakoblet", "frakoblet: skjermen kan leses, valgene er låst")
def s28():
    b = S.event()
    b.append(f'<rect x="0" y="614" width="390" height="190" fill="{K["sky2"]}" opacity=".6"/>')
    b.append(f'<g filter="url(#sh)"><rect x="20" y="384" width="350" height="54" rx="12" fill="{K["ink"]}"/></g>')
    b.append(f'<g transform="translate(46 411)" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"><path d="M-12 -2a17 17 0 0 1 24 0M-7 3a10 10 0 0 1 14 0"/><circle cx="0" cy="8" r="2" fill="#fff"/><path d="M-13 -11L13 13" stroke="#F7C5C0"/></g>')
    b.append(T(72, 407, "Du er frakoblet", 15, "#fff", 800) + T(72, 426, "Valgene låses opp når nettet er tilbake.", 12.5, "#D5E6E2", 500))
    return b


# ------------------------------------------------------------------ 15-19 områdene
def slot(x, y, w, h, kind, label=None, price=None, col=None):
    if kind == "empty":
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" stroke="{K["cobalt"]}" stroke-width="2" stroke-dasharray="6 5"/>' + T(x + w / 2, y + h / 2 + 6, "+ ledig kveld", 14, K["cobalt"], 800, "middle")
    if kind == "work":
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{K["panel"]}"/>' + T(x + w / 2, y + h / 2 - 2, "Ekstravakt", 14, K["soft"], 800, "middle") + T(x + w / 2, y + h / 2 + 16, "ut desember", 12, K["soft"], 500, "middle")
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{col}"/>' + T(x + 14, y + 28, label, 15, K["ink"], 900) + T(x + 14, y + 48, price, 13, K["ink"], 600)


@screen("15-manedsplan", "månedsplanen: fyll ledige kvelder ved å trykke")
def s15():
    b = [sub_page("Kveldene i november")]
    b.append(T(20, 186, "Skole og jobb (14 t/uke) tar resten av tiden.", 13.5, K["soft"], 500))
    b.append(f'<rect x="20" y="200" width="214" height="34" rx="8" fill="{K["panel"]}"/>' + T(127, 222, "Skole", 13.5, K["soft"], 800, "middle"))
    b.append(f'<rect x="240" y="200" width="130" height="34" rx="8" fill="{K["panel"]}"/>' + T(305, 222, "Jobb 14 t", 13.5, K["soft"], 800, "middle"))
    b.append(T(20, 272, "3 ledige kvelder", 17, K["ink"], 900) + T(370, 272, "Planlagt: 650 kr", 14, K["cobalt"], 800, "end"))
    b.append(slot(20, 286, 168, 70, "full", "Konsert", "400 kr · fra Emma", "#FFD45C"))
    b.append(slot(202, 286, 168, 70, "full", "Vennekveld", "250 kr", "#F7C5C0"))
    b.append(slot(20, 368, 168, 70, "empty"))
    b.append(slot(202, 368, 168, 70, "work"))
    b.append(divider(460))
    b.append(T(20, 490, "Trykk for å legge til", 14, K["soft"], 600))
    for i, (n, p, e) in enumerate([("Hvilekveld", "0 kr", "stress ned"), ("Gaming", "0 kr", "hos Jonas"), ("Trening", "0 kr", "stress ned"), ("Kino", "150 kr", "med venner")]):
        y = 504 + i * 56
        b.append(card(20, y, 350, 46))
        b.append(T(38, y + 29, n, 15.5, K["ink"], 700) + T(154, y + 29, e, 12.5, K["soft"], 500) + T(318, y + 29, p, 14.5, K["cobalt"], 800, "end"))
        b.append(f'<circle cx="346" cy="{y+23}" r="11" fill="{K["cobalt"]}"/><path d="M341 {y+23}h10M346 {y+18}v10" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>')
    b.append(secondary(738, "Samme som forrige måned", h=46))
    b.append(home_ind())
    return b


def street_scene(y0, h, shop="BUTIKKEN", col=None, bank=False):
    """Gateplan i 3D: butikken eller banken."""
    col = col or K["press"]
    iso = Iso(232, y0 + h - 104, .8)
    o = [f'<rect x="0" y="{y0}" width="390" height="{h}" fill="url(#sky)"/>']
    o.append(iso.box(-20, -10, -6, 190, 120, 6, "#B7C0CB"))
    o.append(iso.box(0, 0, 0, 150, 70, 60, "#EEF1F5"))
    o.append(iso.left(10, 70, 6, 90, 40, "#9CCBF0") + iso.left(10, 70, 48, 120, 10, col) + iso.face_text_left(70, 70, 50.5, shop, 7.5, "#fff"))
    o.append(iso.left(110, 70, 0, 22, 44, K["ink"]))
    o.append(iso.right(150, 6, 6, 56, 40, "#9CCBF0"))
    if not bank:
        o.append(person(*iso.p(70, 84, 0), 1.25, ME, -1))
    return scene_clip(y0, y0 + h, "".join(o))


@screen("16-jobb", "jobben i butikken på gateplan")
def s16():
    b = [street_scene(0, 250), status(), back_btn(), T(70, 72, "Jobben", 26, K["ink"], 900)]
    b.append(f'<path d="M0 252 Q0 232 20 232 H370 Q390 232 390 252 V844 H0Z" fill="{K["sky2"]}"/>')
    b.append(T(20, 272, "Butikkmedarbeider", 18, K["ink"], 900) + T(20, 292, "Butikken på gateplan", 13, K["soft"], 500) + T(370, 282, "7 242 kr", 18, K["cobalt"], 900, "end"))
    b.append(T(370, 298, "lønn i november", 11.5, K["soft"], 500, "end"))
    b.append(T(20, 336, "Timer per uke", 15, K["ink"], 800))
    b.append(card(20, 348, 350, 60))
    b.append(f'<circle cx="54" cy="378" r="18" fill="{K["panel"]}" stroke="#5F7470" stroke-width="1.5"/><path d="M47 378h14" stroke="{K["ink"]}" stroke-width="2.8" stroke-linecap="round"/>')
    b.append(T(195, 386, "10 t", 24, K["ink"], 900, "middle"))
    b.append(f'<circle cx="336" cy="378" r="18" fill="{K["panel"]}" stroke="#5F7470" stroke-width="1.5"/><path d="M329 378h14M336 371v14" stroke="{K["ink"]}" stroke-width="2.8" stroke-linecap="round"/>')
    b.append(T(20, 430, "Gjelder fra neste måned. Grensen er 40 t i uka.", 12.5, K["soft"], 500))
    b.append(T(20, 470, "Ekstravakter (+4 t/uke ut desember)", 15, K["ink"], 800))
    b.append(card(20, 484, 350, 100, stroke=K["cobalt"]) + f'<rect x="20" y="484" width="350" height="100" rx="10" fill="none" stroke="{K["cobalt"]}" stroke-width="2.5"/>')
    b.append(f'<circle cx="46" cy="510" r="10" fill="{K["cobalt"]}"/><circle cx="46" cy="510" r="4" fill="#fff"/>' + T(66, 515, "Behold ekstravaktene", 15.5, K["ink"], 800))
    b.append(T(66, 540, "+604 kr i måneden etter forbruk", 13, K["cobalt"], 700) + T(66, 562, "3 ledige kvelder i desember", 13, K["soft"], 500))
    b.append(card(20, 596, 350, 76))
    b.append(f'<circle cx="46" cy="622" r="10" fill="#fff" stroke="#7C8F8A" stroke-width="2"/>' + T(66, 627, "Avslutt fra desember", 15.5, K["ink"], 700) + T(66, 652, "4 ledige kvelder i desember", 13, K["soft"], 500))
    b.append(primary(696, "Lagre"))
    b.append(T(195, 786, "Si opp jobben", 13.5, K["press"], 700, "middle", 'text-decoration="underline"'))
    b.append(home_ind())
    return b


@screen("17-penger", "pengene: banken på gateplan")
def s17():
    b = [street_scene(0, 230, "BANKEN", K["cobalt"], bank=True), status(), back_btn(), T(70, 72, "Pengene dine", 26, K["ink"], 900)]
    b.append(f'<path d="M0 232 Q0 212 20 212 H370 Q390 212 390 232 V844 H0Z" fill="{K["sky2"]}"/>')
    for i, (n, v) in enumerate([("Brukskonto", "3 120 kr"), ("Sparekonto", "18 750 kr"), ("BSU", "0 kr")]):
        x = 20 + i * 119
        b.append(card(x, 232, 112, 70) + T(x + 12, 256, n, 12, K["soft"], 600) + T(x + 12, 284, v, 15.5, K["ink"], 900))
    b.append(card(20, 316, 350, 114, stroke=K["cobalt"]))
    b.append(f'<path d="M42 338v26" stroke="{K["ink"]}" stroke-width="2.2"/><path d="M42 338h18l-5 6 5 6h-18z" fill="{K["cobalt"]}"/>')
    b.append(T(72, 352, "Sparemål: Førerkort", 16, K["ink"], 900) + T(352, 352, "75 %", 16, K["cobalt"], 900, "end"))
    b.append(bar(38, 370, 314, 75, K["cobalt"], 10))
    b.append(T(38, 404, "18 750 av 25 000 kr · åpner i januar", 13, K["soft"], 500) + T(352, 420, "Bytt mål", 12.5, K["cobalt"], 700, "end", 'text-decoration="underline"'))
    b.append(T(20, 464, "Livsmålet på taket", 15, K["ink"], 800) + T(370, 464, "19 %", 15, K["cobalt"], 900, "end"))
    b.append(bar(20, 476, 350, 19, K["cobalt"], 8))
    b.append(T(20, 506, "18 750 av 100 000 kr", 12.5, K["soft"], 500))
    b.append(divider(524))
    b.append(T(20, 554, "Gjør noe med pengene", 15, K["ink"], 800))
    for i, (n, r) in enumerate([("Flytt til sparekonto", "›"), ("Sett inn på BSU", "›"), ("Forbruk: normalt", "Endre ›")]):
        y = 568 + i * 52
        b.append(card(20, y, 350, 42) + T(38, y + 27, n, 15, K["ink"], 600) + T(352, y + 27, r, 14, K["cobalt"], 800, "end"))
    b.append(T(20, 750, "Neste måned", 15, K["ink"], 800) + T(370, 750, "1 340 kr faste kostnader", 13.5, K["soft"], 600, "end"))
    b.append(T(20, 778, "Brukt på aktiviteter i år", 13.5, K["soft"], 500) + T(370, 778, "4 850 kr", 13.5, K["ink"], 800, "end"))
    b.append(home_ind())
    return b


@screen("18-rommet-trivsel", "rommet ditt og trivselen")
def s18():
    b = ['<rect width="390" height="400" fill="url(#sky)"/>', status(), back_btn(), T(70, 72, "Rommet ditt", 26, K["ink"], 900)]
    iso = Iso(172, 262, 1.4)
    b.append(open_room(iso, 0, 60, 3, person(*iso.p(92, 54, 0), 1.4, ME, -1), photo=True, phone=True))
    b.append(f'<rect x="0" y="384" width="390" height="460" fill="{K["sky2"]}"/>')
    b.append(T(20, 410, "Nytt: bilde fra hytteturen. Hjelmen til mopeden står på gulvet.", 12.5, K["soft"], 500))
    b.append(T(20, 448, "Trivsel", 18, K["ink"], 900) + T(370, 448, "64", 22, K["cobalt"], 900, "end"))
    b.append(window_meter(20, 460, 350, 64))
    b.append(T(20, 498, "Grensen for ekte seier er 50. Snittet ditt så langt: 58.", 12.5, K["soft"], 500))
    for i, (n, v, s, col) in enumerate([("Stress", 38, "lavere er bedre", K["press"]), ("Fritid", 72, "følger skole og jobb", "#4A7AA8"), ("Sosialt liv", 58, "vanlig 52 · +6 denne måneden", "#5E7E4E")]):
        y = 536 + i * 66
        b.append(T(20, y, n, 15, K["ink"], 800) + T(370, y, str(v), 15, K["ink"], 900, "end"))
        b.append(bar(20, y + 12, 350, v, col, 9))
        b.append(T(20, y + 40, s, 12, K["soft"], 500))
    b.append(home_ind())
    return b


@screen("19-arslinje", "året ditt: januar til desember, År 1 til 5 som etasjer")
def s19():
    b = [sub_page("Året ditt", h=140)]
    for i in range(5):
        x = 20 + i * 70
        sel = i == 2
        b.append(f'<rect x="{x}" y="150" width="64" height="58" rx="8" fill="{YEAR_COL[i+1] if i < 4 else "#D98A98"}" stroke="{K["ink"] if sel else "none"}" stroke-width="3"/>')
        b.append(T(x + 32, 174, f"År {i+1}", 13, K["ink"], 900, "middle") + T(x + 32, 194, f"{15+i} år", 11.5, K["ink"], 600, "middle"))
    events = {0: "Ny mobil? Du ventet", 3: "Bursdag: 1 000 kr fra bestemor", 5: "Tilbud om sommerjobb", 6: "Sommerjobb i butikken",
              8: "Sjefen: ekstravakter", 9: "Hyttetur med Emma", 10: "Du er her", 11: "Siste måned med ekstravakter"}
    y0, step = 238, 46
    for i, m in enumerate(MONTHS):
        y = y0 + i * step
        cur, done = i == 10, i < 10
        fill = K["cobalt"] if cur else (K["tint"] if done else "#fff")
        b.append(f'<rect x="20" y="{y}" width="350" height="{step-6}" rx="8" fill="{fill}" stroke="{K["line"] if not cur else K["cobalt"]}"/>')
        b.append(f'<rect x="32" y="{y+9}" width="16" height="22" rx="2" fill="{"#FFD45C" if (done or cur) else "#5C6F8C"}" stroke="#fff" stroke-width="1.5"/>')
        tc = "#fff" if cur else K["ink"]
        b.append(T(60, y + 26, m, 14.5, tc, 800 if cur else 600))
        if i in events:
            b.append(T(162, y + 26, events[i], 12.5, "#fff" if cur else (K["soft"] if i < 10 else K["soft"]), 700 if cur else 500))
        if i in (0, 3, 6, 9):
            b.append(f'<circle cx="354" cy="{y+20}" r="4" fill="{tc if cur else K["cobalt"]}"/>')
    b.append(f'<circle cx="26" cy="806" r="4" fill="{K["cobalt"]}"/>' + T(36, 810, "= måned med hendelse. Tente vinduer = måneder du har spilt.", 12, K["soft"], 500))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 20-22 press og ferdigheter
def pressure_room(year, extra="", people=""):
    iso = Iso(176, 300, 1.55)
    return open_room(iso, 0, 60, year, extra + people, phone=False), iso


@screen("20-kortvarsel", "kortvarsel: konsekvensen i kroner, uten kjeft")
def s20():
    b = ['<rect width="390" height="460" fill="url(#sky)"/>', topbar("Mars", 18, 4, sub="18 år · År 4 av 5 · kortet ditt", stats=False)]
    iso = Iso(176, 300, 1.55)
    cardbox = iso.box(70, 14, 21, 26, 16, 2, K["press"]) + iso.top(72, 16, 23.1, 22, 3, "#fff")
    people = person(*iso.p(92, 54, 0), 1.5, ME, -1)
    b.append(open_room(iso, 0, 60, 4, cardbox + people, phone=False))
    a, c = iso.p(83, 22, 30)
    b.append(f'<g filter="url(#sh)"><rect x="{a-62:.1f}" y="{c-40:.1f}" width="124" height="28" rx="14" fill="{K["press"]}"/></g>' + T(f"{a:.1f}", f"{c-21:.1f}", "10 000 kr gjeld", 13.5, "#fff", 800, "middle"))
    y0 = 452
    b.append(f'<rect x="0" y="{y0-8}" width="390" height="400" fill="{K["sky2"]}"/>')
    b.append(f'<rect x="20" y="{y0}" width="350" height="5" rx="2.5" fill="{K["press"]}"/>')
    b.append(T(20, y0 + 40, "Renta på kortet har startet", 22, K["ink"], 900))
    b.append(T(20, y0 + 62, "Kortet er fullt, og du fikk ikke betalt hele regningen.", 13, K["soft"], 500))
    for i, (l, r) in enumerate([("Rente i år", "22,6 %"), ("Renter denne måneden", "188 kr"), ("Betaler du bare minstebeløpet", "51 måneder"), ("Renter totalt da", "5 508 kr")]):
        yy = y0 + 94 + i * 28
        b.append(T(20, yy, l, 14, K["ink"], 500) + T(370, yy, r, 15, K["press"] if i else K["ink"], 800, "end"))
    for i, (l, p) in enumerate([("Slå av kortbruk", "0 kr"), ("Ta ekstravakter", "+ timer"), ("Snakk med familien", "kanskje hjelp")]):
        b.append(option(20, y0 + 196 + i * 56, 350, 46, l, p))
    b.append(T(195, y0 + 378, "Ingenting skjer før du velger. Du kan også la det være.", 12, K["soft"], 500, "middle"))
    return b


@screen("21-krisemaned", "krisemåned: opptil tre steg, alltid en vei ut")
def s21():
    b = ['<rect width="390" height="460" fill="url(#sky)"/>', topbar("Mai", 18, 4, sub="18 år · År 4 av 5 · krisemåned", stats=False)]
    iso = Iso(176, 300, 1.55)
    lamp = iso.box(130, 6, 44, 6, 6, 8, K["press"])
    people = person(*iso.p(92, 54, 0), 1.5, ME, -1)
    b.append(open_room(iso, 0, 60, 4, lamp + people, phone=False))
    b.append(f'<rect x="0" y="120" width="390" height="340" fill="{K["press"]}" opacity=".08"/>')
    b.append(f'<rect x="20" y="124" width="140" height="30" rx="15" fill="{K["press"]}"/>' + T(90, 144, "STEG 1 AV 3", 12.5, "#fff", 800, "middle", 'letter-spacing="1.5"'))
    y0 = 452
    b.append(f'<rect x="0" y="{y0-8}" width="390" height="400" fill="{K["sky2"]}"/>')
    b.append(f'<rect x="20" y="{y0}" width="350" height="5" rx="2.5" fill="{K["press"]}"/>')
    b.append(T(20, y0 + 40, "Brukskontoen er under 0 kr", 22, K["ink"], 900))
    b.append(T(20, y0 + 62, "Du mangler 1 640 kr. Hva gjør du først?", 13.5, K["soft"], 500))
    for i, (l, p) in enumerate([("Selg mopeden", "+8 152 kr"), ("Ta ekstravakter", "neste mnd"), ("Senk forbruket", "neste mnd"), ("Spør familien", "kanskje hjelp"), ("Ignorer krisen", "gjelda vokser")]):
        b.append(option(20, y0 + 80 + i * 54, 350, 44, l, p))
    b.append(T(195, y0 + 368, "Krisen tar slutt når kontoen er over 0, eller etter tre steg.", 12, K["soft"], 500, "middle"))
    return b


@screen("22-kjorespill", "kjørespill for mopedførerkort: turbasert, ingen tidspress")
def s22():
    b = ['<rect width="390" height="460" fill="url(#sky)"/>', status(), T(20, 72, "Kjøretimen", 26, K["ink"], 900), T(20, 96, "Moped · 16 år · År 2", 13.5, K["soft"], 600)]
    b.append(T(370, 72, "3 av 6", 15, K["cobalt"], 800, "end"))
    for i in range(6):
        b.append(f'<rect x="{20+i*59}" y="110" width="53" height="6" rx="3" fill="{K["cobalt"] if i < 3 else "#fff"}" stroke="{K["cobalt"]}"/>')
    iso = Iso(195, 236, 1.2)
    o = [iso.box(-90, -90, -6, 180, 180, 6, "#8FC59A")]
    o.append(iso.top(-20, -90, .05, 40, 180, "#2F3640") + iso.top(-90, -20, .06, 180, 40, "#2F3640"))
    for i in range(-86, 90, 18):
        if not -24 < i < 24:
            o.append(iso.top(-1, i, .1, 2, 9, "#fff") + iso.top(i, -1, .1, 9, 2, "#fff"))
    # moped (deg) nederst, bil ovenfra
    o.append(iso.box(4, 52, 0, 7, 16, 8, "#3DB8A5") + iso.box(5, 56, 8, 5, 6, 6, ME["top"]))
    o.append(iso.box(-14, -70, 0, 12, 24, 10, "#FFD45C") + iso.box(-13, -64, 10, 10, 12, 5, "#FFE89A"))
    b.append(scene_clip(124, 452, "".join(o)))
    a1, c1 = iso.p(8, 46, 0)
    a2, c2 = iso.p(-40, 8, 0)
    b.append(f'<path d="M{a1:.0f} {c1:.0f} Q{a1+10:.0f} {c2:.0f} {a2:.0f} {c2:.0f}" fill="none" stroke="{K["cobalt"]}" stroke-width="4" stroke-dasharray="7 6"/>')
    b.append(f'<path d="M{a2+10:.0f} {c2-8:.0f} l-10 8 10 8" fill="none" stroke="{K["cobalt"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    y0 = 452
    b.append(f'<rect x="0" y="{y0-8}" width="390" height="400" fill="{K["sky2"]}"/>')
    b.append(T(20, y0 + 30, "Du skal svinge til venstre.", 20, K["ink"], 900))
    b.append(T(20, y0 + 54, "En bil kommer mot deg og skal rett frem.", 14, K["soft"], 500))
    for i, l in enumerate(["Kjør først, du er raskest", "Vent til bilen har kjørt forbi", "Tut og sving"]):
        b.append(option(20, y0 + 76 + i * 60, 350, 50, l, ""))
    b.append(T(195, y0 + 290, "Ingen klokke. Ta den tiden du trenger.", 12.5, K["soft"], 500, "middle"))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 23-25 år, retur, slutt
@screen("23-arsslutt", "året er ferdig: heisen går opp til neste etasje")
def s23():
    b = ['<rect width="390" height="844" fill="url(#sky)"/>', status()]
    iso = Iso(150, 470, 1.25)
    o = [iso.box(-10, -10, 0, 80, 70, 4, "#B7C0CB")]
    hs = [26, 22, 22, 22, 22, 22]
    z = 4
    for i, h in enumerate(hs):
        col = "#EEF1F5" if i == 0 else YEAR_COL[i]
        o.append(iso.box(0, 0, z, 60, 50, h, col))
        if i:
            o.append(iso.left(8, 50, z + 5, 12, 11, "#FFD45C" if i <= 3 else "#5C6F8C") + iso.left(30, 50, z + 5, 12, 11, "#FFD45C" if i <= 3 else "#5C6F8C"))
            o.append(iso.face_text_left(52, 50, z + 7, f"{i}", 9, K["ink"]))
        z += h
    o.append(iso.right(60, 10, 4, 30, z - 4, "#C9D6E3", 'opacity=".9"'))
    zc = 4 + 26 + 22 * 2 + 14
    o.append(iso.right(60.2, 14, zc, 22, 24, K["cobalt"]))
    a, c = iso.p(60, 25, zc + 34)
    o.append(f'<path d="M{a:.0f} {c:.0f}v-26m-9 9 9-9 9 9" fill="none" stroke="{K["cobalt"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append("".join(o))
    b.append(T(20, 96, "År 3 er ferdig!", 32, K["ink"], 900, extra='letter-spacing="-.8"'))
    b.append(T(20, 124, "Heisen tar deg opp til 4. etasje. Der fyller du 18.", 14, K["soft"], 600))
    b.append(floor_display(298, 60, 4))
    y0 = 480
    b.append(f'<rect x="0" y="{y0-8}" width="390" height="400" fill="{K["sky2"]}"/>')
    b.append(month_strip(y0, 12, 12))
    b.append(T(20, y0 + 92, "Spart i år", 14, K["soft"], 500) + T(370, y0 + 92, "+9 400 kr", 16, K["cobalt"], 900, "end"))
    b.append(T(20, y0 + 120, "Trivsel i snitt", 14, K["soft"], 500) + T(370, y0 + 120, "61", 16, K["ink"], 900, "end"))
    b.append(divider(y0 + 138))
    b.append(T(20, y0 + 168, "I 4. etasje", 15, K["ink"], 900))
    b.append(T(20, y0 + 192, "Bilførerkort og kredittkort åpner.", 14, K["ink"], 500))
    b.append(T(20, y0 + 214, "Et valg du tok i fjor kan også banke på igjen …", 14, K["soft"], 500))
    b.append(primary(y0 + 238, "Ta heisen til År 4"))
    b.append(T(195, y0 + 324, "Alt er lagret. Du kan ta pause nå.", 12.5, K["soft"], 500, "middle"))
    return b


@screen("24-velkommen-tilbake", "velkommen tilbake: kort oppsummering etter pause")
def s24():
    b = s08()
    b.append(f'<rect width="390" height="844" fill="{K["ink"]}" opacity=".5"/>')
    y0 = 170
    b.append(f'<g filter="url(#sh)"><rect x="20" y="{y0}" width="350" height="470" rx="16" fill="#fff"/></g>')
    b.append(f'<circle cx="195" cy="{y0}" r="34" fill="{K["tint"]}" stroke="#fff" stroke-width="4"/>' + person(195, y0 + 30, 1.25, ME, -1))
    b.append(T(195, y0 + 66, "Velkommen tilbake!", 24, K["ink"], 900, "middle"))
    b.append(T(195, y0 + 92, "Du er i november. 17 år, 3. etasje.", 14, K["soft"], 500, "middle"))
    sc = .84
    b.append(f'<g transform="translate({195-195*sc:.1f} {y0+108-146*sc:.1f}) scale({sc})">' + month_strip(146, 10, 10) + "</g>")
    b.append(card(40, y0 + 176, 310, 106, fill=K["panel"]))
    b.append(f'<circle cx="62" cy="{y0+206}" r="8" fill="#FFD45C"/>' + T(80, y0 + 211, "3 120 kr på brukskontoen", 14.5, K["ink"], 700))
    b.append(f'<rect x="56" y="{y0+226}" width="13" height="20" rx="3" fill="none" stroke="{K["ink"]}" stroke-width="2"/>' + T(80, y0 + 242, "2 meldinger kom denne måneden", 14.5, K["ink"], 700))
    b.append(T(62, y0 + 268, "Planlagt: konsert og vennekveld", 13, K["soft"], 500))
    b.append(T(195, y0 + 318, "I 4. etasje kan du ta bilførerkort.", 14, K["cobalt"], 800, "middle"))
    b.append(T(195, y0 + 340, "Det koster rundt 25 000 kr.", 13, K["soft"], 500, "middle"))
    b.append(primary(y0 + 380, "Fortsett", x=40, w=310))
    return b


@screen("25-slutt", "slutten: hele blokka lyser, og målet på taket er nådd")
def s25():
    b = ['<rect width="390" height="380" fill="url(#sky)"/>', status()]
    b.append(mini_block(250, 330, .62, cur=5, lit_all=True))
    iso = Iso(250, 330, .62)
    a, c = iso.p(W - 30, 30, 26 + 5 * 22 + 4)
    b.append(f'<path d="M{a:.0f} {c:.0f}v-44" stroke="{K["ink"]}" stroke-width="3"/><path d="M{a:.0f} {c-44:.0f}h30l-8 8 8 8h-30z" fill="{K["cobalt"]}"/>')
    b.append(f'<circle cx="{a+46:.0f}" cy="{c-44:.0f}" r="13" fill="#FFD45C"/><path d="M{a+40:.0f} {c-44:.0f}l4 4 8-9" fill="none" stroke="{K["ink"]}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    for i in range(14):
        ang = i * 2 * math.pi / 14
        b.append(f'<rect x="{a+15+math.cos(ang)*70:.0f}" y="{c-40+math.sin(ang)*50:.0f}" width="6" height="10" rx="1" fill="{[YEAR_COL[1], YEAR_COL[3], YEAR_COL[4], YEAR_COL[5], "#FFD45C"][i%5]}" transform="rotate({i*25} {a+18+math.cos(ang)*70:.0f} {c-35+math.sin(ang)*50:.0f})"/>')
    b.append(T(20, 92, "Ekte seier!", 34, K["ink"], 900, extra='letter-spacing="-1"'))
    b.append(T(20, 118, "Du fylte 20 og flyttet", 14, K["soft"], 600) + T(20, 136, "ut fra 5. etasje.", 14, K["soft"], 600))
    b.append(f'<path d="M0 372 Q0 352 20 352 H370 Q390 352 390 372 V844 H0Z" fill="{K["sky2"]}"/>')
    b.append(card(20, 372, 168, 74) + T(36, 398, "Spart", 12.5, K["soft"], 600) + T(36, 430, "104 300 kr", 19, K["cobalt"], 900))
    b.append(card(202, 372, 168, 74) + T(218, 398, "Trivsel i snitt", 12.5, K["soft"], 600) + T(218, 430, "58 av 100", 19, K["ink"], 900))
    b.append(T(20, 482, "Valgene som betydde mest", 16, K["ink"], 900))
    for i, (n, w, v, col) in enumerate([("Sparte pengegaven", "1. etasje · januar", "+17 270 kr", YEAR_COL[1]), ("Kortet som debetkort", "4. etasje", "−5 508 kr", YEAR_COL[4]), ("Konserter", "alle etasjene", "−2 600 kr", YEAR_COL[3])]):
        y = 496 + i * 70
        b.append(card(20, y, 350, 60) + f'<rect x="32" y="{y+14}" width="22" height="32" rx="3" fill="{col}"/>' + T(43, y + 35, str(i + 1), 14, K["ink"], 900, "middle"))
        b.append(T(68, y + 26, n, 15, K["ink"], 800) + T(68, y + 45, w, 12.5, K["soft"], 500) + T(336, y + 36, v, 15, K["cobalt"] if v.startswith("+") else K["press"], 900, "end"))
        b.append(f'<path d="M348 {y+25}l6 6-6 6" fill="none" stroke="{K["soft"]}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(primary(712, "Flytt inn på nytt fra 15"))
    b.append(T(195, 794, "Nytt mål, ny pengegave, nytt liv.", 12.5, K["soft"], 500, "middle"))
    b.append(home_ind())
    return b


# ------------------------------------------------------------------ 26-27 meny
@screen("26-meny", "meny: konto, personvern og nytt liv")
def s26():
    b = [sub_page("Meny")]
    y = 186
    for g, items in [("Spillet", ["Året ditt", "Rommet ditt", "Om tallene", "Start et nytt liv"]), ("Kontoen", ["Bytt passord", "Spillerinformasjon", "Logg ut", "Logg ut på alle enheter"])]:
        b.append(T(20, y, g.upper(), 12, K["soft"], 800, extra='letter-spacing="1.5"'))
        y += 12
        b.append(card(20, y, 350, 50 * len(items)))
        for i, n in enumerate(items):
            yy = y + 31 + i * 50
            b.append(T(38, yy, n, 15.5, K["ink"], 600) + T(352, yy, "›", 18, K["soft"], 600, "end"))
            if i < len(items) - 1:
                b.append(divider(y + 50 * (i + 1), 38, 332))
        y += 50 * len(items) + 34
    b.append(secondary(y - 6, "Slett kontoen", col=K["press"]))
    b.append(T(195, y + 68, "Sletting krever passordet og kan ikke angres.", 12, K["soft"], 500, "middle"))
    b.append(home_ind())
    return b


@screen("27-om-tallene", "Om tallene: hvor spillet forenkler")
def s27():
    b = [sub_page("Om tallene")]
    b.append(T(20, 186, "Spillet bruker ekte norske tall fra 2026, men", 13.5, K["soft"], 500))
    b.append(T(20, 205, "forenkler noen ting. Her står alt samlet.", 13.5, K["soft"], 500))
    for i, (h, txt) in enumerate([("Lønn", "Alle jobber gir samme timelønn for alderen."), ("Skatt", "Skatt regnes på årslønna, uten andre fradrag."),
                                  ("Renter", "Renter regnes én gang i måneden, i hele kroner."), ("Kveldene", "Måneden har ledige kvelder, ikke dager."),
                                  ("Mopeden", "Verdien faller litt hver måned, uansett kjøring.")]):
        y = 226 + i * 86
        b.append(card(20, y, 350, 74))
        b.append(f'<circle cx="44" cy="{y+27}" r="11" fill="none" stroke="{K["cobalt"]}" stroke-width="2"/>' + T(44, y + 32, "i", 13, K["cobalt"], 900, "middle"))
        b.append(T(66, y + 32, h, 15.5, K["ink"], 800) + T(38, y + 57, txt, 12.5, K["soft"], 500))
    b.append(T(195, 680, "Første gang en forenkling dukker opp i spillet,", 12.5, K["soft"], 500, "middle"))
    b.append(T(195, 698, "vises den bak et i-symbol.", 12.5, K["soft"], 500, "middle"))
    b.append(home_ind())
    return b


def render(name):
    title, fn = SCREENS[name]
    res = fn()
    bg = None
    if isinstance(res, tuple):
        res, bg = res
    with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
        f.write(page(title, "\n".join(res), bg))


if __name__ == "__main__":
    only = sys.argv[1:]
    for name in sorted(SCREENS):
        if only and not any(name.startswith(o) for o in only):
            continue
        render(name)
        print(name)
