s = "20 40 32 67 40 20 89 300 400 15"
s = list(map(int, s.split()))
s.sort()
S = set()
for e in s:
    S.add(e)
print(S)
