' ###############################################################
' # Ref: https://cauldronofartandcraft.wordpress.com/chartdraw/ #
' ###############################################################
'
' aqDRAW.BAS --- Tue--Jun 02--2015--20:56--CEST
' [QBasic]

DECLARE SUB SUN (tf$)
DECLARE SUB ArrowASC (i$, i%)
DECLARE SUB ArrowMC (i$, i%)

DECLARE SUB ari ()
DECLARE SUB tau ()
DECLARE SUB gem ()
DECLARE SUB can ()
DECLARE SUB leo ()
DECLARE SUB vir ()
DECLARE SUB lib ()
DECLARE SUB sco ()
DECLARE SUB sag ()
DECLARE SUB cap ()
DECLARE SUB aqu ()
DECLARE SUB psc ()

DECLARE SUB ME ()
DECLARE SUB VE ()
DECLARE SUB MA ()
DECLARE SUB JU ()
DECLARE SUB SA ()
DECLARE SUB UR ()
DECLARE SUB NE ()
DECLARE SUB PL ()

DECLARE SUB LineSpaces (xloc%, L$)

'---------------------->
CLEAR : '[,,stackspace?]
'[cls]
'[BEEP]-[?]

'[sp$]'[rpt]
sp$ = "DRAW"
'[xloc%]
xloc% = 6


'' // Use right-left high corner at circle for visuals/hints/alerts/signals etc. --[?}
locate 2, 58: print sp$;
locate 3, 58: print "INIT";

'[sw$]
'[sx$]
'[s%]
'[cg$]
'[f$]
'[ws$]
'[r$]
'' '' '-------------
ws$ = "z": '<[TEMP!]--[cf. 'identity.tie]
'' '' '-------------
'' '' [cf. Menu, g$='N', g$='A']
'' '' [ws$ = LEFT$(sw$, 1)]
'' '' '-------------

'[v]
v = 0

'[r]
'[rr]-[?]
rr = 0
r = 0

OPEN "switch.sw0" FOR INPUT AS #1: '' <[.\]
 INPUT #1, sw$: '[Charts (base directory)]
 INPUT #1, sx$: '[Temp charts (Charts directory)]
 INPUT #1, s%
CLOSE #1

