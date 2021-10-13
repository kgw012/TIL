# 백준 1717 '집합의 표현'
# https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(10**6)

def find(num):
    global p_list
    if num == p_list[num]:
        return num
    
    ret = find(p_list[num])
    p_list[num] = ret
    return ret


def union(num1, num2):
    global p_list
    p1 = find(num1)
    p2 = find(num2)

    if p1 == p2:
        return
    else:
        p_list[p1] = p2
    
    return


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    p_list = [i for i in range(n + 1)]

    for _ in range(m):
        cmd, num1, num2 = map(int, sys.stdin.readline().split())

        if cmd == 0:
            union(num1, num2)
        else:
            if find(num1) == find(num2):
                print('YES')
            else:
                print('NO')
