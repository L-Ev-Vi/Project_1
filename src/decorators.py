import datetime
import time
from functools import wraps
from typing import Callable, Optional


def log(filename: Optional = None):
    """Декоратор 'log', автоматически регистрирует детали выполнения передаваемой функций,
        такие как время вызова и конец выполнения, имя функции, передаваемые аргументы,
        результат выполнения и информация об ошибках, в заданный файл или в консоль если файл сохранения не задан."""

    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            # start_time = time.time()
            call_time = f"Дата и время вызова: {datetime.datetime.now()}"
            function_name = f"Функция: {func.__name__}"
            arguments_passed = f"{args, kwargs}"
            try:
                result_fanc = func(*args, **kwargs)
                execution_result = f"Результат: {result_fanc}"
            except Exception as e:
                execution_result = f"Результат: {func.__name__} error: {str(e)}, Inputs: {arguments_passed}"
                return None
            else:
                return result_fanc
            finally:
                # end = time.time()
                # lead_time = f"Время выполнения {end - start_time}"
                if filename:
                    with open('../data/' + filename, 'a', encoding='UTF-8') as f:
                        f.write(f"{call_time}\n{function_name}\n{execution_result}\n")
                else:
                    print(f"{call_time}\n{function_name}\n{execution_result}\n")

        return inner

    return wrapper
