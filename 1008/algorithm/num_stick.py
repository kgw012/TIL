# swea 2819 '격자판의 숫자 이어 붙이기'

def dfs(i, j, cnt, num):
    global num_set, MAP, di, dj
    if cnt >= 7:
        num_set.add(num)
        return
    
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if not 0<=ni<4 or not 0<=nj<4:
            continue
        
        dfs(ni, nj, cnt + 1, num + MAP[ni][nj])
    
    return


if __name__ == '__main__':
    T = int(input())

    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for t in range(1, T + 1):
        MAP = []
        for _ in range(4):
            MAP.append(input().split())
        
        num_set = set()

        for i in range(4):
            for j in range(4):
                dfs(i, j, 1, MAP[i][j])
            
        print(f'#{t} {len(num_set)}')
        