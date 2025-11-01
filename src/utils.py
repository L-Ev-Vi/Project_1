import json
import logging
from json import JSONDecodeError

util_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
util_logger.addHandler(file_handler)
util_logger.setLevel(logging.DEBUG)


def from_json_to_list(file: str) -> list:
    """Функция, принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    util_logger.info("Запуск программы почтению json файла")
    try:
        with open("data/" + file, "r", encoding="UTF-8") as f:
            try:
                data_file = json.load(f)
            except JSONDecodeError:
                util_logger.error("Ошибка: не возможно декодировать JSON-данные")
                return []
    except FileNotFoundError:
        util_logger.error(f"Ошибка: файл '{file}' отсутствует или не найден")
        return []
    if type(data_file) is not list:
        util_logger.warning(f"Предупреждение: файл '{file}' не содержит не одного списка")
        return []
    if len(data_file) == 0:
        util_logger.warning(f"Предупреждение: файл '{file}' содержит пустой список")
        return []
    util_logger.info(f"Успешное чтение данных из файла '{file}' содержит пустой список")
    return data_file
