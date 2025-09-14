from typing import Iterator

# import random


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """ Функция-генератор принимает список словарей, представляющих транзакции и вид валюты,
    результатом функции является итератор, который поочередно выдает транзакции."""
    operations_list = []
    if not transactions:
        while True:
            # Можно выводить уведомление "Нет операций с волютой {currency}"
            yield {}
            # break
    else:
        for operation in transactions:
            if any(currency_data == currency for values in operation.values() if type(values) is dict for value
                   in values.values() if type(value) is dict for currency_data in value.values()):
                operations_list.append(operation)
        if len(operations_list) == 0:
            while True:
                # Можно выводить уведомление "Нет операций с волютой {currency}"
                yield {}
                # break
        else:
            for i, operation_data in enumerate(operations_list):
                yield operation_data
                if i == len(operations_list) - 1:
                    while True:
                        # Можно выводить уведомление "Больше нет операций с волютой {currency}"
                        yield {}
                        # break


def transaction_descriptions(transactions: list) -> Iterator:
    """Функция генератор которая принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    if not transactions:
        while True:
            # Можно выводить уведомление "Нет операций"
            yield []
            # break
    else:
        new_list = [description["description"] for description in transactions if "description"]
        for i, description in enumerate(new_list):
            yield description
            if i == len(new_list) - 1:
                while True:
                    # Можно выводить уведомление "Больше нет операций"
                    yield "The end"
                    # break


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Iterator:
    """Функция генератор которая принимает значения диапазона чисел,
    и генерирует номера банковских карт в 16 значном формате "XXXX XXXX XXXX XXXX",
    где X — цифра номера карты."""
    for random_number in range(start, stop + 1):
    # while True:
    #     random_number = (random.randint(start, stop))
        if random_number <= 0:
            random_number = 1
        str_number = f"{random_number:016d}"
        card_number = f"{str_number[0:4]} {str_number[4:8]} {str_number[8:-4]} {str_number[-4:]}"
        yield card_number
