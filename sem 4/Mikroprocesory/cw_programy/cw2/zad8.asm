	LJMP	START
	ORG	100H
START:
	SETB RS0
	SETB RS1 ; ustawienie banku 3
	MOV R0, #1FH ; adres rejestru R7
	MOV ACC, #7 ; licznik do p�tli
LOOP:
	MOV @R0, ACC ; wpisanie licznika do rejestru (adresowanie po�rednie)
	DEC R0 ; zmniejszenie adresu o 1
	DJNZ ACC, LOOP ; zmniejszenie licznika o 1, je�li licznik =/= 0 skocz do LOOP
	MOV R0, #0 ; ustaw R0 na 0
STOP:			;nie wykonuj innych dzia�a�
	LJMP	STOP	;- pozosta� w p�tli STOP
	NOP

