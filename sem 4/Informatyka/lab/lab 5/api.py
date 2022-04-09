import requests
import json


def get_api(currency: str, date: list, table=False) -> dict:
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


def get_file(path: str, currency: str, date: list):
    with open(path) as file:
        content = json.load(file)
        if content['code'] != currency.upper():
            return "Invalid currency code"
        rates = content['rates'][0]
        if rates['effectiveDate'] != date:
            return "Invalid date"
        return content


def write_file(path: str, data: dict) -> None:
    with open(path, 'w') as file:
        json_string = json.dumps(data)
        file.write(json_string)


def parse_data(data: dict) -> str:
    bid = data['rates'][0]['bid']
    ask = data['rates'][0]['ask']
    date = data['rates'][0]['effectiveDate']
    return f"{date} - bid: {bid}, ask: {ask}"
