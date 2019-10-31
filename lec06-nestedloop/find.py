n=7744
flag=False
for x in range(1,n+1):
    if x*x==n:
        flag=True
        break
if not flag:
    print("not a square number")
else:
    print("it is a square number")
