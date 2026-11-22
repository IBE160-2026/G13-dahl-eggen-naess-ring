# «Speilet»: alle skjermene. Kjør: python alle.py [nummer ...]
# Tallene er eksempeldata fra PRD-ens brukerreiser (UJ-1 til UJ-6), ikke motorberegninger.
import os, sys
from folk_farger import mix, dark, light
from speil import (C, MONTHS, T, page, status, home_ind, set_month, your_room, mirror_room, mirror, figure, flash, timeline, goal_boxes,
                   note, locked, callout, marker, sticker, stat_stickers, switch, work_shirt, right_wall, scene, dim_all, sheet, field, pill,
                   link, checkbox, phone, banner, tape, trip_photo, CAR, CARD, MOPED, JOBB, LOOKS)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "skjermer")
os.makedirs(OUT, exist_ok=True)
SCREENS = {}
WHITE = "#FFFFFF"


def screen(name, title, desc):
    def deco(fn):
        SCREENS[name] = (title, desc, fn)
        return fn
    return deco


def start_scene():
    """Første skjerm og kontoskjermene: speilet i et tomt rom en sommerkveld, snora venter."""
    set_month(7)
    o = [your_room(), timeline(-1, 1, photos_upto=-1, label=False, compact=True)]
    o.append(mirror(mirror_room(0)))
    return o


# ------------------------------------------------------------------ innlogging og start
@screen("01-velkommen", "Første skjerm: LifeMode",
        "Et tomt speil lent mot veggen og en fotosnor med tolv blanke kort. På glasset står LifeMode og Fem år. Dine valg. To klistremerker: Opprett bruker og Logg inn.")
def s01():
    o = start_scene()
    o.append(T(70, 230, "LifeMode", 40, C["ink"], 800))
    o.append(marker(72, 262, "Fem år. Dine valg.", 20))
    o.append(T(72, 290, "Fra du er 15 til du fyller 20.", 14.5, C["ink"], 600))
    o.append(T(72, 310, "Ett år per kveld.", 14.5, C["ink"], 600))
    o.append(sticker(70, 610, 200, "pil", "Opprett bruker", -2, "Opprett bruker", primary=True))
    o.append(sticker(70, 664, 150, None, "Logg inn", 2, "Logg inn"))
    o.append(status() + home_ind())
    return o


@screen("02-opprett-bruker", "Opprett bruker",
        "Et ark legger seg over speilet med e-post, passord, avkrysning for spillerinformasjonen og knappen Opprett bruker.")
def s02():
    o = start_scene()
    o.append(sheet(230, "Opprett bruker", "Det tar under ett minutt."))
    o.append(field(24, 352, 342, "E-post", "markus@eksempel.no"))
    o.append(field(24, 438, 342, "Passord (minst 8 tegn)", 10, masked=True))
    o.append(checkbox(24, 528, T(60, 545, "Jeg har lest spillerinformasjonen", 14.5, C["ink"], 600), True))
    o.append(link(60, 572, "Les spillerinformasjonen"))
    o.append(pill(24, 612, 342, "Opprett bruker"))
    o.append(T(195, 700, "Har du allerede en bruker?", 14.5, C["ink2"], 600, "middle") + link(195, 724, "Logg inn", "middle"))
    o.append(status(WHITE) + home_ind())
    return o


@screen("03-logg-inn", "Logg inn", "Arket med e-post og passord, lenken Glemt passord? og knappen Logg inn.")
def s03():
    o = start_scene()
    o.append(sheet(300, "Logg inn"))
    o.append(field(24, 390, 342, "E-post", "markus@eksempel.no"))
    o.append(field(24, 476, 342, "Passord", 10, masked=True))
    o.append(link(24, 566, "Glemt passord?"))
    o.append(pill(24, 600, 342, "Logg inn"))
    o.append(T(195, 690, "Ny her?", 14.5, C["ink2"], 600, "middle") + link(195, 714, "Opprett bruker", "middle"))
    o.append(status(WHITE) + home_ind())
    return o


@screen("04-glemt-passord", "Glemt passord", "Arket ber om e-post. Svaret er det samme enten e-posten finnes eller ikke.")
def s04():
    o = start_scene()
    o.append(sheet(330, "Glemt passord", ["Skriv e-posten din. Finnes den,", "får du en lenke for å lage nytt passord."]))
    o.append(field(24, 456, 342, "E-post", "markus@eksempel.no"))
    o.append(pill(24, 540, 342, "Send lenke"))
    o.append(T(24, 628, "Du får det samme svaret uansett,", 13.5, C["ink2"], 600) + T(24, 648, "så ingen kan sjekke om e-posten har en bruker.", 13.5, C["ink2"], 600))
    o.append(link(24, 690, "Tilbake til innlogging"))
    o.append(status(WHITE) + home_ind())
    return o


@screen("05-livsmal", "Velg livsmålet",
        "Januar, År 1. Speilet viser rommet bak deg, og tre ting lyser på gulvet: flyttekasser, en pakket ryggsekk og en liten safe. "
        "Håndskrevne merknader forklarer målene: spare til noe stort, en stor opplevelse eller gjeldfri med buffer.")
