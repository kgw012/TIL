# 1. 모음은 몇 개나 있을까?

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']

    count = 0
    for vowel in vowels:
        count += string.count(vowel)

    return count

print(count_vowels('apple'))
print(count_vowels('banana'))


# 2. 문자열 조작

# (1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.
# (2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를
#       기준으로 나누어 list로 반환한다. 특정 문자를 지정하지 않으면
#       공백을 기준으로 나눈다.
# (3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로
#       바꿔서 반환한다.
# (4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를
#       찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다

# 정답 : 4번
# 특정 문자를 지정하지 않으면 공백을 제거한다.


# 3. 정사각형만 만들기
def only_square_area(list1, list2):
    area_list = []

    for width in list1:
        for height in list2:
            if width == height:
                area = width * height
                area_list.append(area)
    
    return area_list

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))