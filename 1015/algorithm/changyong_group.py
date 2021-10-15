# swea 7465 '창용 마을 무리의 개수'

def find(n):
    global p_list
    if p_list[n] == n:
        return n
    
    ret = find(p_list[n])
    p_list[n] = ret
    return ret


def union(n1, n2):
    global p_list
    p1, p2 = find(n1), find(n2)

    if p1 != p2:
        p_list[p1] = p2
    return
    

if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, M = map(int, input().split())
        p_list = [i for i in range(N)]

        for _ in range(M):
            n1, n2 = map(int, input().split())
            union(n1 - 1, n2 - 1)
        
        answer = 0
        for i in range(N):
            if find(i) == i:
                answer += 1
        
        print(f'#{t} {answer}')
