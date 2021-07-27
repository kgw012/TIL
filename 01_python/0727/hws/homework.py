# 1. Built-in 함수와 메서드

temp_list = [5, 4, 3, 2, 1]
print('sort() 반환 : ', temp_list.sort())
print('temp_list : ', temp_list)

temp_list = [5, 4, 3, 2, 1]
print('sorted() 반환 : ', sorted(temp_list))
print('temp_list : ', temp_list)

# 2. .extend()와 .append()
my_list = ['my_list']
my_list.extend(['extend로 추가'])
my_list.append(['append로 추가'])
print(my_list)


# 3. 복사가 잘 된 건가?
a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(a)
print(b)