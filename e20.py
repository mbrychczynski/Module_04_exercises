# 20. Napisz funkcję, która przyjmuje dowolną liczbę argumentów liczbowych i zwraca ich sumę.

def suma(*args):
    return sum(args)

print(suma(10,10,10,10,10))