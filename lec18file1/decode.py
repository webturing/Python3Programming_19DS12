K = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


with open("code.txt") as myFile:
    text = myFile.readline()
    for offset in range(1, 26):
      
        for char in text:
            if char not in K:
                print(char, end="")
                continue
            pos = K.index(char)
            print(K[(pos + offset) % 26], end="")
        print('...........offset=', offset)
