class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def dequeue(self):
        node = self.head
        if self.head == None:
            print("Queue is empty")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        print("Removed "+str(node.data))

    def printQueue(self):
        start = self.head
        while start:
            print(str(start.data),end=" ")
            start = start.next
        print()


def queueOperations():
    q = LinkedListQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.printQueue()
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.dequeue()
    q.enqueue(9)
    q.printQueue()

queueOperations()