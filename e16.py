# 16. Napisz prosty dekorator, który wypisuje komunikat przed i po wywołaniu funkcji.

def print_func():
    print('Jestem funkcja')


def almost_decorator(func):
    print('Przed f')
    func()
    print('Po f')


almost_decorator(print_func)