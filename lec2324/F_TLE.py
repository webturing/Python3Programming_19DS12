def ok(x):
    s = str(x)
    t = s[::-1]
    return s == t


n = int(input())
for m in range(10 ** (n - 1), 10 ** n):
    if ok(m):
        print(m)