if s% <= 0 then goto Irregular: '<[mayhap run error/clear] <-(redun?)---[<=, =< ?]---
' ' [if s% = 1 then goto Irregular:] '<[mayhap run error]' <-(redun? - never print#ed)


'[PR$]
OPEN sx$ + "SWI.SWI" FOR INPUT AS #1: '' <[.\]
INPUT #1, PR$
CLOSE #1
PR$ = PR$ + "        ": '' // --[Formatting]
'' // ERRCHK PR$ name (if Manual)
'' // + MaxLen PR$


OPEN sx$ + "IDENTITY.TIE" FOR INPUT AS #2: '' <[.\]
INPUT #2, f$: '' //  <-[ws$="z"] -> f$="":?:<>/redun?:[zx$?] [ry ?]
':::          '' //  ws$="p" -> f$=sw$<-<
CLOSE #2


OPEN "choice.sw0" FOR INPUT AS #1: '' // <[.\]
INPUT #1, cg$
CLOSE #1

if cg$ = "i" then goto Irregular: '<[mayhap run error]       <-(redun?)
if cg$ = ""  then goto Irregular: '<[mayhap run error/clear] <-(redun?)

if cg$ = "z" and s% <> 2 then goto Irregular
if cg$ = "N" and s% <> 3 then goto Irregular



SCREEN 12: '<[auto cls]
'' // PAINT (x%, y%), 7: '[flimmer!][=COLOR= background]?  <--<* ==??==
'' //     ' COLOR x2x: ' <==??==
'' // IS LARGER SIZED WIDTH/Window possble?
WIDTH 80, 60
'' // [L$]
LOCATE , , 0
'' // [cls?] <-(nocurs [,0]) [(,x,x) <-(size?)]


'' // [print 'Init']-[??]
locate 2, 58: print sp$;
locate 3, 58: print "INIT";
locate 4, 58: print cg$;: locate 4, 61: print mid$(str$(s%),2);:
locate 5, 58: print left$(PR$, 8);

'===>
' MAIN
'===>

IF cg$ <> "N" THEN GOTO YY

'' // WHAT IS --[?]:
LOCATE 1, 52: PRINT "   xx     a": '' // --[auto-cls ?]
LOCATE 2, 52: PRINT "   xx     a"
LOCATE 3, 52: PRINT "   xx     a"

YY:
 '' // --[IntroTxt/Logo ?!]--[cf1282,20166]
 '' // --[Far right Box-area as msg/confirm etc.]--[before&after INIT] --[?]
'--------------
'' // [WHY ?]:
'' // WHAT IS::::if cg$ = "z" THEN L$ = " ": CALL LineSpaces(xloc%, L$): LOCATE xloc%, 3: PRINT sp$;sp$: '<[locate;]


if cg$ = "N" then LOCATE xloc%, 3: print sp$;: '<[locate;]
'--------------

NP% =10:       '' // [number of planets=8, Sun, Moon] [Node=11] <[np%>hp%?] <[cf2465] [=7= classic!] [Cf. Drawing] <-[dialog prompt!? (to be implemented)]
hp% = NP% + 1: '' // [highest 'planet' no. (w/ Node)] <[+Arab?] <-[Cf. FactorData]]
PP% = hp% + 2: '' // [w/ axes (MC&ASC) [Cf. LT%] <[InMainDraw+/PlanetSymbols+]] <-[Cf. FactorData]]
YS% = 2:       '' // [3 Quadrant House Syst] <[incl. dim's 0-elem] <-[Equal Houses drawed by default]

DIM w$(1, PP%, PP%): '' // [w$(0,0,m)=transit[laan p$(0,m) <--> asp x,y][PreAspectCalc+]]
   '' // [dim w$(2,x,x)]!!
   '' // [x,0]? +transitlaan g$="t"::[cf40060 oo%=1->w$(1,..)!][div.0-dim!]

   '' // DIM RX$(HP%): '[pp%?] <-[TEMPredun!]
DIM H$(1, YS%, 3): '' // [Quadrant houses(har,syst,no.)?!][+ secondary/tertiary/sol/etc.]? <-[Equal Houses default!]
   '' // DIM KH$(3): '<-[redun?!][cf742/2860]

   '' // [0=cyc?]['advanced'?]
DIM N$(2, PP%): '' // (har,planet+axes):(+node/arab!)[(x,0)=f%!]
DIM P$(2, PP%): '' // [0:g$='p'][1:radix][2:g$='h'/a$='x'](chorder?[FactorData+])
:               '' // [p$(0,0)<-cf19600,InMainDraw,1632,2200]
DIM m$(1, 5): '' // [cf18620]
DIM s$(12): '' // [s$(0)]?
DIM K$(PP%)
   '' // DIM Z%(12): 'notz%?[cf.z()]?
   '' // DIM Z(1,PP%):'?[cfL20202]*[L15000+?]

' [chorder m$()]>!
s$(1) = "Ari": m$(0, 0) = "'realname'": F0$ = "navn      "
s$(2) = "Tau": m$(0, 1) = "0x.00.00  ": N0$ = "betegnelse"
s$(3) = "Gem": m$(0, 2) = "Sted X    ": REM:^[n1$=ind/mun/hor]
s$(4) = "Can": m$(0, 3) = "0x=00     ": REM:^[radix,...]
s$(5) = "Leo": m$(0, 4) = "0x0-00 X  ": REM<-long
s$(6) = "Vir": m$(0, 5) = "0x0-00 Y  ": REM<-lat
s$(7) = "Lib"
s$(8) = "Sco": 'kh$(0)='x'
s$(9) = "Sag": 'kh$(1)='y'
s$(10) = "Cap": 'kh$(2)='z'
s$(11) = "Aqu": 'kh$(3)='w'
s$(12) = "Psc": '^[=sy%!]*[seDIM L656]

K$(hp% + 2) = "A": '' // [chorder]!: '[toggle asc/graph)]?
K$(hp% + 1) = "C"
K$(1) = "S"
K$(2) = "L"
K$(3) = "H"
K$(4) = "V"
K$(5) = "M"
K$(6) = "J"
K$(7) = "D"
K$(8) = "U"
K$(9) = "N"
K$(10) = "P": '--[K$ ): hp%]--
K$(11) = "X"
'' // K$(12) = "Y"
'' // K$(0)? <(obs! free?)


H$ = "Har": '' // [+" "?]
c$ = "Cyc"

u% = 1: '' // [movdwn u% ?][fixvals->L700+!][ex:PI][cf. menu g$='*']

PI = 3.1415926535#: '' //  <-[exact-[?] <var# {/d} ?>]

'' // # gosub SizeConstants: goto ...
'' // <-[diverse such gosub-blocks for diverse chartdraw sizes & types!]<->[input-dialog above (early in prg)]
'' // [all prg comments mentioning 'Resizing' regards this!] <-[& some 'use vars!']

SizeConstants:
 x% = 245: x$ = STR$(x%): x$ = MID$(x$, 2):                      '[X%=235]
 y% = 240: y$ = STR$(y%): y$ = MID$(y$, 2): ' <-''''''''''''''-> '# [y$ redun here? - used L3600.. <-[see 'apel'] <<-<*
 p1% = 180: p1$ = STR$(p1% - 5): p1$ = MID$(p1$, 2)
 p2% = 221: p2$ = STR$(p2%): p2$ = MID$(p2$, 2)
 P3% = 226: P3$ = STR$(P3% + 12): P3$ = MID$(P3$, 2)
 PX% = P3% - p2%: PX$ = STR$(PX%): PX$ = MID$(PX$, 2):           '[px$:cf23400+!] <-<<*
 pa% = 56: pa$ = STR$(pa% - 20): pa$ = MID$(pa$, 2):             '[-14 ?] [pa% = circle 'DawnDusk:']
 Q% = INT(p1% - pa%): Q$ = STR$(Q%): Q$ = MID$(Q$, 2)
 Q% = INT((p2% - p1%) / 2): O$ = STR$(Q% + 5): O$ = MID$(O$, 2): '[Q$ ?]
 w% = 5: WW% = (360 / w%):                                       ' [step (grad. outer doubl-circ)]
 WA% = 30
 WB% = 15
 WC% = 5
'' // Memo: radius=168 <(dom/asp-blanking [,6=brown]) <-(use var!)'''<-<* '##[W%=5:<-[gradsep by conj/stellium]?]## <*
'' // # RETURN

tt$ = "i": '  '// [1]:init Menu+] [L53019]:[whynot t$='i'?(cf Boxes+)]
SU$ = "":  '' // --[init/clspart!<-cls introtxt?]:[=chr$(13)?] [cf. EH$:L7000,1646,6060!,20080,20024!]
PO$ = "":  '' // --[Transient Subst for P$(x.x) in 'PrintPos']-['tidy']
'-------
g$ = "h": ' <-[g$--obs!--]
a$ = "p"
'-------

b$ = "?": ' [b$:Boxes+,39044,53300+] <<-<
'[i$=""]-[?]
'[z$=""]-[?]
'[zz$=""]-[?]
'[f$=""]-[?]
za$ = ""
zf$ = ""
L$ = ""
qw$ = "": '<<-<*
in$ = ""
u$ = ""
'-------


'' // [OBS!]
'===========
GOSUB L1630
GOTO dummies
'===========


L1630:
 K% = 1: '' // <-[toggle n$()/p$()] [ch%=1/hc%=1 redun  h e r ][cf53000+]
 H% = 1
 TA$ = "1"
 mm% = 0: '' // <-[mm%->p$() <-cf g$='t',EH$,mi$]!
 AT$ = "1": '' // <-[ta$ nodv? (at$ a$="x" temp) [^cf2200]]
 cT$ = t$
 cf$ = tf$
 f% = 1: '' // <-[f% redun her?][Derived+]

L1640:
 CH% = 1
 HC% = 1
 t$ = "1"
 tf$ = "1": '' // <-[cf6060!]
 SU% = 0
 cc$ = "O"
 MI$ = CHR$(13): '' // <-[init!(&NEW<-redun?)]:[cf. SUorNot+,19864]
 EH$ = "": '' // <-[i]<-[=chr$(13)?][cf:su$:1282]:[cf2224!,20040+] [L7000]
RETURN

'----->
dummies: '' // [+ local loop/linecounts]> <-#( list unfinished!/incomplete!)
aa% = 0
BB% = 0
O% = 0:  '[dum multilocal!]
dd% = 1: '[toggle tec data(box)]:[=0?]
a% = 0
i% = 0
L% = 0
il% = 0
b% = 0
z% = 0: '<[obs! z%()^]
u% = 1: '[dummy][map types]['files'](local) [g$="*"]
v% = 1
'------>
'free':
'i%: '[Cf. Declare's]
'ii%
'l%
'il%
'z%
'm% / m --[?}-[OBS!]
'L%
'-----> ^[varlist structure unfinished !]][blw!]

'[switches]:
'-----
a% = 0: '' // ....
'-----
E = 0: '[sub Asp+][float?]
E% = 0: '<[obs! e % e%]?
ST% = 1: '' // [dummy/loopcounts[g$="x"](local)]
OO% = 0:
OA% = 8: '[aspsymbtoggle/maxorb] [L 42000+]
LY% = 0:
LT% = PP%: '' // [+ + w/ Arab] [lines(scrollmax/screen)]--[t%!?][lx%&lz%?]--[FactorData+,39003,53050+]

'' // [e,z,x,d,v] <-(FLOAT?/var%):?: M <-> M% *!!* -> [z-z%-z()] <-[^no!no! z% & z%()^] <- [use dummy z%]? <(if 'z' used)
'' // [FREE?]:[L%: <(cf. il%)]
'' // [v%,d]:x$[L1800+]?[os$<-opsyst?]
'' // [ro%] R%/K1% U1% K2% U2%/q1$ q2$
 '' // [OBS][!]--[POS 80] '|           | ' ##
'--------
'{xx$]
xx$ = ""
'--------

'' // ==code==(main)
'' // [i]
'' // sx$ <-[se label:In]
'' // [L2010]-[?]--[OBS!]
'' // [--g$='N' in Menu: loops back hereto]
'' //  sx$ = sp$: IF sp$ <> "\qAMAP.BAS" AND sp$ <> "pure" THEN sx$ = "X":
'' // [CLS?:else?:][1stmenu?] --# wrong!#

locate 3, 58: print "        ";
locate 5, 58: print "        ";
locate 2, 58: print sp$;
locate 3, 58: print cg$;: locate 3, 61: print mid$(str$(s%),2);: '' // ---[i]: ---s% [?] ==##
locate 4, 58: print left$(PR$, 8);
'---



'' // (Blw): [f$!?]-[no!]--[cf1632,19600,61050,60030]
'----------------------------------->
L2200: '' // O-B-S----!! ##  (w/ [A]
'----
 '' // [gosub L6000]--[why?]-(Ctrl-F '6000' - no find qAMAP ?!) --[gosub only if cg$ <> 'i']-[?!]
 '' // [Esc?]--(fm2202:g$='N' & [A])
'-----
IF cg$ = "N" THEN GOSUB L6010: IF SU$ = "y" THEN GOTO L2230
if cg$ <> "z" then goto L2210

locate (xloc% + 4), 3: print "ASC  / Aries";: '' // INIT - Blw =z  but not INIT -- FIXTHIS
locate (xloc% + 6), 3: print "<CR> / <y>";
locate (30 + PP%), 72: print "[i]";

gosub Boxes

 '' // [xx$ ?] <-redun 1st round ? [L2210]
L2210: ' [prg:L2210=L2230]
 LOCATE 13, 68: PRINT "[A] <y><CR>"; : '' // [A] --(even more varia!?)
L2222: EH$ = INKEY$: IF EH$ <> CHR$(13) AND EH$ <> "y" THEN GOTO L2222
 IF EH$ = "y" THEN EH$ = "A" ELSE EH$ = " ": '[cf1646]
 LOCATE (34 + PP%), 72: PRINT "[" + EH$ + "]"; : '' // --cfMenuInternAndExternGoto] [L7000]

' ' ###
L2230:
 '' // [LOCATE ,,0 =?= (L2112)]
 xx$ = "[disk]   ": GOSUB WAITx
 GOSUB Boxes
 if cg$ = "z" then locate xloc%, 3: print "           ";: '' // [??} ##
 '' // INIT - Blw =z  but not INIT -- FIXTHIS----##
' ' ###

'[jump]
GOTO in: '-->
'[subs-->]


'' // [if g$='N' in Menu]----
L7000: '//
 LOCATE (32 + PP%), 74: PRINT "N";
 LOCATE (34 + PP%), 74: PRINT EH$;
 :
 IF EH$ = "A" THEN LOCATE 9, 65: PRINT "A!"; : '<-['warning' for the next map!][BEEP?]
 :
 xx$ = "[NEW]    ": GOSUB WAITx: ::::::
RETURN
'-----


'---
L6010:
 il% = 1
 GOSUB L6020
 GOTO L6050: '' // -[cf20032]---[Whatis]-[?]
:
L6020:
 FOR L% = 5 TO 15 STEP 5
 CIRCLE (x%, y%), L%, il%: '--[cf20032]
 NEXT L%
RETURN
'---

L6050: :::stop:::'' // [Whatis]-[?]
' <-[obs!:g$='h'->subx10!]
 '' OPEN f$ + "SWI.SWI" FOR INPUT AS #1: ' <-[cf2200+][+Blw!] <--[f$='identity.tie']---
 '' INPUT #1, sw$
 '' +++
 '' CLOSE #1
 '' ws$ = LEFT$(sw$, 1)
 '' IF ws$ = "p" AND sp$ = "pure" THEN ws$ = "z"
 :
 :
 IF SU$ = CHR$(13) THEN GOSUB L1640: ' [h%=1][t$:20054][tt$:Menu+] <-[cf53025+!]
 : : : : : : ' [gosub 53300?<-cf53025] <<-<*
RETURN: ' [->2200]
'---

L6500: IF SU% = 3 THEN GOTO L6540: ' <ret
 IF SU% = 1 THEN L% = 0: LOCATE 2, 57: PRINT cc$; : REM:<-[simplify!]*
 IF SU% = 2 THEN L% = 21: LOCATE 24, 57: PRINT cc$;
 LOCATE L% + 2, (67 - LEN(f1$)): PRINT f1$;
 LOCATE L% + 3, (67 - LEN(N1$)): PRINT N1$;
 IF SU% = 2 THEN L% = L% - 6
 LOCATE L% + 5, (66 - LEN(cT$)): PRINT cT$;
 LOCATE L% + 6, (66 - LEN(tf$)): PRINT cf$;
L6540:
RETURN:  ' [->20081]
'-----

'[<--subs]
'[<--jump to in]


'##in##=>
'[Label]
in:
OPEN f$ + "pdat.dat" FOR INPUT AS #1: '[ws$='z' ?]
 INPUT #1, m$(1, 0)
 INPUT #1, f1$
 INPUT #1, N1$
 INPUT #1, m$(1, 2)
 IF ws$ = "p" OR ws$ = "z" THEN GOTO L2330: '[chorderin'atie.bas'! [<>'a' ?]]
L2310:
 INPUT #1, m$(1, 1)
 INPUT #1, m$(1, 3)
 IF ws$ = "p" OR ws$ = "z" THEN GOTO L2340
L2330:
 INPUT #1, TZ$: '[zone]
 INPUT #1, ds$: '[dt]
 IF ws$ = "p" OR ws$ = "z" THEN GOTO L2310
L2340:
 INPUT #1, m$(1, 4): '[long!]
 INPUT #1, m$(1, 5): '[lat]
 IF ws$ = "a" THEN INPUT #1, z$: '[height]['a' <-obs!]
 :
 FOR m% = 1 TO hp%: '--[m/m% ?]
  INPUT #1, P$(1, m%)
  '' // IF ws$ = "a" THEN INPUT #1, N$(1, m%): '[=i$+right$(z$,3)+s$ (InTrunc+)]['a' <-obs!] '' '' ''
  '' // IF ws$ = "p" OR ws$ = "z" THEN z$ = P$(1, m%): GOSUB TruncateRounding: N$(1, m%) = z$ '' '' ''
  '' // --(Value check P$() is/was done in TIE! [= 0 etc.])-[?]. (Formatting is repeated here, or use WRITE# in TIE instead of PRINT#)
  z$ = P$(1, m%)
  v= val(z$)
  if int(v) < 100 then z$ = " " + z$: '' // ['0']-[?]
  if int(v) < 10  then z$ = " " + z$
  P$(1, m%) = z$ + "   ": '' // [FORMATTING]--[Why +3 spc ? (--Debug !?)]--[Cf. 'SubHarmonic:'] --[Temp!?][no delay/sub53300  [<+> <=>!]
  GOSUB TruncateRounding: '--[z$]
  N$(1, m%) = z$
   '' // [<>'a']:?:[TruncateRounding<->'Trunc'/'Rounding'!]
   '' // INPUT#1,Z$: '[ecl lat(L2000+)]
 NEXT m%
  '' // [ecl lat pluto?]--[?]
CLOSE #1
'---


'' // [What if other than ZET9]-[?]:
OPEN f$ + "ANGDAT.DAT" FOR INPUT AS #3
  '' // FOR l%=10 TO HP%:[pluto+node+ParsFort]
  '' // (cyc,syst,husnr)[cyc=0=radix]:[=0?]
 SY% = 1: '' // sy%=hussyst (var<-amicras?)[0=Equa][1=Plac][2=Koch]
 FOR m = 1 TO 2: '--[m% ?]
  z$ = "": '' // --[redun]-[?]
  INPUT #3, z$
  P$(1, hp% + m) = z$
  GOSUB TruncateRounding
  N$(1, hp% + m) = z$
  P$(1, hp% + m) = P$(1, hp% + m) + "   ":  '' // [FORMATTING]--[Why +3 spc ?]--[Cf. 'SubHarmonic:'] --[Temp!?][no delay/sub53300  [<+> <=>!]
 NEXT m
CLOSE #3

'-##^##----
a% = 0
GOTO CHART
'[a%]-[!]
'-##^##----

'' // =-------------------------------------=
'' // L9000:  ' errchk [<-MEMO-OLD: reserved]
'' // =-------------------------------------=

'' // [m/m%]-[?]-->

PreAspectCalc:
'' // [cfL620-22]
 FOR m = 1 TO PP%
  w$(0, 0, m) = P$(CH%, m): '' // [Temp Borrow! =NOT= w$! <-> [Change this]-[!!]-[?] ## [ch%=?] ##
 NEXT m: '' // [cf662]
RETURN

AspectCalc:
  FOR m = 1 TO hp%
    K1% = VAL(LEFT$(w$(0, 0, m), 3))
    U1% = VAL(RIGHT$(w$(0, 0, m), 2))
    FOR y = 1 TO hp%
      :
      K2% = VAL(LEFT$(P$(CH%, y), 3)): '' // <[h%>12 --[?]
      U2% = VAL(RIGHT$(P$(CH%, y), 2))
      :
      IF U2% > U1% THEN K1% = K1% - 1: U1% = U1% + 60
      IF K2% > K1% THEN K1% = K1% + 360
      i% = K1% - K2%
      IF i% > 180 THEN r% = ABS(60 - r%): i% = ABS(360 - (i% + 1))
        '' // I% = ABS(I%-360) <<-?
        '' // (c% obs!)* (*i%) <<-?
      Q1$ = STR$(i%)
      Q1$ = MID$(Q1$, 2)
      IF i% < 100 THEN Q1$ = "0" + Q1$
      IF i% < 10 THEN Q1$ = "0" + Q1$
      Q2$ = STR$(r%)
      Q2$ = MID$(Q2$, 2)
      IF r% < 10 THEN Q2$ = "0" + Q2$
      w$(HC%, m, y) = Q1$ + "-" + Q2$
    NEXT y
  NEXT m
RETURN


'[Label]
HARMONIC:
'' // [g$="h"]
GOSUB Waitx: '' // [xx$]-[?]-[rpt]
GOSUB Boxes
 cT$ = t$
 cf$ = tf$: '' // [tf$ here]-[?] [cf19311]
 LOCATE 9, 68: PRINT H$; "-> <ESC>";
 locate 11, 68: GOSUB TypeChoice
 if u$ = CHR$(27) then gosub WAITx: goto Menu: '' // [WAITX Redun or elsewhere]-[?]
 t$ = u$: IF VAL(u$) < 1 OR VAL(u$) > 300 THEN GOTO HARMONIC: '' // --[ErrChk!]
 GOSUB SUorNot
 if SU$ = CHR$(27) then gosub WAITx: goto HARMONIC: '' // [WAITX Redun or elsewhere]-[?]
 if MI$ = CHR$(27) then gosub WAITx: goto HARMONIC: '' // [WAITX Redun or elsewhere]-[?]
 :
 H% = VAL(t$)
 HC% = 1: '' // [movL19140-42->19100+?]? --[hc%:cf18884/w$()]
 '' // ErrChk? [Blank/BlankMain+=subfm2150+,2190,WAITx,39270,46030]--
 xx$ = "[CalcHar]": GOSUB WAITx: '' // [rpt]
 GOSUB Boxes
 IF H% = 1 THEN CH% = 1: GOTO CHART: '' // [cf. whatL16000 ?] [fm19160!] <-[mangler 'RETURN' ??]
 CH% = 2: GOSUB SubHarmonic: GOTO CHART: '' // v%=1 ?: ch%=0 ?[dim]
'[Goto Chart ##]
'' // [errchk:ifleft$='0'thenerr?]

'[Label]
SubHarmonic:
 '' // [Cf. 'in']--[m/m% ?]
 '' // [ Harmonics > 1 ]--(i.e. not Radix) - ['Negative' harmonics (< 1) is not considered here]
 FOR m% = 1 TO PP%
  rr = val(p$(1, m%))
  '' // :: [WHAT IF pos=00.]-[?]-[!]
  :: if rr = 0 then rr = rr + 360: '' // --[Correct or Redun]-[?]-##
  rr = rr * H%
  Loopx: if rr >= 360 then rr = (rr - 360)
  if rr >= 360 then goto Loopx
  z$ = STR$(rr): z$ = MID$(z$, 2): : '' // <--[cf. 'TIE' & DRAW:'in']
  IF INT(rr) < 100 THEN z$ = " " + z$: '' // ["0" + z$]-[?]
  IF INT(rr) < 10 THEN z$ = " " + z$
  P$(CH%, m%) = z$ + "   ": '' // [FORMATTING]--[Why +3 spc ? (--Debug !?)] --[Cf. 'in:'] --[Cf. 'SubHarmonic:'] --[Temp!?][no delay/sub53300  [<+> <=>!]
  GOSUB TruncateRounding: '#(z$ only!)#
  N$(CH%, m%) = z$
   '' // [<>'a']:?:[TruncateRounding<->'Trunc'/'Rounding'!]
   '' // INPUT#1,Z$: '[ecl lat(L2000+)]
 NEXT m%
RETURN


'[Label]
DERIVED:
 '' // derived houses <-g$='t' /// <-[other deriv/cycles/sub\divisions ?] ['Indian'?] [h%>1]?
 '' // [ERR in box: har > 1  <-cyc no.] <-[M]-[?]
 '' // n$(0,0),n$(1,0) <-both free*!? [and p$()]::^^^(t$)^
 '' // n$(h%,f%)=f%-asc [if ft$=1 then f%=1 else f%=0]  [ft$ ??]
 GOSUB L19600: '' // (--EH$!--) ! --[cf20212,InMainDraw]
InDer:
 '' // --[+subWAITx ?]
 GOSUB Boxes:
 cf$ = tf$: cT$ = t$:  '' // --(movup pre InDer?) '<[t$ h e r ?] [cf19030]
 LOCATE 9, 68: PRINT "{Cyc}"; :  '  ' // <[c$ ?] [8,68 ?] ['..']-[?]
 LOCATE 11, 68: print "> ";: GOSUB TypeChoice: '' // --[DIV. 'strange' ERRCHK !!]
 tf$ = u$: IF VAL(u$) < 1 OR VAL(u$) > 12 THEN GOTO InDer
 GOSUB SUorNot: '' // --[S][mi$]
 f% = VAL(tf$)
 xx$ = "[CalcCyc]": GOSUB WAITx: '' // [xx$ =.. +tf$]?
 '' // ##' ' GOSUB BlankMain: '' // Goto ??   [or Sub 'Blank' ?] --[clsparts] --[immy after inputCR]-[!]
 xx$ = "CYC      ": GOSUB Boxes
 FF% = (f% - 1) * 30:                           '' // [cf. other prg inputs]
 FF% = VAL(P$(mm%, hp% + 2)) + FF%: IF FF% > 360 THEN FF% = FF% - 360: '' // # [t$='0' ?!]
 FP$ = STR$(FF%): FP$ = MID$(FP$, 2)
 P$(mm%, hp% + 2) = FP$: '' // [obs!]
 IF SU$ = "y" THEN GOSUB Coordinates
GOTO CHART: '' // [19260 ?]
'' // --[RETURN/Meta-goto]-[?]


'[Label]
L19600:
 '' // EH$:[East=0Aries]  [and/or g$='t' (mi$?)] <-[cf1632,2200]
 IF t$ = "1" THEN mm% = 1: '' // --[cfInMainDraw+]
 IF t$ > "1" THEN mm% = CH%
 : : P$(0, 0) = P$(mm%, hp% + 2): '' // [-- InMainDraw+]--[harm:h% gets > ch% !]
 IF EH$ = "A" THEN P$(mm%, hp% + 2) = "000.00": '' // --[EH$:cf20040+,InMainDraw,1632,2200]
RETURN


'[Label]
SUorNot:
 MI$ = CHR$(13)
 LOCATE 13, 68, 1: PRINT "[S] <y><CR>"; : '' // [,1?]
L19812: SU$ = INKEY$: IF SU$ <> "y" AND SU$ <> CHR$(13) and SU$ <> CHR$(27) THEN GOTO L19812
 IF SU$ = "y" THEN GOSUB InSuorNot: '' // [cf20080+]
 '' // if SU$ = CHR$(27) then gosub WAITx: gosub TypeChoice: '' // [WAITX Redun or elsewhere]-[?]
RETURN: '' // [mi$:<>NEW:cf1640+]
'' // EDIT--[Diff Colored planet glyphs if SU !!]
:
InSuorNot:
 : : LOCATE 13, 68, 1: PRINT "[M] <y><CR>"; : '' // [,1?]
L19862: MI$ = INKEY$: IF MI$ <> "y" AND MI$ <> CHR$(13) and MI$ <> CHR$(27) THEN GOTO L19862
 IF MI$ <> "y" THEN GOTO RETInSuorNot
 '' // if in$ = CHR$(27) then gosub WAITx: goto Menu: '' // [WAITX Redun or elsewhere]-[?]
 : GOSUB TempCirc: CIRCLE (x%, y%), 120: CIRCLE (x%, y%), pa%, 0: '' // [rad?][x10!]
 : CIRCLE (x%, y%), 108: CIRCLE (x%, y%), pa% - 20
 '' // [??: if sp$ <> "\qAMAP.BAS" then goto L2210: '[pure!]<<-< [watchRET!]
RETInSuorNot:
RETURN


'#======#
'[Label]
CHART:
'#======#
 ln% = 0: '<[toggle Asp Lines]
 ::: '' // GOSUB Boxes
 ::: '' // IF SU$="y" THEN goto L20050: ' [EH$ ?]<-[cf19620][mi$=]:::
 m% = 0
 '' // if g$ = "t" or g$ = "h" then m% = 1: '' // [REDUN]-[?]
 LOCATE m% + 9, 68: PRINT "Har-> "; t$;
 LOCATE m% + 10, 68: PRINT "Cyc-> "; tf$; : ' [f%?]
 LOCATE m% + 12, 68: PRINT "Draw: <ESC>";
 LOCATE m% + 13, 68: PRINT "<1> <2> <3>";
 :
 locate (31 + PP%),72:
 IF tt$ = "i" THEN PRINT "[i]"; : GOTO L20020: ' [cfL1636] ' second [i]
 IF MI$ = "y" THEN PRINT "[M]"; : GOTO L20020
 IF SU$ = "y" THEN PRINT "[S]";
 IF SU$ <> "y" THEN PRINT "[ ]"; : '' // [=chr$(13)?]--[cf1282]
 '' // [variations]-[!?]

L20020:
if tt$ <> "i" then goto L20030
xx$ = "": gosub STATUSx: '' // --Firstrun only -[?] -- [xx%="" -[?]
locate (xloc% + 4), 3: print "Choose Chart variant";
locate (xloc% + 6), 3: print "<1> <2> <3>";
locate (32 + PP%), 72: print "[i]";: '' // --REDUN-[?]-[Cf. above] ' third [i]

L20030:
 KK$ = INKEY$: '' // input$()? [blw!:in$=""/i%:cf2170+]
 ::: if kk$ = CHR$(27) then gosub WAITx: goto Menu: '' // DEBUGTEMP =#-#-#=
 '' // IF KK$ = CHR$(27) AND tt$ = "i" THEN in$ = "": i% = 0: GOTO L2130: ' [?][i%?]
 '' // IF KK$ = CHR$(27) THEN il% = 0: GOSUB L6020: GOTO Menu: ' ^[in$:cf3550,3732]
 '' // [cf6000!] <-[su$=,EH$=??]
 IF KK$ <> "1" AND KK$ <> "2" AND KK$ <> "3" THEN GOTO L20030

'' // [OBS! xx$]--
xx$ = "[" + KK$  + "]": GOSUB WAITx: '' // --[rpt in ChartDraw]-[!?]

'---
'' // ## vague:UNFINISHED--[!]
'' // if tt$ <> "i" then GOSUB Boxes: '' //--[REDUN]-[i]-[?]-##
'' // if tt$ <> "i" and g$ <> "t" then goto L20050: '' // [i]-[?]--[if cg$ <> "z"...]-[?]
'---

'' // ##
if g$ <> "t" then goto L20050
for m% = 18 to PP%
 locate m%, 67:
 print "             ";
next m%

L20050:
 : IF SU$ = CHR$(13) THEN GOSUB Blank: '' // [=""]?<-[cf mi$][BlankMain?][cf1282]
 : IF SU$ = "y" THEN SU% = SU% + 1: GOSUB L6500: '' // [20080else?][coll 20087?(x88)][cf2200]
 : '' // [subBlank/BlankMain? redun?]<<-<*
 GOSUB PreAspectCalc
 GOSUB AspectCalc: '' // [asp[(t$)switch=<>5drawing?)]-[?]
 '' // [mov?]^
 IF EH$ = "A" THEN GOSUB L19600: '' // [cf19307]!
 IF SU$ = "y" AND g$ <> "t" THEN GOSUB InMainDraw: GOTO Menu: '' // +[g$='N']/[Mi$='y']..!?:::[sub AspLines her?]-[ No?!!]
 : '' // [swap EH$/su$ ?]^^
'^-----


ChartDraw: '///
 IF tt$ <> "i" THEN GOTO L20180: '' // [Cf. L20020]
 locate (xloc% + 4), 3: print "                    ";
 locate (xloc% + 6), 3: print "                    ";
 GOSUB WAITx:  '' // [xx$ ?] --{rpt fm L20050 ?] [20162<->64 ?]::[cf2000+,20006]--[REDUN ?]
 '' // GOSUB Boxes
'' // ['input VAR' i scr2 ?][notmovupSCR2<-introtxt in SCREEN 0!?]
 
L20180: '' // [default color=15]
 PSET (x%, y%)
 CIRCLE (x%, y%), p2%
 CIRCLE (x%, y%), p1%
 PAINT (x%, y% + (p1% + ((p2% - p1%) / 2))), 11, 15: '<-[define/assign vars!]->
 CIRCLE (x%, y%), P3%:                               '^^[diff color diff house system !??]<->[day/night houses?]
 CIRCLE (x%, y%), pa%:                               '<-[Bordering Earth's horizon (Cyc=1)]
 CIRCLE (x%, y%), P3% + 12, 3:                       '<-[define/assign color vars!]->
 CIRCLE (x%, y%), 267, 3:                            '    -'-

  '' // #  '[Z=Z(1,1):?:[cf688]]
  '' // #  '[ifnoASC=data("xxx"):<noaxes> ?]

  '' // [Definer v/ inputdialog har=Harmonics / cyc=Turned Houses] !!! <*

LOCATE 1, 1: PRINT "Tropical Zodiac"; : '' // <[loc ,0 <-nocurs!?]
LOCATE 2, 1: PRINT "Equal Houses";
LOCATE 3, 1: PRINT "Quadrants";

LOCATE 58, 1:
IF tf$ = "1" THEN PRINT "2-D Radix";
IF tf$ <> "1" THEN PRINT "2-D Turned";: '' // [OBS!]--[Harmonic]--[!] ##
LOCATE 59, 1:
IF tf$ = "1" THEN PRINT "Horizon view";
IF tf$ <> "1" THEN PRINT "Derived houses";
LOCATE 60, 1:
IF tf$ = "1" THEN PRINT "Origo: Tropos"; : '' //      <-^^[g$='r'(adix) !??]
IF tf$ <> "1" THEN PRINT "Radix Quadrants";  '' //      <-  [Center: Xxxxxx](r.[ ]Quadrants)
'' // : : : '>-<why not err mising colon above ?? ^^^>-<
:
'' // :: if EP ! :: [etc.]
:
GOSUB Coordinates
GOSUB MainDraw: '' // --[yz redun: ?][cf20261,20274,20288,]
gosub STATUSx
GOTO Menu: '' // ['ChartDraw:' mangler 'RETURN' !?] <-[cf L2150, L2170, L39240] <* <* <* ==??== <* obs! === ### === OBS-RETURN-ERR--[??] ##

'' // [Debug-Search-Here--gosub maindraw]
'##
'' // <-[mov20570?<->cfg$='h']
'' // [delay!]
'' // HERE=END CHART/ChartDraw <-[is 'ChartDraw:' RETURNed ??] <###
'##



Coordinates:
 '' // [Coord relative to QBasic's intrinsic coordinates]<->['ta0' yields DESC (Cyc 1!)]
 YY = 360 - VAL(P$(CH%, hp% + 2)):
 YZ = YY + 180: IF YZ > 360 THEN YZ = YZ - 360: '' // (asc)
 ZY = 180 - YY: IF ZY < 0 THEN ZY = ZY + 360
RETURN

: '' // # GOTO 20260:?:(see gwAmap) <-[no(equal)housepartit]:?:[blw!:float!'s] ##

'[Label]
MainDraw:
  '' // --['c15'=default]-- 
  FOR x = 0 TO 360 STEP 30: '' // [float! obs!x/x%] <-(use vars!)]
    PSET (x%, y%)
    u$ = STR$(x): u$ = MID$(u$, 2)
        '' //# ZZ=VAL(P$(H%,1))
        '' //# FOR K=1 TO (360/WA%): '' // [1=asc]!
        '' //# ZZ%=INT(ZZ):U$=STR$(ZZ%):U$=MID$(U$,2)
        '' //# PSET(X%,Y%): '[el. circle 0]? [draw "bm240,100"]["x"+var$]
    '' // DRAW "TA" + u$: DRAW "br180 c3 r41": '["BR44 R12"][use vars!] <-[check! <(alternative)]
    DRAW "TA" + u$: DRAW "br181 c15 r40": '' // ["BR44 R12"][use vars!]    <-['c15' redun=default]
        '' //# ZZ=ZZ+WA%:IF ZZ > 360 THEN ZZ=ZZ-360
        '' //# NEXT K
  NEXT x
  :
  ZZ% = YZ: '' // [Zodiac division]['c3']
  FOR K = 1 TO (360 / WA%)
    u$ = STR$(ZZ%): u$ = MID$(u$, 2)
    PSET (x%, y%)
    DRAW "ta" + u$: DRAW "br" + P3$: DRAW "c3 r33": '' // [+var!]
        '' //# GOSUB Zodiac::->[20278!]
    ZZ% = ZZ% + WA%: IF ZZ% > 360 THEN ZZ% = ZZ% - 360
  NEXT K
  :
  ZZ% = YZ + WB%: '' // [Signs]['c3']
  FOR K = 1 TO (360 / WA%)
    PSET (x%, y%)
    IF ZZ% > 360 THEN ZZ% = ZZ% - 360
    u$ = STR$(ZZ%): u$ = MID$(u$, 2)
    v = VAL(u$) - 90: v$ = STR$(v): IF v >= 0 THEN v$ = MID$(v$, 2)
    DRAW "ta" + u$: DRAW "br" + P3$: DRAW "c3 r3 br4": DRAW "ta" + v$: DRAW "bu9 bl9": '' // <-([3+4]! (=7 !] <---
    IF SU$ <> "y" THEN GOSUB Zodiac: '' // <------------->'if g$ <> "t"]<->[M]!
      '' // ---- [Here can be inserted div. choices/options]-[Variants]
      '' // ---- [zodiacal signs/divisions around circle (+subcycles etc.) --[?]-[!]
    ZZ% = ZZ% + WA%: '' // <-[if > ...?]
  NEXT K
  :
  ZZ = YZ
  FOR K = 1 TO (360 / WC%)
    ZZ% = INT(ZZ): u$ = STR$(ZZ%): u$ = MID$(u$, 2)
    PSET (x%, y%)
    DRAW "TA" + u$: DRAW "BR" + p2$: DRAW "r" + PX$: '' // [px$:cf1062:mov->here?] <*
    ZZ = ZZ + WC%: IF ZZ > 360 THEN ZZ = ZZ - 360
  NEXT K
  '' // ['double' 5-degrees subdivs by g$='t'/[M] <-(due Trunc ?)-[!]

  if KK$ = "2" then  
    z = (ZC / 360) * (2 * PI):                             ' <-[movup?][float,x/x%!]
    FOR x = 0 TO 360 - (2 * WC%) STEP (2 * WC%)
      z = z + ((2 * PI) / (360 / WC%))                       ' [IF Z > (2*PI) THEN Z=Z-(2*PI)]
      FOR K = (p2% + 1) TO (P3% - 1)
        CIRCLE (x%, y%), K, , z, z + ((2 * PI) / (360 / WC%))
      NEXT K
      z = z + ((2 * PI) / (360 / WC%))                       ' [ej v/ w%=15 ?]  <[[[ <* missing ':' <-^^ yields err?? ]]]^^ <*
    NEXT x
  end if
  '      '#  CIRCLE (X%,Y%),(P3%+2),,Z,Z+((2*PI)/(360)): '[PI-test !?] <<-<*
  '

'--#--
'[Label]
InMainDraw:
  IF g$ = "t" OR EH$ = "A" THEN P$(mm%, hp% + 2) = P$(0, 0): '' //[MM%=0: <-OBS!] <[cf19600+]-> w h y  mm% ?]
  IF tt$ = "i" THEN m = 1: GOSUB TurnAngle: sv$ = v$
  '' // <[Sun's pos vs. horizon (Desc <- 'ta0')]<-[cf. 'PlanetSymbols:(MO)' + cf. 'Axes:(MC)]
  FOR m = (hp% + 2) TO (hp% + 1) STEP -1: '' // [Reverse hp%+ (Asc/Mc)]:?:[cf. 'Axes:']
    GOSUB axes
  NEXT m
  FOR m = 1 TO (NP% + 1): '' //   :: [^^EH$=""/chr$(13)?]
    GOSUB TurnAngle
    GOSUB PlanetSymbols
  NEXT m
      '' //# [if a%<>0/=2 then ret][<=her?]<-[cf39001]!
  GOSUB Tropos
RETURN: '>[CHART] >(goto Menu)
 '' // [Debug-Search gosub maindraw]
 
'[Label]
Tropos: '' // <-[ z% value assigned in 'DrawASC:[Outer:]' or 'InnerCircleLines:' (via 'PlusAspLines:')]
 '      ' //# <-[check out a%! (if a% <> 0)??] <-[cf. SUB LegendPrgSpecs(Misc)]
  IF ln% = 1 THEN CIRCLE (x%, y%), 168, 7: '' // [,0] [,15 ?] '' // <[remove (brown) paint border]-[Ctrl-F comment 'brown']
  '  ' // & <[cleanup imprecisions in aspect lines drawn (i.e. length)]
  '  ' // & <[give a nice look to border between white and blue]
  IF tf$ = "1" THEN L% = 0: '' // <['free' l% ?]
  IF tf$ <> "1" THEN L% = 15
  CIRCLE (x%, y%), z%, L%: '' // <[diameter inner circle (pa% or 7)]
  PSET (x%, y%), 0: '' // <-^[Tropos point set'd in Origo <(color=DawnDusk-circle!)] <[use var!]
  :
  IF z% <> pa% THEN GOTO InTroposData: '' // <--[UNFINISHED !!]-[!]
  IF tf$ = "1" THEN CIRCLE (x%, y%), 1, 0

InTroposData: '' // [name>[xBoxes]?
  GOSUB DataColumn
  GOSUB DiffStatus
RETURN: '>[InMainDraw & MinusLines]


'[Label]
TurnAngle:
  v = VAL(P$(CH%, m)) - ZY: IF v < 0 THEN v = v + 360: '' //[gosub: cf 'sub' PlusAspLines+]
  '# IF RIGHT$ >30 THEN V+1
  b% = v: v$ = STR$(b%): v$ = MID$(v$, 2): PSET (x%, y%): DRAW "ta" + v$: '' // [pset!]
  RETURN: '>[InMainDraw+ & axes]


'[Label]
DataColumn: '[MAX=60]
 : IF tt$ <> "i" THEN GOTO L20520: ' <[x40?]
L20520:
 IF MI$ = "y" THEN cc$ = "M" ELSE cc$ = "O"
 LOCATE 2, 68: PRINT f1$; : LOCATE 2, 78: IF SU% > 0 THEN PRINT cc$; : '' // [?]
 LOCATE 3, 68: PRINT N1$;
 :
 LOCATE 5, 68: PRINT H$; " "; t$;
 LOCATE 6, 68: PRINT c$; " "; tf$; : ' [f% ?]
RETURN
'----#


'[Label]
DiffStatus:
 ' ' [PP%/vars!]
 ' blw! [-> ca. Menu?][cfsub53300]
 : IF a$ <> "p" THEN GOTO L20586
 LOCATE (22 + PP%), 72: IF tt$ = t$ THEN PRINT "-S-";  ELSE PRINT "-D-"; : '' // <-[Same/Diff --(Cf. Help/Manual)]
L20586:
 : IF a$ <> "x" THEN GOTO L20594: ' >ret
 LOCATE (25 + PP%), 70: IF TA$ = t$ THEN PRINT "-S-";  ELSE PRINT "-D-"; : '' // <-[print; ?]  '<-[S=Same Harmonic as drawing]
 LOCATE (25 + PP%), 73: IF AT$ = t$ THEN PRINT "-S-";  ELSE PRINT "-D-"; : '' //  [or <> ]
L20594:
RETURN: '' // [+ [T|urned ! --###


'-----#
'[Label]
Boxes: '//
 '' // BEEP: '[DosBox soundless?]--[DEBUG]
 '' // --[blw!:[delay/intro-txt ? (ex:tt$='i')]:<-[redun cf2000+?]
 '' // if cg$ = "z" and g$ <> "t" then goto InBoxes: '' // --[='i' ?]----FIX-[!]
 if g$ <> "t" and g$ <> "h" then goto InBoxes
 locate 8, 67:  print "|-----------|";
 for L% = 9 to 13
 locate L%, 67: print "|           |";
 next L%
 locate 14, 67: print "|-----------|";
 :
 locate (19 + PP%), 68: print "           "; :'' // [<+> <=>]
 '' // & [i][M][SU] etc. & -S- -D- etc.
 '' // <p> <x> a.o, --[?]
:
InBoxes:
 IF g$ = "p" OR g$ = "x" THEN GOTO L21070: '' // [mix 210x/212x=eensub?]<-[MOV?] <<-<*!
 IF b$ = "p" THEN CH% = 1: HC% = 1: IF t$ <> "1" THEN CH% = 2: HC% = 1: '' // [hc%?]
 '' // [if b$="x" then if?] <*
 '' // IF tt$ <> "i" THEN LOCATE 14, 67: PRINT E6$;: '' // [DEBUG]
 : GOTO L21082
L21070:
L21082: '' // [REDUN!]
  '' // IF b$ = "p" THEN LOCATE 17, 67: PRINT E6$;
  '' // IF b$ = "x" THEN LOCATE 18, 67: PRINT E6$;
RETURN: '' // [cf1604,20511/39044,53300+]
'-----#

'[Label]
WAITx: '' // locate ,,0 -[?]
 locate 8, 67:  print "             ";
 for L% = 9 to 13
 locate L%, 67: print "             ";
 next L%
 locate 14, 67: print "             ";

 LOCATE 1, 58: PRINT "         ";
 LOCATE 2, 58: PRINT "         ";
 LOCATE 3, 58: PRINT "         ";
 LOCATE 4, 58: PRINT "         ";
 :: LOCATE 5, 58: PRINT "         "; ; '' // [REDUN]-[?] - (plus test if err double ;) ##
 '' // locate 2, 58: print; xx$;: '[; ;]-[?]
InWaitx:
 LOCATE 2, 58: PRINT "WAIT !   ";
 LOCATE 3, 58: PRINT xx$; : '' // --[Maxlen!]
 LOCATE 4, 58: PRINT "         ";
 LOCATE 5, 58: PRINT "         ";
RETURN
'-----#

'[Label]
STATUSx:
LOCATE 2, 58: PRINT "         ";
LOCATE 3, 58: PRINT "         ";
locate 2, 58: print sp$;"  ";KK$;"  "; : '' // [MaxLen!]-[Now:Only DRAW]
locate 3, 58: print cg$;: locate 3, 59: print g$;: locate 3, 61: print mid$(str$(s%),2);: '' // ---[i]
locate 4, 58: print left$(PR$, 8);: '' // --[redun/rpt or variant?]
RETURN
'-----#

'[Label] '' --[REDUN]-[?]
Blank:
 IF g$ = "*" OR a% <> 0 THEN GOTO BlankMain: '' //? [i$='*'?]
 FOR L% = 5 TO 6: '' // <-[fm20080][redun?]
 LOCATE L%, 67: PRINT "             ";"9"; : '' // <[e6$ !?][,0 ?]
 NEXT L%
 '' // [LOCATE L%, 67: PRINT E4$;]
'-----#

'[Label]
BlankMain:
  '' // evt. outercircle radius+1 ? <-[though diff. CornerTexts ?!]
 LINE (528, 0)-(528, 479), 6
 PAINT (x%, y%), 0, 6: '' // <--[+1=480? (leak?)]---
 SU% = 0:
RETURN
'-----#


'[Label]
Zodiac:
 '' // symbols '[pmap etc.? / bitmaps? / load fm file? / ...] [sprites->planets ?]
 SELECT CASE K
 CASE 1
  DRAW "c3"
  CALL ari
 CASE 2
  DRAW "c3"
  CALL tau
 CASE 3
  DRAW "c3"
  CALL gem
 CASE 4
  DRAW "c3"
  CALL can
 CASE 5
  DRAW "c3"
  CALL leo
 CASE 6
  DRAW "c3"
  CALL vir
 CASE 7
  DRAW "c3"
  CALL lib
 CASE 8
  DRAW "c3"
  CALL sco
 CASE 9
  DRAW "c3"
  CALL sag
 CASE 10
  DRAW "c3"
  CALL cap
 CASE 11
  DRAW "c3"
  CALL aqu
 CASE 12
  DRAW "c3"
  CALL psc
 END SELECT
RETURN



'--->
'[Label]
Menu: '' // [text/infopage (toggle)?] /// <-[g$='N'] ///
 IF a% = 2 THEN RETURN: '' // [a%<>0,a%=1,..?]<-[cf2100+]::
 IF g$ = "N" THEN LY% = 0: GOTO PrintPosNewChart: GOTO MenuInternAndExternGoto: '' // <<-<< [err goto]--[!!]
:
 tf$ = "1":
 IF tt$ = "i" THEN  tt$ = "1": LY% = 0: GOTO PrintPosNewChart: '' // [cf20460]:[1674]
 '' // (i) sub^53030-> movup->20500+!?]
:
MenuInternAndExternGoto: '' // --[cf CHART+?]
  '' // FOR L% = 8 TO 8: LOCATE L%, 80: PRINT " "; : NEXT L%: --[WHY / Redun]-[?]
  '' // LOCATE 9, 66: PRINT " ";:'[L7000]
:
 IF g$ = "N" THEN il% = 0: GOSUB L6020
:
L39030:
 GOSUB L39040: GOTO MenuInMenu:  '' // <-[g$='h'/'t'] [Sub20570  h e r e ?<-cf20462]
L39040:
 '' // LOCATE 7, 67: PRINT E4$; : LOCATE 8, 67: PRINT E6$;
 LOCATE 8, 68: PRINT "<#> "; : IF dd% = 1 THEN PRINT "<?>"; : '' // [compare L20470+]
 '' // LOCATE 9, 67: PRINT E4$;
 LOCATE 10, 68: PRINT "<h> <t> <N>";
 LOCATE 11, 68: PRINT "<a> <d> <E>";
 if CH% = 2 then locate 10,72: print "   ";
 '' // --[blankline redun/ u$/ b$ <> ''] --[-?]
:
 IF sp$ = "\qAMAP.BAS" OR sp$ = "pure" THEN GOTO L39060: '' // <-[1.bat or g$='N'][L2000+]
 LOCATE 11, 77: IF MI$ = "y" THEN GOTO L39056: '' // [L39420+]
 IF sx$ = "X" THEN PRINT "OS"
 IF sx$ = "\qAMAP.BAS" THEN PRINT "XS"
 GOTO L39060
L39056:
 IF sx$ = "\qAMAP.BAS" THEN PRINT "XO"
 IF sx$ = "X" THEN PRINT "OX"
:
L39060:
 LOCATE 14, 68: PRINT "<p> <x> <*>";
 '' // LOCATE 15, 67: PRINT E4$;
 IF a$ = "x" THEN LOCATE 18, 67: PRINT "?\|sozx>   ? "; : '' // [x:<L40036 ?]
 IF a$ = "p" THEN LOCATE (19 + PP%), 70: PRINT "<+> <=>";
 RETURN
:
MenuInMenu:
'' // BlankWAITx: '/ -- redun-temp - make own sub --
  LOCATE 9, 68, 0: PRINT "  "; " "; " "; : '' // [,0]!? -- [Note that =D before changes to =S in init run!!] -- [OBS 'SPC']-[!!] ## [?] ##
' ' ' ' '' //  LOCATE (27 + NP%), 68, 0: PRINT " ["; xx$; "]"; : '[,0]!? <*
'' // RETURN -- redun-temp ---
 g$ = INKEY$: IF g$ = "" THEN GOTO MenuInMenu: '' // <-[fm a$='p'/'x']
 IF a$ <> "x" THEN GOTO L39160
 IF g$ = "\" THEN GOTO L40040: '' // ['+'|'-'?]
 IF g$ = "|" THEN BEEP: GOTO MenuInMenu: '' // [L40140][L39650]----[-OBSNOTE-]
 IF g$ = "s" THEN GOTO L42000: '' // aspsymb[toggle]
 IF g$ = "o" THEN GOTO L42100: '' // maxorb
 IF g$ = "z" THEN BEEP: GOTO L42150: '' // [contin/step+maxhp%][toggle]
:
 : IF g$ = "x" THEN BEEP: GOTO MenuInMenu: '' // <-[TEMP!]
     '' // ::: el. nil'e a$ if g$ <> "x" [most simple?][L39102]
     '' // ::: g$="p" or ="x" [lx% both?]::
     '' // ::: A$="": LX%=PP%:LY%=PP%:LW%=PP%:LZ%=PP%:RETURN
:
L39160:
 IF a$ <> "p" THEN GOTO L39240
 IF g$ = "+" THEN GOSUB L53030: GOTO MenuInMenu: '' // [cf53050]
 IF g$ = "=" THEN LY% = LY% - 1: K% = K% + 1: GOSUB L53030: GOTO MenuInMenu: ' '  // [NOsub53300!] --##-- WHAT IS==[??]
:
L39240: ' /// [a$=""]?
 IF g$ = "#" THEN dd% = dd% + 1: GOTO L45000: 'toggle chartinfobox
 IF g$ = "*" THEN IF u% = 2 THEN GOSUB Blank: GOTO ChartDraw
 IF g$ = "*" THEN IF u% = 1 THEN GOTO L46000: '[ChartDraw++?]
 IF g$ = "t" and CH% <> 2 THEN GOTO DERIVED: '' // [t$='1'/h%=1 ?] ' [tf$ ?]
 IF g$ = "h" THEN GOTO HARMONIC: '' // #  IFG$="h"anda$="x"ora$="p"then[subwait]:gosub53xxx:goto Menu:: --##--
 IF g$ = "?" AND dd% = 1 THEN GOSUB L45500: '' // ['<?>'='secret'] -- [3rdpage?(ID)]-[?]
L39350: : : :
 IF g$ = "x" THEN a$ = g$: GOTO FactorData
 IF g$ = "p" THEN a$ = g$: K% = 1: LY% = LY% - 1: GOTO L53000
 IF g$ = "a" AND ln% = 0 THEN ln% = 1: GOSUB AspLines: : GOTO Menu: '' // [L39050 ? <-see sub]<-[goto Menu redun?] <[MenuInMenu ?]
 IF g$ = "a" AND ln% = 1 THEN ln% = 0: GOSUB MinusLines: GOTO Menu
 IF g$ = "d" AND ln% = 0 THEN ln% = 1: GOSUB DomLines: : GOTO Menu: '' // [L39050 ? <-see sub]<-[goto Menu redun?] <[MenuInMenu ?]
 IF g$ = "d" AND ln% = 1 THEN ln% = 0: GOSUB MinusLines: GOTO Menu
:
 IF g$ = "N" THEN GOSUB L7000: GOTO GoOn
:
'=-=-=-=-=
 IF sp$ = "\qAMAP.BAS" OR sp$ = "pure" THEN GOTO L39460: '^^^[L2010?][L39050]
 IF sx$ = "\qAMAP.BAS" THEN IF g$ = "X" THEN sx$ = "X": GOTO L2200
 IF sx$ = "X" THEN IF g$ = "O" THEN sx$ = "\qAMAP.BAS": GOTO L2200
 IF sx$ = "\qAMAP.BAS" THEN IF g$ = "S" THEN sx$ = "X": GOTO L19862: '[19860 ?]
 IF sx$ = "X" THEN IF g$ = "S" THEN sx$ = "\qAMAP.BAS": GOTO L19862: '[19860 ?]
 IF MI$ = "y" THEN IF g$ = "O" THEN sx$ = "\qAMAP.BAS": GOTO L2200
 IF MI$ = "y" THEN IF g$ = "X" THEN sx$ = "X": GOTO L2200
'=-=-=-=-=
:
L39460:
  IF g$ = "E" THEN GOTO Final
'' IF g$ = "A" THEN GOTO - - - - - -##

GOTO Menu: '<[loop]
'#<-----


'[Label]
Final:
'-----
'<[exit to system]
''---[kill [c:] '.swi' etc. fm here ?]
''---[ (- eller syst: .bat-file ?    ]
'-----
 print: '' // --[?] --[clear buffer in order to get back to DOS proper-[?]
 '' CLEAR: ' <-[??]
 SYSTEM
'=====>
'<[Final]


'[Label]
GoOn:
 '----->
 ''' '#[obs! z$ <-label In+]
 ''' '#[ws$]
 OPEN "switch.sw0" FOR OUTPUT AS #3: '[subredun cf39500+]? < '' <[.\]
 PRINT #3, sw$
 PRINT #3, sx$
 PRINT #3, s%
 CLOSE #3
:
'' // '  <[ws$]-[?]
'' // '------------
'' // '  open "identity.tie" for output as #2: '' <[.\]
'' // '  print #2, f$: '[ry]?
'' // '  close #2
'' // '------------
:
cg$ = g$
OPEN "choice.sw0" FOR OUTPUT AS #1: '' <[.\]
PRINT #1, cg$
CLOSE #1
:
'-------------
'' IF g$ = "N" THEN GOTO N
'' if g$ = "A" then - - -
'-------------
:
'' N:
LOCATE 1, 52: PRINT ws$ + ": DRAW     "
LOCATE 2, 52: PRINT "-> TIE     "
LOCATE 3, 52: PRINT "  (loading)"
'' xx:
:
:
CHAIN "\aqTIE.BAS"

'#=#=#
'[redunexit:]>
goto Irregular
END:
'--[pgr exit (path)!?]:cls?:[scr0 ?]:[ms$ ?]--
'--[locate 10,1 -wait?]
'--['filter':sure?/Esc before exit!] ---'
'#=#=#


'---->
'''blw![x=56 if opposit not thru inner circle]? <*<--replaced by smaller circle!!
'----

'[Label]
AspLines:
  '' // # [xx$ = "+ALines": GOSUB WAITx] #
  DO
    GOSUB Boxes
    LOCATE 11, 68
    PRINT "<2-10> "; '' // <[8,68 ?] ' [<>. ?]
    GOSUB TypeChoice
    y$ = u$
  LOOP WHILE VAL(u$) < 2 OR VAL(u$) > 10
  il% = VAL(y$)
  xx$ = "[+Alines]" + STR$(il%)
  GOSUB WAITx  '' // [DO: improve text!!]
  GOSUB Boxes 
  GOSUB TempCirc: '' // --[y$]--
  GOSUB PlusAspLines
RETURN '[menu--]


'[Label]
DomLines:
 '' // [cf. 'AspLines:' !]
 il% = 10: '' // [input no. of planets early in prg!] --[temp!]
 xx$ = "[+DLines]": GOSUB WAITx
 GOSUB Boxes
 GOSUB TempCirc
 GOSUB PlusAspLines: '' // --[Dom!]
RETURN: '[menu]--


'[Label]
TempCirc:
 ' ' ' if mi$ ...
 CIRCLE (x%, y%), 168, 6: '<[paint border] <[removed in 'Tropos:'!]
     '-------' [blw! cf. DawnDusk]>
    '# <[circle e. 'next m' pga unoy 110-->mc/ic]?
    '# FOR M = HP% + 2 TO HP% + 1 STEP -1: 'M=1 TO 2
    '# GOSUB TurnAngle: '[=c0= nil'es v/gosub (pset?)]
    '# DRAW "c0 bl57 l110": PSET (x%, y%): DRAW "c0 br57 r110": '[try mc=90-grad]
    '# NEXT M:
  '''# CIRCLE (x%, y%), pa%, 8: '--<[reinforcement redun]?--< [cf.'MinusLines:']
 PAINT (x%, y% + 4), 15, 6: '<[pset'd  ?][+4=dum (+1 leaks?)]
RETURN '>[AspLines & DomLines][+ InSuorNot/L19862+]


'[Label]
PlusAspLines: ' /// [+varia!]
 ' [mayhap orb-asp overlap![ego:P->H=S->P][cint/int?]]
  z$ = "168":
  IF MI$ = "y" THEN z$ = "108" ' [->CHART+ [vars!] [+swi.swi]]
  IF g$ = "d" THEN z$ = "140"
  FOR z = 1 TO il%:  '<[NP% + 1:] '<[(9+1)][b%=val() ?!] [z?]<->[float?]
    v = VAL(P$(CH%, z)) - ZY
    IF v < 0 THEN v = v + 360 '' // [sub:cfInMainDraw+]
    ' IF RIGHT$ > 30 THEN V+1: '' // [p$=p$() <-free choice of h% ?]
    b% = v
    v$ = MID$(STR$(b%), 2)
    ' [vz=p$() [vx=]:*?]
    i$ = tf$
    i% = 0 '<-(t e m p t r y !!) <*
    
    FOR x = 1 TO il%:  '[NP% + 1:] '[obs! np%][float,x/x%!]
      dr$ = ""
      LOCATE 11, 69
      w$ = w$(HC%, z, x)
      IF g$ = "a" THEN GOSUB Asp '<[DR$]
      IF g$ = "d" THEN GOSUB Dom '<[DR$]
      IF dr$ = "" THEN GOTO L23970 '<[next x]
      
      PSET (x%, y%)
      DRAW "ta" + v$
      DRAW "br" + z$ '[draw rpt (redun) ?]
      PZ$ = MID$(STR$(POINT(0)), 2)
      PY$ = MID$(STR$(POINT(1)), 2)
      XY$ = PZ$ + "," + PY$
      v = VAL(P$(CH%, x)) - ZY
      IF v < 0 THEN v = v + 360 '' // [gosub:cfInMainDraw+]
      D% = v
      PSET (x%, y%) '[^^pz$/px$:cf1062!^^]
      
      SELECT CASE dr$
        CASE "d"
          GOSUB DLines
          i% = 0
        CASE ":"
          GOSUB L24100
          GOTO L23970 '[nil] <next
        CASE "-"
          GOSUB L24150
          GOTO L23970 '[nil] <next
        CASE "*"
          GOSUB L24200
          i% = 2 '<[varptr$ ?]
        CASE "k"
          GOSUB L24250
          i% = 4 '<[check gwAmap for 'goto' or likes.. (all!)]
        CASE "t"
          GOSUB L24300
          i% = 2: '  -'-
        CASE "o"
          GOSUB L24350
          i% = 4
      END SELECT
      ' <[noasp<=orb]! <-<* [?]
      
      IF D% > 359 THEN D% = D% - 360 '[redun?] <*---
      IF D% < 0 THEN D% = D% + 360 '[redun?] <*---
      
      ' [if g$='a'/'d' then d$=] ::::: <-no! erase! <* <*
      
      DRAW "ta" + STR$(D%)
      DRAW "br" + z$
      DRAW "c" + STR$(i%)
      DRAW "m" + XY$ '[cmp 'LINE']
      IF g$ = "d" THEN CALL ArrowASC(i$, i%) '<-[t e m p !] <*
      '# ^^math(equilattrekant)^[radianer..]
      '# ex:for-next V$+/-1 fmbothpos->broadlines*!? [float!]
      '# IF Z=5 AND X=7 THEN STOP
L23970:
    NEXT x
  NEXT z
  GOSUB InnerCircleLines
  PAINT (x%, y% - 4), L%, 6: '<-(see comm 'DrawAsc:[Outer:'] !!) [4=dum]
  CIRCLE (x%, y%), z%, 15
  GOSUB DawnDusk
  GOSUB Tropos
RETURN: '>[menu (fm g$='a'/'d']'''# [GOTO Menu: '[L39050 ?] [vars:+swi.swi]]


'[Label]
InnerCircleLines: '<[pset reduns?]
     ' <[inner circ smaller!? (oppos<>axes)!]? [choice inner circ (switch)]?
     '# O% = pa% - 1: : : i% = pa%: IF MI$ = "y" THEN O% = (pa% - 20) - 1: i% = pa% - 20
 z% = 9: '<[7 ?] <[use vars!] <-[Resizing!]
 CIRCLE (x%, y%), z%, 6
    '# FOR l% = 0 TO O%: CIRCLE (X%, Y%), l%, 0: NEXT l%: CIRCLE (X%, Y%), i%
    '# ^[l%=1?][pset movup?][her ogsaa nil'es,cf39840+]
 ' [Hemispheres]:
 IF VAL(sv$) > 180 THEN i% = 1: il% = 9: L% = 3:      '<-blw![check v$!]
 IF VAL(sv$) < 180 THEN i% = 9: il% = 1: L% = 11
  ' ' IF VAL(sv$) > 170 AND VAL(sv$) < 190 THEN i% = 1: '[dawn]
  ' ' IF VAL(sv$) > 350 AND VAL(sv$) < 10 THEN i% = 1:  '[dusk]
RETURN: '>PlusAspLines



: : '  /// TEMP! (AspLines 0,30] [+ 150!] ///

L24100:
 RETURN: '[cf 23600 <-??] [+ 'deflect' (widen) stellium during chart draw ?!]

L24150:
 RETURN

L24200:
 ' IF B% < D% THEN D%=B%+60:REM:IF D% > 359 THEN D%=D%-360
 ' IF B% > D% THEN D%=B%-60:REM:IF D% < 0   THEN D%=D%+360
 IF b% < D% THEN IF D% - b% > 180 THEN D% = b% - 60
 IF b% < D% THEN IF D% - b% < 180 THEN D% = b% + 60
 IF b% > D% THEN IF b% - D% > 180 THEN D% = b% + 60
 IF b% > D% THEN IF b% - D% < 180 THEN D% = b% - 60
RETURN

L24250:
 ' IF B% > D% THEN 24280::REM*[=180?][math?]:[asp->orb!]*
 IF b% < D% THEN IF D% - b% > 180 THEN D% = b% - 90
 IF b% < D% THEN IF D% - b% < 180 THEN D% = b% + 90
 ' GOTO 24292::[return] [doesn't work-if's mustbe][try 0ari=0]?  <<-<<***
 IF b% > D% THEN IF b% - D% > 180 THEN D% = b% + 90
 IF b% > D% THEN IF b% - D% < 180 THEN D% = b% - 90
 RETURN

L24300:
 ' IF B% < D% THEN D%=B%+120:REM::IF D% > 359 THEN D%=D%-360
 ' IF B% > D% THEN D%=B%-120:REM:IF D% < 0   THEN D%=D%+360
 IF b% < D% THEN IF D% - b% > 180 THEN D% = b% - 120
 IF b% < D% THEN IF D% - b% < 180 THEN D% = b% + 120
 IF b% > D% THEN IF b% - D% > 180 THEN D% = b% + 120
 IF b% > D% THEN IF b% - D% < 180 THEN D% = b% - 120
 RETURN

L24350:
 D% = b% + 180: IF D% > 359 THEN D% = D% - 360
 RETURN

'-----
DLines:
 IF b% < D% THEN IF D% - b% > 180 THEN D% = b% - VAL(XL$)
 IF b% < D% THEN IF D% - b% < 180 THEN D% = b% + VAL(XL$)
 IF b% > D% THEN IF b% - D% > 180 THEN D% = b% + VAL(XL$)
 IF b% > D% THEN IF b% - D% < 180 THEN D% = b% - VAL(XL$)
 RETURN: '>[plusasplines]
'------

'[Label]
Asp:
  XL$ = LEFT$(w$, 3)
  ZL$ = RIGHT$(w$, 2) '[float?]<->[rounded!!]
  XZ$ = XL$ + "." + ZL$
  locate 11, 68
  print "w$: "; w$
  E = VAL(XZ$): '--[w$(0,0) & (0,x)?]--
  locate 12, 68
  print "e:  "; e 
  locate 13, 68
  AO% = OA%
  IF E <= 0 + AO% THEN GOTO L43100
      '' // [[IF Z=5 AND X=7 THEN STOP]] ----
  AO% = (OA% / 4)
  IF E >= 30 - AO% AND E <= 30 + AO% THEN GOTO L43150
  AO% = (OA% / 4) * 3
  IF E >= 60 - AO% AND E <= 60 + AO% THEN GOTO L43200
  AO% = OA%
  IF E >= 90 - AO% AND E <= 90 + AO% THEN GOTO L43250
  AO% = OA%
  IF E >= 120 - AO% AND E <= 120 + AO% THEN GOTO L43300
  AO% = OA%
  IF E >= 180 - AO% AND E <= 180 + AO% THEN GOTO L43350
  ' [^^ abs(val) & if 359-60 ++ etc.][int/cint] [only >&< (not=)]?
  ' [value-360 etc. and +/- aspect <-decide in aspcalc]!?
  ' [ownsymbol(+/-)for asp in/ex temperament]!?ex:[*+]
  ' [<- overlappende aspekter? <-kun ett blir oppdaget]!??
RETURN: '>[plusasplines]

L43100: PRINT ":"; : dr$ = ":": RETURN: '[dr$: >PlusAspLines+]
L43150: PRINT "-"; : dr$ = "-": RETURN: '[TecCompu:compare 'loose' for-next]
L43200: PRINT "*"; : dr$ = "*": RETURN
L43250: PRINT "k"; : dr$ = "k": RETURN
L43300: PRINT "t"; : dr$ = "t": RETURN
L43350: PRINT "o"; : dr$ = "o": RETURN
'---

'[Label]
Dom:
 y$ = RIGHT$(N$(CH%, z), 3)
 XL$ = LEFT$(w$, 3)
 IF y$ = s$(1) THEN IF x = 5 THEN dr$ = "d": RETURN: '<all!? <-[CHECK QBasic CHECK] !! <*
 IF y$ = s$(2) THEN IF x = 4 THEN dr$ = "d": ' -'-
 IF y$ = s$(3) THEN IF x = 3 THEN dr$ = "d"
 IF y$ = s$(4) THEN IF x = 2 THEN dr$ = "d"
 IF y$ = s$(5) THEN IF x = 1 THEN dr$ = "d"
 IF y$ = s$(6) THEN IF x = 3 THEN dr$ = "d"
 IF y$ = s$(7) THEN IF x = 4 THEN dr$ = "d"
 IF y$ = s$(8) THEN IF x = 10 THEN dr$ = "d": '<[modern]
 IF y$ = s$(9) THEN IF x = 6 THEN dr$ = "d"
 IF y$ = s$(10) THEN IF x = 7 THEN dr$ = "d"
 IF y$ = s$(11) THEN IF x = 8 THEN dr$ = "d": '<[modern]
 IF y$ = s$(12) THEN IF x = 9 THEN dr$ = "d": '<[modern]
RETURN: '>[plusasplines]
'---


'[Label]
MinusLines:
 '' // Asp or Dom ---
 xx$ = "[-Lines]": GOSUB WAITx
 GOSUB Boxes
' [fm rolldown]:FOR X=168 TO 155 STEP-1:CIRCLE(245,100),X,0:NEXT X
 ' if mi$='y'/chr$(13)/'' ......................
 '# [pset(x%,y%)]?
 : CIRCLE (x%, y%), 168, 6: '' // --[is kept +lines 'c6' circ ??] --[cf. TempCirc !]  [+ (168+1) cleanup fm asp&dom lines?)
 PAINT (x%, y% - 4), 1, 6: '' // --[pset'd ?][+/- 4=dum <(aspcircle=7)] --(paint color '1' ?)
' Inner Circle Lines>
 CIRCLE (x%, y%), pa%:
 : CIRCLE (x%, y%), 168, 0:     '' // --[remove ?!]
 PAINT (x%, y% - 1), 1, 15:     '' // --[best placement of this code?] --[cmp DawnDusk !!]
 PAINT (x%, y% + 1), 0, 15:     '' //  -'-
  FOR m = (hp% + 2) TO (hp% + 1) STEP -1: '' // [Reverse hp%+ (Asc/Mc)]:?:[cf. 'Axes:']
  GOSUB axes
  NEXT m
 GOSUB Tropos
RETURN: '[menu]--


'[Label]
FactorData:
 '' // [g$='x']--[a$ ?][sub L40500 redun?][h%<-float!]
 '' // [WAITx ?] 
 GOSUB Boxes: LOCATE 10, 68: PRINT "this<CR> or"; : '[c32?]
 LOCATE 11, 68: PRINT "aspects "; "<--";
 LOCATE 12, 68: PRINT ; "har "; : GOSUB TypeChoice: TA$ = u$
 : IF u$ = "" THEN TA$ = t$: AT$ = t$: GOTO InFactorData1
 IF VAL(u$) < 1 OR VAL(u$) > 300 THEN GOTO FactorData: '' // [ERRCHK!]
 LOCATE 11, 76: PRINT "<->";
 LOCATE 13, 68: PRINT ; "har "; : GOSUB TypeChoice: AT$ = u$
 IF VAL(u$) < 1 OR VAL(u$) > 300 THEN GOTO FactorData: '[errchk!<-(kunat$?]
:
InFactorData1:
 GOSUB Boxes
 GOSUB L53300: '' // [L40000?]
 : xx$ = TA$ + "&" + AT$: GOSUB WAITx: '' // --[REVORDER Box-Wait ?]
 : IF u$ = "" AND t$ = "1" THEN HC% = 1: GOSUB L40500: GOTO InFactorData2: '' // [ch%=1 ?]
 HC% = 0: '' // [print h$/c$ ?][cfHC%<-laan w$(0,..] --[check!]
 : CH% = 1: '' // --[check!]--[where's hc%=1 ?]
 v% = 1: H% = VAL(TA$): '' // (for--next errchk [ex: <1])
L40020:
 IF H% > 1 THEN CH% = 2: GOSUB SubHarmonic: '' // obs! [ch%]
 IF v% = 1 THEN O% = 1: GOSUB PreAspectCalc: '' // [o%:cf dummies:]
 v% = v% + 1: IF v% = 2 THEN H% = VAL(AT$): GOTO L40020
 GOSUB AspectCalc: CH% = 1: H% = VAL(t$): '' // --:check!][cf40012][53038][Boxes+]
 '' // [ch%=/h%= -> 39100+?]:[v%gets=3?]
:
InFactorData2:
 LX% = 1: LZ% = 0
 LOCATE 16, 68: PRINT H$; " "; TA$; "^"; AT$;
 '' // >999^999[her]->999sloyfh$(h:)!?[errmax?]
 LOCATE 17, 68: PRINT c$; "..";
 GOSUB L39040
 GOSUB DiffStatus: '' // --[cf L53038][sub DiffStatus movto ca. Menu ?]
 '' // [why L39040 her ?]

L40040: '' // [g$='\']--[]
 FOR v% = 1 TO LT% - 1
 LZ% = LZ% + 1
 LOCATE 18 + v%, 68: PRINT K$(LX%); " ";
 : IF OO% = 1 THEN LOCATE 15 + v% + 2, 69: w$ = w$(1, LZ%, LX%): GOSUB Asp: '[L42200]
 LOCATE 18 + v%, 70: PRINT K$(LZ%); " "; w$(HC%, LX%, LZ%); "x";
 IF LZ% = PP% THEN LX% = LX% + 1: LZ% = 0: IF LX% = PP% THEN LX% = 1
 :::NEXT v%::::stop::::
 LZ% = LZ% - (LT% - 2): IF LZ% < 0 THEN LZ% = LZ% + PP%: LX% = LX% - 1
 GOTO MenuInMenu: '' // --[obs!var, obs!goto]
'' // ---[endlabelfactordata]


L40140: ' ' [g$='|']--[-OBSNOTE-]
 FOR v% = 1 TO LT% - 1
  LZ% = LZ% + 1
  LOCATE 15 + v% + 2, 68
  PRINT K$(LX%); " "; w$(HC%, LX%, LZ%); " "; K$(LZ%); "  ";
  IF LZ% = PP% THEN LX% = LX% + 1: LZ% = 0: IF LX% = PP% THEN LX% = 1
  IF OO% = 1 THEN LOCATE 15 + v% + 2, 78: w$ = w$(1, LZ%, LX%): GOSUB Asp: '' // [L42200]
 NEXT v%
 LZ% = LZ% - (LT% - 2): IF LZ% < 0 THEN LZ% = LZ% + PP%: LX% = LX% - 1
 GOTO MenuInMenu
 '' // [lw%lx%ly%*?:y%u%e%t%st%[input$ ?]]


'###
 '' // ---STOP---whatis----
L40500: ' <CR>[sub dublett?][cf L40000+/SubFactorData+][float?]
:::: STOP ::::: FOR x = 1 TO PP%
 : FOR z = 1 TO PP%
 : w$(HC%, x, z) = w$(1, x, z): REM:tegning=1 or 0 [ch%]?
 : NEXT z
 : NEXT x
 : RETURN
' '  // ---#
'###


'[Label]
L42000:
 '' // aspsymbol --- g$='s [a$ ?]:[toggleshoworb,..?][appl/sep,..?]
 : : IF a$ = "p" THEN STOP: '' // --[Menu]
 GOSUB Boxes: LOCATE 10, 68: PRINT "symbols"; : '' // [expand 's'!]
 IF OO% = 0 THEN LOCATE 10, 76: PRINT "ON ";
 IF OO% = 1 THEN LOCATE 10, 76: PRINT "OFF";
 LOCATE 11, 68: PRINT "maxorb:"; OA%;
 LOCATE 13, 70: GOSUB WaitLoop: '' // <[redun?]
 OO% = OO% + 1: IF OO% = 2 THEN OO% = 0
 GOTO Menu

L42100: ' /// [g$='x'--> a$=g$--> g$='o']
 : : IF a$ = "p" THEN STOP: : : : : ' [Menu]:?:[cf1606]
 GOSUB Boxes: LOCATE 10, 68: PRINT ; "orbis";
 LOCATE 11, 68: PRINT "max-> "; : GOSUB TypeChoice: OA% = VAL(u$): '' // [ERRCHK!]
 GOTO Menu: '' // --[MenuInMenu?]

L42150: '' // [g$='z'::input st% & max hp%]
42160 GOTO Menu: '' // [return?] --UNFINISHED!



L45000: '' // [x,z float?]
 GOSUB L53200: '' // [+whileblankout othermenuitems]-[?]
 IF dd% = 1 THEN GOSUB L20520: GOTO Menu: '<[tt$=?] <-[NO !]
 FOR z = 1 TO 5
 LOCATE z + 1, 68: PRINT m$(1, z); : '[blank '-' ): S/W)]
 x = VAL(m$(1, z)): LOCATE z + 1, 77
 ' <-[variants?][tz$=input#'ed zone!]
 IF z = 3 AND VAL(ds$) = 0 THEN PRINT "zt";
 IF z = 3 AND VAL(ds$) <> 0 THEN PRINT "dt";
 IF z = 3 OR z = 4 AND x = 0 THEN GOTO L45070: '>nextz
 IF z = 4 AND x > 0 THEN PRINT " n";
 IF z = 4 AND x < 0 THEN PRINT " s";
 IF z = 5 AND x > 0 THEN PRINT " e";
 IF z = 5 AND x < 0 THEN PRINT " w";
 '' // simplify loop!?[..else..?][^Long1st!][nil Equat/Greenw]
