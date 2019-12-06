with open("2.txt") as myFile:
    s = myFile.readline().strip()
    a, b = s.split()
    a = int(a)
    b = int(b)
    print(a + b)
