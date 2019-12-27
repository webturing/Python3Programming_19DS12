for a in range(1, 4):
    for b in range(1, 4):
        if a == b: continue
        c = 6 - a - b
        #print(a, b, c)
        ap = (b == c and c == 2)
        aq = (a == 1)
        bp = (b <= 2)
        bq = (c == 3)
        cp = (a != 2)
        cq = (b != 1)
        if a + ap + aq == b + bp + bq == c + cp + cq == 3:
            print(a, b, c)
