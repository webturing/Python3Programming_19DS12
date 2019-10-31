for n in range(1100,9999+1):
    a=int(n/1000)
    b=int(n%1000/100)
    c=int(n%100/10)
    d=n%10
    if a!=b or c!=d:continue
    flag=False
    for x in range(32,100):
        if x*x==n:
            flag=True
            break
    if flag==False:continue
    print(n)
