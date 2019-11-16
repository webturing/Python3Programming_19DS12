def foo(x):
    return x*x

a=list(range(10))
print(a)
b=[foo(x) for x in a]
print(b)
c=list(map(foo,a))
print(c)
