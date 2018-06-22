"""
Reads the files Astro-1.txt and Astro-2.txt and outputs data in JSON for use
by the main program.
"""

import json
import re
import sys
from pathlib import Path

from lib.utils import dms_to_deg

NUM_PLANETS = 10
NUM_HIGH_PLANETS = 11
PP = 13


def get_labels():
    """Return a list of labels"""
    res = [''] * 33
    res[0:12] = ['Earth  ', 'Sun    ', 'Moon   ', 'Mercury', 'Venus  ',
                 'Mars   ', 'Jupiter', 'Saturn ', 'Uranus ', 'Neptune', 'Pluto ', 'Node']
    res[22:34] = ['I', 'II', 'III', 'IV', 'V',
                  'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    return res


def match_to_degrees(match):
    """Turn a regex match into a value in degrees.
    The match object must have four groups corresponding to
    degrees, minutes, seconds and sign of the zodiac, respectively
    """
    degree, minute, second, sign = match.groups()
    degree = int(degree) + 30 * ZODIAC_ZET9.index(sign)
    return dms_to_deg(degree, int(minute), float(second))


ZODIAC_ZET9 = ['Ari', 'Tau', 'Gem', 'Cnc', 'Leo', 'Vir',
               'Lib', 'Sco', 'Sgr', 'Cap', 'Aqr', 'Psc']

LABELS_ZET9 = get_labels()


def calczet9(input_line):
    "Parse an input line from a ZET9 file"
    try:
        degrees = int(input_line[:2])
        minutes = int(input_line[3:5])
        seconds = float(input_line[6:11])
        zodiac_sign = input_line[-3:]
    except ValueError:
        raise ValueError(input_line)
        
    # Add 30 * [place in zodiac] to degrees
    degrees = (degrees + 30 * ZODIAC_ZET9.index(zodiac_sign)) % 360

    return dms_to_deg(degrees, minutes, seconds)


def _read_zet9(infile):
    planet_regexp = '^\\w+\\s+(\\d+)°(\\d+)\'(\\d+\\.\\d+)"(\\w+).*$'
    asc_regexp = '^I\\s+(\\d+)°(\\d+)\'(\\d+\\.\\d+)"(\\w+)$'
    mc_regexp = '^X\\s+(\\d+)°(\\d+)\'(\\d+\\.\\d+)"(\\w+)$'

    planet_angles = []
    for line in infile:
        match = re.match(planet_regexp, line)
        if match:
            planet_angles.append(match_to_degrees(match))
        match = re.match(asc_regexp, line)
        if match:
            asc = match_to_degrees(match)
        match = re.match(mc_regexp, line)
        if match:
            mc = match_to_degrees(match)
    return planet_angles[:NUM_HIGH_PLANETS] + [mc, asc]


def _read_with_encoding(file, encoding):
    with open(file, encoding=encoding) as infile:
        # Sniff file to find source program
        line = infile.readline()
        if line.startswith('Sun'):
            source_program = 'ZET9'
        else:
            raise ValueError('Unsupported file format')
        infile.seek(0)

        if source_program == 'ZET9':
            return {"source_program": source_program,
                    "angles": _read_zet9(infile)}


def read(file):
    try:
        return _read_with_encoding(file, 'utf8')
    except UnicodeDecodeError:
        return _read_with_encoding(file, 'cp1252')


def main():
    """Main function"""
    print(read(sys.argv[1]))


if __name__ == '__main__':
    main()
