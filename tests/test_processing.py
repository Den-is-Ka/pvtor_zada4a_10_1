import pytest

from pvtor_zada4a_10_1.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    operations = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 4, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(operations, "EXECUTED") == [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 4, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_2(operations):
    assert filter_by_state(operations, "EXECUTED") == [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date(operations):
    assert sort_by_date(operations) == [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 4, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
        {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
