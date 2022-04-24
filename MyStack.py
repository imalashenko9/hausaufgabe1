class MyStack:

    def __init__(self):

        self.stack = []

    def top(self) -> int:
        return self.stack[-1]

    def push(self, x: int) -> None:
        self.x = x
        self.stack.append(x)

    def pop(self):
        self.stack.pop()

    def size(self):
        return len(self.stack)
k = MyStack()

k.push(2)
k.push(3)
k.push(5)
k.push(8)


print(k.size())
print(k.top())
print(k.pop())







