with open("3.txt") as inFile, open("5.txt", "w") as outFile:
    for line in inFile.readlines():
        outFile.write(line)
