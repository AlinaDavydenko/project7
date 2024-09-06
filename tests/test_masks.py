import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account
import sys
sys.path.append('/Users/alinadavydenko/PycharmProjects/pythonProject7/src')


# тестирование функций
# тестирование get_mask_card_number


@pytest.mark.parametrize("card_number, expected_result", [
    ('0000000000000000', '0000 00** **** 0000'),
    ('1234567890', '1234 56** **** 7890'),
    ('12', '12 ** **** 12'),
    ('0', '0 ** **** 0'),
    ('73654108430135874305', '7365 41** **** 4305')
])
def test_get_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result


# тестирование get_mask_account
@pytest.mark.parametrize('account_number, expected_result', [
    ('73654108430135874305', '**4305'),
    ('0', '**0')
])
def test_get_mask_account(account_number, expected_result):
    assert get_mask_account(account_number) == expected_result
