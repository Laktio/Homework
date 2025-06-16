from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """создаем функцию которая получает номер карты / счета и возвращает замаскированную версию"""

    if "Счет" in str(account_card):
        mask_variant = get_mask_account(account_card)
    else:
        mask_variant = get_mask_card_number(account_card)
    return str(mask_variant)


# print(mask_account_card("Visa Classic 6831982476737658"))


def get_date(date_input: str) -> str:
    """создаем функцию, которая преобразует полученную дату в требуемую форму"""
    if date_input == "":
        return "Данные не были введены!"
    # if len(date_input) != 26:
    #     return "Введен некорректный формат даты!"
    date_without_points = (
        f"{(date_input[0:10].split("-"))[2]}{(date_input[0:10].split("-"))[1]}{(date_input[0:10].split("-"))[0]}"
    )
    if date_without_points.isdigit() is True:
        date = (
            f"{(date_input[0:10].split("-"))[2]}.{(date_input[0:10].split("-"))[1]}.{(date_input[0:10].split("-"))[0]}"
        )
        return date
    else:
        return "Введен некорректный формат даты!"


# print(get_date("2023-09-05T11:30:32Z"))
