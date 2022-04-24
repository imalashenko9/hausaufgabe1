

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
        node = Node(data, None, None)
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




L = DoublyLinkedList()
L.append(1)
L.append(2)
L.append(3)
L.append(7)
print ("Created Linked List: ")
L.printList()

L.delete(1)

print ("\nLinked List after Deletion of 1:")
L.printList()


