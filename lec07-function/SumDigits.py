def Sum(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret


print(10 == Sum(1234))  # expectedValue==actualValue
print(6 == Sum(123))  # Unit Testing
print(1 == Sum(1))
print(3 == Sum(12))
