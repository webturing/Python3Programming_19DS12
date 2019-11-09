def Print2(n):
    if n < 10:
        print(n, end=" ")
    else:
        Print2(int(n / 10))
        print(n % 10, end=" ")


Print2(1234)
