' #############################################################
'  Ref: https://cauldronofartandcraft.wordpress.com/chartdraw/ 
' #############################################################
'-------------------------------------------------------------
' aqTIE.BAS --[QBasic]---- Wed--May 18--2016---- 10:12--CEST--
'-------------------------------------------------------------
' UNDER_SCORE IN A LABEL GIVES ERROR IN QBasic!
'-------------------------
'' ON ERROR GOTO L63000
'-------------------------
CLEAR : '[,,stackspace?]
'[cls]

'[sp$]
sp$="TIE"

'[sw$]
'[sx$]
'[s%]
'[g$]

'[xloc%]
'[orig=6]
xloc% = 3

OPEN "switch.sw0" FOR INPUT AS #1: '' [.\]
 INPUT #1, sw$: '[Charts (base directory)]
 INPUT #1, sx$: '[Temp charts (Charts directory)]
 INPUT #1, s%
CLOSE #1

'[g$] --[init=g$='i']--[draw-- g$='N']
OPEN "choice.sw0" FOR INPUT AS #1: '' [.\]
 INPUT #1, g$
CLOSE #1

'' [LOCATE , , 0:] : ' '[loc,,0]
LOCATE 1, 1, 1, 0, 7: ' [no 'stray' cursor']

LOCATE 19, 9: '--[blinking cursor 'key']
  '' --[Basic:'WAIT' -?-]  --[default wait-time-loop & forced key-out ?]  --[for all '<key>'s ?]
  ' ' ' [in$ = INPUT$(1)]--[draft template]--[Not here now!]
CLS

'[in$]
'[L$]
'[fi$]
fp$ = ""
fq$ = ""
'[PR$]
'[u$]

 in$ = ""
 L$ = " ": '[cls?][key off?]
 fi$ = ""
 u$ = ""

 IF g$ <> "N" THEN GOTO yy
 LOCATE 1, 52: PRINT "           "
 LOCATE 2, 52: PRINT "           "
 LOCATE 3, 52: PRINT "           "

yy:
 IF g$ = "i" THEN s% = 1: LOCATE xloc%, 3: PRINT sp$; : '--[locate;]
 IF g$ = "N" THEN LOCATE xloc%, 3: PRINT sp$; : '--[locate;]
 :

'' [PH% = 18: ??] ' ---???? ##
'' [number of planets=8, Sun, Moon] [Node=11] --[np%>hp%?] --[cf2465] [=7= classic!] [Cf. Drawing]
'' --[dialog prompt!? (to be implemented)]

NP% = 10:       ' [=7= classical! (lag input-prompt)]--[=10?]--[(np% + 1) = Pluto !!]: '[err inp np% > hp%?] ---
hp% = np% + 1:  ' (12=incl. Node/ParsFort)
PP% = hp% + 2:  ' --incl. axes [L20400+/L60000+]
YS% = 2:        ' 3 house syst [incl. dim=0]
:
 bb% = 33
 DIM b$(bb%):      '[s$(0) ?]
'---
 :
 DIM N$(bb%):       ' [1,x](har,planet+axes)::(+ node/arab *!) [(x,0)=f%] #[N$(PP%)]#
 DIM RX$(bb%):      '[(PP%)]-[(hp%)]-[??]
 DIM H$(1, YS%, 3): '[mlmhus (har,syst,nr) :: + sek/tert/sol etc. ?]
 DIM KH$(3)
 :
 '' [0=cyc ?]
 DIM p$(bb%):     '[2,x[0:g$="p"][1:radix][2:g$="d"]*(changeorder?[L40000+]) #[p$(PP%)]# ''' ## g$ ##
 DIM m$(1, 5)
 DIM s$(12):      '[s$(0) ?]
'----------------------------------
 DIM k$(PP% + 1): '[=15 [k$(15)] ?]
'----------------------------------
 DIM z(1, PP%): '[?]
'-------------------

