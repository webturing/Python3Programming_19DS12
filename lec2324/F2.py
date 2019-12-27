n = int(input())
if n % 2 == 0:
    w = n // 2
    for m in range(10 ** (w - 1), 10 ** w):
        s = str(m)
        print(s + s[::-1])
else:
    w = n // 2 + 1
    for m in range(10 ** (w - 1), 10 ** w):
        s = str(m)
        print(s + s[:-1][::-1])
