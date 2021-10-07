def merge_sort(st, fn):
    if fn - st < 2:
        return
    
    md = (st + fn) // 2

    merge_sort(st, md)
    merge_sort(md, fn)

    global arr, tmp_arr, answer2

    if arr[md - 1] > arr[fn - 1]:
        answer2 += 1

    tmp_idx = st
    l = st
    r = md

    while l < md and r < fn:
        if arr[l] < arr[r]:
            tmp_arr[tmp_idx] = arr[l]
            tmp_idx += 1
            l += 1
            continue
        else:
            tmp_arr[tmp_idx] = arr[r]
            tmp_idx += 1
            r += 1
    
    while l < md:
        tmp_arr[tmp_idx] = arr[l]
        tmp_idx += 1
        l += 1
    
    while r < fn:
        tmp_arr[tmp_idx] = arr[r]
        tmp_idx += 1
        r += 1
    
    for i in range(st, fn):
        arr[i] = tmp_arr[i]

    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        tmp_arr = [0] * N

        answer1 = 0
        answer2 = 0

        merge_sort(0, N)

        answer1 = arr[N // 2]

        print(f'#{t} {answer1} {answer2}')
