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

list1 = [1,2,3,4,5]
stack = Stack()
for i in list1:
    stack.push(i)
reverse_list = []
while stack.size():
    reverse_list.append(stack.pop())
print(list1)
print(reverse_list)
