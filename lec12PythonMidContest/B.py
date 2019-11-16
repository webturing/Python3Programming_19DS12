import math
a,b,c = sorted(map(int, input().strip().split()))
if a+b<=c:
    print("Input error!")
else:
    s=(a+b+c)/2
    a=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("%.2f\n"%a)

