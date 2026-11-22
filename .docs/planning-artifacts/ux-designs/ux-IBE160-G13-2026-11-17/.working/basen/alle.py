# «Basen» (basecamp): alle skjermene. Kjør: python alle.py [nummer ...]
# Tallene er eksempeldata fra PRD-ens brukerreiser (UJ-1 til UJ-6), ikke motorberegninger.
import os, sys
import basen as B
from basen import C, T, G, mix, grad, gloss, coin, heart, page, ICON_PLAN, ICON_MSG
from leir import (MONTHS, hud, status, home, lock_icon, shield, sky_and_mountain, trail, ground, tent, campfire, camp, figure, portrait,
                  bubble, big_button, white_button, bottom_bar, panel, field, link, option_card, dim_all, phone, banner, season_of)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skjermer")
os.makedirs(OUT, exist_ok=True)
SCREENS = {}
W = "#FFFFFF"
SUB = "#C9D2F2"


def screen(name, title, desc):
    def deco(fn):
        SCREENS[name] = (title, desc, fn)
        return fn
    return deco


# ------------------------------------------------------------------ små ikoner
def i_bag(x, y):
    return f'<path d="M{x-11} {y+12} V{y-4} Q{x-11} {y-12} {x} {y-12} Q{x+11} {y-12} {x+11} {y-4} V{y+12} Z" fill="#2E8A6E"/><path d="M{x-6} {y-12} Q{x} {y-20} {x+6} {y-12}" stroke="#1F5E4B" stroke-width="3" fill="none"/><rect x="{x-6}" y="{y}" width="12" height="7" rx="2" fill="#1F5E4B"/>'


def i_shirt(x, y):
    return f'<path d="M{x-6} {y-12} L{x-16} {y-6} L{x-12} {y+2} L{x-8} {y} V{y+13} H{x+8} V{y} L{x+12} {y+2} L{x+16} {y-6} L{x+6} {y-12} Q{x} {y-6} {x-6} {y-12} Z" fill="{C["teal"]}"/>'


def i_phones(x, y):
    return f'<path d="M{x-12} {y+4} Q{x-12} {y-14} {x} {y-14} Q{x+12} {y-14} {x+12} {y+4}" stroke="#3557D6" stroke-width="4" fill="none"/><rect x="{x-16}" y="{y}" width="9" height="13" rx="4" fill="#3557D6"/><rect x="{x+7}" y="{y}" width="9" height="13" rx="4" fill="#3557D6"/>'


def i_house(x, y):
    return f'<path d="M{x-13} {y+12} V{y-2} L{x} {y-13} L{x+13} {y-2} V{y+12} Z" fill="#C2674F"/><rect x="{x-4}" y="{y+2}" width="8" height="10" fill="#6B4128"/>'


def i_plane(x, y):
    return f'<path d="M{x-14} {y+2} L{x+14} {y-8} L{x+8} {y+10} L{x+2} {y+2} L{x-4} {y+8} Z" fill="#3557D6"/>'


def i_shield(x, y):
    return f'<path d="M{x} {y-13} L{x+12} {y-8} V{y} Q{x+12} {y+10} {x} {y+14} Q{x-12} {y+10} {x-12} {y} V{y-8} Z" fill="#2E8A6E"/><path d="M{x-5} {y} l4 4 7 -8" stroke="#FFFFFF" stroke-width="2.6" fill="none"/>'


def i_coin(x, y):
    return coin(x, y, 12)


def i_heart(x, y):
    return heart(x, y, .9)


def i_bsu(x, y):
    return f'<rect x="{x-13}" y="{y-10}" width="26" height="20" rx="4" fill="#3557D6"/>' + T(x, y + 5, "BSU", 9, "#FFFFFF", 800, "middle")


def i_family(x, y):
    return f'<circle cx="{x-6}" cy="{y-6}" r="5" fill="#C2674F"/><circle cx="{x+7}" cy="{y-4}" r="4" fill="#E09A2B"/><path d="M{x-14} {y+12} Q{x-6} {y-2} {x+2} {y+12} Z M{x} {y+12} Q{x+7} {y+2} {x+14} {y+12} Z" fill="#454B66"/>'


def i_moped(x, y):
    return f'<circle cx="{x-9}" cy="{y+7}" r="5" fill="#2A2F50"/><circle cx="{x+9}" cy="{y+7}" r="5" fill="#2A2F50"/><path d="M{x-9} {y+7} L{x-4} {y-4} H{x+5} L{x+9} {y+7}" stroke="#3557D6" stroke-width="3.5" fill="none"/>'


# ------------------------------------------------------------------ innlogging og start
def start_scene(dim=0):
    o = [sky_and_mountain("sommer"), trail(1, 4, 0, summit_label=False), ground("sommer"), tent(), campfire()]
    if dim:
        o.append(dim_all(dim))
    return "".join(o)


@screen("01-velkommen", "Første skjerm", "Fjellet en sommerkveld med en tom leir. LifeMode står stort over fjellet. Knappene Opprett bruker og Logg inn.")
def s01():
    o = [f'<rect width="390" height="156" fill="{C["hud"]}"/>', start_scene(), f'<rect x="0" y="650" width="390" height="194" fill="{C["hud"]}"/>', status()]
    o.append(G(195, 104, "LifeMode", 50, "#FFFFFF", "middle", "#0B1020"))
    o.append(T(195, 136, "Fem år. Én leir per år. Toppen er målet ditt.", 14.5, SUB, 700, "middle"))
    o.append(big_button(672, "OPPRETT BRUKER", size=23))
    o.append(white_button(14, 758, 362, "Logg inn"))
    return o


