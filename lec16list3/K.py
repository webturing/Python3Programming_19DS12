def disp2d(a):
    for row in a:
        for col in row:
            print(col, end=" ")
        print("")
    print("------------")


n = 3
a = [[0]*n for i in range(n)]
disp2d(a)
x, y = n-1, n//2
a[x][y] = 1
disp2d(a)
for i in range(2, n*n+1):
    nx = (x+1) % n
    ny = (y+1) % n
    if a[nx][ny] == 0:
        a[nx][ny] = i
        # disp2d(a)
        x, y = nx, ny
    else:
        nx = (x-1+n) % n
        ny = y
        a[nx][ny] = i
        # disp2d(a)
        x, y = nx, ny
disp2d(a)
