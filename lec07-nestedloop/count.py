cnt = 0
for n in range(1, 100):
    if n % 7 == 0 or n % 10 == 7 or n // 10 == 7:
        cnt += 1
print(cnt)
