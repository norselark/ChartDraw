"""Reads tables from ZET9"""

import json
import re
import sys
from typing import Any, Dict, List, Match, TextIO

from .lib.utils import dms_to_deg

NUM_HIGH_PLANETS = 11
ZODIAC_ZET9 = ['Ari', 'Tau', 'Gem', 'Cnc', 'Leo', 'Vir',
               'Lib', 'Sco', 'Sgr', 'Cap', 'Aqr', 'Psc']


def match_to_degrees(match: Match) -> float:
    """Turn a regex match into a value in degrees.
    The match object must have four groups corresponding to
    degrees, minutes, seconds and sign of the zodiac, respectively
    """
    raw_degree, minute, second, sign = match.groups()
    degree = int(raw_degree) + 30 * ZODIAC_ZET9.index(sign)
    return dms_to_deg(degree, int(minute), float(second))


def _read_zet9(infile: TextIO) -> List[float]:
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


def _read_with_encoding(filename: str, encoding: str) -> Dict:
    with open(filename, encoding=encoding) as infile:
        # Sniff file to find source program
        line = infile.readline()
        if line.startswith('Sun'):
            source_program = 'ZET9'
        infile.seek(0)

        if source_program == 'ZET9':
            return {"source_program": source_program,
                    "angles": _read_zet9(infile)}
        else:
            raise ValueError('Unsupported file format')


def read(filename: str) -> Dict[str, Any]:
    if filename.endswith('.json'):
        with open(filename) as file:
            j = json.load(file)
            if 'angles' in j:
                return j
            else:
                raise ValueError('JSON file does not contain required fields')
    # Not JSON: Parse as ZET9 file
    try:
        return _read_with_encoding(filename, 'utf8')
    except UnicodeDecodeError:
        return _read_with_encoding(filename, 'cp1252')


def main() -> None:
    """Main function"""
    print(read(sys.argv[1]))


if __name__ == '__main__':
    main()
