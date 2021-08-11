T = 10

for t in range(1, T+1):
    lst = []
    _ = int(input())
    for i in range(100):
        lst.append(list(map(int, input().split())))

    max = 0
    for i in range(100):
        max += lst[0][i]


    for i in range(100):
        total = 0
        for j in range(100):
            total += lst[i][j]
        if max < total:
            max = total

    for j in range(100):
        total = 0
        for i in range(100):
            total += lst[i][j]
        if max < total:
            max = total

    total = 0
    for i in range(100):
        total += lst[i][i]

    if max < total:
        max = total

    total = 0
    for i in range(100):
        total += lst[99 - i][i]

    if max < total:
        max = total

    print('#{} {}'.format(t, max))
