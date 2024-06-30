# 23. Napisz program, który formatuje bieżącą datę i czas z użyciem f-stringów.
import datetime

now = datetime.datetime.now()
print(f'{now:%d/%m/%Y}')