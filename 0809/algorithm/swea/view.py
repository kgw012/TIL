def check(buildings, idx):
    l = idx - 2 if idx >= 2 else 0
    r = idx + 3

    sides = buildings[l : idx] + buildings[idx + 1 : r]
    side_max = max(sides)

    height = buildings[idx]

    if height - side_max > 0:
        return height - side_max
    else:
        return 0

T = 10
for t in range(1, T + 1):
    n = int(input().strip())
    buildings = list(map(int, input().split()))

    total = 0
    for idx in range(n):
        total += check(buildings, idx)

    print(f'#{t} {total}')

