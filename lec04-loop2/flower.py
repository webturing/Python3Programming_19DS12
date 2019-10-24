for n in range(100, 1000):
    c = n % 10
    b = (n // 10) % 10
    a = (n // 100)
    # print(a,b,c)
    m = a ** 3 + b ** 3 + c ** 3
    # print('m=',m)
    if m == n:
        print(m)
