from collections import deque

N = int(input())

max_h = 0
lst = list()
for n in range(N):
    L, H = map(int, input().split())
    lst.append((L, H))

    if H > max_h:
        max_h = H

lst.sort()

queue = deque(lst)

area = 0
l_ptr = 0
l_h = 0
r_ptr = 1001
r_h = 0

while queue:
    pop_item = queue.popleft()
    if pop_item[1] == max_h:
        area += (pop_item[0] - l_ptr) * l_h
        l_ptr = pop_item[0]
        queue.appendleft(pop_item)
        break

    if pop_item[1] <= l_h:
        continue

    area += (pop_item[0] - l_ptr) * l_h
    l_ptr = pop_item[0]
    l_h = pop_item[1]

while queue:
    pop_item = queue.pop()
    if pop_item[1] == max_h:
        area += (r_ptr - pop_item[0]) * r_h
        r_ptr = pop_item[0]
        break

    if pop_item[1] <= r_h:
        continue

    area += (r_ptr - pop_item[0]) * r_h
    r_ptr = pop_item[0]
    r_h = pop_item[1]

area += (r_ptr - l_ptr + 1) * max_h

print(area)
