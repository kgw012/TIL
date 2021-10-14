# swea 13159 '그룹 나누기'

def find(n):
    global p_list
    if p_list[n] == n:
        return n
    
    ret = find(p_list[n])
    p_list[n] = ret

    return ret


def union(n1, n2):
    global p_list
    p1 = find(n1)
    p2 = find(n2)

    if p1 == p2:
        return
    
    p_list[p1] = p2
    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N, M = map(int, input().split())
        union_list = list(map(int, input().split()))

        p_list = [i for i in range(N + 1)]

        for i in range(M):
            n1, n2 = union_list[2 * i], union_list[2 * i + 1]
            union(n1, n2)
        
        answer = 0
        for i in range(1, N + 1):
            if i == p_list[i]:
                answer += 1
        
        print(f'#{t} {answer}')

