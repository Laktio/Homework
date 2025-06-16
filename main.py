from src.filter import search_filter
from src.widget import get_date, mask_account_card
from src.transactions_reader import csv_operations

import re

from datetime import datetime


def main():
    """Функция принимает тип файла от пользователя и выдает ссылку на файл"""
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    file_type = str(input('''
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из EXEL-файла 
'''))
    if file_type == '1':
        file_path = "C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\operations.json"

    elif file_type == '2':
        file_path = "C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\transactions.csv"

    elif file_type == '3':
        file_path = "C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\transactions_excel.xlsx"

    else:
        return "Некорректный тип файла"

    return file_path


def status_filter_file_type(file_path = main()):
    """Функция принимает в качкстве аргумента ссылку на файл (main()) и выдает
    список словарей с фильтрацией по статусу операции"""
    if file_path == "Некорректный тип файла":
        return "Некорректный тип файла"
    else:
        type = ""
        if "json" in file_path:
            type = "JSON"
        elif "csv" in file_path:
            type = "CSV"
        elif "xlsx" in file_path:
            type = "EXEL"
        status_string = str(input('''
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))

        while search_filter(file_path, status_string.upper()) == []:
            print(f"Статус операции {status_string} недоступен.")
            status_string = str(input('''
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))

        result = search_filter(file_path, status_string)

        print(f"""Для обработки выбран {type}-файл.
""")
        return result


def sort_by_date(status_sorted_operation_list = status_filter_file_type()):
    """Функция принимает в качестве аргумента список словарей с фильтрацией по статусу операции и выдает
        список словарей с сортировкой по дате"""
    date_sort = str(input('''Отсортировать операции по дате? Да/Нет
'''))

    if date_sort.lower() == "да":
        increase_sort = str(input('''Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
'''))

        if increase_sort.lower() == "по возрастанию":
            date_sorted = sorted(status_sorted_operation_list, key=lambda operation: operation['date'], reverse=False)
        else:
            date_sorted = sorted(status_sorted_operation_list, key=lambda operation: operation['date'], reverse=True)

    else:
        date_sorted = status_sorted_operation_list

    return date_sorted


def currency_sort(date_sorted = sort_by_date()):
    """Функция принимает в качестве аргумента список словарей с фильтрацией по статусу операции и дате и выдает
    список словарей с сортировкой по типу валюты (рублевые операции и все вместе)"""
    currency_sort_list = str(input('''Выводить только рублевые транзакции? Да/Нет
'''))
    if currency_sort_list.lower() == "да":
        date_sorted_rub = []

        for operation in date_sorted:

            if operation.get("operationAmount") is not None :
                if operation["operationAmount"]["currency"]["code"] == 'RUB':
                    date_sorted_rub.append(operation)
            elif  operation["currency_code"] == 'RUB':
                date_sorted_rub.append(operation)

    else:
        date_sorted_rub = date_sorted

    return date_sorted_rub


def discription_sort(date_sorted_rub = currency_sort()):
    """Функция принимает в качестве аргумента список словарей с фильтрацией по статусу операции и дате и по типу валюты
    (рублевые операции и все вместе), и выдает список операций с сортировкой по ключевому слову в описании"""
    discription_sort_request = str(input('''Отфильтровать список транзакций по определенному слову в описании? Да/Нет
'''))
    if discription_sort_request.lower() == "да":
        discription_word = str(input('Введите слово для сортировки '))
        discription_sort_word = []

        for operation in date_sorted_rub:
            discription_text = str(operation.get('description'))
            search_result = re.search(discription_word, discription_text, flags=re.IGNORECASE)

            if search_result is not None:
                discription_sort_word.append(operation)

    else:
        discription_sort_word = date_sorted_rub

    return discription_sort_word


def operation_report(sorted_list = discription_sort()):
    """Функция принимает в качестве аргумента список словарей с фильтрацией по статусу операции и дате и по типу валюты
    (рублевые операции и все вместе) и с сортировкой по ключевому слову в описании, и выдает количество и список
    операций в определенном виде"""
    sorted_list_len = len(sorted_list)
    results = []

    for operation in sorted_list:
        date_string = operation.get("date")
        date = get_date(date_string)

        discription = operation.get("description")

        account_from_string = operation.get("from")
        if account_from_string is not None:
            account_from = mask_account_card(account_from_string) + " -> "
        else:
            account_from = ""

        account_to_string = operation.get("to")
        if account_to_string is not None:
            account_to = mask_account_card(account_to_string)
        else:
            account_to = ""

        operation_amount = operation.get("operationAmount")
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

Всего банковских операций в выборке: {sorted_list_len}

{'\n'.join(results)}
"""
    return main_result


# print(operation_report())
