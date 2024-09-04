import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account

# тестирование функций

# тестирование get_mask_card_number


@pytest.mark.parametrize("card_number, expected_result", [
    ('0000000000000000', '0000 00** **** 0000'),
    ('1234567890', '1234 56** **** 7890'),
    ('12', '12 ** **** 12'),
    ('0', '0 ** **** 0'),
    (' ', '** ****'),
    ('73654108430135874305', '7365 41** **** 4305')
])
def get_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result
