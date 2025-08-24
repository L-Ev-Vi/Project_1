from typing import Any, Iterable


def filter_by_state(original_list: Iterable[list[dict[str, Any]]], state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и 'ЗНАЧЕНИЕ' для ключа (НЕ КЛЮЧ), (если не задано то по умолчанию 'EXECUTED'),
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению."""
    new_list = []
    for dicts in original_list:
        for value in dicts.values():
            if value == state:
                new_list.append(dicts)
    return new_list


def sort_by_date(original_list: Iterable[list[dict[str, Any]]], sort_order: bool = True) -> list:
    """Функция принимает список словарей и параметр 'bool' задающий порядок сортировки (по умолчанию — убывание),
    и возвращает новый список, отсортированный по дате ('date')"""
    return sorted(original_list, key=lambda dic: dic["date"], reverse=sort_order)
