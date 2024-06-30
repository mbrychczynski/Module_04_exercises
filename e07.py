# 07. Napisz program, który tworzy słownik, gdzie kluczami są liczby od 1 do 5,
# a wartościami ich kwadraty z użyciem dictionary comprehension.

num = {num: pow(num, 2) for num in range(1,6)}

print(num)