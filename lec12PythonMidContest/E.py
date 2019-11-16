while True:
    x0,y0,r=map(int,input().strip().split())
    tot=0
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            if x*x+y*y==r*r:
                tot+=1
    print(tot)
    
