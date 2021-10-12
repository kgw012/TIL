# swea 2105 '디저트 카페'

def dfs(desert_set: set, i, j, st_i, st_j, d, cnt):
    global MAP, N, di, dj, answer

    if d == 4:
        if cnt > answer:
            answer = cnt
        return
    
    l = 1
    rm_lst = []
    while True:
        ni = i + l * di[d]
        nj = j + l * dj[d]

        if not 0<=ni<N or not 0<=nj<N:
            break
        
        if d == 3:
            if st_i != ni or st_j != nj:
                if MAP[ni][nj] in desert_set:
                    break
                desert_set.add(MAP[ni][nj])
                rm_lst.append(MAP[ni][nj])
                l += 1
                continue
            else:
                dfs(desert_set, ni, nj, st_i, st_j, d + 1, cnt + l)
                break

        if MAP[ni][nj] in desert_set:
            break

        desert_set.add(MAP[ni][nj])
        rm_lst.append(MAP[ni][nj])


        dfs(desert_set, ni, nj, st_i, st_j, d + 1, cnt + l)
        l += 1
    
    for rm in rm_lst:
        desert_set.remove(rm)
    
    return
    
                    

if __name__ == '__main__':
    T = int(input())

    di = [1, 1, -1, -1]
    dj = [-1, 1, 1, -1]

    for t in range(1, T + 1):
        N = int(input())
        MAP = []
        for _ in range(N):
            MAP.append(list(map(int, input().split())))

        answer = -1
        
        for i in range(N - 2):
            for j in range(1, N - 1):
                desert_set = set()
                desert_set.add(MAP[i][j])
                dfs(desert_set, i, j, i, j, 0, 0)
        
        print(f'#{t} {answer}')
