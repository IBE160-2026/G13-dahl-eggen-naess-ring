# Konsept «Blokka» v2: dagslys, fargerike fasader, rommet åpent inne i blokka.
# Fem etasjer = År 1–5 (15–19 år). Tolv lamper/vinduer = januar–desember.
# Skal skille seg tydelig fra «Veien»: lys modus, flate fasadefarger, koboltblå handling,
# tomatrød for det som presser, egne avatarer, ringeklokkepanel som meny.
import math

K = {
    "sky": "#CFEAFB", "sky2": "#EAF6FD", "ground": "#8FB89A", "street": "#5E6B7A",
    "y1": "#F4C2A1", "y2": "#F6DC7E", "y3": "#A8DCC6", "y4": "#BCC9F4", "y5": "#F3B9CB",
    "frame": "#FFFFFF", "lit": "#FFD45C", "off": "#DCE6EE",
    "ink": "#14213D", "soft": "#4A5872", "line": "#C9D3DE",
    "cobalt": "#1F3FCF", "cobalt2": "#142C99", "press": "#D9402B",
    "paper": "#FFFFFF", "panel": "#E7ECF2", "steel": "#B7C2CF",
    "wall": "#FBF3E6", "floor": "#D7A77E", "stair": "#CFE8D8",
}
FONT = "family=Schibsted+Grotesk:wght@400;500;600;700;800;900"
FAM = "'Schibsted Grotesk', sans-serif"
MONTHS = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]
YEAR_COL = {1: K["y1"], 2: K["y2"], 3: K["y3"], 4: K["y4"], 5: K["y5"]}


