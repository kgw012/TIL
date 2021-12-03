import random
import string

f = open('eval_input.txt','w')
f.write('50\n')
string_pool = string.ascii_lowercase

test_case = [
    'kim',
    'ssafy',
    'apple',
    'banana',
    'card',
]

for t in range(45):
    if t < 5:
        N = 10
    elif t < 15:
        N = 100
    elif t < 25:
        N = 1000
    elif t < 35:
        N = 10000
    else:
        N = 100000

    result = ''

    for _ in range(N):
        result += random.choice(string_pool)

    test_case.append(result)

for i in range(50):
    f.write(f'{test_case[i]}'+'\n')

f.close()
