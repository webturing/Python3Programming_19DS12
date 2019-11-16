def disp2d(a):
    for e in a:
        for t in e:
            print(t,end=" ")
        print("")
    #print("--------------------")
n=10

a=[[0]*n for p in range(n)] #deep copy 
#a=[[0]*n]*n                #shallow copy
for i in range(n):
    for j in range(n):
        a[i][j]=10*i+j
disp2d(a)
#长度17 开始于7 公差是7
