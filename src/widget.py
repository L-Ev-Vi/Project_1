from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Принимать один строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером."""
    data_number = ""
    for letter in data:
        if letter.isalnum():
            data_number += letter
    if len(data_number) > 16:
        return get_mask_account(data_number)
    else:
        return get_mask_card_number(data_number)


def get_date(date_: str) -> str:
    """Принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    date_only = date_[:10]
    date_format = datetime.strptime(date_only, "%Y-%m-%d").date()
    return date_format.strftime("%d.%m.%Y")
