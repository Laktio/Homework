card_number = input("введите номер карты без пробелов ")


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты без пробелов и выводит замаскированную версию с пробелами"""
    card_number_mask = card_number.replace(card_number[4:6] + card_number[6:12], " " + card_number[4:6] + "** **** ")
    return card_number_mask


print(get_mask_card_number(card_number))

account = str(input("введите номер счета "))


def get_mask_account(account: str) -> str:
    """Функция принимает номер cxtnf и выводит замаскированную версию"""
    mask_account = f"**{account[-4:]}"
    return mask_account


print(get_mask_account(account))
