n=100
for x in range(n+1):
    for  y in range(n+1):
        z=n-x-y
        if 5*x+3*y+z/3==n:
            print('cock=%d,hen=%d,chicken=%d'%(x,y,z))
