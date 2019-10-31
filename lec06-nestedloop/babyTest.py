T = int(input().strip())
for cas in range(T):
    n=int(input().strip())
    s=0
    for i in range(1,n+1):
        s+=i*(i+1)//2
    print(s)
