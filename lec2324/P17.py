for n in range(1, 1000000000):
    if n % 10 != 6: continue
    # n=123456
    # m=612345
    x = n // 10
    m = int('6' + str(x))
    if m == 4 * n:
        print(n, m)
        break
