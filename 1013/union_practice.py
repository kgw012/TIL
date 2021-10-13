def Find(ch):
    if ch == parent[ch]:
        return ch

    ret = Find(parent[ch])
    # parent[ch] = ret
    return ret


def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:
        parent[pb] = pa

    return


if __name__ == '__main__':
    parent = dict()

    for ch in range(ord('A') , ord('Z') + 1):
        parent[chr(ch)] = chr(ch)


    parent['E'] = 'D'
    parent['D'] = 'C'
    parent['C'] = 'B'
    parent['B'] = 'A'

    print(Find('E')) # A출력
    print(Find('D')) # A출력
    print(Find('B')) # A출력
    print(Find('A')) # A출력