# 1. 무엇이 중복일까

def duplicated_letters(text):
    # result = []
    # for i in text:
    #     if i in result:
    #         continue
        
    #     if text.count(i) > 1:
    #         result.append(i)
    
    # return result

    result = set()
    for char in text:
        if text.count(char) > 1:
            result.add(char)
    
    return list(result)

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))


# 2. 소대소대
def low_and_up(text):
    result = ''

    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i].lower()
        else:
            result += text[i].upper()
    
    return result

print(low_and_up('apple'))
print(low_and_up('banana'))


# 3. 숫자의 의미
def lonely(my_list):
    if len(my_list) == 0:
        return []
    
    result = [my_list[0]]
    save_num = my_list[0]
    
    for i in range(1, len(my_list)):
        if save_num == my_list[i]:
            continue
        result.append(my_list[i])
        save_num = my_list[i]

    return result

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))