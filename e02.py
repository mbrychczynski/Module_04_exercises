# 02. Napisz program, który tworzy listę liczb parzystych od 1 do 20 z użyciem list comprehension.

even_list = [even for even in range(1,21) if even % 2 == 0]

print(even_list)