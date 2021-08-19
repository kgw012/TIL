def func(s, cnt):
    if cnt == 3:
        print(s, end=' ')
        return

    for path in range(1, 4):
        func(s + str(path), cnt + 1)

    return


if __name__ == '__main__':
    func('', 0)