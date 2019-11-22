def disp2d(a):
    for e in a:
        for t in e:
            print(t, end=" ")
        print("")


A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

B = [[0]*2 for p in range(3)]  # deep copy/clone
# B=[[0]*2]*3 #shallow copy

for i in range(3):  # row
    for j in range(2):  # col
        B[i][j] = A[j][i]

disp2d(A)
disp2d(B)
