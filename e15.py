# 15. Napisz program, który przyjmuje funkcję jako argument i wywołuje ją wewnątrz innej funkcji.

def greet(name):
    return f"Hello, {name}!"


def call_function(func, name):
    result = func(name)
    return result


name = "Magda"
print(call_function(greet, name))
