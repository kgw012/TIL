# 1. Python 예약어
import keyword
print(keyword.kwlist)

# 2. 실수 비교
num1 = 0.1 * 3
num2 = 0.3
import math
print(math.isclose(num1, num2))

# 3. 이스케이프 시퀀스
newLine = '\n'
tab = '\t'
backSlash = '\\'

# 4. String Interpolation
name = '철수'
print(f'안녕 {name}야!')

# 5. 형 변환
# (1) str(1) 
# (2) int('30') 
# (3) int(5) 
# (4) bool('50') 
# (5) int('3.5')

# 6. 네모 출력
n = 5
m = 9

star = ('*' * n + '\n') * m
print(star)

# 7. 이스케이프 시퀀스 응용
print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다.\'cd를 써서 git bash로 들어가 봐야지.\'')

# 8. 근의 공식
a = 1
b = 2
c = 2

d = (b**2 - 4 * a * c)**0.5

x = x1, x2 = (b * -1 - d) / (2 * a), (b * -1 + d) / (2 * a)
print(x)