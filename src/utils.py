import json
from json import JSONDecodeError


def from_json_to_list(file: str) -> list:
    """Функция, принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open("../data/" + file, "r", encoding="UTF-8") as f:
            try:
                data_file = json.load(f)
            except JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    if type(data_file) is not list:
        return []
    if len(data_file) == 0:
        return []
    return data_file
