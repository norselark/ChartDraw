"""Functions used by aq_draw"""
ZODIAC_SIGNS = ['Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir',
                'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Psc']

PPINT = 13
HPINT = 12

def truncate_rounding(decimal_string):
    """Sub TruncateRounding"""
    int_part = int(decimal_string[:3])
    zodiac_sign = ZODIAC_SIGNS[int_part // 30]
    int_part -= 30 * (int_part // 30)
    decimal_part = float(decimal_string[3:])
    i = int(decimal_part * 60 + 0.5)
    if i > 59:
        i -= 60
        int_part += 1
    return '{:02}-{:02} {}'.format(int_part, i, zodiac_sign)


def coordinates(angle):
    """Coord relative to QBasic's intrinsic coordinates]<->['ta0' yields DESC (Cyc 1!)]"""
    yy = 360 - angle
    yz = yy + 180
    if yz > 360:
        yz -= 360
    zy = 180 - yy
    if zy < 0:
        zy += 360
    return yy, yz, zy


def preAspectCalc(target, source, ch):
    """Mutates as well as returns target"""
    target[0, 0, 1:PPINT + 1] = source[ch, 1:PPINT + 1]
    return target


def aspectCalc(w, p, ch, hc):
    """Mutates as well as returns w
    Is it supposed to turn spaces at the end into a zero?"""
    r = 0
    for m in range(1, HPINT + 1):
        dec_str = w[0, 0, m]
        k1 = int(dec_str[:3])
        u1 = int(dec_str[-2:]) if dec_str[-2:].strip() else 0
        for y in range(1, HPINT + 1):
            dec_str = p[ch, y]
            k2 = int(dec_str[:3])
            u2 = int(dec_str[-2:]) if dec_str[-2:].strip() else 0
            if u2 > u1:
                k1 = k1 - 1
                u1 = u1 + 60
            if k2 > k1:
                k1 = k1 + 360
            i = k1 - k2
            if i > 180:
                r = abs(60 - r)
                i = abs(360 - (i + 1))
            w[hc, m, y] = '{:03}-{:02}'.format(i, r)
    return w
