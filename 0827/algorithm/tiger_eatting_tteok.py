# 정올 1997 '떡 먹는 호랑이'

D, K = map(int, input().split())

dp = [0, 0, 1]

for i in range(3, D + 1):
    dp.append(dp[i - 1] + dp[i - 2])

a = 1
while True:
    if (K - dp[D - 1] * a) % dp[D] == 0:
        b = (K - dp[D - 1] * a) // dp[D]
        break
    a += 1

print(a)
print(b)
