import datetime
import os
from pathlib import Path

import pytest

from src.decorators import log


# Тест вывода в консоль при успешной операции
def test_log_output_to_the_console(capsys):
    @log()
    def retune_resul(n):
        return n * 2

    retune_resul("Hello, World! ")
    captured = capsys.readouterr()
    assert captured.out == (f"Дата и время вызова: {datetime.datetime.now()}\n"
                            f"Функция: retune_resul\nРезультат: Hello, World! Hello, World! \n\n")


# Тест вывода в консоль при возникновении ошибки
def test_log_output_to_the_console_error(capsys):
    @log()
    def retune_resul_error(n):
        if n <= 0:
            raise ValueError("ValueError")
        print("Hello, World!")

    retune_resul_error(0)
    captured = capsys.readouterr()
    assert captured.out == (f"Дата и время вызова: {datetime.datetime.now()}\nФункция: retune_resul_error\n"
                            f"Результат: retune_resul_error error: ValueError, Inputs: {((0,), {})}\n\n")


# Тест вывода в консоль при возникновении ошибки
def test_log_output_to_the_console_err(capsys):
    @log()
    def funcs(n):
        if type(n) != int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "ok"

    funcs("5")
    captured = capsys.readouterr()
    assert captured.out == (f"Дата и время вызова: {datetime.datetime.now()}\n"
                            f"Функция: funcs\nРезультат: funcs error: TypeError, Inputs: {(("5",), {})}\n\n")


# Тест вывода в консоль при успешной операции
def test_log_console(capsys):
    @log()
    def funcs(n):
        if type(n) != int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "ok"

    funcs(5)
    captured = capsys.readouterr()
    assert captured.out == f"Дата и время вызова: {datetime.datetime.now()}\nФункция: funcs\n"f"Результат: ok\n\n"


# Тест записи в файл при успешной операции
def test_log_file():
    @log('test_file.txt')
    def log_in_file(n):
        if type(n) != int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "Hello" * n

    log_in_file(2)
    with open('../data/test_file.txt', 'r', encoding='UTF-8') as f:
        result = f.read()
        x = (f"Дата и время вызова: {datetime.datetime.now()}\n"
             f"Функция: log_in_file\n"
             "Результат: HelloHello\n"
             "")
    assert result == x
    os.remove(Path(str(Path('test_file.txt').absolute()).replace('tests', 'data')))


# Тест записи в файл при возникновении ошибки
def test_log_file_err():
    @log('test_file.txt')
    def log_in_file(n):
        if type(n) != int:
            raise TypeError("TypeError")
        if n <= 0:
            raise ValueError("ValueError")
        return "Hello" * n

    log_in_file('2')
    with open('../data/test_file.txt', 'r', encoding='UTF-8') as f:
        result = f.read()
        x = (f"Дата и время вызова: {datetime.datetime.now()}\n"
             f"Функция: log_in_file\n"
             f"Результат: log_in_file error: TypeError, Inputs: {(("2",), {})}\n"
             "")
    assert result == x
    os.remove(Path(str(Path('test_file.txt').absolute()).replace('tests', 'data')))
