from unittest.mock import patch

from src.external_api import exchange_currency
from src.utils import operations_transform

# import requests


def test_exchange_currency_1():
    trans = operations_transform("../data/operations.json")[0]
    result = exchange_currency(trans)
    assert result == 31957.58


@patch("requests.get")
def test_exchange_currency_2(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1748779696, "rate": 77.180757},
        "date": "2025-06-01",
        "result": 634531.560177,
    }

    result1 = exchange_currency(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
    assert round(result1, 2) == 634531.56
