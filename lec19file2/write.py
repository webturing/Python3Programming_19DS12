with open("1.txt", "w") as myFile:
    myFile.write('Hello world')
    myFile.write('\n')
    for i in range(10):
        myFile.write(str(i))

with open("1.txt", 'r') as myFile:
    print(myFile.read())
