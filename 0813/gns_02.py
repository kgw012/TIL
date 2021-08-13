# swea 1221 'GNS'

word_to_num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
                'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

num_to_word = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR',
                5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

T = int(input())

for t in range(1, T+1):
    N = input().split()[1]
    cnt_list = [0 for _ in range(10)]
    for word in input().split():
        cnt_list[word_to_num[word]] += 1

    print('#{}'.format(t))
    for num in range(10):
        print((num_to_word[num] + ' ') * cnt_list[num], end='')
    print()