from dateutil import parser


def filter_by_state(original_list: list, status: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и значение для ключа 'state', (если не задано то по умолчанию 'EXECUTED'),
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению."""
    new_list = []
    if not isinstance(original_list, list):
        return []
    else:
        for operation in original_list:
            if operation["state"] == status:
                new_list.append(operation)
        return new_list


def sort_by_date(original_list: list, sort_order: bool = True) -> list:
    """Функция принимает список словарей и параметр 'bool' задающий порядок сортировки (по умолчанию — убывание),
    и возвращает новый список, отсортированный по дате ('date')"""
    for di in original_list:
        date_format = parser.parse(di["date"])
        date_string = date_format.strftime("%Y-%m-%dT%H:%M:%S.%f")
        di["date"] = date_string
    return sorted(original_list, key=lambda dic: dic["date"], reverse=sort_order)
