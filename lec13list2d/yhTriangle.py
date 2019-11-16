def disp2d(a):
    for e in a:
        for t in e:
            print(t,end=" ")
        print("")
    #print("--------------------")
n=5
a=[]
for i in range(1,n+1,1):
    a.append([1]*i)
    
for i in range(2,n):
    for j in range(1,i):
        a[i][j]=a[i-1][j-1]+a[i-1][j]
disp2d(a)
       
