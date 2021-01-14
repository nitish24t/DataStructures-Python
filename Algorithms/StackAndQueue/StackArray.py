class StackArray:
    def __init__(self,size):
        self.stack = []
        self.size = size

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        if self.size > len(self.stack):
            self.stack.insert(0, value)
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop(0)
        else:
            print("Pop() can't be performed on empty stack")

    def getLength(self):
        return len(self.stack)

    def printStack(self):
        for x in self.stack:
            print(x,end=" ")
        print()


def runQueue():
    print("Stack Array operations")
    sa = StackArray(5)
    sa.push(1)
    sa.push(2)
    sa.push(3)
    sa.push(4)
    sa.push(5)
    sa.printStack()
    print(str(sa.pop()))
    sa.printStack()
    sa.push(30)
    sa.printStack()
    sa.push(40)
    sa.push(50)


#runQueue()