def factorial(n):
    if n <= 1:
        return 1  # termination
    else:
        return n * factorial(n - 1)


print(120 == factorial(5))
print(2 == factorial(2))
print(1 == factorial(1))
print(1 == factorial(0))
