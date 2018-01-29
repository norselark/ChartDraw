"""
# ###############################################################
# # Ref: https://cauldronofartandcraft.wordpress.com/chartdraw/ #
# ###############################################################
#
# aqDRAW.BAS --- Tue--Jun 02--2015--20:56--CEST
# [QBasic]
"""
from pathlib import Path

import numpy as np
import qb_utils

from aq_functions import *

NPINT = 10
HPINT = 11
PPINT = 13

def waitx():
    """Sub WAITx"""
    pass


def l1640():
    """Sub L1640"""
    global chINT, hcINT, tSTR, tfSTR # pylint: disable=W0601
    global suINT, ccSTR, miSTR, ehSTR # pylint: disable=W0601
    chINT = 1
    hcINT = 1
    tSTR = '1'
    tfSTR = '1'
    suINT = 0
    ccSTR = 'O'
    miSTR = '\n'
    ehSTR = ''

def l1630():
    """Sub L1630"""
    global kINT, hINT, taSTR, mmINT # pylint: disable=W0601
    global atSTR, ctSTR, cfSTR, fINT # pylint: disable=W0601
    kINT = 1
    hINT = 1
    taSTR = '1'
    mmINT = 0
    atSTR = '1'
    ctSTR = tSTR
    cfSTR = tfSTR
    fINT = 1
    l1640()

def l6020():
    """Draws three small concentric circles at (x%, y%)"""
    for l in [5, 10, 15]:
        print('CIRCLE ({}, {}), {}, {}'.format(xINT, yINT, l, ilINT))

def l6010():
    global ilINT # pylint: disable=W0601
    ilINT = 1
    l6020()
    raise SystemExit('GOTO L6050')

def in_boxes():
    global chINT, hcINT # pylint: disable=W0601
    if gSTR in ['p', 'x']:
        return
    if bSTR == 'p':
        chINT = 1
        hcINT = 1
        if tSTR != '1':
            chINT = 2
            hcINT = 1
    # There are a couple of labels here

def boxes():
    if gSTR not in ['t', 'h']:
        in_boxes()
    print('|-----------|')
    in_boxes()

spSTR = 'DRAW'
xlocINT = 6

#'' // Use right-left high corner at circle for visuals/hints/alerts/signals etc. --[?}

wsSTR = 'z'

vFLT = 0

rrFLT = 0
rFLT = 0

with open('switch.sw0') as infile:
    swSTR = Path(infile.readline().rstrip('\n'))
    sxSTR = Path(infile.readline().rstrip('\n'))
    sINT = int(infile.readline())

if sINT <= 0:
    raise SystemExit('Irregular')

with (sxSTR / 'SWI.SWI').open() as infile: #pylint: disable=E1101
    prSTR = infile.readline().rstrip('\n')
prSTR = prSTR + "        "

with (sxSTR / 'IDENTITY.TIE').open() as infile: #pylint: disable=E1101
    fSTR = Path(infile.readline().rstrip('\n'))

with open('choice.sw0') as infile:
    cgSTR = infile.readline().rstrip('\n')

if any([cgSTR == 'i',
        not cgSTR,
        cgSTR == 'z' and sINT != 2,
        cgSTR == 'N' and sINT != 3]):
    raise SystemExit('Irregular')

print('SCREEN 12') # '<[auto cls]

# MAIN

ysINT = 2

wSTR_ARR = np.empty((2, PPINT + 1, PPINT + 1), dtype=str).astype(object)
hSTR_ARR = np.empty((2, ysINT + 1, 4), dtype=str).astype(object)

nSTR_ARR = np.empty((3, PPINT + 1), dtype=str).astype(object)
pSTR_ARR = np.empty((3, PPINT + 1), dtype=str).astype(object)
mSTR_ARR = np.empty((2, 6), dtype=str).astype(object)
sSTR_ARR = ['', 'Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir',
            'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Psc']

mSTR_ARR[0, 0] = "'realname'"
mSTR_ARR[0, 1] = '0x.00.00  '
mSTR_ARR[0, 2] = 'Sted X    '
mSTR_ARR[0, 3] = '0x=00     '
mSTR_ARR[0, 4] = '0x0-00 X  '
mSTR_ARR[0, 5] = '0x0-00 Y  '
f0STR = 'navn      '
n0STR = 'betegnelse'


kSTR_ARR = ['', 'S', 'L', 'H', 'V', 'M', 'J', 'D', 'U', 'N', 'P', 'X', 'C', 'A']

hSTR = 'Har'
cSTR = 'Cyc'

uINT = 1
PI = np.pi

#SizeConstants:
xINT = 245
xSTR = str(xINT)
yINT = 240
ySTR = str(yINT)
p1INT = 180
p1STR = str(p1INT - 5)
p2INT = 221
p2STR = str(p2INT)
p3INT = 226
p3STR = str(p3INT + 12)
pxINT = p3INT - p2INT
pxSTR = str(pxINT)
paINT = 56
paSTR = str(paINT - 20)
qINT = p1INT - paINT
qSTR = str(qINT)
qINT = int((p2INT - p1INT) / 2)
oSTR = str(qINT + 5)
wINT = 5
wwINT = int(360 / wINT)
waINT = 30
wbINT = 15
wcINT = 5

ttSTR = 'i'
suSTR = ''
poSTR = ''

gSTR = 'h'
aSTR = 'p'

bSTR = '?'
zaSTR = ''
zfSTR = ''
lSTR = ''
qwSTR = ''
inSTR = ''
uSTR = ''

tSTR = '' # This variable must be defined
tfSTR = '' # This one, too
l1630()

aaINT = 0
bbINT = 0
oINT = 0
ddINT = 1
aINT = 0
iINT = 0
lINT = 0
ilINT = 0
bINT = 0
zINT = 0
uINT = 1
vINT = 1
aINT = 0
eFLT = 0
eINT = 0
stINT = 1
ooINT = 0
oaINT = 8
lyINT = 0
ltINT = PPINT

xxSTR = ''

#locate 3, 58: print "        ";

#L2200: '' // O-B-S----!! ##  (w/ [A]
#IF cg$ = "N" THEN GOSUB L6010: IF SU$ = "y" THEN GOTO L2230
if cgSTR == 'N':
    l6010()
    if suSTR == 'y':
        raise SystemExit('GOTO L2230')
#if cg$ <> "z" then goto L2210
if cgSTR != 'z':
    raise SystemExit('GOTO L2210')

