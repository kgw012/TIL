def selection_sort(arr, st):
    if st >= len(arr):
        return

    min_num = 100
    min_idx = -1
    for i in range(st, len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
            min_idx = i
    
    arr[st], arr[min_idx] = arr[min_idx], arr[st]

    selection_sort(arr, st + 1)


if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    st = 0
    selection_sort(arr, st)

    print(arr)