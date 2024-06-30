# 13. Napisz generator, który generuje pierwszych 10 liczb z ciągu Fibonacciego.

def fibb_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


gen = fibb_gen(10)
print(type(gen))
for g in gen:
    print(g)

gen = fibb_gen(10)
print(list(gen))