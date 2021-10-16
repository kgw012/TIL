from collections import deque

def drop(MAP, m):
    i = 0
    m1, m2 = m[0] - 1, m[1]
    while i < 6:
        if MAP[i][m1]:
            MAP[i - 1][m1] = m2
            return (i - 1, m1)
        i += 1
    
    MAP[5][m1] = m2
    return (5, m1)


def gravity(MAP):
    for j in range(6):
        stk = []
        for i in range(6):
            if MAP[i][j]:
                stk.append(MAP[i][j])
        
        i = 5
        while stk:
            MAP[i][j] = stk.pop()
            i -= 1
    
    return


def check(MAP, color, i, j):
    global di, dj

    visits = [[False] * 6 for _ in range(6)]
    visits[i][j] = True
    
    que = deque()
    que.append((i, j))
    pop_list = []
    while que:
        i, j = que.popleft()
        pop_list.append((i, j))
        for d in range(4):
            ni = i + di[d]
            nj = j = dj[d]
            if not 0<=ni<6 or not 0<=nj<6:
                continue

            if visits[ni][nj]:
                continue

            if MAP[ni][nj] == color:
                que.append((ni, nj))
                pop_list.append((ni, nj))
                visits[ni][nj] = True
    
    if len(pop_list) >= 3:
        for i, j in pop_list:
            print((i, j))
            MAP[i][j] = 0
    
    return


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def solution(macaron):
    MAP = [[0] * 6 for _ in range(6)]

    for m in macaron:
        i, j = drop(MAP, m)
        check(MAP, m[1], i, j)
        gravity(MAP)
        print(MAP)

    answer = []
    for i in range(6):
        s = ''
        for j in range(6):
            s += str(MAP[i][j])
        
        answer.append(s)
    return answer


if __name__ == '__main__':
    macaron = [[1, 1], [1, 1], [1, 1]]
    solution(macaron)