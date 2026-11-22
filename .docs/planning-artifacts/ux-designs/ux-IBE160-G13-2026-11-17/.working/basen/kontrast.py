# Kontrastmåling mot WCAG 2.2 AA for «Basen».
from basen import C, mix


def lum(h):
    h = h.lstrip("#")
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))
    return .2126 * r + .7152 * g + .0722 * b


def ratio(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + .05) / (y + .05)


PAIRS = [
    ("Hvit tekst i toppfeltet", "#FFFFFF", C["hud"], 15, True),
    ("Dempet tekst i toppfeltet", "#C9D2F2", C["hud"], 13, True),
    ("Tall i pillene", "#FFFFFF", C["hud2"], 18, False),
    ("Spilte måneder: bokstav på gull", "#5A3A00", C["gold"], 11, True),
    ("Kommende måneder: bokstav", "#AEB8DE", C["hud2"], 11, True),
    ("Kommende måneder: kant (grafikk)", "#8592C4", C["hud2"], 0, "g"),
    ("Nåværende måned: bokstav på hvitt", C["ink"], "#FFFFFF", 13, True),
    ("Merkelapper over stasjonene", "#FFFFFF", C["hud"], 13, True),
    ("Undertekst på merkelapper", "#C9D2F2", C["hud"], 12, True),
    ("Lønn å hente: gull på mørk pille", C["gold"], C["hud"], 13, True),
    ("Varselprikk: hvitt på rødt", "#FFFFFF", C["red"], 14, True),
    ("NESTE MÅNED: hvitt på grønn (lyseste del)", "#FFFFFF", mix(C["green"], "#FFFFFF", .22), 26, True),
    ("Hint under knappen", "#C9D2F2", C["hud"], 12.5, True),
    ("Spillvindu: hvit tekst", "#FFFFFF", C["hud2"], 14, True),
    ("Spillvindu: dempet tekst", "#C9D2F2", C["hud2"], 13, True),
    ("Spillvindu: gull beløp", C["gold"], C["hud2"], 17, True),
    ("Kort: tittel", C["ink"], "#FFFFFF", 16, True),
    ("Kort: undertekst", "#454B66", "#EEF1FA", 13, True),
    ("Hvit knapp: tekst", C["ink"], "#E6EAF6", 16, True),
    ("Felt: tekst", C["ink"], "#FFFFFF", 15.5, False),
    ("Felt: kant mot spillvindu (grafikk)", "#8592C4", C["hud2"], 0, "g"),
    ("Rødt bånd: tekst", "#FFFFFF", C["red"], 13.5, True),
    ("Grå knapp (frakoblet): tekst", "#FFFFFF", mix("#6A7090", "#FFFFFF", .22), 26, True),
    ("Slett bruker: rosa tekst", "#FF8A8E", C["hud2"], 16, True),
    ("Mobil: dempet tekst", "#4A5068", "#F6F7FB", 12.5, True),
    ("Mobil: avsenderikon Emma", "#FFFFFF", "#94601A", 18, True),
    ("Mobil: avsenderikon Butikken", "#FFFFFF", "#1F6B58", 18, True),
    ("Mobil: avsenderikon Mamma", "#FFFFFF", "#7154A8", 18, True),
    ("Mobil: avsenderikon Banken", "#FFFFFF", "#2F4BC0", 18, True),
    ("Info-ikon i Om tallene", "#5A3A00", C["gold"], 14, True),
    ("Merkelapper mot fjellet og bakken (grafikk)", C["hud"], "#BFD6B4", 0, "g"),
    ("Toppkortet: tekst på hvitt", C["ink"], "#FFFFFF", 11.5, True),
    ("Lønn å hente på kiosken", C["gold"], C["hud"], 13, True),
]
bad = 0
for what, fg, bg, size, bold in PAIRS:
    r = ratio(fg, bg)
    need = 3.0 if bold == "g" or size >= 24 or (bold and size >= 18.66) else 4.5
    bad += r < need
    print(f"{'OK ' if r >= need else 'FEIL'} {r:5.2f}:1 (krav {need}) {what}")
print(f"{len(PAIRS)} par, {bad} under kravet")
