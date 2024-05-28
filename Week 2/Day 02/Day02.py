class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)  # Output: Point(6, 8)

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'w') as file:
    file.write('Hello, World!')