def T(x, y, s, size, fill=None, w=500, anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" font-family="{FAM}" font-size="{size}" font-weight="{w}" fill="{fill or K["ink"]}" text-anchor="{anchor}" {extra}>{s}</text>'


def page(title, body, bg=None):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="390" height="844" viewBox="0 0 390 844">
  <title>Blokka: {title}</title>
  <defs>
    <style>@import url('https://fonts.googleapis.com/css2?{FONT}&amp;display=block');</style>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{K['sky']}"/><stop offset="1" stop-color="{K['sky2']}"/></linearGradient>
    <filter id="sh" x="-20%" y="-20%" width="140%" height="170%"><feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#14213D" flood-opacity=".16"/></filter>
    <filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="5"/></filter>
  </defs>
  <rect width="390" height="844" fill="{bg or K['sky2']}"/>
{body}
</svg>"""


def status(fill=None):
    fill = fill or K["ink"]
    return (T(24, 30, "9:41", 15, fill, 600) +
            f'<g fill="{fill}"><rect x="331" y="19" width="23" height="11" rx="3" fill="none" stroke="{fill}" stroke-width="1.4"/><rect x="333.5" y="21.5" width="16" height="6" rx="1.2"/></g>')


def floor_display(x, y, floor, label="ETG"):
    """Heisens etasjeviser: alderen og året står som etasje."""
    return (f'<rect x="{x}" y="{y}" width="72" height="44" rx="8" fill="{K["ink"]}"/>'
            f'<path d="M{x+12} {y+16}l6 -6 6 6" fill="none" stroke="{K["lit"]}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
            + T(x + 18, y + 34, label, 9.5, "#9FB0C8", 700, "middle", 'letter-spacing="1"')
            + T(x + 52, y + 33, str(floor), 26, K["lit"], 800, "middle"))


def topbar(month, age, year_no, sub=None, stats=True):
    o = [status(), T(20, 82, month, 30, K["ink"], 900, extra='letter-spacing="-.8"'),
         T(20, 104, sub or f"{age} år · År {year_no} av 5", 14, K["soft"], 600),
         floor_display(298, 60, year_no)]
    if stats:
        o.append(f'<circle cx="28" cy="128" r="8" fill="{K["lit"]}"/><circle cx="28" cy="128" r="4.5" fill="none" stroke="#C79A1F" stroke-width="1.5"/>' + T(42, 133, "3 120 kr", 15, K["ink"], 800))
        o.append(f'<path transform="translate(140 128)" d="M0 6 C-10 -2 -8 -10 -2 -10 C1 -10 0 -7 0 -6 C0 -7 -1 -10 2 -10 C8 -10 10 -2 0 6Z" fill="{K["press"]}"/>' + T(154, 133, "Trivsel 64", 15, K["ink"], 800))
    return "".join(o)


# ------------------------------------------------------------------ avatarer (egen stil)
def human(x, y, k=1.0, jacket="#E2653F", shirt="#FFFFFF", pants="#2C3E66", hair="#3B2416", skin="#F2C3A0",
          style="short", face=1, wave=False, shoes="#FFFFFF"):
    """Skandinavisk flat illustrasjon: lange proporsjoner, jakke over T-skjorte, ingen konturer."""
    X = lambda v: f"{x+v*k:.1f}"
    Y = lambda v: f"{y+v*k:.1f}"
    s = lambda v: f"{v*k:.1f}"
    shade = "#000"
    o = [f'<ellipse cx="{x}" cy="{Y(1)}" rx="{s(22)}" ry="{s(4)}" fill="#14213D" opacity=".12"/>']
    if style == "long":
        o.append(f'<path d="M{X(-12)} {Y(-124)} Q{X(-17)} {Y(-96)} {X(-12)} {Y(-78)} H{X(12)} Q{X(17)} {Y(-96)} {X(12)} {Y(-124)}Z" fill="{hair}"/>')
    # bein
    o.append(f'<path d="M{X(-11)} {Y(-62)} L{X(-12)} {Y(-6)} H{X(-3)} L{X(0)} {Y(-48)} L{X(3)} {Y(-6)} H{X(12)} L{X(11)} {Y(-62)}Z" fill="{pants}"/>')
    o.append(f'<path d="M{X(0)} {Y(-48)} L{X(3)} {Y(-6)} H{X(12)} L{X(11)} {Y(-62)}Z" fill="{shade}" opacity=".12"/>')
    # sko
    o.append(f'<path d="M{X(-15)} {Y(-1)} q0 {s(-7)} {s(6)} {s(-7)} h{s(7)} v{s(7)}z" fill="{shoes}"/><path d="M{X(2)} {Y(-1)} v{s(-7)} h{s(8)} q{s(7)} 0 {s(8)} {s(7)}z" fill="{shoes}"/>')
    o.append(f'<path d="M{X(-15)} {Y(-1)}h{s(13)}M{X(2)} {Y(-1)}h{s(16)}" stroke="#14213D" stroke-width="{s(2)}" opacity=".35"/>')
    # T-skjorte og jakke
    o.append(f'<path d="M{X(-13)} {Y(-100)} H{X(13)} L{X(12)} {Y(-60)} H{X(-12)}Z" fill="{shirt}"/>')
    o.append(f'<path d="M{X(-15)} {Y(-100)} Q{X(-17)} {Y(-80)} {X(-14)} {Y(-58)} H{X(-4)} L{X(-5)} {Y(-100)}Z" fill="{jacket}"/>')
    o.append(f'<path d="M{X(15)} {Y(-100)} Q{X(17)} {Y(-80)} {X(14)} {Y(-58)} H{X(4)} L{X(5)} {Y(-100)}Z" fill="{jacket}"/>')
    o.append(f'<path d="M{X(15)} {Y(-100)} Q{X(17)} {Y(-80)} {X(14)} {Y(-58)} H{X(8)} L{X(9)} {Y(-100)}Z" fill="{shade}" opacity=".14"/>')
    o.append(f'<path d="M{X(-5)} {Y(-100)} l{s(5)} {s(8)} l{s(5)} {s(-8)}" fill="{skin}"/>')
    # armer
    o.append(f'<path d="M{X(-15)} {Y(-98)} Q{X(-21)} {Y(-80)} {X(-19)} {Y(-62)}" stroke="{jacket}" stroke-width="{s(8)}" fill="none" stroke-linecap="round"/>')
    o.append(f'<circle cx="{X(-19)}" cy="{Y(-58)}" r="{s(4)}" fill="{skin}"/>')
    if wave:
        o.append(f'<path d="M{X(15)} {Y(-98)} Q{X(28)} {Y(-104)} {X(30)} {Y(-122)}" stroke="{jacket}" stroke-width="{s(8)}" fill="none" stroke-linecap="round"/><circle cx="{X(30)}" cy="{Y(-126)}" r="{s(4.2)}" fill="{skin}"/>')
    else:
        o.append(f'<path d="M{X(15)} {Y(-98)} Q{X(21)} {Y(-80)} {X(19)} {Y(-62)}" stroke="{jacket}" stroke-width="{s(8)}" fill="none" stroke-linecap="round"/>')
        o.append(f'<path d="M{X(15)} {Y(-98)} Q{X(21)} {Y(-80)} {X(19)} {Y(-62)}" stroke="{shade}" stroke-width="{s(8)}" fill="none" stroke-linecap="round" opacity=".12"/>')
        o.append(f'<circle cx="{X(19)}" cy="{Y(-58)}" r="{s(4)}" fill="{skin}"/>')
    # hals og hode (litt avlangt)
    o.append(f'<rect x="{X(-3.5)}" y="{Y(-108)}" width="{s(7)}" height="{s(9)}" fill="{skin}"/><rect x="{X(-3.5)}" y="{Y(-108)}" width="{s(7)}" height="{s(4)}" fill="{shade}" opacity=".12"/>')
    o.append(f'<ellipse cx="{x}" cy="{Y(-120)}" rx="{s(10.5)}" ry="{s(12.5)}" fill="{skin}"/>')
    o.append(f'<ellipse cx="{X(-10*face)}" cy="{Y(-119)}" rx="{s(2.2)}" ry="{s(3.2)}" fill="{skin}"/>')
    # hår
    if style == "short":
        o.append(f'<path d="M{X(-11)} {Y(-118)} Q{X(-12)} {Y(-135)} {X(1)} {Y(-134)} Q{X(13)} {Y(-134)} {X(11)} {Y(-118)} Q{X(6)} {Y(-127)} {X(-4)} {Y(-125)} Q{X(-8)} {Y(-124)} {X(-11)} {Y(-118)}Z" fill="{hair}"/>')
    elif style == "bun":
        o.append(f'<circle cx="{X(-2*face)}" cy="{Y(-137)}" r="{s(6)}" fill="{hair}"/>')
        o.append(f'<path d="M{X(-11)} {Y(-116)} Q{X(-12)} {Y(-134)} {X(0)} {Y(-133)} Q{X(12)} {Y(-134)} {X(11)} {Y(-116)} Q{X(4)} {Y(-128)} {X(-11)} {Y(-116)}Z" fill="{hair}"/>')
    elif style == "long":
        o.append(f'<path d="M{X(-12)} {Y(-112)} Q{X(-13)} {Y(-135)} {X(0)} {Y(-134)} Q{X(13)} {Y(-135)} {X(12)} {Y(-112)} Q{X(6)} {Y(-128)} {X(-12)} {Y(-112)}Z" fill="{hair}"/>')
    elif style == "curly":
        for dx, dy in [(-8, -128), (-2, -132), (5, -131), (10, -125), (-11, -121)]:
            o.append(f'<circle cx="{X(dx)}" cy="{Y(dy)}" r="{s(5.5)}" fill="{hair}"/>')
    # ansikt: små øyne, bryn, nese-skygge, munn
    ex = 4.5 * face
    for e in (ex - 2.6 * face, ex + 3.4 * face):
        o.append(f'<ellipse cx="{X(e)}" cy="{Y(-120)}" rx="{s(1.3)}" ry="{s(1.8)}" fill="#14213D"/>')
    o.append(f'<path d="M{X(ex-4.5*face)} {Y(-124.5)} h{s(3.5*face)} M{X(ex+1.8*face)} {Y(-124.5)} h{s(3.5*face)}" stroke="{hair}" stroke-width="{s(1.3)}" stroke-linecap="round"/>')
    o.append(f'<path d="M{X(ex+0.6*face)} {Y(-119)} l{s(1.8*face)} {s(4)} h{s(-2*face)}" fill="none" stroke="#C98E6E" stroke-width="{s(1.1)}" stroke-linecap="round"/>')
    o.append(f'<path d="M{X(ex-1.5*face)} {Y(-111.5)} q{s(2.2*face)} {s(1.6)} {s(4.4*face)} 0" fill="none" stroke="#9C4A3A" stroke-width="{s(1.3)}" stroke-linecap="round"/>')
    return "".join(o)


ME = dict(jacket="#E2653F", shirt="#FFFFFF", pants="#2C3E66", hair="#3B2416", style="short", face=1)
EMMA = dict(jacket="#2F7D6B", shirt="#F6DC7E", pants="#3D3456", hair="#7A3B1E", style="bun", face=-1, skin="#E0A57E")


# ------------------------------------------------------------------ blokka (åpen etasje)
BX, BW = 16, 340          # fasade; heissjakt til høyre
SHAFT = 26


def windows_row(x, y, w, h, year, cur_year, cur_month):
    """Tolv vinduer i en lukket etasje."""
    o = []
    ww = 18
    gap = (w - 24 - 12 * ww) / 11
    for m in range(12):
        wx = x + 12 + m * (ww + gap)
        done = year < cur_year or (year == cur_year and m < cur_month)
        o.append(f'<rect x="{wx:.1f}" y="{y+8}" width="{ww}" height="{h-16}" rx="2" fill="{K["frame"]}"/>')
        o.append(f'<rect x="{wx+2:.1f}" y="{y+10}" width="{ww-4}" height="{h-20}" rx="1" fill="{K["lit"] if done else K["off"]}"/>')
    return "".join(o)


def lamps(x, y, w, cur_month):
    """Tolv taklamper i etasjen du bor i: månedene. Tente = spilt, kobolt = nå."""
    o = []
    step = (w - 30) / 11
    for m, L in enumerate("JFMAMJJASOND"):
        cx = x + 15 + m * step
        o.append(f'<path d="M{cx:.1f} {y}v10" stroke="{K["ink"]}" stroke-width="1.2" opacity=".5"/>')
        if m < cur_month:
            o.append(f'<circle cx="{cx:.1f}" cy="{y+15}" r="8" fill="{K["lit"]}" opacity=".45" filter="url(#glow)"/><path d="M{cx-6:.1f} {y+16} a6 6 0 0 1 12 0z" fill="{K["lit"]}"/>')
        elif m == cur_month:
            o.append(f'<circle cx="{cx:.1f}" cy="{y+15}" r="11" fill="{K["cobalt"]}" opacity=".35" filter="url(#glow)"/><path d="M{cx-7:.1f} {y+17} a7 7 0 0 1 14 0z" fill="{K["cobalt"]}"/>')
        else:
            o.append(f'<path d="M{cx-6:.1f} {y+16} a6 6 0 0 1 12 0z" fill="none" stroke="{K["ink"]}" stroke-width="1.4" opacity=".45"/>')
        o.append(T(f"{cx:.1f}", y + 30, L, 9, K["cobalt"] if m == cur_month else K["soft"], 800 if m == cur_month else 600, "middle"))
    return "".join(o)


def room_interior(x, y, w, h, people="", photo=False, notes=""):
    cid = f"ri{x}{y}"
    o = [f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath><g clip-path="url(#{cid})">',
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{K["wall"]}"/>',
         f'<rect x="{x}" y="{y+h-34}" width="{w}" height="34" fill="{K["floor"]}"/><path d="M{x} {y+h-34}H{x+w}" stroke="#B9875F" stroke-width="2"/>',
         # vindu ut (november: tidlig mørkt, lett snø)
         f'<rect x="{x+w-104}" y="{y+40}" width="78" height="70" rx="3" fill="#5D7BB0"/><path d="M{x+w-65} {y+40}v70M{x+w-104} {y+75}h78" stroke="#fff" stroke-width="4"/>'
         f'<rect x="{x+w-104}" y="{y+40}" width="78" height="70" rx="3" fill="none" stroke="#fff" stroke-width="4"/>',
         # hylle med planter, plakat
         f'<rect x="{x+18}" y="{y+52}" width="56" height="74" fill="{K["cobalt"]}"/><circle cx="{x+46}" cy="{y+80}" r="14" fill="{K["lit"]}"/><path d="M{x+18} {y+126} l20 -24 14 12 22 -20 v32z" fill="{K["ink"]}" opacity=".7"/>',
         f'<rect x="{x+92}" y="{y+70}" width="70" height="5" fill="#B9875F"/><path d="M{x+104} {y+70} q-6 -14 4 -18 q8 6 -4 18z M{x+112} {y+70} q4 -16 12 -12 q-2 10 -12 12z" fill="#4E9E6E"/><rect x="{x+100}" y="{y+60}" width="14" height="10" fill="#C96B4F"/>',
         # seng
         f'<rect x="{x+12}" y="{y+h-74}" width="128" height="40" rx="6" fill="#7E9BD6"/><rect x="{x+12}" y="{y+h-86}" width="40" height="18" rx="6" fill="#fff"/><rect x="{x+60}" y="{y+h-80}" width="80" height="10" rx="4" fill="#A9BCE8"/>',
         # pult med laptop
         f'<rect x="{x+w-138}" y="{y+h-80}" width="112" height="7" fill="#B9875F"/><rect x="{x+w-132}" y="{y+h-73}" width="5" height="39" fill="#B9875F"/><rect x="{x+w-36}" y="{y+h-73}" width="5" height="39" fill="#B9875F"/>',
         f'<path d="M{x+w-110} {y+h-80} l6 -26 h40 l-6 26z" fill="{K["ink"]}"/><path d="M{x+w-106} {y+h-84} l5 -19 h33 l-5 19z" fill="#8FB8E8"/>',
         # mopedhjelm
         f'<path d="M{x+w-24} {y+h-34} a16 15 0 0 0 -32 0z" fill="{K["press"]}"/><path d="M{x+w-52} {y+h-41} h22" stroke="#fff" stroke-width="3"/>']
    if photo:
        o.append(f'<g transform="rotate(-5 {x+128} {y+100})"><rect x="{x+106}" y="{y+82}" width="46" height="40" fill="#fff" filter="url(#sh)"/><rect x="{x+110}" y="{y+86}" width="38" height="26" fill="#F3B9A0"/><path d="M{x+114} {y+112} l12 -12 10 8 8 -6 v10z" fill="#2F7D6B"/><circle cx="{x+128}" cy="{y+80}" r="3" fill="{K["press"]}"/></g>')
    o.append(notes)
    o.append(people)
    o.append("</g>")
    return "".join(o)


def building(top, cur_year=3, cur_month=10, open_h=214, closed_h=40, people="", photo=False, notes="", goal="Livsmål 19 %"):
    """Blokka sett forfra. Etasjen du bor i står åpen. Returnerer (svg, bunn-y)."""
    o = []
    # tak og livsmålet
    o.append(f'<path d="M{BX-6} {top} L{BX+24} {top-22} H{BX+BW+SHAFT-24} L{BX+BW+SHAFT+6} {top}Z" fill="#6E7F95"/>')
    o.append(f'<path d="M{BX+40} {top-22}v-26" stroke="{K["ink"]}" stroke-width="2"/><path d="M{BX+40} {top-48}h22l-6 6 6 6h-22z" fill="{K["cobalt"]}"/>'
             + T(BX + 70, top - 30, goal, 12, K["ink"], 800))
    y = top
    for yr in range(5, 0, -1):
        h = open_h if yr == cur_year else closed_h
        col = YEAR_COL[yr]
        o.append(f'<rect x="{BX}" y="{y}" width="{BW}" height="{h}" fill="{col}"/>')
        if yr == cur_year:
            o.append(room_interior(BX + 8, y + 8, BW - 16, h - 16, people=people, photo=photo, notes=notes))
            o.append(f'<rect x="{BX+8}" y="{y+8}" width="{BW-16}" height="{h-16}" fill="none" stroke="{col}" stroke-width="2"/>')
            o.append(f'<rect x="{BX+8}" y="{y+8}" width="{BW-16}" height="36" fill="{K["wall"]}" opacity=".0"/>')
            o.append(lamps(BX + 8, y + 8, BW - 16, cur_month))
        else:
            o.append(windows_row(BX, y, BW, h, yr, cur_year, cur_month))
        # år-merke på fasaden
        o.append(f'<rect x="{BX-4}" y="{y+(h-22)/2:.0f}" width="40" height="22" rx="4" fill="{K["ink"] if yr == cur_year else "#fff"}"/>'
                 + T(BX + 16, y + (h - 22) / 2 + 15.5, f"År {yr}", 11, "#fff" if yr == cur_year else K["ink"], 800, "middle"))
        o.append(f'<rect x="{BX}" y="{y+h}" width="{BW}" height="3" fill="#fff" opacity=".7"/>')
        y += h + 3
    # heissjakt med heisen ved etasjen du er i
    o.append(f'<rect x="{BX+BW}" y="{top}" width="{SHAFT}" height="{y-top}" fill="#D3DBE4"/>')
    o.append(f'<path d="M{BX+BW+SHAFT/2} {top}V{y}" stroke="#9AA8B8" stroke-width="1.5"/>')
    ey = top + (5 - cur_year) * (closed_h + 3)
    o.append(f'<rect x="{BX+BW+3}" y="{ey+ (open_h-60)/2:.0f}" width="{SHAFT-6}" height="60" rx="4" fill="{K["cobalt"]}"/>'
             f'<path d="M{BX+BW+SHAFT/2} {ey+(open_h-60)/2+14:.0f}l-5 6h10z M{BX+BW+SHAFT/2} {ey+(open_h-60)/2+46:.0f}l-5 -6h10z" fill="#fff"/>')
    # gateplan: butikken og banken
    o.append(f'<rect x="{BX}" y="{y}" width="{BW+SHAFT}" height="54" fill="#F2F4F7"/>')
    o.append(f'<rect x="{BX+10}" y="{y+16}" width="150" height="38" fill="#9FC7E8"/><rect x="{BX+10}" y="{y+6}" width="150" height="14" fill="{K["press"]}"/>' + T(BX + 85, y + 17, "BUTIKKEN", 9.5, "#fff", 800, "middle", 'letter-spacing="1.5"'))
    o.append(f'<rect x="{BX+170}" y="{y+18}" width="28" height="36" fill="{K["ink"]}"/>')
    o.append(f'<rect x="{BX+208}" y="{y+16}" width="146" height="38" fill="#9FC7E8"/><rect x="{BX+208}" y="{y+6}" width="146" height="14" fill="{K["cobalt"]}"/>' + T(BX + 281, y + 17, "BANKEN", 9.5, "#fff", 800, "middle", 'letter-spacing="1.5"'))
    y += 54
    o.append(f'<rect x="0" y="{y}" width="390" height="14" fill="{K["ground"]}"/>')
    return "".join(o), y + 14


# ------------------------------------------------------------------ ringeklokkepanelet (meny)
def doorbells(y, items, cta, cta_sub=None):
    """Navneskilt med ringeknapper, som i oppgangen, og én bred hovedknapp."""
    o = [f'<rect x="0" y="{y}" width="390" height="{844-y}" fill="{K["panel"]}"/>', f'<path d="M0 {y}H390" stroke="{K["steel"]}" stroke-width="2"/>']
    for i, (name, note) in enumerate(items):
        cx = 16 + (i % 2) * 183
        cy = y + 14 + (i // 2) * 54
        o.append(f'<rect x="{cx}" y="{cy}" width="175" height="46" rx="8" fill="#fff" stroke="{K["steel"]}" stroke-width="1.5"/>')
        o.append(f'<circle cx="{cx+24}" cy="{cy+23}" r="12" fill="{K["panel"]}" stroke="{K["steel"]}" stroke-width="2"/><circle cx="{cx+24}" cy="{cy+23}" r="6" fill="{K["cobalt"] if note else "#fff"}"/>')
        o.append(T(cx + 46, cy + 21, name, 14.5, K["ink"], 800))
        o.append(T(cx + 46, cy + 37, note or " ", 11.5, K["cobalt"] if note else K["soft"], 700))
    by = y + 120
    o.append(f'<rect x="16" y="{by}" width="358" height="50" rx="10" fill="{K["cobalt"]}"/>')
    o.append(T(36, by + 32, cta, 17, "#fff", 800))
    if cta_sub:
        o.append(T(330, by + 32, cta_sub, 14, "#C9D4FF", 600, "end"))
    o.append(f'<path d="M340 {by+25}h16m-6-6 6 6-6 6" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>')
    o.append(f'<rect x="140" y="832" width="110" height="4" rx="2" fill="{K["ink"]}" opacity=".5"/>')
    return "".join(o)


def option(x, y, w, h, label, price, disabled=False):
    return (f'<g opacity="{.45 if disabled else 1}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fff" stroke="{K["cobalt"]}" stroke-width="2"/>'
            + T(x + 16, y + h / 2 + 6, label, 16, K["ink"], 700) + T(x + w - 16, y + h / 2 + 6, price, 16, K["cobalt"], 800, "end") + "</g>")


def sticky(x, y, label, col, rot=-4, w=None):
    w = w or (len(label) * 8 + 24)
    return (f'<g transform="rotate({rot} {x+w/2} {y+20})"><rect x="{x}" y="{y}" width="{w}" height="40" fill="{col}" filter="url(#sh)"/>'
            f'<rect x="{x+w/2-12}" y="{y-5}" width="24" height="10" fill="#fff" opacity=".6"/>'
            + T(x + w / 2, y + 26, label, 15, K["ink"], 800, "middle") + "</g>")


def window_meter(x, y, w, val, new=0, thr=50):
    """Trivsel som vinduer som lyser: 20 vinduer à 5 poeng."""
    n, gap = 20, 3
    sw = (w - gap * (n - 1)) / n
    lit = round(val / 5)
    o = []
    for i in range(n):
        on = i < lit
        newest = lit - new <= i < lit
        f = K["lit"] if on else "#5C6F8C"
        stroke = K["cobalt"] if newest else "#5C6F8C"
        o.append(f'<rect x="{x+i*(sw+gap):.1f}" y="{y}" width="{sw:.1f}" height="16" rx="2" fill="{f}" stroke="{stroke}" stroke-width="{2.5 if newest else 1}"/>')
    mx = x + (thr / 5) * (sw + gap) - gap / 2
    o.append(f'<path d="M{mx:.1f} {y-5}v26" stroke="{K["ink"]}" stroke-width="2"/>')
    return "".join(o)
