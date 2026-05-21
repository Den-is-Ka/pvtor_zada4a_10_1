from pvtor_zada4a_10_1.widget import get_date


def test_get_date():
    date_string = "2024-03-11T02:26:18.671407"
    result = get_date(date_string)
    assert result == '11.03.2024'
