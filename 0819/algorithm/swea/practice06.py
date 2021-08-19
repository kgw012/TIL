def func(num):
    if num == 1:
        return 1

    return num + func(num - 1)


if __name__ == '__main__':
    total = func(5)
    print(total)