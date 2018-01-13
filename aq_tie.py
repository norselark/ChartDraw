import numpy as np

##############################################################
#  Ref: https://cauldronofartandcraft.wordpress.com/chartdraw/
##############################################################
#-------------------------------------------------------------
# aqTIE.BAS --[QBasic]---- Wed--May 18--2016---- 10:12--CEST--
#-------------------------------------------------------------

ZODIAC_ZET9 = ['Ari', 'Tau', 'Gem', 'Cnc', 'Leo', 'Vir',
               'Lib', 'Sco', 'Sgr', 'Cap', 'Aqr', 'Psc']

def calczet9(input_line):
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

spSTR = "TIE"

with open('switch.sw0') as infile:
    swSTR = infile.readline().strip() # Charts (base directory)
    sxSTR = infile.readline().strip() # Temp charts (Charts directory)
    sINT = int(infile.readline().strip())

with open('choice.sw0') as infile:
    gSTR = infile.readline().strip()

fpSTR = ''
fqSTR = ''

inSTR = ''
LSTR = ' '
fiSTR = ''
uSTR = ''

if gSTR == 'N':
    print('           ')
    print('           ')
    print('           ')
elif gSTR == 'i':
    sINT = 1
    print(spSTR)
elif gSTR == 'N':
    print(spSTR)
#
#'' [PH% = 18: ??] ' ---???? ##
#'' [number of planets=8, Sun, Moon] [Node=11] --[np%>hp%?] --[cf2465] [=7= classic!] [Cf. Drawing]
#'' --[dialog prompt!? (to be implemented)]
#
#NP% = 10:       ' [=7= classical! (lag input-prompt)]--[=10?]--[(np% + 1) = Pluto !!]: '[err inp np% > hp%?] ---
npINT = 10
#hp% = np% + 1:  ' (12=incl. Node/ParsFort)
hpINT = npINT + 1
#PP% = hp% + 2:  ' --incl. axes [L20400+/L60000+]
ppINT = hpINT + 2

ysINT = 3 # 3 house syst
bbINT = 33

bSTR_ARR = [''] * (bbINT + 1)
nSTR_ARR = [''] * (bbINT + 1)
rxSTR_ARR = [' '] * (bbINT + 1)
# DIM H$(1, YS%, 3): '[mlmhus (har,syst,nr) :: + sek/tert/sol etc. ?]
hSTR_ARR = np.empty((2, ysINT, 4), dtype=str).astype(object)
# DIM KH$(3)
khSTR_ARR = [''] * 4
# '' [0=cyc ?]
# DIM p$(bb%):     '[2,x[0:g$="p"][1:radix][2:g$="d"]*(changeorder?[L40000+]) #[p$(PP%)]# ''' ## g$ ##
pSTR_ARR = np.empty((bbINT + 1), dtype=str).astype(object)
# DIM m$(1, 5)
mSTR_ARR = np.empty((2, 6), dtype=str).astype(object)
#'----------------------------------
# DIM k$(PP% + 1): '[=15 [k$(15)] ?]
kSTR_ARR = np.empty((ppINT + 2), dtype=str).astype(object)
#'----------------------------------
# DIM z(1, PP%): '[?]
zFLT_ARR = np.zeros((2, ppINT + 1), dtype=float)
#'-------------------

#'--string inits--------

khSTR_ARR[0] = 'x'
khSTR_ARR[1] = 'y'
khSTR_ARR[2] = 'z'
khSTR_ARR[3] = 'w'
mSTR_ARR[0, 0] = "'realname'    "
mSTR_ARR[0, 1] = '0x.00.00      '
mSTR_ARR[0, 2] = 'Place X       '
mSTR_ARR[0, 3] = '0x=00         ' # time
mSTR_ARR[0, 4] = '0x0-00 X      ' # long
mSTR_ARR[0, 5] = '0x0-00 Y      ' # lat
f0STR = 'name          '
n0STR = 'type          '
z0STR = 'zone'
d0STR = 'ds'
h0STR = 'height'

if fiSTR == '':
    print('[Temp]')

if fiSTR == '':
    fiSTR = sxSTR

if fpSTR == '':
    fpSTR = 'astro-1.txt'

print('x')
print('WAIT...')

#' ' ' ' ' '|---change order !?----------------------|' ' ' ' ' '
#' ' ' ' ' '|F0$ = "name          "                  |' ' ' ' ' '
#' ' ' ' ' '|N0$ = "type          "                  |' ' ' ' ' '
#' ' ' ' ' '|:
#' ' ' ' ' '| m$(0, 0) = "'realname'    "            |' ' ' ' ' '
#' ' ' ' ' '| m$(0, 1) = "0x.00.00      ": ' date  |' ' ' ' ' '
#' ' ' ' ' '| m$(0, 2) = "Place X       "            |' ' ' ' ' '
#' ' ' ' ' '| m$(0, 3) = "0x=00         ": ' time  |' ' ' ' ' '
#' ' ' ' ' '| m$(0, 4) = "0x0-00 X      ": ' long  |' ' ' ' ' '
#' ' ' ' ' '| m$(0, 5) = "0x0-00 Y      ": ' lat   |' ' ' ' ' '
#' ' ' ' ' '|:
#' ' ' ' ' '| Z0$ = "zone"                           |' ' ' ' ' '
#' ' ' ' ' '| D0$ = "ds": '[Daylight Saving"]        |' ' ' ' ' '
#' ' ' ' ' '| h0$ = "height"                         |' ' ' ' ' '
#' ' ' ' ' '|----------------------------------------|' ' ' ' ' '

