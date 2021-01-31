from Algorithms.StackAndQueue import QueueWithLinkedList as Q

def quickSort(S):
    n = len(S)
    if n < 2:
        return
    pivot = S.getFirst()
    L = Q.QueueWithLinkedList()
    E = Q.QueueWithLinkedList()
    G = Q.QueueWithLinkedList()
    while not S.isEmpty():
        if S.getFirst() < pivot:
            L.enQueue(S.deQueue())
        elif S.getFirst() == pivot:
            E.enQueue(S.deQueue())
        elif S.getFirst() > pivot:
            G.enQueue(S.deQueue())
    quickSort(L)
    quickSort(G)
    while not L.isEmpty():
        S.enQueue(L.deQueue())
    while not E.isEmpty():
        S.enQueue(E.deQueue())
    while not G.isEmpty():
        S.enQueue(G.deQueue())



S = Q.QueueWithLinkedList()
S.enQueue(1)
S.enQueue(7)
S.enQueue(12)
S.enQueue(5)
S.enQueue(4)
S.printQueue()

# Applying mergesort algorithm
quickSort(S)

# Sorted Linked List
S.printQueue()