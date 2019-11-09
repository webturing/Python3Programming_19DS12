def binormial(n, r):
    if n == r or r == 0:
        return 1
    else:
        return binormial(n - 1, r - 1) + binormial(n - 1, r)


def triangle(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(binormial(i, j), end=" ")
        print("")


triangle(5)
