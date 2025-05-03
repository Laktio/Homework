def filter_by_state(account_list: list, state: str ='EXECUTED') -> list:
    """функция принимает список словарей с данными по операциям по счетам и выводит
    список словарей только тех операций состояние ('state') которых соответствует вводному параметру"""
    account_state = []
    for account in account_list:
        if account.get('state'):
            if account['state'] == state:
                account_state.append(account)
    if account_state == []:
        return 'Введены некорректные данные транзакции!'
    else:
        return account_state


# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED'))


def sort_by_date(account_list: list, sort_parametr=True) -> list:
    """функция принимает список словарей с данными по операциям по счетам и выводит
    список словарей отсортированный по дате"""
    sorted_account_list = sorted(account_list, key=lambda account: account['date'], reverse=sort_parametr)
    return sorted_account_list


# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], False))