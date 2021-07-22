# 1. Built-in 함수

abs(-3)
print('built-in 함수')
range(1)
int('3')
min(3, 5)


# 2. 정중앙 문자

def get_middle_char(s):
    if len(s) == 0:
        return ''
    if len(s) % 2 == 0:
        return s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
    return s[len(s) // 2]

print(get_middle_char('asdfg'))
print(get_middle_char('coding'))


# 3. 위치 인자와 키워드 인자

def asdf(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

# (1)
asdf('허준')

# (2)
asdf(location='대전', name='철수')

# (3)
asdf('영희', location='광주')

# (4)
# asdf(name='길동', '구미')


# 4. 나의 반환값은

def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
print(result)


# 5. 가변 인자 리스트

def my_avg(*args):
    total = 0
    for arg in args:
        total += arg
    
    avg = total / len(args)
    return avg

print(my_avg(77, 83, 95, 80, 70))