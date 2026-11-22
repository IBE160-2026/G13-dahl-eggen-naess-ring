# «Veien» v2: veien er hovedmotivet. Et nivåkart i perspektiv der månedene er milepæler.
import math
from veien import C, FONT, FAM, T, status, level_badge, year_track, coin, heart, wellbeing_bar, float_tag, burst, cabin

C2 = dict(C)
C2.update({"ground0": "#3A1690", "ground1": "#1C0858", "asphalt": "#2FE3D2", "edge": "#0FA394", "jacket": "#E9E2FF"})


def page(title, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="390" height="844" viewBox="0 0 390 844">
  <title>{title}</title>
  <defs>
    <style>@import url('https://fonts.googleapis.com/css2?{FONT}&amp;display=block');</style>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C['sky0']}"/><stop offset=".55" stop-color="{C['sky1']}"/><stop offset="1" stop-color="{C['sky2']}"/></linearGradient>
    <linearGradient id="ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C2['ground0']}"/><stop offset="1" stop-color="{C2['ground1']}"/></linearGradient>
    <linearGradient id="road" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#5CF2E4"/><stop offset="1" stop-color="#B8FFF7"/></linearGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#12053A" stop-opacity="0"/><stop offset=".45" stop-color="#12053A" stop-opacity=".85"/><stop offset="1" stop-color="#12053A"/></linearGradient>
    <filter id="sh" x="-20%" y="-20%" width="140%" height="170%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#0B0426" flood-opacity=".5"/></filter>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7"/></filter>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.5"/></filter>
  </defs>
  <rect width="390" height="844" fill="#12053A"/>
{body}
</svg>"""


# ------------------------------------------------------------------ veien i perspektiv
SEGS = [((200, 900), (60, 760), (340, 600), (215, 500)),
        ((215, 500), (120, 430), (300, 350), (212, 262))]


def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1])


def road_pt(t):
    """t = 0 nærmest, 1 ved horisonten."""
    if t < .5:
        return bez(*SEGS[0], t / .5)
    return bez(*SEGS[1], (t - .5) / .5)


def road_w(t):
    return 8 + 190 * (1 - t) ** 1.7


def road_scale(t):
    return road_w(t) / road_w(.3)


def road_poly(t0=0.0, t1=1.0, n=90, widen=1.0):
    L, R = [], []
    for i in range(n + 1):
        t = t0 + (t1 - t0) * i / n
        x, y = road_pt(t)
        x2, y2 = road_pt(min(1, t + .004))
        dx, dy = x2 - x, y2 - y
        d = math.hypot(dx, dy) or 1
        nx, ny = -dy / d, dx / d
        w = road_w(t) * widen / 2
        L.append((x + nx * w, y + ny * w))
        R.append((x - nx * w, y - ny * w))
    pts = L + R[::-1]
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + "Z"


def center_dashes():
    o = []
    for i in range(26):
        t = .02 + i * .037
        if t > .97:
            break
        x, y = road_pt(t)
        x2, y2 = road_pt(t + .012)
        o.append(f'<path d="M{x:.1f} {y:.1f}L{x2:.1f} {y2:.1f}" stroke="#fff" stroke-width="{max(1, 5*road_scale(t)):.1f}" stroke-linecap="round" opacity=".9"/>')
    return "".join(o)


def pine(x, y, s, fill):
    return f'<path d="M{x} {y-40*s} L{x+12*s} {y-16*s} H{x+6*s} L{x+16*s} {y} H{x-16*s} L{x-6*s} {y-16*s} H{x-12*s} Z" fill="{fill}"/>'


def landscape(sun=True):
    o = ['<rect width="390" height="300" fill="url(#sky)"/>']
    for i, (x, y) in enumerate([(30, 60), (88, 120), (140, 48), (212, 96), (250, 40), (318, 128), (360, 70), (176, 150), (60, 170), (110, 210)]):
        o.append(f'<circle cx="{x}" cy="{y}" r="{1.5 if i % 3 else 2.2}" fill="#fff" opacity="{.5 if i % 2 else .9}"/>')
    if sun:
        o.append(f'<circle cx="300" cy="250" r="64" fill="{C["sun"]}" opacity=".35" filter="url(#glow)"/><circle cx="300" cy="252" r="46" fill="{C["sun"]}"/>')
    o.append(f'<path d="M0 250 C70 220 130 246 190 226 S300 214 390 236 V300 H0Z" fill="{C["far"]}"/>')
    o.append(f'<path d="M0 262 C90 248 160 266 240 252 S350 246 390 256 V300 H0Z" fill="{C["mid"]}"/>')
    o.append('<rect x="0" y="262" width="390" height="582" fill="url(#ground)"/>')
    o.append(f'<path d="M-20 330 C60 300 120 330 150 380 S120 520 -20 560Z" fill="{C["mid"]}" opacity=".55"/>')
    o.append(f'<path d="M410 300 C330 290 280 330 300 400 S380 520 410 540Z" fill="{C["mid"]}" opacity=".45"/>')
    o.append(f'<path d="M-20 600 C80 560 150 640 120 760 L-20 844Z" fill="{C["near"]}" opacity=".7"/>')
    o.append(f'<path d="M410 560 C320 580 300 680 340 844 H410Z" fill="{C["near"]}" opacity=".7"/>')
    for i, (lx, ly) in enumerate([(40, 420), (70, 470), (340, 380), (318, 440), (26, 640), (360, 620)]):
        o.append(f'<circle cx="{lx}" cy="{ly}" r="2.2" fill="{C["lime"] if i % 2 else C["road"]}" opacity=".8"/>')
    # trær langs veien, mindre lenger unna
    for t, side, k in [(.92, -1, .35), (.86, 1, .45), (.78, -1, .55), (.7, 1, .7), (.6, -1, .85), (.52, 1, 1.0), (.42, -1, 1.15), (.22, 1, 1.6), (.12, -1, 1.9)]:
        x, y = road_pt(t)
        off = road_w(t) / 2 + 26 * k
        o.append(pine(x + side * off, y + 4 * k, k, C["near"] if k > .8 else C["mid"]))
    o.append(f'<path d="{road_poly(widen=1.25)}" fill="{C["road"]}" opacity=".35" filter="url(#glow)"/>')
    o.append(f'<path d="{road_poly(widen=1.08)}" fill="{C2["edge"]}"/>')
    o.append(f'<path d="{road_poly()}" fill="url(#road)"/>')
    o.append(center_dashes())
    return "".join(o)


def milestone(t, label, state="past", side=1):
    """Lyktestolpe med månedsskilt. past = tent, now = her du står, future = slukket."""
    x, y = road_pt(t)
    k = max(.62, min(1.1, road_scale(t)))
    px = x + side * (road_w(t) / 2 + 10 * k)
    hgt = 46 * k
    lit = state in ("past", "now")
    o = [f'<path d="M{px:.1f} {y:.1f}v{-hgt:.1f}" stroke="#E9E2FF" stroke-width="{2.6*k:.1f}"/>']
    if lit:
        o.append(f'<circle cx="{px:.1f}" cy="{y-hgt:.1f}" r="{12*k:.1f}" fill="{C["lime"]}" opacity=".45" filter="url(#soft)"/>')
    o.append(f'<circle cx="{px:.1f}" cy="{y-hgt:.1f}" r="{4.5*k:.1f}" fill="{C["lime"] if lit else "#6C5AB0"}"/>')
    if True:
        w = len(label) * 7.6 * k + 16 * k
        bx = px + side * 8 * k - (w if side < 0 else 0)
        o.append(f'<rect x="{bx:.1f}" y="{y-hgt*0.7:.1f}" width="{w:.1f}" height="{20*k:.1f}" rx="{5*k:.1f}" fill="{"#fff" if state != "future" else "#2A1470"}" stroke="{"none" if state != "future" else "#6C5AB0"}"/>')
        o.append(T(f"{bx+w/2:.1f}", f"{y-hgt*0.7+14*k:.1f}", label, f"{12*k:.1f}", C["ink"] if state != "future" else "#E9E2FF", 800, "middle"))
    return "".join(o)


def age_gate(t, age, sub):
    """Port over veien ved nyttår: nytt nivå."""
    x, y = road_pt(t)
    k = max(.85, road_scale(t))
    w = max(road_w(t) * 1.7, 120)
    h = 66 * k
    o = [f'<path d="M{x-w/2:.1f} {y:.1f}v{-h:.1f}M{x+w/2:.1f} {y:.1f}v{-h:.1f}" stroke="{C["lime"]}" stroke-width="{5*k:.1f}" stroke-linecap="round"/>',
         f'<rect x="{x-w/2-6*k:.1f}" y="{y-h-20*k:.1f}" width="{w+12*k:.1f}" height="{24*k:.1f}" rx="{7*k:.1f}" fill="{C["lime"]}"/>',
         T(f"{x:.1f}", f"{y-h-3*k:.1f}", f"NIVÅ {age} · JANUAR", f"{12.5*k:.1f}", C["ink"], 900, "middle", 'letter-spacing=".6"'),
         f'<rect x="{x-w/2-6*k:.1f}" y="{y-h-20*k:.1f}" width="{w+12*k:.1f}" height="{24*k:.1f}" rx="{7*k:.1f}" fill="none" stroke="{C["lime"]}" stroke-width="6" opacity=".5" filter="url(#soft)"/>']
    if sub:
        o.append(T(f"{x+w/2+12*k:.1f}", f"{y-h+12*k:.1f}", sub, 11.5, "#E9E2FF", 700))
    return "".join(o)


def flag(x, y, label, sub, k=1):
    return (f'<path d="M{x} {y}v{-60*k}" stroke="#fff" stroke-width="{3*k}"/><path d="M{x} {y-60*k}h{30*k}l{-8*k} {10*k} {8*k} {10*k}h{-30*k}z" fill="{C["lime"]}"/>'
            f'<g filter="url(#sh)"><rect x="{x+6}" y="{y-34*k}" width="96" height="38" rx="10" fill="{C["panel"]}"/></g>'
            + T(x + 54, y - 34 * k + 17, label, 12, "#fff", 800, "middle") + T(x + 54, y - 34 * k + 31, sub, 11.5, C["lime"], 800, "middle"))


# ------------------------------------------------------------------ figurene
def person(x, y, k=1.0, top="#FF7A59", top2="#D85536", hair="#2A1A12", style="swoop", pants="#25307E", face=1, wave=False, rim="#FF9BC2"):
    """Ungdom i 3/4-profil. (x, y) = mellom føttene. Ca. 118k høy."""
    s = lambda v: f"{v*k:.1f}"
    X = lambda v: f"{x+v*k:.1f}"
    Y = lambda v: f"{y+v*k:.1f}"
    o = [f'<ellipse cx="{x}" cy="{Y(2)}" rx="{s(26)}" ry="{s(6)}" fill="#0B0426" opacity=".45"/>']
    # langt hår bak (Emma)
    if style == "long":
        o.append(f'<path d="M{X(-15)} {Y(-100)} C{X(-22)} {Y(-70)} {X(-20)} {Y(-56)} {X(-12)} {Y(-50)} L{X(14)} {Y(-52)} C{X(20)} {Y(-62)} {X(18)} {Y(-84)} {X(14)} {Y(-100)}Z" fill="{hair}"/>')
    # bein (jeans) og sko
    o.append(f'<path d="M{X(-12)} {Y(-48)} L{X(-15)} {Y(-8)} L{X(-4)} {Y(-8)} L{X(-1)} {Y(-40)} L{X(3)} {Y(-8)} L{X(14)} {Y(-8)} L{X(12)} {Y(-48)}Z" fill="{pants}"/>')
    o.append(f'<path d="M{X(-1)} {Y(-40)} L{X(1)} {Y(-14)}" stroke="#0B0426" stroke-width="{s(1.2)}" opacity=".35"/>')
    for sx, d in ((-10, -1), (9, 1)):
        o.append(f'<path d="M{X(sx-9)} {Y(-1)} q{s(0)} {s(-9)} {s(9)} {s(-10)} h{s(6)} q{s(10*d if d>0 else 4)} {s(2)} {s(10 if d>0 else 6)} {s(9)} q{s(0)} {s(3)} {s(-3)} {s(3)} h{s(-19)} q{s(-3)} 0 {s(-3)} {s(-3)}z" fill="#fff"/>')
        o.append(f'<path d="M{X(sx-9)} {Y(-1)}h{s(22)}" stroke="#C9C2E8" stroke-width="{s(2.4)}" stroke-linecap="round"/>')
        o.append(f'<path d="M{X(sx-3)} {Y(-6)}l{s(6)} {s(-3)}" stroke="{C["lime"]}" stroke-width="{s(2)}" stroke-linecap="round"/>')
    # overdel: genser/jakke
    o.append(f'<path d="M{X(-17)} {Y(-84)} Q{X(-21)} {Y(-60)} {X(-16)} {Y(-44)} Q{X(0)} {Y(-38)} {X(16)} {Y(-44)} Q{X(21)} {Y(-60)} {X(17)} {Y(-84)} Q{X(0)} {Y(-92)} {X(-17)} {Y(-84)}Z" fill="{top}"/>')
    o.append(f'<path d="M{X(6)} {Y(-88)} Q{X(19)} {Y(-82)} {X(17)} {Y(-60)} Q{X(18)} {Y(-48)} {X(16)} {Y(-44)} Q{X(10)} {Y(-41)} {X(6)} {Y(-41)}Z" fill="{top2}" opacity=".7"/>')
    o.append(f'<path d="M{X(-17)} {Y(-82)} Q{X(-21)} {Y(-60)} {X(-16)} {Y(-46)}" fill="none" stroke="{rim}" stroke-width="{s(2.2)}" opacity=".9"/>')
    if style != "long":
        # hette bak nakken, lomme og snorer
        o.append(f'<path d="M{X(-12)} {Y(-90)} Q{X(0)} {Y(-100)} {X(12)} {Y(-90)} Q{X(0)} {Y(-84)} {X(-12)} {Y(-90)}Z" fill="{top2}"/>')
        o.append(f'<path d="M{X(-10)} {Y(-60)} h{s(20)} q{s(3)} 0 {s(3)} {s(3)} v{s(9)} h{s(-26)} v{s(-9)} q0 {s(-3)} {s(3)} {s(-3)}z" fill="{top2}" opacity=".55"/>')
        o.append(f'<path d="M{X(-4)} {Y(-86)} v{s(12)} M{X(4)} {Y(-86)} v{s(10)}" stroke="#fff" stroke-width="{s(1.6)}" stroke-linecap="round"/>')
    else:
        o.append(f'<path d="M{X(0)} {Y(-88)} V{Y(-42)}" stroke="#B9AEE6" stroke-width="{s(1.4)}"/>')
        o.append(f'<path d="M{X(-17)} {Y(-70)} H{X(17)} M{X(-17)} {Y(-56)} H{X(17)}" stroke="#C9BEF2" stroke-width="{s(1.2)}" opacity=".8"/>')
    # armer
    if wave:
        o.append(f'<path d="M{X(14)} {Y(-82)} Q{X(28)} {Y(-90)} {X(30)} {Y(-110)}" stroke="{top}" stroke-width="{s(9)}" fill="none" stroke-linecap="round"/>')
        o.append(f'<circle cx="{X(30)}" cy="{Y(-114)}" r="{s(5)}" fill="{C["skin"]}"/>')
    else:
        o.append(f'<path d="M{X(15)} {Y(-82)} Q{X(22)} {Y(-66)} {X(18)} {Y(-50)}" stroke="{top2}" stroke-width="{s(9)}" fill="none" stroke-linecap="round"/>')
        o.append(f'<circle cx="{X(18)}" cy="{Y(-47)}" r="{s(4.6)}" fill="{C["skin"]}"/>')
    o.append(f'<path d="M{X(-15)} {Y(-82)} Q{X(-22)} {Y(-66)} {X(-19)} {Y(-50)}" stroke="{top}" stroke-width="{s(9)}" fill="none" stroke-linecap="round"/>')
    o.append(f'<circle cx="{X(-19)}" cy="{Y(-47)}" r="{s(4.6)}" fill="{C["skin"]}"/>')
    # hals og hode
    o.append(f'<rect x="{X(-4)}" y="{Y(-96)}" width="{s(8)}" height="{s(8)}" fill="{C["skin2"]}"/>')
    o.append(f'<path d="M{X(-12)} {Y(-112)} Q{X(-13)} {Y(-96)} {X(-1)} {Y(-93)} Q{X(12)} {Y(-95)} {X(12)} {Y(-110)} Q{X(12)} {Y(-126)} {X(0)} {Y(-127)} Q{X(-12)} {Y(-126)} {X(-12)} {Y(-112)}Z" fill="{C["skin"]}"/>')
    o.append(f'<ellipse cx="{X(-10*face)}" cy="{Y(-109)}" rx="{s(2.6)}" ry="{s(3.6)}" fill="{C["skin2"]}"/>')
    # hår
    if style == "swoop":
        o.append(f'<path d="M{X(-13)} {Y(-112)} Q{X(-16)} {Y(-130)} {X(0)} {Y(-132)} Q{X(16)} {Y(-133)} {X(15)} {Y(-118)} Q{X(8)} {Y(-124)} {X(-2)} {Y(-118)} Q{X(-6)} {Y(-122)} {X(-9)} {Y(-110)}Z" fill="{hair}"/>')
    elif style == "long":
        o.append(f'<path d="M{X(-14)} {Y(-108)} Q{X(-16)} {Y(-131)} {X(0)} {Y(-132)} Q{X(16)} {Y(-132)} {X(15)} {Y(-108)} Q{X(6)} {Y(-124)} {X(-6)} {Y(-118)} Q{X(-10)} {Y(-114)} {X(-14)} {Y(-108)}Z" fill="{hair}"/>')
    # ansikt (vendt mot face = 1 høyre, -1 venstre)
    ex = 5 * face
    o.append(f'<path d="M{X(ex-3)} {Y(-115)} q{s(3)} {s(-2)} {s(6)} 0" stroke="{hair}" stroke-width="{s(1.6)}" fill="none" stroke-linecap="round"/>')
    o.append(f'<ellipse cx="{X(ex)}" cy="{Y(-110)}" rx="{s(1.7)}" ry="{s(2.3)}" fill="#1E1450"/><circle cx="{X(ex+0.6)}" cy="{Y(-110.8)}" r="{s(.6)}" fill="#fff"/>')
    o.append(f'<path d="M{X(ex-3)} {Y(-102)} q{s(3)} {s(2.4)} {s(6)} 0" stroke="#8A3A2A" stroke-width="{s(1.5)}" fill="none" stroke-linecap="round"/>')
    o.append(f'<circle cx="{X(ex+4*face)}" cy="{Y(-105)}" r="{s(2.6)}" fill="#FF8A8A" opacity=".45"/>')
    return "".join(o)


# ------------------------------------------------------------------ HUD og meny
def phone_btn(x, y, n):
    o = f'<g transform="translate({x} {y})"><rect width="44" height="44" rx="14" fill="#12053A" opacity=".55"/><rect x="15" y="10" width="14" height="24" rx="3.5" fill="none" stroke="#fff" stroke-width="2.4"/>'
    if n:
        o += f'<circle cx="38" cy="6" r="10" fill="{C["lime"]}"/>' + T(38, 10.5, str(n), 12, C["ink"], 900, "middle")
    return o + "</g>"


def hud(month, age, done, current, sub=None, stats=True):
    o = ['<rect width="390" height="150" fill="#12053A" opacity=".0"/>', status(), level_badge(42, 86, age),
         T(76, 84, month, 28, "#fff", 900, extra='letter-spacing="-.5"')]
    o.append(T(76, 104, sub, 13, "#E9E2FF", 600) if sub else year_track(76, 94, 150, done, current))
    if stats:
        o.append(f'<g filter="url(#sh)"><rect x="20" y="128" width="128" height="36" rx="18" fill="#12053A" opacity=".72"/></g>' + coin(40, 146, 10) + T(58, 152, "3 120 kr", 16, "#fff", 900))
        o.append(f'<g filter="url(#sh)"><rect x="156" y="128" width="112" height="36" rx="18" fill="#12053A" opacity=".72"/></g>' + heart(176, 145, 1.05) + T(192, 152, "64", 16, "#fff", 900) + T(216, 152, "trivsel", 11.5, C["soft"], 600))
    return "".join(o)


def dock(go_label="GÅ", go_sub="til desember", badges=None):
    badges = badges or {}
    o = ['<rect x="0" y="630" width="390" height="214" fill="url(#fade)"/>']
    items = [("Plan", 46, 'M-9 -8h18v16h-18z M-9 -3h18 M-4 -11v5 M4 -11v5'), ("Jobb", 116, 'M-10 -4h20v12h-20z M-4 -4v-4h8v4'),
             ("Mobil", 274, 'M-6 -10h12v20h-12z M-2 6h4'), ("Penger", 344, 'M-10 -7h20v14h-20z M4 0h6 M-10 -2h20')]
    for name, x, d in items:
        o.append(f'<g filter="url(#sh)"><circle cx="{x}" cy="742" r="26" fill="#2A1470" stroke="#5B44B8" stroke-width="1.5"/></g>')
        o.append(f'<path transform="translate({x} 742)" d="{d}" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>')
        o.append(T(x, 786, name, 11.5, "#E9E2FF", 700, "middle"))
        if name in badges:
            o.append(f'<circle cx="{x+19}" cy="722" r="10" fill="{C["lime"]}"/>' + T(x + 19, 726.5, badges[name], 12, C["ink"], 900, "middle"))
    o.append(f'<circle cx="195" cy="736" r="54" fill="{C["lime"]}" opacity=".3" filter="url(#glow)"/>')
    o.append(f'<circle cx="195" cy="742" r="44" fill="{C["lime2"]}"/><circle cx="195" cy="736" r="44" fill="{C["lime"]}"/>')
    o.append(f'<path d="M168 716 a30 30 0 0 1 30 -12" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".6"/>')
    o.append(T(195, 738, go_label, 22, C["ink"], 900, "middle", 'letter-spacing="1"') + f'<path d="M184 750h22m-7-6 7 6-7 6" fill="none" stroke="{C["ink"]}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>')
    o.append(T(195, 804, go_sub, 12, C["lime"], 800, "middle"))
    o.append('<rect x="140" y="828" width="110" height="4" rx="2" fill="#fff" opacity=".5"/>')
    return "".join(o)


def bubble(x, y, lines, tail="left"):
    w = max(len(l) for l in lines) * 8.2 + 28
    h = 22 + 18 * len(lines)
    tx = x + 24 if tail == "left" else x + w - 30
    o = [f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#fff"/></g>', f'<path d="M{tx} {y+h-1}l-4 14 18-14z" fill="#fff"/>']
    for i, l in enumerate(lines):
        o.append(T(x + w / 2, y + 27 + i * 18, l, 14, C["ink"], 800, "middle"))
    return "".join(o)


def chunky(x, y, w, h, label, price, picked=False):
    fill = C["lime"] if picked else "#2A1470"
    tc = C["ink"] if picked else "#fff"
    return (f'<rect x="{x}" y="{y+5}" width="{w}" height="{h}" rx="16" fill="#0B0426"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="#5B44B8" stroke-width="1.5"/>'
            f'<rect x="{x+14}" y="{y+6}" width="{w*0.25:.0f}" height="4" rx="2" fill="#fff" opacity=".18"/>'
            + T(x + 18, y + h / 2 + 6, label, 16, tc, 700) + T(x + w - 16, y + h / 2 + 6, price, 16, C["ink"] if picked else C["lime"], 900, "end"))
