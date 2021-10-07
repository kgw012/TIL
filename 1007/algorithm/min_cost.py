# swea 13119 '최소 생산 비용'

def dfs(cnt, total):
    global N, M, visits, answer

    if total >= answer:
        return

    if cnt >= N:
        if total < answer:
            answer = total
        return
    
    for i in range(N):
        if visits[i]:
            continue

        visits[i] = True
        dfs(cnt + 1, total + MAP[cnt][i])
        visits[i] = False
    
    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        MAP = []
        for _ in range(N):
            MAP.append(list(map(int, input().split())))
        
        visits = [False] * N
        answer = 21e8

        dfs(0, 0)

        print(f'#{t} {answer}')
