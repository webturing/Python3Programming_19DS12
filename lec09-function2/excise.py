def Length(n):
    if n<10:
        return 1
    else:
        return Length(n//10)+1

def Sum(n):
    if n<1:
        return n
    else:
        return Sum(n//10)+(n%10)


print(4==Length(1234))
print(10==Sum(1234))


