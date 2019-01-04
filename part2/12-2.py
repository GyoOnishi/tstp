import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

circle_area = Circle(10)
print(circle_area.area())
