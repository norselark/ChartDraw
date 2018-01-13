"""Functions used by aq_draw"""
ZODIAC_SIGNS = ['Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir',
                'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Psc']

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
    res = '{:02}-{:02} {}'.format(int_part, i, zodiac_sign)
    return res
