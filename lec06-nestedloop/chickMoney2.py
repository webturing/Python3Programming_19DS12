n=1000
for x in range(n//5+1):
    for y in range(n//3+1):
        z=n-x-y
        if 5*x+3*y+z/2==n:
            print(x,y,z)
