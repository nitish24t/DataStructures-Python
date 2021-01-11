class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        elif self.head.next == None:
            print("popped "+str(self.head.data))
            del self.head
            self.head = None
        else:
            element = self.head.data
            newhead = self.head.next
            del self.head
            self.head = newhead
            print("popped "+str(element))

    def isEmpty(self):
        return self.head == None

    def printStack(self):
        current = self.head
        if current == None:
            print("Stack is empty")
            return
        while current != None:
            print(str(current.data), end=" ")
            current = current.next
        print()


def stackOperations():
    st = LinkedListStack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.printStack()
    st.pop()
    st.printStack()
    st.pop()
    st.printStack()
    st.pop()
    st.printStack()
    st.pop()

#stackOperations()