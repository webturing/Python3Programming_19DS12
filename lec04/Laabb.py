import math
for n in range(1000,10000):
    a=n//100
    b=n%100
    if a%11!=0 or b%11!=0:continue
    sq=int(math.sqrt(n))
    if sq*sq!=n:continue
    print(n)


