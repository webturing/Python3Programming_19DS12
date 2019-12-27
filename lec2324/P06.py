def left(p, q):
    return p + 1 == q or (p == 4 and q == 0)


def right(p, q):
    return left(q, p)


def near(p, q):
    return left(p, q) or right(p, q)


zhao = 0
for qian in range(1, 5):
    for sun in range(1, 5):
        for li in range(1, 5):

            if qian == sun or qian == li or li == sun: continue
            # ，周回忆说：“吃饭时，赵坐在钱旁边，钱的左边是孙或李”；
            zhou = 10 - zhao - qian - sun - li
            if near(zhao, qian): continue
            if left(sun, qian) or left(li, qian): continue
            # 李回忆说：“钱坐在孙左边，我挨着孙坐”。结果他们一句也没有说对。请问，
            if left(qian, sun): continue
            if near(li, sun): continue
            print(zhao, qian, sun, li, zhou)
