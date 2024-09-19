# модуль для размещения декораторов
from datetime import time
from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:  # создаём будущий декоратор логирования
    """ запись вызова функции и её результат в файл или в консоль """
    def timer(func):  # определяем функцию подсчёта времени исполнения функции
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                time_1 = time()
                result = sum(args)
                time_2 = time()
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'my function start in {time_1} \nmy function is ok \nmy function stop in {time_2}')
                else:
                    print(f'my function start in {time_1} \nmy function is ok \nmy function stop in {time_2}')
            except Exception as e:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(f'my function error: {e}. Input: {args}, {kwargs}')
                else:
                    print(f'my function error: {e}. Input: {args}, {kwargs}')
            return result
        return wrapper
    return timer


@log(filename='mylog.txt')
def my_function(x: int, y: int) -> int:
    """ суммирует два значения """
    return x+y


a = my_function(x=5, y=8)
print(a)

