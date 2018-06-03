"""
Reads the files Astro-1.txt and Astro-2.txt and outputs data in JSON for use
by the main program.
"""

import json
from pathlib import Path
import numpy as np

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


ZODIAC_ZET9 = ['Ari', 'Tau', 'Gem', 'Cnc', 'Leo', 'Vir',
               'Lib', 'Sco', 'Sgr', 'Cap', 'Aqr', 'Psc']

LABELS_ZET9 = get_labels()


def dms_to_deg(degrees, minutes, seconds):
    "Convert a DMS angle to decimal degrees"
    return degrees + (minutes * 60 + seconds) / 3600


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


def main():
    """Main function"""
    with open('switch.sw0') as infile:
        # Charts (base directory)
        infile.readline() # don't need this for now
        # Temp charts (Charts directory)
        data_dir = Path(infile.readline().strip())

    input_dir = data_dir
    filename_1 = 'Astro-1.txt'
    filename_2 = 'Astro-2.txt'

    num_labels = len(LABELS_ZET9)

    pSTR_ARR = np.empty((num_labels + 1), dtype=float)

    # Sniff file to find source program
    with open(input_dir / filename_1) as infile:
        line = infile.readline()
        if line.startswith('Astrolog 5.34a'):
            source_program = 'astrolog543a'
        elif line.startswith('Astrolog 542J') or line[8:].startswith('Astrolog 542J'):
            source_program = 'astrolog542j07'
        elif line.startswith('Sun'):
            source_program = 'ZET9'

    # ZET9 calculations
    if source_program == 'ZET9':
        with open(input_dir / filename_1, encoding='utf-8') as infile:
            for line in infile:
                line = line.strip('\n')  # Remove trailing newline
                for idx in range(1, num_labels):
                    if line[:1] == 'X':
                        if line[1] not in ['I', 'V', 'X']:
                            pSTR_ARR[NUM_HIGH_PLANETS + 1] = calczet9(line[-15:])
                            break
                    if line[:1] == 'I':
                        if line[1] not in ['I', 'V', 'X']:
                            pSTR_ARR[NUM_HIGH_PLANETS + 2] = calczet9(line[-15:])
                            break

    with open(input_dir / filename_2, encoding='utf-8') as infile:
        for line in infile:
            line = line.rstrip('\n')  # Remove trailing newline
            for idx in range(1, num_labels):
                if line[:4] == LABELS_ZET9[idx][:4]:
                    line = line[18:27]
                    pSTR_ARR[idx] = float(line)
                    break
    
    data = {"angles": list(pSTR_ARR[1:NUM_HIGH_PLANETS + 3])}
    json.dump(data, open(data_dir / 'data.json', 'w'), indent=2)


if __name__ == '__main__':
    main()
