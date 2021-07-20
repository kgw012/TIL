# 1. Mutable & Immutable
mutable = ['List', 'Set', 'Dictionary']
immutable = ['String', 'Tuple', 'Range']


# 2. 홀수만 담기
my_list = list(map(int, range(1, 51)[0:50:2]))
print(my_list)


# 3. Dictionary 만들기
class_dic = {
    '김길웅' : 29
}


# 4. 반복문으로 네모 출력
n = 5
m = 9

stars = ''
for i in range(m):
    for j in range(n):
        stars += '*'
    stars += '\n'

print(stars)


# 5. 조건 표현식
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')


# 6. 평균 구하기
scores = [80, 89, 99, 83]
print(sum(scores) / len(scores))