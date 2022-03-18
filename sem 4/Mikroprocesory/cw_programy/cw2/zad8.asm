	LJMP	START
	ORG	100H
START:
	SETB RS0
	SETB RS1 ; ustawienie banku 3
	MOV R0, #1FH ; adres rejestru R7
	MOV ACC, #7 ; licznik do pêtli
LOOP:
	MOV @R0, ACC ; wpisanie licznika do rejestru (adresowanie poœrednie)
	DEC R0 ; zmniejszenie adresu o 1
	DJNZ ACC, LOOP ; zmniejszenie licznika o 1, jeœli licznik =/= 0 skocz do LOOP
	MOV R0, #0 ; ustaw R0 na 0
STOP:			;nie wykonuj innych dzia³añ
	LJMP	STOP	;- pozostañ w pêtli STOP
	NOP

