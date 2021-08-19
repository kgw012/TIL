# swea 12625 '종이 붙이기'(전용)

dp = list()
dp.append(0)
dp.append(1)
dp.append(3)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    N //= 10

    st = max(len(dp), 3)
    for i in range(st, N + 1):
        dp.append(dp[i - 1] + 2 * dp[i - 2])

    print('#{} {}'.format(t, dp[N]))