L45070: NEXT z
 : dd% = 0: GOTO L39030: '' // [i]<-(dd%=1)

L45500: ' /// ****
 aa% = aa% + 1
 LOCATE 2, 67: PRINT "             ";"8";
 LOCATE 2, 68
 IF aa% = 1 THEN PRINT m$(1, 0); : '[(0,1)etc.?]
 IF aa% = 2 THEN PRINT f1$; : aa% = 0
RETURN
  '' // [simplify loop?(=0/1)

L46000: '--------
 u% = 2: '[x%=h%][ch%?]<<-<*
 z$ = "|:::::::::|:::::::::|:::::::::| "
 GOSUB Blank: b% = 0: O% = 2: 'grid loc [row,col]
 FOR z = 1 TO 12: LOCATE b% + z, O%: PRINT z$; s$(z): NEXT z
FOR L% = 1 TO 12: '[blw! &^ <-(z,d float?)]
il% = -1: FOR z = 1 TO 12
IF RIGHT$(N$(CH%, L%), 3) = s$(z) THEN il% = z: z = 12
NEXT z
FOR D = 0 TO 29
IF VAL(LEFT$(N$(CH%, L%), 2)) = D THEN D% = D: D = 29: '<[float?]
IF VAL(MID$(N$(CH%, L%), 4, 2)) > 29 THEN D% = D% + 1
NEXT D
 ' [Z%(M)=il%+D%]
