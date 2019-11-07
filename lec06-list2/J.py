import math

n = int(input())
a = list(range(n + 1))
a.remove(0)
a.remove(1)
for i in range(2, int(math.sqrt(n)) + 1):
    if i not in a:
        continue
    for j in range(i * i, n + 1, i):
        if j in a:
            a.remove(j)

for i in a:
    print(i)
