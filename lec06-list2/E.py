while True:
    a = [0] * int(input())
    a[-1] = 1
    for i in range(1, len(a)):
        a[-i - 1] = 2 * (a[-i] + 1)
    print(a[0])
