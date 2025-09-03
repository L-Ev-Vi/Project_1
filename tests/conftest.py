import pytest


@pytest.fixture
def old_standard():
    return 6571529785965


@pytest.fixture
def american_express():
    return 65715


@pytest.fixture
def union_pay():
    return 6571552397456239821


@pytest.fixture
def date_():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def list_dic():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_dic_replay():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_dic_play():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2020-11-15"},
        {"id": 939719570, "state": "EXECUTED", "date": "2020-10-17 09:40:33.614581+02:00"},
        {"id": 594226727, "state": "EXECUTED", "date": "2020.11.16 15:43:32.249588"},
        {"id": 594226727, "state": "EXECUTED", "date": "2020/11/14 15:43:32.249588"},
        {"id": 615064591, "state": "EXECUTED", "date": "Thursday, 17. October 2019 5:10PM"},
        {"id": 615064591, "state": "EXECUTED", "date": "Thu Oct 17 17:10:28 2019"},
    ]
