"""
-add node at start
-add node in end
-delete node from start
-delete node from end
-find and delete node

-first
-last
-isEmpty
-size

-sort the linked list
-insert node in sorted linked list
"""

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def size(self):
        return self.size

    def insertAtEnd(self, data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.size += 1

    def insertAtStart(self, data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        else:
            curr_head = self.head
            self.head = newnode
            newnode.next = curr_head
        self.size += 1

    def deleteEndNode(self):
        if self.isEmpty():
            return
        if self.head.next is None:
            del self.head
            self.head = self.tail = None
            self.size = 0
            return
        curr_head = self.head
        while curr_head.next != self.tail:
            curr_head = curr_head.next
        curr_head.next = None
        del self.tail
        self.tail = curr_head
        self.size -= 1


    def deleteStartNode(self):
        if not self.isEmpty():
            curr_head = self.head
            self.head = self.head.next
            del curr_head
            self.size -= 1
        if self.isEmpty():
            self.head = self.tail = None


    def printLinkedList(self):
        start = self.head
        while start:
            print(str(start.data), end=' ')
            start = start.next
        print()



def StackOperations():
    s = SinglyLinkedList()
    s.insertAtEnd(1)
    s.insertAtEnd(2)
    s.insertAtEnd(4)
    s.printLinkedList()
    s.deleteEndNode()
    s.deleteEndNode()
    s.insertAtStart(12)
    s.insertAtStart(15)
    s.printLinkedList()
    s.deleteEndNode()
    s.deleteEndNode()
    s.printLinkedList()


StackOperations()