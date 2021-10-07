# swea 12166 'NUMBER OF INVERSION'

def merge_sort(st, fn):
    if fn - st < 2:
        return
    
    md = (st + fn) // 2
    merge_sort(st, md)
    merge_sort(md, fn)

    l = st
    r = md

    global lst, tmp_lst, answer
    tmp_idx = st
    while l < md and r < fn:
        if lst[l] > lst[r]:
            tmp_lst[tmp_idx] = lst[r]
            tmp_idx += 1
            r += 1
            answer += (md - l)
        else:
            tmp_lst[tmp_idx] = lst[l]
            tmp_idx += 1
            l += 1
    
    while l < md:
        tmp_lst[tmp_idx] = lst[l]
        tmp_idx += 1
        l += 1
    
    while r < fn:
        tmp_lst[tmp_idx] = lst[r]
        tmp_idx += 1
        r += 1
    
    for i in range(st, fn):
        lst[i] = tmp_lst[i]
    
    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        lst = list(map(int, input().split()))

        tmp_lst = [0] * N
        answer = 0
        merge_sort(0, N)

        print(f'#{t} {answer}')
