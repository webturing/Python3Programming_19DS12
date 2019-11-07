a = [1] * 20
for i in range(2, 20):
    a[i] = a[i - 1] + a[i - 2]
for i in a:
    print(i)
