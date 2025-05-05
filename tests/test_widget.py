from typing import Union

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("account_card, exception", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("", "Данные не были введены!"),
    ("Счет 736541084301358743051111", "Номер счета введен неверно!"),
    ("Visa Gold 59994142284263531111", "Номер карты введен неверно!"),
    ("Счет 7365410843013587abcd", "Номер счета введен неверно!"),
    ("Visa Gold abcd414228426353", "Номер карты введен неверно!")
])
def test_mask_account_card(account_card: str, exception: str) -> None:
    assert mask_account_card(account_card) == exception


@pytest.mark.parametrize("date_input, exception", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2022-01-25T02:26:18.671407", "25.01.2022"),
    ("2025-01-01T02:26:18.671407", "01.01.2025"),
    ("25-01-01T02:26:18.671407", "Введен некорректный формат даты!"),
    ("AB25-01-01T02:26:18.671407", "Введен некорректный формат даты!"),
    ("", "Данные не были введены!")
])
def test_get_date(date_input: str, exception: str) -> None:
    assert get_date(date_input) == exception
