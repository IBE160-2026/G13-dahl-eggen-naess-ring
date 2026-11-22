# Kontrastmåling mot WCAG 2.2 AA for alle tekst/bakgrunn-par i «Veien»-skissene.
# Krav: 4.5:1 for vanlig tekst, 3:1 for stor tekst (>= 24px, eller >= 18.66px fet)
# og 3:1 for grafiske elementer og grenser på kontroller (1.4.11).
# Halvgjennomsiktige felt er blandet med bakgrunnen de ligger over.
import sys
from veien import C

PANEL, P2, P3, LINE = C["panel"], "#24125E", "#2A1470", "#5B44B8"
SOFT, LIME, INK, PRESS, SUN, ROAD = C["soft"], C["lime"], C["ink"], C["press"], C["sun"], C["road"]
DARK = "#12053A"


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def hexc(c):
    return "#" + "".join(f"{round(v):02X}" for v in c)


def mix(top, bottom, a):
    t, b = rgb(top), rgb(bottom)
    return hexc(tuple(t[i] * a + b[i] * (1 - a) for i in range(3)))


def lum(h):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb(h)
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def sky(t):
    """Himmelgradienten: 0 = sky0, .55 = sky1, 1 = sky2 (relativt til rektangelet)."""
    stops = [(0, C["sky0"]), (.55, C["sky1"]), (1, C["sky2"])]
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t <= t1:
            return mix(c1, c0, (t - t0) / (t1 - t0))
    return C["sky2"]


# (skjerm, element, tekstfarge, bakgrunn, størrelse px, fet, type) — type: tekst | grafikk
P = []
def add(s, e, fg, bg, size=14, bold=False, kind="tekst"):
    P.append((s, e, fg, bg, size, bold, kind))


# --- tekst rett på himmelen (landskap: rektangel 300 px, bånd: egen høyde)
add("08,12,13,20,21", "Månedsnavn i HUD", "#FFFFFF", sky(80 / 300), 27, True)
add("08,12,13,20,21", "Undertekst «År 3 av 5»", "#E9E2FF", sky(99 / 300), 12.5, True)
add("08 m.fl.", "«ÅR» under nivåmerket", "#FFFFFF", sky(116 / 300), 9.5, True)
add("alle", "Klokka i statuslinja", "#FFFFFF", sky(30 / 300), 15, True)
add("01", "Logo «LifeMode»", "#FFFFFF", sky(132 / 300), 50, True)
add("01", "Slagord under logoen", "#E9E2FF", sky(166 / 300), 16, True)
add("23", "«År 3 er ferdig!»", "#FFFFFF", sky(100 / 300), 32, True)
add("23", "Undertekst under", "#E9E2FF", sky(128 / 300), 15, True)
add("02,15–18,26,27", "Sidetittel (bånd 170 px)", "#FFFFFF", sky(72 / 170), 26, True)
add("03,04", "Sidetittel (bånd 240 px)", "#FFFFFF", sky(72 / 240), 26, True)
add("19", "Sidetittel (bånd 150 px)", "#FFFFFF", sky(72 / 150), 26, True)
add("20,21", "HUD-undertekst med rosa skjær", "#E9E2FF", mix(PRESS, sky(99 / 300), .10), 12.5, True)
# --- HUD-brikker: mørkt felt med 72 % dekning over himmelen
pill = mix(DARK, sky(190 / 300), .72)
add("08,09", "Saldo i HUD-brikke", "#FFFFFF", pill, 16, True)
add("08,09", "«trivsel» i HUD-brikke", SOFT, pill, 11.5, True)
yl = mix(DARK, sky(133 / 300), .6)
add("08,09", "Bokstaver i årslinja (HUD)", "#E9E2FF", yl, 9.5, True)
add("08,09", "Inneværende måned i årslinja", LIME, yl, 9.5, True)
add("08,09", "Punkter i årslinja", "#FFFFFF", yl, kind="grafikk")
# --- dokk nederst (mørk toning over bakken)
dock_bg = mix(DARK, "#1C0858", .93)
add("08,09", "Etiketter i dokken", "#E9E2FF", dock_bg, 11.5, True)
add("08,09", "«til desember» under GÅ", LIME, dock_bg, 12, True)
add("08,09", "GÅ-knappen mot bakgrunnen", LIME, dock_bg, kind="grafikk")
add("08,09", "Merketall på dokk-knapp", INK, LIME, 12, True)
# --- skilt, port, flagg og flytende tall
add("08", "Milepæl (passert) «OKT»", INK, "#FFFFFF", 12, True)
add("08", "Milepæl (kommende) «DES»", "#E9E2FF", P3, 7.5, True)
add("08", "Port «NIVÅ 18 · JANUAR»", INK, LIME, 10.6, True)
add("08", "Flagg «Førerkort»", "#FFFFFF", mix(PANEL, sky(.7), .88), 12, True)
add("08", "Flagg «75 % spart»", LIME, mix(PANEL, sky(.7), .88), 11.5, True)
add("07,13", "Svevende tall på gult", INK, SUN, 14, True)
add("13", "Svevende tall på lime", INK, LIME, 14, True)
add("13", "Svevende tall på turkis", INK, ROAD, 14, True)
add("20", "Svevende tall på rosa («10 000 kr gjeld»)", INK, PRESS, 14, True)
add("21", "«STEG 1 AV 3» på rosa", INK, PRESS, 13, True)
add("12", "Snakkeboble", INK, "#FFFFFF", 14, True)
# --- dialogbokser og mørke paneler
for s, e, fg, size, bold in [("alle", "Brødtekst hvit", "#FFFFFF", 13, False), ("alle", "Dempet tekst", SOFT, 12, False),
                             ("13,15,17", "Limegrønn tekst", LIME, 12.5, True), ("23,24", "Gul tekst «Neste år»", SUN, 15, True),
                             ("16,25,26", "Rosa varseltekst", "#FFB3C9", 13.5, True)]:
    add(s, e + " på panel", fg, PANEL, size, bold)
