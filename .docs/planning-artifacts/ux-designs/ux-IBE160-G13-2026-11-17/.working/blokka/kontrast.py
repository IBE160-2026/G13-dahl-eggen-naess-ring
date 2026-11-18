# Kontrastmåling mot WCAG 2.2 AA for «Blokka» (Fjord-paletten).
# Krav: 4.5:1 vanlig tekst, 3:1 stor tekst (>= 24px, eller >= 18.66px fet), 3:1 grafikk og kontrollgrenser.
import sys
from skjermer import PALETTES

P = PALETTES["fjord"]
INK, SOFT, ACT, ACT2, TINT, PRESS = P["ink"], P["soft"], P["cobalt"], P["cobalt2"], P["tint"], P["press"]
SKY, SKY2, PANEL, LINE = P["sky"], P["sky2"], P["panel"], P["line"]
Y = {i: P[f"y{i}"] for i in range(1, 6)}
LIT, WHITE = "#FFD45C", "#FFFFFF"


def rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


def lum(h):
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = map(f, rgb(h))
    return .2126 * r + .7152 * g + .0722 * b


def ratio(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + .05) / (y + .05)


PAIRS = []
def add(s, e, fg, bg, size=14, bold=False, kind="tekst"):
    PAIRS.append((s, e, fg, bg, size, bold, kind))


# himmel og lyse flater
add("alle", "Tittel på himmelen", INK, SKY, 26, True)
add("alle", "Undertittel på himmelen", SOFT, SKY, 14, True)
add("08", "Saldo, trivsel og mål i toppen", INK, SKY, 15, True)
add("alle", "Brødtekst på lys flate", INK, SKY2, 14)
add("alle", "Dempet tekst på lys flate", SOFT, SKY2, 12)
add("alle", "Dempet tekst på hvitt kort", SOFT, WHITE, 12.5)
add("alle", "Dempet tekst på grått kort", SOFT, PANEL, 12.5)
add("alle", "Lenke i handlingsfarge", ACT, SKY2, 14, True)
add("16,26", "Rød lenke («Si opp», «Slett»)", PRESS, SKY2, 13.5, True)
add("20,25", "Røde tall på lys flate", PRESS, SKY2, 15, True)
add("25", "Røde tall på hvitt kort", PRESS, WHITE, 15, True)
# etasjeviser
add("alle", "Etasjetall i heisviseren", LIT, INK, 26, True)
add("alle", "«ETG» i heisviseren", "#9FB0C8", INK, 9.5, True)
# månedsstripa
add("08,23,24", "Spilt måned i stripa", ACT2, TINT, 9.5, True)
add("08,23,24", "Denne måneden i stripa", WHITE, ACT, 9.5, True)
add("08,23,24", "Kommende måned i stripa", SOFT, WHITE, 9.5, True)
add("08,23,24", "Kant på rutene i stripa", "#7C8F8A", WHITE, kind="grafikk")
# knapper og kontroller
add("alle", "Hovedknapp", WHITE, ACT, 17, True)
add("08", "«desember» i hovedknappen", "#C9D4FF", ACT, 14, False)
add("alle", "Valgknapp: tekst", INK, WHITE, 16, True)
add("alle", "Valgknapp: pris", ACT, WHITE, 16, True)
add("alle", "Valgknapp: kant mot bakgrunnen", ACT, SKY2, kind="grafikk")
add("08", "Ringeklokke: navn", INK, WHITE, 14.5, True)
add("08", "Ringeklokke: merknad", ACT, WHITE, 11.5, True)
add("08", "Ringeklokke: knapp mot skiltet", ACT, WHITE, kind="grafikk")
add("02–04", "Tekstfelt: kant", "#7C8F8A", WHITE, kind="grafikk")
add("02–04", "Tekstfelt: kant mot bakgrunnen", "#7C8F8A", SKY2, kind="grafikk")
add("02,03", "Avkrysningsboks: kant", "#7C8F8A", SKY2, kind="grafikk")
add("16", "Pluss/minus-knapp: kant", "#5F7470", PANEL, kind="grafikk")
# merkelapper i scenen
add("08", "«År 3 · din etasje»", WHITE, INK, 12, True)
add("01", "År-merke (lys)", INK, WHITE, 11, True)
add("13", "«Nytt på veggen»", WHITE, INK, 11.5, True)
add("07", "«+18 400 kr» på gult", INK, LIT, 14, True)
add("13", "Lapp gul", INK, LIT, 10, True)
add("13", "Lapp blå", INK, "#BFE3F5", 10, True)
add("13", "Lapp rosa", INK, "#F7C5C0", 10, True)
add("20", "«10 000 kr gjeld» på rødt", WHITE, PRESS, 13.5, True)
add("21", "«STEG 1 AV 3» på rødt", WHITE, PRESS, 12.5, True)
add("12", "Snakkeboble", INK, WHITE, 14.5, True)
add("01,16", "Skilt «BUTIKKEN»", WHITE, PRESS, 8, True)
add("01,17", "Skilt «BANKEN»", WHITE, ACT, 8, True)
# årsfarger med tekst
for i in range(1, 5):
    add("19,25", f"Tekst på årsfarge {i}", INK, Y[i], 13, True)
