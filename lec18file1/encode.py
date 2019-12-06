K = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
offset = 3
with open("message.txt") as myFile:
    text = myFile.readline()
    for char in text:
        if char not in K:
            print(char, end="")
            continue
        pos = K.index(char)
        print(K[(pos + offset) % 26], end="")
