# swea 1865 '동철이의 일 분배'

def dfs(cnt, success_percent):
    global N, MAP, visits, answer
    if success_percent <= answer:
        return
        
    if cnt >= N:
        if success_percent > answer:
            answer = success_percent
        return
    
    i = cnt
    for j in range(N):
        if visits[j]:
            continue
        
        visits[j] = True
        dfs(cnt + 1, success_percent * (MAP[i][j] / 100))
        visits[j] = False
    
    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        MAP = []
        for _ in range(N):
            MAP.append(list(map(int, input().split())))
        
        visits = [False] * N
        answer = 0

        dfs(0, float(100))

        print('#{} {:.6f}'.format(t, round(answer, 6)))
