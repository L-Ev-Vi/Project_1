import pytest

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_filter_by_state_positive(list_dic):
    assert filter_by_state(list_dic) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "meaning, status, result",
    [
        ([], "CANCELED", []),
        ("list", "CANCELED", []),
        ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}], "CANCELED", []),
    ],
)
def test_filter_by_state_positive_not_list(meaning, status, result):
    assert filter_by_state(meaning, status) == result


def test_filter_by_state_positive_status(list_dic):
    assert filter_by_state(list_dic, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date_positive_positive(list_dic):
    assert sort_by_date(list_dic) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_positive_positive_rivers(list_dic):
    assert sort_by_date(list_dic, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "list_d, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 594226727, "state": "EXECUTED", "date": "2020.11.16 15:43:32.249588"},
                {"id": 41428829, "state": "EXECUTED", "date": "2020-11-15"},
                {"id": 594226727, "state": "EXECUTED", "date": "2020/11/14 15:43:32.249588"},
                {"id": 939719570, "state": "EXECUTED", "date": "2020-10-17 09:40:33.614581+02:00"},
                {"id": 615064591, "state": "EXECUTED", "date": "Thu Oct 17 17:10:28 2019"},
                {"id": 615064591, "state": "EXECUTED", "date": "Thursday, 17. October 2019 5:10PM"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            [
                {"id": 594226727, "state": "EXECUTED", "date": "2020-11-16T15:43:32.249588"},
                {"id": 41428829, "state": "EXECUTED", "date": "2020-11-15T00:00:00.000000"},
                {"id": 594226727, "state": "EXECUTED", "date": "2020-11-14T15:43:32.249588"},
                {"id": 939719570, "state": "EXECUTED", "date": "2020-10-17T09:40:33.614581"},
                {"id": 615064591, "state": "EXECUTED", "date": "2019-10-17T17:10:28.000000"},
                {"id": 615064591, "state": "EXECUTED", "date": "2019-10-17T17:10:00.000000"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_positive(list_d, result):
    assert sort_by_date(list_d) == result


def test_process_bank_search_title(data_list):
    assert process_bank_search(data_list, "Перевод") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_process_bank_search_lower(data_list):
    assert process_bank_search(data_list, "вклад") == [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]


def test_process_bank_search_upper(data_list):
    assert process_bank_search(data_list, "ВКЛАД") == [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]


def test_process_bank_search_not(data_list):
    assert process_bank_search(data_list, "обналичивание") == []


def test_process_bank_operations(data_list, categories_list):
    result = process_bank_operations(data_list, categories_list)
    assert result == {"Перевод со счета на счет": 1, "Открытие вклада": 1, "Перевод организации": 1}


def test_process_bank_operations_excess(data_list, categories_list_excess):
    result = process_bank_operations(data_list, categories_list_excess)
    assert result == {"Перевод организации": 1, "Обналичивание": 0, "Неизвестная операция": 0}
