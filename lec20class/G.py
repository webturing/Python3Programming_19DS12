class Person:  # PERSON
    def __init__(self, _name, _y, _m, _d):
        self.name = _name
        self.y = _y
        self.m = _m
        self.d = _d

    def __repr__(self):
        return '%s %04d-%02d-%02d' % (self.name, self.y, self.m, self.d)

    def __lt__(self, other):
        if self.y != other.y: return self.y < other.y
        if self.m != other.m: return self.m < other.m
        if self.d != other.d: return self.d < other.d
        return self.name < other.name


n = int(input())
persons = []
for i in range(n):
    name, y, m, d = input().strip().split()
    y = int(y)
    m = int(m)
    d = int(d)
    persons.append(Person(name, y, m, d))
persons.sort()  # <
# print(persons)#debug
for person in persons:
    print(person.name)
