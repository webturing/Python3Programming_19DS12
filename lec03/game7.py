for i in range(1,101):
   
    if i%7==0:continue
    if i%10==7:continue
    if i//10==7:continue
    if i%10!=0:
        print('%3d'%i,end=' ')
    else:
        print('%3d'%i)
   
