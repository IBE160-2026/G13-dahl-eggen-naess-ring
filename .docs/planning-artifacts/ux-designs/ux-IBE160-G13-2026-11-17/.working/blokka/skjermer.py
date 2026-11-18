# «Blokka» v3-skjermer: isometrisk 3D-dukkehus. Kjør: python skjermer.py [nummer ...]
import os, sys
from blokka import K, T, page, topbar, doorbells, option, window_meter, YEAR_COL, status
from iso import Iso, shade
from folk import person

PALETTES = {
    "fjord": dict(sky="#DCEAE5", sky2="#F3F7F5", y1="#F0A24A", y2="#E6D7B0", y3="#8DAA7B", y4="#6E9BC4", y5="#C25B6E",
                  cobalt="#1E5A6B", cobalt2="#143E4A", tint="#D5E6E2", press="#B3364F", ink="#18262B", soft="#4D5F63",
                  panel="#E4ECE9", line="#C3D2CD", steel="#AFC0BA"),
    "solnedgang": dict(sky="#FFC9A3", sky2="#FFF0E3", y1="#E0603E", y2="#F2B33D", y3="#2E9C93", y4="#7B5EA7", y5="#2D4D7C",
                       cobalt="#2D4D7C", cobalt2="#1D3459", tint="#FBDCC8", press="#C8102E", ink="#2A1E1A", soft="#6B5048",
                       panel="#F7E6DA", line="#E9CDBB", steel="#D7B8A4"),
    "mint": dict(sky="#C9F1E6", sky2="#F2FCF9", y1="#FF8C69", y2="#FFD166", y3="#06A77D", y4="#118AB2", y5="#8E5BD9",
                 cobalt="#073B4C", cobalt2="#04252F", tint="#CDEFE6", press="#EF476F", ink="#073B4C", soft="#3D6670",
                 panel="#E2F4EF", line="#BFE3D9", steel="#A6CFC4"),
}


def apply_palette(name):
    P = PALETTES[name]
    K.update(P)
    for i in range(1, 6):
        YEAR_COL[i] = P[f"y{i}"]

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "skjermer")
os.makedirs(OUT, exist_ok=True)
SCREENS = {}

ME = dict(skin="#F0BE98", hair="#3B2416", top="#E2653F", shirt="#FFFFFF", pants="#2C3E66", shoes="#FFFFFF", style="short")
EMMA = dict(skin="#D9A07A", hair="#6E3518", top="#2F8A74", shirt="#F6DC7E", pants="#3D3456", shoes="#F3B9CB", style="bun")
WOOD, WALL, GLASS, DARKWIN = "#D8A97E", "#FBF3E6", "#9CCBF0", "#5C6F8C"


def screen(name, title):
    def deco(fn):
        SCREENS[name] = (title, fn)
        return fn
    return deco


# ------------------------------------------------------------------ tidsstripa (egen, utenfor huset)
def month_strip(y, cur, done, events=(0, 3, 6, 9)):
    o = [f'<rect x="12" y="{y}" width="366" height="52" rx="10" fill="#fff" stroke="{K["line"]}" stroke-width="1.5"/>']
    cw = (366 - 16) / 12
    for m, name in enumerate(["JAN", "FEB", "MAR", "APR", "MAI", "JUN", "JUL", "AUG", "SEP", "OKT", "NOV", "DES"]):
        x = 20 + m * cw
        if m == cur:
            o.append(f'<rect x="{x:.1f}" y="{y+7}" width="{cw-3:.1f}" height="38" rx="6" fill="{K["cobalt"]}"/>')
            col = "#fff"
        elif m < done:
            o.append(f'<rect x="{x:.1f}" y="{y+7}" width="{cw-3:.1f}" height="38" rx="6" fill="{K["tint"]}" stroke="#7C8F8A" stroke-width="1"/>')
            col = K["cobalt2"]
        else:
            o.append(f'<rect x="{x:.1f}" y="{y+7}" width="{cw-3:.1f}" height="38" rx="6" fill="none" stroke="#7C8F8A" stroke-width="1"/>')
            col = K["soft"]
        o.append(T(f"{x+(cw-3)/2:.1f}", y + 27, name, 9.5, col, 800, "middle"))
        if m in events:
            o.append(f'<circle cx="{x+(cw-3)/2:.1f}" cy="{y+37}" r="2.4" fill="{col}"/>')
    return "".join(o)