#gosub Boxes
boxes()

#L2210: ' [prg:L2210=L2230]
# LOCATE 13, 68: PRINT "[A] <y><CR>"; : '' // [A] --(even more varia!?)
#L2222: EH$ = INKEY$: IF EH$ <> CHR$(13) AND EH$ <> "y" THEN GOTO L2222
# Wait for input here
ehSTR = 'y'
# IF EH$ = "y" THEN EH$ = "A" ELSE EH$ = " ": '[cf1646]
if ehSTR == 'y':
    ehSTR = 'A'
else:
    ehSTR = ' '
# LOCATE (34 + PP%), 72: PRINT "[" + EH$ + "]"; : '' // --cfMenuInternAndExternGoto] [L7000]

#L2230:
# xx$ = "[disk]   ": GOSUB WAITx
xxSTR = '[disk]   '
waitx()
# GOSUB Boxes
boxes()
# if cg$ = "z" then locate xloc%, 3: print "           ";: '' // [??} ##

with (fSTR / 'PDAT.DAT').open() as infile: #pylint: disable=E1101
    mSTR_ARR[1, 0] = infile.readline().rstrip('\n')
    f1STR = infile.readline().rstrip('\n')
    n1STR = infile.readline().rstrip('\n')
    mSTR_ARR[1, 2] = infile.readline().rstrip('\n')
    if wsSTR in ['p', 'z']:
        tzSTR = infile.readline().rstrip('\n')
        dsSTR = infile.readline().rstrip('\n')
        mSTR_ARR[1, 1] = infile.readline().rstrip('\n')
        mSTR_ARR[1, 3] = infile.readline().rstrip('\n')
    else:
        mSTR_ARR[1, 1] = infile.readline().rstrip('\n')
        mSTR_ARR[1, 3] = infile.readline().rstrip('\n')
        tzSTR = infile.readline().rstrip('\n')
        dsSTR = infile.readline().rstrip('\n')
    mSTR_ARR[1, 4] = infile.readline().rstrip('\n')
    mSTR_ARR[1, 5] = infile.readline().rstrip('\n')
    if wsSTR == 'a':
        zSTR = infile.readline().rstrip('\n')
    for idx in range(1, HPINT + 1):
        line = infile.readline().rstrip('\n')
        pSTR_ARR[1, idx] = line
        v = float(line)
        pSTR_ARR[1, idx] = line + '   '
        line = truncate_rounding(line)
        nSTR_ARR[1, idx] = line

with (fSTR / 'ANGDAT.DAT').open() as infile: #pylint: disable=E1101
    syINT = 1 # What is this variable
    for m in [1, 2]:
        zSTR = infile.readline().rstrip('\n')
        pSTR_ARR[1, HPINT + m] = zSTR
        zSTR = truncate_rounding(zSTR)
        nSTR_ARR[1, HPINT + m] = zSTR
        pSTR_ARR[1, HPINT + m] = pSTR_ARR[1, HPINT + m] + '   '

aINT = 0
wSTR_ARR = preAspectCalc(wSTR_ARR, pSTR_ARR, chINT)
wSTR_ARR = aspectCalc(wSTR_ARR, pSTR_ARR, chINT, hcINT)

yyFLT, yzFLT, zyFLT = coordinates(float(pSTR_ARR[chINT, PPINT]))

# LOCATE 1, 58: PRINT "         ";
# LOCATE 2, 58: PRINT "         ";
# LOCATE 3, 58: PRINT "         ";
# LOCATE 4, 58: PRINT "         ";
# LOCATE 5, 58: PRINT "         "; ; '' // [REDUN]-[?] - (plus test if err double ;) ##
#InWaitx:
# LOCATE 2, 58: PRINT "WAIT !   ";
# LOCATE 3, 58: PRINT xx$; : '' // --[Maxlen!]
# LOCATE 4, 58: PRINT "         ";
# LOCATE 5, 58: PRINT "         ";
#RETURN

#STATUSx:
#LOCATE 2, 58: PRINT "         ";
#LOCATE 3, 58: PRINT "         ";
#locate 2, 58: print sp$;"  ";KK$;"  "; : '' // [MaxLen!]-[Now:Only DRAW]
#locate 3, 58: print cg$;: locate 3, 59: print g$;: locate 3, 61: print mid$(str$(s%),2);: '' // ---[i]
#locate 4, 58: print left$(PR$, 8);: '' // --[redun/rpt or variant?]
#RETURN
#
#Blank:
# IF g$ = "*" OR a% <> 0 THEN GOTO BlankMain: '' //? [i$='*'?]
# FOR L% = 5 TO 6: '' // <-[fm20080][redun?]
# LOCATE L%, 67: PRINT "             ";"9"; : '' // <[e6$ !?][,0 ?]
# NEXT L%

#BlankMain:
# LINE (528, 0)-(528, 479), 6
# PAINT (x%, y%), 0, 6: '' // <--[+1=480? (leak?)]---
# SU% = 0:
#RETURN

#Zodiac:
# SELECT CASE K
# CASE 1
#  DRAW "c3"
#  CALL ari
# CASE 2
#  DRAW "c3"
#  CALL tau
# CASE 3
#  DRAW "c3"
#  CALL gem
# CASE 4
#  DRAW "c3"
#  CALL can
# CASE 5
#  DRAW "c3"
#  CALL leo
# CASE 6
#  DRAW "c3"
#  CALL vir
# CASE 7
#  DRAW "c3"
#  CALL lib
# CASE 8
#  DRAW "c3"
#  CALL sco
# CASE 9
#  DRAW "c3"
#  CALL sag
# CASE 10
#  DRAW "c3"
#  CALL cap
# CASE 11
#  DRAW "c3"
#  CALL aqu
# CASE 12
#  DRAW "c3"
#  CALL psc
# END SELECT
#RETURN

#Menu: '' // [text/infopage (toggle)?] /// <-[g$='N'] ///
# IF a% = 2 THEN RETURN: '' // [a%<>0,a%=1,..?]<-[cf2100+]::
# IF g$ = "N" THEN LY% = 0: GOTO PrintPosNewChart: GOTO MenuInternAndExternGoto: '' // <<-<< [err goto]--[!!]

# tf$ = "1":
# IF tt$ = "i" THEN  tt$ = "1": LY% = 0: GOTO PrintPosNewChart: '' // [cf20460]:[1674]