def s05():
    set_month(0)
    glow = lambda cx, cy, r: f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*.7}" fill="{C["note"]}" opacity=".55" filter="url(#glow)"/>'
    objs = (glow(94, 570, 50) + goal_boxes(3, None) +
            glow(176, 590, 34) + '<path d="M152 612 C148 572 158 552 176 548 C194 552 204 572 200 612 Z" fill="#2E6E6A"/><path d="M160 576 H192 V600 H160 Z" fill="#245652"/>'
            '<path d="M164 552 C166 536 186 536 188 552" stroke="#245652" stroke-width="5" fill="none"/><rect x="180" y="560" width="14" height="8" rx="2" fill="#FF6F59"/>' +
            glow(256, 590, 36) + '<rect x="230" y="562" width="52" height="50" rx="5" fill="#5B6270"/><rect x="236" y="568" width="40" height="38" rx="3" fill="#6E7685"/>'
            '<circle cx="256" cy="587" r="9" fill="none" stroke="#E9ECF2" stroke-width="3"/><path d="M256 587 l5 -4" stroke="#E9ECF2" stroke-width="3"/>')
    o = [your_room(), timeline(0, 1, photos_upto=-1)]
    o.append(mirror(mirror_room(0) + objs))
    o.append(marker(68, 322, "Hva drømmer du om?", 22))
    o.append(T(68, 346, "Velg ett mål. Det teller mest", 14, C["ink"], 600) + T(68, 364, "når du fyller 20.", 14, C["ink"], 600))
    o.append(callout(110, 414, "Noe stort", "egen leilighet", "M100 442 V462", 15, "middle"))
    o.append(callout(184, 450, "Opplevelse", "interrail", "M180 478 V530", 15, "middle"))
    o.append(callout(258, 490, "Buffer", "gjeldfri", "M258 518 V548", 15, "middle"))
    o.append(T(70, 700, "Trykk på tingen du vil jobbe mot.", 14, C["ink"], 700))
    o.append(status() + home_ind())
    return o


@screen("06-avatar", "Velg hvem du er",
        "Seks bilder er teipet øverst på speilet, og speilbildet viser den du har valgt. Klistremerket Dette er meg bekrefter. Utseendet påvirker ikke tallene.")
def s06():
    set_month(0)
    o = [your_room(), timeline(0, 1, photos_upto=-1)]
    o.append(mirror(mirror_room(0) + figure(206, 742, 410, "sara", "smil", "stand", 15)))
    looks = ["markus", "amina", "jonas", "sara", "ali", "linh"]
    for i, lk in enumerate(looks):
        x, y = 66 + (i % 3) * 64, 170 + (i // 3) * 76
        rot = [-4, 3, -2, 2, -3, 4][i]
        portrait = figure(100, 1000, 1000, lk, "smil", "stand", 15)
        o.append(f'<g transform="translate({x} {y}) rotate({rot} 28 34)" filter="url(#soft)"><rect width="56" height="68" fill="#FFFFFF" stroke="{C["ink2"]}" stroke-width="1"/>'
                 f'<svg x="4" y="4" width="48" height="50" viewBox="34 -36 136 142" preserveAspectRatio="xMidYMid slice"><rect x="0" y="-60" width="300" height="300" fill="{C["wall_mir"]}"/>{portrait}</svg></g>')
        o.append(tape(x + 28, y + 1, rot, 24))
        if lk == "sara":
            o.append(f'<ellipse cx="{x+28}" cy="{y+34}" rx="36" ry="42" fill="none" stroke="{C["case"]}" stroke-width="3" transform="rotate({rot+6} {x+28} {y+34})"/>'
                     f'<ellipse cx="{x+28}" cy="{y+34}" rx="37.5" ry="43.5" fill="none" stroke="{C["ink"]}" stroke-width="1" transform="rotate({rot+6} {x+28} {y+34})"/>')
    o.append(marker(68, 360, "Hvem er du?", 22))
    o.append(T(68, 382, "Utseendet påvirker", 13.5, C["ink"], 600) + T(68, 399, "ikke tallene.", 13.5, C["ink"], 600))
    o.append(sticker(220, 690, 150, "pil", "Dette er meg", -2, "Dette er meg", primary=True))
    o.append(status() + home_ind())
    return o


@screen("07-pengegave", "Første valg: pengegaven",
        "Januar, 15 år. Speilbildet holder en åpen konvolutt med penger fra besteforeldrene. Tre klistremerker er valgene: alt i BSU, halvparten i BSU eller alt på brukskontoen.")
def s07():
    o = scene(0, 15, 1, mood="glad", pose="stand", boxes=0, locks=(("Mopedlappen", 16, MOPED), ("Kredittkort", 18, CARD)),
              kveldene=None, stats=None, job=False, switch_on=False, photos_upto=-1, item="konvolutt")
    o.append(callout(66, 380, "Pengegave", "18 000 kr", "M120 392 C190 410 270 440 300 470", 16, strong=True))
    o.append(T(66, 444, "fra besteforeldrene", 13.5, C["ink"], 600))
    o.append(marker(66, 500, "Hva gjør du", 19) + marker(66, 522, "med pengene?", 19))
    o.append(sticker(196, 610, 178, None, "Alt i BSU", -2, "Alt i BSU", sub="BSU er låst til bolig"))
    o.append(sticker(196, 666, 178, None, "Halvparten i BSU", 2, "Halvparten i BSU", sub="9 000 kr, resten fritt"))
    o.append(sticker(196, 722, 178, None, "Alt på brukskonto", -1, "Alt på brukskonto", sub="fritt å bruke"))
    o.append(status() + home_ind())
    return o


# ------------------------------------------------------------------ måneden og mobilen
@screen("08-maned", "Månedsnavet: april, 16 år",
        "Fotosnora med tolv klyper viser året: april henger størst med navnet under og en ring. Speilbildet tar en speilselfie. Du, 16 år står med tusj på glasset. "
        "Gule lapper viser det som er låst. Mobil, trivsel og penger er klistremerker på speilrammen. Jobbskjorta henger på knaggen, og lysbryteren tar deg til neste måned.")
def s08():
    return scene() + [status(), home_ind()]


@screen("09-sms-varsel", "SMS fra Emma",
        "Et varsel glir ned øverst på skjermen, som en ekte SMS: Emma spør om du blir med på hytta i påsken.")
def s09():
    o = scene()
    o.append(banner("Emma", ["Hytta i påsken? Vi er fire stykker.", "Bli med?"], "#D99A2B"))
    o.append(home_ind())
    return o


def msg_row(y, name, text, when, col, unread=False):
    return (f'<circle cx="84" cy="{y}" r="22" fill="{col}"/>' + T(84, y + 7, name[0], 18, WHITE, 800, "middle") +
            T(118, y - 4, name, 16, C["ink"], 800 if unread else 700) + T(326, y - 4, when, 12.5, "#5A5E6B", 600, "end") +
            T(118, y + 17, text, 13.5, C["ink"] if unread else "#5A5E6B", 600 if unread else 500) +
            (f'<circle cx="326" cy="{y+12}" r="6" fill="{C["case"]}" stroke="{C["ink"]}" stroke-width="1"/>' if unread else "") +
            f'<path d="M118 {y+38} H326" stroke="#E2E2E8"/>')


@screen("10-mobil-meldinger", "Mobil: meldingene",
        "Mobilen i hendene dine. Meldingsappen viser Emma, Mamma, Butikken og Banken. Du kan ikke svare i spillet.")
def s10():
    o = scene()
    body = (msg_row(202, "Emma", "Hytta i påsken? Vi er fire…", "14:02", "#94601A", True) +
            msg_row(272, "Butikken", "Kan du ta en ekstravakt lørdag?", "11:30", "#2E7D6B", True) +
            msg_row(342, "Mamma", "Husk tannlegen på torsdag", "i går", "#7154A8") +
            msg_row(412, "Banken", "Lønn satt inn: 4 290 kr", "man.", "#2B4CC4") +
            T(195, 720, "Du kan ikke svare på meldinger i spillet.", 13, "#5A5E6B", 600, "middle"))
    o.append(phone("Meldinger", body))
    o.append(status(WHITE))
    return o


def bubble(y, lines, w=230):
    h = 16 + 20 * len(lines)
    return (f'<rect x="62" y="{y}" width="{w}" height="{h}" rx="18" fill="#ECECF1"/>' +
            "".join(T(78, y + 26 + i * 20, l, 14.5, C["ink"], 500) for i, l in enumerate(lines)))


@screen("11-mobil-samtale", "Mobil: invitasjonen fra Emma",
        "Samtalen med Emma. Under meldingene ligger invitasjonen som et kort med knappen Legg i planen. Du kan ikke svare i spillet.")
def s11():
    o = scene()
    body = (T(195, 186, "I dag 14:02", 12.5, "#5A5E6B", 600, "middle") +
            bubble(200, ["Hei! Vi drar på hytta til", "mormoren min i påsken"]) +
            bubble(268, ["Vi er fire stykker. Mat og buss", "deler vi på, ca. 1 200 kr hver"], 246) +
            bubble(336, ["Bli med?"], 96) +
            f'<rect x="62" y="400" width="266" height="190" rx="18" fill="#FFFFFF" stroke="{C["ink2"]}" stroke-width="1.5"/>' +
            trip_photo(63.5, 401.5, 263, 70) +
            T(80, 498, "Påske på hytta", 17, C["ink"], 800) + T(80, 520, "Påskeferien · ca. 1 200 kr", 14, "#5A5E6B", 600) +
            pill(80, 534, 230, "Legg i planen", True, 42) +
            T(195, 620, "Du bestemmer deg når påsken kommer.", 13, "#5A5E6B", 600, "middle") +
            T(195, 720, "Du kan ikke svare i spillet.", 13, "#5A5E6B", 600, "middle"))
    o.append(phone("Emma", body, back="Meldinger"))
    o.append(status(WHITE))
    return o


# ------------------------------------------------------------------ hendelser
@screen("12-hendelse", "Hendelse: påsken",
        "Rommet i speilet blir mørkere, og bare tre ting lyser: hodetelefonene på speilrammen, jobbskjorta på knaggen og den pakkede sekken på gulvet. "
        "Hver ting har en håndskrevet merknad med valget og hva det koster.")
def s12():
    o = scene(locks=(), mood="tenker", pose="stand", dim=.55, stats=None, kveldene=None, show_age=False, job=False, switch_on=False)
    glow = lambda cx, cy, rx, ry: f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C["note"]}" opacity=".6" filter="url(#glow)"/>'
    o.append(f'<g transform="translate(66 196) rotate(-4)" filter="url(#soft)"><rect width="74" height="86" fill="#FFFFFF" stroke="{C["ink2"]}"/>{trip_photo(5, 5, 64, 60)}</g>' + tape(103, 197, -4, 26))
    o.append(T(150, 222, "Emma:", 15, WHITE, 700, font="k") + T(150, 244, "«Hytta i påsken?»", 16, WHITE, 700, font="k"))
    o.append(marker(66, 330, "Hva gjør du i påsken?", 21, fill=WHITE))
    # hodetelefoner på venstre side av rammen
    o.append(glow(64, 450, 40, 40) + '<path d="M44 452 C44 416 86 416 86 452" stroke="#F4F1EA" stroke-width="7" fill="none"/><rect x="34" y="444" width="18" height="28" rx="7" fill="#F4F1EA" stroke="#1C1C20" stroke-width="1.5"/><rect x="78" y="444" width="18" height="28" rx="7" fill="#F4F1EA" stroke="#1C1C20" stroke-width="1.5"/>')
    o.append(callout(104, 456, "Slapp av hjemme", "0 kr", "M100 460 L94 460", 15, fill=WHITE))
    # jobbskjorta, lyser
    o.append(glow(346, 220, 50, 70) + work_shirt())
    o.append(callout(346, 316, "Ekstravakter", "+1 090 kr", "M346 298 V290", 14, "middle"))
    # sekken på gulvet foran speilet
    o.append(glow(330, 760, 52, 34) + '<path d="M300 800 C296 752 308 730 330 726 C352 730 362 752 358 800 Z" fill="#2E6E6A" stroke="#1C1C20" stroke-width="1.5"/>'
             '<path d="M308 762 H352 V788 H308 Z" fill="#245652"/><path d="M314 730 C316 712 344 712 346 730" stroke="#245652" stroke-width="5" fill="none"/><rect x="338" y="740" width="16" height="9" rx="2" fill="#FF6F59"/>')
    o.append(callout(286, 696, "Bli med på hytta", "−1 200 kr", "M290 712 L302 724", 15, "end", fill=WHITE))
    o.append(T(24, 812, "Trykk på en ting for å velge.", 14, C["ink"], 700))
    o.append(status() + home_ind())
    return o


@screen("13-resultat", "Resultat: påsken på hytta",
        "Speilbildet smiler. I fotosnora har april fått et bilde fra hytta. Ved klistremerkene står endringene med tusj: penger minus 1200 kroner, trivsel opp 6. "
        "Klistremerkene Hvorfor? og Fortsett ligger nederst til venstre.")
def s13():
    o = scene(mood="glad", pose="stand", special={3: "trip"}, stats=("2 nye", "Trivsel 70", "17 250 kr"), kveldene=None, switch_on=False)
    o.append(callout(132, 180, "Nytt bilde:", "påsken på hytta", "M128 174 C124 166 122 162 120 156 M116 162 L120 156 L126 160", 14))
    o.append(marker(214, 676, "+6", 18) + marker(186, 724, "−1 200", 16))
    o.append(sticker(58, 650, 120, "hvorfor", "Hvorfor?", -2, "Hvorfor? Se hva som endret seg"))
    o.append(sticker(58, 700, 120, "pil", "Fortsett", 2, "Fortsett", primary=True))
    o.append(status() + home_ind())
    return o


@screen("14-hvorfor", "Hvorfor?",
        "Glasset blir mørkere, og med hvit tusj er sammenhengen tegnet opp: Du ble med på hytta i påsken, det kostet 1200 kroner, pengene ble 17250 kroner. "
        "Du var sammen med venner, sosialt gikk opp, og trivselen gikk fra 64 til 70.")
def s14():
    o = scene(locks=(), mood="noytral", pose="stand", special={3: "trip"}, stats=None, kveldene=None, show_age=False, dim=.62, switch_on=False, job=False)
    W = WHITE
    arrow = lambda d: f'<path d="{d}" stroke="{W}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    o.append(marker(68, 200, "Hvorfor endret", 24, fill=W) + marker(68, 228, "dette seg?", 24, fill=W))
    o.append(f'<g transform="translate(70 252) rotate(-3)"><rect width="68" height="76" fill="#FFFFFF"/>{trip_photo(5, 5, 58, 54)}</g>')
    o.append(T(152, 276, "Du ble med på", 15, W, 700, font="k") + T(152, 296, "hytta i påsken", 15, W, 700, font="k"))
    o.append(arrow("M104 340 C104 370 108 384 116 396 M108 390 L116 396 L118 386"))
    o.append(T(76, 420, "Det kostet", 15, W, 700, font="k") + T(76, 442, "−1 200 kr", 18, W, 800))
    o.append(arrow("M120 452 C126 470 130 480 136 490"))
    o.append(T(76, 512, "Penger nå:", 15, W, 700, font="k") + T(76, 534, "17 250 kr", 18, W, 800))
    o.append(arrow("M196 330 C214 360 222 380 226 400 M218 394 L226 400 L230 390"))
    o.append(T(196, 420, "Sammen med", 15, W, 700, font="k") + T(196, 440, "venner: sosialt opp", 15, W, 700, font="k"))
    o.append(arrow("M228 452 C232 470 232 480 230 490"))
    o.append(T(196, 512, "Trivsel:", 15, W, 700, font="k") + T(196, 534, "64 → 70", 18, W, 800))
    o.append(sticker(232, 690, 130, None, "Lukk", 2, "Lukk", primary=True))
    o.append(status() + home_ind())
    return o


# ------------------------------------------------------------------ områdene
@screen("15-manedsplan", "Kveldene i april",
        "Glasset blir mørkere, og fire kvelder er tegnet opp med hvit tusj. To er fylt med klistremerker: Trening og Kino med Emma. To er ledige. "
        "Under ligger aktiviteter du kan trykke på for å fylle en ledig kveld. Ferdig er hovedhandlingen.")
def s15():
    o = scene(locks=(), pose="stand", stats=None, kveldene=None, show_age=False, dim=.6, switch_on=False, job=False)
    W = WHITE
    o.append(marker(68, 196, "Kveldene i april", 24, fill=W) + T(68, 220, "Trykk på en aktivitet for å fylle", 13.5, W, 600) + T(68, 238, "en ledig kveld.", 13.5, W, 600))
    slots = [(66, 262, "Trening", "0 kr"), (178, 262, "Kino", "150 kr"), (66, 360, None, None), (178, 360, None, None)]
    for x, y, t, v in slots:
        o.append(f'<rect x="{x}" y="{y}" width="104" height="84" rx="10" fill="none" stroke="{W}" stroke-width="2.4" stroke-dasharray="7 5"/>')
        if t:
            o.append(f'<g filter="url(#soft)"><rect x="{x+6}" y="{y+14}" width="92" height="56" rx="14" fill="#FFFFFF" stroke="{C["ink2"]}" stroke-width="1.5"/></g>'
                     + T(x + 16, y + 38, t, 14, C["ink"], 800) + T(x + 16, y + 58, v, 12.5, C["ink2"], 650))
        else:
            o.append(f'<path d="M{x+52} {y+30} V{y+54} M{x+40} {y+42} H{x+64}" stroke="{W}" stroke-width="2.6" stroke-linecap="round"/>' + T(x + 52, y + 74, "ledig", 13, W, 700, "middle"))
    o.append(T(68, 476, "Aktiviteter", 15, W, 800))
    acts = [("Gaming", "0 kr"), ("Venner", "ca. 200 kr"), ("Trening", "0 kr"), ("Hvile", "0 kr")]
    for i, (a, v) in enumerate(acts):
        o.append(sticker(64 + (i % 2) * 116, 490 + (i // 2) * 58, 110, None, a, (-2, 2, 1, -1)[i], f"{a}, {v}", sub=v))
    o.append(T(68, 640, "Fritid er aldri bortkastet:", 13.5, W, 700) + T(68, 658, "hvile teller for trivselen.", 13.5, W, 600))
    o.append(sticker(250, 700, 120, "pil", "Ferdig", -2, "Ferdig", primary=True))
    o.append(status() + home_ind())
    return o


@screen("16-jobb", "Jobben", "Mobilen i hendene med vakt-appen: deltidsjobb i butikken, timer per uke med minus og pluss, maksimum i skoleåret, lønn i april og en ekstravakt du kan ta.")
def s16():
    o = scene()
    sub = "#5A5E6B"
    stepper = (f'<circle cx="92" cy="330" r="22" fill="#FFFFFF" stroke="{C["ink"]}" stroke-width="2"/><path d="M82 330 H102" stroke="{C["ink"]}" stroke-width="3" stroke-linecap="round"/>'
               + T(195, 340, "8 t/uke", 26, C["ink"], 800, "middle") +
               f'<circle cx="298" cy="330" r="22" fill="#FFFFFF" stroke="{C["ink"]}" stroke-width="2"/><path d="M288 330 H308 M298 320 V340" stroke="{C["ink"]}" stroke-width="3" stroke-linecap="round"/>')
    body = (f'<rect x="62" y="176" width="266" height="86" rx="16" fill="#E7F2EE"/>' +
            f'<g transform="translate(76 192)" fill="none" stroke="#2E7D6B" stroke-width="2.4">{JOBB}</g>' +
            T(134, 214, "Butikken", 18, C["ink"], 800) + T(134, 236, "Deltid · ved siden av skolen", 13.5, sub, 600) + T(134, 254, "Timelønn 136,41 kr", 13.5, sub, 600) +
            T(66, 296, "Timer i uka", 15, C["ink"], 800) + stepper +
            T(195, 378, "Maks 12 t/uke i skoleåret", 13.5, sub, 600, "middle") +
            f'<path d="M62 404 H328" stroke="#E2E2E8"/>' +
            T(66, 436, "Lønn i april", 15, C["ink"], 700) + T(324, 436, "4 290 kr", 15, C["ink"], 800, "end") +
            T(66, 462, "Skatt (frikort)", 15, C["ink"], 700) + T(324, 462, "0 kr", 15, C["ink"], 800, "end") +
            f'<rect x="62" y="492" width="266" height="122" rx="16" fill="#FFF5DA" stroke="{C["ink2"]}" stroke-width="1.2"/>' +
            T(80, 522, "Ekstravakt lørdag", 16, C["ink"], 800) + T(80, 544, "5 timer · +545 kr", 14, sub, 600) +
            pill(80, 556, 230, "Ta vakten", True, 44))
    o.append(phone("Vakter", body, back="Tilbake"))
    o.append(status(WHITE))
    return o


@screen("17-penger", "Pengene", "Mobilen i hendene med bankappen: totalt 18450 kroner fordelt på brukskonto, sparekonto og BSU, fremgang mot livsmålet, og kredittkortet som er låst til 18 år.")
def s17():
    o = scene()
    sub = "#5A5E6B"
    row = lambda y, name, info, val: (T(66, y, name, 16, C["ink"], 800) + T(66, y + 20, info, 13, sub, 600) + T(324, y + 8, val, 16, C["ink"], 800, "end") + f'<path d="M62 {y+38} H328" stroke="#E2E2E8"/>')
    body = (T(66, 196, "Totalt", 14, sub, 700) + T(66, 234, "18 450 kr", 34, C["ink"], 800) +
            row(282, "Brukskonto", "til hverdagen", "4 450 kr") + row(344, "Sparekonto", "1,5 % rente", "6 000 kr") + row(406, "BSU", "låst til bolig · skattefradrag", "8 000 kr") +
            f'<g opacity=".7">' + T(66, 468, "Kredittkort", 16, C["ink"], 800) + T(66, 488, "Åpnes når du fyller 18", 13, sub, 600) +
            f'<g transform="translate(306 460)" fill="{C["ink2"]}" stroke="{C["ink2"]}"><rect x="0" y="6" width="14" height="11" rx="2"/><path d="M3 6 V3.5 a4 4 0 0 1 8 0 V6" fill="none" stroke-width="2"/></g></g>' +
            f'<rect x="62" y="520" width="266" height="86" rx="16" fill="#F1EBDD"/>' + T(80, 548, "Livsmål: egen leilighet", 15, C["ink"], 800) +
            f'<rect x="80" y="562" width="230" height="14" rx="7" fill="#FFFFFF" stroke="{C["ink2"]}" stroke-width="1.2"/><rect x="80" y="562" width="71" height="14" rx="7" fill="{C["box"]}" stroke="{C["ink2"]}" stroke-width="1.2"/>' +
            T(80, 596, "31 % spart", 13.5, C["ink"], 700) +
            pill(62, 630, 266, "Flytt penger", True, 50))
    o.append(phone("Banken", body, back="Tilbake"))
    o.append(status(WHITE))
    return o


def scale_marks(x, y, label, val, word, n=5, W=None):
    W = W or C["ink"]
    o = [T(x, y, label, 15, W, 700, font="k") + T(x + 56, y, word, 13, W, 700)]
    for i in range(n):
        cx = x + 116 + i * 18
        o.append(f'<circle cx="{cx}" cy="{y-5}" r="6.5" fill="{W if i < val else "none"}" stroke="{W}" stroke-width="2"/>')
    return "".join(o)


@screen("18-trivsel", "Rommet og trivselen",
        "Speilbildet ser rolig ut. Med tusj står Slik har du det og tre skalaer: stress lavt, fritid passe, sosialt bra, og trivsel 64, ganske bra. "
        "Merknader peker på det i rommet: mopedhjelmen og flyttekassene til egen leilighet.")
def s18():
    o = scene(locks=(), pose="stand", stats=None, kveldene=None, show_age=False, helmet=True, switch_on=False)
    o.append(marker(68, 196, "Slik har du det", 22))
    o.append(scale_marks(68, 232, "Stress", 2, "lavt"))
    o.append(scale_marks(68, 262, "Fritid", 3, "passe"))
    o.append(scale_marks(68, 292, "Sosialt", 4, "bra"))
    o.append(T(68, 330, "Trivsel 64", 20, C["ink"], 800) + T(68, 350, "ganske bra", 14, C["ink"], 600))
    o.append(callout(250, 412, "Mopedhjelm", "", "M254 418 L254 426", 14, "middle"))
    o.append(callout(132, 470, "Flyttekasser:", "egen leilighet 31 %", "M130 484 C122 490 116 496 112 504", 14))
    o.append(sticker(250, 700, 120, "pil", "Tilbake", -2, "Tilbake", primary=True))
    o.append(status() + home_ind())
    return o


@screen("19-arslinje", "Livet ditt: År 1 til 5",
        "Fem fotosnorer henger under hverandre på veggen, én per år fra 15 til 19 år. År 1 er full av bilder. I År 2 har januar til april bilder, og april er ringet inn. År 3 til 5 er blanke kort.")
def s19():
    set_month(3)
    o = [f'<polygon points="0,150 150,108 150,520 0,600" fill="{C["wall_lit"]}"/>', f'<rect x="0" y="742" width="390" height="10" fill="{C["base"]}"/>',
         f'<rect x="0" y="752" width="390" height="92" fill="{C["floor"]}"/>']
    o.append(T(20, 84, "Livet ditt", 28, C["ink"], 800) + marker(20, 112, "Fem år, ett bilde per måned.", 17))
    for k in range(5):
        y0 = 176 + k * 112
        cur = 3 if k == 1 else -1
        upto = 11 if k == 0 else (3 if k == 1 else -1)
        o.append(T(20, y0 - 18, f"År {k+1} · {15+k} år", 15, C["ink"], 800 if k == 1 else 700))
        if k == 1:
            o.append(T(370, y0 - 18, "her er du", 15, C["ink"], 700, "end", font="k"))
        o.append(timeline(cur, k + 1, upto, {3: "trip"} if k == 1 else None, y0=y0, label=False, compact=k != 1))
    o.append(sticker(250, 770, 120, "pil", "Tilbake", -2, "Tilbake", primary=True))
    o.append(status() + home_ind())
    return o


# ------------------------------------------------------------------ press og ferdigheter
@screen("20-kortvarsel", "Kortvarsel ved 18 år",
        "Mars, 18 år, År 4. Et varsel fra banken glir ned: kortregningen på 4200 kroner forfaller. Betaler du bare minstebeløpet, kommer det renter. "
        "To klistremerker er valgene: betal hele eller betal minstebeløpet.")
def s20():
    o = scene(2, 18, 4, locks=(("Fulltidsjobb", 19, JOBB),), stats=("1 ny", "Trivsel 58", "9 800 kr"), helmet=True, boxes=2, goal="54 %", kveldene="3 av 4 ledige")
    o.append(banner("Banken", ["Kortregning 4 200 kr forfaller 20. mars.", "Betaler du bare minstebeløpet, kommer renter."], "#2B4CC4", initial="B"))
    o.append(sticker(56, 640, 182, None, "Betal hele", -2, "Betal hele regningen: 4200 kroner", primary=True, sub="4 200 kr, ingen renter"))
    o.append(sticker(56, 696, 182, None, "Betal minstebeløp", 2, "Betal minstebeløpet: 420 kroner", sub="420 kr, resten får renter"))
    o.append(home_ind())
    return o


@screen("21-krisemaned", "Krisemåned i oktober",
        "Oktober, 18 år. Det regner, glasset er mørkere og speilbildet ser slitent ut. Med hvit tusj står: Oktober går ikke opp, det mangler 2300 kroner, steg 1 av 3. "
        "Tre klistremerker er veier ut: ta ekstravakter, selg mopeden eller spør familien om hjelp.")
def s21():
    o = scene(9, 18, 4, mood="sliten", pose="stand", locks=(), stats=None, kveldene=None, show_age=False,
              helmet=True, dim=.5, switch_on=False, boxes=2, goal="47 %")
    W = WHITE
    o.append(marker(68, 200, "Oktober går ikke opp", 23, fill=W))
    o.append(T(68, 228, "Det mangler 2 300 kr.", 15, W, 700))
    o.append(T(68, 250, "Steg 1 av 3.", 14, W, 600) + T(68, 270, "Det finnes alltid en vei ut.", 14, W, 600))
    o.append(sticker(150, 600, 220, None, "Ta ekstravakter", -2, "Ta ekstravakter: pluss 1600 kroner", sub="+1 600 kr · mer stress"))
    o.append(sticker(150, 656, 220, None, "Selg mopeden", 2, "Selg mopeden: pluss 6000 kroner", sub="+6 000 kr · mister mopeden"))
    o.append(sticker(150, 712, 220, None, "Spør familien om hjelp", -1, "Spør familien om hjelp", sub="lån uten renter, betales tilbake"))
    o.append(status() + home_ind())
    return o


@screen("22-kjorespill", "Kjørespill for mopedlappen",
        "Mobilen i hendene med øvingskjøring: et kryss sett ovenfra, mopeden din og en bil som kommer mot deg. Du skal svinge til venstre. "
        "Tre valg uten tidspress: vent til bilen har kjørt, sving med en gang eller stopp midt i krysset.")
def s22():
    o = scene(0, 16, 2)
    sub = "#5A5E6B"
    road = (f'<rect x="62" y="176" width="266" height="250" rx="16" fill="#A8C49A"/>'
            f'<rect x="62" y="270" width="266" height="64" fill="#5B6270"/><rect x="164" y="176" width="64" height="250" fill="#5B6270"/>'
            f'<path d="M62 302 H160 M232 302 H328 M196 176 V266 M196 338 V426" stroke="#F4F1EA" stroke-width="2.5" stroke-dasharray="10 8"/>'
            f'<rect x="200" y="372" width="18" height="34" rx="6" fill="{C["case"]}" stroke="{C["ink"]}" stroke-width="1.5"/>'
            f'<path d="M209 366 C206 320 190 306 150 302" stroke="{C["ink"]}" stroke-width="2.4" fill="none" stroke-dasharray="5 5"/><path d="M158 296 L148 302 L158 308" stroke="{C["ink"]}" stroke-width="2.4" fill="none"/>'
            f'<rect x="172" y="196" width="20" height="38" rx="6" fill="#2B4CC4" stroke="{C["ink"]}" stroke-width="1.5"/>')
    body = (T(66, 168, "Runde 3 av 5", 13, sub, 700) + road +
            T(66, 456, "Du skal svinge til venstre.", 16, C["ink"], 800) + T(66, 478, "En bil kommer mot deg.", 15, C["ink"], 600) +
            pill(62, 498, 266, "Vent til bilen har kjørt", False, 46) + pill(62, 552, 266, "Sving med en gang", False, 46) + pill(62, 606, 266, "Stopp midt i krysset", False, 46) +
            T(195, 680, "Ingen klokke. Ta den tiden du trenger.", 13, sub, 600, "middle"))
    o.append(phone("Øvingskjøring", body, back="Tilbake"))
    o.append(status(WHITE))
    return o


# ------------------------------------------------------------------ år, retur og slutt
@screen("23-arsslutt", "Året er ferdig",
        "Desember, År 2. Alle tolv kort i fotosnora har bilder, april med bildet fra hytta. Med tusj står År 2 er ferdig. Klistremerker oppsummerer året, og hovedhandlingen er Videre til År 3, 17 år.")
def s23():
    o = scene(11, 16, 2, locks=(), pose="stand", mood="glad", photos_upto=11, special={3: "trip"}, stats=None, kveldene=None, show_age=False, switch_on=False, helmet=True, goal="38 %")
    o.append(marker(68, 196, "År 2 er ferdig!", 26))
    o.append(T(68, 222, "Tolv bilder på snora.", 14.5, C["ink"], 600))
    o.append(sticker(56, 560, 150, None, "+6 200 kr spart", -2, "Spart i år: 6200 kroner", sub="i år"))
    o.append(sticker(56, 616, 150, None, "Trivsel 68", 2, "Trivsel 68", sub="opp fra 61"))
    o.append(sticker(56, 672, 150, None, "Leilighet 38 %", -1, "Livsmål egen leilighet 38 prosent", sub="opp fra 22 %"))
    o.append(sticker(214, 716, 166, "pil", "Til År 3", 2, "Videre til År 3, 17 år", primary=True, sub="du blir 17"))
    o.append(status() + home_ind())
    return o


@screen("24-velkommen-tilbake", "Velkommen tilbake",
        "Du har vært borte en stund. Glasset er litt mørkere, og med hvit tusj står en kort oppsummering: Sist ble du med på hytta i påsken, pengene er 17250 kroner, trivsel 70. Hovedhandlingen er Fortsett.")
def s24():
    o = scene(locks=(), special={3: "trip"}, stats=None, kveldene=None, show_age=False, dim=.55, switch_on=False)
    W = WHITE
    o.append(marker(68, 204, "Velkommen tilbake!", 25, fill=W))
    o.append(T(68, 240, "Sist gang:", 15, W, 800))
    for i, l in enumerate(["Du ble med på hytta i påsken.", "Pengene: 17 250 kr", "Trivsel 70, bra", "Neste: resten av april"]):
        o.append(T(68, 266 + i * 24, l, 15, W, 600))
    o.append(sticker(220, 700, 150, "pil", "Fortsett", -2, "Fortsett", primary=True))
    o.append(status() + home_ind())
    return o


@screen("25-slutt", "Slutten: 20 år",
        "Desember, År 5. Du fyller 20. Speilbildet er eldre og smiler. Flyttekassene er borte, og nøklene til egen leilighet henger på knaggen. "
        "Med tusj står Målet er nådd. Klistremerker oppsummerer livet, og to valg: Se historien din og Start et nytt liv.")
def s25():
    keys = '<circle cx="346" cy="300" r="4" fill="#454656"/><circle cx="346" cy="324" r="14" fill="none" stroke="#C9A24A" stroke-width="4"/><path d="M346 338 V368 M346 352 H356 M346 362 H354" stroke="#C9A24A" stroke-width="4"/>'
    o = scene(11, 20, 5, mood="glad", pose="stand", boxes=0, locks=(), stats=None, kveldene=None, show_age=False, job=False, switch_on=False, photos_upto=11, helmet=True)
    o.append(f'<ellipse cx="346" cy="330" rx="44" ry="50" fill="{C["note"]}" opacity=".5" filter="url(#glow)"/>' + keys)
    o.append(callout(346, 404, "Nøkkelen til", "egen leilighet", "M346 386 V376", 14, "middle"))
    o.append(marker(68, 200, "Målet er nådd!", 26) + T(68, 226, "Du fyller 20 år.", 15, C["ink"], 700))
    o.append(T(68, 290, "Du", 22, C["ink"], 700, font="k") + T(68, 318, "20 år", 26, C["ink"], 800))
    o.append(sticker(56, 560, 158, None, "Ekte seier", -2, "Slutt: ekte seier", sub="mål nådd, trivsel god"))
    o.append(sticker(56, 616, 158, None, "Trivsel 72", 2, "Trivsel 72", sub="i snitt over fem år"))
    o.append(sticker(214, 660, 166, "pil", "Se historien din", -2, "Se historien din", primary=True))
    o.append(sticker(214, 716, 166, None, "Start et nytt liv", 2, "Start et nytt liv"))
    o.append(status() + home_ind())
    return o


# ------------------------------------------------------------------ meny og frakoblet
def menu_row(y, text, red=False):
    c = C["press"] if red else C["ink"]
    return (T(24, y, text, 17, c, 700) + f'<path d="M352 {y-12} l7 7 -7 7" stroke="{c}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            + f'<path d="M24 {y+20} H366" stroke="#DDD8CC"/>')


@screen("26-meny", "Meny", "Et ark over scenen med Konto og e-post, Spillerinformasjon, Om tallene, Personvern, Start et nytt liv, Logg ut og Slett bruker.")
def s26():
    o = scene()
    o.append(sheet(190, "Meny"))
    for i, (t, r) in enumerate([("Konto og e-post", False), ("Spillerinformasjon", False), ("Om tallene", False), ("Personvern", False),
                                ("Start et nytt liv", False), ("Logg ut", False), ("Slett bruker", True)]):
        o.append(menu_row(300 + i * 62, t, r))
    o.append(T(24, 760, "Sletting krever passordet og kan ikke angres.", 13, C["ink2"], 600))
    o.append(status(WHITE) + home_ind())
    return o


@screen("27-om-tallene", "Om tallene", "Et ark som forklarer hvor spillet forenkler: lønn, skatt, renter, kveldene og mopeden.")
def s27():
    o = scene()
    o.append(sheet(110, "Om tallene", ["Spillet bruker ekte norske tall fra 2026,", "men forenkler noen ting."]))
    items = [("Lønn", "Alle jobber gir samme timelønn for alderen."), ("Skatt", "Skatt regnes på årslønna, uten andre fradrag."),
             ("Renter", "Renter regnes én gang i måneden, i hele kroner."), ("Kveldene", "Måneden har fire ledige kvelder, ikke dager."),
             ("Mopeden", "Verdien faller litt hver måned, uansett kjøring.")]
    for i, (h, t) in enumerate(items):
        y = 250 + i * 92
        o.append(f'<circle cx="38" cy="{y+4}" r="12" fill="none" stroke="{C["ink"]}" stroke-width="2"/>' + T(38, y + 9, "i", 14, C["ink"], 800, "middle"))
        o.append(T(62, y + 10, h, 17, C["ink"], 800) + T(62, y + 34, t, 14, C["ink2"], 600) + f'<path d="M24 {y+58} H366" stroke="#DDD8CC"/>')
    o.append(status(WHITE) + home_ind())
    return o


@screen("28-frakoblet", "Frakoblet",
        "Ingen nett. Speilet og rommet vises som vanlig, men klistremerkene og lysbryteren er bleke. En gul lapp på glasset sier: Ingen nett. Du kan se deg rundt. Valgene venter til du er på nett igjen.")
def s28():
    o = scene(stats=None, switch_on=False)
    o.append(stat_stickers(faded=True))
    o.append(f'<g opacity=".5">{switch(glow=False)}</g>' + callout(344, 490, "Slå av lyset", "venter på nett", "", 14, "middle"))
    o.append(note(70, 420, 150, 96, -3, T(12, 30, "Ingen nett", 19, C["ink"], 700, font="k") + T(12, 54, "Du kan se deg rundt.", 13.5, C["ink"], 600)
                  + T(12, 74, "Valgene venter til du", 13.5, C["ink"], 600) + T(12, 90, "er på nett igjen.", 13.5, C["ink"], 600), label="Ingen nett: valgene venter"))
    o.append(status() + home_ind())
    return o


def render(name):
    title, desc, fn = SCREENS[name]
    with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
        f.write(page(title, desc, "\n".join(fn())))


if __name__ == "__main__":
    only = sys.argv[1:]
    for name in sorted(SCREENS):
        if only and not any(name.startswith(x) for x in only):
            continue
        render(name)
        print(name)
