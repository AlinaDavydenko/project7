def get_mask_account(account_number: str) -> str:
    """ принимает на вход номер счета и возвращает его маску """
    return f'**{account_number[-4:]}'  # выход функции

account_number = input()
a = get_mask_account(account_number)
print(a)

