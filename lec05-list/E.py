n = 4

a = [0] * n
a[-1] = 1  # base
#a[-2] = (a[-1] + 1) * 2
for i in range(n-2,-1,-1): # iteration
    a[i]=2*(a[i+1]+1)
    
print(a)
