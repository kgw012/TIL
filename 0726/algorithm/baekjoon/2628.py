x, y = map(int, input().split())
n = int(input())

x_list = [0, x]
y_list = [0, y]

for i in range(n):
    direction, idx = map(int, input().split())

    if direction:
        x_list.append(idx)
    else:
        y_list.append(idx)

x_list.sort()
y_list.sort()

x_max = 0
for i in range(1, len(x_list)):
    x_len = x_list[i] - x_list[i - 1]
    
    if x_len > x_max:
        x_max = x_len

y_max = 0
for j in range(1, len(y_list)):
    y_len = y_list[j] - y_list[j - 1]

    if y_len > y_max:
        y_max = y_len

print(x_max * y_max)