IF il% <> -1 THEN LOCATE il%, (D% + 1) + O%: PRINT K$(m); : '[;]?
NEXT L%
GOTO Menu
'--------


'[Label]
TruncateRounding:
 i%  = int(val(z$))
 ii% = VAL(LEFT$(z$, 3))
 GOSUB InTrunc
RETURN
:
'[SubLabel]
InTrunc:
 s$ = ""
 FOR L% = 11 TO 0 STEP -1: '<[step redun?]
  IF ii% >= (L% * 30) THEN s$ = s$(L% + 1): L% = 0: '' // [Blw> [ii%= ii% -( ) here!?]-[whatis]-[?]
 NEXT L%
 '' // L52035: // [why double (cfSubHarmonic+)]? <--- obs! <---
 FOR L% = 0 TO 11: '' // <[L52040 ?]
  IF s$ = s$(L% + 1) THEN ii% = ii% - (L% * 30): L% = 11
 NEXT L%
 r = val(mid$(z$,4))
 r = (r*60)
 r = r + 0.5
 i% = int(r)
 if i% > 59 then i% = (i% - 60): ii% = (ii% + 1)
 i$ = STR$(ii%): i$ = MID$(i$, 2)
 IF ii% < 10 THEN i$ = "0" + i$: '' // [" " + i$-]-[?]
 r$ = str$(i%): r$ = mid$(r$,2)
 if i% < 10 then r$ = "0" + r$: '' // [" " + i$-]-[?]
 z$ = i$ + "-" + r$ + " " + s$: '' // (z$:file:L2000+) [-/r (Rx) ?]
 : : : if ii% >= 360 then stop::
 : : : if i% > 59    then stop::
 : : : if len(r$) > 2 then stop::
 '' // also ERRCHKerrchk if ii% = 0]-[?]-[!]
 '' // --[whatif  r [a.o].= 0]-[?]-[#]
