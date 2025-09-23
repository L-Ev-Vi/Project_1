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
        assert cap.out == (f"{datetime.datetime.now()}\n"
                           "retune_resul(n)\n"
                           "Hello, World! "
                           "Hello, World! Hello, World!\n")