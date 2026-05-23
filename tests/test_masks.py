from pvtor_zada4a_10_1.masks import get_mask_account, get_mask_card_number


def test_mask_card_number():
    card_number = "7000792289606361"
    result = get_mask_card_number(card_number)
    assert result == "7000 79** **** 6361"


def test_mask_card_number_int():
    card_number = 7000792289606361
    result = get_mask_card_number(card_number)
    assert result == "7000 79** **** 6361"


def test_mask_card_number_anoter_num():
    card_number = "7636192289606361"
    result = get_mask_card_number(card_number)
    assert result == "7636 19** **** 6361"


def test_get_mask_account():
    account_num = "40817810000000006578"
    result = get_mask_account(account_num)
    assert result == "**6578"


def test_get_mask_account_int():
    account_num = 40817810000000006578
    result = get_mask_account(account_num)
    assert result == "**6578"


def test_get_mask_account_num():
    account_num = "1212"
    result = get_mask_account(account_num)
    assert result == "**1212"


def test_get_mask_account_num_2():
    account_num = "12"
    result = get_mask_account(account_num)
    assert result == "**12"
