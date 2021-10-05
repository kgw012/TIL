# 백준 15649 'N과 M(1)'

def dfs(N, M, nums, visits, cnt):
    if cnt >= M:
        print(*nums, sep=' ')
        return
    
    for num in range(1, N + 1):
        if visits[num]:
            continue

        nums[cnt] = num
        visits[num] = True
        dfs(N, M, nums, visits, cnt + 1)
        visits[num] = False


if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = [0 for _ in range(M)]
    visits = [False for _ in range(N + 1)]
    cnt = 0
    dfs(N, M, nums, visits, cnt)