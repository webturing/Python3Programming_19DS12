words = "to know everything is to know nothing".split()
words.sort()
print(len(words))
D = {}
for word in words:
    if word in D:
        D[word] += 1
    else:
        D[word] = 1
print(D)
for w in D:
    print(w+":"+str(D[w]))
