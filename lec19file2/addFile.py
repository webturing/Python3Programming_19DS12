with open("input.txt") as inFile, open("output.txt", "w") as outFile:  # 1
    for line in inFile.readlines():  # 2
        a, b = map(int, line.strip().split())  # 3
        outFile.write('%d\n' % (a + b))
