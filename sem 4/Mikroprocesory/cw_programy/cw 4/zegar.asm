LED EQU P1.7
;********* Ustawienie TIMERów *********

;TIMER 0
T0_G EQU 0 ;GATE
T0_C EQU 0 ;COUNTER/-TIMER
T0_M EQU 1 ;MODE (0..3)
TIM0 EQU T0_M+T0_C*4+T0_G*8

;TIMER 1
T1_G EQU 0 ;GATE
T1_C EQU 0 ;COUNTER/-TIMER
T1_M EQU 1 ;MODE (0..3)
TIM1 EQU T1_M+T1_C*4+T1_G*8
TMOD_SET EQU TIM0+TIM1*16

;50[ms] = 50 000[ŠS]*(11.0592[MHz]/12) =
; = 46 080 cykli = 180 * 256
TH0_SET EQU 256-180
TL0_SET EQU 0

TH1_SET EQU 256-180
TL1_SET EQU 0

;==================================
	LJMP	START
	ORG	100H
START:
	LCALL LCD_CLR
	
; wprowadzanie godziny
	LCALL WPROWADZ
	MOV R7, A ; godziny - zegar
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	LCALL WPROWADZ
	MOV R6, A ; minuty - zegar
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	LCALL WPROWADZ
	MOV R5, A ; sekundy - zegar
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	MOV A, #' '
	LCALL WRITE_DATA

;Wprowadzenie godziny, w ktorej wystapi alarm
	LCALL WPROWADZ;godziny - alarmu
	MOV 13H, A
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	LCALL WPROWADZ;minuty - alarmu
	MOV 12H, A
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	MOV A, #' '
	LCALL WRITE_DATA
	
; wprowadzanie czasu trwania alarmu
	LCALL WPROWADZ;sekundy - alarm
	MOV 14H, A
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	MOV A, #10	
	LCALL DELAY_100MS

; config
	MOV TMOD,#TMOD_SET ;Timer 0 liczy czas
	MOV TH0,#TH0_SET ;Timer 0 na 50ms
	MOV TL0,#TL0_SET
	SETB TR0 ; start timera
	
PREPARE:
	MOV A, R5 ; obecne sekundy
	
	ADD A, #1 ; inkrementacja
	MOV B, #60
	DIV AB ; sekundy % 60
	MOV R5, B ; aktualizacja sekund
	
	ADD A, R6 ; inkrementacja minut?
	MOV B, #60
	DIV AB
	MOV R6, B ; aktualizacja minut
	
	ADD A, R7 ; inkrementacja godzin?
	MOV B, #24
	DIV AB
	MOV R7, B ; aktualizacja godzin
	
	LCALL WRITE_HOUR
	
; porównywanie alarmu
	MOV A, R7
	CJNE A, 13H, RESET_FLAG ; porównanie godzin
 
	MOV A, R6

	CJNE A, 12H, RESET_FLAG ; porównanie minut
	
	MOV A, 10H ; flaga alarmu
	JNZ SKIP
	MOV 10H, #1 ; flaga alarmu = 1
	MOV 11H, 14H ; czas alarmu
	CLR LED
	SJMP SKIP

RESET_FLAG:
	MOV A, #11H
	JNZ SKIP ; jeśli trwa odliczanie nie resetuj
	MOV 10H, #0
	
SKIP:	
	MOV R4, #20
	MOV A, 11H
	JNZ DECREMENT
	SETB LED
	LJMP TIME_LOOP
DECREMENT:
	DEC 11H
	
TIME_LOOP:
	JNB TF0, TIME_LOOP ; odczekaj 50ms
	MOV TH0, #TH0_SET ; ustaw timer ponownie
	CLR TF0 ; zerowanie flagi timera 0
	DJNZ R4, TIME_LOOP ; 20x50ms
	LJMP PREPARE

STOP:
	LJMP	STOP
	NOP

TO_BCD:
	;ZAMIANA NA BCD -POCZĄTEK
	MOV B,#10; DZIELNIK
	DIV AB; WYDZIELAMY CYFRE DZIESIATEK
	SWAP A; PRZESUWAMY CYFRĘ DZIESIĄTEK NA WYŻSZY 4 BITY
	ORL A,B; DODAJEMY CYFRĘ JEDNOŚCI
	;ZAMIANA NA BCD -KONIEC
	RET
	NOP
	
WPROWADZ:
	LCALL WAIT_KEY ; Wczytaj liczbę dziesiątek
	MOV B,#10 ; pomnóż
	MUL AB ; przez 10
	MOV R1,A ; zapisz liczbę w R1
	LCALL WAIT_KEY ;wczytaj liczbę jedności
	ADD A,R1 ; dodaj liczbę jedności do R1
	RET ; wyjdź z podprogramu. Wynik w A.

WRITE_HOUR:
	LCALL LCD_CLR
	MOV A, R7
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	MOV A, #':'
	LCALL WRITE_DATA
	
	MOV A, R6
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	MOV A, #':'
	LCALL WRITE_DATA
	
	MOV A, R5
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	RET
	