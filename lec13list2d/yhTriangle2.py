import math


def disp2d(a):
    for e in a:
        for t in e:
            print(t, end=" ")
        print("")


while True:
    n = int(input())
    if n == 0:
        break
    a = [[0]*n for i in range(n)]

    x, y = n-1, n//2
    a[x][y] = 1
    # disp2d(a)
    for i in range(2, n*n+1):
        nx, ny = (x+1) % n, (y+1) % n
        if a[nx][ny] != 0:
            nx, ny = (x-1+n) % n, y
        x, y = nx, ny
        a[x][y] = i
    disp2d(a)
    print("")
