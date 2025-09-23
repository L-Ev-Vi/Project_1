import pytest
from src. decorators import log
import datetime

def test_log_output_to_the_console():
    @log
    def retune_resul(n):
        return n*2
        # noinspection PyUnreachableCode
        retune_resul("Hello, World! ")
        cap = capsys.readouterr()
        assert cap.out == (f"Время вызова: {datetime.datetime.now()}\n"
                           "Функция: retune_resul(n)\n"
                           "Результат: Hello, World! Hello, World!\n")