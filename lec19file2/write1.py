with open("1.txt", "w") as myFile:
    myFile.write("hello world\n")
    for i in range(10):
        myFile.write(str(i))
    myFile.write('\n')
