import pytest
from mypy.types import NoneType

from src.decorators import log


def test_log():
    """тестирование вывоза ошибки декоратора log() с параметрами при вводе
    некорректных аргументов проверочной функции my_function()"""

    @log(filename="mylog.txt")
    def my_function(x, y):
        """Проверочная функция работы декоратора"""
        return x + y

    with pytest.raises(Exception):
        my_function(1, "2")


def test_log_consol(capsys):
    """тестирования вывода сообщений в консоль декоратора
    log() если не указан файл для сохранения логов"""

    @log(filename=None)
    def my_function(x, y):
        """Проверочная функция работы декоратора"""
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function is ok\n"
