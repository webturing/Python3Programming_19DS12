def Add(a, b):
    return a + b


Mul = lambda a, b: a - b


def foo(a, b):
    return a + b, a * b


Add_Mul = lambda a, b: (a + b, a * b)

print(Add(3, 4))  # 7
print(Mul(3, 4))  # -1

# x, y = foo(3, 4)
x, y = Add_Mul(3, 4)
print(x, y)

a = 3
b = 4
a, b = b, a
print(a, b)

print((lambda a_, b_: (a_ + b_, (lambda a__,b__:a__*b__)(a,b)))(3, 4)) #unamed
print((lambda _1,_2:_1+_2))
