class Leader:
    def __init__(self, _name):
        self.name = _name
        self.count = 0

    def add(self):
        self.count += 1

    def __str__(self):
        return '%s:%d' % (self.name, self.count)


leaders = [Leader('Li'), Leader('Zhang'), Leader('Fun')]
for case in range(int(input())):
    name = input().strip()
    for leader in leaders:
        if leader.name == name:
            leader.add()

for leader in leaders:
    print(leader)
