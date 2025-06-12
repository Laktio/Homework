from src.filter import search_filter
from src.widget import get_date, mask_account_card

import re

from datetime import datetime

def main():
    """Функция принимает список словарей из функции search_filter() по выбору источника пользователем
    проводит опрос пользователя и выдает список транзакций по его ответам"""
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    file_type = str(input('''
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла 
'''))

    # JSON===================================#

    if file_type == '1':
        file_path = "../data/operations.json"
        status_string = str(input('''
Для обработки выбран JSON-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))
        search_filter_status = search_filter(file_path, status_string)

    # STATUS------------------------------------------------#

        while search_filter(file_path, status_string.upper()) == []:
            print(f"Статус операции {status_string} недоступен.")
            status_string = str(input('''
Для обработки выбран JSON-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))
            search_filter_status = search_filter(file_path, status_string.upper())

    # DATE--------------------------------------------------#

        date_sort = str(input('''Отсортировать операции по дате? Да/Нет
'''))
        if date_sort.lower() == "да":
            increase_sort = str(input('''Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
'''))
            if increase_sort.lower() == "по возрастанию":
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=False)
            else:
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=True)

        else:
            date_sorted = search_filter_status

    # CURRENCY-----------------------------------------------#

        currency_sort = str(input('''Выводить только рублевые транзакции? Да/Нет
'''))
        if currency_sort.lower() == "да":
            date_sorted_rub = []

            for transaction in date_sorted:

                if transaction["operationAmount"]["currency"]["code"] == 'RUB':
                    date_sorted_rub.append(transaction)

        else:
            date_sorted_rub = date_sorted
    # DICRIPTION----------------------------------------------#

        discription_sort = str(input('''Отфильтровать список транзакций по определенному слову в описании? Да/Нет
'''))
        if discription_sort.lower() == "да":
            discription_word = str(input('Введите слово для сортировки '))
            discription_sort_word = []

            for transaction in date_sorted_rub:
                discription_text = str(transaction.get('description'))
                search_result = re.search(discription_word, discription_text, flags=re.IGNORECASE)

                if search_result is not None:
                    discription_sort_word.append(transaction)
                else:
                    discription_sort_word = date_sorted_rub

        else:
            discription_sort_word = date_sorted_rub

    # TRANSACTION LIST-----------------------------------------#

            discription_sort_word_len = len(discription_sort_word)
            results = []

            for transaction in discription_sort_word:
                date_string = transaction.get("date")
                date = get_date(date_string)

                discription = transaction.get("description")

                account_from_string = transaction.get("from")
                if account_from_string is not None:
                    account_from = mask_account_card(account_from_string) + " -> "
                else:
                    account_from = ""

                account_to_string = transaction.get("to")
                if account_to_string is not None:
                    account_to = mask_account_card(account_to_string)
                else:
                    account_to = ""

                operation_amount = transaction.get("operationAmount")
                amount = operation_amount.get("amount")

                currency = operation_amount.get("currency")
                currency_name = currency.get("name")

                result = f'''{date} {discription}
{account_from}{account_to}
Сумма: {amount} {currency_name}
'''
                results.append(result)


    main_result = f"""
Распечатываю итоговый список транзакций...

Всего банковских операций в выборке: {discription_sort_word_len}

{'\n'.join(results)}
"""

    # CSV===================================#

    if file_type == '2':
        file_path = "../data/operations.json"
        status_string = str(input('''
    Для обработки выбран JSON-файл.
    Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
    EXECUTED, CANCELED, PENDING
    '''))
        search_filter_status = search_filter(file_path, status_string)

        # STATUS------------------------------------------------#

        while search_filter(file_path, status_string.upper()) == []:
            print(f"Статус операции {status_string} недоступен.")
            status_string = str(input('''
    Для обработки выбран JSON-файл.
    Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
    EXECUTED, CANCELED, PENDING
    '''))
            search_filter_status = search_filter(file_path, status_string.upper())

        # DATE--------------------------------------------------#

        date_sort = str(input('''Отсортировать операции по дате? Да/Нет
    '''))
        if date_sort.lower() == "да":
            increase_sort = str(input('''Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
    '''))
            if increase_sort.lower() == "по возрастанию":
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=False)
            else:
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=True)

        else:
            date_sorted = search_filter_status

        # CURRENCY-----------------------------------------------#

        currency_sort = str(input('''Выводить только рублевые транзакции? Да/Нет
    '''))
        if currency_sort.lower() == "да":
            date_sorted_rub = []

            for transaction in date_sorted:

                if transaction["operationAmount"]["currency"]["code"] == 'RUB':
                    date_sorted_rub.append(transaction)

        else:
            date_sorted_rub = date_sorted
        # DICRIPTION----------------------------------------------#

        discription_sort = str(input('''Отфильтровать список транзакций по определенному слову в описании? Да/Нет
    '''))
        if discription_sort.lower() == "да":
            discription_word = str(input('Введите слово для сортировки '))
            discription_sort_word = []

            for transaction in date_sorted_rub:
                discription_text = str(transaction.get('description'))
                search_result = re.search(discription_word, discription_text, flags=re.IGNORECASE)

                if search_result is not None:
                    discription_sort_word.append(transaction)
                else:
                    discription_sort_word = date_sorted_rub

        else:
            discription_sort_word = date_sorted_rub

            # TRANSACTION LIST-----------------------------------------#

            discription_sort_word_len = len(discription_sort_word)
            results = []

            for transaction in discription_sort_word:
                date_string = transaction.get("date")
                date = get_date(date_string)

                discription = transaction.get("description")

                account_from_string = transaction.get("from")
                if account_from_string is not None:
                    account_from = mask_account_card(account_from_string) + " -> "
                else:
                    account_from = ""

                account_to_string = transaction.get("to")
                if account_to_string is not None:
                    account_to = mask_account_card(account_to_string)
                else:
                    account_to = ""

                operation_amount = transaction.get("operationAmount")
                amount = operation_amount.get("amount")

                currency = operation_amount.get("currency")
                currency_name = currency.get("name")

                result = f'''{date} {discription}
    {account_from}{account_to}
    Сумма: {amount} {currency_name}
    '''
                results.append(result)

    main_result = f"""
    Распечатываю итоговый список транзакций...

    Всего банковских операций в выборке: {discription_sort_word_len}

    {'\n'.join(results)}
    """






    return a




print(main())