# ------------------------------------------------------------------ blokka i 3D
W, D = 140, 100


def windows(iso, z, h, year, cur_year):
    lit = year < cur_year
    col = "#FFD45C" if lit else DARKWIN
    o = []
    for i in range(6):     # venstre fasade (y = D)
        o.append(iso.left(10 + i * 23, D, z + h * .28, 13, h * .5, col))
    for i in range(4):     # høyre fasade (x = W)
        o.append(iso.right(W, 10 + i * 25, z + h * .28, 14, h * .5, shade(col, .85)))
    return "".join(o)


def closed_floor(iso, z, h, year, cur_year):
    col = YEAR_COL[year]
    return (iso.box(0, 0, z, W, D, h, col) + windows(iso, z, h, year, cur_year)
            + iso.left(0, D, z + h - 2, W, 2, shade(col, .7)) + iso.face_text_left(-4 + 6, D, z + h * .18, "", 1, "#000"))


def year_tag(iso, z, h, year, current):
    a, b = iso.p(0, D, z + h * .5)
    fill = K["ink"] if current else "#fff"
    tc = "#fff" if current else K["ink"]
    return (f'<rect x="{a-44:.1f}" y="{b-11:.1f}" width="40" height="22" rx="5" fill="{fill}" stroke="{K["line"]}" stroke-width="{0 if current else 1}"/>'
            + T(f"{a-24:.1f}", f"{b+4.5:.1f}", f"År {year}", 11, tc, 800, "middle"))


def open_room(iso, z, h, year, people, photo=False, phone=True):
    col = YEAR_COL[year]
    o = [iso.box(0, 0, z - 4, W, D, 4, col)]                    # gulvskive i årsfargen
    o.append(iso.top(0, 0, z, W, D, WOOD))
    o.append(iso.top(46, 40, z + .1, 56, 40, "#E9C7A6"))           # teppe
    o.append(iso.right(0, 0, z, D, h, shade(WALL, .92)))           # bakvegg (x = 0)
    o.append(iso.left(0, 0, z, W, h, WALL))                        # bakvegg (y = 0)
    o.append(iso.left(0, 0, z + h - 3, W, 3, shade(col, .9)) + iso.right(0, 0, z + h - 3, D, 3, shade(col, .8)))
    # vindu i bakveggen med kveld ute
    o.append(iso.left(92, 0, z + 20, 34, 26, "#5D7BB0") + iso.left(108, 0.1, z + 20, 2, 26, "#fff") + iso.left(92, 0.1, z + 32, 34, 2, "#fff"))
    # plakat på sideveggen
    o.append(iso.right(0, 26, z + 20, 22, 26, K["cobalt"]) + iso.right(0.1, 33, z + 31, 8, 8, "#FFD45C"))
    if photo:
        o.append(iso.left(58, 0.2, z + 30, 26, 20, "#fff") + iso.left(60, 0.3, z + 32, 22, 15, "#F3B9A0") + iso.left(64, 0.4, z + 32, 12, 6, "#2F8A74"))
    # seng
    o.append(iso.box(4, 56, z, 30, 42, 9, "#7E9BD6") + iso.box(4, 56, z + 9, 30, 12, 4, "#FFFFFF"))
    # pult og laptop
    o.append(iso.box(60, 4, z, 4, 20, 18, "#B9875F") + iso.box(106, 4, z, 4, 20, 18, "#B9875F") + iso.box(58, 2, z + 18, 54, 24, 3, "#C99569"))
    o.append(iso.box(76, 8, z + 21, 18, 12, 1.5, K["ink"]) + iso.left(76, 8, z + 22.5, 18, 11, "#8FB8E8"))
    # mopedhjelm
    o.append(iso.box(120, 76, z, 10, 10, 7, K["press"]) + iso.box(122, 84, z + 3, 7, 2.5, 2, K["ink"]))
    if phone:
        o.append(iso.box(16, 76, z + 13, 4, 7, 1, K["ink"]))
        a, b = iso.p(18, 78, z + 22)
        o.append(f'<circle cx="{a:.1f}" cy="{b:.1f}" r="8" fill="{K["cobalt"]}"/>' + T(f"{a:.1f}", f"{b+4:.1f}", "2", 10.5, "#fff", 800, "middle"))
    o.append(people)
    return "".join(o)


