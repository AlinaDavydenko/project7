# Список значений для функции filter_by_state
lists_of_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


# Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
def filter_by_state(lists_of_data: list[dict[str]], state: str = 'EXECUTED') -> list[dict[str]]:
    """ принимает на вход список словарей, возвращает новый список,отсортированный по значению state."""
    new_list_of_data = []
    for list_of_data in lists_of_data:
        for element in list_of_data:
            if list_of_data['state'] == 'EXECUTED':
                new_list_of_data.append(list_of_data)
    return new_list_of_data


# Функция возвращает новый список, отсортированный по дате
def sort_by_date(lists_of_data: list[dict[str]]) -> list:
    """ принимает список словарей и необязательный параметр, задающий порядок сортировки """
    sorted_list = sorted(lists_of_data, key = lambda x: x['date'], reverse = True)
    return sorted_list


a = filter_by_state(lists_of_data)  # вызов 1 функции
print(a)

b = sort_by_date(lists_of_data)  # вызов 2 функции
print(b)

