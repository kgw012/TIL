# swea 1213 'String'

def brute_force(word, string):

    cnt = 0
    for i in range(len(string) - len(word) + 1):
        flag = True
        for j in range(len(word)):
            if string[i + j] != word[j]:
                flag = False
                break
        if flag:
            cnt += 1

    return cnt


if __name__ == '__main__':
    T = 10

    for t in range(1, T+1):
        _ = int(input())
        word = input()
        string = input()

        result = brute_force(word, string)
        print('#{} {}'.format(t, result))