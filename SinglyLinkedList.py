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

print ("\nLinked List after Deletion of 2:")
L.printList()

print(L.get_data(3))

print(L.get_data(2))

L.clear()
print(L)

print(L.get_size())
