# swea 2005 '파스칼의 삼각형'

factorial = [1]
for i in range(1, 10):
    factorial.append(i * factorial[i - 1])

dp = []
for i in range(10):
    dp.append([])
    for j in range(i + 1):
        dp[i].append(factorial[i] // (factorial[j] * factorial[i - j]))

T = int(input())

for t in range(1, T+1):
    N = int(input())

    print('#{}'.format(t))
    for i in range(N):
        print(*dp[i], sep=' ')