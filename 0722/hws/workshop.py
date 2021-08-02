# 1. 숫자의 의미

def get_secret_word(chars):
    result = ''
    for char in chars:
        result += chr(char)

    return result

print(get_secret_word([80, 81, 82, 83, 84]))


# 2. 내 이름은 몇일까?
def get_secret_number(name):
    result = 0
    for char in name:
        result += ord(char)

    return result

print(get_secret_number('tom'))


# 3. 강한 이름
def get_strong_word(str1, str2):
    num1 = get_secret_number(str1)
    num2 = get_secret_number(str2)
    if num1 > num2:
        return str1
    else:
        return str2

print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))