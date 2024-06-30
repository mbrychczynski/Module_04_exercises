# 21. Napisz funkcję, która przyjmuje dowolną liczbę argumentów nazwanych i zwraca je jako słownik,
# w którym klucze posortowane są w kolejności alfabetycznej.

def sort_alfabetic(**kwargs):
    return dict(sorted(kwargs.items()))


print(sort_alfabetic(name="Mateusz", age=1, legs=2, arms=2, eye_color="Brown"))