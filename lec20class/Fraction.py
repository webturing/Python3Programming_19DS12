import math


class Fraction:
    def __init__(self, up=0, down=1):
        g = math.gcd(up, down)
        up, down = up // g, down // g
        self.up, self.down = up, down

    def __str__(self): return '%d/%d' % (self.up, self.down)

    def __add__(self, other):
        up, down = self.up * other.down + self.down * other.up, self.down * other.down
        return Fraction(up, down)


print(Fraction())
print(Fraction(2))
print(Fraction(3, 6))
print(Fraction(1, 3) + Fraction(1, 6))
s = Fraction()
for i in range(1, 11):
    s += Fraction(1, i)
print(s)
