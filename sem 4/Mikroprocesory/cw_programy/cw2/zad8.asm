	LJMP	START
	ORG	100H
START:
	SETB RS0
	SETB RS1
	MOV R0, #20H
	MOV ACC, #7
LOOP:
	DEC R0
	MOV @R0, ACC
	DJNZ ACC, LOOP
	MOV R0, #0
STOP:			;nie wykonuj innych dzia�a�
	LJMP	STOP	;- pozosta� w p�tli STOP
	NOP

