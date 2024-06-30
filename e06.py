# 06. Napisz program, który tworzy zbiór unikalnych znaków z podanego słowa z użyciem set comprehension.

word = "abcdeabcdeabcde"

unique_chars = {char for char in word}
print(unique_chars)