PI = 3.1415926


def area(r):
    s = PI * r * r
    return s


def perimter(r):
    return 2 * PI * r


def f(x):  # f(x)=x^2
    return x * x


r = 10
print("Area=", area(r))
print("Perimeter=", perimter(r))
