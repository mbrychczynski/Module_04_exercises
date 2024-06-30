# 19. Napisz dekorator, który do tekstu zwracanego przez funkcję dodaje dokładną godzinę,
# w której wywołana została funkcja.
import datetime


def print_func():
    def wrapper():
        print("Jakis tam tekst")

    return wrapper


def time_decorator(func):
    def wrapper():
        func()
        print(f'Time: {datetime.datetime.now()}')

    return wrapper

x = time_decorator(print_func())
x()