from Algorithms.StackAndQueue import QueueWithLinkedList as Q

def merge(S1,S2,S):
    """inside merge"""
    

def mergesort(S):
    """Mergesort"""
    n = len(S)
    if n < 2 :
        return

    m = n // 2
    count = 0
    S1 = Q.QueueWithLinkedList()
    S2 = Q.QueueWithLinkedList()

    while count < n:
        if count < m:
            S1.enQueue(S.deQueue())
        else:
            S2.enQueue(S.deQueue())
        count += 1

    S1.printQueue()
    S2.printQueue()
    mergesort(S1)
    mergesort(S2)
    merge(S1,S2,S)


S = Q.QueueWithLinkedList()
S.enQueue(1)
S.enQueue(7)
S.enQueue(12)
S.enQueue(5)
S.enQueue(4)
S.printQueue()

# Applying mergesort algorithm
mergesort(S)

# Sorted Linked List
#S.printQueue()

