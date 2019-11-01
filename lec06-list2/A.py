A = list(map(int, input().strip().split()))
a = A[0]
b = A[1]
c = A[2]

s = 0
for i in range(a, b + 1):
    if c % i == 0:
        s += 1

print(s)
