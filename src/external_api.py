import os

import requests
# from src.utils import operations_transform
# import json
from dotenv import load_dotenv


def exchange_currency(transaction: dict):
    """функция принимает в качестве аргумента словарь из списка словарей из файла operations.json
    (результат работы функции operations_transform() c указанием индекса конкретной транзации,
    и выдает стоимость (amount) в рублях (RUB)"""
    if "RUB" == transaction["operationAmount"]["currency"]["code"]:
        return float(transaction["operationAmount"]["amount"])
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB",
        }
        load_dotenv()
        api_key = os.getenv("API_KEY")

        headers = {"apikey": api_key}

        response = requests.get(url, headers=headers, params=payload)

        # status_code = response.status_code
        result = response.json()
        # result_dict = json.loads(result)

        return round(float(result["result"]), 2)
        # return response


# trans = operations_transform('../data/operations.json')[1]
# print(exchange_currency(trans))
