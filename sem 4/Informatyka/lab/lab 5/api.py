import requests
import json
from datetime import datetime


def get_api(currency: str, date: list, table=False) -> dict:
    if len(date) == 1:
        url = f"http://api.nbp.pl/api/exchangerates/{'table' if table else 'rates'}" \
              f"/c/{'' if table else currency + '/'}{date[0]}/?format=json"
    else:
        url = f"http://api.nbp.pl/api/exchangerates/{'table' if table else 'rates'}" \
              f"/c/{'' if table else currency + '/'}{date[0]}/{date[1]}/?format=json"

    # request do NBP
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
    else:
        return {"error": "Not found - probably invalid date"}

    data_parsed = {'date': data['rates'][0]['effectiveDate'],
                   'bid': data['rates'][0]['bid'],
                   'ask': data['rates'][0]['ask']}
    return data_parsed


def get_file(path: str) -> dict:
    with open(path) as file:
        content = json.load(file)
        return content


def write_file(path: str, data: dict) -> None:
    with open(path, 'w') as file:
        json_string = json.dumps(data)
        file.write(json_string)


def parse_data(data: dict) -> str:
    error = data.get('error')
    if error is not None:
        return f"error: {error}"
    else:
        return f"{data['date']} - bid: {data['bid']}, ask: {data['ask']}"


def sort_content(data: list) -> list:
    def fun(x: dict):
        return datetime.strptime(x['date'], "%Y-%m-%d").timestamp()

    sorted_data = sorted(data, key=fun)
    return sorted_data
