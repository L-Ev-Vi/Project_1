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
            pass

        return inner

    return wrapper
