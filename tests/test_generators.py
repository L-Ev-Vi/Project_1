import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_USD(list_transactions):
    gen = filter_by_currency(list_transactions, "USD")

    result = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(gen) == result
    assert next(gen) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(gen) == {}
    # assert next(gen) == {}


def test_filter_by_currency_RUB(list_transactions):
    gen = filter_by_currency(list_transactions, "RUB")

    assert next(gen) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(gen) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(gen) == {}
    # assert next(gen) == {}


@pytest.mark.parametrize('list_, currency, result',
                         [
                             ([], "USD", {}),
                             ([{
                                 "id": 142264268,
                                 "state": "EXECUTED",
                                 "date": "2019-04-04T23:20:05.206878",
                                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                                 "description": "Перевод со счета на счет",
                                 "from": "Счет 19708645243227258542",
                                 "to": "Счет 75651667383060284188",
                             }], "EUR", {})])
def test_filter_by_currency_zero(list_, currency, result):
    gen = filter_by_currency(list_, currency)

    assert next(gen) == result


def test_transaction_descriptions(list_transactions):
    gen = transaction_descriptions(list_transactions)

    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "The end"
    # assert next(gen) == "The end"


def test_transaction_descriptions_zero():
    gen = transaction_descriptions([])

    assert next(gen) == []


@pytest.mark.parametrize('start, stop, result',
                         [
                             (1, 1, "0000 0000 0000 0001"),
                             (0, 1, "0000 0000 0000 0001"),
                             (-5, 0, "0000 0000 0000 0001"),
                             (-2, -2, "0000 0000 0000 0001"),
                             (-1, -2, "0000 0000 0000 0001"),
                             (2, 0, "0000 0000 0000 0001")
                         ])
def test_card_number_generator(start, stop, result):
    gen = card_number_generator(start, stop)

    assert next(gen) == result


def test_card_number_type():
    gen = card_number_generator()
    result = str

    assert type(next(gen)) == result
