# import json
import re
from collections import Counter

from dateutil import parser


def filter_by_state(original_list: list, status: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и значение для ключа 'state', (если не задано то по умолчанию 'EXECUTED'),
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению.
    """
    new_list = []
    if not isinstance(original_list, list):
        return []
    else:
        for operation in original_list:
            if operation["state"] == status:
                new_list.append(operation)
        return new_list


def sort_by_date(original_list: list, sort_order: bool = True) -> list:
    """
    Функция принимает список словарей и параметр 'bool' задающий порядок сортировки (по умолчанию — убывание),
    и возвращает новый список, отсортированный по дате ('date')
    """
    for di in original_list:
        date_format = parser.parse(di["date"])
        date_string = date_format.strftime("%Y-%m-%dT%H:%M:%S.%f")
        di["date"] = date_string
    return sorted(original_list, key=lambda dic: dic["date"], reverse=sort_order)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании (в 'description') есть данная строка.
    """
    new_list = [case for case in data if re.search(f'({search})', str(case.get("description")), flags=re.I)]

    return new_list


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории. Категории операций хранятся в поле 'description'.
    """
    counter_operations = Counter([case["description"] for case in data if case.get("description") in categories])
    for category in categories:
        if category not in counter_operations:
            counter_operations[category] = 0

    return counter_operations

# if __name__ == '__main__':
#     with open('data/operations.json', 'r', encoding='utf-8') as file:
#         operations = json.load(file)
#
#     # print(process_bank_search(operations, "ПЕРЕВОД"))
#
#     categories_list = list(set(operation["description"] for operation in operations if operation.get("description")))
#
#     print(process_bank_operations(operations, categories_list))