#MenuInternAndExternGoto: '' // --[cf CHART+?]
# IF g$ = "N" THEN il% = 0: GOSUB L6020

#L39030:
# GOSUB L39040: GOTO MenuInMenu:  '' // <-[g$='h'/'t'] [Sub20570  h e r e ?<-cf20462]
#L39040:
# LOCATE 8, 68: PRINT "<#> "; : IF dd% = 1 THEN PRINT "<?>"; : '' // [compare L20470+]
# LOCATE 10, 68: PRINT "<h> <t> <N>";
# LOCATE 11, 68: PRINT "<a> <d> <E>";
# if CH% = 2 then locate 10,72: print "   ";

# IF sp$ = "\qAMAP.BAS" OR sp$ = "pure" THEN GOTO L39060: '' // <-[1.bat or g$='N'][L2000+]
# LOCATE 11, 77: IF MI$ = "y" THEN GOTO L39056: '' // [L39420+]
# IF sx$ = "X" THEN PRINT "OS"
# IF sx$ = "\qAMAP.BAS" THEN PRINT "XS"
# GOTO L39060
#L39056:
# IF sx$ = "\qAMAP.BAS" THEN PRINT "XO"
# IF sx$ = "X" THEN PRINT "OX"

#L39060:
# LOCATE 14, 68: PRINT "<p> <x> <*>";
# IF a$ = "x" THEN LOCATE 18, 67: PRINT "?\|sozx>   ? "; : '' // [x:<L40036 ?]
# IF a$ = "p" THEN LOCATE (19 + PP%), 70: PRINT "<+> <=>";
# RETURN

#MenuInMenu:
#  LOCATE 9, 68, 0: PRINT "  "; " "; " "; : '' // [,0]!? -- [Note that =D before changes to =S in init run!!] -- [OBS 'SPC']-[!!] ## [?] ##
# g$ = INKEY$: IF g$ = "" THEN GOTO MenuInMenu: '' // <-[fm a$='p'/'x']
# IF a$ <> "x" THEN GOTO L39160
# IF g$ = "\" THEN GOTO L40040: '' // ['+'|'-'?]
# IF g$ = "|" THEN BEEP: GOTO MenuInMenu: '' // [L40140][L39650]----[-OBSNOTE-]
# IF g$ = "s" THEN GOTO L42000: '' // aspsymb[toggle]
# IF g$ = "o" THEN GOTO L42100: '' // maxorb
# IF g$ = "z" THEN BEEP: GOTO L42150: '' // [contin/step+maxhp%][toggle]

# IF g$ = "x" THEN BEEP: GOTO MenuInMenu: '' // <-[TEMP!]

#L39160:
# IF a$ <> "p" THEN GOTO L39240
# IF g$ = "+" THEN GOSUB L53030: GOTO MenuInMenu: '' // [cf53050]
# IF g$ = "=" THEN LY% = LY% - 1: K% = K% + 1: GOSUB L53030: GOTO MenuInMenu: ' '  // [NOsub53300!] --##-- WHAT IS==[??]

#L39240: ' /// [a$=""]?
# IF g$ = "#" THEN dd% = dd% + 1: GOTO L45000: 'toggle chartinfobox
# IF g$ = "*" THEN IF u% = 2 THEN GOSUB Blank: GOTO ChartDraw
# IF g$ = "*" THEN IF u% = 1 THEN GOTO L46000: '[ChartDraw++?]
# IF g$ = "t" and CH% <> 2 THEN GOTO DERIVED: '' // [t$='1'/h%=1 ?] ' [tf$ ?]
# IF g$ = "h" THEN GOTO HARMONIC: '' // #  IFG$="h"anda$="x"ora$="p"then[subwait]:gosub53xxx:goto Menu:: --##--
# IF g$ = "?" AND dd% = 1 THEN GOSUB L45500: '' // ['<?>'='secret'] -- [3rdpage?(ID)]-[?]
#L39350: : : :
# IF g$ = "x" THEN a$ = g$: GOTO FactorData
# IF g$ = "p" THEN a$ = g$: K% = 1: LY% = LY% - 1: GOTO L53000
# IF g$ = "a" AND ln% = 0 THEN ln% = 1: GOSUB AspLines: : GOTO Menu: '' // [L39050 ? <-see sub]<-[goto Menu redun?] <[MenuInMenu ?]
# IF g$ = "a" AND ln% = 1 THEN ln% = 0: GOSUB MinusLines: GOTO Menu
# IF g$ = "d" AND ln% = 0 THEN ln% = 1: GOSUB DomLines: : GOTO Menu: '' // [L39050 ? <-see sub]<-[goto Menu redun?] <[MenuInMenu ?]
# IF g$ = "d" AND ln% = 1 THEN ln% = 0: GOSUB MinusLines: GOTO Menu

# IF g$ = "N" THEN GOSUB L7000: GOTO GoOn

# IF sp$ = "\qAMAP.BAS" OR sp$ = "pure" THEN GOTO L39460: '^^^[L2010?][L39050]
# IF sx$ = "\qAMAP.BAS" THEN IF g$ = "X" THEN sx$ = "X": GOTO L2200
# IF sx$ = "X" THEN IF g$ = "O" THEN sx$ = "\qAMAP.BAS": GOTO L2200
# IF sx$ = "\qAMAP.BAS" THEN IF g$ = "S" THEN sx$ = "X": GOTO L19862: '[19860 ?]
# IF sx$ = "X" THEN IF g$ = "S" THEN sx$ = "\qAMAP.BAS": GOTO L19862: '[19860 ?]
# IF MI$ = "y" THEN IF g$ = "O" THEN sx$ = "\qAMAP.BAS": GOTO L2200
# IF MI$ = "y" THEN IF g$ = "X" THEN sx$ = "X": GOTO L2200

#L39460:
#  IF g$ = "E" THEN GOTO Final
#
#GOTO Menu: '<[loop]
#
#
#Final:
# print: '' // --[?] --[clear buffer in order to get back to DOS proper-[?]
# SYSTEM

#GoOn:
# OPEN "switch.sw0" FOR OUTPUT AS #3: '[subredun cf39500+]? < '' <[.\]
# PRINT #3, sw$
# PRINT #3, sx$
# PRINT #3, s%
# CLOSE #3

#cg$ = g$
#OPEN "choice.sw0" FOR OUTPUT AS #1: '' <[.\]
#PRINT #1, cg$
#CLOSE #1

