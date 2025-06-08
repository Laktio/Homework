import json

import mypy.types

from src.decorators import log


@log(filename="../logs/utils.log")
def operations_transform(operations_file: list) -> list:
    """Данная функция принимaет путь к файлу JSON из дирректории data преобразует данные json
    в данные python и выводит их в виде списка. обрабатывает ошибки возникающие если файл
    пустой, содержит не список или не найден - функция возвращает пустой список.
    :rtype: list"""
    try:
        with open(operations_file, encoding="utf-8") as json_file:
            operations_list = json.load(json_file)
            return operations_list
    except json.JSONDecodeError:
        return []
    except TypeError:
        return []
    except KeyError:
        return []
    except ValueError:
        return []
    except FileNotFoundError:
        return []


# print(operations_transform("../data/operations.json")[0])
