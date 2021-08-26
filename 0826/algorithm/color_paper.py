# jungol 1438 '색종이(초)'

n = int(input())

MAP = [[False for _ in range(100)] for _ in range(100)]

for _ in range(n):
    st_j, st_i = map(int, input().split())

    for i in range(st_i, st_i + 10):
        for j in range(st_j, st_j + 10):
            MAP[i][j] = True

area = 0
for i in range(100):
    for j in range(100):
        if MAP[i][j]:
            area += 1

print(area)