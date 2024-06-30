# 26. Napisz program, który używa adnotacji do określenia typów argumentów i zwracanej wartości funkcji.

def suma(a: 'pierwsza liczba', b: 'druga liczna') -> 'suma liczby a oraz b':
    return a+b


print(suma(5,1))