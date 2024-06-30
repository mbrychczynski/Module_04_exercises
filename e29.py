# 29. Napisz program, który łączy dwie listy (np. imiona i nazwiska) w jedną listę krotek z użyciem zip.

names = ['Ace', 'Ari', 'Scotty']
type = ['Dog', 'Dog', 'Cat']

zipped = zip(names, type)
print(dict(zipped))