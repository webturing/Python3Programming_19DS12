input()
a = list(map(int, input().strip().split()))
a.sort()
for i in range(len(a)):
    if a[i] != 0:
        a[0], a[i] = a[i], a[0]
        break
for e in a:
    print(e, end="")
