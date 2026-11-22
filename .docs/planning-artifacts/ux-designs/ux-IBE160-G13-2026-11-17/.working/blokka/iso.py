# Liten isometrisk tegnemotor for «Blokka» v3 (3D-dukkehus).
# Akser: x går ned mot høyre, y går ned mot venstre, z går opp.
import math

C30, S30 = math.cos(math.radians(30)), 0.5


def shade(hexc, f):
    """f < 1 mørkere, f > 1 lysere."""
    h = hexc.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    if f <= 1:
        r, g, b = (round(v * f) for v in (r, g, b))
    else:
        r, g, b = (round(v + (255 - v) * (f - 1)) for v in (r, g, b))
    return f"#{r:02X}{g:02X}{b:02X}"


class Iso:
    def __init__(self, ox, oy, k=1.0):
        self.ox, self.oy, self.k = ox, oy, k

    def p(self, x, y, z):
        return (self.ox + (x - y) * C30 * self.k, self.oy + ((x + y) * S30 - z) * self.k)

    def poly(self, pts, fill, extra=""):
        d = " ".join(f"{a:.1f},{b:.1f}" for a, b in (self.p(*q) for q in pts))
        return f'<polygon points="{d}" fill="{fill}" {extra}/>'

    # flater
    def top(self, x, y, z, w, d, fill, extra=""):
        return self.poly([(x, y, z), (x + w, y, z), (x + w, y + d, z), (x, y + d, z)], fill, extra)

    def left(self, x, y, z, w, h, fill, extra=""):     # plan y = konstant, synlig mot venstre
        return self.poly([(x, y, z), (x + w, y, z), (x + w, y, z + h), (x, y, z + h)], fill, extra)

    def right(self, x, y, z, d, h, fill, extra=""):    # plan x = konstant, synlig mot høyre
        return self.poly([(x, y, z), (x, y + d, z), (x, y + d, z + h), (x, y, z + h)], fill, extra)

    def box(self, x, y, z, w, d, h, col, lit=1.0):
        """Kloss med tre synlige sider: topp lysest, venstre middels, høyre mørkest."""
        return (self.left(x, y + d, z, w, h, shade(col, .88 * lit)) +
                self.right(x + w, y, z, d, h, shade(col, .74 * lit)) +
                self.top(x, y, z + h, w, d, shade(col, 1.0) if lit >= 1 else shade(col, lit)))

    def text(self, x, y, z, s, size, fill, w=700, anchor="middle", fam="'Schibsted Grotesk', sans-serif"):
        a, b = self.p(x, y, z)
        return f'<text x="{a:.1f}" y="{b:.1f}" font-family="{fam}" font-size="{size*self.k:.1f}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>'

    def face_text_left(self, x, y, z, s, size, fill, w=800):
        """Tekst lagt på en venstre flate (skjev som flaten)."""
        a, b = self.p(x, y, z)
        return (f'<text transform="translate({a:.1f} {b:.1f}) matrix({C30:.3f} {S30:.3f} 0 1 0 0)" font-family="\'Schibsted Grotesk\', sans-serif" '
                f'font-size="{size*self.k:.1f}" font-weight="{w}" fill="{fill}" text-anchor="middle">{s}</text>')

    def face_text_right(self, x, y, z, s, size, fill, w=800):
        a, b = self.p(x, y, z)
        return (f'<text transform="translate({a:.1f} {b:.1f}) matrix({C30:.3f} {-S30:.3f} 0 1 0 0)" font-family="\'Schibsted Grotesk\', sans-serif" '
                f'font-size="{size*self.k:.1f}" font-weight="{w}" fill="{fill}" text-anchor="middle">{s}</text>')


