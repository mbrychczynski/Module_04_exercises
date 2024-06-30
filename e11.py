# 11. Napisz program, który używa operatora walrus do jednoczesnego przypisania i sprawdzenia,
# czy wpisana przez użytkownika liczba jest dodatnia.

def is_positive(number):
    if is_positive_number := number > 0:
        print(is_positive_number)
    else:
        print(is_positive_number)


is_positive(-10)
is_positive(0)
is_positive(10)