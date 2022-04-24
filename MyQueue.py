class MyQueue:

    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = []
        self.front = 0
        self.rear = -1
    def __str__ (self):
        values = [str(x) for x in self.stack]
        return "".join(values)

    def show_left(self):
        return self.stack[self.front]

    def show_right(self):
        return self.stack[self.rear]

    def push(self, x: int) -> None:
        self.x = x
        self.stack.append(x)

    def pop(self):
        return self.stack.pop(0)

    def size(self):
        return len(self.stack)
k = MyQueue()

k.push(2)
k.push(3)
k.push(5)
k.push(8)
print(k.show_left())
print(k.show_right())


print(k.size())

print(k.pop())
print(k)