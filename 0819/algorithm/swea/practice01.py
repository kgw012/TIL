def abc(lst, idx):
    if idx == len(lst) - 1:
        print(lst[idx])
        return

    print(lst[idx])
    abc(lst, idx + 1)
    print(lst[idx])


if __name__ == '__main__':
    lst = [3, 5, 7, 9, 10, 6]
    abc(lst, 0)