@screen("02-opprett-bruker", "Opprett bruker", "Et spillvindu over fjellet med e-post, passord, avkrysning for spillerinformasjonen og knappen Opprett.")
def s02():
    o = [start_scene(.55), status(), panel(18, 190, 354, 560, "Opprett bruker")]
    o.append(T(40, 250, "Det tar under ett minutt.", 14, SUB, 700))
    o.append(field(40, 282, 310, "E-post", "markus@eksempel.no") + field(40, 370, 310, "Passord (minst 8 tegn)", 10, masked=True))
    o.append(f'<rect x="40" y="462" width="26" height="26" rx="7" fill="{C["green"]}" stroke="#FFFFFF" stroke-width="2"/><path d="M46 475 l5 5 9 -10" stroke="#FFFFFF" stroke-width="3" fill="none"/>'
             + T(76, 480, "Jeg har lest spillerinformasjonen", 14, W, 700) + link(76, 506, "Les spillerinformasjonen"))
    o.append(big_button(540, "OPPRETT", w=310, x=40, h=62, size=24))
    o.append(T(195, 650, "Har du allerede en bruker?", 14, SUB, 700, "middle") + link(195, 676, "Logg inn", "middle"))
    o.append(home())
    return o


@screen("03-logg-inn", "Logg inn", "Spillvinduet med e-post og passord, Glemt passord? og knappen Logg inn.")
def s03():
    o = [start_scene(.55), status(), panel(18, 250, 354, 440, "Logg inn")]
    o.append(field(40, 310, 310, "E-post", "markus@eksempel.no") + field(40, 398, 310, "Passord", 10, masked=True))
    o.append(link(40, 492, "Glemt passord?"))
    o.append(big_button(516, "LOGG INN", w=310, x=40, h=62, size=24))
    o.append(T(195, 626, "Ny her?", 14, SUB, 700, "middle") + link(195, 652, "Opprett bruker", "middle"))
    o.append(home())
    return o


@screen("04-glemt-passord", "Glemt passord", "Spillvinduet ber om e-post. Svaret er det samme enten e-posten finnes eller ikke.")
def s04():
    o = [start_scene(.55), status(), panel(18, 270, 354, 400, "Glemt passord")]
    o.append(T(40, 328, "Skriv e-posten din. Finnes den, får du", 14, W, 600) + T(40, 348, "en lenke for å lage nytt passord.", 14, W, 600))
    o.append(field(40, 380, 310, "E-post", "markus@eksempel.no"))
    o.append(big_button(470, "SEND LENKE", w=310, x=40, h=62, size=24, arrow=False))
    o.append(T(40, 574, "Du får samme svar uansett, så ingen kan", 13, SUB, 600) + T(40, 592, "sjekke om e-posten har en bruker.", 13, SUB, 600))
    o.append(link(40, 632, "Tilbake til innlogging"))
    o.append(home())
    return o


@screen("05-livsmal", "Velg toppen din", "Januar, nivå 15. Et spillvindu over fjellet: Velg toppen din, med tre mål som kort: spare til noe stort, råd til en stor opplevelse, gjeldfri med buffer.")
def s05():
    o = [camp(0, 15, 1, "0 kr", "60", 0, stations=False, tags=False, belongings=()), hud(15, 1, 0, "0 kr", "60"), dim_all(.5)]
    o.append(panel(14, 236, 362, 470, "Velg toppen din"))
    o.append(T(36, 294, "Toppen er livsmålet ditt. Det teller mest", 14, W, 700) + T(36, 314, "når du fyller 20.", 14, W, 700))
    o.append(option_card(30, 336, 330, i_house, "Spare til noe stort", "for eksempel egen leilighet", "›", col="#FCE7DD"))
    o.append(option_card(30, 426, 330, i_plane, "En stor opplevelse", "for eksempel interrail", "›", col="#DDE4FC"))
    o.append(option_card(30, 516, 330, i_shield, "Gjeldfri med buffer", "penger til det uventede", "›", col="#DDF3EA"))
    o.append(T(195, 640, "Trykk på målet du vil klatre mot.", 13.5, SUB, 700, "middle"))
    o.append(home())
    return o