add("19", "Tekst på År 5-fanen (lysere tyttebær)", INK, "#D98A98", 13, True)
add("10–12", "Avsender-ikon Emma (hvit bokstav)", WHITE, "#24705E", 15, True)
add("07,10", "Avsender-ikon Mamma (hvit bokstav)", WHITE, "#A9475A", 15, True)
# trivsel og stolper
add("13,18", "Tent vindu mot slukket vindu", LIT, "#5C6F8C", kind="grafikk")
add("13,18", "Kant og slukkede vinduer mot bakgrunnen", "#5C6F8C", SKY2, kind="grafikk")
add("13", "Kant på nyeste vindu mot bakgrunnen", ACT, SKY2, kind="grafikk")
add("18", "Stress-stolpe mot hvitt spor", PRESS, WHITE, kind="grafikk")
add("18", "Fritid-stolpe mot hvitt spor", "#4A7AA8", WHITE, kind="grafikk")
add("18", "Sosialt-stolpe mot hvitt spor", "#5E7E4E", WHITE, kind="grafikk")
add("17", "Sparemål-stolpe mot hvitt spor", ACT, WHITE, kind="grafikk")
add("17,18", "Spor-kant mot bakgrunnen", "#7C8F8A", SKY2, kind="grafikk")
# telefonens egne skjermer
add("09", "SMS-varsel: «MELDINGER»", "#5E5E66", "#F4F3F8", 11.5)
add("10", "Meldinger: grå tekst", "#6C6C70", WHITE, 15)
add("10", "Meldinger: blå lenker", "#0066CC", WHITE, 17)
add("10", "Meldinger: søk", "#6C6C70", "#EFEFF4", 16)
add("10", "Avatar-bokstav på multebær", INK, Y[1], 22, True)
add("10", "Avatar-bokstav på fjordblå", INK, Y[4], 22, True)
add("10", "Avatar-bokstav på mørk tyttebær", WHITE, "#A9475A", 22, True)
add("10", "Avatar-bokstav på handlingsfarge", WHITE, ACT, 22, True)
add("11", "Svarfelt «Du kan ikke svare»", "#6C6C70", WHITE, 15)
add("28", "Frakoblet: undertekst", "#D5E6E2", INK, 12.5)
# kjørespill
add("22", "Vei mot gress", "#2F3640", "#8FC59A", kind="grafikk")
add("22", "Mopeden mot veien", "#3DB8A5", "#2F3640", kind="grafikk")
add("22", "Bilen mot veien", "#FFD45C", "#2F3640", kind="grafikk")
add("22", "Kjørepil mot gress", ACT, "#8FC59A", kind="grafikk")
add("22", "Fremdriftsstrek (tom) mot himmel", ACT, SKY, kind="grafikk")


def need(size, bold, kind):
    if kind == "grafikk":
        return 3.0, "grafikk"
    large = size >= 24 or (bold and size >= 18.66)
    return (3.0, "stor") if large else (4.5, "vanlig")


fails = 0
for s, e, fg, bg, size, bold, kind in PAIRS:
    r = ratio(fg, bg)
    req, typ = need(size, bold, kind)
    ok = r >= req
    fails += not ok
    print(f"{'  ' if ok else 'X '}{r:6.2f}  {req:3.1f}  {typ:<8} {s:<9} {e}  ({fg} på {bg})")
print(f"\n{len(PAIRS)} par målt, {fails} under kravet.")
