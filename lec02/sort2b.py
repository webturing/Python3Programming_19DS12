s = input("Please input two integers").strip()
#print(s)
a,b = s.split()
a,b = int(a),int(b)
if a > b:
    a,b=b,a
print("a=",a,"b=",b)
