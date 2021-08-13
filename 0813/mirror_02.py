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

    result = ''
    for i in range(len(word) - 1, -1, -1):
        result += mirror[word[i]]

    print('#{} {}'.format(t, result))