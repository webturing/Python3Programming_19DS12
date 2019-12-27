s = 0
left, right = 1, 100000000000000000
left = (left + 14) // 15 * 15
right = right // 15 * 15
print(left, right)
n = (right - left) // 15 + 1
print((left + right) * n // 2)
