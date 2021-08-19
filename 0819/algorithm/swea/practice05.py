def get_dice(cnt, s):
    global n

    if cnt == n:
        print(s)
        return

    for num in range(1, 6+1):
        get_dice(cnt + 1, s + str(num))

    return


if __name__ == '__main__':
    n = int(input())
    get_dice(0, '')