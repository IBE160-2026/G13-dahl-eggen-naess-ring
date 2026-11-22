# Konsept «Veien»: felles byggeklosser (scene, HUD, panel, knapper) for alle skjermene.
# Fargeregel: fiolett-familien er verden, turkis er veien, lime er handling.
# Rosa er reservert for det som presser (gjeld, stress, krise) og for skumringslyset.
import math

C = {
    "sky0": "#24107A", "sky1": "#6A22E0", "sky2": "#FF6FA8", "sun": "#FFD36E",
    "far": "#9A55FF", "mid": "#6A25D9", "near": "#3D1499", "front": "#2A0D73",
    "road": "#2FE3D2", "road2": "#A9FFF6",
    "lime": "#B4E86E", "lime2": "#7FAE45",
    "panel": "#170A40", "panel2": "#24125E", "line": "#3A2580",
    "text": "#FFFFFF", "soft": "#C9BEF2", "ink": "#170A40",
    "press": "#FF5D8F", "skin": "#FFD2B8", "skin2": "#B87452",
}
FONT = "family=Rubik:wght@400;500;700;800;900"
FAM = "Rubik, sans-serif"

_uid = [0]


def uid(p="u"):
    _uid[0] += 1
    return f"{p}{_uid[0]}"


def T(x, y, s, size, fill=None, w=500, anchor="start", extra=""):
    fill = fill or C["text"]
    return f'<text x="{x}" y="{y}" font-family="{FAM}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'


