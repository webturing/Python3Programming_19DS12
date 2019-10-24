n = int(input().strip())
h = 100
s = 0

s += h
for i in range(1,n):
    h /= 2
    s += h * 2

print(s)
