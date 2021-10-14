# swea 13162 '최소 신장 트리'

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
        V, E = map(int, input().split())
        e_list = []
        p_list = [i for i in range(V + 1)]
        for _ in range(E):
            n1, n2, w = map(int, input().split())
            e_list.append((w, n1, n2))
        
        e_list.sort()

        answer = 0
        for w, n1, n2 in e_list:
            if find(n1) == find(n2):
                continue
            answer += w
            union(n1, n2)
        
        print(f'#{t} {answer}')
