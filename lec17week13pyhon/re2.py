import re

s = input()
s = re.sub(r'[^a-zA-Z]', "", s)
print(len(s))
