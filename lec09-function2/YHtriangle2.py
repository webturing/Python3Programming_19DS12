def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def binormial(n, r):
    return int(factorial(n) / factorial(r) / factorial(n - r))


def triangle(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(binormial(i, j), end=" ")
        print("")


triangle(5)
