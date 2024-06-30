# 25. Napisz program, który formatuje liczbę zmiennoprzecinkową jako procent z użyciem f-stringów.

def float_to_percentage(number):
    return f'{number:.2%}'


print(float_to_percentage(10))
print(float_to_percentage(0.1))