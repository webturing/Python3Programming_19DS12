import sys

L = []
try:
    with open("input2.txt") as inFile:
        L = inFile.readlines()
except:
    L = sys.stdin.readlines()

for line in L:
    a, b = map(int, line.strip().split())
    print('%d' % (a + b))
