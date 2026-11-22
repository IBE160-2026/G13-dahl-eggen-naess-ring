# Fargehjelpere for «Speilet».
LED = "#FF4FA3"


def _rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def _hex(c):
    return "#" + "".join(f"{max(0, min(255, int(round(v)))):02X}" for v in c)


def mix(a, b, t):
    a, b = _rgb(a), _rgb(b)
    return _hex([a[i] + (b[i] - a[i]) * t for i in range(3)])


def dark(c, t):
    return mix(c, "#120A1E", t)


def light(c, t):
    return mix(c, "#FFF4EA", t)
