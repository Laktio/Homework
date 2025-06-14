import re
from src.transactions_reader import csv_operations, excel_operation
from src.utils import operations_transform
from collections import Counter


def search_filter(operations:str, search_string:str):
    """Функция принимает список банковских операций (список словарей из функций operations_transform() из
     utils, csv_operations() из transactions_reader, excel_operation() из transactions_reader) и
     строку поиска и выводит список словарей содержащие данные из строки поиска"""
    if 'json' in operations:
        operations_list = operations_transform(operations)
    elif 'csv' in operations:
        operations_list = csv_operations(operations)
    elif 'xlsx' in operations:
        operations_list = excel_operation(operations)
    search_list = []
    for operation in operations_list:
        operation_state = str(operation.get('state'))
        search_result = re.search(search_string, operation_state, flags=re.IGNORECASE)
        if search_result is not None:
            search_list.append(operation)
    return search_list


# print(search_filter("C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\transactions.csv", "CANCELED"))


def category_filter(operations:str, categories:list):
    """Функция принимает список банковских операций (список словарей из функций operations_transform() из
     utils, csv_operations() из transactions_reader, excel_operation() из transactions_reader) и
     список категорий операций и выводит словарь, в котором ключи — это названия категорий, а значения
     — это количество операций в каждой категории"""
    if 'json' in operations:
        operations_list = operations_transform(operations)
    elif 'csv' in operations:
        operations_list = csv_operations(operations)
    elif 'xlsx' in operations:
        operations_list = excel_operation(operations)
    else:
        return "incorrect input data!"
    categories_list = []
    for operation in operations_list:
        operation_state = str(operation.get('description'))
        for category in categories:
            search_result = re.search(category, operation_state, flags=re.IGNORECASE)
            if search_result is not None:
                categories_list.append(operation.get('description'))
    counted_category_list = Counter(categories_list)
    return str(counted_category_list)


print(category_filter('../data/transactions.csv',
                      ['Перевод организации', 'Перевод с карты на карту']))