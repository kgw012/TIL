# swea 5356 '의석이의 세로로 말해요'

T = int(input())

for t in range(1, T+1):
    my_dict = {}
    for i in range(15):
        my_dict[i] = ''
    
    for _ in range(5):
        string = input()
        
        for i, c in enumerate(string):
            my_dict[i] += c
    
    print('#{}'.format(t), end=' ')
    for i in range(15):
        if len(my_dict[i]):
            print(my_dict[i], end='')
        else:
            break
    print()