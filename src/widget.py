from dateutil import parser

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str = None) -> str:
    """Принимать одну строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером."""
    if not isinstance(data, str):
        raise TypeError("Ошибка ввода")
    else:
        data_name = ""
        data_number = ""
        for letter in data:
            if letter.isdigit():
                data_number += letter
            else:
                data_name += letter
        if data_name == "" or data_number == "":
            raise AssertionError("Не полный ввод данных")
        if len(data_number) > 19:
            return data_name + get_mask_account(int(data_number))
        else:
            return data_name + get_mask_card_number(int(data_number))


def get_date(date_: str = None) -> str:
    """Принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    if not isinstance(date_, str):
        raise TypeError("Ошибка ввода даты")
    date_format = parser.parse(date_)
    return date_format.strftime("%d.%m.%Y")
