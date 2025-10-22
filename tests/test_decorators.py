import datetime
import unittest
from unittest.mock import patch

from src.decorators import log


# Тест вывода в консоль при успешной операции
def test_log_output_to_the_console(capsys):
    @log()
    def retune_resul(n):
        return n * 2

    retune_resul("Hello, World! ")
    captured = capsys.readouterr()
    assert captured.out == (
        f"Дата и время вызова: {(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M')}\n"
        f"Функция: retune_resul\n"
        f"Результат: Hello, World! Hello, World! \n\n\n"
    )


# Тест вывода в консоль при возникновении ошибки
def test_log_output_to_the_console_error(capsys):
    @log()
    def retune_resul_error(n):
        if n <= 0:
            raise ValueError("ValueError")
        print("Hello, World!")

    retune_resul_error(0)
    captured = capsys.readouterr()
    assert captured.out == (
        f"Дата и время вызова: {(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M')}\n"
        f"Функция: retune_resul_error\n"
        f"Результат: retune_resul_error error: ValueError, Inputs: {((0,), {})}\n\n\n"
    )


# Тест вывода в консоль при возникновении ошибки
def test_log_output_to_the_console_err(capsys):
    @log()
    def funcs(n):
        if type(n) is not int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "ok"

    funcs("5")
    captured = capsys.readouterr()
    assert captured.out == (
        f"Дата и время вызова: {(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M')}\n"
        f"Функция: funcs\n"
        f"Результат: funcs error: TypeError, Inputs: {(("5",), {})}\n\n\n"
    )


# Тест вывода в консоль при успешной операции
def test_log_console(capsys):
    @log()
    def funcs(n):
        if type(n) is not int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "ok"

    funcs(5)
    captured = capsys.readouterr()
    assert captured.out == (
        f"Дата и время вызова: {(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M')}\n"
        f"Функция: funcs\n"
        f"Результат: ok\n\n\n"
    )


def test_log_file():
    @log(filename=None)
    def log_in_file(n):
        if type(n) is not int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "Hello" * 2

    assert log_in_file(2) == "HelloHello"


class TestLog(unittest.TestCase):

    # Тест записи в файл при успешной операции
    @patch("builtins.open")
    def test_log_file(self, mock_opens):

        @log("filename.txt")
        def log_in_file(n):
            if type(n) is not int:
                raise TypeError("TypeError")
            if n <= 0:
                raise ValueError("ValueError")
            return "Hello" * n

        self.assertEqual(log_in_file(2), "HelloHello")

    # Тест записи в файл при возникновении ошибки
    @patch("builtins.open")
    def test_log_file_err(self, mock_opens):
        @log("test_file.txt")
        def log_in_file(n):
            if type(n) is not int:
                raise TypeError("TypeError")
            if n <= 0:
                raise ValueError("ValueError")
            return "Hello" * n

        self.assertEqual(log_in_file("2"), None)
