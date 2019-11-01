a, b = map(int, input().strip().split())
if a < 100: a = 100
if b > 999: b = 999
for n in range(a, b + 1):
    x, y, z = n // 100, n % 100 // 10, n % 10
    if x ** 3 + y ** 3 + z ** 3 == n:
        print(n)
