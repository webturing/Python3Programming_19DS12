while True:
    a, b = map(int, input().strip().split())
    print('%.5f' % sum(1 / i ** 2 for i in range(a, b + 1)))
