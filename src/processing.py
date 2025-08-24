from typing import Iterable


def filter_by_state(original_list: Iterable[list[dict]], state: str = 'EXECUTED') -> list[dict]:
    """Функция принимает список словарей и 'ЗНАЧЕНИЕ' для ключа (НЕ КЛЮЧ), (если не задано то по умолчанию 'EXECUTED'),
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению."""
    new_list = []
    for dicts in original_list:
        for value in dicts.values():
            if value == state:
                new_list.append(dicts)
    return new_list
