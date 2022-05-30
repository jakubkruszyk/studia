import requests

BASE_URL = "http://api.weatherapi.com/v1"


def get_data(localization: list[str], key: str) -> dict:
    if len(localization) == 2:  # Latitude and Longitude
        response = requests.get(f"{BASE_URL}/forecast.json",
                                params={'key': key, 'q': f"{localization[0]},{localization[1]}",
                                        'days': 1, 'aqi': 'no'})
    elif len(localization) == 1:  # city name
        response = requests.get(f"{BASE_URL}/forecast.json", params={'key': key, 'q': localization[0],
                                                                     'days': 1, 'aqi': 'no'})
    else:
        return {"error": "Inappropriate number of localization parameters"}
    code = response.status_code
    response = response.json()
    if code != 200:
        return {"error": response['error']['message']}
    return response