add("alle", "Hvit tekst på kort", "#FFFFFF", P2, 13, False)
add("alle", "Dempet tekst på kort", SOFT, P2, 12, False)
add("17,25", "Lime tekst på kort", LIME, P2, 13, True)
add("25", "Rosa tall på kort", "#FFB3C9", P2, 15, True)
add("12,20,21", "Valgknapp: tekst", "#FFFFFF", P3, 16, True)
add("12,20,21", "Valgknapp: pris i lime", LIME, P3, 16, True)
add("13", "Ekko-tittel i lime", LIME, P3, 14, True)
add("15", "Skole/Ekstravakt-blokk", SOFT, "#3A2580", 11.5, True)
add("15", "Aktivitet på gult kort", INK, SUN, 13, True)
add("15", "Aktivitet på rosa kort", INK, "#FF9BC2", 13, True)
add("alle", "Hovedknapp", INK, LIME, 17, True)
add("19", "Valgt år-fane", INK, LIME, 13, True)
add("19", "«Du er her» på kort", LIME, P2, 12.5, True)
add("02,03", "Feltgrense mot feltet", "#7E68D8", P2, kind="grafikk")
add("02,03", "Feltgrense mot panelet rundt", "#7E68D8", PANEL, kind="grafikk")
add("02,03", "Avkrysningsboks (tom)", SOFT, PANEL, kind="grafikk")
add("15", "Stiplet ledig plass", LIME, PANEL, kind="grafikk")
add("18", "Trivselsstolpe lime mot spor", LIME, "#3A2580", kind="grafikk")
add("18", "Stress-stolpe rosa mot spor", PRESS, "#3A2580", kind="grafikk")
add("18", "Fritid-stolpe turkis mot spor", ROAD, "#3A2580", kind="grafikk")
add("13", "Trivselssegment tomt mot panel", "#6B57C9", PANEL, kind="grafikk")
add("18", "Kant på stolpespor mot panel", "#6B57C9", PANEL, kind="grafikk")
add("13", "Fylt trivselssegment mot tomt", LIME, "#6B57C9", kind="grafikk")
# --- telefonens egne skjermer (lyse)
add("09", "SMS-varsel: «MELDINGER»/tid", "#6B6B76", "#F4F3F8", 11.5, False)
add("09", "SMS-varsel: avsender og tekst", "#222222", "#F4F3F8", 14.5, False)
add("10", "Meldinger: forhåndsvisning og tid", "#6C6C70", "#FFFFFF", 15, False)
add("10", "Meldinger: blå lenker «Spill», «Rediger»", "#0066CC", "#FFFFFF", 17, False)
add("10", "Meldinger: søkefelt", "#6C6C70", "#EFEFF4", 16, False)
add("10", "Meldinger: bunntekst", "#6C6C70", "#F7F7F9", 12.5, False)
add("10", "Meldinger: blå ulest-prikk", "#0066CC", "#FFFFFF", kind="grafikk")
add("11", "Samtale: boble", "#111111", "#E9E9EB", 15.5, False)
add("11", "Samtale: «Oktober», «I dag», «Levert»", "#6C6C70", "#FFFFFF", 12, True)
add("11", "Samtale: svarfelt «Du kan ikke svare»", "#6C6C70", "#FFFFFF", 15, False)
add("11", "Invitasjonskort: dempet tekst", SOFT, PANEL, 12.5, True)
add("28", "Frakoblet-varsel: undertekst", "#4A3D7A", "#FFFFFF", 12.5, True)
# --- kjørespill
add("22", "Vei mot gress", "#1F2230", "#2E7D4F", kind="grafikk")
add("22", "Mopeden mot veien", ROAD, "#1F2230", kind="grafikk")
add("22", "Bilen mot veien", SUN, "#1F2230", kind="grafikk")


def need(size, bold, kind):
    if kind == "grafikk":
        return 3.0, "grafikk"
    large = size >= 24 or (bold and size >= 18.66)
    return (3.0, "stor") if large else (4.5, "vanlig")


fails = 0
print(f"{'':2}{'ratio':>6}  {'krav':>4}  {'type':<8} skjerm      element")
for s, e, fg, bg, size, bold, kind in P:
    r = ratio(fg, bg)
    req, typ = need(size, bold, kind)
    ok = r >= req
    fails += not ok
    print(f"{'  ' if ok else 'X '}{r:6.2f}  {req:4.1f}  {typ:<8} {s:<11} {e}  ({fg} på {bg})")
print(f"\n{len(P)} par målt, {fails} under kravet.")
sys.exit(0)
