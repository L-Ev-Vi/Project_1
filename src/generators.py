from typing import Generator, Iterator


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
