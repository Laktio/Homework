import logging


def log(filename=None):
    """Функция декоратор для логирования работы функций в файл (если в параметрах декоратора указан файл)
    или в консоль"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename is not None:
                logging.basicConfig(
                    filename=filename,
                    level=logging.DEBUG,
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(filename)s %(funcName)s %(message)s",
                )
                try:
                    func(*args, **kwargs)
                    result = func(*args, **kwargs)
                    logging.debug(f"{func.__name__} is ok, result is {result}")
                    return result
                except Exception:
                    logging.error(f"{func.__name__} error: TypeError. Inputs {args}, {kwargs}")
                    raise Exception("error")
            elif filename is None:
                try:
                    func(*args)
                    print(f"{func.__name__} is ok")
                    return None
                except Exception:
                    print(f"{func.__name__} error: TypeError. Inputs {args}, {kwargs}")
                    raise Exception("error")
            return None

        return wrapper

    return decorator


# @log(filename="mylog.txt")
# def my_function(x, y):
#     """Проверочная функция работы декоратора"""
#     return x + y


# print(my_function(1, "2"))
