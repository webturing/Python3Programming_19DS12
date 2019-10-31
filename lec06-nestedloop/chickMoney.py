n=1000
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            if x+y+z==n and 5*x+3*y+z/2==n:
                print(x,y,z)
