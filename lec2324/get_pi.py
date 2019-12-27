import random
import math

N = 1000000
M = 0

for i in range(N):
    x = random.random()# [0,1)之间均匀分布的随机小数
    y = random.random()
    if math.sqrt(x*x+y*y)<=1:
        M += 1
print(4 * M / N)
