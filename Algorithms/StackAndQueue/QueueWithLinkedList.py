"""Queue Methods
-isEmpty()
-enqueue (add element)
-dequeue (remove element)
-printQueue()
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueWithLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == self.tail == None

    def enQueue(self,data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = self.tail = newnode
        else:
            current_tail = self.tail
            self.tail = newnode
            current_tail.next = self.tail

    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty!!")
        else:
            current_head = self.head
            if current_head.next:
                self.head = self.head.next
                print(f"{current_head.data} popped")
                del current_head
            else:
                print(f"{current_head.data} popped")
                del self.head
                self.head = self.tail = None

    def printQueue(self):
        current = self.head
        while(current):
            print(f"{current.data}", end=" ")
            current = current.next
        print()

def QueueOperations():
    Q = QueueWithLinkedList()
    Q.enQueue(1)
    Q.enQueue(2)
    Q.enQueue(3)
    Q.printQueue()
    Q.deQueue()
    Q.deQueue()
    Q.deQueue()
    Q.deQueue()

QueueOperations()