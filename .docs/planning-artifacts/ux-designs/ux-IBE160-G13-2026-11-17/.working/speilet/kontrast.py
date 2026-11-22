# Kontrastmåling mot WCAG 2.2 AA for «Speilet» (grafisk speilselfie, alle skjermene).
# Krav: 4.5:1 vanlig tekst, 3:1 stor tekst (>= 24px, eller >= 18.66px fet), 3:1 grafikk og kontrollgrenser.
from speil import BASE, SEASONS
from folk_farger import mix


def lum(h):
    h = h.lstrip("#")
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))
    return .2126 * r + .7152 * g + .0722 * b


def ratio(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x + .05) / (y + .05)


B = BASE
PAIRS = []
for name, sz in SEASONS.items():
    S = dict(B, **{k: v for k, v in sz.items() if isinstance(v, str)})
    d = .5 if name == "høst" else .55    # svakeste mørklegging brukt i årstiden (krisemåned .5, påske .55)
    PAIRS += [(f"Tusj og merknader på glasset ({name})", B["ink"], S["wall_mir"], 14, True),
              (f"Merknader og statuslinje på veggen ({name})", B["ink"], S["wall"], 14, True),
              (f"Bokstaver for kommende måneder ({name})", B["ink2"], S["wall"], 12, True),
              (f"Hvit tusj på mørklagt glass ({name})", "#FFFFFF", mix(S["wall_mir"], "#14161F", d), 14, True),
              (f"Hvit tusj over vinduet ({name})", "#FFFFFF", mix(S["sky"], "#14161F", d), 15, True),
              (f"Tusj over vinduet ({name})", B["ink"], S["sky"], 15, True) if name != "høst" or True else None,
              (f"Kant rundt lapper og klistremerker mot glasset ({name})", B["ink2"], S["wall_mir"], 0, "g"),
              (f"Ring rundt nåværende måned ({name})", B["ink"], S["wall"], 0, "g")]
PAIRS += [
    ("Tekst på gul lapp", B["ink"], B["note"], 13, True),
    ("Dempet tekst på gul lapp", B["ink2"], B["note"], 13, True),
    ("Tekst på klistremerker", B["ink"], "#FFFFFF", 14, True),
    ("Undertekst på klistremerker", B["ink2"], "#FFFFFF", 12, True),
    ("Tekst på korall hovedhandling", B["ink"], B["case"], 14.5, True),
    ("Undertekst på korall hovedhandling", B["ink"], B["case"], 12, True),
    ("Tekst på arket (konto, meny)", B["ink"], B["paper"], 14, True),
    ("Dempet tekst på arket", B["ink2"], B["paper"], 13.5, False),
    ("Rød tekst på arket (Slett bruker, feil)", B["press"], B["paper"], 13, True),
    ("Felt: kant mot arket (grafikk)", B["ink2"], B["paper"], 0, "g"),
    ("Mobilen: dempet tekst", "#5A5E6B", "#FFFFFF", 12.5, True),
    ("Mobilen: bokstav i avsenderikon (Emma)", "#FFFFFF", "#94601A", 18, True),
    ("Mobilen: bokstav i avsenderikon (Butikken)", "#FFFFFF", "#2E7D6B", 18, True),
    ("Mobilen: bokstav i avsenderikon (Mamma)", "#FFFFFF", "#7154A8", 18, True),
    ("Varsel: dempet tid", "#5A5E6B", "#FBFBFD", 13, True),
    ("Merknad på gulvet", B["ink"], B["floor"], 14, True),
    ("Speilrammen mot veggen (grafikk)", B["frame"], B["wall"], 0, "g"),
]

if __name__ == "__main__":
    bad = 0
    for what, fg, bg, size, bold in PAIRS:
        r = ratio(fg, bg)
        need = 3.0 if bold == "g" or size >= 24 or (bold and size >= 18.66) else 4.5
        bad += r < need
        print(f"{'OK ' if r >= need else 'FEIL'} {r:5.2f}:1 (krav {need}) {what}")
    print(f"{len(PAIRS)} par, {bad} under kravet")
