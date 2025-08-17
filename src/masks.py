def get_mask_card_number(number_card: int) -> str:
    """Принимает 16-и значный НОМЕР КАРТЫ в виде числа (int)
    и возвращает ее маску в виде строки (str)."""
    conv_number_card_str = str(number_card)
    return f"{conv_number_card_str[:4]} {conv_number_card_str[4:6]}** **** {conv_number_card_str[-4:]}"


def get_mask_account(number_account: int) -> str:
    """Принимает НОМЕР СЧЕТА в виде числа (int)
    и возвращает ее маску в виде строки (str)."""
    conv_number_account = str(number_account)
    return f"**{conv_number_account[-4:]}"
