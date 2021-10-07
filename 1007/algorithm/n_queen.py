# swea 2806 'N-Queen'

def dfs(cnt):
    global N, visits1, visits2, visits3, answer

    if cnt >= N:
        answer += 1
        return
    
    i = cnt
    for j in range(N):
        if visits1[j]:
            continue

        if visits2[i + j]:
            continue

        if visits3[i - j + N - 1]:
            continue
        
        visits1[j] = True
        visits2[i + j] = True
        visits3[i - j + N - 1] = True

        dfs(cnt + 1)
        
        visits1[j] = False
        visits2[i + j] = False
        visits3[i - j + N - 1] = False

    return
    

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())

        visits1 = [False] * N
        visits2 = [False] * (2 * N - 1)
        visits3 = [False] * (2 * N - 1)

        answer = 0

        dfs(0)

        print(f'#{t} {answer}')