RETURN
'<---

L53000: ' *** pos* [trop/sid ?]*
 'rem:[+this <CR> <-cf40000+]
 '' // GOSUB Boxes
 LOCATE 9, 68: PRINT "positions:";
 LOCATE 10, 68: PRINT "har "; : GOSUB TypeChoice: tt$ = u$: H% = VAL(tt$)
 IF H% < 1 OR H% > 300 THEN GOTO L53000

PrintPosNewChart:
 '' // [WAITx ?] 
 '' // GOSUB Boxes:
 GOSUB L53300: '' //<-[x50redun='N'?<-cf2210,6032][gotox27?]
 xx$ = tt$: '' // GOSUB WAITx:::::::  'blw!:[ch%/hc%:cf1633] <-[k%!] --[REVORDER Box-Wait ?]
 IF H% = 1 THEN CH% = 1: HC% = 1: GOTO L53029: '' // [h% i draw/pos?] <-[cf6050]!
 CH% = 0: GOSUB SubHarmonic: HC% = 0: '' // [hc% mov/chng/coll?]
L53029:
 GOSUB L53030
 GOTO MenuInternAndExternGoto: '' // --[!] ### [LOOP AROUND Menu: not meta-sub, but 'goto' !!] ###
:'###
:
L53030:
'' // [ly%=0 ?]
 LOCATE 16, 68: PRINT H$; " "; tt$; " :"; : '' // [er h% nullet[tt$]]?
 GOSUB DiffStatus: '' // --[cf40036]::LOCATE 17,67:PRINT E4$;:'[^movsubx70?]
 :
