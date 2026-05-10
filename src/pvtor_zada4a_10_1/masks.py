def get_mask_card_number(card_number: int | str) -> str:
    """функция для создания маски номера карты"""
    stroka = str(card_number)
    first_part = stroka[0:4]
    second_part = stroka[4:6]
    last_part = stroka[-4:]
    mask = f"{first_part} {second_part}** **** {last_part}"
    return mask


def get_mask_account(account_num: int | str) -> str:
    """функция для создания маски номера счета"""
    stroka = str(account_num)
    last_part = stroka[-4:]
    mask_num = f"**{last_part}"
    return mask_num


if __name__ == "__main__":
    card_number = "7000792289606361"
    result = get_mask_card_number(card_number)
    print(result)

    account_num = "40817810000000006578"
    result = get_mask_account(account_num)
    print(result)
