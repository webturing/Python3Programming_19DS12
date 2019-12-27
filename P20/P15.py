'''
15.	A，B，C，D，E五个人合伙夜间捕鱼，凌晨时都疲惫不堪，各自在河边的树丛中找地   方睡着了，日上三竿，E第一个醒来，他将鱼数了数，平分成五分，把多余的一条扔进河中，   拿走一份回家去了，
D第二个醒来，他并不知道有人已经走了,照样将鱼平分成五分，又扔掉多余的一条，拿走自己的一份，接着C，B，A依次醒来，
也都按同样的办法分鱼(平分成   五份，扔掉多余的一条，拿走自己的一份)，问五人至少合伙捕到多少条鱼。     也许你能用数学办法推出鱼的条数，但我们的要求你编出一个程序，让计算机帮你算出鱼的总数。
'''
for n in range(6, 100000000):
    m = n  # 因为n要做为循环变量不能程序中修改
    if m % 5 != 1: continue
    m -= m // 5 + 1  # a分鱼
    if m % 5 != 1: continue
    m -= m // 5 + 1  # b分鱼
    if m % 5 != 1: continue
    m -= m // 5 + 1  # c分鱼
    if m % 5 != 1: continue
    m -= m // 5 + 1  # d分鱼
    if m % 5 != 1: continue
    m -= m // 5 + 1  # e分鱼
    print(n)
    break

# 以下验证
m = n  # 因为n要做为循环变量不能程序中修改
m -= m // 5 + 1  # a分鱼
print(m // 5, m)
m -= m // 5 + 1  # b分鱼
print(m // 5, m)
m -= m // 5 + 1  # c分鱼
print(m // 5, m)
m -= m // 5 + 1  # d分鱼
print(m // 5, m)
m -= m // 5 + 1  # e分鱼
print(m // 5, m)