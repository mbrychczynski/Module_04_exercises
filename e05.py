# 05. Napisz program, który tworzy listę pierwszych liter każdego słowa w podanym zdaniu z użyciem list comprehension.

text = "Jakies przykladowe zdanie do zadania"
char_list = [char[0::-1] for char in text.split()]
print(char_list)