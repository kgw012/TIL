def is_same(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False

    return True


if __name__=='__main__':
    lst1 = [3, 2, 7, 5, 8, 9]
    lst2 = list(map(int, input().split()))

    ret = is_same(lst1, lst2)
    print(ret)

    ret2 = lst1 == lst2
    print(ret2)