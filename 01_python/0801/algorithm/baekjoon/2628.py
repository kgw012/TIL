width, height = map(int, input().split())

cuts = [[0], [0]]
n = int(input())
for i in range(n):
    cut_direction, idx = map(int, input().split())
    cuts[cut_direction].append(idx)

cuts[0].append(height)
cuts[1].append(width)

cuts[0].sort()
cuts[1].sort()

max_height = 0
max_width = 0
for idx in range(1, len(cuts[0])):
    h = cuts[0][idx] - cuts[0][idx - 1]
    if max_height < h:
        max_height = h

for idx in range(1, len(cuts[1])):
    w = cuts[1][idx] - cuts[1][idx - 1]
    if max_width < w:
        max_width = w

print(max_height * max_width)