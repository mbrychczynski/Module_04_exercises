# 03. Napisz program, który tworzy listę, która zawiera “parzysta” lub “nieparzysta” dla liczb od 1 do 10 z użyciem
# list comprehension.

string_list = ["parzysta" if num % 2 == 0 else "nieparzysta" for num in range(1,11)]

print(string_list)