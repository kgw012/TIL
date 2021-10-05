# 백준 1182 '부분수열의 합'
# https://www.acmicpc.net/problem/1182

if __name__ == '__main__':
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0

    for i in range(1, 1<<N):
        sum_subset = 0
        for j in range(N):
            if i & (1<<j):
                sum_subset += arr[j]
        
        if sum_subset == S:
            answer += 1
    print(answer)
