n=int(input().strip())
for i in range(n):
    head,leg=map(int,input().strip().split())
    flag=False
    for chick in range(head+1):
        hair=n-chick
        if chick+hair==head and chick*2+hair*4==leg:
            print(chick,hair)
            flag=True
            break
    if not flag:
        print("No answer")
