with open("3.txt") as inFile, open("4.txt", "w") as outFile:  # 1
    content = inFile.read()  # 2
    outFile.write(content)  # 3
