# program pobiera kurs wybranej waluty z dowolnego dnia/ zakresu dat

from api import *

path = "table.json"

# pobranie danych
currency = input("Podaj kod waluty: ").lower()
date = input("Podaj datę/ zakres dat rozdzielone spacją: ").split(" ")

record = get_api(currency=currency, date=date)
record2 = get_api(currency=currency, date=date, table=True)
record3 = get_api(currency=currency, date=['2022-03-01', '2022-03-30'])
print(1)
