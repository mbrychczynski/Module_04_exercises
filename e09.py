# 09. Napisz program, który używa operatora walrus do jednoczesnego przypisania i sprawdzenia długości listy.

list = [1, 2, 3, 4, 5, 6]
if (length := len(list)) > 0:
    print(f"Length of list is {length}")
else:
    print("Empty")
