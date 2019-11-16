def Reverse(n):
    m=0
    while n>0:
        d=n%10
        m=m*10+d
        n//=10
    return m


print(4321==Reverse(1234))#expectedValue==actualValue
print(321==Reverse(123))#Unit Testing
print(1==Reverse(1))
print(21==Reverse(12))


for n in range(100,1000):
    if n==Reverse(n):
        print(n)
