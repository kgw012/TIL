# swea 12677 '토너먼트 카드 게임'(전용)

def rsp(lst, a, b):
    if lst[a] == 1:
        if lst[b] == 1:
            return a
        elif lst[b] == 2:
            return b
        else:
            return a
    elif lst[a] == 2:
        if lst[b] == 1:
            return a
        elif lst[b] == 2:
            return a
        else:
            return b
    else:
        if lst[b] == 1:
            return b
        elif lst[b] == 2:
            return a
        else:
            return a


def dfs(lst, st, fn):
    if fn == st:
        return st

    if fn - st == 1:
        winner = rsp(lst, st, fn)
        return winner

    md = (st + fn) // 2
    winner1 = dfs(lst, st, md)
    winner2 = dfs(lst, md + 1, fn)

    return rsp(lst, winner1, winner2)


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T+1):
        N = int(input())
        lst = [0]
        lst.extend(list(map(int, input().split())))

        winner = dfs(lst, 1, N)

        print('#{} {}'.format(t, winner))