#LOCATE 1, 52: PRINT ws$ + ": DRAW     "
#LOCATE 2, 52: PRINT "-> TIE     "
#LOCATE 3, 52: PRINT "  (loading)"

#CHAIN "\aqTIE.BAS"
#
#goto Irregular
#END:

#AspLines:
# GOSUB Boxes
# LOCATE 11, 68: PRINT "<2-10>"; " "; : '' // <[8,68 ?] ' [<>. ?]
# GOSUB TypeChoice: y$ = u$: IF VAL(u$) < 2 OR VAL(u$) > 10 THEN GOTO AspLines
# il% = VAL(y$)
# xx$ = "[+Alines]" + STR$(il%): GOSUB WAITx:  '' // [DO: improve text!!]
#GOSUB Boxes 
#GOSUB TempCirc: '' // --[y$]--
# GOSUB PlusAspLines
#RETURN: '[menu--]
#
#
#DomLines:
# il% = 10: '' // [input no. of planets early in prg!] --[temp!]
# xx$ = "[+DLines]": GOSUB WAITx
# GOSUB Boxes
# GOSUB TempCirc
# GOSUB PlusAspLines: '' // --[Dom!]
#RETURN: '[menu]--

#TempCirc:
# CIRCLE (x%, y%), 168, 6: '<[paint border] <[removed in 'Tropos:'!]
# PAINT (x%, y% + 4), 15, 6: '<[pset'd  ?][+4=dum (+1 leaks?)]
#RETURN: '>[AspLines & DomLines][+ InSuorNot/L19862+]

#PlusAspLines: ' /// [+varia!]

# FOR z = 1 TO il%:  '<[NP% + 1:] '<[(9+1)][b%=val() ?!] [z?]<->[float?]
#  v = VAL(P$(CH%, z)) - ZY: IF v < 0 THEN v = v + 360: '' // [sub:cfInMainDraw+]
#  b% = v: v$ = STR$(b%): v$ = MID$(v$, 2)

#  z$ = "168":
#  IF MI$ = "y" THEN z$ = "108": ' [->CHART+ [vars!] [+swi.swi]]

# IF g$ = "d" THEN z$ = "140": i$ = tf$: i% = 0: '<-(t e m p t r y !!) <*

# FOR x = 1 TO il%:  '[NP% + 1:] '[obs! np%][float,x/x%!]
#  dr$ = "": LOCATE 11, 69
#  w$ = w$(HC%, z, x)
#  IF g$ = "a" THEN GOSUB Asp: '<[DR$]
#  IF g$ = "d" THEN GOSUB Dom: '<[DR$]
#  IF dr$ = "" THEN GOTO L23970: '<[next x]

#  PSET (x%, y%): DRAW "ta" + v$: DRAW "br" + z$: '[draw rpt (redun) ?]
#  PZ% = POINT(0): PZ$ = STR$(PZ%): PZ$ = MID$(PZ$, 2)
#  PY% = POINT(1): PY$ = STR$(PY%): PY$ = MID$(PY$, 2):
#  XY$ = PZ$ + "," + PY$
#  v = VAL(P$(CH%, x)) - ZY: IF v < 0 THEN v = v + 360: '' // [gosub:cfInMainDraw+]
#  D% = v
#  PSET (x%, y%): '[^^pz$/px$:cf1062!^^]

#  IF dr$ = "d" THEN GOSUB DLines: i% = 0
#  IF dr$ = ":" THEN GOSUB L24100: GOTO L23970: '[nil] <next
#  IF dr$ = "-" THEN GOSUB L24150: GOTO L23970: '[nil] <next
#  IF dr$ = "*" THEN GOSUB L24200: i% = 2: '<[varptr$ ?]
#  IF dr$ = "k" THEN GOSUB L24250: i% = 4: '<[check gwAmap for 'goto' or likes.. (all!)]
#  IF dr$ = "t" THEN GOSUB L24300: i% = 2: '  -'-
#  IF dr$ = "o" THEN GOSUB L24350: i% = 4

#  IF D% > 359 THEN D% = D% - 360: '[redun?] <*---
#  IF D% < 0 THEN D% = D% + 360: '[redun?] <*---

#  D$ = STR$(D%): D$ = MID$(D$, 2)

#  DRAW "ta" + D$: DRAW "br" + z$
#  DRAW "c" + STR$(i%): DRAW "m" + XY$: '[cmp 'LINE']
# IF g$ = "d" THEN CALL ArrowASC(i$, i%): '<-[t e m p !] <*
#L23970:
# NEXT x
# NEXT z
# GOSUB InnerCircleLines
# PAINT (x%, y% - 4), L%, 6: '<-(see comm 'DrawAsc:[Outer:'] !!) [4=dum]
# CIRCLE (x%, y%), z%, 15
# GOSUB DawnDusk
# GOSUB Tropos
#RETURN: '>[menu (fm g$='a'/'d']'''# [GOTO Menu: '[L39050 ?] [vars:+swi.swi]]

