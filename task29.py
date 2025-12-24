lst = []

for i in range(10):
    num = int(input('num: '))
    if num not in lst:
        lst.append(num)

print(lst)