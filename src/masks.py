def get_mask_card_number(card_number: str) -> str:
    """ принимает на вход номер карты и возвращает ее маску """
    return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}'  # выход функции


def get_mask_account(account_number: str) -> str:
    """ принимает на вход номер счета и возвращает его маску """
    return f'**{account_number[-4:]}'  # выход функции


card_number = str(input('Введите номер карты.'))
account_number = str(input('Введите номер счёта.'))


mask_card_number = get_mask_card_number(card_number)  # возвращает маску номера карты
mask_account = get_mask_account(account_number)  # возвращает маску номера счёта


print(mask_card_number)
print(mask_account)