#InnerCircleLines: '<[pset reduns?]
# z% = 9: '<[7 ?] <[use vars!] <-[Resizing!]
# CIRCLE (x%, y%), z%, 6
# IF VAL(sv$) > 180 THEN i% = 1: il% = 9: L% = 3:      '<-blw![check v$!]
# IF VAL(sv$) < 180 THEN i% = 9: il% = 1: L% = 11
#RETURN: '>PlusAspLines
#L24100:
# RETURN: '[cf 23600 <-??] [+ 'deflect' (widen) stellium during chart draw ?!]
#
#L24150:
# RETURN
#
#L24200:
# IF b% < D% THEN IF D% - b% > 180 THEN D% = b% - 60
# IF b% < D% THEN IF D% - b% < 180 THEN D% = b% + 60
# IF b% > D% THEN IF b% - D% > 180 THEN D% = b% + 60
# IF b% > D% THEN IF b% - D% < 180 THEN D% = b% - 60
#RETURN
#
#L24250:
# IF b% < D% THEN IF D% - b% > 180 THEN D% = b% - 90
# IF b% < D% THEN IF D% - b% < 180 THEN D% = b% + 90
# IF b% > D% THEN IF b% - D% > 180 THEN D% = b% + 90
# IF b% > D% THEN IF b% - D% < 180 THEN D% = b% - 90
# RETURN
#
#L24300:
# IF b% < D% THEN IF D% - b% > 180 THEN D% = b% - 120
# IF b% < D% THEN IF D% - b% < 180 THEN D% = b% + 120
# IF b% > D% THEN IF b% - D% > 180 THEN D% = b% + 120
# IF b% > D% THEN IF b% - D% < 180 THEN D% = b% - 120
# RETURN
#
#L24350:
# D% = b% + 180: IF D% > 359 THEN D% = D% - 360
# RETURN
#
#DLines:
# IF b% < D% THEN IF D% - b% > 180 THEN D% = b% - VAL(XL$)
# IF b% < D% THEN IF D% - b% < 180 THEN D% = b% + VAL(XL$)
# IF b% > D% THEN IF b% - D% > 180 THEN D% = b% + VAL(XL$)
# IF b% > D% THEN IF b% - D% < 180 THEN D% = b% - VAL(XL$)
# RETURN: '>[plusasplines]
#
#Asp:
# XL$ = LEFT$(w$, 3): ZL$ = RIGHT$(w$, 2): '[float?]<->[rounded!!]
# XZ$ = XL$ + "." + ZL$:
# E = VAL(XZ$): '--[w$(0,0) & (0,x)?]--
# AO% = OA%:           IF E <= 0 + AO% THEN GOTO L43100
# AO% = (OA% / 4):     IF E >= 30 - AO% AND E <= 30 + AO% THEN GOTO L43150
# AO% = (OA% / 4) * 3: IF E >= 60 - AO% AND E <= 60 + AO% THEN GOTO L43200
# AO% = OA%:           IF E >= 90 - AO% AND E <= 90 + AO% THEN GOTO L43250
# AO% = OA%:           IF E >= 120 - AO% AND E <= 120 + AO% THEN GOTO L43300
# AO% = OA%:           IF E >= 180 - AO% AND E <= 180 + AO% THEN GOTO L43350
# RETURN: '>[plusasplines]
#
#L43100: PRINT ":"; : dr$ = ":": RETURN: '[dr$: >PlusAspLines+]
#L43150: PRINT "-"; : dr$ = "-": RETURN: '[TecCompu:compare 'loose' for-next]
#L43200: PRINT "*"; : dr$ = "*": RETURN
#L43250: PRINT "k"; : dr$ = "k": RETURN
#L43300: PRINT "t"; : dr$ = "t": RETURN
#L43350: PRINT "o"; : dr$ = "o": RETURN
#
#Dom:
# y$ = RIGHT$(N$(CH%, z), 3)
# XL$ = LEFT$(w$, 3)
# IF y$ = s$(1) THEN IF x = 5 THEN dr$ = "d": RETURN: '<all!? <-[CHECK QBasic CHECK] !! <*
# IF y$ = s$(2) THEN IF x = 4 THEN dr$ = "d": ' -'-
# IF y$ = s$(3) THEN IF x = 3 THEN dr$ = "d"
# IF y$ = s$(4) THEN IF x = 2 THEN dr$ = "d"
# IF y$ = s$(5) THEN IF x = 1 THEN dr$ = "d"
# IF y$ = s$(6) THEN IF x = 3 THEN dr$ = "d"
# IF y$ = s$(7) THEN IF x = 4 THEN dr$ = "d"
# IF y$ = s$(8) THEN IF x = 10 THEN dr$ = "d": '<[modern]
# IF y$ = s$(9) THEN IF x = 6 THEN dr$ = "d"
# IF y$ = s$(10) THEN IF x = 7 THEN dr$ = "d"
# IF y$ = s$(11) THEN IF x = 8 THEN dr$ = "d": '<[modern]
# IF y$ = s$(12) THEN IF x = 9 THEN dr$ = "d": '<[modern]
#RETURN: '>[plusasplines]
#
#
#MinusLines:
# xx$ = "[-Lines]": GOSUB WAITx
# GOSUB Boxes
# CIRCLE (x%, y%), 168, 6: '' // --[is kept +lines 'c6' circ ??] --[cf. TempCirc !]  [+ (168+1) cleanup fm asp&dom lines?)
# PAINT (x%, y% - 4), 1, 6: '' // --[pset'd ?][+/- 4=dum <(aspcircle=7)] --(paint color '1' ?)
# CIRCLE (x%, y%), pa%:
# CIRCLE (x%, y%), 168, 0:     '' // --[remove ?!]
# PAINT (x%, y% - 1), 1, 15:     '' // --[best placement of this code?] --[cmp DawnDusk !!]
# PAINT (x%, y% + 1), 0, 15:     '' //  -'-
#  FOR m = (hp% + 2) TO (hp% + 1) STEP -1: '' // [Reverse hp%+ (Asc/Mc)]:?:[cf. 'Axes:']
#  GOSUB axes
#  NEXT m
# GOSUB Tropos
#RETURN: '[menu]--
#
#
#FactorData:
# GOSUB Boxes: LOCATE 10, 68: PRINT "this<CR> or"; : '[c32?]
# LOCATE 11, 68: PRINT "aspects "; "<--";
# LOCATE 12, 68: PRINT ; "har "; : GOSUB TypeChoice: TA$ = u$
# IF u$ = "" THEN TA$ = t$: AT$ = t$: GOTO InFactorData1
# IF VAL(u$) < 1 OR VAL(u$) > 300 THEN GOTO FactorData: '' // [ERRCHK!]
# LOCATE 11, 76: PRINT "<->";
# LOCATE 13, 68: PRINT ; "har "; : GOSUB TypeChoice: AT$ = u$
# IF VAL(u$) < 1 OR VAL(u$) > 300 THEN GOTO FactorData: '[errchk!<-(kunat$?]

#InFactorData1:
# GOSUB Boxes
# GOSUB L53300: '' // [L40000?]
# xx$ = TA$ + "&" + AT$: GOSUB WAITx: '' // --[REVORDER Box-Wait ?]
# IF u$ = "" AND t$ = "1" THEN HC% = 1: GOSUB L40500: GOTO InFactorData2: '' // [ch%=1 ?]
# HC% = 0: '' // [print h$/c$ ?][cfHC%<-laan w$(0,..] --[check!]
# CH% = 1: '' // --[check!]--[where's hc%=1 ?]
# v% = 1: H% = VAL(TA$): '' // (for--next errchk [ex: <1])
#L40020:
# IF H% > 1 THEN CH% = 2: GOSUB SubHarmonic: '' // obs! [ch%]
# IF v% = 1 THEN O% = 1: GOSUB PreAspectCalc: '' // [o%:cf dummies:]
# v% = v% + 1: IF v% = 2 THEN H% = VAL(AT$): GOTO L40020
# GOSUB AspectCalc: CH% = 1: H% = VAL(t$): '' // --:check!][cf40012][53038][Boxes+]

