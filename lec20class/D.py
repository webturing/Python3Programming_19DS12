class Student:
    def __init__(self, _number, _name, _x, _y, _z):
        self.number, self.name, self.x, self.y, self.z = _number, _name, _x, _y, _z

    def __lt__(self, other):
        if self.x + self.y + self.z != other.x + other.y + other.y:
            return self.x + self.y + self.z > other.x + other.y + other.z
        return x > other.x

    def __repr__(self):
        return '%s %s %d %d %d' % (self.number, self.name, self.x, self.y, self.z)


students = []
total = {"x": 0, "y": 0, "z": 0}
for i in range(10):
    number, name, x, y, z = input().strip().split()
    x, y, z = int(x), int(y), int(z)
    total['x'] += x
    total['y'] += y
    total['z'] += z
    # print(number, name, x, y, z)
    students.append(Student(number, name, x, y, z))
students.sort()
print("%.2f %.2f %.2f" % (total['x'] / 10, total['y'] / 10, total['z'] / 10))
print(students[0])
