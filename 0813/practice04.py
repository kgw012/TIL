def count_pattern(lst, pattern):
    cnt = 0

    for i in range(len(lst) - len(pattern) + 1):
        flag = True
        for j in range(len(pattern)):
            if lst[i + j] != pattern[j]:
                flag = False
                break
        if flag:
            cnt += 1

    return cnt


if __name__ == '__main__':
    lst = [7, 1, 2, 5, 3, 2, 7, 9, 1, 2, 5]
    pattern = [1, 2, 5]

    cnt = count_pattern(lst, pattern)

    print(cnt)
