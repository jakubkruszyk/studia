# program pobiera kurs wybranej waluty z dowolnego dnia/ zakresu dat

from api import *

path = "table.json"

while True:
    operation = input("1 - pobierz dane i zapisz do pliku \n2 - wyświetl z pliku \n3 - wyjdź \n")
    if operation == '1':
        # pobranie danych
        currency = input("Podaj kod waluty: ").lower()
        date = input("Podaj datę(yyyy-mm-dd)/ zakres dat rozdzielone spacją: ").split(" ")
        record = get_api(currency=currency, date=date)
        if type(record) is str:
            print(record)
            continue
        file_content = get_file(path)
        currency_content = file_content.get(currency)  # jeżeli dana waluta jest w bazie pobierz jej dane
        if currency_content:
            filtered_content = [True for x in currency_content if x['date'] == date]
            if not filtered_content:  # sprawdz czy dana data była już dodana
                file_content[currency].append(record)
                # sortowanie recordów dla wygody wyswietlania
                file_content[currency] = sort_content(file_content[currency])
        else:  # nie ma danej waluty w bazie -> dodaj ją z pierwszy recordem
            file_content[currency] = [record]
        write_file(path, file_content)

    elif operation == '2':
        # pobranie danych
        currency = input("Podaj kod waluty: ").lower()
        date = input("Podaj datę(yyyy-mm-dd)/ zakres dat rozdzielone spacją ('all' drukuje wszystkie recordy): ").split(" ")
        file_content = get_file(path)
        currency_content = file_content.get(currency)
        if not currency_content:
            print("brak waluty w bazie danych")
            continue

        if len(date) == 1:  # druk konkretnej daty
            if date[0] == 'all':  # druk wszystkich danych
                for record in currency_content:
                    print(parse_data(record))
                continue

            filtered_content = [x for x in currency_content if x['date'] == date[0]]
            if filtered_content:
                print(parse_data(filtered_content[0]))
            else:
                print("brak danych z tego dnia")

        elif len(date) == 2:  # druk zakresu dat
            date1 = datetime.strptime(date[0], "%Y-%m-%d").timestamp()
            date2 = datetime.strptime(date[1], "%Y-%m-%d").timestamp()
            filtered_data = [x for x in currency_content
                             if date1 <= datetime.strptime(x['date'], "%Y-%m-%d").timestamp() <= date2]
            for record in filtered_data:
                print(parse_data(record))

        else:
            print("Zła liczba dat")

    elif operation == '3':  # koniec programu
        break

    else:
        print("Zły numer")
