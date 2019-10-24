while True:
    a = int(input())
    if a < 0 or a > 100:
        print('Score is error!')
    elif a < 60:
        print('E')
    elif a < 70:
        print('D')
    elif a < 80:
        print('C')
    elif a < 90:
        print('B')
    else:
        print('A')
