a = list(range(10))
k = 877
for i in range(len(a)):
    print(a[(k+i) % len(a)], end=" ")
