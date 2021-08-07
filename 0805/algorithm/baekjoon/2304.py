n = int(input())

buildings = []
for i in range(n):
    buildings.append(list(map(int, input().split())))

buildings.sort()

max_height = max(buildings[i][1] for i in range(n))

i = 0
total = 0
save_idx = 0
save_height = 0

while True:
    idx = buildings[i][0]
    height = buildings[i][1]

    if buildings[i][1] == max_height:
        total += (save_height * (idx - save_idx))
        save_idx = idx
        break


    if height > save_height:
        total += (save_height * (idx - save_idx))
        save_idx = idx
        save_height = height
    
    i += 1

j = n - 1
save_idx2 = n - 1
save_height = 0

while True:
    idx = buildings[j][0]
    height = buildings[j][1]

    if buildings[j][1] == max_height:
        total += (save_height * (save_idx2 - idx))
        save_idx2 = idx
        break


    if height > save_height:
        total += (save_height * (save_idx2 - idx))
        save_idx2 = idx
        save_height = height
    
    j -= 1

total += max_height * (save_idx2 - save_idx + 1)
print(total)