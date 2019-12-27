# 9.     输入一个字符串，内有数字和非数字字符。如A123X456Y7A，302ATB567BC，
# 打印字符串中所有连续（指不含非数字字符）的数字所组成的整数，并统计共有多少个整数。
import re

s = "A123X456Y7A，302ATB567BC"
for word in re.split('\\D+', s):
    if word.strip():
        print(word,end=" ")

