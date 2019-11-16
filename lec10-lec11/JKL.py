H,W=5,6

for i in range(H):
    for j in range(W):
        #print('(%d,%d)'%(i,j),end="")
        if (i+j)%2==0:
            print('#',end='')
        else:
            print('.',end='')
    print("")
