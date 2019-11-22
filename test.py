def create2d(row, col):
    return [[0]*col for i in range(row)]


def disp2d(a):
    for r in a:
        for c in r:
            print(c, end=" ")
        print("")


def findmax(a):
    mr, mc = 0, 0
    for r in range(len(a)):
        for c in range(len(a[r])):
            if a[r][c] > a[mr][mc]:
                mr, mc = r, c
    return (mr, mc)


a = create2d(3, 4)
a[0] = list(map(int, input().strip().split()))
a[1] = list(map(int, input().strip().split()))
a[2] = list(map(int, input().strip().split()))
r, c = findmax(a)
print(a[r][c])
print(r)
print(c)
