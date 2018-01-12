rem ###############################################################
rem # Ref: https://cauldronofartandcraft.wordpress.com/chartdraw/ #
rem ###############################################################
rem ---
rem Oct 31 2011
rem -----------

rem echo off
rem erase existing or --seqx.swi --slow--
rem erase \aqCHARTS\aq_temp\*

copy MASTER.MAS switch.sw0 /Y
copy CHOICE.MAS choice.sw0 /Y
dir *. > catdirs.ms

rem rem --menu--here--
bin\qbasic /run aqTIE.BAS

rem erase catdirs.*
rem erase *.swi -----
rem erase *.sw0
rem erase \identity.tie
rem erase \aqCHARTS\aq_temp\*
