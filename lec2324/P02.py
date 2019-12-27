s = 0
for n in range(1, 1000000000 + 1):
    if n % 3 == 0 and n % 5 == 0:
        s += n
print(s)
