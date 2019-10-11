s = input("Please input two integers").strip()
#print(s)
a,b = s.split()
a = int(a)
b = int(b)

print(min(a,b),max(a,b))
