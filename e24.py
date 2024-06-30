# 24. Napisz program, który formatuje liczbę zmiennoprzecinkową do dwóch miejsc po przecinku z użyciem f-stringów.
import random


def form_int(number):
    return f"{number:.2f}"


print(form_int(2.143232))
print(form_int(random.random()))
print(form_int(3))
