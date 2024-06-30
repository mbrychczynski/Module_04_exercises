# 30. Napisz funkcję, która zwraca inną funkcję jako wynik. Wywołaj zwróconą funkcję.

def outer(name):
    def inner():
        print(f'Hi {name}! I\'m Inner.')
    return inner


x = outer("Mateusz")
x()
