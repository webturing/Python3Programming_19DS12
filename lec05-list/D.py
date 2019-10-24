m = 10 # input()
s = 0

s += 1
for i in range(2,m+1):
    s -= 1 / i**2
    
print(s)
