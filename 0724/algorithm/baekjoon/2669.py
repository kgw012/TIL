xy_map = [[False for x in range(101)] for y in range(101)]

area = 0
for cnt in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if xy_map[i][j]: continue
            
            area += 1
            xy_map[i][j] = True

print(area)