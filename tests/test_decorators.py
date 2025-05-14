import pytest

from src.decorators import my_function

def test_log():
    """тестирование вывоза ошибки декоратора log() с параметрами при вводе
    некорректных аргументов проверочной функции my_function()"""
    with pytest.raises(Exception):
        my_function(1, "2")


def test_log_consol(capsys):
    """тестирования вывода сообщений в консоль декоратора
    log() если не указан файл для сохранения логов"""
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function is ok\n"
