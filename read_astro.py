"""Reads tables from ZET9"""

import re
import sys
from pathlib import Path

from lib.utils import dms_to_deg

NUM_HIGH_PLANETS = 11
ZODIAC_ZET9 = ['Ari', 'Tau', 'Gem', 'Cnc', 'Leo', 'Vir',
               'Lib', 'Sco', 'Sgr', 'Cap', 'Aqr', 'Psc']


def match_to_degrees(match):
    """Turn a regex match into a value in degrees.
    The match object must have four groups corresponding to
    degrees, minutes, seconds and sign of the zodiac, respectively
    """
    degree, minute, second, sign = match.groups()
    degree = int(degree) + 30 * ZODIAC_ZET9.index(sign)
    return dms_to_deg(degree, int(minute), float(second))


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


def _read_with_encoding(filename, encoding):
    with open(filename, encoding=encoding) as infile:
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


def read(filename):
    try:
        return _read_with_encoding(filename, 'utf8')
    except UnicodeDecodeError:
        return _read_with_encoding(filename, 'cp1252')


def main():
    """Main function"""
    print(read(sys.argv[1]))


if __name__ == '__main__':
    main()
