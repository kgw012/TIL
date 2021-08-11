def my_abs(num):
    if num < 0:
        return -num
    return num

if __name__=='__main__':
    T = 10
    for t in range(1, T+1):
        n = int(input())
        lst = []
        for i in range(n):
            lst.append(list(map(int, input().split())))

        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        total = 0
        for i in range(n):
            for j in range(n):
                num = lst[i][j]
                for d in range(4):
                    test_i = i + di[d]
                    test_j = j + dj[d]
                    if 0 <= test_i < n and 0 <= test_j < n:
                        total += my_abs(num - lst[test_i][test_j])

        print('#{} {}'.format(t, total))