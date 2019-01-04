class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 50)
a_square = Square(25)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())
