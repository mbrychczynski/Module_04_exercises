# 18. Napisz dekorator, który liczy, ile razy dana funkcja została wywołana.
import random


def print_func():
    def wrapper():
        print('Random text')

    return wrapper


def counting_func(func):
    randon_number = random.randint(1, 10)

    def wrapper():
        count = 0
        for number in range(randon_number+1):
            func()
            count += 1
        print(f'Number: {count}')

    return wrapper


x = counting_func(print_func())
x()
