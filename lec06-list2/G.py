while True:
    a, b, c = map(int, input().strip().split())
    flag = False
    for i in range(10, 101):
        if i % 3 == a and i % 5 == b and i % 7 == c:
            print(i)
            flag = True
            break
    if not flag:
        print('No answer')
