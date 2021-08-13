def is_exist(lst, target):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == target:
                return True

    return False


if __name__=='__main__':
    MAP = [
        [3, 2, 7, 9], [5, 1, 2, 5], [1, 2, 3, 4]
    ]

    ret = is_exist(MAP, 1)
    print(ret)