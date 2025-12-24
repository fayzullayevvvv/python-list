lst = [3, 5, 3, 2, 5, 5, 1]

top_num = lst[0]

for i in lst:
    if lst.count(i) > lst.count(top_num):
        top_num = i

print(top_num)