def is_prime(n):
    if n < 2: return False  # patch
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(True == is_prime(13))
print(False == is_prime(25))
print(False == is_prime(9))
print(True == is_prime(2))
print(False == is_prime(1))

for n in range(1, 100):
    if is_prime(n):
        print(n, end=' ')
