for c in range(32,100):
    n=c*c
    high,low=n//100,n%100
    if high%11==0 and low%11==0:
        print(n)
