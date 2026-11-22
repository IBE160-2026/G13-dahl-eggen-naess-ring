# Myke figurer for «Blokka»: slanke, avrundede former sett skrått forfra (ikke klosser).
# (x, y) = mellom føttene i skjermkoordinater. Høyde ca. 46 * k px.


def darker(hexc, f=.8):
    h = hexc.lstrip("#")
    r, g, b = (round(int(h[i:i + 2], 16) * f) for i in (0, 2, 4))
    return f"#{r:02X}{g:02X}{b:02X}"


def person(x, y, k, look, facing=-1, wave=False):
    """facing = -1 vender ned mot venstre, 1 ned mot høyre."""
    f = facing
    X = lambda v: f"{x + v * k * -f:.2f}"     # speiles slik at "fram" alltid er mot betrakteren
    Y = lambda v: f"{y + v * k:.2f}"
    s = lambda v: f"{v * k:.2f}"
    L = look
    top, top2 = L["top"], darker(L["top"], .78)
    pants, pants2 = L["pants"], darker(L["pants"], .75)
    skin, skin2 = L["skin"], darker(L["skin"], .86)
    hair = L["hair"]
    o = [f'<ellipse cx="{x}" cy="{Y(.6)}" rx="{s(10)}" ry="{s(2.8)}" fill="#000" opacity=".16"/>']
    # langt hår bak skuldrene
    if L.get("style") == "long":
        o.append(f'<path d="M{X(-4.6)} {Y(-41)} Q{X(-6.4)} {Y(-31)} {X(-4.4)} {Y(-27)} L{X(4.6)} {Y(-27)} Q{X(6.4)} {Y(-31)} {X(4.6)} {Y(-41)}Z" fill="{darker(hair,.85)}"/>')
    # bein: bakre bein mørkere
    o.append(f'<path d="M{X(2.2)} {Y(-20)} Q{X(2.8)} {Y(-10)} {X(3.6)} {Y(-1.6)}" stroke="{pants2}" stroke-width="{s(4)}" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M{X(-2.2)} {Y(-20)} Q{X(-2.8)} {Y(-10)} {X(-3.4)} {Y(-1.2)}" stroke="{pants}" stroke-width="{s(4.2)}" fill="none" stroke-linecap="round"/>')
    # sko
    sh = L.get("shoes", "#FFFFFF")
    o.append(f'<ellipse cx="{X(4.6)}" cy="{Y(-.9)}" rx="{s(3)}" ry="{s(1.6)}" fill="{darker(sh,.85)}"/>')
    o.append(f'<ellipse cx="{X(-4.6)}" cy="{Y(-.6)}" rx="{s(3.2)}" ry="{s(1.7)}" fill="{sh}"/>')
    # bakre arm
    if wave:
        o.append(f'<path d="M{X(5)} {Y(-32)} Q{X(9)} {Y(-37)} {X(9.6)} {Y(-44)}" stroke="{top2}" stroke-width="{s(3.4)}" fill="none" stroke-linecap="round"/>'
                 f'<circle cx="{X(9.8)}" cy="{Y(-45.6)}" r="{s(1.7)}" fill="{skin2}"/>')
    else:
        o.append(f'<path d="M{X(5)} {Y(-32)} Q{X(7.2)} {Y(-26)} {X(6.6)} {Y(-20.5)}" stroke="{top2}" stroke-width="{s(3.4)}" fill="none" stroke-linecap="round"/>'
                 f'<circle cx="{X(6.6)}" cy="{Y(-19.4)}" r="{s(1.6)}" fill="{skin2}"/>')
    # overkropp
    o.append(f'<path d="M{X(-5.6)} {Y(-33)} Q{X(-6.6)} {Y(-26)} {X(-4.8)} {Y(-19)} L{X(4.8)} {Y(-19)} Q{X(6.6)} {Y(-26)} {X(5.6)} {Y(-33)} Q{X(0)} {Y(-35.4)} {X(-5.6)} {Y(-33)}Z" fill="{top}"/>')
    o.append(f'<path d="M{X(1.6)} {Y(-34.6)} Q{X(5.6)} {Y(-34)} {X(5.6)} {Y(-33)} Q{X(6.6)} {Y(-26)} {X(4.8)} {Y(-19)} L{X(1.2)} {Y(-19)}Z" fill="{top2}" opacity=".55"/>')
    # T-skjorte som stripe foran (åpen jakke)
    o.append(f'<path d="M{X(-2.4)} {Y(-34.2)} L{X(-1.6)} {Y(-19.2)} L{X(1)} {Y(-19.2)} L{X(.6)} {Y(-34.4)}Z" fill="{L["shirt"]}"/>')
    # fremre arm
    o.append(f'<path d="M{X(-5)} {Y(-32)} Q{X(-7.4)} {Y(-26)} {X(-6.6)} {Y(-20.5)}" stroke="{top}" stroke-width="{s(3.6)}" fill="none" stroke-linecap="round"/>'
             f'<circle cx="{X(-6.6)}" cy="{Y(-19.3)}" r="{s(1.7)}" fill="{skin}"/>')
    # hals og hode
    o.append(f'<path d="M{X(-1.3)} {Y(-36)} L{X(-1.3)} {Y(-33.6)} L{X(1.5)} {Y(-33.6)} L{X(1.5)} {Y(-36)}Z" fill="{skin2}"/>')
    o.append(f'<path d="M{X(-4.2)} {Y(-40.4)} Q{X(-4.4)} {Y(-35.4)} {X(-.6)} {Y(-35)} Q{X(3.8)} {Y(-35.6)} {X(4.2)} {Y(-40.4)} Q{X(4.2)} {Y(-46)} {X(0)} {Y(-46)} Q{X(-4.2)} {Y(-46)} {X(-4.2)} {Y(-40.4)}Z" fill="{skin}"/>')
    o.append(f'<path d="M{X(1.8)} {Y(-45.4)} Q{X(4.2)} {Y(-44.6)} {X(4.2)} {Y(-40.4)} Q{X(3.8)} {Y(-35.6)} {X(-.2)} {Y(-35.1)} Q{X(2.6)} {Y(-37)} {X(1.8)} {Y(-45.4)}Z" fill="{skin2}" opacity=".7"/>')
    o.append(f'<ellipse cx="{X(3.6)}" cy="{Y(-40.2)}" rx="{s(1)}" ry="{s(1.5)}" fill="{skin2}"/>')
    # hår
    st = L.get("style", "short")
    if st == "short":
        o.append(f'<path d="M{X(-4.5)} {Y(-41)} Q{X(-5.2)} {Y(-47.6)} {X(.2)} {Y(-47.6)} Q{X(5)} {Y(-47.6)} {X(4.6)} {Y(-41.4)} Q{X(3.6)} {Y(-44)} {X(1)} {Y(-44.6)} Q{X(-2)} {Y(-43)} {X(-4.5)} {Y(-41)}Z" fill="{hair}"/>')
    elif st == "bun":
        o.append(f'<circle cx="{X(1.4)}" cy="{Y(-48.4)}" r="{s(2.4)}" fill="{hair}"/>')
        o.append(f'<path d="M{X(-4.5)} {Y(-40.4)} Q{X(-5)} {Y(-47.2)} {X(0)} {Y(-47.2)} Q{X(5)} {Y(-47.2)} {X(4.6)} {Y(-40.4)} Q{X(3)} {Y(-44.6)} {X(-1)} {Y(-44)} Q{X(-3.4)} {Y(-43.4)} {X(-4.5)} {Y(-40.4)}Z" fill="{hair}"/>')
    elif st == "long":
        o.append(f'<path d="M{X(-4.8)} {Y(-38)} Q{X(-5.4)} {Y(-47.6)} {X(0)} {Y(-47.6)} Q{X(5.4)} {Y(-47.6)} {X(4.8)} {Y(-38)} Q{X(3.6)} {Y(-44)} {X(-.6)} {Y(-44.4)} Q{X(-3.6)} {Y(-43.6)} {X(-4.8)} {Y(-38)}Z" fill="{hair}"/>')
    elif st == "curly":
        for dx, dy, r in [(-3.6, -43.6, 2.4), (-1, -46, 2.6), (2, -46, 2.6), (4, -43.4, 2.2), (-4.4, -41, 1.8)]:
            o.append(f'<circle cx="{X(dx)}" cy="{Y(dy)}" r="{s(r)}" fill="{hair}"/>')
    # ansikt
    for ex, ey in [(-2.6, -40.6), (.2, -40.8)]:
        o.append(f'<ellipse cx="{X(ex)}" cy="{Y(ey)}" rx="{s(.55)}" ry="{s(.75)}" fill="#1D1B22"/>')
    o.append(f'<path d="M{X(-3.4)} {Y(-42.4)} l{s(1.6*-f)} {s(-.3)} M{X(-.6)} {Y(-42.6)} l{s(1.6*-f)} {s(-.2)}" stroke="{darker(hair,.9)}" stroke-width="{s(.5)}" stroke-linecap="round"/>')
    o.append(f'<path d="M{X(-1.6)} {Y(-40)} l{s(-.6*-f)} {s(1.6)} l{s(.8*-f)} {s(.2)}" fill="none" stroke="{skin2}" stroke-width="{s(.45)}" stroke-linecap="round"/>')
    o.append(f'<path d="M{X(-2.4)} {Y(-37.4)} q{s(1.2*-f)} {s(.7)} {s(2.2*-f)} {s(0)}" fill="none" stroke="#8E3B33" stroke-width="{s(.55)}" stroke-linecap="round"/>')
    return "".join(o)
