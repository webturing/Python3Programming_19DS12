for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                for e in range(0, 2):
                    if a + b + c + d + e != 3: continue
                    if a + c == 2: continue
                    if b + c == 0: continue
                    if c == 1 and (d + e) != 1: continue
                    if b + c + d == 3: continue
                    if b == 1 and (d + e == 2): continue
                    print(a, b, c, d, e)
