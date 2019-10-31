n = 555555
flag = False
for c in range(999, 99, -1):
    if n % c == 0:
        print(c)
        flag = True
        break
if not flag:
    print("NOT FOUND")
