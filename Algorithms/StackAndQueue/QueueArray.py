class QueueArray:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("Dequeue can't be performed on empty queue")

    def getLength(self):
        return len(self.queue)

    def printQueue(self):
        for x in self.queue:
            print(x ,end=" ")
        print()


def runQueue():
    print("Queue Array operations")
    qa = QueueArray()
    qa.enqueue(1)
    qa.enqueue(2)
    qa.enqueue(3)
    qa.enqueue(4)
    qa.enqueue(5)
    qa.printQueue()
    print(str(qa.dequeue()))
    qa.printQueue()

#runQueue()