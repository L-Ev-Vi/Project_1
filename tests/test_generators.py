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


def test_filter_by_currency_zero():
    resul = {}
    gen = filter_by_currency([], "USD")
    assert next(gen) == resul
    # assert next(gen) == {}
    # assert next(gen) == resul


def test_filter_by_currency_non(list_transactions):
    resul = {}
    gen = filter_by_currency(list_transactions, "EUR")
    assert next(gen) == resul


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


def test_card_number_generator():
    gen = card_number_generator(1, 1)
    result = "0000 0000 0000 0001"

    assert next(gen) == result


def test_card_number_generator_zero():
    gen = card_number_generator(0, 1)
    result = "0000 0000 0000 0001"

    assert next(gen) == result


def test_card_number_generator_negative():
    gen = card_number_generator(-5, 0)
    result = "0000 0000 0000 0001"

    assert next(gen) == result


def test_card_number_type():
    gen = card_number_generator()
    result = str

    assert type(next(gen)) == result
