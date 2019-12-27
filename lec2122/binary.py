def binary_print(n):
    B=[]
    while n > 0:
        #print(n % 2,end=" ")
        B.append(n&1)
        n //= 2
    print(B[::-1])

n = 6
binary_print(n)
#print(bin(n))
