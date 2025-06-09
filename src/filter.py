import re
from src.transactions_reader import csv_operations, excel_operation
from src.utils import operations_transform

def search_filter(operations:str, search_string:str=str(input('''
Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: 
EXECUTED, CANCELED, PENDING 
'''))):
    """Функция принимает список банковских операций (список словарей из функций operations_transform() из
     utils, csv_operations() из transactions_reader, excel_operation() из transactions_reader) и
     строку поиска и выводит список словарей содержащие данные из строки поиска"""
    if 'json' in operations:
        operations_list = operations_transform(operations)
    elif 'csv' in operations:
        operations_list = csv_operations(operations)
    elif 'xlsx' in operations:
        operations_list = excel_operation(operations)
    else:
        return "incorrect input data!"
    search_list = []
    for operation in operations_list:
        operation_state = str(operation.get('state'))
        search_result = re.search(search_string, operation_state, flags=re.IGNORECASE)
        if search_result is not None:
            search_list.append(operation)
    return search_list



# print(search_filter("../data/transactions_excel.xlsx"))
