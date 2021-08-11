T = 10

for t in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    result = 0
    for i in range(1<<n):
        total = 0
        for j in range(n):
            if i & (1<<j):
                total += lst[j]

        if total == 0:
            result += 1

    print('#{} {}'.format(t, result))