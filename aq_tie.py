"""
##############################################################
#  Ref: https://cauldronofartandcraft.wordpress.com/chartdraw/
##############################################################
#-------------------------------------------------------------
# aqTIE.BAS --[QBasic]---- Wed--May 18--2016---- 10:12--CEST--
#-------------------------------------------------------------
"""

import numpy as np

NUM_PLANETS = 10
NUM_HIGH_PLANETS = 11
PP = 13

ZODIAC_ZET9 = ['Ari', 'Tau', 'Gem', 'Cnc', 'Leo', 'Vir',
               'Lib', 'Sco', 'Sgr', 'Cap', 'Aqr', 'Psc']

LABELS_ZET9 = ['Earth  ', 'Sun    ', 'Moon   ', 'Mercury', 'Venus  ', 'Mars   ',
               'Jupiter', 'Saturn ', 'Uranus ', 'Neptune', 'Pluto ', 'Node',
               'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
               'X', 'XI', 'XII']

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
        base_dir = infile.readline().strip() # Charts (base directory)
        data_dir = infile.readline().strip() # Temp charts (Charts directory)
        switch = int(infile.readline().strip())

    with open('choice.sw0') as infile:
        choice = infile.readline().strip()

    fpSTR = ''
    fqSTR = ''

    fiSTR = ''

    if choice == 'N':
        print('           ')
        print('           ')
        print('           ')
    elif choice == 'i':
        switch = 1
        print(PROGRAM_NAME)
    elif choice == 'N':
        print(PROGRAM_NAME)
    #
    #'' [PH% = 18: ??] ' ---???? ##
    #'' --[dialog prompt!? (to be implemented)]
    #

    bbINT = 33

    rxSTR_ARR = [' '] * (bbINT + 1)
    pSTR_ARR = np.empty((bbINT + 1), dtype=str).astype(object)
    mSTR_ARR = np.empty((2, 6), dtype=str).astype(object)

    #'--string inits--------
    mSTR_ARR[0, 0] = "'realname'    "
    mSTR_ARR[0, 1] = '0x.00.00      '
    mSTR_ARR[0, 2] = 'Place X       '
    mSTR_ARR[0, 3] = '0x=00         ' # time
    mSTR_ARR[0, 4] = '0x0-00 X      ' # long
    mSTR_ARR[0, 5] = '0x0-00 Y      ' # lat

    if fiSTR == '':
        print('[Temp]')

    if fiSTR == '':
        fiSTR = data_dir

    if fpSTR == '':
        fpSTR = 'astro-1.txt'

    print('x')
    print('WAIT...')

    mSTR_ARR[1, 0] = 'RealName'
    mSTR_ARR[1, 1] = 'test1'
    mSTR_ARR[1, 2] = 'GeoPlace'
    mSTR_ARR[1, 3] = 'test2'
    mSTR_ARR[1, 4] = 'test3'
    mSTR_ARR[1, 5] = 'test4'
    n1STR = 'Type'
    d1STR = '0'
    f1STR = 'Alias name'
    z1STR = 'zone'

    # Sniff file to find input program
    with open(fiSTR + fpSTR) as infile:
        line = infile.readline()
        if line.startswith('Astrolog 5.34a'):
            prSTR = 'astrolog543a'
        if line.startswith('Astrolog 542J') or line[8:].startswith('Astrolog 542J'):
            prSTR = 'astrolog542j07'
        if line.startswith('Sun'):
            prSTR = 'ZET9'
        fqSTR = 'astro-2.txt'

    #'####################################
    #'[p$(no axes)]-[??]-[cf. aqDRAW]    '
    #'####################################

    #if PR$ = "astrolog543a" then goto astrolog
    #if PR$ = "astrolog542j07" then goto astrolog
    #if PR$ = "ZET9" then goto ZET9

    #ZET9:

    #' ' // --------------------------------------'
    #' ' // # p$(index) corresponds to b$(index) !
    #' ' // --------------------------------------'

    # ZET9 calculations
    with open(fiSTR + fpSTR) as infile:
        for line in infile:
            line = line.strip('\n') # Remove trailing newline
            for iINT in range(1, bbINT + 1):
                if line[:7] == LABELS_ZET9[iINT] and line[25:26] == '-':
                    rxSTR_ARR[iINT] = 'r'
                if line[:1] == LABELS_ZET9[31]:
                    xSTR = line[1]
                    if xSTR not in ['I', 'V', 'X']:
                        line = line[-15:]
                        line = calczet9(line)
                        pSTR_ARR[NUM_HIGH_PLANETS + 1] = line
                        iINT = bbINT
                if line[:1] == LABELS_ZET9[22]:
                    xSTR = line[1]
                    if xSTR not in ['I', 'V', 'X']:
                        line = line[-15:]
                        line = calczet9(line)
                        pSTR_ARR[NUM_HIGH_PLANETS + 2] = line
                        iINT = bbINT

    with open(fiSTR + fqSTR) as infile:
        for line in infile:
            line = line.rstrip('\n') # Remove trailing newline
            for iINT in range(1, bbINT + 1):
                if line[:4] == LABELS_ZET9[iINT][:4]:
                    line = line[18:27]
                    pSTR_ARR[iINT] = line
                    break


    with open(data_dir + 'SWI.SWI', mode='w') as outfile:
        outfile.write(prSTR + '\n')

    with open(data_dir + 'PDAT.DAT', mode='w') as outfile:
        outfile.write('"' + mSTR_ARR[1, 0] + '"\n')
        outfile.write('"' + f1STR + '"\n')
        outfile.write('"' + n1STR + '"\n')
        outfile.write('"' + mSTR_ARR[1, 2] + '"\n')
        outfile.write('"' + z1STR + '"\n') # zone
        outfile.write('"' + d1STR + '"\n') # ds
        outfile.write('"' + mSTR_ARR[1, 1] + '"\n')
        outfile.write('"' + mSTR_ARR[1, 3] + '"\n')
        outfile.write('"' + mSTR_ARR[1, 4] + '"\n')
        outfile.write('"' + mSTR_ARR[1, 5] + '"\n')
        for idx in range(1, NUM_HIGH_PLANETS + 1):
            outfile.write(pSTR_ARR[idx] + '\n')

    with open(data_dir + 'ANGDAT.DAT', mode='w') as outfile:
        for idx in [NUM_HIGH_PLANETS + 1, NUM_HIGH_PLANETS + 2]:
            outfile.write(pSTR_ARR[idx] + '\n')

    with open(data_dir + 'IDENTITY.TIE', mode='w') as outfile:
        outfile.write(fiSTR + '\n')
        outfile.write(fpSTR + '\n')

    if choice == 'i':
        switch = 2
        choice = 'z'

    with open('switch.sw0', mode='w') as outfile:
        outfile.write(base_dir + '\n')
        outfile.write(data_dir + '\n')
        outfile.write(' {} \n'.format(switch))

    with open('choice.sw0', mode='w') as outfile:
        outfile.write(choice + '\n')

    if choice == 'N':
        print('TIE        ')
        print('-> DRAW    ')
        print('(loading)  ')
    else:
        print('TIE-> DRAW (loading)' + ' - WAIT...', end='')

    print('CHAIN aqDRAW.BAS')

if __name__ == '__main__':
    main()
