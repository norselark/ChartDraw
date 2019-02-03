"""Functions used by aq_draw"""

from typing import List, Optional, Sequence, Tuple

from lib.constants import ZODIAC as ZODIAC_SIGNS

PPINT = 13
HPINT = 12


def truncate_rounding(angle: float) -> str:
    """Convert an absolute angle to an angle within a zodiac sign.

    Args:
        angle: a positive angle in degrees
    Returns:
        A string containing an angle less than 30 degrees
        together with one of the signs of the zodiac
    """
    int_part = int(angle)
    decimal_part = angle - int_part
    zodiac_sign = ZODIAC_SIGNS[int_part // 30]
    int_part = int_part % 30
    i = round(decimal_part * 60)
    if i > 59:
        i -= 60
        int_part += 1
    return "{:02}° {:02}' {}".format(int_part, i, zodiac_sign)


def dms_to_deg(degrees: int, minutes: int, seconds: float) -> float:
    """Convert a DMS angle to decimal degrees."""
    if minutes < 0 or minutes >= 60:
        raise ValueError('Minutes must be 0 <= m < 60')
    if seconds < 0 or seconds >= 60:
        raise ValueError('Seconds must be 0 <= s < 60')
    return degrees + (minutes * 60 + seconds) / 3600


def mirror_angle(angle: float) -> float:
    "Mirrors the angle: 0 deg to the left, going clockwise"
    return (180 - angle) % 360


def asp(a: float, b: float, orbis: int = 8) -> Optional[Tuple[int, float]]:
    """Get the aspect between two angles, if any.

    Args:
        a: The first angle, in degrees
        b: The second angle, in degrees
        orbis: The orbis to use for calculating aspect

    Returns:
        A tuple of the basic angle and a number between 0 and 1 indicating
        how close to exact the angle is
    """
    dist = abs(a - b)
    angle = min(dist, 360 - dist)
    aspects = [0, 30, 60, 90, 120, 180]
    for aspect in aspects:
        if aspect == 30:
            orbis_factor = 0.25
        elif aspect == 60:
            orbis_factor = 0.75
        else:
            orbis_factor = 1.0
        if abs(aspect - angle) <= (orbis * orbis_factor):
            return aspect, 1 - abs(aspect - angle) / (orbis * orbis_factor)
    return None


def dist(a: float, b: float) -> float:
    """Closest angular distance between points a and b, in degrees"""
    return min(abs(a - b), 360 - abs(a - b))


def is_sorted(a: float, b: float) -> bool:
    """return true if a' is the clockwise-most angle"""
    return (b - a) % 360 == dist(a, b)


def complex_to_coords(coords: Sequence[complex]) -> List[float]:
    """Maps a list of complex numbers to coordinates suitable for Tkinter"""
    res = []
    for c in coords:
        res.append(c.real)
        res.append(c.imag)
    return res


def harmonics(angles: Sequence[float], harmonic: int) -> List[float]:
    return [(harmonic * angle) % 360 for angle in angles]
