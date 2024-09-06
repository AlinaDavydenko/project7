import pytest
from src.processing import filter_by_state
from src.processing import sort_by_date


# тестирование filter_by_state
@pytest.mark.parametrize('lists_of_data, expected_result', [(
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
])
def test_filter_by_state(lists_of_data, expected_result):
    assert filter_by_state(lists_of_data) == expected_result


# тестирование sort_by_date
@pytest.mark.parametrize('lists_of_data, expected_result', [[[
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
    [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]]
])
def test_sort_by_date(lists_of_data, expected_result):
    assert sort_by_date(lists_of_data) == expected_result