def page(title, body, bg=None):
    bg = bg or C["panel"]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="390" height="844" viewBox="0 0 390 844">
  <title>{title}</title>
  <defs>
    <style>@import url('https://fonts.googleapis.com/css2?{FONT}&amp;display=block');</style>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C['sky0']}"/><stop offset=".3" stop-color="{C['sky1']}"/><stop offset=".56" stop-color="{C['sky2']}"/></linearGradient>
    <filter id="sh" x="-20%" y="-20%" width="140%" height="170%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#0B0426" flood-opacity=".45"/></filter>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
  </defs>
  <rect width="390" height="844" fill="{bg}"/>
{body}
</svg>"""


# ------------------------------------------------------------------ scenen
def stars(h):
    pts = [(30, 60), (88, 120), (140, 48), (212, 96), (250, 40), (318, 128), (360, 70), (176, 150), (60, 170), (330, 190)]
    return "".join(f'<circle cx="{x}" cy="{y}" r="{1.6 if i % 3 else 2.2}" fill="#fff" opacity="{.5 if i % 2 else .85}"/>' for i, (x, y) in enumerate(pts) if y < h - 120)


def pine(x, y, s, fill):
    return f'<path d="M{x} {y-34*s} L{x+11*s} {y-12*s} H{x+6*s} L{x+15*s} {y} H{x-15*s} L{x-6*s} {y-12*s} H{x-11*s} Z" fill="{fill}"/>'


def scene(h=486, road=True, sun=True, cabin=None, extra=""):
    """Skumringslandskap. h = hvor scenen slutter (panelet starter der)."""
    o = [f'<rect width="390" height="{h+30}" fill="url(#sky)"/>', stars(h)]
    if sun:
        o.append(f'<circle cx="286" cy="{h-214}" r="58" fill="{C["sun"]}" opacity=".25" filter="url(#glow)"/><circle cx="286" cy="{h-214}" r="44" fill="{C["sun"]}"/>')
    o.append(f'<path d="M0 {h-190} C60 {h-232} 120 {h-200} 170 {h-226} S280 {h-250} 390 {h-206} V{h+30} H0Z" fill="{C["far"]}"/>')
    o.append(pine(70, h - 196, .7, C["mid"]) + pine(92, h - 192, .55, C["mid"]))
    o.append(f'<path d="M0 {h-128} C80 {h-170} 160 {h-130} 240 {h-160} S350 {h-170} 390 {h-150} V{h+30} H0Z" fill="{C["mid"]}"/>')
    o.append(pine(330, h - 150, .9, C["near"]) + pine(356, h - 146, .7, C["near"]) + pine(30, h - 128, 1, C["near"]))
    if cabin:
        o.append(cabin)
    o.append(f'<path d="M0 {h-66} C110 {h-96} 210 {h-60} 300 {h-86} S370 {h-92} 390 {h-86} V{h+30} H0Z" fill="{C["near"]}"/>')
    if road:
        rd = f"M10 {h+30} C110 {h-40} 190 {h-80} 250 {h-118} S330 {h-178} 360 {h-200}"
        o.append(f'<path d="{rd}" fill="none" stroke="{C["road"]}" stroke-width="30" stroke-linecap="round" opacity=".28" filter="url(#glow)"/>')
        o.append(f'<path d="{rd}" fill="none" stroke="{C["road"]}" stroke-width="20" stroke-linecap="round"/>')
        o.append(f'<path d="{rd}" fill="none" stroke="{C["road2"]}" stroke-width="3" stroke-dasharray="3 14" stroke-linecap="round"/>')
    o.append(f'<path d="M0 {h-14} C120 {h-34} 260 {h-6} 390 {h-24} V{h+30} H0Z" fill="{C["front"]}"/>')
    o.append(extra)
    return "".join(o)


def cabin(x, y, lit=False):
    win = C["sun"] if lit else C["mid"]
    o = (f'<g transform="translate({x} {y})"><path d="M0 28 L30 4 L60 28 V58 H0Z" fill="{C["front"]}"/><rect x="40" y="-2" width="8" height="18" fill="{C["front"]}"/>'
         f'<rect x="10" y="34" width="12" height="12" rx="2" fill="{win}"/><rect x="38" y="34" width="12" height="12" rx="2" fill="{win}"/>')
    if lit:
        o += f'<rect x="4" y="30" width="52" height="20" fill="{C["sun"]}" opacity=".25" filter="url(#glow)"/>'
        o += '<path d="M44 -6c-6-9 6-13 0-22s6-13 0-20" fill="none" stroke="#fff" stroke-width="3" opacity=".55" stroke-linecap="round"/>'
    return o + "</g>"


def hero(x, y, s=1.0, hoodie="#FF7A59", hair="#2A1A12", wave=False, look=1):
    """Spillerfiguren: hettegenser, bukse, joggesko. Stående, sett litt fra siden."""
    k = s
    arm = (f'<path d="M{x+10*k} {y-50*k} q{14*k} {-10*k} {18*k} {-26*k}" stroke="{hoodie}" stroke-width="{8*k}" fill="none" stroke-linecap="round"/>'
           if wave else f'<path d="M{x+10*k} {y-50*k} q{6*k} {12*k} {4*k} {24*k}" stroke="{hoodie}" stroke-width="{8*k}" fill="none" stroke-linecap="round"/>')
    return (f'<ellipse cx="{x}" cy="{y+2*k}" rx="{18*k}" ry="{5*k}" fill="#0B0426" opacity=".35"/>'
            f'<path d="M{x-6*k} {y-26*k} l{-5*k} {24*k} M{x+6*k} {y-26*k} l{6*k} {24*k}" stroke="#1E1450" stroke-width="{9*k}" stroke-linecap="round"/>'
            f'<rect x="{x-16*k}" y="{y-4*k}" width="{14*k}" height="{7*k}" rx="{3.5*k}" fill="#fff"/><rect x="{x+4*k}" y="{y-4*k}" width="{14*k}" height="{7*k}" rx="{3.5*k}" fill="#fff"/>'
            f'<rect x="{x-14*k}" y="{y-62*k}" width="{28*k}" height="{40*k}" rx="{12*k}" fill="{hoodie}"/>'
            f'<path d="M{x-8*k} {y-34*k}h{16*k}" stroke="#0B0426" stroke-width="{2*k}" opacity=".25"/>'
            + arm +
            f'<circle cx="{x}" cy="{y-74*k}" r="{12*k}" fill="{C["skin"]}"/>'
            f'<path d="M{x-12*k} {y-76*k} q{2*k} {-16*k} {14*k} {-14*k} q{12*k} {0} {10*k} {12*k} q{-8*k} {-6*k} {-24*k} {2*k}z" fill="{hair}"/>'
            f'<circle cx="{x+5*k*look}" cy="{y-74*k}" r="{1.6*k}" fill="#1E1450"/>')


def sign(x, y, label, sub=None, w=None):
    w = w or (len(label) * 8.4 + 24)
    o = f'<path d="M{x} {y}v-38" stroke="#fff" stroke-width="3"/><g filter="url(#sh)"><rect x="{x-w/2}" y="{y-66}" width="{w}" height="{30 if not sub else 44}" rx="8" fill="#fff"/></g>'
    o += T(x, y - 46, label, 13, C["ink"], 800, "middle")
    if sub:
        o += T(x, y - 30, sub, 11, "#5A4C8C", 500, "middle")
    return o


def goal_flag(x, y, label, pct):
    return (f'<path d="M{x} {y}v-56" stroke="#fff" stroke-width="3"/><path d="M{x} {y-56}h30l-8 10 8 10h-30z" fill="{C["lime"]}"/>'
            + f'<rect x="{x-96}" y="{y-82}" width="88" height="38" rx="10" fill="{C["panel"]}" opacity=".88"/>'
            + T(x - 52, y - 66, label, 12, "#fff", 800, "middle") + T(x - 52, y - 51, f"{pct} % spart", 11.5, C["lime"], 800, "middle"))


# ------------------------------------------------------------------ HUD
def status(fill="#fff"):
    return (T(24, 30, "9:41", 15, fill, 600) +
            f'<g fill="{fill}"><rect x="331" y="19" width="23" height="11" rx="3" fill="none" stroke="{fill}" stroke-width="1.4"/><rect x="333.5" y="21.5" width="16" height="6" rx="1.2"/></g>')


def level_badge(x, y, age):
    """Alderen som nivåmerke."""
    return (f'<g filter="url(#sh)"><path d="M{x} {y-22} l19 11 v22 l-19 11 l-19 -11 v-22z" fill="{C["lime"]}"/></g>'
            + T(x, y + 7, str(age), 18, C["ink"], 900, "middle") + T(x, y + 30, "ÅR", 9.5, "#fff", 800, "middle", 'letter-spacing="1.5"'))


def year_track(x, y, w, done, current, active=(0, 3, 6, 9)):
    """Året som tolv biter. Hendelsesmåneder er litt høyere. Ingen tall."""
    gap = 3
    sw = (w - gap * 11) / 12
    o = []
    for i in range(12):
        hx = x + i * (sw + gap)
        hh = 8 if i in active else 5
        yy = y + (8 - hh) / 2
        if i < done:
            f, op = "#fff", 1
        elif i == current:
            f, op = C["lime"], 1
        else:
            f, op = "#fff", .28
        o.append(f'<rect x="{hx:.1f}" y="{yy}" width="{sw:.1f}" height="{hh}" rx="{hh/2}" fill="{f}" opacity="{op}"/>')
    return "".join(o)


def phone_btn(x, y, n):
    o = f'<g transform="translate({x} {y})"><rect width="44" height="44" rx="14" fill="#fff" opacity=".16"/><rect x="15" y="10" width="14" height="24" rx="3.5" fill="none" stroke="#fff" stroke-width="2.4"/>'
    if n:
        o += f'<circle cx="38" cy="6" r="10" fill="{C["lime"]}"/>' + T(38, 10.5, str(n), 12, C["ink"], 900, "middle")
    return o + "</g>"


def header(month, age, done, current, msgs=2, sub=None):
    o = [status(), level_badge(42, 86, age), T(76, 84, month, 28, "#fff", 900, extra='letter-spacing="-.5"')]
    o.append(T(76, 104, sub, 13, C["soft"], 500) if sub else year_track(76, 94, 150, done, current))
    o.append(phone_btn(326, 62, msgs))
    return "".join(o)


# ------------------------------------------------------------------ panel og knapper
def panel(y):
    return (f'<path d="M0 {y+28} Q0 {y} 28 {y} H362 Q390 {y} 390 {y+28} V844 H0Z" fill="{C["panel"]}"/>'
            f'<rect x="170" y="{y+10}" width="50" height="5" rx="2.5" fill="{C["line"]}"/>')


def cta(y, label, x=20, w=350, arrow=True):
    o = (f'<rect x="{x}" y="{y+6}" width="{w}" height="58" rx="18" fill="{C["lime2"]}"/>'
         f'<rect x="{x}" y="{y}" width="{w}" height="58" rx="18" fill="{C["lime"]}"/>'
         f'<rect x="{x+16}" y="{y+8}" width="{w*0.3:.0f}" height="5" rx="2.5" fill="#fff" opacity=".55"/>'
         + T(x + w / 2 - (10 if arrow else 0), y + 37, label, 18, C["ink"], 900, "middle", 'letter-spacing=".8"'))
    if arrow:
        o += f'<path d="M{x+w-46} {y+29}h18m-7-7 7 7-7 7" fill="none" stroke="{C["ink"]}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>'
    return o


def ghost(y, label, x=20, w=350):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="52" rx="16" fill="none" stroke="{C["soft"]}" stroke-width="2"/>'
            + T(x + w / 2, y + 32, label, 16, "#fff", 700, "middle"))


def option(y, label, price, sub=None, x=20, w=350, state="idle"):
    fill = C["panel2"] if state != "picked" else C["lime"]
    tc = "#fff" if state != "picked" else C["ink"]
    pc = C["lime"] if state != "picked" else C["ink"]
    h = 62
    o = (f'<rect x="{x}" y="{y+4}" width="{w}" height="{h}" rx="16" fill="#0E0630"/>'
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{C["line"] if state != "picked" else C["lime"]}" stroke-width="1.5"/>')
    o += T(x + 20, y + (28 if sub else 37), label, 16, tc, 700)
    if sub:
        o += T(x + 20, y + 47, sub, 12.5, C["soft"] if state != "picked" else C["ink"], 400)
    o += T(x + w - 18, y + 37, price, 16, pc, 900, "end")
    return o


def coin(x, y, r=9):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C["sun"]}"/><circle cx="{x}" cy="{y}" r="{r*0.62}" fill="none" stroke="#C99A2E" stroke-width="1.8"/>'


def heart(x, y, s=1, fill=None):
    fill = fill or C["press"]
    return f'<path transform="translate({x} {y}) scale({s})" d="M0 6 C-10 -2 -8 -10 -2 -10 C1 -10 0 -7 0 -6 C0 -7 -1 -10 2 -10 C8 -10 10 -2 0 6Z" fill="{fill}"/>'


def wellbeing_bar(x, y, w, val, new=0, thr=50, h=10):
    n = 20
    gap = 2.5
    sw = (w - gap * (n - 1)) / n
    lit = round(val / 5)
    o = []
    for i in range(n):
        if i < lit - new:
            f = C["lime"]
        elif i < lit:
            f = "#fff"
        else:
            f = "#6B57C9"
        o.append(f'<rect x="{x+i*(sw+gap):.1f}" y="{y}" width="{sw:.1f}" height="{h}" rx="2" fill="{f}"/>')
    mx = x + (thr / 5) * (sw + gap) - gap / 2
    o.append(f'<path d="M{mx:.1f} {y-5}v{h+10}" stroke="#fff" stroke-width="2"/>')
    return "".join(o)


def avatar(cx, cy, r, letter, fill):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>' + T(cx, cy + r * 0.36, letter, r * 0.95, C["ink"], 900, "middle")


def tabbar(active="Veien"):
    tabs = ["Veien", "Plan", "Mobil", "Jobb", "Penger"]
    o = [f'<rect x="0" y="776" width="390" height="68" fill="{C["panel"]}"/>', f'<path d="M0 776H390" stroke="{C["line"]}"/>']
    icons = {
        "Veien": 'M-8 6 C-2 -2 2 2 8 -6',
        "Plan": 'M-8 -7h16v14h-16z M-8 -2h16',
        "Mobil": 'M-5 -8h10v16h-10z',
        "Jobb": 'M-8 -3h16v10h-16z M-3 -3v-4h6v4',
        "Penger": 'M-8 -6h16v12h-16z M3 0h5',
    }
    for i, t in enumerate(tabs):
        cx = 39 + i * 78
        on = t == active
        col = C["lime"] if on else C["soft"]
        o.append(f'<path transform="translate({cx} 796)" d="{icons[t]}" fill="none" stroke="{col}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
        o.append(T(cx, 822, t, 11.5, col, 800 if on else 500, "middle"))
    o.append('<rect x="140" y="834" width="110" height="4" rx="2" fill="#fff" opacity=".5"/>')
    return "".join(o)


def float_tag(x, y, label, fill, tc=None):
    w = len(label) * 8.2 + 22
    tc = tc or C["ink"]
    return (f'<g filter="url(#sh)"><rect x="{x-w/2}" y="{y-16}" width="{w}" height="30" rx="15" fill="{fill}"/></g>'
            + T(x, y + 4, label, 14, tc, 900, "middle"))


def burst(cx, cy, r1, r2, col, n=10):
    o = []
    for i in range(n):
        a = math.radians(i * 360 / n + 8)
        o.append(f'<path d="M{cx+math.cos(a)*r1:.0f} {cy+math.sin(a)*r1:.0f}L{cx+math.cos(a)*r2:.0f} {cy+math.sin(a)*r2:.0f}" stroke="{col}" stroke-width="3.5" stroke-linecap="round"/>')
    return "".join(o)
