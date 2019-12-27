def prime(n):
    return n in [2, 3, 5, 7, 11, 13, 17]


for n in range(100, 999 + 1):
    a, b, c = n // 100, n % 100 // 10, n % 10
    if a == b: continue
    if b == c: continue
    if c == a: continue
    if b <= a + c: continue
    if prime(a + b): continue
    print(n)
