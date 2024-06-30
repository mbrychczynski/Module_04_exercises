# 28. Napisz program, który używa funkcji all i any do sprawdzenia,
# czy wszystkie lub niektóre elementy listy spełniają określony warunek.

ages = [10, 18, 20, 22, 17, 16]
is_adult = [True if age >= 18 else False for age in ages]

print(ages)
print(is_adult)
print(any(is_adult))
print(all(is_adult))
