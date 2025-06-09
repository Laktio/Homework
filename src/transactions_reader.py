import csv

import pandas as pd

from src.decorators import log


@log(filename="../logs/transaction_reader.log")
def csv_operations(file_path: str) -> list[dict]:
    """Функция принимет путь к файлу формата CSV и после считывания выдает список
    словарей, где ключи это заголовок таблицы, а значения это содержимое рядов
    в соответсвии с заголовками"""
    try:
        with open(file_path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            transaction_list = []
            for row in reader:
                for head, content in row.items():
                    head_list = head.split(";")
                    content_list = content.split(";")
                    transaction_dict = {}
                    for i in range(len(head_list)):
                        key = head_list[i]
                        value = content_list[i]
                        transaction_dict[key] = value
                transaction_list.append(transaction_dict)
            return transaction_list
    except Exception:
        return []


# print(csv_operations('../data/transactions.csv'))


@log(filename="../logs/transaction_reader.log")
def excel_operation(file_path: str) -> list[dict]:
    """Функция принимет путь к файлу формата Excel и после считывания выдает список
    словарей, где ключи это заголовок таблицы, а значения это содержимое рядов
    в соответсвии с заголовками"""
    try:
        with open(file_path, encoding="utf-8"):
            reader = pd.read_excel(file_path)
            transaction_list = reader.to_dict(orient="records")
            return transaction_list
    except Exception:
        return []


# print(excel_operation("../data/transactions_excel.xlsx"))
