queue = [3,7,2,1,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
front = 0
rear = len(queue)

while front != rear:
    print(queue[front], end=' ')
    front += 1

print()
print(front)
