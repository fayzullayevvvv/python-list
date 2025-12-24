lst = []

while True:
    name = input('Name: ')
    if name:
        lst.append(name)
    else:
        break

print(len(lst))