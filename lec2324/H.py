while True:
    s = 0
    dif = 0
    for char in input():
        if char == '(':
            dif += 1
            s = max(s, dif)
        elif char == ')':
            dif -= 1
    print(s)
