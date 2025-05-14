from typing import Union

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "account_list, state, exception",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "invalid state",
            "Введены некорректные данные транзакции!",
        ),
        (
            [
                {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            "Введены некорректные данные транзакции!",
        ),
        (
            [
                {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            "Введены некорректные данные транзакции!",
        ),
    ],
)
def test_filter_by_state(account_list: list, state: str, exception: Union[str, list]) -> None:
    assert filter_by_state(account_list, state) == exception


def test_sort_by_date_fix_False(test_list_filter_state_1: list) -> None:
    assert sort_by_date(test_list_filter_state_1, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_fix_True(test_list_filter_state_1: list) -> None:
    assert sort_by_date(test_list_filter_state_1, True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_fix_empty(test_list_filter_state_2: list) -> None:
    assert sort_by_date(test_list_filter_state_2, True) == "Данные не были введены!"


def test_sort_by_date_fix_duplicate(test_list_filter_state_3: list) -> None:
    assert sort_by_date(test_list_filter_state_3, True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date_fix_incorrect(test_list_filter_state_4: list) -> None:
    assert sort_by_date(test_list_filter_state_4, True) == "Некорректный формат даты!"
