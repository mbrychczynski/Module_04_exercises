# 01. Napisz program, który tworzy listę kwadratów liczb od 1 do 10 z użyciem list comprehension.

list = [pow(square, 2) for square in range(1,11)]

print(list)