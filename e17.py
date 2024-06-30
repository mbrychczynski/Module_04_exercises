# 17. Napisz dekorator, który mierzy czas wykonywania funkcji.
import time


def print_func():
    print('Random text to show up')


def timer(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print(f'Time: {(end_time - start_time) * 1000}')


timer(print_func)