import logging
from typing import Optional

mask_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
mask_logger.addHandler(file_handler)
mask_logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: Optional[int] = None) -> str:
    """Принимает НОМЕР КАРТЫ различных форматов в виде числа (int)
    и возвращает ее маску в виде строки (str)."""
    mask_logger.info("Запуск метода по созданию маски карты")
    if not isinstance(number_card, int):
        mask_logger.error(f"Указан не верный формат номера карты: {type(number_card)} {number_card}")
        raise TypeError(f"Указан не верный формат номера карты: {type(number_card)} {number_card}")
    conv_number_card_str = str(number_card)
    if len(conv_number_card_str) == 19:
        mask_logger.info(f"Создана маска для карты 'UnionPay': {number_card}")
        return f"{conv_number_card_str[:4]} {conv_number_card_str[4:6]}** **** **** {conv_number_card_str[-3:]}"
    elif len(conv_number_card_str) == 13:
        mask_logger.info(f"Создана маска для карты 'Old Standard': {number_card}")
        return f"{conv_number_card_str[:4]} **** **{conv_number_card_str[-3:]}"
    elif len(conv_number_card_str) == 5:
        mask_logger.info(f"Создана маска для карты 'AmericanExpress': {number_card}")
        return f"***{conv_number_card_str[-2:]}"
    else:
        mask_logger.info(f"Создана маска для карты 'Standard': {number_card}")
        return f"{conv_number_card_str[:4]} {conv_number_card_str[4:6]}** **** {conv_number_card_str[-4:]}"


def get_mask_account(number_account: Optional[int] = None) -> str:
    """Принимает НОМЕР СЧЕТА в виде числа (int)
    и возвращает ее маску в виде строки (str)."""
    mask_logger.info("Запуск метода по созданию маски счёта")
    if not isinstance(number_account, int):
        mask_logger.error(f"Указан не верный формат номера счёта: {type(number_account)} {number_account}")
        raise TypeError(f"Указан не верный формат номера счёта: {type(number_account)} {number_account}")
    conv_number_account = str(number_account)
    mask_logger.info(f"Создана маска для счёта: {number_account}")
    return f"**{conv_number_account[-4:]}"
