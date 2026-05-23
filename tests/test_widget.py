import pytest

from pvtor_zada4a_10_1.widget import get_date, mask_account_card


def test_get_date():
    date_string = "2024-03-11T02:26:18.671407"
    result = get_date(date_string)
    assert result == "11.03.2024"


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.000000", "31.12.2023"),
        ("2022-01-01T00:00:00.000000", "01.01.2022"),
    ],
)
def test_get_date_3(date_string, expected):
    assert get_date(date_string) == expected


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_2():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("счет 40817810000000006578", "счет **6578"),
    ],
)
def test_mask_account_card_3(info, expected):
    assert mask_account_card(info) == expected
