a = list(map(int, input().strip().split()))
k = int(input())
left, right, flag = 0, len(a) - 1, False
while left <= right:
    mid = (left + right) // 2
    if k == a[mid]:
        print(mid)
        flag = True
        break
    elif k < a[mid]:
        right = mid - 1
    else:
        left = mid + 1
if not flag:
    print('Not exist!')
