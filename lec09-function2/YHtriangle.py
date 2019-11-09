def factorial(n):  # n!
    s = 1
    for i in range(2, n + 1):  # [a,b+1) == [a,b]
        s *= i
    return s


def binormial(n, r):
    return int(factorial(n) / factorial(r) / factorial(n - r))


def triangle(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(binormial(i, j), end=" ")
        print("")


triangle(5)
