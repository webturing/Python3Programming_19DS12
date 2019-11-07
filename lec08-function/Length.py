def Length(n):
    ret = 0
    while n > 0:
        n //= 10
        ret += 1

    return ret


print(4 == Length(1234))  # expectedValue==actualValue
print(3 == Length(123))  # Unit Testing
print(1 == Length(1))
print(2 == Length(12))
