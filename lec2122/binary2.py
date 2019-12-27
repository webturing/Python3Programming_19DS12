def binary_print(n):
    for i in range(31, -1, -1):
        print((n >> i) & 1, end="")


n = -6
binary_print(n)
# print(bin(n))
