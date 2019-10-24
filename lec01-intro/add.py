while True:
    x = int(input())
    cnt = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        cnt = cnt + 1
    print(cnt)
