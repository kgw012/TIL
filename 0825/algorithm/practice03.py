from collections import deque

queue = deque()
queue.append(3)
queue.append(2)
queue.append(1)
queue.append(5)
queue.append(7)

ret = queue[0]
ret = queue.popleft()

while queue:
    ret = queue.popleft()
    print(ret, end=' ')