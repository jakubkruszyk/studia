# program pobiera kurs wybranej waluty z dowolnego dnia/ zakresu dat

import requests
import json

path = "table.json"


def get_api(currency, date, table=False):
    if len(date) == 1:
        url = f"http://api.nbp.pl/api/exchangerates/{'table' if table else 'rates'}" \
              f"/c/{'' if table else currency + '/'}{date[0]}/?format=json"
    else:
        url = f"http://api.nbp.pl/api/exchangerates/{'table' if table else 'rates'}" \
              f"/c/{'' if table else currency + '/'}{date[0]}/{date[1]}/?format=json"

    # request do NBP
    resp = requests.get(url)
    data = resp.json() if resp.status_code == 200 else "Not found - probably invalid date"
    return data


def get_file(path, currency, date):
    with open(path) as file:
        content = json.load(file)
        if content['code'] != currency.upper():
            return "Invalid currency code"
        rates = content['rates'][0]
        if rates['effectiveDate'] != date:
            return "Invalid date"
        return content
    

# pobranie danych
currency = input("Podaj kod waluty: ").lower()
date = input("Podaj datę/ zakres dat rozdzielone spacją: ").split(" ")
data = get_api(currency=currency, date=date)

with open(path, 'w') as file:
    json_string = json.dumps(data)
    file.write(json_string)

get_file(path=path, currency='usd', date='2022-03-30')
