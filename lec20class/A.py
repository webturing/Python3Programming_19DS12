class Pipe:
    def __init__(self, length, diameter, number):
        self.length = length
        self.diameter = diameter
        self.number = number

    def __lt__(self, other):
        if self.length != other.length:
            return self.length > other.length
        if self.diameter != other.diameter:
            return self.diameter < other.diameter
        if self.number != other.number:
            return self.number > other.number


for case in range(int(input())):
    pipes, size = [], int(input())
    for i in range(size):
        length, diameter, number = map(int, input().strip().split())
        pipes.append(Pipe(length, diameter, number))
    pipes = sorted(pipes)
    print(pipes[0].number)
