class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height * 0.5

triangle_area = Triangle(10,20)
print(triangle_area.area())
