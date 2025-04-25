# card_number = input("введите номер карты без пробелов ")


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты без пробелов и выводит замаскированную версию с пробелами"""
    mask_variant = ""
    for sign in card_number:
        if sign.isalpha() == True or sign.isspace() == True:
            mask_variant += sign
    card_number_mask = mask_variant + card_number[-16:-12] + " " + card_number[-12:-10] + "** **** " + card_number[-4:]
    return card_number_mask


# print(get_mask_card_number("MasterCard 7158300734726758"))

# account = str(input("введите номер счета "))


def get_mask_account(account: str) -> str:
    """Функция принимает номер cxtnf и выводит замаскированную версию"""
    mask_variant = ""
    for sign in account:
        if sign.isalpha() == True or sign.isspace() == True:
            mask_variant += sign
    mask_account = f"{mask_variant}**{account[-4:]}"
    return mask_account


# print(get_mask_account("35383033474447895560"))
