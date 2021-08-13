lst = [
    [3, 2, 7, 9],
    [5, 1, 2, 3],
    [3, 2, 7, 9],
    [3, 2, 7, 9],
    [1, 2, 3, 4],
    [4, 3, 2, 1]
]

pattern = [3, 2, 7, 9]

cnt = 0
for floor in lst:
    if floor == pattern:
        cnt += 1

print(cnt)