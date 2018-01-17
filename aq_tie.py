"""
##############################################################
#  Ref: https://cauldronofartandcraft.wordpress.com/chartdraw/
##############################################################
#-------------------------------------------------------------
# aqTIE.BAS --[QBasic]---- Wed--May 18--2016---- 10:12--CEST--
#-------------------------------------------------------------
"""

from pathlib import PurePath
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
    """Convert DMS to decimal degrees and pad with zeros"""
    degrees = int(input_line[:2])
    minutes = int(input_line[3:5])
    seconds = float(input_line[6:11])
    zodiac_sign = input_line[-3:]
    decimal_part = (minutes * 60 + seconds) / 3600

    # Add 30 * [place in zodiac] to degrees
    degrees += 30 * ZODIAC_ZET9.index(zodiac_sign)
    # degrees should be < 360, but just in case
    while degrees > 360:
        degrees -= 360

    result_string = str(degrees + decimal_part)
    # Pad left with zeros
    if degrees < 100:
        result_string = '0' + result_string
    if degrees < 10:
        result_string = '0' + result_string
    return result_string


PROGRAM_NAME = "TIE"


def main():
    """Main function"""
    with open('switch.sw0') as infile:
        # Charts (base directory)
        base_dir = PurePath(infile.readline().strip())
        # Temp charts (Charts directory)
        data_dir = PurePath(infile.readline().strip())
        switch = int(infile.readline().strip())

    with open('choice.sw0') as infile:
        choice = infile.readline().strip()

    print('[Temp]')
    input_dir = PurePath(data_dir)
    filename_1 = PurePath('astro-1.txt')
    filename_2 = PurePath('astro-2.txt')

    if choice == 'N':
        print('           ')
        print('           ')
        print('           ')
    elif choice == 'i':
        switch = 1
        print(PROGRAM_NAME)

    bbINT = 33

    rxSTR_ARR = [' '] * (bbINT + 1)
    pSTR_ARR = np.empty((bbINT + 1), dtype=str).astype(object)
    mSTR_ARR = np.empty((2, 6), dtype=str).astype(object)

    mSTR_ARR[0, 0] = "'realname'    "
    mSTR_ARR[0, 1] = '0x.00.00      '
    mSTR_ARR[0, 2] = 'Place X       '
    mSTR_ARR[0, 3] = '0x=00         '  # time
    mSTR_ARR[0, 4] = '0x0-00 X      '  # long
    mSTR_ARR[0, 5] = '0x0-00 Y      '  # lat

    print('x')
    print('WAIT...')

    mSTR_ARR[1, 0] = 'RealName'
    mSTR_ARR[1, 1] = 'test1'
    mSTR_ARR[1, 2] = 'GeoPlace'
    mSTR_ARR[1, 3] = 'test2'
    mSTR_ARR[1, 4] = 'test3'
    mSTR_ARR[1, 5] = 'test4'

    # Sniff file to find source program
    with open(input_dir / filename_1) as infile:
        line = infile.readline()
        if line.startswith('Astrolog 5.34a'):
            source_program = 'astrolog543a'
        if line.startswith('Astrolog 542J') or line[8:].startswith('Astrolog 542J'):
            source_program = 'astrolog542j07'
        if line.startswith('Sun'):
            source_program = 'ZET9'

    # ZET9 calculations
    with open(input_dir / filename_1) as infile:
        for line in infile:
            line = line.strip('\n')  # Remove trailing newline
            for idx in range(1, bbINT + 1):
                if line[:7] == LABELS_ZET9[idx] and line[25:26] == '-':
                    rxSTR_ARR[idx] = 'r'
                if line[:1] == 'X':
                    if line[1] not in ['I', 'V', 'X']:
                        pSTR_ARR[NUM_HIGH_PLANETS + 1] = calczet9(line[-15:])
                        break
                if line[:1] == 'I':
                    if line[1] not in ['I', 'V', 'X']:
                        pSTR_ARR[NUM_HIGH_PLANETS + 2] = calczet9(line[-15:])
                        break

    with open(input_dir / filename_2) as infile:
        for line in infile:
            line = line.rstrip('\n')  # Remove trailing newline
            for idx in range(1, bbINT + 1):
                if line[:4] == LABELS_ZET9[idx][:4]:
                    line = line[18:27]
                    pSTR_ARR[idx] = line
                    break

    with open(data_dir / 'SWI.SWI', mode='w') as outfile:
        outfile.write(source_program + '\n')

    with open(data_dir / 'PDAT.DAT', mode='w') as outfile:
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
            outfile.write(pSTR_ARR[idx] + '\n')

    with open(data_dir / 'ANGDAT.DAT', mode='w') as outfile:
        for idx in [NUM_HIGH_PLANETS + 1, NUM_HIGH_PLANETS + 2]:
            outfile.write(pSTR_ARR[idx] + '\n')

    with open(data_dir / 'IDENTITY.TIE', mode='w') as outfile:
        outfile.write(str(input_dir) + '\n')
        outfile.write(str(filename_1) + '\n')

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
