words = ['apple', 'cow', 'alla', 'kok', 'TV']

polindrom = []
for i in words:
    if i.lower() == i[::-1].lower():
        polindrom.append(i)

print(polindrom)