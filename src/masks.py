from decorators import log


@log(filename="../logs/masks.log")
def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты без пробелов и выводит замаскированную версию с пробелами"""
    mask_variant = ""
    for sign in card_number:
        if sign.isalpha() is True or sign.isspace() is True:
            mask_variant += sign
    if len(card_number) - len(mask_variant) != 16 and len(card_number) > 0:
        return "invalid card number!"
    if card_number == "":
        return "no input data!"
    if card_number[-16:-1].isdigit() is False:
        return "invalid card number!"
    card_number_mask = mask_variant + card_number[-16:-12] + " " + card_number[-12:-10] + "** **** " + card_number[-4:]
    return card_number_mask


print(get_mask_card_number("Maestro 1596837868705199"))


@log(filename="../logs/masks.log")
def get_mask_account(account: str) -> str:
    """Функция принимает номер cxtnf и выводит замаскированную версию"""
    mask_variant = ""
    for sign in account:
        if sign.isalpha() is True or sign.isspace() is True:
            mask_variant += sign
    if len(account) - len(mask_variant) != 20 and len(account) > 0:
        return "valid account number!"
    if account == "":
        return "no input data!"
    if account[-20:-1].isdigit() is False:
        return "valid account number!"
    mask_account = f"{mask_variant}**{account[-4:]}"
    return mask_account


print(get_mask_account("Счет 64686473678894779589"))
