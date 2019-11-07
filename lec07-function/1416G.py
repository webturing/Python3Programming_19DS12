def days(m):
    if m in [1, 3, 5, 7, 8, 10, 12]: return 31
    if m in [4, 6, 9, 11]: return 30
    return 28


def leap(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


y, m, d = 2000, 11, 7
for i in range(1, m): d += days(i)
if leap(y) and m > 2: d += 1
print(d)
