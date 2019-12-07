with open("2.txt", "a") as myFile:
    myFile.write('Hello world')
    myFile.write('\n')
    for i in range(10):
        myFile.write(str(i))

with open("2.txt", 'r') as myFile:
    print(myFile.read())
