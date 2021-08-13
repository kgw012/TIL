# swea 10804 '문자열의 거울상'

T = int(input())

mirror = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}

for t in range(1, T+1):
    word = input()
    word = word[::-1]
    result = ''
    for c in word:
        result += mirror[c]

    print('#{} {}'.format(t, result))