def quick_sort(arr, st, fn):
    if fn - st < 2:
        return

    pivot = st
    l = st + 1
    r = fn - 1

    while True:
        while l <= r and arr[l] <= arr[pivot]:
            l += 1
        while l <= r and arr[r] > arr[pivot]:
            r -= 1

        if l > r:
            break

        arr[l], arr[r] = arr[r], arr[l]

    arr[pivot], arr[r] = arr[r], arr[pivot]

    quick_sort(arr, st, r)
    quick_sort(arr, r + 1, fn)

    return


if __name__ == '__main__':
    T = int(input())

    for t in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))

        quick_sort(arr, 0, N)

        answer = arr[N // 2]

        print(f'#{t} {answer}')
        