def get_mask_card_number(number_card: int = None) -> str:
    """Принимает НОМЕР КАРТЫ различных форматов в виде числа (int)
    и возвращает ее маску в виде строки (str)."""
    if not isinstance(number_card, int):
        raise TypeError ("Указан не верный номер карты")
    conv_number_card_str = str(number_card)
    if len(conv_number_card_str) == 19:
        return f"{conv_number_card_str[:4]} {conv_number_card_str[4:6]}** **** **** {conv_number_card_str[-3:]}"
    elif len(conv_number_card_str) == 13:
        return f"{conv_number_card_str[:4]} **** **{conv_number_card_str[-3:]}"
    elif len(conv_number_card_str) == 5:
        return f"***{conv_number_card_str[-2:]}"
    else:
        return f"{conv_number_card_str[:4]} {conv_number_card_str[4:6]}** **** {conv_number_card_str[-4:]}"


def get_mask_account(number_account: int) -> str:
    """Принимает НОМЕР СЧЕТА в виде числа (int)
    и возвращает ее маску в виде строки (str)."""
    conv_number_account = str(number_account)
    return f"**{conv_number_account[-4:]}"


if __name__ == '__main__':
    print(get_mask_card_number())
