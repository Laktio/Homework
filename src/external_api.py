import requests
import utils
import json

def external_api(transaction: dict):
    """функция принимает в качестве аргумента словарь из списка словарей из файла operations.json
    (результат работы функции operations_transform() c указанием индекса конкретной транзации,
    и выдает стоимость (amount) в рублях (RUB)"""
    if "RUB" == transaction["operationAmount"]["currency"]["code"]:
        return float(transaction["operationAmount"]['amount'])
    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {
            "amount": transaction["operationAmount"]['amount'],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB"
        }

        headers= {
          "apikey": "HFnk0WdgKxXiPK4Rkl4qQvddRvu3CJ9O"
        }

        response = requests.get(url, headers=headers, params=payload)

        status_code = response.status_code
        result = response.text
        result_dict = json.loads(result)

        return round(float(result_dict['result']), 2)


trans = utils.operations_transform('../data/operations.json')[1]
print(external_api(trans))

#
