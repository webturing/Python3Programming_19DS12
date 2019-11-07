a = [1] * 10
for i in range(2, len(a)):
    a[i] = a[i - 1] * i
for n in range(1, 10 ** 7):
    m = n
    s = 0  # s=1!+4!+5!
    while m > 0:
        d = m % 10
        s += a[d]  # d!
        m //= 10
    if s == n:
        print(n, end=" ")
