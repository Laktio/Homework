import logging

from mypy.types import UnionType


def log(filename=None):
    """Функция декоратор для логирования работы функций в файл (если в параметрах декоратора указан файл)
    или в консоль"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename != None:
                logging.basicConfig(
                    filename="mylog.txt",
                    level=logging.DEBUG,
                    filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s",
                )
                try:
                    func(*args, **kwargs)
                    logging.debug(f"{func.__name__} is ok")
                except Exception:
                    logging.debug(f"{func.__name__} error: TypeError. Inputs {args}, {kwargs}")
                    raise Exception("error")
            elif filename == None:
                try:
                    func(*args)
                    print(f"{func.__name__} is ok")
                except Exception:
                    print(f"{func.__name__} error: TypeError. Inputs {args}, {kwargs}")
                    raise Exception("error")

        return wrapper

    return decorator


# @log(filename="mylog.txt")
# def my_function(x, y):
#     """Проверочная функция работы декоратора"""
#     return x + y


# print(my_function(1, "2"))
