	LJMP	START
	ORG	100H
START:
	MOV R0, #40H
	MOV A, #10
LOOP:
	MOV @R0, #0 ; wyzeruj kom�rk� pami�ci pod adresem zapisanym w R0
	INC R0 ; 
	DJNZ ACC, LOOP ; pozosta� w p�tli dop�ki A > 0
STOP:			;nie wykonuj innych dzia�a�
	LJMP	STOP	;- pozosta� w p�tli STOP
	NOP

