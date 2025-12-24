lst1 = []
lst2 = []
lst3 = []

while True:
    word = input('word: ')
    if word:
        if len(word) <= 3:
            lst1.append(word)
        elif 4 <= len(word) <= 6:
            lst2.append(word)
        else:
            lst3.append(word)
    else:
        break

print(lst1)
print(lst2)
print(lst3)