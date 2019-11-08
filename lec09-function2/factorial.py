def factorial(n): #n!
    '''
    n!=2*3*4....*n
    n!=n*(n-1)!
    '''
    s=1
    for i in range(2,n+1):#[a,b+1) == [a,b] 
        s*=i
    return s


print(120==factorial(5))
print(2==factorial(2))
print(1==factorial(1))
print(1==factorial(0))


m=145
s=0
while m>0:
    s+=factorial(m%10)
    m//=10
print(s)

