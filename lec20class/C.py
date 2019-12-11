class Student:
    def __init__(self, _number, _name, _x, _y, _z):
        self.number, self.name, self.x, self.y, self.z = _number, _name, _x, _y, _z

    def __str__(self):
        return '%s %s %d %d %d' % (self.number, self.name, self.x, self.y, self.z)


for i in range(10):
    number, name, x, y, z = input().strip().split()
    x, y, z = int(x), int(y), int(z)
    print(Student(number, name, x, y, z))
