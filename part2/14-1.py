class Square:
    square_list = []

    def __init__(self, s):
        self.s = s
        self.square_list.append(self.s)

s1 = Square(10)
s2 = Square(10)
s3 = Square(10)

print(Square.square_list)
