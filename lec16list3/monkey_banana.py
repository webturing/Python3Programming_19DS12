n = 12
k = 3
a = list(range(1, n+1))

b = [a[s:s+k] for s in range(0, n, k)]

print(b)
