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
        self.size = 0

class QueueWithLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def getFirst(self):
        if self.size > 0:
            return self.head.data

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
        self.size += 1

    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty!!")
        else:
            current_head = self.head
            if current_head.next:
                self.head = self.head.next
                #print(f"{current_head.data} popped")
                value = current_head.data
                del current_head
            else:
                #print(f"{current_head.data} popped")
                value = self.head.data
                del self.head
                self.head = self.tail = None
            self.size -= 1
            return value

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
    print("Size of queue : "+str(len(Q)))
    Q.deQueue()
    Q.deQueue()
    Q.deQueue()
    Q.deQueue()


#QueueOperations()