# 27. Napisz program, który definiuje zmienne z określonymi typami, a następnie uruchom mypy,
# aby sprawdzić zgodność typów.

def suma(a: int, b: float) -> int:
    return a + int(b)


print(suma(3,5))
# Success: no issues found in 1 source file