# __package__ = "src"

from datetime import datetime

from .masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Принимать один строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером."""
    data_name = ""
    data_number = ""
    for letter in data:
        if letter.isdigit():
            data_number += letter
        else:
            data_name += letter
    if len(data_number) > 16:
        return data_name + get_mask_account(int(data_number))
    else:
        return data_name + get_mask_card_number(int(data_number))


def get_date(date_: str) -> str:
    """Принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    date_only = date_[:10]
    date_format = datetime.strptime(date_only, "%Y-%m-%d").date()
    return date_format.strftime("%d.%m.%Y")
