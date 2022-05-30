import json


def read_database(path: str) -> dict:
    with open(path) as file:
        data = json.load(file)
        return data


def write_database(path: str, data: dict):
    with open(path, "w") as file:
        json_str = json.dumps(data)
        file.write(json_str)
