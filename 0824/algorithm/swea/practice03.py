def dfs(lst, visits, cnt):
    if len(lst) == cnt:
        for i in range(len(lst)):
            if visits[i]:
                print(lst[i], end=' ')
        print()
        return

    visits[cnt] = True
    dfs(lst, visits, cnt + 1)
    visits[cnt] = False
    dfs(lst, visits, cnt + 1)


if __name__ == '__main__':
    lst = ['A', 'B', 'C', 'D']
    visits = [True for _ in range(4)]
    dfs(lst, visits, 0)
