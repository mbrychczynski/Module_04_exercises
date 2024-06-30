# 12. Napisz generator, który generuje liczby od 1 do 10.

gen = (num for num in range(1,11))
print(type(gen))
for g in gen:
    print(g)