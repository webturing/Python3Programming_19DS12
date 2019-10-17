s=0
for i in range(1,100):
    s=s+i**3
    print(i,end='^3+')
    if s>=1000:break

print(s)
        
