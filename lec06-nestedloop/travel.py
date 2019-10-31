for n in range(100,1000):
    a,b,c=int(n/100),int(n%100/10),n%10
    if a**3+b**3+c**3==n:
        print(n)
