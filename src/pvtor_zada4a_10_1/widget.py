from pvtor_zada4a_10_1.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: int | str) -> str:
    """Функция маскировки номера карты и счета."""
    stroka = str(info)
    stroka_2 = stroka.split()
    finish_element = stroka_2[-1]
    too_element = stroka_2[:-1]
    name = " ".join(too_element)

    if name == "счет" or name == "Счет":
        masked_number = get_mask_account(finish_element)
    else:
        masked_number = get_mask_card_number(finish_element)

    itog = f"{name} {masked_number}"
    return itog


def get_date(date_string: str) -> str:
    """Функция для получения даты из строки."""
    stroka = date_string.split("T")
    date_parts = stroka[0].split("-")
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]
    finish = f"{day}.{month}.{year}"
    return finish


if __name__ == "__main__":  # pragma: no cover
    info = "Счет 73654108430135874305"
    result = mask_account_card(info)
    print(result)


    info = "Visa Platinum 7000792289606361"
    result = mask_account_card(info)
    print(result)


    date_string = "2024-03-11T02:26:18.671407"
    result = get_date(date_string)
    print(result)