#InFactorData2:
# LX% = 1: LZ% = 0
# LOCATE 16, 68: PRINT H$; " "; TA$; "^"; AT$;
# LOCATE 17, 68: PRINT c$; "..";
# GOSUB L39040
# GOSUB DiffStatus: '' // --[cf L53038][sub DiffStatus movto ca. Menu ?]
#
#L40040: '' // [g$='\']--[]
# FOR v% = 1 TO LT% - 1
# LZ% = LZ% + 1
# LOCATE 18 + v%, 68: PRINT K$(LX%); " ";
# IF OO% = 1 THEN LOCATE 15 + v% + 2, 69: w$ = w$(1, LZ%, LX%): GOSUB Asp: '[L42200]
# LOCATE 18 + v%, 70: PRINT K$(LZ%); " "; w$(HC%, LX%, LZ%); "x";
# IF LZ% = PP% THEN LX% = LX% + 1: LZ% = 0: IF LX% = PP% THEN LX% = 1
# NEXT v%::::stop::::
# LZ% = LZ% - (LT% - 2): IF LZ% < 0 THEN LZ% = LZ% + PP%: LX% = LX% - 1
# GOTO MenuInMenu: '' // --[obs!var, obs!goto]
#
#
#L40140: ' ' [g$='|']--[-OBSNOTE-]
# FOR v% = 1 TO LT% - 1
#  LZ% = LZ% + 1
#  LOCATE 15 + v% + 2, 68
#  PRINT K$(LX%); " "; w$(HC%, LX%, LZ%); " "; K$(LZ%); "  ";
#  IF LZ% = PP% THEN LX% = LX% + 1: LZ% = 0: IF LX% = PP% THEN LX% = 1
#  IF OO% = 1 THEN LOCATE 15 + v% + 2, 78: w$ = w$(1, LZ%, LX%): GOSUB Asp: '' // [L42200]
# NEXT v%
# LZ% = LZ% - (LT% - 2): IF LZ% < 0 THEN LZ% = LZ% + PP%: LX% = LX% - 1
# GOTO MenuInMenu
#
#
#L40500: ' <CR>[sub dublett?][cf L40000+/SubFactorData+][float?]
#:::: STOP ::::: FOR x = 1 TO PP%
# FOR z = 1 TO PP%
# w$(HC%, x, z) = w$(1, x, z): REM:tegning=1 or 0 [ch%]?
# NEXT z
# NEXT x
# RETURN

#L42000:
# IF a$ = "p" THEN STOP: '' // --[Menu]
# GOSUB Boxes: LOCATE 10, 68: PRINT "symbols"; : '' // [expand 's'!]
# IF OO% = 0 THEN LOCATE 10, 76: PRINT "ON ";
# IF OO% = 1 THEN LOCATE 10, 76: PRINT "OFF";
# LOCATE 11, 68: PRINT "maxorb:"; OA%;
# LOCATE 13, 70: GOSUB WaitLoop: '' // <[redun?]
# OO% = OO% + 1: IF OO% = 2 THEN OO% = 0
# GOTO Menu
#
#L42100: ' /// [g$='x'--> a$=g$--> g$='o']
# IF a$ = "p" THEN STOP: : : : : ' [Menu]:?:[cf1606]
# GOSUB Boxes: LOCATE 10, 68: PRINT ; "orbis";
# LOCATE 11, 68: PRINT "max-> "; : GOSUB TypeChoice: OA% = VAL(u$): '' // [ERRCHK!]
# GOTO Menu: '' // --[MenuInMenu?]
#
#L42150: '' // [g$='z'::input st% & max hp%]
#42160 GOTO Menu: '' // [return?] --UNFINISHED!
#
#
#
#L45000: '' // [x,z float?]
# GOSUB L53200: '' // [+whileblankout othermenuitems]-[?]
# IF dd% = 1 THEN GOSUB L20520: GOTO Menu: '<[tt$=?] <-[NO !]
# FOR z = 1 TO 5
# LOCATE z + 1, 68: PRINT m$(1, z); : '[blank '-' ): S/W)]
# x = VAL(m$(1, z)): LOCATE z + 1, 77
# IF z = 3 AND VAL(ds$) = 0 THEN PRINT "zt";
# IF z = 3 AND VAL(ds$) <> 0 THEN PRINT "dt";
# IF z = 3 OR z = 4 AND x = 0 THEN GOTO L45070: '>nextz
# IF z = 4 AND x > 0 THEN PRINT " n";
# IF z = 4 AND x < 0 THEN PRINT " s";
# IF z = 5 AND x > 0 THEN PRINT " e";
# IF z = 5 AND x < 0 THEN PRINT " w";
#L45070: NEXT z
# dd% = 0: GOTO L39030: '' // [i]<-(dd%=1)
#
#L45500: ' /// ****
# aa% = aa% + 1
# LOCATE 2, 67: PRINT "             ";"8";
# LOCATE 2, 68
# IF aa% = 1 THEN PRINT m$(1, 0); : '[(0,1)etc.?]
# IF aa% = 2 THEN PRINT f1$; : aa% = 0
#RETURN
#
#L46000: '--------
# u% = 2: '[x%=h%][ch%?]<<-<*
# z$ = "|:::::::::|:::::::::|:::::::::| "
# GOSUB Blank: b% = 0: O% = 2: 'grid loc [row,col]
# FOR z = 1 TO 12: LOCATE b% + z, O%: PRINT z$; s$(z): NEXT z
#FOR L% = 1 TO 12: '[blw! &^ <-(z,d float?)]
#il% = -1: FOR z = 1 TO 12
#IF RIGHT$(N$(CH%, L%), 3) = s$(z) THEN il% = z: z = 12
#NEXT z
#FOR D = 0 TO 29
#IF VAL(LEFT$(N$(CH%, L%), 2)) = D THEN D% = D: D = 29: '<[float?]
#IF VAL(MID$(N$(CH%, L%), 4, 2)) > 29 THEN D% = D% + 1
#NEXT D
#IF il% <> -1 THEN LOCATE il%, (D% + 1) + O%: PRINT K$(m); : '[;]?
#NEXT L%
#GOTO Menu

