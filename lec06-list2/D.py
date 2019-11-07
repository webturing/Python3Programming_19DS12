m, s = int(input()), 1
for i in range(2, m + 1):
    s -= 1 / i ** 2
print('%f' % s)