#' ' ###
#' ' // [TEMP]--[SEE DEFs ABOVE]--[Edit]
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

#'########## # # # # # ###########
#'[EDIT]: INPUT DIALOG - WHICH PRG
#'########## # # # # # ###########

with open(fiSTR + fpSTR) as infile:
    zSTR = infile.readline()
    if zSTR.startswith('Astrolog 5.34a'):
        prSTR = 'astrolog543a'
    if zSTR.startswith('Astrolog 542J') or zSTR[8:].startswith('Astrolog 542J'):
        prSTR = 'astrolog542j07'
    if zSTR.startswith('Sun'):
        prSTR = 'ZET9'
    fqSTR = 'astro-2.txt'

#'####################################
#'[p$(no axes)]-[??]-[cf. aqDRAW]    '
#'####################################

#if PR$ = "astrolog543a" then goto astrolog
#if PR$ = "astrolog542j07" then goto astrolog
#if PR$ = "ZET9" then goto ZET9

#ZET9:
bSTR_ARR[0] = 'Earth  '
bSTR_ARR[1] = 'Sun    '
bSTR_ARR[2] = 'Moon   '
bSTR_ARR[3] = 'Mercury'
bSTR_ARR[4] = 'Venus  '
bSTR_ARR[5] = 'Mars   '
bSTR_ARR[6] = 'Jupiter'
bSTR_ARR[7] = 'Saturn '
bSTR_ARR[8] = 'Uranus '
bSTR_ARR[9] = 'Neptune'
bSTR_ARR[10] = 'Pluto '
bSTR_ARR[11] = 'Node'
bSTR_ARR[22] = 'I'
bSTR_ARR[23] = 'II'
bSTR_ARR[24] = 'III'
bSTR_ARR[25] = 'IV'
bSTR_ARR[26] = 'V'
bSTR_ARR[27] = 'VI'
bSTR_ARR[28] = 'VII'
bSTR_ARR[29] = 'VIII'
bSTR_ARR[30] = 'IX'
bSTR_ARR[31] = 'X'
bSTR_ARR[32] = 'XI'
bSTR_ARR[33] = 'XII'

#' ' // --------------------------------------'
#' ' // # p$(index) corresponds to b$(index) !
#' ' // --------------------------------------'

# ZET9 calculations
with open(fiSTR + fpSTR) as infile:
    for zSTR in infile:
        zSTR = zSTR.strip('\n') # Remove trailing newline
        for iINT in range(1, bbINT + 1):
            if zSTR[:7] == bSTR_ARR[iINT] and zSTR[25:26] == '-':
                rxSTR_ARR[iINT] = 'r'
            if zSTR[:1] == bSTR_ARR[31]:
                xSTR = zSTR[1]
                if xSTR not in ['I', 'V', 'X']:
                    zSTR = zSTR[-15:]
                    zSTR = calczet9(zSTR)
                    pSTR_ARR[hpINT + 1] = zSTR
                    iINT = bbINT
            if zSTR[:1] == bSTR_ARR[22]:
                xSTR = zSTR[1]
                if xSTR not in ['I', 'V', 'X']:
                    zSTR = zSTR[-15:]
                    zSTR = calczet9(zSTR)
                    pSTR_ARR[hpINT + 2] = zSTR
                    iINT = bbINT

with open(fiSTR + fqSTR) as infile:
    for zSTR in infile:
        zSTR = zSTR.rstrip('\n') # Remove trailing newline
        for iINT in range(1, bbINT + 1):
            if zSTR[:4] == bSTR_ARR[iINT][:4]:
                zSTR = zSTR[18:27]
                pSTR_ARR[iINT] = zSTR
                break


with open(sxSTR + 'SWI.SWI', mode='w') as outfile:
    outfile.write(prSTR + '\n')

with open(sxSTR + 'PDAT.DAT', mode='w') as outfile:
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
    for zINT in range(1, hpINT + 1):
        outfile.write(pSTR_ARR[zINT] + '\n')

with open(sxSTR + 'ANGDAT.DAT', mode='w') as outfile:
    for zINT in range(hpINT + 1, hpINT + 3):
        outfile.write(pSTR_ARR[zINT] + '\n')

with open(sxSTR + 'IDENTITY.TIE', mode='w') as outfile:
    outfile.write(fiSTR + '\n')
    outfile.write(fpSTR + '\n')

if gSTR == 'i':
    sINT = 2
    gSTR = 'z'

with open('switch.sw0', mode='w') as outfile:
    outfile.write(swSTR + '\n')
    outfile.write(sxSTR + '\n')
    outfile.write(' {} \n'.format(sINT))

with open('choice.sw0', mode='w') as outfile:
    outfile.write(gSTR + '\n')

if gSTR == 'N':
    print('TIE        ')
    print('-> DRAW    ')
    print('(loading)  ')
else:
    print('TIE-> DRAW (loading)' + ' - WAIT...', end='')

print('CHAIN aqDRAW.BAS')
