class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None  # pointer to the next node


# Class for managing the list and nodes
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
        else:  # if not empty iterate through items and append new node at the end (tail)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  # always update the size to prevent costly iterations to get the size

    # defining iteration function to make iterating over nodes in the list possible
    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    def clear(self): #1
        current = self.head
        while current:
            prev = current.next  # move next node
            del current.data
            current = prev



    def get_data(self, data): #2
         current = self.head
         while current != None:
             if current.data == data:
                 return data
             current = current.next
         return False


    def delete(self, data):  #3
        current = self.head
        if (current != None):
            if (current.data == data):
                self.head = current.next
                current = None
                self.size -= 1

        while (current != None):
            if current.data == data:
                break
            prev = current
            current = current.next

        if (current == None):
            return
        prev.next = current.next
        current = None
        self.size -= 1

    def printList(self):
           current = self.head
           while(current):
              print (" %d" %(current.data))
              current = current.next




L = SinglyLinkedList()
L.append(1)
L.append(2)
L.append(3)
L.append(7)
print ("Created Linked List: ")
L.printList()

L.delete(2)

L.printList()
print(L.get_data(3))
print(L.get_data(2))
L.clear()
print(L)

print(L.get_size())

class NodeDLL:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next  # pointer to the next node
        self.prev = prev

# Class for managing the list and nodes
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = NodeDLL(data, None, None)
        if self.head == None:  # if the node is empty, the new node is the head
            self.head = node
            self.tail = self.head
        else:  # if not empty iterate through items and append new node at the end (tail)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def get_size(self):
        return self.size

    def clear(self):
        current = self.head
        while current:
            prev = current.next  # move next node
            del current.data
            del current.next
            current = prev
            self.size -=1
        self.head = None
    def get_data(self, data):
         current = self.head
         while current != None:
             if current.data == data:
                 return data
             current = current.next
         return False


    def delete(self, data):
        current = self.head
        node_deleted = False
        if self.head == None or data == None: #check if List is empty, or data to delete is Na
            return

        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.size -= 1



    def printList(self):
           current = self.head
           while(current):
              print (" %d" %(current.data)),
              current = current.next




O = DoublyLinkedList()
O.append(1)
O.append(2)
O.append(3)
O.append(7)
print ("Created Linked List: ")
O.printList()

O.delete(1)

print ("\nLinked List after Deletion of 1:")
O.printList()

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
q = MyQueue()

q.push(2)
q.push(3)
q.push(5)
q.push(8)
print(q.show_left())
print(q.show_right())


print(q.size())

print(q.pop())
print(q)
