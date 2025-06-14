from src.filter import search_filter, category_filter

import pytest



@pytest.mark.parametrize(
    "operations, search_string, expected",
    [
        ("C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\operations.json", "CANCELED",[
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
              'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588',
              'to': 'Счет 14211924144426031657'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441',
              'operationAmount': {'amount': '77751.04', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Перевод с карты на счет', 'from': 'Maestro 3928549031574026',
              'to': 'Счет 84163357546688983493'},
             {'id': 476991061, 'state': 'CANCELED', 'date': '2018-11-23T17:47:33.127140',
              'operationAmount': {'amount': '26971.25', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Перевод с карты на карту', 'from': 'Visa Gold 7305799447374042',
              'to': 'Maestro 3364923093037194'},
             {'id': 970724427, 'state': 'CANCELED', 'date': '2019-01-15T17:58:27.064377',
              'operationAmount': {'amount': '90688.44', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод организации', 'from': 'Visa Platinum 2241653116508487',
              'to': 'Счет 26494285169417058486'},
             {'id': 608117766, 'state': 'CANCELED', 'date': '2018-10-08T09:05:05.282282',
              'operationAmount': {'amount': '77302.31', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод с карты на счет', 'from': 'Visa Gold 6527183396477720',
              'to': 'Счет 38573816654581789611'},
             {'id': 464419177, 'state': 'CANCELED', 'date': '2018-07-15T18:44:13.346362',
              'operationAmount': {'amount': '71024.64', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Перевод с карты на счет', 'from': 'Visa Gold 9657499677062945',
              'to': 'Счет 19213886662094884261'},
             {'id': 560813069, 'state': 'CANCELED', 'date': '2019-12-03T04:27:03.427014',
              'operationAmount': {'amount': '17628.50', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод с карты на карту', 'from': 'MasterCard 1796816785869527',
              'to': 'Visa Classic 7699855375169288'},
             {'id': 556488059, 'state': 'CANCELED', 'date': '2019-05-17T01:50:00.166954',
              'operationAmount': {'amount': '74604.56', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод с карты на карту', 'from': 'МИР 8021883699486544',
              'to': 'Visa Gold 8702717057933248'},
             {'id': 692008409, 'state': 'CANCELED', 'date': '2019-02-14T17:38:09.910336',
              'operationAmount': {'amount': '37044.95', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Перевод организации', 'from': 'Visa Classic 4610247282706784',
              'to': 'Счет 63229171188548882700'},
             {'id': 176798279, 'state': 'CANCELED', 'date': '2019-04-18T11:22:18.800453',
              'operationAmount': {'amount': '73778.48', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Открытие вклада', 'to': 'Счет 90417871337969064865'},
             {'id': 200634844, 'state': 'CANCELED', 'date': '2018-02-13T04:43:11.374324',
              'operationAmount': {'amount': '42210.20', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Перевод организации', 'from': 'Счет 33355011456314142963',
              'to': 'Счет 45735917297559088682'},
             {'id': 710136990, 'state': 'CANCELED', 'date': '2018-08-17T03:57:28.607101',
              'operationAmount': {'amount': '66906.45', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод организации', 'from': 'Maestro 1913883747791351',
              'to': 'Счет 11492155674319392427'},
             {'id': 121646999, 'state': 'CANCELED', 'date': '2018-06-08T16:14:59.936274',
              'operationAmount': {'amount': '91121.62', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Перевод организации', 'from': 'Maestro 7552745726849311',
              'to': 'Счет 34799481846914116850'},
             {'id': 816266176, 'state': 'CANCELED', 'date': '2018-06-24T00:46:32.422648',
              'operationAmount': {'amount': '60030.73', 'currency': {'name': 'USD', 'code': 'USD'}},
              'description': 'Перевод организации', 'from': 'МИР 6381702861749111', 'to': 'Счет 27804394774631586026'},
             {'id': 27192367, 'state': 'CANCELED', 'date': '2018-12-24T20:16:18.819037',
              'operationAmount': {'amount': '991.49', 'currency': {'name': 'руб.', 'code': 'RUB'}},
              'description': 'Перевод со счета на счет', 'from': 'Счет 71687416928274675290',
              'to': 'Счет 87448526688763159781'}
        ] ),
        ("C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\transactions_excel.xlsx", "___", []),
    ],
)
def test_search_filter(operations, search_string, expected):
    assert search_filter(operations, search_string) == expected


@pytest.mark.parametrize(
    "operations, categories, expected",
    [
        ("C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\transactions.csv",
         ['Перевод организации', 'Перевод с карты на карту'],
         "Counter({'Перевод с карты на карту': 587, 'Перевод организации': 117})"),
        ("C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\transactions.csv",
         ['Перевод со счета на счет', 'Недовод'],
        "Counter({'Перевод со счета на счет': 110})")
    ]
)
def test_category_filter(operations, categories, expected):
    assert category_filter(operations, categories) == expected