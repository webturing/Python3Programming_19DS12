with open("2.txt", "r") as inFile, open("3.txt", "w") as outFile:
    for line in inFile.readlines():
        outFile.write(line)
