# 14.	山乡希望小学收到一箱捐赠图书，邮件上署名是“兴华中学高二班”，山乡希望小学校   长送来了感谢信，
# 可是兴华中学高二年级有四个班，校长找来了四个班的班长，问他们是哪   个班做的这件好事。
# 一班的班长说：“是四班做的。
# ”二班的班长说：“是三班做的好事。”
# 三   班的班长说：“不是我们班。”   四班的班长说：“三班的班长说的不对。”
#  四个班的班长都说不是自己班做的，这就难坏了校长，后来得知四个班的班长中有两个   说得是真话，有两个没有说真话，请你利用计算机的逻辑判断编一个程序，
# 找出究竟是哪个   班做了这件好事。不能手算后直接打印结果。
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                if a + b + c + d != 1: continue
                pa = (d == 1)
                pb = (c == 1)
                pc = (c == 0)
                pd = not pc
                if pa + pb + pc + pd == 2:
                    print(a, b, c, d)