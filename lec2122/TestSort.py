import random
a=[]
for i in range(20):
    x,y,z=random.randint(1,10),random.randint(1,10),i
    a.append((x,y,z))
print(sorted(a))
print(sorted(a,key=lambda  t:(t[0],t[2])))