	LJMP	START
	ORG	100H
START:
	MOV R0, #40H
	MOV A, #10
LOOP:
	MOV @R0, #0 ; wyzeruj komórkê pamiêci pod adresem zapisanym w R0
	INC R0 ; 
	DJNZ ACC, LOOP ; pozostañ w pêtli dopóki A > 0
STOP:			;nie wykonuj innych dzia³añ
	LJMP	STOP	;- pozostañ w pêtli STOP
	NOP

