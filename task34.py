lst = [int(input('num: ')) for i in range(6)]
result = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == 10:
            result.append((lst[i], lst[j]))

print(result)