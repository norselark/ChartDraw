"""Functions used by aq_draw"""

ZODIAC_SIGNS = ['Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir',
                'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Psc']

PPINT = 13
HPINT = 12


def truncate_rounding(angle):
    """Sub TruncateRounding"""
    if type(angle) == str:
        angle = float(angle)
    int_part = int(angle)
    decimal_part = angle - int_part
    zodiac_sign = ZODIAC_SIGNS[int_part // 30]
    int_part = int_part % 30
    i = round(decimal_part * 60)
    if i > 59:
        i -= 60
        int_part += 1
    return '{:02}-{:02} {}'.format(int_part, i, zodiac_sign)


def coordinates(angle):
    "Coord relative to QBasic's intrinsic coordinates]<->['ta0' yields DESC (Cyc 1!)]"
    return (180 - angle) % 360


def asp(a, b, orbis=8):
    "Second argument is size of orbis"
    angle = min(abs(a - b), 360 - abs(a - b)) 
    if angle <= orbis:
        return 0
    if abs(30 - angle) <= orbis * 0.25:
        return 30
    if abs(60 - angle) <= orbis * 0.75:
        return 60
    if abs(90 - angle) <= orbis:
        return 90
    if abs(120 - angle) <= orbis:
        return 120
    if abs(180 - angle) <= orbis:
        return 180
    return None


def complex_to_coords(coords):
    "Maps a list of complex numbers to coordinates suitable for Tkinter"
    res = []
    for c in coords:
        res.append(c.real)
        res.append(c.imag)
    return res
