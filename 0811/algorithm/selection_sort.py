def selection_sort(lst):
    n = len(lst)

    for i in range(n-1):
        for j in range(i+1, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


if __name__=='__main__':
    lst = [3, 2, 9, 5, 8, 6, 1]

    selection_sort(lst)
    print(lst)