n, s, h = int(input()), 0, 100
s -= h
for i in range(n):
    s += 2 * h
    h /= 2
print('%.4f' % s)
