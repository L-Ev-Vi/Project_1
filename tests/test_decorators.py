import pytest
import datetime
import os
from pathlib import Path


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
        f"Результат: Hello, World! Hello, World! \n"
        f"Время выполнения 0:00:00\n\n"
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
        f"Результат: retune_resul_error error: ValueError, Inputs: {((0,), {})}\n"
        f"Время выполнения 0:00:00\n\n"
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
        f"Результат: funcs error: TypeError, Inputs: {(("5",), {})}\n"
        f"Время выполнения 0:00:00\n\n"
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
        f"Результат: ok\n"
        f"Время выполнения 0:00:00\n\n"
    )


# Тест записи в файл при успешной операции
def test_log_file():
    @log("test_file.txt")
    def log_in_file(n):
        if type(n) is not int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "Hello" * n

    log_in_file(2)
    with open("../data/test_file.txt", "r", encoding="UTF-8") as f:
        result = f.read()
        x = (
            f"Дата и время вызова: {(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M')}\n"
            f"Функция: log_in_file\n"
            "Результат: HelloHello\n"
            "Время выполнения 0:00:00\n"
            ""
        )
    assert result == x
    os.remove(Path(str(Path("test_file.txt").absolute()).replace("tests", "data")))


# Тест записи в файл при возникновении ошибки
def test_log_file_err():
    @log("test_file.txt")
    def log_in_file(n):
        if type(n) is not int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "Hello" * n

    log_in_file("2")
    with open("../data/test_file.txt", "r", encoding="UTF-8") as f:
        result = f.read()
        x = (
            f"Дата и время вызова: {(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M')}\n"
            f"Функция: log_in_file\n"
            f"Результат: log_in_file error: TypeError, Inputs: {(("2",), {})}\n"
            "Время выполнения 0:00:00\n"
            ""
        )
    assert result == x
    os.remove(Path(str(Path("test_file.txt").absolute()).replace("tests", "data")))
