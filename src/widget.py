from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """создаем функцию которая получает номер карты / счета и возвращает замаскированную версию"""
    mask_variant = ""
    if account_card[-20:].isdigit() == True:
        mask_variant = get_mask_account(account_card)
    else:
        mask_variant = get_mask_card_number(account_card)
    return mask_variant


print(mask_account_card("64686473678894779589"))


def get_date(date_input: str) -> str:
    """создаем функцию которая перобразует полученную дату в требуемую форму"""
    date = f"{(date_input[0:10].split("-"))[2]}.{(date_input[0:10].split("-"))[1]}.{(date_input[0:10].split("-"))[0]}"
    return date


print(get_date("2024-03-11T02:26:18.671407"))
