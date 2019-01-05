class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
item = stack.pop()
print(item)
print(stack.is_empty())

"""
for i in range(0, 6):
    stack.push(i)
print(stack.items)
print(stack.peek())
print(stack.size())
"""

for c in 'Hello':
    stack.push(c)
reverse = ''
while stack.size():
    reverse += stack.pop()
print(reverse)
