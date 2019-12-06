with open("3.txt") as myFile:
    # print(myFile.readlines())
    for line in myFile.readlines():
        a, b = map(int, line.strip().split())
        print(a + b)
