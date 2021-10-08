# swea 1486 '장훈이의 높은 선반'

def dfs(cnt, total):
    global N, B, lst, answer
    if answer == 0:
        return

    if total >= B:
        h = total - B
        if h < answer:
            answer = h
        return

    if cnt >= N:
        return
    
    dfs(cnt + 1, total + lst[cnt])
    dfs(cnt + 1, total)

    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, B = map(int, input().split())
        lst = list(map(int, input().split()))

        lst.sort(reverse=True)
        answer = 21e8

        dfs(0, 0)

        print(f'#{t} {answer}')
