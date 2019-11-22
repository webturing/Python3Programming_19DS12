a = [1]*10
for i in range(2, 10):
    a[i] = a[i-1]*i
for i in range(2, 10):
    a[i] += a[i-1]
m = int(input().strip())
print(a[m])
