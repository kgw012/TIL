# swea 1961 '숫자 배열 회전'

T = int(input())

for t in range(1, T+1):
    N = int(input())
    MAP = []
    for _ in range(N):
        MAP.append(list(input().split()))
    
    result_list = [[] for _ in range(N)]

    result_idx = 0
    for j in range(N):
        result = ''
        for i in range(N-1, -1, -1):
            result += MAP[i][j]
        result_list[result_idx].append(result)
        result_idx += 1
    
    result_idx = 0
    for i in range(N-1, -1, -1):
        result = ''
        for j in range(N-1, -1, -1):
            result += MAP[i][j]
        result_list[result_idx].append(result)
        result_idx += 1
    
    result_idx = 0
    for j in range(N-1, -1, -1):
        result = ''
        for i in range(N):
            result += MAP[i][j]
        result_list[result_idx].append(result)
        result_idx += 1
    
    print('#{}'.format(t))

    for i in range(N):
        print(*result_list[i], sep=' ')