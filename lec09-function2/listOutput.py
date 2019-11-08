n=12345

a=[]

while n>0:
    a.append(n%10)
    n=int(n/10)
print(a)# [5,4,3,2,1]


a.reverse()
for i in a:
    print(i,end=" ")
print("")
for i in range(len(a)):
    print(a[i],end=" ")
print("")
for i in range(-1,-len(a)-1,-1):
    print(a[i],end=" ")
print("")
