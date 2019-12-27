n = 1288989889889
n = str(n)
while len(n) % 3 != 0:
    n = '0' + n
print(n)
m = len(n)
head = n[0:m // 3]
mid = n[m // 3:m // 3 * 2]
tail = n[m // 3 * 2:]
print(head, mid, tail)
head, mid, tail = map(int, [head, mid, tail])
print(head + tail - mid)
# n=>001234567
# 001 234 567
