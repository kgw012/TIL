#swea 12595 '마법사의 사냥'

di = [1, 1, -1, -1]
dj = [1, -1, 1, -1]

T = 5
for t in range(1, T+1):
    N = int(input())
    MAP = [[-1 for j in range(N + 2)] for i in range(N + 2)]

    for i in range(1, N + 1):
        lst = list(map(int, input().split()))
        for j in range(1, N + 1):
            MAP[i][j] = lst[j - 1]
    
    K = int(input())
    
    max_total = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            total = 0
            for d in range(4):
                for k in range(1, K + 1):
                    test_i = i + di[d] * k
                    test_j = j + dj[d] * k
                    if MAP[test_i][test_j] == -1:
                        break
                    total += MAP[test_i][test_j]
            if max_total < total:
                max_total = total
    
    print('#{} {}'.format(t, max_total))