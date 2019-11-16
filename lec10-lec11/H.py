
def is_prime(n):
    if n<2:return False 
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def get_reverse(n):
    m=0
    while n>0:
        m=m*10+(n%10)
        n//=10
    return m

def is_sysmetric(n):
    return n==get_reverse(n)


a,b=map(int,input().strip().split())
for n in range(a,b+1):
    if is_sysmetric(n) and is_prime(n):
        print(n)
