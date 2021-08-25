T = int(input())

for t in range(1, T+1):
    X, Y = map(int, input().split())
    h = (X + Y - (X**2 + Y**2 - X * Y)**0.5) / 6
    a = X - 2*h
    b = Y - 2*h
    area = a*b*h
    print('#{} {:.6f}'.format(t, area))