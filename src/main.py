from src.filter import search_filter

import re

def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    file_type = str(input('''
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла 
'''))

    if file_type == '1':
        file_path = "../data/operations.json"
        status_string = str(input('''
Для обработки выбран JSON-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))
        search_filter_status = search_filter(file_path, status_string)

        if search_filter(file_path, status_string.upper()) == []:
            print(f"Статус операции {status_string} недоступен.")
            status_string = str(input('''
Для обработки выбран JSON-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))
            search_filter_status = search_filter(file_path, status_string.upper())

        date_sort = str(input('''Отсортировать операции по дате? Да/Нет
'''))
        increase_sort = str(input('''Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
'''))
        currency_sort = str(input('''Выводить только рублевые транзакции? Да/Нет
'''))
        discription_sort = str(input('''Отфильтровать список транзакций по определенному слову в описании? Да/Нет
'''))

        if date_sort.lower() == "да":
            if increase_sort.lower() == "по возрастанию":
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=False)
            else:
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=True)
        else:
            date_sorted = search_filter_status

        if currency_sort.lower() == "да":
            date_sorted_rub = []
            for transaction in date_sorted:
                if transaction["operationAmount"]["currency"]["code"] == 'RUB':
                    date_sorted_rub.append(transaction)
        else:
            date_sorted_rub = date_sorted

        if discription_sort.lower() == "да":
            discription_word = str(input('Введите слово для сортировки '))
            discription_sort_word = []
            for transaction in date_sorted_rub:
                discription_text = str(transaction.get('description'))
                search_result = re.search(discription_word, discription_text, flags=re.IGNORECASE)

                if search_result is not None:
                    discription_sort_word.append(transaction)
            return discription_sort_word

    if file_type == '2':
        file_path = "../data/transactions.csv"
        status_string = str(input('''
Для обработки выбран CSV-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))
        search_filter_status = search_filter(file_path, status_string)

        if search_filter(file_path, status_string.upper()) == []:
            print(f"Статус операции {status_string} недоступен.")
            status_string = str(input('''
Для обработки выбран CSV-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))
            search_filter_status = search_filter(file_path, status_string.upper())

        date_sort = str(input('''Отсортировать операции по дате? Да/Нет
'''))
        increase_sort = str(input('''Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
'''))
        currency_sort = str(input('''Выводить только рублевые транзакции? Да/Нет
'''))
        discription_sort = str(input('''Отфильтровать список транзакций по определенному слову в описании? Да/Нет
'''))

        if date_sort.lower() == "да":
            if increase_sort.lower() == "по возрастанию":
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=False)
            else:
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=True)
        else:
            date_sorted = search_filter_status

        if currency_sort.lower() == "да":
            date_sorted_rub = []
            for transaction in date_sorted:
                if transaction["currency_code"] == 'Ruble':
                    date_sorted_rub.append(transaction)
        else:
            date_sorted_rub = date_sorted

        if discription_sort.lower() == "да":
            discription_word = str(input('Введите слово для сортировки '))
            discription_sort_word = []
            for transaction in date_sorted_rub:
                discription_text = str(transaction.get('description'))
                search_result = re.search(discription_word, discription_text, flags=re.IGNORECASE)

                if search_result is not None:
                    discription_sort_word.append(transaction)
            return discription_sort_word

    if file_type == '3':
        file_path = "../data/transactions_excel.xlsx"
        status_string = str(input('''
Для обработки выбран EXCEL-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))
        if search_filter(file_path, status_string.upper()) == []:
            print(f"Статус операции {status_string} недоступен.")
            status_string = str(input('''
Для обработки выбран EXCEL-файл.
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы:
EXECUTED, CANCELED, PENDING
'''))
        search_filter_status = search_filter(file_path, status_string.upper())

        date_sort = str(input('''Отсортировать операции по дате? Да/Нет
'''))
        increase_sort = str(input('''Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию
'''))
        currency_sort = str(input('''Выводить только рублевые транзакции? Да/Нет
'''))
        discription_sort = str(input('''Отфильтровать список транзакций по определенному слову в описании? Да/Нет
'''))

        if date_sort.lower() == "да":
            if increase_sort.lower() == "по возрастанию":
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=False)
            else:
                date_sorted = sorted(search_filter_status, key=lambda operation: operation['date'], reverse=True)
        else:
            date_sorted = search_filter_status

        if currency_sort.lower() == "да":
            date_sorted_rub = []
            for transaction in date_sorted:
                if transaction["currency_code"] == 'Ruble':
                    date_sorted_rub.append(transaction)
        else:
            date_sorted_rub = date_sorted

        if discription_sort.lower() == "да":
            discription_word = str(input('Введите слово для сортировки '))
            discription_sort_word = []
            for transaction in date_sorted_rub:
                discription_text = str(transaction.get('description'))
                search_result = re.search(discription_word, discription_text, flags=re.IGNORECASE)

                if search_result is not None:
                    discription_sort_word.append(transaction)
            return discription_sort_word


print(main())