L53050: '' // [GOSUB 39040] '[mov?]<-[cf39162] <<-<*
 IF K% = 3 THEN K% = 1
 FOR v% = 1 TO LT%: LY% = LY% + 1: IF LY% > PP% THEN LY% = 1
 LOCATE 17 + v%, 68: ON K% GOSUB L53410, L53430
 IF LY% = PP% THEN LY% = 0
 NEXT v%
 : LY% = LY% - (LT% - 1): IF LY% <= 0 THEN LY% = LY% + PP%
RETURN

 
'' // WHAT IS -[?];
'' // L53170: :::stop::: 'IF A$<>"" THEN 53045 ?::
'' // L53180: ::::stop:::: 'GOTO 39350: '[53600 ?]:k%=1::

L53200:
 FOR L% = 2 TO 6: '' // --[fm45020]
 LOCATE L%, 67: PRINT "             ";: '' // --[13 spc]
 NEXT L%
 LOCATE 8, 72: PRINT "   "; : '' // [if toggl e%=?]
RETURN

L53300: '[cfsub 20570,6000, (L7000 <-g$='N') !][cf Menu]
 FOR L% = 16 TO 24: LOCATE L%, 67: PRINT E6$; : NEXT L%: '' //[?]
 FOR L% = 70 TO 73 STEP 3: LOCATE 25, L%: PRINT " "; : NEXT L%
 LOCATE 25, 76
 IF a$ = "p" THEN PRINT "p"; : b$ = a$
 IF a$ = "x" THEN PRINT "x"; : b$ = a$
RETURN: '[->20570+?]


'' // [00-00/00r00 Xxx]!
'' // [L850/52]:[SubHarmonic+]
L53410:
PRINT K$(LY%); " "; N$(HC%, LY%);
RETURN

L53430:
PRINT K$(LY%); " ";
PO$ = P$(HC%, LY%)
print left$(PO$, 11);
RETURN
' ---

'[Label]
TypeChoice:
 '' // <DIR> input-emul (screen2)[common] [input$() ?]:key(n)off
 u$ = ""
 '' // (input):poss writerubbish! (line input??)::arrows etc.
LocLoop: in$ = INKEY$: IF in$ = "" THEN GOTO LocLoop: '' // Blw:[cf2100+/amap]
 IF in$ = CHR$(13) OR in$ = CHR$(27) OR LEN(u$) = 8 THEN GOTO RetThis
 IF ASC(in$) > 96 AND ASC(in$) < 123 THEN in$ = CHR$(ASC(in$) - 32): '' // [ERRCHK] & [HIGH HARMONIC !]
 IF u% = 1 THEN PRINT in$; : u$ = u$ + in$: '' // [u%=0 ?]
 GOTO LocLoop: '' // [where? <-u%= ][cfL1670]
RetThis:
if in$ = CHR$(27) then gosub WAITx: goto Menu: '' // [WAITX Redun or elsewhere]-[?]
RETURN: '' // [cf'atie']
 '' // [errchk/changes/varia,..!]--[ex:del-tast,no -space-!]


'' // [WHAT IS]-[?]
'' // 57000 ::print "<key>";
'' // 57010 in$=inkey$:if in$="" then 57010
'' // 57020 return

WaitLoop:
'' // ['wait'?]--[cpu-depend!]-[Redun]-[?]
 FOR L% = 1 TO 99999: NEXT L%
RETURN

'---

'[Label]
axes:
  '' // '# [Unprecise axes! (trunc vals)] ###
  '' // <[Asc or MC first (hp% + ?] <[coord!] :?: [cf. 'InMainDraw:'] [asc=asc]?
  i$ = tf$ '' // <[best placement in prg ?] <--
  SELECT CASE m
    CASE hp% + 2: '[ASC]
      GOSUB TurnAngle
      GOSUB DrawASC
    CASE hp% + 1: '[MC]
      GOSUB TurnAngle
    IF tt$ = "i" THEN mcv$ = v$ '' // <[MC's pos vs. horizon (Desc <- 'ta0')] <-[cf. 'InMainDraw:'<(m=1=Sun) + cf. MO]
    GOSUB DrawMC
  END SELECT
  i$ = tf$
  IF m = (hp% + 1) THEN GOTO RETimd '' // <[if hp%+2 ?]<->[Asc/MC +1/+2 ?] <-(which 1st ?)
  DRAW "ta0"
  '' // IF tf$ <> "1" THEN DRAW "c" + STR$(i%): '<[color lost by Gosub, Pset, etc. (not by Call)]
  LOCATE 59, 51
  PRINT "MC";
  PSET (440, 465)
  CALL ArrowMC(i$, i%)
  LOCATE 60, 51
  PRINT "ASC";
  PSET (440, 475)
  CALL ArrowASC(i$, i%) '' // <['asc'; nocurs]^
  '' // IF tf$ <> "1" THEN DRAW "bu3": PAINT STEP(0, 0), i%, 15 --[?]
  LOCATE 59, 59 '' // ['mc =    spaces]-[??]
  IF tf$ = "1" and CH% = 1 THEN PRINT " S";
  IF tf$ <> "1" THEN PRINT "Turned  ";
  if CH% <> 1 then print "HAR     ";
  LOCATE 60, 59: '' // ['asc =      ' ?] <-[backgrcolor problem !?]
  IF tf$ = "1" and CH% = 1 THEN PRINT " E";
  IF tf$ <> "1" THEN PRINT "Turned  ";
  if CH% <> 1 then print "HAR     "; '' // [What if SU etc]. --[?]
RETimd:
RETURN '>[InMainDraw & MinusLines]


PlanetSymbols: ' /// 'planet's
  '  node/arab..!?
  '  axes/lines..draw1stdue'luft'tilsymboler!!
  '# L60030:
  IF MI$ = CHR$(13) THEN GOTO L60050
  DRAW "br163"
  FOR L% = 1 TO 3
    CIRCLE STEP(0, 0), L%
  NEXT L%: '[br/blxx]?
  DRAW "bl49"
  CIRCLE STEP(0, 0), 3 '[48]?
  DRAW "br2" '<[br <-place 'planet' symb]!
  GOTO L60052
L60050:
  DRAW "br" + p1$
  CIRCLE STEP(0, 0), 3
  DRAW "br56"
  FOR L% = 1 TO 3
    CIRCLE STEP(0, 0), L%
  NEXT L%
  DRAW "bl56"
L60052:
  DRAW "br" + O$
  DRAW "ta0"
  DRAW "bu6 bl12"
 ' IF tf$ <> "1" THEN STOP

 '' // [ON m gosub SUN,MO >- -> case 3] <[alternative]-[?]

  SELECT CASE m
  CASE 1
    CALL SUN(tf$)
  CASE 2
    GOSUB MO
    IF tt$ = "i" THEN mv$ = v$ '' // <[MO's pos vs. horizon (Desc <- 'ta0')] <-[cf. 'InMainDraw:'<(m=1=Sun) + cf. 'Axes:(MC)]
  CASE 3
    CALL ME
  CASE 4
    CALL VE
  CASE 5
    CALL MA
  CASE 6
    CALL JU
  CASE 7
    CALL SA
  CASE 8
    CALL UR
  CASE 9
    CALL NE
  CASE 10
    CALL PL
  END SELECT
RETURN '>[InMainDraw] '[<=Select Case ??]


'[Label]
DrawASC: ' /// '<[56/57 ??] [cf DawnDusk!] # ['ta0'=Desc !!]  ['right'<->'left' (on screen!)]  ['up'<->'down'] <-!!!
  ' [l%=color horiz plane day/night (Tropos/inner circle): '<['free' l%/i%/il% ??] '[redun pset etc. ?]
  ' [i%/il%=sky color above/below horizon]
  '# FOR l%=1 TO 10
  '# CIRCLE (X%,Y%),P1%-l%,,V,V+((2*PI)/360)
  '# CIRCLE (X%,Y%),P1%-l%,,(V-PI),(V-PI)+((2*PI)/360) <<-<*
  '# NEXT l%

  '[Hemispheres]: '[cf. 'DawnDusk:'] '>[Drawasc & Innercirclelines]
  IF VAL(sv$) > 180 THEN
    i% = 1
    il% = 9
    L% = 3      '<-blw![check v$!]
  END IF
  IF VAL(sv$) < 180 THEN
    i% = 9
    il% = 1
    L% = 11
  END IF
  ' IF VAL(sv$) > 170 AND VAL(sv$) < 190 THEN i% = 1: '[dawn]
  ' IF VAL(sv$) > 350 AND VAL(sv$) < 10 THEN i% = 1:  '[dusk]
 
  IF MI$ <> CHR$(13) THEN
    DRAW "bl57 l110"
    PSET (x%, y%)
    DRAW "br57 r110" '' // <[where pre-pset'd ?]
    CALL ArrowASC(i$, i%)
    PSET (x%, y%) '' // >pset? ::[i$=?? (tf$?)
  ELSE
    '// # [DRAW "r" + PA$: DRAW "br"+Q$:DRAW "br"+O$:DRAW "ta0":DRAW "bu6 bl12"[+mc]]
    DRAW "bl57 l110 l12" '<[where pre-pset'd ?][cf TurnAngle]<-[left/right mirrored!] <* [bl57/br57]<->[cf. PAINT 'DawnDusk']
    PSET (x%, y%): DRAW "br57 r110 r12 br41 r9" '' // [drawn axes inside main circle]
    ' ' IF tf$ <> "1" THEN DRAW "c" + STR$(i%):  '<[color as above radix horizon]
    CALL ArrowASC(i$, i%) '' // [cf. 'DrawMC:']
    PAINT STEP(0, 0), i%, 15 ' <-[use vars! <-pa%+dum] [turnangle'd ??]
    DRAW "bu20" '<[dum]<[cf. comments in 'ArrowASC:']
    PAINT STEP(0, 0), il%, 15
    PAINT (x%, y% - 10), L%, 15  ' [,,defaultborder <(var) ?] <-[Tropos default] <[pset'd ?]
      ' [10=dum]      '[magenta/light magenta? (shades/sunrise/set?)] ^^ [init inner circle = horizon plane (symbolic!)]
      '' // [is painted (first) even if ='t' !? <(also A&D Lines!?)]
    z% = pa%
    GOSUB DawnDusk
  END IF
