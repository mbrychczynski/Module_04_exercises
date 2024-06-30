# 22. Napisz funkcję, która przyjmuje zarówno *args, jak i **kwargs, i wypisuje je.

def print_args_kwargs(*args, **kwargs):
    print('Argumenty pozycyjne (*args):')
    for arg in args:
        print(arg)

    print('\nArgumenty nazwane (**kwargs):')
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_args_kwargs(1,2,"b",4, a=1, name="Mateusz", c=True)