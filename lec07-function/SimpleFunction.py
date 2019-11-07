def get_max(a, b):
    if a > b:
        return a
    else:
        return b


def get_sign(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0


print(get_max(3, 4))

print(get_sign(4) == 1)  # 1
print(get_sign(-4) == -1)  # -1
print(get_sign(0) == 0)  # 0
