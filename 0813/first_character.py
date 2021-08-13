# swea 12579 '앞글자 따기' (전용)

T = int(input())

offset = ord('a') - ord('A')

for t in range(1, T+1):
    N = int(input())

    word_list = input().split()
    result = ''

    for word in word_list:
        c = word[0]
        C = chr(ord(c) - offset)
        result += C

    print('#{} {}'.format(t, result))