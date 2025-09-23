import datetime
from typing import Optional, Callable
from functools import wraps


def log(filename: Optional = None):
    """Декоратор 'log', автоматически регистрирует детали выполнения передаваемой функций,
    такие как время вызова и конец выполнения, имя функции, передаваемые аргументы,
    результат выполнения и информация об ошибках, в заданный файл или в консоль если файл сохранения не задан"""

    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            call_time = f"Время вызова: {datetime.datetime.now()}\n"
            function_name = f"Функция: {func.__name__}"
            arguments_passed = f"Передаваемые аргументы:{[args], [kwargs]}"
            try:
                result = func(*args, **kwargs)
                execution_result = f"Результат: {result}"
            except Exception as n:
                execution_result = f"Результат: {func.__name__} error: {str(n)} Inputs: {arguments_passed}"
            if filename:
                with open('../date/filename', 'a', encoding='UTF-8') as f:
                    f.write(f"{call_time}\n"
                            f"{function_name}\n"
                            f"{execution_result}")
            else:
                print(f"{call_time}\n {function_name}\n {execution_result}")

        return inner

    return wrapper
