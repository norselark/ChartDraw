"""
##############################################################
#  Ref: https://cauldronofartandcraft.wordpress.com/chartdraw/
##############################################################
#-------------------------------------------------------------
# aqTIE.BAS --[QBasic]---- Wed--May 18--2016---- 10:12--CEST--
#-------------------------------------------------------------
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


def calczet9(input_line):
    "Convert DMS to decimal degrees and pad with zeros"
    try:
        degrees = int(input_line[:2])
        minutes = int(input_line[3:5])
        seconds = float(input_line[6:11])
        zodiac_sign = input_line[-3:]
    except ValueError:
        raise ValueError(input_line)
        
    decimal_part = (minutes * 60 + seconds) / 3600

    # Add 30 * [place in zodiac] to degrees
    degrees += 30 * ZODIAC_ZET9.index(zodiac_sign) % 360

    return degrees + decimal_part


PROGRAM_NAME = "TIE"


def main():
    """Main function"""
    with open('switch.sw0') as infile:
        # Charts (base directory)
        base_dir = Path(infile.readline().strip())
        # Temp charts (Charts directory)
        data_dir = Path(infile.readline().strip())
        switch = int(infile.readline().strip())

    with open('choice.sw0') as infile:
        choice = infile.readline().strip()

    print('[Temp]')
    input_dir = data_dir
    filename_1 = Path('Astro-1.txt')
    filename_2 = Path('Astro-2.txt')

    if choice == 'N':
        print('           ')
        print('           ')
        print('           ')
    elif choice == 'i':
        switch = 1
        print(PROGRAM_NAME)

    num_labels = len(LABELS_ZET9)

    pSTR_ARR = np.empty((num_labels + 1), dtype=float)

    print('x')
    print('WAIT...')

    # Sniff file to find source program
    with (input_dir / filename_1).open() as infile:
        line = infile.readline()
        if line.startswith('Astrolog 5.34a'):
            source_program = 'astrolog543a'
        elif line.startswith('Astrolog 542J') or line[8:].startswith('Astrolog 542J'):
            source_program = 'astrolog542j07'
        elif line.startswith('Sun'):
            source_program = 'ZET9'

    # ZET9 calculations
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

    with (data_dir / 'SWI.SWI').open(mode='w') as outfile: # pylint: disable=E1101
        outfile.write(source_program + '\n')

    with (data_dir / 'PDAT.DAT').open(mode='w') as outfile: # pylint: disable=E1101
        outfile.writelines(['"RealName"\n',
                            '"Alias name"\n',
                            '"Type"\n',
                            '"GeoPlace"\n',
                            '"zone"\n',
                            '"0"\n',
                            '"test1"\n',
                            '"test2"\n',
                            '"test3"\n',
                            '"test4"\n'])
        for idx in range(1, NUM_HIGH_PLANETS + 1):
            outfile.write(str(pSTR_ARR[idx]) + '\n')

    with (data_dir / 'ANGDAT.DAT').open(mode='w') as outfile: # pylint: disable=E1101
        for idx in [NUM_HIGH_PLANETS + 1, NUM_HIGH_PLANETS + 2]:
            outfile.write(str(pSTR_ARR[idx]) + '\n')

    with (data_dir / 'IDENTITY.TIE').open(mode='w') as outfile: # pylint: disable=E1101
        outfile.write(str(input_dir) + '\n')
        outfile.write(str(filename_1) + '\n')
    
    data = {"angles": list(pSTR_ARR[1:NUM_HIGH_PLANETS + 3])}
    json.dump(data, open(data_dir / 'data.json', 'w'))

    if choice == 'i':
        switch = 2
        choice = 'z'

    with open('switch.sw0', mode='w') as outfile:
        outfile.write(str(base_dir) + '\n')
        outfile.write(str(data_dir) + '\n')
        outfile.write(' {} \n'.format(switch))

    with open('choice.sw0', mode='w') as outfile:
        outfile.write(choice + '\n')

    print('TIE-> DRAW (loading) - WAIT...')
    print('CHAIN aqDRAW.BAS')


if __name__ == '__main__':
    main()