'--string inits--------
for m% = 1 to 12
 s$(m%) = ""
next m%
'----------------------
for m% = 1 to bb%
 b$(m%) = ""
next m%
'----------------------
for m% = 1 to bb%
RX$(m%) = " "
next m%
'----------------------

 KH$(0) = "x": m$(0, 0) = "'realname'    ": F0$ = "name          "
 KH$(1) = "y": m$(0, 1) = "0x.00.00      ": N0$ = "type          "
 KH$(2) = "z": m$(0, 2) = "Place X       "
 KH$(3) = "w": m$(0, 3) = "0x=00         ": 'time
:             : m$(0, 4) = "0x0-00 X      ": 'long
:             : m$(0, 5) = "0x0-00 Y      ": 'lat
:
: Z0$ = "zone"
: D0$ = "ds"
: h0$ = "height"

'---
'[Label]
'' New:
 ' ' LOCATE (xloc% + 2), 68: PRINT "[DATA] <CR>";
 ' ' LOCATE (xloc% + 3), 68: PRINT "[man]   <m>";
 ' ' LOCATE (xloc% + 4), 68: PRINT "[set]   <s>";
 :
 ' ' LOCATE (xloc% + 5), 74: ' ' // --[Blinking cursor awaiting input]

'[Label]
'' choose:
 ' ' in$ = INKEY$: '--[I$ ?][Esc!?]
 ' ' IF in$ = "m" THEN GOTO ManVals
 ' ' IF in$ = "s" THEN GOTO SetVals
 ' ' IF in$ <> CHR$(13) THEN GOTO choose
'---

 LOCATE (xloc% + 2), 68: PRINT "           ";
 LOCATE (xloc% + 3), 68: PRINT "           ";
 LOCATE (xloc% + 4), 68: PRINT "           ";

 GOTO dialog1
'---

'---
' ' ManVals: '---------------
 ' ' LOCATE 8, 68:  PRINT "Unfinished!";
 ' ' LOCATE 9, 68:  PRINT "See manual ";
 ' ' LOCATE 10, 68: PRINT "           ";
 ' ' FOR m% = 1 TO 10000: NEXT m%: '--['WAIT'?]
 '-----------------------                 
 ' ' GOTO New:


' ' SetVals: '---------------
 ' ' LOCATE 8, 68:  PRINT "Unfinished!";
 ' ' LOCATE 9, 68:  PRINT "See manual ";
 ' ' LOCATE 10, 68: PRINT "           ";
 ' ' FOR m% = 1 TO 10000: NEXT m%: '--['WAIT'?]     ' - [The thought here is to enable AUTOMATIC input of positions & data.]
 '------------------------                          '   [(run-time - set within 'A's program lines)                        ]
 ' ' GOTO New

'[Label]
dialog1:

'[Default]:
 ' ' // [Len(sp$)= then xloc% plus]
 if fi$ = "" then LOCATE (xloc%), 16: PRINT "[Temp]";
'---

