# for n in range(10000000,99999999+1):
#    if str(n)==str(n)[::-1]:
#        print(n)
for n in range(1000, 9999 + 1):
    print(str(n) + str(n)[:-1][::-1])
