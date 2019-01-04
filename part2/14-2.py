class Square:
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.s,self.s,self.s,self.s)

s1 = Square(29)
print(s1)
