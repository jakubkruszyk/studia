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
        response = {
            'localization': (response['location']['name'], (response['location']['lat'], response['location']['lon'])),
            'data': [{'timestamp': response['current']['last_updated_epoch'],
                      'temperature': response['current']['temp_c'],
                      'humidity': response['current']['humidity'],
                      'pressure': response['current']['pressure_mb']
                      }]
        }
        city = response['localization'][0]
        # file part ====================================================================================================
        file_content = read_database(DATABASE_PATH)
        if file_content.get(city) is None:  # selected city does not exists in database
            file_content[city] = response['data']  # simply add response as it is
        else:  # selected city exists in database, check for timestamp and add if necessary
            filtered_data = [True for record in file_content[city]
                             if record["timestamp"] == response['data'][0]['timestamp']]
            if len(filtered_data) == 0:
                file_content[city].extend(response['data'])
        write_database(DATABASE_PATH, file_content)

    elif option == "2":  # preview
        city = input("Podaj miasto: ")
        data = read_database(DATABASE_PATH)[city]
        plot_data(data, 't')

    elif option == "3":  # exit
        break
