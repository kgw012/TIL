# swea 1251 '하나로'

import heapq

def find(node):
    global p_list
    if p_list[node] == node:
        return node
    
    ret = find(p_list[node])
    p_list[node] = ret
    return ret


def union(n1, n2):
    global p_list
    p1 = find(n1)
    p2 = find(n2)
    
    if p1 != p2:
        p_list[p1] = p2
    return


def calc_e(p1, p2):
    global E
    x1, y1 = p1
    x2, y2 = p2

    L2 = (x1 - x2)**2 + (y1 - y2)**2
    return E * L2
    

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        x_list = list(map(int, input().split()))
        y_list = list(map(int, input().split()))
        xy_list = list(zip(x_list, y_list))
        E = float(input())
        p_list = [i for i in range(N)]

        e_list = []
        for i in range(N):
            p1 = xy_list[i]
            for j in range(i + 1, N):
                p2 = xy_list[j]
                e = calc_e(p1, p2)
                e_list.append((e, i, j))

        e_list.sort()

        answer = 0
        for e, i, j in e_list:
            if find(i) == find(j):
                continue

            union(i, j)
            answer += e
        
        print(f'#{t} {round(answer)}')