RETURN
  
'[Label]
DawnDusk:
  '' // <[inner circle hemispheres <(center)] '<[55/56/57]<?>[5/6/7]['t': br 1/2/3 ?]  <#['taX'/pset reduns?]#
  '' // <[spare (free) var l% ?]        ^^[cf DrawASC] ^[less black night]<?>[seasons/latitudes][dawn/dusk][moonlight?]
  '' //                                               ' [polar regions/polar Sun] <*
  IF tf$ <> "1" OR ln% = 1 THEN GOTO t: '' // --[make switch? - e.g. necessary only 1st time turned]
RETURN
t:
  '' // [i$='0' redun (2x) here (Asc&MC), but 'HorizDiagonal:' may be used in later prg development!?]
  '' // l% = 11: '<[cf. 'Tropos:'] <-[remove this line ...!!]
  DRAW "ta180": '<['normal' Asc] <[pset'd ?]
  GOSUB HorizDiagonal
  PAINT (x%, y% - 4), i%, 15
  PAINT (x%, y% + 4), il%, 15
IF ln% <> 1 THEN '' // --[1st -> --??--label for MC]! <-temp!!: <-^[cf. SUB LEGENDprgSPECS]
  GOSUB HorizDiagonal: '' // --[horizon=ArrowASC / paint->pset?] ' <-^&blw![where go(es) the color(s) ??] <-['pset' yields default !]
  i$ = "0": CALL ArrowASC(i$, i%): '' // --[g$ ??] [+ draw 'br2'?]
  PSET (x%, y%): DRAW "ta0": '' // --[pset=c15 !??] --['ta0'<-not 180]!
  DRAW "ta" + mcv$
  GOSUB HorizDiagonal
  i$ = "0": CALL ArrowMC(i$, i%)
  :
  CIRCLE (x%, y%), 6, 0: '' // --[radius=6 ?] --['fractal' Tropos]
  PAINT (x%, y% + 3), L%, 0
  GOSUB CenterSunMoon
RETURN
END IF
      '' // &blw![use color-var!] <-[Resizing]
'[Label]
IfLinesDrawn:
  PSET (x%, y%)
  DRAW "ta0": '' // --[pset=c15 !??] <-['ta0'<-not 180]!
  DRAW "ta" + mcv$
  GOSUB HorizDiagonal
  IF tf$ <> "1" THEN
    PSET (x%, y%)
    DRAW "c0"
    DRAW "bl3 l3"'' // --[Asc] ' --['pset' redun after 'paint' ??]
    PSET (x%, y%)
    DRAW "ta0"
    DRAW "ta" + mcv$
    DRAW "br3 r3"
  END IF
  CIRCLE (x%, y%), 2, L%
  PAINT (x%, y%), L%, L%
RETplusasplines:
RETURN
'' // Tropos: ['Tropos:' drawn last (just before Menu)]
'' // ''''''' [due to color leaks <(?)]--[cf. 'MainDraw:']
'' // ''''''''[imperfect circles <(?)]
'' // ''''''''[grad-lines]-[?]

HorizDiagonal:
 PSET (x%, y%): '<[redun?] <-(cf. 'DrawAsc:[Outer:]' & 'DawnDusk:[t:]')
 IF ln% = 0 THEN DRAW "l56": PSET (x%, y%): DRAW "r57": '[pa%+1 (56+1) ?] <[use vars!]
 IF ln% = 1 THEN DRAW "l" + STR$(z%): PSET (x%, y%): DRAW "r" + STR$(z%): '[(z%+1) ?]
RETURN: '>DawnDusk:[t:]

CenterSunMoon:
 PSET (x%, y%): DRAW "ta0":
 DRAW "ta" + sv$: DRAW "br50"
 PSET STEP(0, 0), 0
 CIRCLE STEP(0, 0), 2, 0
 PAINT STEP(0, 1), 14, 0
 :
 PSET (x%, y%): DRAW "ta0":
 DRAW "ta" + mv$: DRAW "br50"
 CIRCLE STEP(0, 0), 2, 0
 PAINT STEP(0, 1), 7, 0
RETURN: '>DawnDusk:[t:]

'[Label]
DrawMC: ' ///
  ' :FOR l%=1 TO 10
  ' :CIRCLE (X%,Y%),P1%-l%,,V,V+((2*PI)/360)
  ' :IF V <  PI  THEN CIRCLE (X%,Y%),P1%-l%,,(V+PI),(V+PI)+((2*PI)/360)
  ' :IF V >= PI  THEN CIRCLE (X%,Y%),P1%-l%,,(V-PI),(V-PI)+((2*PI)/360)
  ' NEXT l%
 : IF MI$ = CHR$(13) THEN GOTO L61160
 DRAW "bl57 l110": PSET (x%, y%): DRAW "br57 r110": GOTO L61190: ' >[110]?
L61160:
 DRAW "bl57 l110 l12": PSET (x%, y%): DRAW "br57 r110 r12 br41 r9"
 ' ' IF tf$ <> "1" THEN DRAW "c" + STR$(i%):  '<[i% retained fm 'DrawAsc:']
L61190:
 CALL ArrowMC(i$, i%)
RETURN: '>axes


' SU&MO: [SUBs w/ arg sv$ ?]<->[or args & alternate colors/drawings in 'Select Case' loop in 'PlanetSymbols:' ??]
' Memo:  [E c l i p s e s !]

MO: DRAW "c0": '-----------------MO-----|''''|''''|''^'|''''|''''|:rem <[phases!]
 DRAW "br10 r5 br10              bd1": '|          *****          '
 DRAW "bl6 l4 bl5 l4 bl6         bd1": '|      ****     ****      '
 DRAW "br3 r3 br4 r1 br8 r3 br3  bd1": '|   ***    *        ***   '
 DRAW "bl2 l2 bl8 l2 bl7 l2 bl2  bd1": '|  **       **        **  '
 DRAW "br1 r2 br10 r1 br8 r2 br1 bd1": '| **          *        ** '
 DRAW "l1 bl9 l1 bl13 l1         bd1": '|*             *         *'
 DRAW "r1 br14 r1 br8 r1         bd1": '-*              *        *'
 DRAW "l1 bl9 l1 bl13 l1         bd1": '|*             *         *'
 DRAW "br1 r2 br10 r1 br8 r2 br1 bd1": '| **          *        ** '
 DRAW "bl2 l2 bl8 l2 bl7 l2 bl2  bd1": '|  **       **        **  '
 DRAW "br3 r3 br4 r1 br8 r3 br3  bd1": '|   ***    *        ***   '
 DRAW "bl6 l4 bl5 l4 bl6         bd1": '|      ****     ****      '
 DRAW "br10 r5                      ": '|          *****          '<[bu 3]:?:[bl 6]
 DRAW "bu3": '---------------------------
IF tf$ <> "1" THEN GOTO TurnedMO
 i% = 14: IF VAL(sv$) < 180 THEN i% = 7: '' // <[7=daytime!] <[fading/graduated colors?]
 '' //                                   '' // [sv$ <(Sun's radix 'ta' assigned in 'InMainDraw:']
 PAINT STEP(0, 0), i%, 0: '' // <[cf SUN] -- <[cf. DrawAsc+DawnDusk]  [i% free ?]<->(SUBlocal?)]
TurnedMO:
 DRAW "bl6": PAINT STEP(0, 0), 0, 0
 RETURN
 ' [var$=phase <-[aspSU-MO]!?] <(eclipses?)
 ' ^^[MO1,MO2,MO3,MO4 ?] <-(Quarters) <- (mirror images/bitmaps ??)
 ' ^^[gibbous, 'first sight' (visual), etc. ??]

'-->
'mmmmmmmm
Irregular:
locate xloc%+10,10: print "IRREGULAR": stop
: '' ---loc!?---[autoexec.bat: 'break=off' !?]
: '' ---cls!?
: LOCATE xloc%, 40: PRINT "[tie]  'A' is started with '<a> <CR>' in base directory!"
: locate xloc%, 42: print "<key>";
: in$ = INPUT$(1)
'' '' [input$(1)]
'' '' [DO UNTIL INKEY$ <> "": LOOP]
: CLEAR
: SYSTEM
:
: '[-> astrap.bat -> a.bat (erase switches, etc.) -> end]
'mmmmmmmm
END: '<[redunexit]
'#<--

'---------
'A_QB_DRAW.BAS

'---'
SUB aqu : ' ' DRAW "c3": '-------------aqu----|''''|''''|''^'|''''|''''|
 DRAW "br4 r2 br6 r2 br3               bd1": '|    **      **
 DRAW "bl1 l2 bl2 l2 bl2 l2 bl2 l2 bl2 bd1": '|  **  **  **  **
 DRAW "r2 br6 r2 br6 r1                bd1": '|**      **      *
 DRAW "bl17                            bd1": '|
 DRAW "br4 r2 br6 r2 br3               bd1": '-    **      **
 DRAW "bl1 l2 bl2 l2 bl2 l2 bl2 l2 bl2 bd1": '|  **  **  **  **
 DRAW "r2 br6 r2 br6 r1                   ": '|**      **      *
 : : :                                    : '|
 : : :                                    : '|
END SUB

SUB ari :  ' ' DRAW "c3": '------------ari----|''''|''''|''^'|''''|''''|
 DRAW "r5 br15 r5                      bd1": '|*****               *****
 DRAW "l2 bl3 l2 bl11 l2 bl3 l2        bd1": '|**   **           **   **
 DRAW "br1 r2 br3 r2 br9 r2 br3 r2 br1 bd1": '| **   **         **   **
 DRAW "bl7 l2 bl7 l2 bl7               bd1": '|       **       **
 DRAW "br8 r2 br5 r2 br8               bd1": '-       **     **
 DRAW "bl9 l2 bl3 l2 bl9               bd1": '|         **   **
 DRAW "br10 r2 br1 r2 br10             bd1": '|          ** **
 DRAW "bl11 l3 bl11                    bd1": '|           ***
 DRAW "br11 r3 br11                    bd1": '|           ***
END SUB

