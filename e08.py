# 08. Napisz program, który tworzy słownik z liczbami od 1 do 10 jako kluczami i ich kwadratami jako wartościami,
# ale tylko dla liczb parzystych, z użyciem dictionary comprehension.

pow_dict = {num: pow(num, 2) for num in range(1,11) if num % 2 == 0}
print(pow_dict)