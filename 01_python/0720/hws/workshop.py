# 1. 간단한 N의 약수(SWEA #1933)
n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')


# 2. 중간값 찾기(SWEA #2063 변형)
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

# 1) sort이용
numbers.sort()

num_len = len(numbers)
median = 0
if num_len % 2:
    median = numbers[num_len // 2]
else:
    m1 = numbers[num_len // 2 - 1]
    m2 = numbers[num_len // 2]
    median = (m1 + m2) / 2
print(median)

# 2) 2중 for문 이용(numbers의 길이가 홀수라고 가정)
num_len = len(numbers)

median = 0
min_abs = 100000
min_abs_num = 0
for number in numbers:
    count1 = 0
    count2 = 0
    for number2 in numbers:
        if number < number2:
            count1 += 1
        elif number > number2:
            count2 += 1
    if count1 == count2:
        median = number
        break
    
    # 중간값과 같은 숫자가 여러개 있는 경우를 위해,,
    cnt_abs = abs(count1 - count2)
    if min_abs > cnt_abs:
        min_abs = cnt_abs
        min_abs_num = number

# 중간값과 같은 숫자가 여러개 있는 경우
else:
    median = min_abs_num
    
print(median)


# 3. 계단 만들기
number = int(input())
for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()