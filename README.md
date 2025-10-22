# Prodject_1
## *Виджет банковских операций*

Это проект виджета, который получает данные о банковских картах и счетах клиента, 
и даты проведения финансовых операций. Он предоставляет все транзакции 
за указанный временной интервал и может отсортировать их по статусу выполнения 
(например, выполненные или невыполненные).

### *Содержание* 
- [Структура проекта](#Структура-проекта)
- [Установка](#установка)
- [Пример использование](#пример-использование)
- [Тестирование](#тестирование)
- [Команда проекта](#Команда-проекта)
- [Цель проекта](#цель-проекта)

### Структура проекта
+ src/masks.py — модуль, скрывающий часть банковских данных
+ src/widget.py — модуль, который получает банковские данные и 
дату операции, скрывает часть банковских данных и 
форматирует дату
+ data/operations.json — это файл содержащий список банковских операций с различными счетами и валютами в формате .JSON 
(JavaScript Object Notation)
+ data/transactions.csv — это файл содержащий список банковских операций с различными счетами и валютами в формате .CSV 
(Comma-Separated Values — значения, разделенные запятыми)
+ data/transactions_excel.xlsx — это файл содержащий список банковских операций с различными счетами и валютами в формате 
.XLSX (формат файла для электронных таблиц Microsoft Excel)
+ src/processing.py — модуль, сортирующий операции по дате и выполнению
+ src/generators.py — модуль, который выводит данные по транзакциям и их описание, а также генерирует 16-и значные номера карт 
+ src/decorators.py — этот модуль использоваться для размещения декораторов
+ src/utils.py — этот модуль использоваться для десериализации файлов в формате .json в объекты python
+ src/external_api.py — этот модуль использоваться для конвертации иностранной валюты в рубли через HTTP-запрос на интернет 
ресурс https://apilayer.com/exchangerates_data-api
+ src/reading_csv_and_xlsx.py — этот модуль использоваться для считывания финансовых операций из CSV- и XLSX-файлов
+ tests/ — пакет с модулями для проверки работоспособности и отладки ПО виджета

### Установка
Чтобы работать с проекта необходимо:
1. Скачать и установить интерпретатор [Python](https://www.python.org/downloads/) версии-3.13 и выше;
2. Установить интегрированную среду разработки (IDE), например [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows);
3. Установить Менеджер пакетов *poetry* 
    - используя`pip install poetry`;
    - или `curl -sSL https://install.python-poetry.org | python3` - для macOS и Linux
    - и `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python` - для Windows
4. Скачать и установить [Git](https://git-scm.com/downloads/win);
5. Загрузить проект в IDE через инструмент *'clone repository'* или команду `git clon`
   используя ключь: 
    - SSH: `git@github.com:L-Ev-Vi/Project_1.git`
    - или HTTPS: `https://github.com/L-Ev-Vi/Project_1.git`;
6. Установить зависимости проекта, выполнив команду `poetry install`;
7. В некоторых случаях может не корректно устанавливаться пакет `dateutil`, в этом случае можно установить пакет в ручную:
    - через `Terminal` используя команду `poetry add --group dev python-dateutil`
    - или через `pip install python-dateutil`

### Пример использования
Пример использования программы в модуле `processing.py`
```
if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
    )

if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
```
Пример использования программы в модуле `widget.py`
```
if __name__ == '__main__':
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))

if __name__ == '__main__':
    print(get_date("2024-03-11T02:26:18.671407"))
```
Пример использования программы в модуле `generators.py`
```
if __name__ == '__main__':
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
             "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"},
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]

    gen1 = filter_by_currency(transactions, "USD")

    for _ in range(3):
        print(next(gen1))

    print()
    gen2 = transaction_descriptions(transactions)

    for _ in range(2):
        print(next(gen2))

    print()
    gen3 = card_number_generator()

    for _ in range(5):
        print(next(gen3))
```
Пример использования декоратора "log" из модуля `decorators.py`

Результата вызова функции, будет храниться в файле с результатами логированияв в директории 'data'.
```
from src.decorators import log


if __name__ == '__main__':

    @log()
    def retune_resul(n):
        return n * 2
    
    retune_resul("Hello, World")
```
#Результат вывода в консоль:

`>> Дата и время вызова: 2025-09-26 23:06
Функция: retune_resul
Результат: Hello, WorldHello, World`

Пример использования программы в модуле `reading_csv_and_xlsx.py`
Модуль выполняет чтение файлов содержащих данные о банковских операциях в форматах .csv и .xlsx, и возвращает информацию 
в виде списка словарей, где каждый словарь это одна транзакция.
Запуска программы из модуля:
```
if __name__ == '__main__':
    path_CSV = 'transactions.csv'
    path_XLSX = 'transactions_excel.xlsx'
    
    print(from_xlsx_to_list(path_XLSX))
    print(from_csv_to_list(path_CSV))
```

### Тестирование
Проверка работоспособность программы проводится в пакете (директории) `tests`, структуру которой составляют:
- модуль `conftest.py` для хранения фикстур;
-  и тестируемые модули с прификсом `test` (test_masks.py, test_widget.py, test_processing.py, test_generators.py, 
test_decorators.py, test_utils.py, test_external_api.py, test_reading_csv_and_xlsx.py)
В модулях задаются параметры для функций, и проводится отработка сценариев поведения программы.
- Пример:
```
import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 15684", "Visa Gold ***84"),
        ("MasterCina 6571552397456239821", "MasterCina 6571 55** **** **** 821"),
    ],
)
def test_mask_account_card_positive(data, result):
    assert mask_account_card(data) == result
```
- Для проведения тестов используется фреймворк 'pytest', он устанавливается вместе с зависимостями проекта, но также 
возможно выполнить установку через команду: `poetry add --group dev pytest`
- Запуск тестов производится через команду `pytest` (или конфигурацию используемой IDE)

Для формирования отчёта о том какое количество кода охвачено тестами в процентном соотношении, устанавливается библиотека 
'pytest-cov' через команду: `poetry add --group dev pytest-cov`

Чтобы запустить тесты с оценкой покрытия, можно воспользоваться следующими командами:
+ `pytest --cov` — при активированном виртуальном окружении.
+ `poetry run pytest --cov` — через poetry.
+ `pytest --cov-report term-missing --cov=src` — проверка покрытия тестом с выводом строк
+ `pytest --cov=src --cov-report=html` — чтобы сгенерировать отчет о покрытии в HTML-формате, где 
src — пакет c модулями, которые тестируем. 
  - при последнем варианте был сгенерирован отчет `index.html` который храниться в папке `htmlcov`.

### Команда проекта
- Евгений Лобачёв(GitHub: L-Ev-Vi) — студент курса "Python - разработчик" 

### Цель проекта
Повышения уровня финансовой грамотности и эффективное управления личным временем.

![Python](https://images.techinsider.ru/upload/img_cache/761/761cc2dc61090b0411ca5366422a1eca_ce_1024x683x0x0_cropped_510x340.webp)