#L53000: ' *** pos* [trop/sid ?]*
# LOCATE 9, 68: PRINT "positions:";
# LOCATE 10, 68: PRINT "har "; : GOSUB TypeChoice: tt$ = u$: H% = VAL(tt$)
# IF H% < 1 OR H% > 300 THEN GOTO L53000
#
#PrintPosNewChart:
# GOSUB L53300: '' //<-[x50redun='N'?<-cf2210,6032][gotox27?]
# xx$ = tt$: '' // GOSUB WAITx:::::::  'blw!:[ch%/hc%:cf1633] <-[k%!] --[REVORDER Box-Wait ?]
# IF H% = 1 THEN CH% = 1: HC% = 1: GOTO L53029: '' // [h% i draw/pos?] <-[cf6050]!
# CH% = 0: GOSUB SubHarmonic: HC% = 0: '' // [hc% mov/chng/coll?]
#L53029:
# GOSUB L53030
# GOTO MenuInternAndExternGoto: '' // --[!] ### [LOOP AROUND Menu: not meta-sub, but 'goto' !!] ###

#L53030:
# LOCATE 16, 68: PRINT H$; " "; tt$; " :"; : '' // [er h% nullet[tt$]]?
# GOSUB DiffStatus: '' // --[cf40036]::LOCATE 17,67:PRINT E4$;:'[^movsubx70?]

#L53050: '' // [GOSUB 39040] '[mov?]<-[cf39162] <<-<*
# IF K% = 3 THEN K% = 1
# FOR v% = 1 TO LT%: LY% = LY% + 1: IF LY% > PP% THEN LY% = 1
# LOCATE 17 + v%, 68: ON K% GOSUB L53410, L53430
# IF LY% = PP% THEN LY% = 0
# NEXT v%
# LY% = LY% - (LT% - 1): IF LY% <= 0 THEN LY% = LY% + PP%
#RETURN

#L53200:
# FOR L% = 2 TO 6: '' // --[fm45020]
# LOCATE L%, 67: PRINT "             ";: '' // --[13 spc]
# NEXT L%
# LOCATE 8, 72: PRINT "   "; : '' // [if toggl e%=?]
#RETURN
#
#L53300: '[cfsub 20570,6000, (L7000 <-g$='N') !][cf Menu]
# FOR L% = 16 TO 24: LOCATE L%, 67: PRINT E6$; : NEXT L%: '' //[?]
# FOR L% = 70 TO 73 STEP 3: LOCATE 25, L%: PRINT " "; : NEXT L%
# LOCATE 25, 76
# IF a$ = "p" THEN PRINT "p"; : b$ = a$
# IF a$ = "x" THEN PRINT "x"; : b$ = a$
#RETURN: '[->20570+?]

#L53410:
#PRINT K$(LY%); " "; N$(HC%, LY%);
#RETURN
#
#L53430:
#PRINT K$(LY%); " ";
#PO$ = P$(HC%, LY%)
#print left$(PO$, 11);
#RETURN

#TypeChoice:
# u$ = ""
#LocLoop: in$ = INKEY$: IF in$ = "" THEN GOTO LocLoop: '' // Blw:[cf2100+/amap]
# IF in$ = CHR$(13) OR in$ = CHR$(27) OR LEN(u$) = 8 THEN GOTO RetThis
# IF ASC(in$) > 96 AND ASC(in$) < 123 THEN in$ = CHR$(ASC(in$) - 32): '' // [ERRCHK] & [HIGH HARMONIC !]
# IF u% = 1 THEN PRINT in$; : u$ = u$ + in$: '' // [u%=0 ?]
# GOTO LocLoop: '' // [where? <-u%= ][cfL1670]
#RetThis:
#if in$ = CHR$(27) then gosub WAITx: goto Menu: '' // [WAITX Redun or elsewhere]-[?]
#RETURN: '' // [cf'atie']

#WaitLoop:
# FOR L% = 1 TO 99999: NEXT L%
#RETURN

#axes:
# i$ = tf$: '' // <[best placement in prg ?] <--
# SELECT CASE m
#  CASE hp% + 2: '[ASC]
#   GOSUB TurnAngle
#   GOSUB DrawASC
#  CASE hp% + 1: '[MC]
#   GOSUB TurnAngle
#   IF tt$ = "i" THEN mcv$ = v$: '' // <[MC's pos vs. horizon (Desc <- 'ta0')] <-[cf. 'InMainDraw:'<(m=1=Sun) + cf. MO]
#   GOSUB DrawMC
# END SELECT
# i$ = tf$
# IF m = (hp% + 1) THEN GOTO RETimd: '' // <[if hp%+2 ?]<->[Asc/MC +1/+2 ?] <-(which 1st ?)
# DRAW "ta0"
# LOCATE 59, 51: PRINT "MC";: PSET (440, 465): CALL ArrowMC(i$, i%)
# LOCATE 60, 51: PRINT "ASC";: PSET (440, 475): CALL ArrowASC(i$, i%): '' // <['asc'; nocurs]^
# LOCATE 59, 59: '' // ['mc =    spaces]-[??]
# IF tf$ = "1" and CH% = 1 THEN PRINT " S";
# IF tf$ <> "1" THEN PRINT "Turned  ";
# if CH% <> 1 then print "HAR     ";
# LOCATE 60, 59: '' // ['asc =      ' ?] <-[backgrcolor problem !?]
# IF tf$ = "1" and CH% = 1 THEN PRINT " E";
# IF tf$ <> "1" THEN PRINT "Turned  ";
# if CH% <> 1 then print "HAR     ";: '' // [What if SU etc]. --[?]
#RETimd: RETURN: '>[InMainDraw & MinusLines]
#
#
#PlanetSymbols: ' /// 'planet's
# IF MI$ = CHR$(13) THEN GOTO L60050
# DRAW "br163": FOR L% = 1 TO 3: CIRCLE STEP(0, 0), L%: NEXT L%: '[br/blxx]?
# DRAW "bl49": CIRCLE STEP(0, 0), 3: '[48]?
# DRAW "br2": '<[br <-place 'planet' symb]!
# GOTO L60052
#L60050: : DRAW "br" + p1$: CIRCLE STEP(0, 0), 3
# DRAW "br56": FOR L% = 1 TO 3: CIRCLE STEP(0, 0), L%: NEXT L%: DRAW "bl56"
#L60052: DRAW "br" + O$: DRAW "ta0": DRAW "bu6 bl12"

