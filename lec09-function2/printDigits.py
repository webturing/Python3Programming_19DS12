def Print(n):
    if n<10:
        print(n,end="")
    else:
        print(n%10,end="")
        Print(int(n/10))


Print(1234)

