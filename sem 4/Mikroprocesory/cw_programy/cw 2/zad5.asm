	LJMP	START
	ORG	100H
START:
	; bank 0
	MOV R7, #0
	
	; bank 1
	SETB RS0
	MOV R7, #1
	
	;bank 2
	CLR RS0
	SETB RS1
	MOV R7, #2
	
	;bank 3
	SETB RS0
	MOV R7, #3
	
	; czyszczenie LCD i wypisywanie wyników
	LCALL LCD_CLR
	MOV A, 07H
	LCALL WRITE_HEX
	MOV A, 0FH
	LCALL WRITE_HEX
	MOV A, 17H
	LCALL WRITE_HEX
	MOV A, 1FH
	LCALL WRITE_HEX
STOP:			;nie wykonuj innych dzia³añ
	LJMP	STOP	;- pozostañ w pêtli STOP
	NOP

