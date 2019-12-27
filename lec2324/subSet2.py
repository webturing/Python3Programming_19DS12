for n in range(0, 32):
    a = n // 16
    b = n % 16 // 8
    c = n % 8 // 4
    d = n % 4 // 2
    e = n % 2
    print(a, b, c, d, e)
