import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор 'log', автоматически регистрирует детали выполнения передаваемой функций,
    такие как время вызова и конец выполнения, имя функции, передаваемые аргументы,
    результат выполнения и информация об ошибках в заданный файл в папку 'data',
    или в консоль если файл сохранения не задан."""

    def wrapper(func: Callable) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            # start_time = datetime.datetime.now()
            call_time = f"Дата и время вызова: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
            function_name = f"Функция: {func.__name__}"
            arguments_passed = f"{args, kwargs}"
            try:
                result_fanc = func(*args, **kwargs)
                execution_result = f"Результат: {result_fanc}"
            except Exception as e:
                execution_result = f"Результат: {func.__name__} error: {str(e)}, Inputs: {arguments_passed}"
                result_fanc = None
            # end = datetime.datetime.now()
            # lead_time = f"Время выполнения {":".join(str(end - start_time).split('.')[:1])}"
            if filename:
                with open("../data/" + filename, "a", encoding="UTF-8") as f:
                    f.write(f"{call_time}\n{function_name}\n{execution_result}\n")
            else:
                print(f"{call_time}\n{function_name}\n{execution_result}\n")

            return result_fanc

        return inner

    return wrapper
