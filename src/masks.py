
def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты без пробелов и выводит замаскированную версию с пробелами"""
    mask_variant = ""
    for sign in card_number:
        if sign.isalpha() == True or sign.isspace() == True:
            mask_variant += sign
    if len(card_number) - len(mask_variant) != 16 and len(card_number) > 0:
        return "Номер карты введен неверно!"
    if card_number == "":
        return "Данные не были введены!"
    if card_number[-16: -1].isdigit() == False:
        return "Номер карты введен неверно!"
    card_number_mask = mask_variant + card_number[-16:-12] + " " + card_number[-12:-10] + "** **** " + card_number[-4:]
    return card_number_mask


# print(get_mask_card_number("Visa Platinum aaaa922113665229"))


def get_mask_account(account: str) -> str:
    """Функция принимает номер cxtnf и выводит замаскированную версию"""
    mask_variant = ""
    for sign in account:
        if sign.isalpha() == True or sign.isspace() == True:
            mask_variant += sign
    if len(account) - len(mask_variant) != 20 and len(account) > 0:
        return "Номер счета введен неверно!"
    if account == "":
        return "Данные не были введены!"
    if account[-20: -1].isdigit() == False:
        return "Номер счета введен неверно!"
    mask_account = f"{mask_variant}**{account[-4:]}"
    return mask_account


# print(get_mask_account("Счет 7365410843013587"))
