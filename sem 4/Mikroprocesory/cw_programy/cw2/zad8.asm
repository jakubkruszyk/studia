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
STOP:			;nie wykonuj innych dzia³añ
	LJMP	STOP	;- pozostañ w pêtli STOP
	NOP

