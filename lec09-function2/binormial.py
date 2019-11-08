def factorial(n): #n!
    '''
    n!=2*3*4....*n
    n!=n*(n-1)!
    '''
    s=1
    for i in range(2,n+1):#[a,b+1) == [a,b] 
        s*=i
    return s

def binormial(n,r):
    return int(factorial(n)/factorial(r)/factorial(n-r))



for i in range(5):#C(4,i)
    print(binormial(4,i))