def figure(iso, x, y, z, look, face="left", wave=False):
    """Kloss-figur (low-poly). look: dict med skin, hair, top, shirt, pants, shoes, style."""
    L = look
    o = []
    # skygge
    o.append(iso.top(x - 6, y - 6, z + .1, 14, 12, "#000", 'opacity=".12"'))
    # bein og sko
    for dx in (0, 4.5):
        o.append(iso.box(x + dx, y, z, 3.6, 4, 2.2, L.get("shoes", "#FFFFFF")))
        o.append(iso.box(x + dx, y, z + 2.2, 3.6, 3.6, 11, L["pants"]))
    # overkropp: jakke med T-skjorte foran
    o.append(iso.box(x - .6, y - .6, z + 13, 9.4, 5.2, 13, L["top"]))
    if face == "left":
        o.append(iso.left(x + 2.4, y + 4.6, z + 15, 3.2, 10, L["shirt"]))
    else:
        o.append(iso.right(x + 8.8, y + .6, z + 15, 3.2, 10, L["shirt"]))
    # armer
    o.append(iso.box(x - 3, y, z + 14, 2.4, 3.6, 11.5, shade(L["top"], .95)))
    if wave:
        o.append(iso.box(x + 9.2, y, z + 25, 2.4, 3.6, 10, L["top"]) + iso.box(x + 9.2, y, z + 35, 2.4, 3.2, 3, L["skin"]))
    else:
        o.append(iso.box(x + 9.2, y, z + 14, 2.4, 3.6, 11.5, shade(L["top"], .95)))
        o.append(iso.box(x + 9.2, y, z + 11.5, 2.4, 3.2, 2.6, L["skin"]))
    o.append(iso.box(x - 3, y, z + 11.5, 2.4, 3.2, 2.6, L["skin"]))
    # hals og hode
    o.append(iso.box(x + 3, y + 1, z + 26, 3, 3, 2, shade(L["skin"], .9)))
    o.append(iso.box(x + .4, y - .6, z + 28, 8.2, 7.4, 9, L["skin"]))
    # hår
    st = L.get("style", "short")
    o.append(iso.box(x, y - 1, z + 36, 9, 8.2, 3.2, L["hair"]))
    if st in ("short", "bun"):
        o.append(iso.box(x, y - 1, z + 33, 9, 2.4, 3, L["hair"]))          # bakhode
    if st == "bun":
        o.append(iso.box(x + 2.6, y + 1.4, z + 39.2, 4, 4, 3.6, L["hair"]))
    if st == "long":
        o.append(iso.box(x - .6, y - 1.2, z + 24, 9.8, 2.6, 15, L["hair"]))
    # pannelugg mot betrakteren
    if face == "left":
        o.append(iso.left(x + .4, y + 6.8, z + 34.6, 5.5, 2.6, shade(L["hair"], .9)))
        for ex in (2.2, 5.6):
            a, b = iso.p(x + ex, y + 6.8, z + 32.2)
            o.append(f'<ellipse cx="{a:.1f}" cy="{b:.1f}" rx="{.75*iso.k:.1f}" ry="{1.1*iso.k:.1f}" fill="#14213D"/>')
        a, b = iso.p(x + 4, y + 6.8, z + 29.6)
        o.append(f'<path d="M{a-1.6*iso.k:.1f} {b-.6*iso.k:.1f} q{1.6*iso.k:.1f} {1.4*iso.k:.1f} {3.2*iso.k:.1f} {.9*iso.k:.1f}" fill="none" stroke="#9C4A3A" stroke-width="{.7*iso.k:.1f}" stroke-linecap="round"/>')
    else:
        o.append(iso.right(x + 8.6, y - .6, z + 34.6, 5.5, 2.6, shade(L["hair"], .8)))
        for ey in (1.4, 4.8):
            a, b = iso.p(x + 8.6, y + ey, z + 32.2)
            o.append(f'<ellipse cx="{a:.1f}" cy="{b:.1f}" rx="{.75*iso.k:.1f}" ry="{1.1*iso.k:.1f}" fill="#14213D"/>')
        a, b = iso.p(x + 8.6, y + 3.2, z + 29.6)
        o.append(f'<path d="M{a-1.6*iso.k:.1f} {b+.4*iso.k:.1f} q{1.6*iso.k:.1f} {.9*iso.k:.1f} {3.2*iso.k:.1f} {-.6*iso.k:.1f}" fill="none" stroke="#9C4A3A" stroke-width="{.7*iso.k:.1f}" stroke-linecap="round"/>')
    return "".join(o)
