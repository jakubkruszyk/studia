	LJMP	START
	ORG	100H
START:

;Wczytujemy do R7 wartosc pierwszej liczby 
	
	LCALL LCD_CLR
	LCALL WAIT_KEY ;Podajemy  pierwsza liczbe
	MOV B,#10 
	MUL AB ;Liczba dziesiatek
	MOV R7,A 
	
	LCALL WAIT_KEY
	
	MOV B,R7;liczba jednosci
	ADD A,B;Dodajemy jednosci i dziesiatki
	MOV R7,A
	
	LCALL TO_BCD ; Konwersja do bcd
	LCALL WRITE_HEX;Wypisanie
	
	MOV A, #' ';Spacja
	
	LCALL WRITE_DATA; Wypisanie spacji
	
;Wczytujemy do R6 wartosc drugiej liczby
;To samo dla drugij liczby ale zapisana w R6	
	LCALL WAIT_KEY
	MOV B,#10
	MUL AB
	MOV R6,A
	
	LCALL WAIT_KEY
	
	MOV B,R6
	ADD A,B
	MOV R6,A
	
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	MOV A, #' '
	LCALL WRITE_DATA
	
;Wczytujemy znaki  operacji
;Kododwanie
; A - Dodawanie
; B - Odejmowanie
; C - Mnożenie
; D - Dzielenie


	LCALL WAIT_KEY
	
dodawanie:
	CJNE A,#10, odejmowanie ;Skok do etykiety odejmowanie jesli 
	MOV A, #'+'
	LCALL WRITE_DATA;Wypisanie znaku +
	MOV A, #'='
	LCALL WRITE_DATA;Wypisanie znaku = 
	MOV A,R7;Przypisujemy do A R7 
	ADD A,R6; Dodajemy do A R6
	LCALL TO_BCD;Konwersja do BCD
	LCALL WRITE_HEX;Wyswieltanie
	LJMP koniec
	
odejmowanie:
	CJNE A,#11, mnozenie
	MOV A, #'-'
	LCALL WRITE_DATA
	MOV A, #'='
	LCALL WRITE_DATA
	MOV A,R7
	CLR C;zerowanie flagi przeniesienia
	SUBB A,R6;Odejmowanie A 0d R6
	LCALL TO_BCD
	LCALL WRITE_HEX
	LJMP koniec
	
	
mnozenie:
	CJNE A,#12, dzielenie
	MOV A, #'*'
	LCALL WRITE_DATA
	MOV A, #'='
	LCALL WRITE_DATA
	MOV A,R7 ;
	MOV B,R6 ; wczytanie danych
	MUL AB ; mnożenie
	PUSH ACC;Dodaanie na stos wartosci ACC
	MOV A,B
	LCALL WRITE_HEX
	POP ACC;Pobieranie ze stosu wartosci ACC
	LCALL WRITE_HEX
	LJMP koniec
	
	
dzielenie:
	CJNE A,#13, koniec
	MOV A, #'/'
	LCALL WRITE_DATA
	MOV A, #'='
	LCALL WRITE_DATA
	MOV A,R7
	MOV B,R6
	PUSH B
	DIV AB;Operacja dzielenia
	PUSH B
	LCALL TO_BCD
	LCALL WRITE_HEX
	
	MOV A, #' '
	LCALL WRITE_DATA
	
	
	POP ACC
	LCALL TO_BCD
	LCALL WRITE_HEX;Wyswietlanie reszty
	
	MOV A, #'/'
	LCALL WRITE_DATA
	
	POP ACC
	LCALL TO_BCD
	LCALL WRITE_HEX;Wysiwetlanie dzielnika
	LJMP koniec
	
	
koniec:
	LCALL WAIT_KEY
	CJNE A,#0EH, STOP
	LJMP START
	
	
STOP:
	MOV A,#'-'
	LCALL WRITE_DATA
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
