import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, exception", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Visa Gold 59994142284263531111", "Номер карты введен неверно!"),
    ("", "Данные не были введены!"),
    ("Visa Gold asdf414228426353", "Номер карты введен неверно!")
])
def test_get_mask_card_number(card_number, exception):
    assert get_mask_card_number(card_number) == exception


@pytest.mark.parametrize("account, exception", [
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 736541084301358743051111", "Номер счета введен неверно!"),
    ("Счет 7365410843013587", "Номер счета введен неверно!"),
    ("", "Данные не были введены!"),
    ("Счет 7365410843013587asdf", "Номер счета введен неверно!")
])
def test_get_mask_account(account, exception):
    assert get_mask_account(account) == exception
