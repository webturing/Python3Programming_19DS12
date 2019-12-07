fileName = input('Input a code file to number:')
number = 1
with open(fileName, 'r') as inFile:
    for line in inFile.readlines():
        code = line.rstrip()
        while len(code) < 60:
            code = code + " "
        print(code + " #%02d" % (number))
        number += 1
