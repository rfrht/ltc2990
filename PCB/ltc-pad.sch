EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:ltc-pad-cache
EELAYER 27 0
EELAYER END
$Descr User 5906 4724
encoding utf-8
Sheet 1 1
Title "LTC2990 - Test board"
Date "26 apr 2015"
Rev "2"
Comp "Rodrigo A B Freire"
Comment1 "LTC2990 Test Board"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L LTC2990 U1
U 1 1 54F784E6
P 2800 1850
F 0 "U1" H 2800 1500 60  0000 C CNN
F 1 "LTC2990" H 2800 2200 60  0000 C CNN
F 2 "~" H 2800 1850 60  0000 C CNN
F 3 "~" H 2800 1850 60  0000 C CNN
	1    2800 1850
	-1   0    0    1   
$EndComp
$Comp
L CONN_5 P1
U 1 1 54F785DA
P 1700 1850
F 0 "P1" V 1650 1850 50  0000 C CNN
F 1 "CONN_5" V 1750 1850 50  0000 C CNN
F 2 "~" H 1700 1850 60  0000 C CNN
F 3 "~" H 1700 1850 60  0000 C CNN
	1    1700 1850
	-1   0    0    1   
$EndComp
$Comp
L CONN_5 P2
U 1 1 54F785F8
P 3900 1850
F 0 "P2" V 3850 1850 50  0000 C CNN
F 1 "CONN_5" V 3950 1850 50  0000 C CNN
F 2 "~" H 3900 1850 60  0000 C CNN
F 3 "~" H 3900 1850 60  0000 C CNN
	1    3900 1850
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 553D14F8
P 2250 2400
F 0 "C1" H 2250 2500 40  0000 L CNN
F 1 "0.1 µF" H 2256 2315 40  0000 L CNN
F 2 "~" H 2288 2250 30  0000 C CNN
F 3 "~" H 2250 2400 60  0000 C CNN
	1    2250 2400
	-1   0    0    1   
$EndComp
Wire Wire Line
	2100 2050 2250 2050
Wire Wire Line
	2100 1950 2250 1950
Wire Wire Line
	2100 1850 2250 1850
Wire Wire Line
	2100 1750 2250 1750
Wire Wire Line
	2100 1650 2250 1650
Wire Wire Line
	3350 2050 3500 2050
Wire Wire Line
	3350 1950 3500 1950
Wire Wire Line
	3350 1850 3500 1850
Wire Wire Line
	3350 1750 3500 1750
Wire Wire Line
	3350 1650 3500 1650
Wire Wire Line
	2250 2050 2250 2200
Wire Wire Line
	2250 2600 2800 2600
Wire Wire Line
	2800 2600 2800 1400
Wire Wire Line
	2800 1400 3350 1400
Wire Wire Line
	3350 1400 3350 1650
$EndSCHEMATC