def ground(iso):
    o = [iso.box(-26, -26, -8, W + 70, D + 52, 8, "#8FC59A")]
    o.append(iso.top(-26, D + 6, 0.05, W + 70, 20, "#B7C0CB"))      # fortau foran
    # trær
    for tx, ty in [(-16, 30), (W + 26, D + 6)]:
        o.append(iso.box(tx, ty, 0, 4, 4, 14, "#8A5A3C") + iso.box(tx - 6, ty - 6, 14, 16, 16, 14, "#4E9E6E") + iso.box(tx - 3, ty - 3, 28, 10, 10, 8, "#5DB07E"))
    return "".join(o)


def shopfront(iso, z, h):
    o = [iso.box(0, 0, z, W, D, h, "#EEF1F5")]
    o.append(iso.left(8, D, z + 4, 70, h - 12, GLASS) + iso.left(8, D, z + h - 9, 70, 7, K["press"]))
    o.append(iso.face_text_left(43, D, z + h - 7.2, "BUTIKKEN", 6.2, "#fff"))
    o.append(iso.left(90, D, z, 16, h - 10, K["ink"]))
    o.append(iso.right(W, 8, z + 4, 90, h - 12, GLASS) + iso.right(W, 8, z + h - 9, 90, 7, K["cobalt"]))
    o.append(iso.face_text_right(W, 53, z + h - 7.2, "BANKEN", 6.2, "#fff"))
    return "".join(o)


def building(iso, cur_year=3, people="", goal="Livsmål 19 %"):
    o = [ground(iso)]
    zs = {}
    z = 0
    o.append(shopfront(iso, z, 26))
    z += 26
    hs = {1: 22, 2: 22, 3: 64, 4: 22, 5: 22}
    for yr in range(1, 6):
        if yr == cur_year + 1:
            gap = 58
            # sprengtegning: stiplede hjørnelinjer der etasjene er løftet
            for cx, cy in [(W, D), (0, D), (W, 0)]:
                a1, b1 = iso.p(cx, cy, z)
                a2, b2 = iso.p(cx, cy, z + gap)
                o.append(f'<path d="M{a1:.1f} {b1:.1f}L{a2:.1f} {b2:.1f}" stroke="{K["soft"]}" stroke-width="1.3" stroke-dasharray="3 4"/>')
            z += gap
        zs[yr] = z
        if yr == cur_year:
            o.append(open_room(iso, z, hs[yr], yr, people))
        elif yr > cur_year:
            o.append(f'<g opacity=".42">{closed_floor(iso, z, hs[yr], yr, cur_year)}</g>')
        else:
            o.append(closed_floor(iso, z, hs[yr], yr, cur_year))
        z += hs[yr]
    # tak med livsmålet
    o.append(f'<g opacity=".42">{iso.box(-3, -3, z, W + 6, D + 6, 4, "#6E7F95")}{iso.box(20, 20, z + 4, 26, 18, 10, "#8796AA")}</g>')
    a, b = iso.p(W - 30, 30, z + 4)
    o.append(f'<path d="M{a:.1f} {b:.1f}v-34" stroke="{K["ink"]}" stroke-width="2"/><path d="M{a:.1f} {b-34:.1f}h22l-6 6 6 6h-22z" fill="{K["cobalt"]}"/>')
    o.append(f'<g><rect x="{a+26:.1f}" y="{b-40:.1f}" width="92" height="24" rx="6" fill="#fff" stroke="{K["line"]}"/></g>' + T(f"{a+72:.1f}", f"{b-23.5:.1f}", goal, 11.5, K["ink"], 800, "middle"))
    # heistårn på høyre side, heisen står ved etasjen din
    o.append(iso.right(W + 16, -22, 0, 20, z, "#C9D6E3", 'opacity=".9"') + iso.top(W, -22, z, 16, 20, "#B5C3D2"))
    o.append(iso.right(W + 16.2, -19, zs[cur_year] + 10, 14, 36, K["cobalt"]))
    a, b = iso.p(W + 16, -12, zs[cur_year] + 32)
    o.append(f'<path d="M{a:.1f} {b-6:.1f}l-4 5h8z M{a:.1f} {b+8:.1f}l-4 -5h8z" fill="#fff"/>')
    # år-merker på venstre hjørne
    for yr in range(1, 6):
        o.append(year_tag(iso, zs[yr], hs[yr], yr, yr == cur_year))
    return "".join(o)


