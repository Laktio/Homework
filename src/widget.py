account_card = input("Введите номер счета/карты ")


def mask_account_card(account_card: str) -> str:
    mask_variant = ""
    for sign in account_card:
        if sign.isalpha() == True or sign.isspace() == True:
            mask_variant += sign
    if account_card[-20:].isdigit() == True:
        mask_variant = mask_variant + "**" + account_card[-4:]
    else:
        mask_variant = (
            mask_variant + account_card[-16:-12] + " " + account_card[-12:-10] + "** **** " + account_card[-4:]
        )
    return mask_variant


print(mask_account_card(account_card))

date_input = input("Введите дату ")


def get_date(date_input: str) -> str:
    date = f"{(date_input[0:10].split("-"))[2]}.{(date_input[0:10].split("-"))[1]}.{(date_input[0:10].split("-"))[0]}"
    return date


print(get_date(date_input))