# SELECT CASE m
# CASE 1
#  CALL SUN(tf$)
# CASE 2
#  GOSUB MO
#   IF tt$ = "i" THEN mv$ = v$: '' // <[MO's pos vs. horizon (Desc <- 'ta0')] <-[cf. 'InMainDraw:'<(m=1=Sun) + cf. 'Axes:(MC)]
# CASE 3
#  CALL ME
# CASE 4
#  CALL VE
# CASE 5
#  CALL MA
# CASE 6
#  CALL JU
# CASE 7
#  CALL SA
# CASE 8
#  CALL UR
# CASE 9
#  CALL NE
# CASE 10
#  CALL PL
# END SELECT
#RETURN: '>[InMainDraw] '[<=Select Case ??]

#DrawASC: ' /// '<[56/57 ??] [cf DawnDusk!] # ['ta0'=Desc !!]  ['right'<->'left' (on screen!)]  ['up'<->'down'] <-!!!

# IF VAL(sv$) > 180 THEN i% = 1: il% = 9: L% = 3:      '<-blw![check v$!]
# IF VAL(sv$) < 180 THEN i% = 9: il% = 1: L% = 11
# IF MI$ <> CHR$(13) THEN GOTO Middle

#Outer:
# DRAW "bl57 l110 l12": '<[where pre-pset'd ?][cf TurnAngle]<-[left/right mirrored!] <* [bl57/br57]<->[cf. PAINT 'DawnDusk']
# PSET (x%, y%): DRAW "br57 r110 r12 br41 r9": '' // [drawn axes inside main circle]
# CALL ArrowASC(i$, i%): '' // [cf. 'DrawMC:']
# PAINT STEP(0, 0), i%, 15: ' <-[use vars! <-pa%+dum] [turnangle'd ??]
# DRAW "bu20": '<[dum]<[cf. comments in 'ArrowASC:']
# PAINT STEP(0, 0), il%, 15
# PAINT (x%, y% - 10), L%, 15:  ' [,,defaultborder <(var) ?] <-[Tropos default] <[pset'd ?]
# z% = pa%
# GOSUB DawnDusk
# GOTO RETaxes

#Middle: '' // [UNFINISHED!]
# DRAW "bl57 l110": PSET (x%, y%): DRAW "br57 r110": '' // <[where pre-pset'd ?]
# CALL ArrowASC(i$, i%): PSET (x%, y%): '' // >pset? ::[i$=?? (tf$?)

#RETaxes: RETURN

#DawnDusk:
# IF tf$ <> "1" OR ln% = 1 THEN GOTO t: '' // --[make switch? - e.g. necessary only 1st time turned]
# GOTO RETdrawasc

#t:
# DRAW "ta180": '<['normal' Asc] <[pset'd ?]
# GOSUB HorizDiagonal
# PAINT (x%, y% - 4), i%, 15
# PAINT (x%, y% + 4), il%, 15

#IF ln% = 1 THEN GOTO IfLinesDrawn: '' // --[1st -> --??--label for MC]! <-temp!!: <-^[cf. SUB LEGENDprgSPECS]

# GOSUB HorizDiagonal: '' // --[horizon=ArrowASC / paint->pset?] ' <-^&blw![where go(es) the color(s) ??] <-['pset' yields default !]
# i$ = "0": CALL ArrowASC(i$, i%): '' // --[g$ ??] [+ draw 'br2'?]
# PSET (x%, y%): DRAW "ta0": '' // --[pset=c15 !??] --['ta0'<-not 180]!
# DRAW "ta" + mcv$
# GOSUB HorizDiagonal
# i$ = "0": CALL ArrowMC(i$, i%)

# CIRCLE (x%, y%), 6, 0: '' // --[radius=6 ?] --['fractal' Tropos]
# PAINT (x%, y% + 3), L%, 0
# GOSUB CenterSunMoon
# GOTO RETdrawasc

#IfLinesDrawn:
# PSET (x%, y%): DRAW "ta0": '' // --[pset=c15 !??] <-['ta0'<-not 180]!
# DRAW "ta" + mcv$
# GOSUB HorizDiagonal
# IF tf$ <> "1" THEN PSET (x%, y%): DRAW "c0": DRAW "bl3 l3": '' // --[Asc] ' --['pset' redun after 'paint' ??]
# IF tf$ <> "1" THEN PSET (x%, y%): DRAW "ta0": DRAW "ta" + mcv$: DRAW "br3 r3"
# CIRCLE (x%, y%), 2, L%
# PAINT (x%, y%), L%, L%
#RETplusasplines:
#RETURN

#RETdrawasc: RETURN:
#
#HorizDiagonal:
# PSET (x%, y%): '<[redun?] <-(cf. 'DrawAsc:[Outer:]' & 'DawnDusk:[t:]')
# IF ln% = 0 THEN DRAW "l56": PSET (x%, y%): DRAW "r57": '[pa%+1 (56+1) ?] <[use vars!]
# IF ln% = 1 THEN DRAW "l" + STR$(z%): PSET (x%, y%): DRAW "r" + STR$(z%): '[(z%+1) ?]
#RETURN: '>DawnDusk:[t:]
#
#CenterSunMoon:
# PSET (x%, y%): DRAW "ta0":
# DRAW "ta" + sv$: DRAW "br50"
# PSET STEP(0, 0), 0
# CIRCLE STEP(0, 0), 2, 0
# PAINT STEP(0, 1), 14, 0

# PSET (x%, y%): DRAW "ta0":
# DRAW "ta" + mv$: DRAW "br50"
# CIRCLE STEP(0, 0), 2, 0
# PAINT STEP(0, 1), 7, 0
#RETURN: '>DawnDusk:[t:]
#
#DrawMC: ' ///
# IF MI$ = CHR$(13) THEN GOTO L61160
# DRAW "bl57 l110": PSET (x%, y%): DRAW "br57 r110": GOTO L61190: ' >[110]?
#L61160:
# DRAW "bl57 l110 l12": PSET (x%, y%): DRAW "br57 r110 r12 br41 r9"
#L61190:
# CALL ArrowMC(i$, i%)
#RETURN: '>axes