BELLS = [("Plan", "3 ledige kvelder"), ("Mobil", "2 nye meldinger"), ("Jobb", None), ("Penger", None)]


@screen("08-maned", "månedsnavet i november, 17 år")
def hub():
    b = ['<rect width="390" height="660" fill="url(#sky)"/>', topbar("November", 17, 3)]
    b.append(month_strip(146, 10, 10))
    iso = Iso(186, 482, 1.06)
    people = person(*iso.p(90, 54, 70), 1.05, ME, -1)
    b.append(building(iso, 3, people=people))
    b.append(doorbells(652, BELLS, "Neste måned", "desember"))
    return b


def corridor(iso, z=0):
    """Oppgangen i 3D: grønne vegger, postkasser, døra di åpen, trapp."""
    Wc, Dc, H = 120, 84, 64
    o = [iso.box(0, 0, z - 5, Wc, Dc, 5, "#9DBFA9"), iso.top(0, 0, z, Wc, Dc, "#C6D9CB")]
    for i in range(0, Wc, 20):
        for j in range(0, Dc, 21):
            if (i // 20 + j // 21) % 2 == 0:
                o.append(iso.top(i, j, z + .05, 20, 21, "#B9CFC0"))
    o.append(iso.right(0, 0, z, Dc, H, shade(K["stair"], .9)) + iso.left(0, 0, z, Wc, H, K["stair"]))
    o.append(iso.left(0, 0, z + 30, Wc, 3, "#B7D6C2") + iso.right(0, 0, z + 30, Dc, 3, "#A9CBB5"))
    # døra di i bakveggen, åpen
    o.append(iso.left(14, 0, z, 26, 46, "#5A4636") + iso.left(16, 0.1, z, 22, 44, "#FBF3E6"))
    o.append(iso.right(40, 0, z, 16, 44, K["cobalt"]))                 # dørblad svingt ut
    o.append(iso.left(20, 0.1, z + 49, 14, 6, "#FFD45C") + iso.face_text_left(27, 0.2, z + 50.4, "3. etg", 3.6, K["ink"]))
    # postkasser på sideveggen
    for i in range(3):
        for j in range(2):
            o.append(iso.right(0.1, 40 + i * 13, z + 32 + j * 11, 11, 9, "#E9EEF2") + iso.right(0.2, 42 + i * 13, z + 38 + j * 11, 7, 1.2, "#7F8C99"))
    # trapp opp mot høyre
    for s in range(5):
        o.append(iso.box(Wc - 34, Dc - 20 - s * 10, z + s * 6, 30, 10, 6, "#D5DDE5"))
    return "".join(o)


def bubble(x, y, lines, tail_x):
    w = max(len(l) for l in lines) * 8.2 + 28
    h = 22 + 18 * len(lines)
    o = [f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff"/></g>', f'<path d="M{tail_x} {y+h-1}l-2 14 16-14z" fill="#fff"/>']
    for i, l in enumerate(lines):
        o.append(T(x + w / 2, y + 27 + i * 18, l, 14.5, K["ink"], 800, "middle"))
    return "".join(o)


@screen("12-hendelse", "hendelsen: det ringer på døra i oktober")
def event():
    b = ['<rect width="390" height="460" fill="url(#sky)"/>', topbar("Oktober", 17, 3, sub="Det ringer på døra", stats=False)]
    iso = Iso(200, 268, 1.75)
    b.append(corridor(iso))
    b.append(person(*iso.p(28, 18, 0), 2.15, ME, 1))
    b.append(person(*iso.p(66, 50, 0), 2.15, EMMA, -1, wave=True))
    b.append(bubble(220, 128, ["Blir du med", "på hyttetur?"], 236))
    cy = 452
    b.append(f'<rect x="0" y="{cy-8}" width="390" height="{844-cy+8}" fill="{K["sky2"]}"/>')
    b.append(f'<rect x="20" y="{cy+6}" width="32" height="32" rx="6" fill="#24705E"/>' + T(36, cy + 28, "E", 15, "#fff", 800, "middle") + T(62, cy + 19, "Emma", 14.5, K["ink"], 800) + T(62, cy + 35, "nabo i 2. etasje", 12, K["soft"], 500))
    b.append(T(20, cy + 78, "Hyttetur i høstferien", 25, K["ink"], 900, extra='letter-spacing="-.5"'))
    b.append(T(20, cy + 102, "Tre dager på hytta. 1 800 kr per person med mat.", 14, K["soft"], 500))
    b.append(f'<rect x="20" y="{cy+116}" width="350" height="32" rx="6" fill="{K["panel"]}"/>' + T(32, cy + 137, "Brukskonto 4 220 kr · Sparing 18 750 kr · Gjeld 0 kr", 12.5, K["ink"], 600))
    for i, (l, p) in enumerate([("Bli med og betal alt", "1 800 kr"), ("Bli med, ta med egen mat", "1 100 kr"), ("Stå over denne gangen", "0 kr")]):
        b.append(option(20, cy + 162 + i * 60, 350, 50, l, p))
    b.append(T(195, cy + 356, "Hvordan valget påvirker trivselen, ser du etterpå.", 12.5, K["soft"], 500, "middle"))
    b.append(f'<rect x="140" y="832" width="110" height="4" rx="2" fill="{K["ink"]}" opacity=".5"/>')
    return b


def wall_note(iso, x, z, w, label, col, size=6.6):
    return iso.left(x, 0.3, z, w, 17, col) + iso.left(x + w / 2 - 4, 0.4, z + 15, 8, 3, "#fff", 'opacity=".7"') + iso.face_text_left(x + w / 2, 0.5, z + 5.6, label, size, K["ink"])


def side_note(iso, y, z, d, label, col, size=6.6):
    return iso.right(0.3, y, z, d, 17, col) + iso.right(0.4, y + d / 2 - 4, z + 15, 8, 3, "#fff", 'opacity=".7"') + iso.face_text_right(0.5, y + d / 2, z + 5.6, label, size, K["ink"])


@screen("13-resultat", "resultatet: lapper på veggen og et nytt bilde")
def result():
    b = ['<rect width="390" height="460" fill="url(#sky)"/>', topbar("Oktober", 17, 3, sub="Hyttetur · du tok med egen mat", stats=False)]
    iso = Iso(176, 300, 1.55)
    notes = wall_note(iso, 4, 38, 42, "+6 sosialt", "#FFD45C") + wall_note(iso, 4, 16, 42, "−3 stress", "#BFE3F5") + side_note(iso, 52, 30, 44, "−1 100 kr", "#F7C5C0")
    people = person(*iso.p(92, 54, 0), 1.5, ME, -1, wave=True)
    b.append(open_room(iso, 0, 60, 3, notes + people, photo=True, phone=False))
    a, c = iso.p(71, 0, 60)
    b.append(f'<g filter="url(#sh)"><rect x="{a-50:.1f}" y="{c-36:.1f}" width="100" height="24" rx="12" fill="{K["ink"]}"/></g>' + T(f"{a:.1f}", f"{c-19.5:.1f}", "Nytt på veggen", 11.5, "#fff", 700, "middle"))
    cy = 440
    b.append(f'<rect x="0" y="{cy}" width="390" height="{844-cy}" fill="{K["sky2"]}"/>')
    b.append(T(20, cy + 46, "−1 100 kr", 40, K["ink"], 900, extra='letter-spacing="-1"') + T(370, cy + 44, "igjen 3 120 kr", 14, K["soft"], 600, "end"))
    b.append(T(20, cy + 84, "Trivsel", 15, K["ink"], 800) + T(370, cy + 84, "61 → 64", 16, K["cobalt"], 800, "end"))
    b.append(window_meter(20, cy + 96, 350, 64, new=1))
    b.append(T(20, cy + 132, "Sosialt liv +6 og stress −3 denne måneden.", 12.5, K["soft"], 500))
    ey = cy + 150
    b.append(f'<rect x="20" y="{ey}" width="350" height="76" rx="10" fill="#fff" stroke="{K["line"]}" stroke-width="1.5"/>')
    mini = Iso(52, ey + 54, .19)
    b.append(mini.box(0, 0, 0, W, D, 26, YEAR_COL[1]) + mini.box(0, 0, 26, W, D, 26, YEAR_COL[2]) + mini.box(0, 0, 52, W, D, 26, YEAR_COL[3]))
    a, c = mini.p(40, D, 10)
    b.append(f'<circle cx="{a:.1f}" cy="{c:.1f}" r="7" fill="#FFD45C" opacity=".6" filter="url(#glow)"/><circle cx="{a:.1f}" cy="{c:.1f}" r="3" fill="#FFD45C"/>')
    b.append(T(92, ey + 32, "Et lys fra År 1", 14.5, K["ink"], 800) + T(92, ey + 54, "Du sparte pengegaven. Derfor hadde du råd.", 12.5, K["soft"], 500))
    b.append(T(20, ey + 106, "Hvorfor?", 15, K["cobalt"], 700, extra='text-decoration="underline"'))
    b.append(f'<rect x="16" y="{ey+124}" width="358" height="54" rx="10" fill="{K["cobalt"]}"/>' + T(36, ey + 158, "Videre", 17, "#fff", 800) + f'<path d="M340 {ey+151}h16m-6-6 6 6-6 6" fill="none" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>')
    b.append(f'<rect x="140" y="832" width="110" height="4" rx="2" fill="{K["ink"]}" opacity=".5"/>')
    return b


def render(name, palette="fjord", fname=None):
    apply_palette(palette)
    title, fn = SCREENS[name]
    with open(os.path.join(OUT, f"{fname or name}.svg"), "w", encoding="utf-8") as f:
        f.write(page(title, "\n".join(fn())))


if __name__ == "__main__":
    only = sys.argv[1:]
    if only and only[0] == "paletter":
        for pal in PALETTES:
            render("08-maned", pal, f"palett-{pal}")
            print(pal)
        sys.exit(0)
    for name in SCREENS:
        if only and not any(name.startswith(o) for o in only):
            continue
        render(name)
        print(name)
