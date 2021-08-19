def func(lev):
    global a
    if lev == 3:
        print(a, end=' ')
        a += 1
        return
    func(lev + 1)
    func(lev + 1)
    return


if __name__ == '__main__':
    a = 1
    func(0)