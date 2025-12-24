lst = []
while True:
    word = input('word: ')
    if word:
        lst.append(word)
    else:
        break


result = lst[0]

for i in lst:
    if len(i) > len(result):
        result = i

print(result)