# 10. Napisz program, który używa operatora walrus do jednoczesnego przypisania i sprawdzenia, czy liczba jest parzysta.

def is_even(number):
    if is_even_number := (number % 2 == 0):
        return is_even_number
    else:
        return is_even_number

print(is_even(1))
print(is_even(2))
print(is_even(12))
print(is_even(21))