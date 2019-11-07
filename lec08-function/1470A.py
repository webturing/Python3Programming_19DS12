n = int(input().strip())
while n != 1:
    if n % 2 == 0:
        print("%d/2=%d" % (n, int(n / 2)))
        n = int(n / 2)
    else:
        print("%d*3+1=%d" % (n, 3 * n + 1))
        n = 3 * n + 1
