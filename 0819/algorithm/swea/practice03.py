def abc(level, s):
    if level == 2:
        print(s, end=' ')
        return
    abc(level + 1, s+'L')
    abc(level + 1, s+'M')
    abc(level + 1, s+'R')
    return


if __name__ == '__main__':
    abc(0, '')