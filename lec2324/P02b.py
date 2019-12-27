s = 0
left, right = 1, 1000000000000
while left % 15 != 0: left += 1
while right % 15 != 0: right -= 1
print(left, right)
n = (right - left) // 15 + 1
print((left + right) * n // 2)
