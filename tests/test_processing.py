import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_positive(list_dic):
    assert filter_by_state(list_dic) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.mark.parametrize('meaning, status, result', [
    ([], 'CANCELED', []),
    ('list', 'CANCELED', []),
    ([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], 'CANCELED', [])])
def test_filter_by_state_positive_not_list(meaning, status, result):
    assert filter_by_state(meaning, status) == result


def test_filter_by_state_positive_status(list_dic):
    assert filter_by_state(list_dic, 'CANCELED') == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


def test_sort_by_date_positive_positive(list_dic):
    assert sort_by_date(list_dic) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_sort_by_date_positive_positive_rivers(list_dic):
    assert sort_by_date(list_dic, False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


@pytest.mark.parametrize('list_d, result', [(
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}
         ],
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'},
         {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
         ]),
    ([
         {'id': 594226727, 'state': 'EXECUTED', 'date': '2020.11.16 15:43:32.249588'},
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2020-11-15'},
         {'id': 594226727, 'state': 'EXECUTED', 'date': '2020/11/14 15:43:32.249588'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2020-10-17 09:40:33.614581+02:00'},
         {'id': 615064591, 'state': 'EXECUTED', 'date': 'Thu Oct 17 17:10:28 2019'},
         {'id': 615064591, 'state': 'EXECUTED', 'date': 'Thursday, 17. October 2019 5:10PM'},
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
     ],
     [
         {'id': 594226727, 'state': 'EXECUTED', 'date': '2020-11-16T15:43:32.249588'},
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2020-11-15T00:00:00.000000'},
         {'id': 594226727, 'state': 'EXECUTED', 'date': '2020-11-14T15:43:32.249588'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2020-10-17T09:40:33.614581'},
         {'id': 615064591, 'state': 'EXECUTED', 'date': '2019-10-17T17:10:28.000000'},
         {'id': 615064591, 'state': 'EXECUTED', 'date': '2019-10-17T17:10:00.000000'},
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
     ])
]
                         )
def test_sort_by_date_positive(list_d, result):
    assert sort_by_date(list_d) == result
