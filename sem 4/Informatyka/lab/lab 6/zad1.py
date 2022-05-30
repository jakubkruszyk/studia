# zrobić wykres np temperatury od daty
# matplotlib
# dane api --> dowolne, wybrac sb
# dzialanie:
# 1. odpalenie programu: pobieranie danych(miejsce - miasto/koordynaty,
#                                           daty - opcjonalnie, request, odpowiedz zapis do pliku)
# zwrócić uwagęna duplikaty, chronologia, całość w pętli 1-kontunuuj, 2-wizualizacja, 3-wyjscie

from web import get_data
from database import read_database, write_database
from plot import plot_data

AUTH_KEY = "ffb77367178d4d3a864113735221904"
DATABASE_PATH = "database.txt"

while True:
    print("Wybierz opcję:\n1 - pobierz dane\n2 - wyświetl dane\n3 - wyjdź")
    option = input()
    if option == "1":  # make request and save data
        # request part =================================================================================================
        localization = input("Podaj nazwę miasta lub długość i szerokość geograficzną rozdzielone spacją:\n")
        localization = localization.replace(",", '.').split(" ")
        response = get_data(localization, key=AUTH_KEY)
        # response parsing
        if response.get("error") is not None:
            print(response["error"])
            break

        city = response['location']['name']
        response_parsed = {
            'localization': (response['location']['lat'], response['location']['lon']),
            'records': [{'date': response['forecast']['forecastday'][0]['date'],
                        'data': [{'hour': record['time'].split(" ")[-1], 'temp': record['temp_c']}
                                 for record in response['forecast']['forecastday'][0]['hour']
                                 ]
                         }]
        }

        # file part ====================================================================================================
        file_content = read_database(DATABASE_PATH)
        if file_content.get(city) is None:  # selected city does not exists in database
            file_content[city] = response_parsed  # simply add response as it is
        else:  # selected city exists in database, check for date and add if necessary
            filtered_data = [True for record in file_content[city]['records']
                             if record["date"] == response_parsed['records'][0]['date']]
            if len(filtered_data) == 0:
                file_content[city].extend(response_parsed['records'])
                continue
        write_database(DATABASE_PATH, file_content)

    elif option == "2":  # preview
        city = input("Podaj miasto: ")
        date = input("Podaj datę (yyyy-mm-dd): ")
        data = read_database(DATABASE_PATH)
        city_data = data.get(city)
        if city_data is None:  # check if city is in database
            print(f"Brak miasta {city} w bazie")
            continue
        records = city_data['records']
        filtered_records = [record for record in records if record['date'] == date][0]
        if not filtered_records:  # check for record with specific date
            print(f"Brak danych dla daty {date}, dla miasta {city} w bazie")
            continue
        plot_data(filtered_records['data'], city, date)

    elif option == "3":  # exit
        break