SUB ArrowASC (i$, i%) : '-------|''''|''''|''^'|''''|''''|
: : :                        : '|
: : :                        : '|
DRAW "u3                    ": '|
DRAW "r5 br3             bd1": '|     *****
DRAW "l8                 bd1": '|     ********
DRAW "r11 br4            bd1": '|     ***********
DRAW "l15                bd1": '-     ***************
DRAW "r11 br4            bd1": '|     ***********
DRAW "bl7 l8             bd1": '|     ********
DRAW "r5                    ": '|     *****
: : :                        : '|
: : :                        : '|
: : :                        : '|
'--------------------------------
DRAW "bu3"
IF VAL(i$) > 1 THEN CIRCLE STEP(0, 0), 2, i%: PAINT STEP(0, 0), i%, i%: '15: '<[no pset'd !?]
DRAW "bl5"
'' // ^[colored inside when turned!] ^
'' // ^['c15'=default]               ^
DRAW "bl150 bd10            ": '|
'' //  ^^  ^[150/10 <-dum!]^[u/bu ?]^
'' // ['step' for 'paint' hemispheres]
'' // [USE VARS! <(not dums)]       ^
'' // [^for (re)size of chartdraws]  ^
'' // [^cf. label SizeConstants:     ^
END SUB: '-----------------------

SUB ArrowMC (i$, i%) : '--------|''''|''''|''^'|''''|''''|
: : :                        : '|
: : :                        : '|
DRAW "u3                    ": '|
DRAW "r5 br3             bd1": '|     *****
DRAW "l3 bl4 l1          bd1": '|     *oooo***
DRAW "r1 br7 r3 br4      bd1": '|     *ooooooo***
DRAW "l5 bl9 l1          bd1": '-     *oooooooo*****
DRAW "r1 br7 r3          bd1": '|     *ooooooo***
DRAW "bl3 l3 bl4 l1      bd1": '|     *oooo***
DRAW "r5                    ": '|     *****
: : :                        : '|
: : :                        : '|
: : :                        : '|
'--------------------------------
IF VAL(i$) > 1 THEN DRAW "c" + STR$(i%): DRAW "bu1 l4 u4 r3 d3 l2 u2 r1 d2 r2 u2 r1 d2 r1 u2 d1 r1"
'' // ^[colored inside when turned!]
END SUB: '-----------------------

SUB can : '------------------can----|''''|''''|''^'|''''|''''|
 DRAW "r20                  bd1": '|********************
 DRAW "l2 bl10 l1 bl6 l1    bd1": '|*      *          **
 DRAW "r1 br7 r1 br8 r2 br1 bd1": '|*       *        **
 DRAW "bl11 l9              bd1": '|*********
 DRAW "br20                 bd1": '-
 DRAW "l9 bl11              bd1": '|           *********
 DRAW "br1 r2 br8 r2 br7 r1 bd1": '| **        *       *
 DRAW "l1 bl6 l1 bl10 l2    bd1": '|**          *      *
 DRAW "r20                  bd1": '|********************
END SUB

SUB cap : '----------------------cap----|''''|''''|''^'|''''|''''|
 DRAW "br9 r5 br3               bd1": '|          *****
 DRAW "bl2 l2 bl3 l2 bl5 l2 l1  bd1": '|  **     **   **
 DRAW "br2 r2 br5 r2 br1 r2 br3 bd1": '|   **     ** **
 DRAW "bl3 l3 bl6 l2 bl3        bd1": '|    **      ***
 DRAW "br4 r2 br4 r2 br2 r2 br1 bd1": '-     **    **  **
 DRAW "l2 bl4 l2 bl2 l2 bl5     bd1": '|      **  **    **
 DRAW "br7 r3 br3 r2               ": '|        ***   **
 : : :                             : '|
 : : :                             : '|
END SUB

SUB DerivedMsgText
 '' //  Use dialog-input at start of prg to decide if msg-boxes thruout is wanted by user?! <-(boxes can be ESCed)
 ' ---
 '' // [Derived-derived-derived-... must be calculated mentally. ] '<-[per now, as prg is]
 '' // [Ex: You are turned to derived House 4 (from radix=Cyc 1).] '<-[msg-box with description ?]
 '' // [--  You get to derived 7 from derived 4 by 4+7=11        ] '  [- that can be chosen/esc'd]
 '' // [--  You press 't' and give '11' in dialog                ] '
 '' // [--  As prg stands, you must remember where you are!      ] '  [etc. ...]
 '
 '' //  <[Would a choice dialog + databox have any end?     ]
 '' // [ex: derived 7 fm derived 4 from radix (Cyc 4 <- 1)]
 '' // [ex: der 11 fm der 3 fm dr 2 fm der 9 fm ...       ]
END SUB

SUB EKSEMPEL : '[float?]
' FOR X=1 TO 13
' FOR Y=1 TO 25
' RR$ = MID$(DR$(X),Y,1)
' IF RR$ = "*" THEN DRAW "r1" ELSE DRAW "br1"
' NEXT Y
' DRAW "bl25 bd1"
' NEXT X
' RETURN <*
' # [diagonaler etc. ?]
'---
' '  >?>?>?>?>?  DRAW "u7 d2 l3 r6 l3 d5 r2 e3 r2 f4 l2 g3 l3" <<-<*
'---
END SUB

SUB gem : '---------------gem----|''''|''''|''^'|''''|''''|
 DRAW "r25               bd1": '|*************************
 DRAW "l25               bd1": '|*************************
 DRAW "br6 r3 br7 r3 br6 bd1": '|      ***       ***
 DRAW "bl6 l3 bl7 l3 bl6 bd1": '|      ***       ***
 DRAW "br6 r3 br7 r3 br6 bd1": '-      ***       ***
 DRAW "bl6 l3 bl7 l3 bl6 bd1": '|      ***       ***
 DRAW "br6 r3 br7 r3 br6 bd1": '|      ***       ***
 DRAW "l25               bd1": '|*************************
 DRAW "r25               bd1": '|*************************
END SUB

SUB JU : DRAW "c0": '------JU-----|''''|''''|''^'|''''|''''|
 DRAW "br25               bd1": '|
 DRAW "bl19 l2 bl4        bd1": '|    **
 DRAW "br6 r2 br17        bd1": '|      **
 DRAW "bl15 l2 bl8        bd1": '|        **
 DRAW "br9 r2 br14        bd1": '|         **
 DRAW "bl14 l1 bl10       bd1": '|          *
 DRAW "br10 r1 br8 r1 br5 bd1": '-          *        *
 DRAW "bl5 l1 bl8 l1 bl10 bd1": '|          *        *
 DRAW "br11 r11 br3       bd1": '|           ***********
 DRAW "bl5 l1 bl19        bd1": '|                   *
 DRAW "br19 r1 br5        bd1": '|                   *
 DRAW "bl5 l1 bl19        bd1": '|                   *
 DRAW "br19 r1 br5           ": '|                   *
END SUB

SUB leo : '------------------leo----|''''|''''|''^'|''''|''''|
 DRAW "r17                  bd1": '|      ***
 DRAW "l17                  bd1": '|     *   **
 DRAW "r17                  bd1": '|    *     **
 DRAW "l17                  bd1": '|   *       **
 DRAW "r17                  bd1": '-***         **  *
 DRAW "l17                  bd1": '|* *          ** *
 DRAW "r17                  bd1": '|***           **
 : : :                         : '|
 : : :                         : '|
END SUB

SUB lib : '---------------lib----|''''|''''|''^'|''''|''''|
 DRAW "br17              bd1": '|
 DRAW "bl7 l3 bl7        bd1": '|        ***
 DRAW "br4 r2 br5 r2 br4 bd1": '|     **     **
 DRAW "l5 bl7 l5         bd1": '| *****       *****
 DRAW "br17              bd1": '-
 DRAW "l8 bl1 l8            ": '| ******** ********
 : : :                      : '|
 : : :                      : '|
 : : :                      : '|
END SUB

SUB LineSpaces (xloc%, L$)
 LOCATE xloc%, 1: PRINT SPC(79); L$;
 ' <-[locate again ? (xloc%,3) -?-]
END SUB

SUB MA : DRAW "c0": '------MA-----|''''|''''|''^'|''''|''''|
 DRAW "br12 r10 br3       bd1": '|            **********
 DRAW "bl2 l2 bl1 l1 bl19 bd1": '|                   * **
 DRAW "br17 r1 br4 r2 br1 bd1": '|                 *    **
 DRAW "l2 bl6 l1 bl16     bd1": '|                *      **
 DRAW "br14 r1 br10       bd1": '|              *
 DRAW "bl11 l1 bl13       bd1": '|             *
 DRAW "br6 r13 br6        bd1": '-      *************
 DRAW "bl5 l1 bl13 l1 bl5 bd1": '|     *             *
 DRAW "br4 r1 br15 r1 br4 bd1": '|    *               *
 DRAW "bl3 l1 bl17 l1 bl3 bd1": '|   *                 *
 DRAW "br4 r1 br15 r1 br4 bd1": '|    *               *
 DRAW "bl5 l1 bl13 l1 bl5 bd1": '|     *             *
 DRAW "br6 r13 br6           ": '|      *************
 '  [why br6 ?]^
END SUB

'xx: draw "c0": '-rem-rem--xx-----|!!!!|!!!!|!!^!|!!!!|!!!!|:rem <[nil'd!]
'DRAW "br25                bd1": '|                         '
'DRAW "bl8 l17             bd1": '|  *****************      '
'DRAW "br4 r1 br12 r1 br7  bd1": '|      *            *     '
'DRAW "bl5 l1 bl13 l1 bl5  bd1": '|       *             *   '
'DRAW "br7 r1 br13 r1 br3  bd1": '|         *             * '
'DRAW "bl2 l1 bl12 l1 bl9  bd1": '|           *            *'
'DRAW "br10 r1 br12 r1 br1 bd1": '-           *            *'
'DRAW "bl2 l1 bl12 l1 bl9  bd1": '|           *            *'
'DRAW "br7 r1 br13 r1 br3  bd1": '|         *             * '
'DRAW "bl5 l1 bl13 l1 bl5  bd1": '|       *             *   '
'DRAW "br4 r1 br12 r1 br7  bd1": '|      *            *     '
'DRAW "bl8 l17            bd1":  '|  *****************      '
': : :                         : '|                         '
'RETURN
SUB ME : DRAW "c0": '------ME-----|''''|''''|''^'|''''|''''|
 DRAW "br4 r4 br9 r4 br4  bd1": '|    ****         ****
 DRAW "bl4 l4 bl9 l4 bl4  bd1": '|    ****         ****
 DRAW "br5 r4 br7 r4 br5  bd1": '|     ****       ****
 DRAW "bl5 l15 bl5        bd1": '|     ***************
 DRAW "br3 r4 br11 r4 br3 bd1": '|   ****           ****
 DRAW "bl2 l4 bl13 l4 l2  bd1": '|  ****             ****
 DRAW "br3 r4 br11 r4 br3 bd1": '-   ****           ****
 DRAW "bl6 l13 bl6        bd1": '|      *************
 DRAW "br11 r3 br11       bd1": '|           ***
 DRAW "bl11 l3 bl11       bd1": '|           ***
 DRAW "br8 r9 br8         bd1": '|        *********
 DRAW "bl11 l3 bl11       bd1": '|           ***
 DRAW "br11 r3 br11          ": '|           ***
END SUB

SUB NE : DRAW "c8": '------------NE-----|''''|''''|''^'|''''|''''|
 DRAW "br25                     bd1": '|
 DRAW "bl1 l1 bl19 l2 bl1       bd1": '| **                   **
 DRAW "br2 r2 br8 r1 br8 r2 br2 bd1": '|  **        *        **
 DRAW "bl3 l2 bl7 l1 bl7 l2 bl3 bd1": '|   **       *       **
 DRAW "br3 r2 br7 r1 br7 r2 br3 bd1": '|   **       *       **
 DRAW "bl4 l2 bl6 l1 bl6 l2 bl4 bd1": '|    **      *      **
 DRAW "br6 r13 br6              bd1": '-      *************
 DRAW "bl12 l1 bl12             bd1": '|            *
 DRAW "br12 r1 br12             bd1": '|            *
 DRAW "bl12 l1 bl12             bd1": '|            *
 DRAW "br8 r9 br8               bd1": '|        *********
 DRAW "bl12 l1 bl12             bd1": '|            *
 DRAW "br12 r1 br12                ": '|            *
END SUB

SUB PL : DRAW "c8": '------PL-----|''''|''''|''^'|''''|''''|
 DRAW "br25               bd1": '|
 DRAW "bl8 l12 bl5        bd1": '|     ************
 DRAW "br4 r2 br11 r2 br6 bd1": '|    **           **
 DRAW "bl5 l2 bl12 l2 bl4 bd1": '|    **            **
 DRAW "br4 r2 br12 r2 br5 bd1": '|    **            **
 DRAW "bl6 l2 bl11 l2 bl4 bd1": '|    **           **
 DRAW "br4 r13 br8        bd1": '-    *************
 DRAW "bl19 l2 bl4        bd1": '|    **
 DRAW "br4 r2 br19        bd1": '|    **
 DRAW "bl5 l2 bl12 l2 bl4 bd1": '|    **            **
 DRAW "br4 r2 br12 r2 br5 bd1": '|    **            **
 DRAW "bl6 l15 bl4        bd1": '|    ***************
 DRAW "br25               bd1": '|
END SUB

SUB psc : '---------------psc----|''''|''''|''^'|''''|''''|
 DRAW "r3 br11 r3        bd1": '| ***           ***
 DRAW "bl2 l2 bl9 l2 bl2 bd1": '|   **         **
 DRAW "br3 r2 br7 r2 br3 bd1": '|    **       **
 DRAW "bl4 l9 bl4        bd1": '|     *********
 DRAW "br3 r2 br7 r2 br3 bd1": '-    **       **
 DRAW "bl2 l2 bl9 l2 bl2 bd1": '|   **         **
 DRAW "r3 br11 r3           ": '| ***           ***
 : : :                      : '|
 : : :                      : '|
END SUB

SUB sag : '---------------sag----|''''|''''|''^'|''''|''''|
 DRAW "br4 r8 br5        bd1": '|     ********
 DRAW "bl4 l1 bl2 l2 bl8 bd1": '|         **  *
 DRAW "br7 r2 br3 r1 br4 bd1": '|        **   *
 DRAW "bl9 l2 bl6        bd1": '|       **
 DRAW "br2 r8 br7        bd1": '-   ********
 DRAW "bl11 l2 bl4       bd1": '|     **
 DRAW "br3 r2               ": '|    **
 : : :                      : '|
 : : :                      : '|
END SUB

SUB SA : DRAW "c0": '-----------SA-----|''''|''''|''^'|''''|''''|
 DRAW "br5 r1 br19              bd1": '|     *
 DRAW "bl19 l1 bl5              bd1": '|     *
 DRAW "br1 r9 br15              bd1": '| *********
 DRAW "bl19 l1 bl5              bd1": '|     *
 DRAW "br5 r1 br5 r4 br10       bd1": '|     *     ****
 DRAW "bl7 l2 bl5 l2 bl3 l1 bl5 bd1": '|     *   **     **
 DRAW "br5 r1 br2 r2 br8 r2 br5 bd1": '-     *  **        **
 DRAW "bl5 l2 bl10 l3 bl5       bd1": '|     ***          **
 DRAW "br17 r2 br6              bd1": '|                 **
 DRAW "bl8 l2 bl15              bd1": '|               **
 DRAW "br13 r2 br10             bd1": '|             **
 DRAW "bl12 l2 bl11             bd1": '|           **
 DRAW "br12 r2 br11                ": '|            **
END SUB

SUB sco : '------------------------------------sco----|''''|''''|''^'|''''|''''|
 DRAW "br2 r8 br7                             bd1": '|   ********
 DRAW "bl1 l1 bl5 l1 bl2 l1 bl2 l1 bl1 l1 bl1 bd1": '| * *  *  *    **
 DRAW "r1 br2 r1 br2 r1 br2 r1 br2 r2 br1 r2  bd1": '| *  *  *  *  ** **
 DRAW "bl3 l1 bl3 l1 bl2 l1 bl2 l1 bl2 l1     bd1": '| *  *  *  *   *
 DRAW "r1 br2 r1 br2 r1 br2 r1 br2 r1 br4     bd1": '- *  *  *  *  *
 DRAW "bl5 l1 bl1 l1 bl2 l1 bl2 l1 bl3        bd1": '|    *  *  * *
 DRAW "br3 r1 br5 r2                             ": '|    *     **
 : : :                                           : '|
 : : :                                           : '|
END SUB

SUB SUN (tf$) : DRAW "c0": '------|''''|''''|''^'|''''|''''|
 DRAW "br10 r5 br10       bd1": '|          *****          '
 DRAW "bl6 l4 bl5 l4 bl6  bd1": '|      ****     ****      '
 DRAW "br3 r3 br13 r3 br3 bd1": '|   ***             ***   '
 DRAW "bl2 l2 bl17 l2 bl2 bd1": '|  **                 **  '
 DRAW "br1 r2 br19 r2 br1 bd1": '| **                   ** '
 DRAW "l1 bl23 l1         bd1": '|*                       *'
 DRAW "r1 br11 r1 br11 r1 bd1": '-*           *           *'
 DRAW "l1 bl23 l1         bd1": '|*                       *'
 DRAW "br1 r2 br19 r2 br1 bd1": '| **                   ** '
 DRAW "bl2 l2 bl17 l2 bl2 bd1": '|  **                 **  '
 DRAW "br3 r3 br13 r3 br3 bd1": '|   ***             ***   '
 DRAW "bl6 l4 bl5 l4 bl6  bd1": '|      ****     ****      '
 DRAW "br10 r5               ": '|          *****          '<[bu 10?]
 DRAW "bu10": '-------------------
IF tf$ <> "1" THEN GOTO TurnedSu
 i% = 14
 '' // # [IF VAL(sv$) < 180 THEN i% = ?: '<[?=???!] <[eclipse? (colors)]
 '' // ['sv$' <(Sun's radix 'ta' assigned in 'InMainDraw:']
 PAINT STEP(0, 0), i%, 0: '<[cf. MO]
TurnedSu:
'RETURN
END SUB

SUB tau : '----------------tau----|''''|''''|''^'|''''|''''|
 DRAW "br3 r3 br13 r3 br3 bd1": '|   ***             ***
 DRAW "bl4 l3 bl11 l3 bl4 bd1": '|    ***           ***
 DRAW "br5 r3 br9 r3 br5  bd1": '|     ***         ***
 DRAW "bl6 l3 bl7 l3 bl6  bd1": '|      ***       ***
 DRAW "br1 r23 br1        bd1": '-  *********************
 DRAW "bl1 l2 bl19 l2 bl1 bd1": '| **                   **
 DRAW "r2 br21 r2         bd1": '|**                     **
 DRAW "bl1 l2 bl19 l2 bl1 bd1": '| **                   **
 DRAW "br2 r21 br2        bd1": '|  *********************
END SUB

SUB UR : DRAW "c8": '------------UR-----|''''|''''|''^'|''''|''''|
 DRAW "br25                     bd1": '|
 DRAW "bl3 l2 bl15 l2 bl3       bd1": '|   **               **
 DRAW "br4 r2 br6 r1 br6 r2 br4 bd1": '|    **      *      **
 DRAW "bl6 l1 bl5 l1 bl5 l1 bl6 bd1": '|      *     *     *
 DRAW "br7 r11 br7              bd1": '|       ***********
 DRAW "bl6 l1 bl5 l1 bl5 l1 bl6 bd1": '|      *     *     *
 DRAW "br4 r2 br6 r1 br6 r2 br4 bd1": '-    **      *      **
 DRAW "bl3 l2 bl15 l2 bl3       bd1": '|   **       *       **
 DRAW "br12 r1 br 12            bd1": '|            *
 DRAW "bl11 l3 bl11             bd1": '|           ***
 DRAW "br10 r1 br3 r1 br10      bd1": '|          *   *
 DRAW "bl11 l3 bl11             bd1": '|           ***
 DRAW "br25                        ": '|
END SUB

SUB VE : DRAW "c0": '------VE-----|''''|''''|''^'|''''|''''|
 DRAW "br6 r13 br6 bd1       ": '|      *************
 DRAW "bl5 l1 bl13 l1 bl5 bd1": '|     *             *
 DRAW "br4 r1 br15 r1 br4 bd1": '|    *               *
 DRAW "bl3 l1 bl17 l1 bl3 bd1": '|   *                 *
 DRAW "br4 r1 br15 r1 br4 bd1": '|    *               *
 DRAW "bl5 l1 bl13 l1 bl5 bd1": '|     *             *
 DRAW "br6 r13 br6        bd1": '-      *************
 DRAW "bl12 l1 bl12       bd1": '|            *
 DRAW "br12 r1 br12       bd1": '|            *
 DRAW "bl12 l1 bl12       bd1": '|            *
 DRAW "br9 r7 br9         bd1": '|         *******
 DRAW "bl12 l1 bl12       bd1": '|            *
 DRAW "br12 r1 br12          ": '|            *
END SUB

SUB vir : '--------------------------------vir----|''''|''''|''^'|''''|''''|
 DRAW "br2 r5 br1 r9                      bd1": '|   ***** *********
 DRAW "l1 bl4 l1 bl3 l1 bl3 l1 bl1 l1 bl1 bd1": '|  * *   *   *    *
 DRAW "r1 br2 r1 br3 r1 br3 r1 br2 r1 br2 bd1": '| *  *   *   *  *
 DRAW "bl4 l2 bl3 l1 bl3 l1 bl2 l1        bd1": '| *  *   *   **
 DRAW "r1 br2 r1 br3 r1 br2 r2 br5        bd1": '- *  *   *  **
 DRAW "bl5 l1 bl1 l1 bl1 l1 bl3 l1 bl3    bd1": '|    *   * * *
 DRAW "br3 r1 br3 r1 br2 r2                  ": '|    *   *  **
 : : :                                       : '|
 : : :                                       : '|
END SUB

'---'
' aqDRAW.BAS
'---'
