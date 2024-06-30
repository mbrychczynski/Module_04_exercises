# 04. Napisz program, który tworzy listę, gdzie liczby z zakresu 1-10 są podwojone jeśli są parzyste,
# a potrojone jeśli są nieparzyste, z użyciem list comprehension.

num_list = [num * 2 if num % 2 == 0 else num * 3 for num in range(1,11)]

print(num_list)