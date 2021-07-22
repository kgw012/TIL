# 1. 세로로 출력하기
# number = int(input())
# for num in range(1, number + 1):
#     print(num)

# 2. 거꾸로 세로로 출력하기
# number = int(input())
# for num in range(number, -1, -1):
#     print(num)

# 3. N줄 덧셈 (SWEA #2025)
number = int(input())
sum = 0
for num in range(1, number + 1):
    sum += num
    
print(sum)