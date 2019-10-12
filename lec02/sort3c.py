a, b, c = map(int, input().strip().split())
x = min(a, b, c)
z = max(a, b, c)
y = a + b + c - x - z
print(x, y, z)