@screen("06-avatar", "Hvem er du?", "Et spillvindu med seks utseender som runde bilder. Det valgte står stort i midten med gull rundt. Knappen Dette er meg. Utseendet påvirker ikke tallene.")
def s06():
    o = [camp(0, 15, 1, "0 kr", "60", 0, stations=False, tags=False, belongings=()), hud(15, 1, 0, "0 kr", "60"), dim_all(.5)]
    o.append(panel(14, 200, 362, 610, "Hvem er du?"))
    o.append(f'<circle cx="195" cy="330" r="74" fill="{grad("#8CC3CF", "#6FA9B8")}" stroke="{C["gold"]}" stroke-width="5"/>'
             f'<clipPath id="big"><circle cx="195" cy="330" r="70"/></clipPath><g clip-path="url(#big)">{figure(195, 520, 260, "sara")}</g>')
    looks = ["markus", "amina", "jonas", "sara", "ali", "linh"]
    for i, lk in enumerate(looks):
        cx, cy = 80 + (i % 3) * 115, 466 + (i // 3) * 100
        o.append(portrait(cx, cy, 38, lk))
        if lk == "sara":
            o.append(f'<circle cx="{cx}" cy="{cy}" r="43" fill="none" stroke="{C["gold"]}" stroke-width="5"/>')
    o.append(T(195, 676, "Utseendet påvirker ikke tallene.", 13.5, SUB, 700, "middle"))
    o.append(big_button(700, "DETTE ER MEG", w=320, x=35, h=62, size=24))
    o.append(home())
    return o


@screen("07-pengegave", "Pengegaven", "Januar, nivå 15. Et gullvindu: Pengegave, 18 000 kroner fra besteforeldrene, med mynter og en konvolutt. Tre valg: alt i BSU, halvparten i BSU eller alt på brukskonto.")
def s07():
    o = [camp(0, 15, 1, "0 kr", "60", 0, stations=False, tags=False, belongings=()), hud(15, 1, 0, "0 kr", "60"), dim_all(.5)]
    o.append(panel(14, 210, 362, 560, "Pengegave!"))
    o.append(f'<g transform="rotate(-8 195 300)"><rect x="150" y="262" width="90" height="62" rx="6" fill="#FFFFFF"/><path d="M150 264 L195 296 L240 264" stroke="#C9D0DE" stroke-width="3" fill="none"/></g>' + coin(146, 320, 14) + coin(246, 316, 14) + coin(232, 334, 12))
    o.append(G(195, 384, "18 000 kr", 34, C["gold"], "middle", "#0B1020") + T(195, 408, "fra besteforeldrene", 14, SUB, 700, "middle"))
    o.append(T(36, 446, "Hva gjør du med pengene?", 16, W, 800))
    o.append(option_card(30, 462, 330, i_bsu, "Alt i BSU", "låst til bolig", "18 000", col="#DDE4FC"))
    o.append(option_card(30, 552, 330, i_coin, "Halvparten i BSU", "resten fritt å bruke", "9 000", col="#FFF3D1"))
    o.append(option_card(30, 642, 330, i_coin, "Alt på brukskonto", "fritt å bruke", "18 000", col="#FFF3D1"))
    o.append(home())
    return o


# ------------------------------------------------------------------ måneden og mobilen
@screen("08-maned", "Månedsnavet: april, nivå 16",
        "Basecamp i fjellet en kveld i april. Toppfeltet med nivå 16, penger, trivsel og årsbanen. Stien opp har én leir per år, du er i leir 2, leir 4 er låst til nivå 18, toppen er livsmålet. "
        "Stasjoner: radiomasten (mobil, 2 nye), teltet med mopeden, bålet (kveldene, 2 ledige), lageret (penger) og kiosken (jobb, lønn å hente). Knappen Neste måned.")
def s08():
    return [camp(), hud(), bottom_bar(), home()]


@screen("09-sms-varsel", "SMS fra Emma", "Et varsel glir ned øverst, som en ekte SMS: Emma spør om du blir med på hytta i påsken.")
def s09():
    return [camp(), hud(), bottom_bar(), banner("Emma", ["Hytta i påsken? Vi er fire stykker.", "Bli med?"], "#94601A"), home()]


def msg_row(y, name, text, when, col, unread=False):
    return (f'<circle cx="84" cy="{y}" r="22" fill="{col}"/>' + T(84, y + 7, name[0], 18, W, 800, "middle") +
            T(118, y - 4, name, 16, C["ink"], 800 if unread else 700) + T(326, y - 4, when, 12.5, "#4A5068", 600, "end") +
            T(118, y + 17, text, 13.5, C["ink"] if unread else "#4A5068", 600 if unread else 500) +
            (f'<circle cx="326" cy="{y+12}" r="6" fill="{C["red"]}"/>' if unread else "") + f'<path d="M118 {y+38} H326" stroke="#E2E4EE"/>')


@screen("10-mobil-meldinger", "Mobil: meldingene", "Mobilen fra radiomasten: meldinger fra Emma, Butikken, Mamma og Banken. Du kan ikke svare i spillet.")
def s10():
    body = (msg_row(202, "Emma", "Hytta i påsken? Vi er fire…", "14:02", "#94601A", True) + msg_row(272, "Butikken", "Kan du ta en ekstravakt lørdag?", "11:30", "#1F6B58", True) +
            msg_row(342, "Mamma", "Husk tannlegen på torsdag", "i går", "#7154A8") + msg_row(412, "Banken", "Lønn satt inn: 4 290 kr", "man.", "#2F4BC0") +
            T(195, 720, "Du kan ikke svare på meldinger i spillet.", 13, "#4A5068", 600, "middle"))
    return [camp(), hud(), bottom_bar(), phone("Meldinger", body)]


def mbubble(y, lines, w=230):
    h = 16 + 20 * len(lines)
    return f'<rect x="62" y="{y}" width="{w}" height="{h}" rx="18" fill="#E7E9F2"/>' + "".join(T(78, y + 26 + i * 20, l, 14.5, C["ink"], 500) for i, l in enumerate(lines))


@screen("11-mobil-samtale", "Mobil: invitasjonen", "Samtalen med Emma og invitasjonen som kort med knappen Legg i planen. Du kan ikke svare i spillet.")
def s11():
    body = (T(195, 186, "I dag 14:02", 12.5, "#4A5068", 600, "middle") + mbubble(200, ["Hei! Vi drar på hytta til", "mormoren min i påsken"]) +
            mbubble(268, ["Vi er fire stykker. Mat og buss", "deler vi på, ca. 1 200 kr hver"], 246) + mbubble(336, ["Bli med?"], 96) +
            f'<rect x="62" y="400" width="266" height="182" rx="18" fill="#FFFFFF" stroke="#C9CFE3" stroke-width="1.5"/>' +
            f'<rect x="62" y="400" width="266" height="64" rx="18" fill="{grad("#8EA3C9", "#DCE6F2")}"/><path d="M150 464 V440 L172 424 L194 440 V464 Z" fill="#C2674F"/>' +
            T(80, 490, "Påske på hytta", 17, C["ink"], 800) + T(80, 512, "Påskeferien · ca. 1 200 kr", 14, "#4A5068", 600) +
            gloss(80, 524, 230, 42, 14, C["green"], 4) + G(195, 552, "Legg i planen", 17, W, "middle", C["green2"]) +
            T(195, 614, "Du bestemmer deg når påsken kommer.", 13, "#4A5068", 600, "middle") + T(195, 720, "Du kan ikke svare i spillet.", 13, "#4A5068", 600, "middle"))
    return [camp(), hud(), bottom_bar(), phone("Emma", body, back="Meldinger")]


# ------------------------------------------------------------------ hendelser
@screen("12-hendelse", "Hendelse: påsken", "Emma kommer til leiren. Et spillvindu: Påsken, med tre valg som kort: bli med på hytta, ta ekstravakter eller slappe av i leiren. Trivselen ser du etter valget.")
def s12():
    o = [camp(stations=False, tags=False), figure(300, 640, 104, dict(skin="#C68E68", hair="#1D1B22", hood="#E09A2B", style="lang"), "smil"), hud(), dim_all(.5)]
    o.append(panel(14, 232, 362, 470, "Påsken", C["red"]))
    o.append(f'<circle cx="62" cy="304" r="28" fill="#FCE7DD"/>' + f'<clipPath id="em"><circle cx="62" cy="304" r="26"/></clipPath><g clip-path="url(#em)">{figure(62, 400, 110, dict(skin="#C68E68", hair="#1D1B22", hood="#E09A2B", style="lang"))}</g>')
    o.append(T(102, 296, "Emma: «Hytta i påsken?", 15, W, 700) + T(102, 316, "Vi er fire stykker. Bli med?»", 15, W, 700))
    o.append(option_card(30, 350, 330, i_bag, "Bli med på hytta", "mat og buss deles", "−1 200 kr", col="#DDF3EA"))
    o.append(option_card(30, 440, 330, i_shirt, "Ta ekstravakter", "fire vakter i butikken", "+1 090 kr", col="#DDF3EA"))
    o.append(option_card(30, 530, 330, i_phones, "Slapp av i leiren", "hjemme hele påsken", "0 kr", col="#DDE4FC"))
    o.append(T(195, 646, "Trivselen ser du etter at du har valgt.", 13.5, SUB, 700, "middle"))
    o.append(f'<rect x="0" y="720" width="390" height="124" fill="{C["hud"]}"/>' + T(195, 776, "Trykk på et kort for å velge.", 15, W, 800, "middle") + home())
    return o


def result_row(y, icon, text, value, sub=None):
    return (f'<rect x="34" y="{y}" width="322" height="60" rx="16" fill="#FFFFFF" opacity=".1"/>' + f'<circle cx="64" cy="{y+30}" r="20" fill="#FFFFFF"/>' + icon(64, y + 30) +
            T(96, y + 26, text, 15, W, 800) + (T(96, y + 46, sub, 13, SUB, 700) if sub else "") + G(342, y + 37, value, 19, C["gold"], "end", "#0B1020"))


@screen("13-resultat", "Resultat: påsken på hytta", "Du jubler i leiren. Et gullvindu viser resultatet: 1 200 kroner brukt på turen, sosialt opp, trivsel fra 64 til 70, og et nytt minne. Knappene Hvorfor? og Fortsett.")
def s13():
    o = [camp(money="17 250 kr", trivsel="70", mood="glad", stations=False, tags=False), hud(money="17 250 kr", trivsel="70"), dim_all(.45)]
    o.append(panel(14, 236, 362, 438, "Påsken på hytta"))
    o.append(result_row(286, i_coin, "Brukt på turen", "−1 200 kr", "penger nå: 17 250 kr"))
    o.append(result_row(358, i_family, "Sosialt", "opp", "sammen med Emma og gjengen"))
    o.append(result_row(430, i_heart, "Trivsel", "64 → 70", "bra"))
    o.append(f'<rect x="34" y="502" width="322" height="70" rx="16" fill="{grad("#8EA3C9", "#DCE6F2")}"/><path d="M60 572 V548 L84 530 L108 548 V572 Z" fill="#C2674F"/>'
             + T(124, 532, "Nytt minne i leiren", 15, C["ink"], 800) + T(124, 552, "Påske på hytta, 16 år", 13, C["ink"], 700))
    o.append(white_button(34, 596, 130, "Hvorfor?", 54, 17) + big_button(596, "FORTSETT", w=180, x=176, h=54, size=19))
    o.append(f'<rect x="0" y="700" width="390" height="144" fill="{C["hud"]}"/>' + home())
    return o


@screen("14-hvorfor", "Hvorfor?", "Et spillvindu som tegner opp sammenhengen: Du ble med på hytta, det kostet 1200 kroner, pengene ble 17250. Du var sammen med venner, sosialt gikk opp, og trivselen gikk fra 64 til 70.")
def s14():
    o = [camp(money="17 250 kr", trivsel="70", stations=False, tags=False), hud(money="17 250 kr", trivsel="70"), dim_all(.6)]
    o.append(panel(14, 220, 362, 500, "Hvorfor?"))
    arrow = lambda x, y1, y2: f'<path d="M{x} {y1} V{y2} m-7 -8 7 8 7 -8" stroke="{C["gold"]}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    box = lambda y, t, v: f'<rect x="34" y="{y}" width="322" height="50" rx="14" fill="#FFFFFF"/>' + T(52, y + 31, t, 15, C["ink"], 800) + G(338, y + 33, v, 17, C["ink"], "end")
    o.append(box(266, "Du ble med på hytta i påsken", "") + arrow(195, 320, 346))
    o.append(T(52, 370, "Det kostet", 14, W, 700) + G(338, 372, "−1 200 kr", 17, C["gold"], "end", "#0B1020") + arrow(110, 382, 406))
    o.append(box(410, "Penger nå", "17 250 kr"))
    o.append(T(52, 492, "Sammen med venner: sosialt opp", 14, W, 700) + arrow(110, 502, 526))
    o.append(box(530, "Trivsel", "64 → 70"))
    o.append(big_button(610, "LUKK", w=200, x=95, h=58, size=22, arrow=False))
    o.append(f'<rect x="0" y="730" width="390" height="114" fill="{C["hud"]}"/>' + home())
    return o


# ------------------------------------------------------------------ områdene
@screen("15-manedsplan", "Kveldene ved bålet", "Et spillvindu: Kveldene i april. Fire plasser rundt bålet, to fylt med Trening og Kino, to ledige. Under ligger aktiviteter som kort du trykker på. Knappen Ferdig.")
def s15():
    o = [camp(stations=False, tags=False), hud(), dim_all(.5), panel(14, 196, 362, 600, "Kveldene i april")]
    o.append(T(36, 254, "Fyll en ledig kveld ved å trykke på en aktivitet.", 13.5, SUB, 700))
    o.append(f'<ellipse cx="195" cy="330" rx="46" ry="22" fill="#FFB35C" opacity=".35"/><path d="M174 350 L216 338 M176 338 L218 350" stroke="#8A5A3C" stroke-width="7" stroke-linecap="round"/>'
             f'<path d="M184 342 C182 322 196 316 194 298 C206 310 214 324 210 342 Z" fill="{grad("#FFD27A", "#FF7A3D")}"/>')
    slots = [(40, 276, "Trening", "0 kr"), (250, 276, "Kino", "150 kr"), (40, 376, None, None), (250, 376, None, None)]
    for x, y, t, v in slots:
        if t:
            o.append(f'<rect x="{x}" y="{y+4}" width="100" height="66" rx="16" fill="#A9B2D6"/><rect x="{x}" y="{y}" width="100" height="66" rx="16" fill="{grad("#FFFFFF", "#EEF1FA")}"/>'
                     + T(x + 50, y + 30, t, 15, C["ink"], 800, "middle") + T(x + 50, y + 50, v, 13, "#454B66", 700, "middle"))
        else:
            o.append(f'<rect x="{x}" y="{y}" width="100" height="66" rx="16" fill="none" stroke="#FFFFFF" stroke-width="2.5" stroke-dasharray="7 6"/>'
                     f'<path d="M{x+50} {y+18} V{y+40} M{x+39} {y+29} H{x+61}" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round"/>' + T(x + 50, y + 58, "ledig", 12.5, W, 700, "middle"))
    o.append(G(36, 482, "Aktiviteter", 18, W))
    acts = [("Gaming", "0 kr"), ("Venner", "ca. 200 kr"), ("Trening", "0 kr"), ("Hvile", "0 kr")]
    for i, (a, v) in enumerate(acts):
        x, y = 34 + (i % 2) * 166, 496 + (i // 2) * 76
        o.append(f'<rect x="{x}" y="{y+4}" width="156" height="62" rx="16" fill="#A9B2D6"/><rect x="{x}" y="{y}" width="156" height="62" rx="16" fill="{grad("#FFFFFF", "#EEF1FA")}"/>'
                 + T(x + 16, y + 27, a, 15, C["ink"], 800) + T(x + 16, y + 47, v, 13, "#454B66", 700))
    o.append(T(36, 668, "Fritid er aldri bortkastet: hvile teller for trivselen.", 13, SUB, 700))
    o.append(big_button(692, "FERDIG", w=200, x=95, h=58, size=22, arrow=False))
    o.append(home())
    return o


@screen("16-jobb", "Jobben i kiosken", "Et grønt spillvindu: Butikken. Timelønn, timer i uka med minus og pluss, maksimum i skoleåret, lønn i april og skatt med frikort. Et tilbud om ekstravakt med knappen Ta vakten.")
def s16():
    o = [camp(stations=False, tags=False), hud(), dim_all(.5), panel(14, 196, 362, 600, "Butikken", C["teal"])]
    o.append(T(36, 254, "Deltid ved siden av skolen", 14, SUB, 700) + T(36, 276, "Timelønn 136,41 kr", 15, W, 800))
    o.append(G(36, 320, "Timer i uka", 18, W))
    o.append(gloss(36, 336, 56, 56, 18, "#4A5890", 5) + G(64, 374, "−", 30, W, "middle") + G(195, 378, "8 t/uke", 30, W, "middle", "#0B1020") +
             gloss(298, 336, 56, 56, 18, "#4A5890", 5) + G(326, 376, "+", 30, W, "middle"))
    o.append(T(195, 420, "Maks 12 t/uke i skoleåret", 13.5, SUB, 700, "middle"))
    o.append(T(36, 462, "Lønn i april", 15, W, 700) + G(354, 464, "4 290 kr", 18, C["gold"], "end", "#0B1020"))
    o.append(T(36, 490, "Skatt (frikort)", 15, W, 700) + G(354, 492, "0 kr", 18, W, "end"))
    o.append(f'<rect x="34" y="514" width="322" height="140" rx="18" fill="#FFF3D1"/>' + T(52, 546, "Ekstravakt lørdag", 17, C["ink"], 800) + T(52, 568, "5 timer · +545 kr", 14, "#454B66", 700))
    o.append(big_button(584, "TA VAKTEN", w=286, x=52, h=54, size=20, arrow=False))
    o.append(white_button(95, 690, 200, "Tilbake", 50, 17) + home())
    return o


@screen("17-penger", "Pengene i lageret", "Et spillvindu: Lageret. Totalt 18450 kroner fordelt på brukskonto, sparekonto og BSU, kredittkortet låst til nivå 18, livsmålet 31 prosent og knappen Flytt penger.")
def s17():
    o = [camp(stations=False, tags=False), hud(), dim_all(.5), panel(14, 196, 362, 610, "Lageret")]
    o.append(T(36, 252, "Totalt", 14, SUB, 700) + G(36, 290, "18 450 kr", 34, C["gold"], "start", "#0B1020"))
    rows = [(i_coin, "Brukskonto", "til hverdagen", "4 450 kr"), (i_coin, "Sparekonto", "1,5 % rente", "6 000 kr"), (i_bsu, "BSU", "låst til bolig", "8 000 kr")]
    for k, (ic, a, b, v) in enumerate(rows):
        o.append(option_card(30, 310 + k * 84, 330, ic, a, b, v, h=70, col="#FFF3D1" if k < 2 else "#DDE4FC"))
    o.append(f'<rect x="30" y="566" width="330" height="54" rx="16" fill="#FFFFFF" opacity=".12"/>' + lock_icon(46, 576) + T(76, 590, "Kredittkort", 15, W, 800) + T(76, 608, "åpner på nivå 18", 13, SUB, 700))
    o.append(T(36, 652, "Livsmål: egen leilighet", 15, W, 800) + f'<rect x="36" y="664" width="318" height="16" rx="8" fill="#3A4778"/><rect x="36" y="664" width="99" height="16" rx="8" fill="{grad("#7FE08F", C["green"])}"/>' + T(354, 652, "31 %", 15, W, 800, "end"))
    o.append(big_button(700, "FLYTT PENGER", w=300, x=45, h=58, size=21, arrow=False) + home())
    return o


def meter(y, label, val, word):
    o = [T(36, y, label, 16, W, 800) + T(354, y, word, 15, C["gold"], 800, "end")]
    for i in range(5):
        o.append(f'<rect x="{36 + i*64}" y="{y+12}" width="58" height="18" rx="9" fill="{grad("#FFE27A", C["gold"]) if i < val else "none"}" stroke="{C["gold"]}" stroke-width="2"/>')
    return "".join(o)


@screen("18-trivsel", "Teltet: slik har du det", "Et spillvindu ved teltet: Slik har du det. Tre målere: stress lavt, fritid passe, sosialt bra. Trivsel 64, ganske bra. Eiendelene i leiren: mopeden.")
def s18():
    o = [camp(stations=False, tags=False), hud(), dim_all(.5), panel(14, 196, 362, 560, "Slik har du det")]
    o.append(f'<circle cx="195" cy="300" r="52" fill="{grad("#8CC3CF", "#6FA9B8")}"/><clipPath id="me"><circle cx="195" cy="300" r="50"/></clipPath><g clip-path="url(#me)">{figure(195, 446, 200, "markus")}</g>')
    o.append(G(195, 384, "Trivsel 64", 26, W, "middle", "#0B1020") + T(195, 406, "ganske bra", 14, SUB, 700, "middle"))
    o.append(meter(446, "Stress", 2, "lavt") + meter(502, "Fritid", 3, "passe") + meter(558, "Sosialt", 4, "bra"))
    o.append(T(36, 626, "I leiren: mopeden (fra nivå 16)", 14, SUB, 700))
    o.append(white_button(95, 660, 200, "Tilbake", 54, 18) + home())
    return o


@screen("19-arslinje", "Turen din: År 1 til 5", "Hele fjellet med fem leirer, én per år. Ved hver leir står årets tolv måneder: År 1 er fullført, i År 2 er januar til april spilt, og april er markert. Toppen er livsmålet.")
def s19():
    o = [f'<rect width="390" height="844" fill="{grad("#6E77C8", "#F3B18E")}"/>', status(), G(20, 84, "Turen din", 30, W, "start", "#0B1020"),
         T(20, 110, "Én leir per år. Toppen er livsmålet.", 14, W, 700)]
    o.append('<path d="M-20 820 L195 150 L410 820 Z" fill="#8E86C6"/><path d="M195 150 L410 820 H300 Z" fill="#5F5A9C" opacity=".6"/><path d="M195 150 L232 236 L212 226 L198 244 L180 224 L162 238 Z" fill="#FFFFFF"/>')
    o.append('<path d="M195 150 V112" stroke="#2A2F50" stroke-width="3"/><path d="M195 112 L229 120 L195 130 Z" fill="#1C8441"/>')
    for k in range(5):
        y = 720 - k * 116
        done = 12 if k == 0 else (4 if k == 1 else 0)
        o.append(f'<rect x="24" y="{y-30}" width="342" height="62" rx="16" fill="{C["hud"]}" opacity=".88" stroke="{C["gold"] if k == 1 else "#3A4778"}" stroke-width="{3 if k == 1 else 2}"/>')
        o.append(G(42, y - 6, f"År {k+1}", 17, W) + T(42, y + 16, f"{15+k} år", 12.5, SUB, 700))
        for i in range(12):
            cx = 122 + i * 20
            fill = grad("#FFE27A", C["gold"]) if i < done else "none"
            o.append(f'<circle cx="{cx}" cy="{y}" r="7" fill="{fill}" stroke="{C["gold"] if i < done else "#8592C4"}" stroke-width="1.6"/>')
            if k == 1 and i == 3:
                o.append(f'<circle cx="{cx}" cy="{y}" r="10" fill="none" stroke="#FFFFFF" stroke-width="2.5"/>')
        if k == 1:
            o.append(T(340, y + 26, "du er her", 12, C["gold"], 800, "end"))
        if k == 3:
            o.append(lock_icon(338, y - 12, s=.8))
    o.append(white_button(95, 774, 200, "Tilbake", 50, 17) + home())
    return o


# ------------------------------------------------------------------ press og ferdigheter
@screen("20-kortvarsel", "Kortvarsel på nivå 18", "Mars, nivå 18, leir 4. Bilen står i leiren. Et varsel fra banken: kortregningen på 4200 kroner forfaller. To knapper: betal hele eller betal minstebeløpet.")
def s20():
    o = [camp(2, 18, 4, "9 800 kr", "58", 54, lock_camp=5, belongings=("moped", "bil"), msgs="1", plan="3", wage="+6 120 kr"), hud(18, 4, 2, "9 800 kr", "58")]
    o.append(f'<rect x="0" y="650" width="390" height="194" fill="{C["hud"]}"/>' + T(195, 678, "Kortregning 4 200 kr forfaller 20. mars", 15, W, 800, "middle"))
    o.append(big_button(692, "BETAL HELE · 4 200 KR", h=60, size=19, arrow=False) + white_button(14, 766, 362, "Betal minstebeløp · 420 kr (resten får renter)", 50, 14))
    o.append(banner("Banken", ["Kortregning 4 200 kr forfaller 20. mars.", "Betaler du bare minstebeløpet, kommer renter."], "#2F4BC0", "B"))
    return o


@screen("21-krisemaned", "Storm i oktober", "Oktober, nivå 18. Storm over leiren, bålet er slukket og du ser sliten ut. Et rødt spillvindu: det mangler 2300 kroner, steg 1 av 3, alltid en vei ut. Tre kort: ta ekstravakter, selg mopeden eller spør familien om hjelp.")
def s21():
    o = [camp(9, 18, 4, "−2 300 kr", "48", 47, lock_camp=5, belongings=("moped",), mood="sliten", weather="storm", lit=False, stations=False, tags=False), hud(18, 4, 9, "−2 300 kr", "48")]
    o.append(panel(14, 300, 362, 470, "Storm i oktober", C["red"]))
    o.append(T(36, 356, "Det mangler 2 300 kr til faste utgifter.", 15, W, 800) + T(36, 378, "Steg 1 av 3. Det finnes alltid en vei ut.", 14, SUB, 700))
    o.append(option_card(30, 398, 330, i_shirt, "Ta ekstravakter", "mer stress", "+1 600 kr", col="#DDF3EA"))
    o.append(option_card(30, 488, 330, i_moped, "Selg mopeden", "mopeden forsvinner", "+6 000 kr", col="#DDE4FC"))
    o.append(option_card(30, 578, 330, i_family, "Spør familien", "lån uten renter", "lån", col="#FCE7DD"))
    o.append(T(195, 700, "Trykk på et kort for å velge.", 14, W, 800, "middle"))
    o.append(f'<rect x="0" y="790" width="390" height="54" fill="{C["hud"]}"/>' + home())
    return o


@screen("22-kjorespill", "Øvingskjøring for mopedlappen", "Et spillvindu med et kryss sett ovenfra: mopeden din skal svinge til venstre og en bil kommer mot deg. Tre valg uten tidspress.")
def s22():
    o = [camp(0, 16, 2, "16 200 kr", "62", 24, stations=False, tags=False, belongings=()), hud(16, 2, 0, "16 200 kr", "62"), dim_all(.55), panel(14, 196, 362, 610, "Øvingskjøring", C["teal"])]
    o.append(T(36, 254, "Mopedlappen · runde 3 av 5", 14, SUB, 700))
    o.append(f'<rect x="34" y="270" width="322" height="230" rx="18" fill="#9ED17E"/><rect x="34" y="356" width="322" height="58" fill="#5B6270"/><rect x="166" y="270" width="58" height="230" fill="#5B6270"/>'
             f'<path d="M34 385 H160 M230 385 H356 M195 270 V352 M195 418 V500" stroke="#F4F1EA" stroke-width="3" stroke-dasharray="10 8"/>'
             f'<rect x="200" y="446" width="18" height="34" rx="6" fill="{C["red"]}" stroke="#151A2E" stroke-width="1.5"/><path d="M209 440 C206 400 190 388 150 385" stroke="#FFFFFF" stroke-width="3" fill="none" stroke-dasharray="5 5"/>'
             f'<rect x="172" y="290" width="20" height="38" rx="6" fill="#3557D6" stroke="#151A2E" stroke-width="1.5"/>')
    o.append(T(36, 534, "Du skal svinge til venstre.", 16, W, 800) + T(36, 556, "En bil kommer mot deg.", 15, SUB, 700))
    o.append(white_button(34, 574, 322, "Vent til bilen har kjørt", 48, 16) + white_button(34, 632, 322, "Sving med en gang", 48, 16) + white_button(34, 690, 322, "Stopp midt i krysset", 48, 16))
    o.append(T(195, 774, "Ingen klokke. Ta den tiden du trenger.", 13, SUB, 700, "middle") + home())
    return o


# ------------------------------------------------------------------ år, retur og slutt
@screen("23-arsslutt", "Leir 3 nådd", "Desember, år 2 er ferdig. Årsbanen er full. Et grønt spillvindu: Leir 3 nådd! Oppsummering av året: 6200 kroner spart, trivsel 68, livsmålet 38 prosent. Knappen Til År 3, nivå 17.")
def s23():
    o = [camp(11, 16, 2, "24 650 kr", "68", 38, mood="glad", stations=False, tags=False), hud(16, 2, 12, "24 650 kr", "68"), dim_all(.45)]
    o.append(panel(14, 236, 362, 460, "Leir 3 nådd!", C["green"]))
    o.append(T(195, 292, "År 2 er ferdig. Hele årsbanen er fylt.", 14, SUB, 700, "middle"))
    o.append(result_row(312, i_coin, "Spart i år", "+6 200 kr"))
    o.append(result_row(384, i_heart, "Trivsel", "68", "opp fra 61"))
    o.append(result_row(456, i_house, "Egen leilighet", "38 %", "opp fra 22 %"))
    o.append(T(195, 548, "Neste år: nivå 17. Sommerjobb og nye leirer.", 13.5, W, 700, "middle"))
    o.append(big_button(574, "TIL ÅR 3", w=300, x=45, h=64, size=24))
    o.append(f'<rect x="0" y="720" width="390" height="124" fill="{C["hud"]}"/>' + home())
    return o


@screen("24-velkommen-tilbake", "Velkommen tilbake", "Du har vært borte en stund. Et spillvindu med kort oppsummering: Sist ble du med på hytta i påsken, pengene er 17250 kroner, trivsel 70. Knappen Fortsett.")
def s24():
    o = [camp(money="17 250 kr", trivsel="70", stations=False, tags=False), hud(money="17 250 kr", trivsel="70"), dim_all(.5)]
    o.append(panel(14, 260, 362, 380, "Velkommen tilbake!"))
    o.append(T(36, 318, "Sist gang", 16, W, 800))
    for i, (ic, t) in enumerate([(i_bag, "Du ble med på hytta i påsken."), (i_coin, "Pengene: 17 250 kr"), (i_heart, "Trivsel 70, bra")]):
        y = 344 + i * 58
        o.append(f'<circle cx="56" cy="{y+16}" r="18" fill="#FFFFFF"/>' + ic(56, y + 16) + T(86, y + 22, t, 15, W, 700))
    o.append(big_button(536, "FORTSETT", w=300, x=45, h=62, size=24))
    o.append(f'<rect x="0" y="660" width="390" height="184" fill="{C["hud"]}"/>' + T(195, 700, "Resten av april venter.", 14, SUB, 700, "middle") + home())
    return o


@screen("25-slutt", "Toppen er nådd", "Du fyller 20. Hele stien er gull og flagget står på toppen. Et gullvindu: Toppen er nådd! Egen leilighet, ekte seier, trivsel 72 i snitt. Knappene Se historien din og Start et nytt liv.")
def s25():
    o = [sky_and_mountain("vinter"), trail(5, None, 100, summit_label=False, done_all=True), ground("vinter"), tent(), campfire(), figure(250, 230, 70, "markus", "glad"),
         hud(20, 5, 12, "112 400 kr", "72"), dim_all(.35)]
    o.append(panel(14, 330, 362, 430, "Toppen er nådd!"))
    o.append(G(195, 392, "Egen leilighet", 26, C["gold"], "middle", "#0B1020") + T(195, 416, "Målet ditt er nådd. Du er 20 år.", 14, SUB, 700, "middle"))
    o.append(result_row(436, i_shield, "Slutt", "Ekte seier", "mål nådd og god trivsel"))
    o.append(result_row(508, i_heart, "Trivsel", "72", "i snitt over fem år"))
    o.append(big_button(588, "SE HISTORIEN DIN", w=322, x=34, h=60, size=21, arrow=False) + white_button(34, 668, 322, "Start et nytt liv", 50, 17))
    o.append(f'<rect x="0" y="776" width="390" height="68" fill="{C["hud"]}"/>' + home())
    return o


# ------------------------------------------------------------------ meny og frakoblet
def menu_row(y, text, red=False):
    col = "#FF8A8E" if red else W
    return (f'<rect x="34" y="{y}" width="322" height="52" rx="14" fill="#FFFFFF" opacity=".08"/>' + T(52, y + 33, text, 16, col, 800) +
            f'<path d="M332 {y+18} l8 8 -8 8" stroke="{col}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')


@screen("26-meny", "Meny", "Et spillvindu: Meny, med konto og e-post, spillerinformasjon, om tallene, personvern, start et nytt liv, logg ut og slett bruker.")
def s26():
    o = [camp(), hud(), dim_all(.6), panel(14, 190, 362, 600, "Meny")]
    for i, (t, r) in enumerate([("Konto og e-post", False), ("Spillerinformasjon", False), ("Om tallene", False), ("Personvern", False), ("Start et nytt liv", False), ("Logg ut", False), ("Slett bruker", True)]):
        o.append(menu_row(234 + i * 62, t, r))
    o.append(T(195, 694 + 32, "Sletting krever passordet og kan ikke angres.", 13, SUB, 700, "middle"))
    o.append(white_button(95, 744, 200, "Lukk", 46, 17) + home())
    return o


@screen("27-om-tallene", "Om tallene", "Et spillvindu som forklarer hvor spillet forenkler: lønn, skatt, renter, kveldene og mopeden.")
def s27():
    o = [camp(), hud(), dim_all(.6), panel(14, 190, 362, 620, "Om tallene")]
    o.append(T(36, 248, "Ekte norske tall fra 2026, men noen", 14, SUB, 700) + T(36, 268, "ting er forenklet:", 14, SUB, 700))
    items = [("Lønn", "Alle jobber gir samme timelønn for alderen."), ("Skatt", "Skatt regnes på årslønna, uten andre fradrag."),
             ("Renter", "Renter regnes én gang i måneden, i hele kroner."), ("Kveldene", "Måneden har fire ledige kvelder, ikke dager."),
             ("Mopeden", "Verdien faller litt hver måned, uansett kjøring.")]
    for i, (h, t) in enumerate(items):
        y = 290 + i * 84
        o.append(f'<rect x="34" y="{y}" width="322" height="72" rx="14" fill="#FFFFFF" opacity=".08"/>' + f'<circle cx="58" cy="{y+24}" r="12" fill="{C["gold"]}"/>' + T(58, y + 29, "i", 14, "#5A3A00", 800, "middle") +
                 T(80, y + 30, h, 16, W, 800) + T(52, y + 56, t, 13.5, SUB, 700))
    o.append(white_button(95, 724, 200, "Lukk", 46, 17) + home())
    return o


@screen("28-frakoblet", "Frakoblet", "Ingen nett. Leiren vises, men et rødt bånd sier Ingen nett, og knappen Neste måned er grå: valgene venter til du er på nett igjen.")
def s28():
    o = [camp(stations=False), hud(), f'<rect x="0" y="156" width="390" height="494" fill="#0B1020" opacity=".25"/>']
    o.append(f'<rect x="20" y="196" width="350" height="64" rx="18" fill="{C["red"]}" stroke="#FFFFFF" stroke-width="2"/>' + G(195, 226, "Ingen nett", 21, W, "middle", "#7A1E22") +
             T(195, 248, "Du kan se deg rundt. Valgene venter.", 13.5, W, 700, "middle"))
    o.append(bottom_bar(button="NESTE MÅNED", hint="Valgene venter til du er på nett igjen.", disabled=True))
    o.append(home())
    return o


def render(name):
    title, desc, fn = SCREENS[name]
    B.DEFS.clear()
    body = "\n".join(fn())
    with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
        f.write(page(title, desc, body))


if __name__ == "__main__":
    only = sys.argv[1:]
    for name in sorted(SCREENS):
        if only and not any(name.startswith(x) for x in only):
            continue
        render(name)
        print(name)
