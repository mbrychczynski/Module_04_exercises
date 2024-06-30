# 31. Napisz funkcję, która zwraca funkcję do mnożenia podanej liczby przez inną liczbę.

def multiplier(x):
    def multiply_by_multiplier(y):
        return x*y
    return multiply_by_multiplier


times_two = multiplier(2)
print(times_two(10))