:
 IF fi$ = "" THEN fi$ = sx$: ' ' ' [GOTO dialog2]--[Template--Not here now!]
 '                           ' ' ' [fi$ = sw$ + fi$ + "\"]
:'---
'[Default]
IF fp$ = "" THEN fp$ = "astro-1.txt"
:


locate ,,0
locate (xloc% + 16),1: print "x";
for m% = 2 to 11: locate (xloc% + m%), 3
print; "                                                                             ";: '[BlankLineLen=(80-3);]
next m%
locate (xloc% + 1),3: print "WAIT...";


'[Label]
L6000:
'#--
' ' ' ' ' '|---change order !?----------------------|' ' ' ' ' '
' ' ' ' ' '|F0$ = "name          "                  |' ' ' ' ' '
' ' ' ' ' '|N0$ = "type          "                  |' ' ' ' ' '
' ' ' ' ' '|:
' ' ' ' ' '| m$(0, 0) = "'realname'    "            |' ' ' ' ' '
' ' ' ' ' '| m$(0, 1) = "0x.00.00      ": ' date  |' ' ' ' ' '
' ' ' ' ' '| m$(0, 2) = "Place X       "            |' ' ' ' ' '
' ' ' ' ' '| m$(0, 3) = "0x=00         ": ' time  |' ' ' ' ' '
' ' ' ' ' '| m$(0, 4) = "0x0-00 X      ": ' long  |' ' ' ' ' '
' ' ' ' ' '| m$(0, 5) = "0x0-00 Y      ": ' lat   |' ' ' ' ' '
' ' ' ' ' '|:
' ' ' ' ' '| Z0$ = "zone"                           |' ' ' ' ' '
' ' ' ' ' '| D0$ = "ds": '[Daylight Saving"]        |' ' ' ' ' '
' ' ' ' ' '| h0$ = "height"                         |' ' ' ' ' '
' ' ' ' ' '|----------------------------------------|' ' ' ' ' '


' ' ###
' ' // [TEMP]--[SEE DEFs ABOVE]--[Edit]
m$(1, 0) = "RealName"
m$(1, 1) = "test1"
m$(1, 3) = "test2"
m$(1, 4) = "test3"
m$(1, 5) = "test4"
N1$ = "Type"
m$(1, 2) = "GeoPlace"
D1$ = "0"
' ' ###
' ' // TEMPORARY CODING: (write - input fm Charts)
F1$ = "Alias name": '[TEMP?]--[Edit]
' ' N1$
z1$ = "zone"
' ' // plus declare more vars here '' --edit--
' ' // ###


'########## # # # # # ###########
'[EDIT]: INPUT DIALOG - WHICH PRG
'########## # # # # # ###########

'-----------------------------
z$ = ""
OPEN fi$ + fp$ FOR INPUT AS #1
LINE INPUT #1, z$: ' ' ' ' ' z$ = right$(z$,37): ' ' ' ' if left$(z$,3) <> "-zi" then ERROR: ' ' ' 'EDIT edit ---OR---
' ' ' ' if left$(z$,3) <> "-YF" then ERROR: '' ### EDIT #####
if LEFT$(z$,14) = "Astrolog 5.43a" then PR$ = "astrolog543a": fq$ = "astro-2.txt"
: : : : if LEFT$(z$,14) = "Astrolog 542J" then PR$ = "astrolog542j07": fq$ = "astro-2.txt":  ' ' ' x2 - w-h-y-#####
: : : : if MID$(z$,9,13) = "Astrolog 542J" then PR$ = "astrolog542j07": fq$ = "astro-2.txt": ' ' ' ' ' ' ' ' ' ' '
if LEFT$(z$,3) = "Sun" then PR$ = "ZET9": fq$ = "astro-2.txt"
' ' if MID$(z$,9,xx) = then goto Astrowin365: '--[unfinished - temporarily disabled]
CLOSE #1
'-----------------------------

' ' // + Open fq
' ' // Edit - CHECK THAT Astro-1 and Astro-2 are interrelated (or dedicated Identity folder)



' # # # # # # # # #
''--else irregular
' # # # # # # # # #

'####################################
'[p$(no axes)]-[??]-[cf. aqDRAW]    '
'####################################



if PR$ = "astrolog543a" then goto astrolog
if PR$ = "astrolog542j07" then goto astrolog
if PR$ = "ZET9" then goto ZET9


'[Label]
ZET9:
 s$(1) = "Ari"
 s$(2) = "Tau"
 s$(3) = "Gem"
 s$(4) = "Cnc"
 s$(5) = "Leo"
 s$(6) = "Vir"
 s$(7) = "Lib"
 s$(8) = "Sco"
 s$(9) = "Sgr"
 s$(10) = "Cap"
 s$(11) = "Aqr"
 s$(12) = "Psc"
:
 b$(0) = "Earth  "
 b$(1) = "Sun    "
 b$(2) = "Moon   "
 b$(3) = "Mercury"
 b$(4) = "Venus  "
 b$(5) = "Mars   "
 b$(6) = "Jupiter"
 b$(7) = "Saturn "
 b$(8) = "Uranua "
 b$(9) = "Neptune"
 b$(10) = "Pluto "
:
 ' ' b$(11) = "Chi": ' --[fm 'astrolog']
 ' ' b$(12) = "Cer"
 ' ' b$(13) = "Pal"
 ' ' b$(14) = "Jun"
 ' ' b$(15) = "Ves"
 b$(11) = "Node"
 ' ' b$(17) = "Mea"
 ' ' b$(18) = "Lilith"
 ' ' b$(19) = "For"
 ' ' b$(20) = "Ver"
 ' ' b$(21) = "Eas"
:
 b$(22) = "I"
 b$(23) = "II"
 b$(24) = "III"
 b$(25) = "IV"
 b$(26) = "V"
 b$(27) = "VI"
 b$(28) = "VII"
 b$(29) = "VIII"
 b$(30) = "IX"
 b$(31) = "X"
 b$(32) = "XI"
 b$(33) = "XII"
:
 rh% = 100: '' // [random high number - lines in saved ZET9 sheets may vary]

' ' // --------------------------------------'
' ' // # p$(index) corresponds to b$(index) !
' ' // --------------------------------------'

' ' // [z% / z$ ?]--[cf Menu+]
OPEN fi$ + fp$ FOR INPUT AS #1
FOR z% = 1 TO rh%
z$ = ""
LINE INPUT #1, z$
for i% = 1 to bb%: ' ' // [hp%,pp%]-[?]
if left$(z$,7) = b$(i%) and mid$(z$,26,1) = "-" then RX$(i%) = "r"
if left$(z$,1) = b$(31) then x$ = mid$(z$,2,1): if x$ <> "I" and x$ <> "V" and x$ <> "X" then z$ = right$(z$,15): gosub calczet9: p$(hp% + 1) = z$: i% = bb%: '[involves tab]
if left$(z$,1) = b$(22) then x$ = mid$(z$,2,1): if x$ <> "I" and x$ <> "V" and x$ <> "X" then z$ = right$(z$,15): gosub calczet9: p$(hp% + 2) = z$: i% = bb%: '[    -"-     ]
next i%
' ' // [input #1, z$]
if EOF(1) then z% = rh%
' ' // [if z% < bb% then input #1, z$]
NEXT z%
a% = 0: ' ' // --[redun L16000 ?]
CLOSE #1
'=-=-=
OPEN fi$ + fq$ FOR INPUT AS #1
FOR z% = 1 TO rh%
z$ = ""
LINE INPUT #1, z$
for i% = 1 to bb%: ' ' // [hp%,pp%]-[?]
if left$(z$,4) = left$(b$(i%),4) then z$ = mid$(z$,19,9):  p$(i%) = z$: i% = bb%: ' ' // [ERRCHK-Sheet-saved-as-Decimal!]
' ' // [z% / z$ ?]--[cf Menu+]
' ' // [approx -- see sub]
next i%
' ' // [input #1, z$]
if EOF(1) then z% = rh%
' ' // [if z% < bb% then input #1, z$]
NEXT z%
a% = 0: ' ' // --[redun L16000 ?]--[a%]
CLOSE #1
goto L7000


'[Label]
Astrowin365:
 s$(1) = "ARI"
 s$(2) = "TAU"
 s$(3) = "GEM"
 s$(4) = "CAN"
 s$(5) = "LEO"
 s$(6) = "VIR"
 s$(7) = "LIB"
 s$(8) = "SCO"
 s$(9) = "SAG"
 s$(10) = "CPR"
 s$(11) = "AQU"
 s$(12) = "PIS"

OPEN fi$ + fp$ FOR INPUT AS #1
 '' '' '' '' INPUT #1, m$(1, 0)
 '' '' '' '' INPUT #1, m$(1, 2)
 '' '' '' '' INPUT #1, D1$: '--[ds]
 '' '' '' '' input#1,h1$: '--[height]
:
 z$ = "": LINE INPUT #1, z$
 z$ = "": LINE INPUT #1, z$: F1$ = z$
 z$ = "": LINE INPUT #1, z$: m$(1, 1) = MID$(z$, 3, 11)
 :      :              : Z1$ = MID$(z$, 18, 11): '--[zone]
 :      :              : m$(1, 3) = MID$(z$, 32, 11)
 :      :              : m$(1, 4) = MID$(z$, 47, 7)
 :      :              : m$(1, 5) = MID$(z$, 57, 5)
:
:
z$ = "": LINE INPUT #1, z$
z$ = "": LINE INPUT #1, z$
z$ = "": LINE INPUT #1, z$
z$ = "": LINE INPUT #1, z$
z$ = "": LINE INPUT #1, z$
:
FOR z% = 1 TO (NP% + 1)
 LINE INPUT #1, z$: z$ = MID$(z$, 12, 9)
 GOSUB calcastrowin: '[z% / z$ ?]--[cf Menu+]
 p$(z%) = z$: ''[approx -- see sub]
NEXT z%
a% = 0: '--[redun L16000 ?]

'' #########################
''  + Retrograd [R] !!!
'' #########################
:
z$ = "": LINE INPUT #1, z$
z$ = "": LINE INPUT #1, z$

'' ##################################
''  + Node, PF, Asteroids, etc. !! ??
'' ##################################
:
FOR z% = (hp% + 2) TO (hp% + 1) STEP -1: '--[mc --1, asc --2]
 LINE INPUT #1, z$: z$ = MID$(z$, 12, 9)
GOSUB calcastrowin: '[z% / z$ ?]--[cf Menu+]
p$(z%) = z$: : : : : ' ' a p p r o x -- see sub --!!
'' '' '' '' '' '' [PRINT #2, p$(z%)]
NEXT z%
a% = 0: '[redun L16000 ?]
:
'' #############
''  + Chiron !?
'' ############
:
CLOSE #1
goto L7000


'[Label]
astrolog:
'[astrolog543a & astrolog542j07]
'
'---r-e-d-u-n-mayhap--#
z$ = ""
OPEN fi$ + fq$ FOR INPUT AS #1
LINE INPUT #1, z$: '' z$ = right$(z$,37): ' ' ' ' if left$(z$,3) <> "-zi" then ERROR: ' ' ' 'edit--OR-
' ' ' ' if left$(z$,3) <> "-YF" then ERROR: '' ## EDIT ##
if LEFT$(z$,3) = "-zi" then z$ = "astrolog"
CLOSE #1

'##########################################################################
' THESE INPUT LINES WILL VARY ACCORDING TO 'astrolog.dat' AND the switches.
' (cf. 'astrolog' version) - (cf. sh/bat-scripts)
' These variables may be moved to and input#ed from a .dat-file
'##########################################################################
 s$(1) = "Ari"
 s$(2) = "Tau"
 s$(3) = "Gem"
 s$(4) = "Can"
 s$(5) = "Leo"
 s$(6) = "Vir"
 s$(7) = "Lib"
 s$(8) = "Sco"
 s$(9) = "Sag"
 s$(10) = "Cap"
 s$(11) = "Aqu"
 s$(12) = "Pis"

 b$(1) = "Sun"
 b$(2) = "Moo"
 b$(3) = "Mer"
 b$(4) = "Ven"
 b$(5) = "Mar"
 b$(6) = "Jup"
 b$(7) = "Sat"
 b$(8) = "Ura"
 b$(9) = "Nep"
 b$(10) = "Plu"

 b$(11) = "Chi"
 b$(12) = "Cer"
 b$(13) = "Pal"
 b$(14) = "Jun"
 b$(15) = "Ves"
 b$(16) = "Nod"
 b$(17) = "Mea"
 b$(18) = "Lil"
 b$(19) = "For"
 b$(20) = "Ver"
 b$(21) = "Eas"

 b$(22) = "Asc"
 b$(23) = "2nd"
 b$(24) = "3rd"
 b$(25) = "IC": '[543a-nul-see below]
 if PR$ = "astrolog542j07" then b$(25) = "I.C"
 b$(26) = "5th"
 b$(27) = "6th"
 b$(28) = "Des"
 b$(29) = "8th"
 b$(30) = "9th"
 b$(31) = "Mid"
 if PR$ = "astrolog542j07" then b$(31) = "M.C"
 b$(32) = "11t"
 b$(33) = "12t"

'------------------------------------------------------------------------'
 rh% = 100: ''[random high number - lines in 'astrolog' output may vary]
'------------------------------------------------------------------------'

' ' ' [z% / z$ ?]--[cf Menu+]
OPEN fi$ + fp$ FOR INPUT AS #1
FOR z% = 1 TO rh%
z$ = ""
INPUT #1, z$
for i% = 1 to bb%: '[hp%,pp%]-[?]
if left$(z$,3) = b$(i%) then if mid$(z$,20,3) = " R " then RX$(i%) = "r"
next i%
' ' ' input #1, z$
if EOF(1) then z% = rh%
' ' ' if z% < bb% then input #1, z$
NEXT z%
a% = 0: '--[redun L16000 ?]
CLOSE #1

''=-=-=

OPEN fi$ + fq$ FOR INPUT AS #1
FOR z% = 1 TO rh%
z$ = ""
INPUT #1, z$
for i% = 1 to bb%: '[hp%,pp%]-[?]
if mid$(z$,5,3) = b$(i%) then z$ = mid$(z$,10,19): gosub calcastrolog: p$(i%) = z$: i% = bb%
' ' ' [543a: WATCH OUT: 'IC'-line contains a nul-character (ICnul:)]
' ' ' [z% / z$ ?]--[cf Menu+]
' ' ' [approx -- see sub]
next i%
' ' ' input #1, z$
if EOF(1) then z% = rh%
' ' ' if z% < bb% then input #1, z$
NEXT z%
a% = 0: '--[redun L16000 ?]
CLOSE #1

'####################################
'p$(index) corresponds to b$(index) !
'####################################
p$(hp% + 1) = p$(31)
p$(hp% + 2) = p$(22)
'####################################
'[p$(no axes)]-[??]-[cf. aqDRAW]
goto L7000

'----------------
'[other imports?]
'----------------


'[Label]
L7000:
'------------------------------------
OPEN sx$ + "SWI.SWI" FOR OUTPUT AS #1
PRINT #1, PR$
CLOSE #1
'------------------------------------
'--[e.g. (AstroWin365) + (identity)]

'-------------------------------'
' goto open pdat.dat for output '
'-------------------------------'
'
' ' ' // [7010 : IF sp$ = "qATIE.BAS" THEN OPEN fi$ + "\pdat.dat" FOR OUTPUT AS #2]
OPEN sx$ + "PDAT.DAT" FOR OUTPUT AS #2
' ' ' // [7020 : IF sp$ = "B" THEN OPEN ms$ + "\pdat.tmp" FOR OUTPUT AS #2]
7200 WRITE #2, m$(1, 0)
7210 WRITE #2, F1$
7220 WRITE #2, N1$
7230 WRITE #2, m$(1, 2)
7240 WRITE #2, Z1$: REM:zone
7242 WRITE #2, D1$: REM:ds
7250 : : : ' write #2,h1$: ' '[height]
7270 WRITE #2, m$(1, 1)
7280 WRITE #2, m$(1, 3)
7290 WRITE #2, m$(1, 4)
7300 WRITE #2, m$(1, 5)
:
7350 FOR z% = 1 TO hp%
7360 PRINT #2, p$(z%)
7370 NEXT z%
7450 CLOSE #2

:
'[angles/axes] ///
OPEN sx$ + "ANGDAT.DAT" FOR OUTPUT AS #2
 FOR z% = (hp% + 1) TO (hp% + 2): '--[mc to asc !!]
 PRINT #2, p$(z%)
 NEXT z%
 a% = 0: '[redun L16000 ?]
CLOSE #2


'[ws$ ??]
OPEN sx$ + "IDENTITY.TIE" FOR OUTPUT AS #2: '' [.\]
PRINT #2, fi$: '--[if sp$=3=B <> X -- or always ?]--[^4 --amap]!
print #2, fp$
CLOSE #2


 IF g$ = "i" THEN s% = 2: g$ = "z": '--['z'] --[t e m p o r a r y !!]--[ws$ ??]--


 OPEN "switch.sw0" FOR OUTPUT AS #3: '' '--[.\]
 PRINT #3, sw$
 PRINT #3, sx$
 PRINT #3, s%
 CLOSE #3

'[ws$ ??]
OPEN "choice.sw0" FOR OUTPUT AS #1: '' '--[.\]
 PRINT #1, g$
CLOSE #1



if g$ = "N" then goto N
LOCATE (xloc% + 1), 3: PRINT "TIE-> DRAW (loading)";" - WAIT...";: GOTO xx:
N:
LOCATE 1, 52: PRINT "TIE        "
LOCATE 2, 52: PRINT "-> DRAW    "
LOCATE 3, 52: PRINT "(loading)  ": '[;]-[WAIT?]
xx:

CHAIN "aqDRAW.BAS": '' --[.\]
'---------------------
:
'[redunexit:]
GOTO Irregular
END



'[Label]
BackOut:
'--------------------------------------
'[exit to system]
''---[kill [c:] '.swi' etc. fm here ?]
''---[ (- eller syst: .bat-file ?    ]
'--------------------------------------
 PRINT :  ' [??]--[clear buffer in order to get back to DOS proper ?]
 ' CLEAR: ' [??] -[why don't we always get out into DOS/system, but just to QBasic (loaded prg)]-[??]
 SYSTEM
'=====
'--[BackOut]
'' ########



'' ===== ===== ===== ===== =====
 ' ' // --[::FOR M=10 TO PP%::]--

'[Label]
calczet9:
 :
 a% = VAL(LEFT$(z$, 2)): ' ' //: : :: // '' '' '' (N$(1,M),2)
 r$ = MID$(z$, 4, 2):    ' ' //: : :: // '' '' '' (N$(1,M),3,2): ''[,4,2]'' --[right$(z$, 2) ??]
 q$ = MID$(z$, 7, 2)
 s$ = RIGHT$(z$, 3):     ' ' //: : :: // '' '' '' (N$(1,M),3)

r = VAL(r$)
rz = r * 60
' ' // [r$ = STR$(r)] --[No!]
r = VAL(q$)
r = r + rz
:
z$=MID$(z$,9,3) 
rz = val(z$)
r = r + rz
:
r = (r / (60*60))
' ' // ::::stop:::
' ' // r = (r*60)/100
' ' // :::stop::

 ' ' // [z / z%]--[?]
 FOR z = 0 TO 11
  IF s$ = s$(z + 1) THEN a% = a% + (z * 30): z = 11
 NEXT z
:::if a% >  360 then stop::: ' ' // --[DEBUG]
loopz: if a% > 360 then a% = (a% - 360): goto loopz
:
 p = a% + r
 :
 ' ' // i$ = STR$(a%): i$ = MID$(i$, 2)
 i$ = STR$(p): i$ = MID$(i$, 2)
 IF a% < 100 THEN i$ = "0" + i$
 IF a% < 10 THEN i$ = "0" + i$
 z$ = i$
 :
RETURN: '--[zet9 input-file]

 ' ' // --[::NEXT M::]--
'' ===== ===== ===== ===

'[Label]
calcastrowin:
:
 a% = VAL(LEFT$(z$, 2)): ': : :: '' '' '' (N$(1,M),2))
 s$ = MID$(z$, 4, 3): ': : : : : '' '' '' (N$(1,M),3)
 r$ = MID$(z$, 8, 2): ': : : : : '' '' '' (N$(1,M),3,2): ''[,4,2]'' --[right$(z$, 2) ??]
 :
 r = VAL(r$)
 r = r / 60
 '' ''[r$ = STR$(r)]--[No!]
 :
 FOR z = 0 TO 11
  IF s$ = s$(z + 1) THEN a% = a% + (z * 30): z = 11
 NEXT z

 p = a% + r

 :
 '' '' i$ = STR$(a%): i$ = MID$(i$, 2)
 i$ = STR$(p): i$ = MID$(i$, 2)
 IF a% < 100 THEN i$ = "0" + i$
 IF a% < 10 THEN i$ = "0" + i$
 ' ' ' ' ' --[IF m = 1 THEN p$(hp% + 1) = i$ + "." + r$]: : : ''[(1,x) ??]--
 ' ' ' ' ' --[IF m = 4 THEN p$(hp% + 2) = i$ + "." + r$]--
 '' ''[z$ = i$ + "." + r$] --[No!]
 z$ = i$
 :
 ' ' ' ' ' --[::NEXT M::]--
RETURN: '--[astrowin input-file]
'' ===== ===== ===== ===== =====

'[Label]
calcastrolog:
:
 a% = VAL(LEFT$(z$, 2)): ': : :: '' '' '' (N$(1,M),2)
 s$ = MID$(z$, 4, 3):    ': : :: '' '' '' (N$(1,M),3)
 r$ = MID$(z$, 8, 2):    ': : :: '' '' '' (N$(1,M),3,2): ''[,4,2]'' --[right$(z$, 2) ??]
 :
 r = VAL(r$)
 r = r / 60
 '' ''[r$ = STR$(r)]--[No!]
 :
 FOR z = 0 TO 11
  IF s$ = s$(z + 1) THEN a% = a% + (z * 30): z = 11
 NEXT z
 p = a% + r
 :
 '' '' i$ = STR$(a%): i$ = MID$(i$, 2)
 i$ = STR$(p): i$ = MID$(i$, 2)
 IF a% < 100 THEN i$ = "0" + i$
 IF a% < 10 THEN i$ = "0" + i$
 ' ' ' ' ' --[IF m = 1 THEN p$(hp% + 1) = i$ + "." + r$]: : : ''[(1,x) ??]--
 ' ' ' ' ' --[IF m = 4 THEN p$(hp% + 2) = i$ + "." + r$]--
 '' ''[z$ = i$ + "." + r$] --[No!]
 z$ = i$
 :
 ' ' ' ' ' --[::NEXT M::]--
RETURN: '--[astrolog input-file]
'' ===== ===== ===== ===== =====


'[Label]
Irregular:
: : : : : locate xloc%+10,10: print "IRREGULAR": stop: '' --[t e m p o r a r y]
: '' ---loc!?---'cls'?---[autoexec.bat: 'break=off' !?]*
: LOCATE xloc%, 6: PRINT "[tie]  'A' is started with '<a> <CR>' in base directory!"
: LOCATE xloc%, 7: PRINT "<key>;"
: in$ = INPUT$(1)
: CLEAR
: SYSTEM
:
: '[-- astrap.bat -- a.bat (erase switches, etc.) -- end]

'------
L63000:
 ' on error* --loc!?---
 ': PRINT "nofile / pls insert...": : : ':[like in syst-bat?]
 ': ON ERROR GOTO 0: : : REM::'end' or --syst*?*
 ': : : : : : : : : : in$ = INPUT$(1): : CLEAR : SYSTEM
 ':
 '---
 'END 


'---'
' aqTIE.BAS
'---'