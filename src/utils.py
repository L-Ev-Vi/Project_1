import json
import os


def from_json_to_list(file: str) -> list:
    """Функция, принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    if file not in os.listdir('../data'):
        return []
    with open('../data/' + file, 'r', encoding='UTF-8') as f:
        data_file = json.load(f)
        if type(data_file) != list:
            return []
        if len(data_file) == 0:
            return []
        return data_file


if __name__ == '__main__':
    (from_json_to_list("operations.json"))