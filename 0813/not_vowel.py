# swea 4406 '모음이 보이지 않는 사람'

T = int(input())

vowels = {'a', 'e', 'i', 'o', 'u'}

for t in range(1, T+1):
    word = input()
    result = ''

    for c in word:
        if c in vowels:
            continue
        result += c

    print('#{} {}'.format(t, result))