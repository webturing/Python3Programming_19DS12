D = [0]*10
# print(D)
D[0] = D[6] = D[9] = 1
D[8] = 2
# print(D)
while True:
    s = input().strip()
    if s == "":
        break
    n = int(s)
    if n == 0:
        print(1)
        continue
    s = 0
    while n > 0:
        s += D[n % 10]
        n = n//10
    print(s)
